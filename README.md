# Build My Own Redis by Python

* [codecrafters-io/build-your-own-x: Master programming by recreating your favorite technologies from scratch.](https://github.com/codecrafters-io/build-your-own-x#build-your-own-database)
* [charles leifer | Write your own miniature Redis with Python](https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)

## Redis Container by docker (compose)

* [docker-composeでredis環境をつくる - Qiita](https://qiita.com/uggds/items/5e4f8fee180d77c06ee1)

## Redis cli

* [redis-cliでよく使うコマンド20選 - Qiita](https://qiita.com/hatsu/items/a52817364160e0b6bb60)

## gevent

* [Gevent チュートリアル](https://methane.github.io/gevent-tutorial-ja/)

### gevent StreamServer

gevent は初めてだったので少し調べてみた。
簡単にまとめると「シンプルなsocket server」らしい。

私の (python) socket プログラミング遍歴で言えば、fastapi の WebSocket をちょっと使ったことがあるくらいかも.. というのを思い出したので書いておく

[WebSocket - FastAPI](https://fastapi.tiangolo.com/ja/advanced/websockets/)

genevt にはいくつかのサーバーを実装したクラスがあるようだが、それらはどれも `((host, post), handler)` を取得して、「呼び出すと内部でハンドル処理をして結果を返す」というインターフェースを継承しているらしい

```python
def handle(socket, address):
     print('new connection!')

server = StreamServer(('127.0.0.1', 1234), handle) # creates a new server
server.start() # start accepting new connections
```

ただし、上記のコードそのままではサーバーとしては動かず、サーバーが待機状態にならずにプログラムが終了してしまう。(おそらく"あくまでもインターフェース"であるため)

```python
def handle(socket, address):
     print('new connection!')

server = StreamServer(('127.0.0.1', 1234), handle)
server.server_forever()
```

`server.start()` ではなく `server.serve_forever()` を使うと、サーバーが指定したポートで待ち受け状態になって、通信を行うことができる

レスポンスなどを返していないので、正常終了にはならないものの、サーバーのログ(笑)として `new connection!` が出力されることが確認できた

```shell
$ cat main.py
def handle(socket, address):
     print('new connection!')

server = StreamServer(('127.0.0.1', 16379), handle)
server.server_forever()

$ python main.py
new connection!
new connection!

# -----
$ curl localhost:16379
curl: (56) Recv failure: Connection reset by peer
$ curl localhost:16379
curl: (56) Recv failure: Connection reset by peer
```

socket なサーバーと curl のように CLI で通信するには telnet を使うと良いらしい

[windows - How to establish socket connection using the command line - Stack Overflow](https://stackoverflow.com/questions/20346456/how-to-establish-socket-connection-using-the-command-line)

# appendix

## ソケットサーバー

- [geventやasync/awaitで切断検知付きソケットサーバを実装 - Qiita](https://qiita.com/haminiku/items/0af7c47f073e05b4424c)
  - gevent についてもう少し詳しく知りたい、async/await を実装して確かめたい、とかなったら良さそうな記事

## Echo サーバー

クライアントが送信した文字列を、反復して返す (Echo する) というサーバー実装の最初の一歩としてある概念っぽい

サーバーサイド系の言語とかのチュートリアルとして良さそう

- [ECHOプロトコル - Wikipedia](https://ja.wikipedia.org/wiki/ECHO%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB)
- 様々な言語での入門記事がある
  - [pythonで簡単な echo サーバーを作りましょう - Qiita](https://qiita.com/iari/items/5872a024bbd362efe63b)
  - [C言語でTCPソケットを使ってechoサーバーを実装してみた - reboooot․net](https://reboooot.net/post/implement-tcp-echo-server/)
  - [TypeScript＋Node.jsで、Echo Server／Clientを書いてみる - CLOVER🍀](https://kazuhira-r.hatenablog.com/entry/2021/11/20/222927)
  - [PHP で echo サーバーを書いて I/Oモデルを理解する by 富所 亮 | トーク | PHPerKaigi 2022 #phperkaigi - fortee.jp](https://fortee.jp/phperkaigi-2022/proposal/bdffee45-28c2-4f8f-976e-bf1de310fdb1)
    PHPKaigi の記事だ
  - [Echo - High performance, minimalist Go web framework](https://echo.labstack.com/) 
    しまった。これはフレームワークの Echo だった

## Python code formatter

* [black - Qiita](https://qiita.com/sin9270/items/85e2dab4c0144c79987d#black)
