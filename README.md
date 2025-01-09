# landmark

## mypkg  
千葉工業大学 未来ロボティクス学科2024年度ロボットシステム学の講義で使用したROS2のパッケージに課題2で作成したファイルを追加したものです。

[![test](https://github.com/junsei0/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/junsei0/mypkg/actions/workflows/test.yml)

## テスト環境
- Ubuntu 20.04.6 LTS
- ROS2 Humble 

## 開発環境
- ubuntu20.04 LTS
- ROS2 Foxy

## ノード
- landmark
  - 特定の名所の緯度経度を3秒おきにトピックにパブリッシュします。

## トピック
- landmark_topic
  - ノードからパブリッシュされた名所の名前、緯度経度をを持ちます。

## 使用方法
以下のコマンドで実行します。  
```
$ ros2 run mypkg landmark
```
実行しても端末上では何も表示されません。
トピックの内容を確認するには以下のコマンドで確認できます。
```
$ ros2 topic echo /landmark_topic
```

```
data: '東京タワー: 緯度 35.6586, 経度 139.7454'
---
data: 'シドニー・オペラハウス: 緯度 -33.8568, 経度 151.2153'
---
data: 'ギザのピラミッド: 緯度 29.5845, 経度 31.0803'
---
data: 'モン・サン=ミシェル: 緯度 48.381, 経度 -1.511111'
---
data: 'カッパドキア: 緯度 38.6705, 経度 34.8391'
---
data: 'エッフェル塔: 緯度 48.8583, 経度 2.2944'
---
data: '自由の女神: 緯度 40.6892, 経度 -74.0445'
---
```

## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/junsei0/mypkg/blob/main/LICENSE)を確認してください。
- © 2025 Junsei Iimori 
