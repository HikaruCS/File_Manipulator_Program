# File Manipulator Program
コマンドを使ってファイル操作をするプログラム
## コマンド
1. python3 file_manipulator.py reverse <input-file-path> <output-file-path>: input-file-pathの内容を逆にして、output-file-pathとして保存します。
2. python3 file_manipulator.py copy <input-file-path> <output-file-path>: input-file-pathの内容をコピーして、output-file-pathとして保存します。
3. python3 file_manipulator.py duplicate-contents <input-file-path> n: input-file-pathの内容を複製し、その複製したものをinput-file-pathにn回複製します。
4. python3 file_manipulator.py replace-string <input-file-path> needle newstring: input-file-path内のある文字列'needle'を検索し、その'needle'をすべてある文字列'newstring'に置き換えます。
## 注意
細かな例外処理などはしていないので、予期せぬエラーが起こる可能性があります。ご容赦ください。
