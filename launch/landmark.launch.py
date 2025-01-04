# SPDX-FileCopyrightText: 2024 Junsei Iimori <craftboy0228@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    landmark = launch_ros.actions.Node(
        package='mypkg',
        executable='landmark',
        output='screen',
        parameters=[{'use_sim_time': False}]
    )

    return launch.LaunchDescription([landmark])
