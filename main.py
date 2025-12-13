"""ローカルでポモドーロWebアプリ(index.html)を配信する簡易サーバー."""

from functools import partial
# partial: 関数に引数をあらかじめ固定した新しい関数を作るために使う。
# ここではSimpleHTTPRequestHandlerに「どのディレクトリを配信するか」を固定するために利用。

from http.server import SimpleHTTPRequestHandler
# SimpleHTTPRequestHandler: 標準ライブラリの簡易HTTPサーバー用ハンドラー。
# 静的ファイル(index.htmlやCSS/JS)を返す役割を持つ。

from pathlib import Path
# Path: ファイルパスを扱う標準ライブラリのクラス。
# main.py が置かれたディレクトリを基準に index.html へのパスを解決するために使う。

from socketserver import TCPServer
# TCPServer: TCP接続を受け付けるサーバークラス。
# ハンドラー(SimpleHTTPRequestHandler)と組み合わせてHTTPサーバーを立てる。


def serve(port: int = 8000) -> None:
    """index.htmlをルートで配信するローカルサーバーを起動する."""
    # なぜTCPServer + SimpleHTTPRequestHandler?
    # - 標準ライブラリだけで完結し、依存なしで動く
    # - 少量の静的ファイル配信に十分
    # 代替案:
    # - http.server.ThreadingHTTPServer: 複数同時接続を並列処理できるが、本用途では不要
    # - Flask/FastAPIなど: 動的処理や拡張性は高いが、今回の静的配信にはオーバーキル
    #
    # port引数: ブラウザでアクセスする番号。デフォルト8000番を使う。
    #   もし別のアプリと衝突したら、serve(8080) のように呼び出し時に変えられる。
    #
    # Path(__file__).parent: このmain.pyが置かれているフォルダを指す
    # resolve(): 絶対パスに変換
    # → index.htmlがある同じディレクトリをドキュメントルートにする
    root = Path(__file__).parent.resolve()
    # SimpleHTTPRequestHandlerは静的ファイルを配るサーバー用ハンドラー
    # directory=... で root 配下のファイル(index.htmlやCSS/JS)を返す
    # partialで引数を固定し、後でTCPServerに渡す
    #   → handlerは「リクエストを受けたらrootの中から探して返す関数」になる
    # 代替案:
    # - functools.partialを使わず、カスタムクラスを作って__init__でdirectoryを指定する手もある。
    #   ただし数行で済むpartialの方が短く、挙動も明確。
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))

    with TCPServer(("", port), handler) as httpd:
        print(f"ローカルサーバー起動: http://localhost:{port}")
        print("Ctrl+Cで停止します。")
        # serve_forever(): サーバーを起動し、Ctrl+Cで止めるまでHTTPリクエストを処理し続ける
        # 代替案:
        # - httpd.handle_request() を自前ループで呼ぶ: 1リクエストずつ処理するがループを自作する必要がある
        # - with文を使わず手動でclose: リソース解放を忘れやすいのでwithが安全
        httpd.serve_forever()


if __name__ == "__main__":
    serve()
