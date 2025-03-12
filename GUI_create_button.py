import tkinter as tk
from tkinter import ttk

# Tkinter 창 생성
win = tk.Tk()
win.title("Python GUI")

# 라벨 생성
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# 클릭 이벤트 함수
def click_me():
    action.configure(text="** I have been clicked **")  # 버튼의 텍스트 변경
    a_label.configure(foreground="Red")
    a_label.configure(text="RED")

# 버튼 생성 (이걸 안 만들면 action 변수가 없음)
action = ttk.Button(win, text="Click Me", command=click_me)
action.grid(column=1, row=0)  # 버튼 위치 설정

# 이벤트 루프 시작
win.mainloop()