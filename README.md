# landmark

## mypkg  
千葉工業大学 未来ロボティクス学科2024年度ロボットシステム学の講義で使用したROS2のパッケージに課題2で作成したファイルを追加したものです。

## テスト結果
[![test](https://github.com/junsei0/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/junsei0/mypkg/actions/workflows/test.yml)

## テスト済みの環境
- Ubuntu 20.04.6 LTS
- ROS2 Humble Hawksbil

## トピック内容
本パッケージでは、特定の名所の緯度経度を3秒おきにstd_msgs.msg.String 型のメッセージを送るトピックを扱います。

## 使用方法
使用する場合は、gitコマンドを使用してリポジトリをクローンしてください。
```
$ git clone https://github.com/junsei0/mypkg.git
```
- landmark.py
3秒おきに特定の名所の緯度経度をトピック/landmark_topicを通じて送信するノードです。
以下のコマンドで実行します。  
```
$ ros2 mypkg landmark
```
実行してもその端末上では何も表示されません。

トピック/landmark_topicを受信して、特定の名所の緯度経度の内容を端末に表示するには以下のコマンドを別の端末で実行します。
```
$ ros2 topic echo /landmark_topic
```
## 著作権・ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下で公開されています。
- 詳細は[LICENSE](https://github.com/junsei0/mypkg/blob/main/LICENSE)を確認してください。
- ©︎ 2024 Junsei Iimorii
