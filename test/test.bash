#!/bin/bash
# SPDX-FileCopyrightText: 2024 Junsei Iimori <craftboy0228@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
log_file="/tmp/landmark_test.log"
timeout 10 ros2 launch mypkg talk_listen.launch.py > "$log_file" &

sleep 10

previous_time=0
landmark_list=("エッフェル塔: 緯度 48.8583, 経度 2.2944" \ 
               "自由の女神: 緯度 40.6892, 経度 -74.0445" \ 
               "東京タワー: 緯度 35.6586, 経度 139.7454" \ 
               "シドニー・オペラハウス: 緯度 -33.8568, 経度 151.2153" \                
               "ギザのピラミッド: 緯度 29.5845, 経度 31.0803")
landmark_counter=0
interval_check=true
order_check=true

while read -r line; do
    if [[ "$line" =~ "Publishing: " ]]; then
        message=$(echo "$line" | sed 's/.*Publishing: "\(.*\)"/\1/')

        if [ "$message" == "${landmark_list[$landmark_counter]}" ]; then
            landmark_counter=$(( (landmrak_counter + 1) % ${#landmark_list[@]} ))
        else
            order_check=false
            break
        fi

        timestamp=$(echo "$line" | grep -op '\[\d+\.\d+\]' | tr -d '[]')
        timestamp_int=${timestamp%.*}

        if [ $previous_time -eq 0]; then
            previous_time=$timestamp_int
            continue
        fi

        interval=$((timestamp_int - previous_time))
        if [ $interval -ne 2 ]; then
            interval_check=false
            break
        fi

        previous_time=$timestamp_int
    fi
done < /tmp/landmark_test.log

if [ "$order_check" = true ] && [ "$interval_check" = true ]; then
    echo "success"
else
    if [ "$order_check" = false ]; then
        echo "number false"
    fi
    if [ "$interval_check" = false ]; then
        echo "sending interval false"
    fi
fi
