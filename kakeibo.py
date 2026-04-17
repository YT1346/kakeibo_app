import csv
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import matplotlib.pyplot as plt
FILE_NAME="kakeibo.csv"
def add_data():
    category=combo_category.get()
    amount=entry_amount.get()
    if category =="" or amount=="":
        return
    now=datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME,"a",newline="",encoding="utf-8-sig")as f:
        writer=csv.writer(f)
        writer.writerow([now,category,amount])
    combo_category["values"]=load_categories()
    print(combo_category)
    entry_amount.delete(0,tk.END)
    show_data()
       
def show_data():
    listbox.delete(0,tk.END)
    total=0  
    try:
        with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
            reader=csv.reader(f)
            for row in reader:
                listbox.insert(tk.END,f"{row[0]}|{row[1]}|{row[2]}円") 
                total +=int(row[2])
    except FileNotFoundError:
        pass
    label_total.config(text=f"合計:{total}円")
def delete_data():
   
    try:
        selected=listbox.curselection()
        if not selected:
            return
        index=selected[0]
        with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
            rows=list(csv.reader(f))
            rows.pop(index)
        with open(FILE_NAME,"w",newline="",encoding="utf-8-sig")as f:
            writer=csv.writer(f)
            writer.writerows(rows)
        
        show_data()
    except FileNotFoundError:
       pass
def select_data(event):
    selected=listbox.curselection()
    if not selected:
        return
    index=selected[0]

    with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
        reader=csv.reader(f)
        rows=list(reader)
        row=rows[index]
    entry_amount.delete(0,tk.END)
    entry_amount.insert(0,row[2])
    combo_category.set(row[1])
def load_categories():
    categories=set()
    try:
        with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
            reader=csv.reader(f)
            for row in reader:
                categories.add(row[1])
            
    except FileNotFoundError:
        pass
    return list(categories)
    
def update_data():
    selected=listbox.curselection()
    if not selected:
        return
    index=selected[0]
    category=combo_category.get()
               
    amount=entry_amount.get()
    print("カテゴリ取得",category)
    with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
        rows=list(csv.reader(f))
        print(rows[index])
        rows[index][1]=category
        rows[index][2]=amount
    with open(FILE_NAME,"w",newline="",encoding="utf-8-sig")as f:
        writer=csv.writer(f)
        writer.writerows(rows)
        print(rows[index])
    listbox.selection_clear(0, tk.END)
    combo_category.set("")
    entry_amount.delete(0,tk.END)
    show_data()   
def show_graph():
    import matplotlib.font_manager as fm
    category_total={}
    try:
        with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
            reader=csv.reader(f)
            for row in reader:
                category=row[1]
                amount=int(row[2])
                if category in category_total:
                    category_total[category] +=amount
                else:
                    category_total[category]=amount
    except FileNotFoundError:
        return
    categories = list(category_total.keys())
    amounts = list(category_total.values())
    font_path = "C:/Windows/Fonts/msgothic.ttc"
    font_prop = fm.FontProperties(fname=font_path)
       
    plt.rcParams["font.family"] = font_prop.get_name()
    plt.figure()
    plt.bar(categories, amounts)
    plt.title("カテゴリ別支出")
    plt.show()
    
root=tk.Tk()
root.title("家計簿アプリ")
categories=load_categories()
label_title=tk.Label(root,text="家計簿アプリ",font=("Arial",16,"bold"))
label_title.pack(pady=10)
label_total=tk.Label(root,text="合計:0円",font=("Arial",12))
label_total.pack(pady=5)

frame_input=tk.Frame(root)
frame_input.pack(pady=5)
combo_category=ttk.Combobox(frame_input,values=categories)
combo_category.set("食費")
entry_amount=tk.Entry(frame_input)
tk.Label(frame_input,text="カテゴリ").pack(side="left")
combo_category.pack(in_=frame_input, side="left", padx=5)
tk.Label(frame_input, text="金額").pack(side="left")
entry_amount.pack(in_=frame_input, side="left", padx=5)

frame_button=tk.Frame(root)
frame_button.pack()
btn_width=10
tk.Button(frame_button,text="追加",bg="green",fg="white",command=add_data,width=btn_width).pack(side="left",padx=5)
tk.Button(frame_button,text="一覧表示",bg="red",fg="white",command=show_data,width=btn_width).pack(side="left",padx=5)
tk.Button(frame_button,text="削除",bg="blue",fg="white",command=delete_data, width=btn_width).pack(side="left",padx=5)
tk.Button(frame_button,text="更新",bg="orange",fg="white",command=update_data, width=btn_width).pack(side="left",padx=5)
tk.Button(frame_button,text="グラフ",command=show_graph, width=btn_width).pack(side="left",padx=5)

listbox=tk.Listbox(root,width=50,height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>",select_data)
combo_category.bind("<<ComboboxSelected>>",lambda e:print(combo_category.get()))
show_data()
root.mainloop()
        