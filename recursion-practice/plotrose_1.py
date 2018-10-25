from turtle import *  # 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-100, -100], [100, -100], [100, 100], [-100, 100]], 0.4, 80)
done()  # turtleの終了処理