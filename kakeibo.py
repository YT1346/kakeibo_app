<<<<<<< HEAD
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
        
=======
!apt-get -y install fonts-ipafont-gothic
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
font_prop = fm.FontProperties(fname=font_path)

plt.rcParams["font.family"]=font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False
FILE_NAME="kakeibo.csv"
def init_file():
    try:
        with open(FILE_NAME,"x",newline="",encoding="utf-8-sig") as f:
            writer=csv.writer(f)
            writer.writerow(["日付","カテゴリ","金額"])
    except FileExistsError:
        pass
def save_data(expenses):
    with open(FILE_NAME,"w",newline="",encoding="utf-8-sig")as f:
        fieldnames=["日付","カテゴリ","金額"]
        writer=csv.DictWriter(f,fieldnames=fieldnames)

        writer.writeheader()
        for item in expenses:
            writer.writerow({"日付":item["date"],"カテゴリ":item["category"],"金額":item["amount"]})
def to_half_width(s):
    return s.translate(str.maketrans("０１２３４５６７８９", "0123456789"))
def add_data(expenses):
    date=datetime.now().strftime("%Y-%m-%d")
    categories=["食費","交通費","娯楽","日用品","その他"]
    for i,c in enumerate(categories,1):
        print(i,c)
    try:
        choice=int(input("番号を選択:"))
    except:
        print("数字を入力してください")
        return
    if 1<=choice<=len(categories):
        category=categories[choice-1]
    else:
        print("正しい番号入力してください")
        return

    try:
        amount_input=input("金額を入力:")
        amount=to_half_width(amount_input)
        amount=int(amount_input)

        if amount<0:
            print("0以上を入力してください")
            return
    except:
        print("数字を入力してください")
        return
    expenses.append({"date":date,"category":category,"amount":amount})

    print("保存しました")

def load_data():
    expenses=[]
    try:
        with open(FILE_NAME,"r",encoding="utf-8-sig")as f:
            reader=csv.DictReader(f)
            for row in reader:
                if not row["日付"]:
                    continue

                expenses.append({"date":row["日付"],"category":row["カテゴリ"],"amount":int(row["金額"])})

    except FileNotFoundError:
        print("データがありません")
    return expenses
def show_data(expenses):
    if not expenses:
        print("データがありません")
        return
    print("番号 日付　カテゴリ　金額")
    for i,item in enumerate((expenses),1):
        print(i,item["date"],item["category"],item["amount"],"円")
def delete_data(expenses):
    show_data(expenses)

    try:
        index=int(input("削除する番号"))
        if 1<=index<=len(expenses):
            confirm=input("本当に削除しますか？y/n")
            if confirm=="y":
                del expenses[index-1]
                print("削除しました")
            else:
                print("キャンセルしました")
        else:
           print("番号がありません")
    except:
        print("数字を入力してください")
def update_data(expenses):
    show_data(expenses)
    try:
        index=int(input("編集する番号:"))
        if not (1<=index<=len(expenses)):
            print("番号が違います")
            return
    except:
        print("数字を入力してください")
        return
    item=expenses[index-1]
    print(f"現在:{item['category']}{item['amount']}円")
    categories=["食費","交通費","娯楽","日用品","その他"]

    print("カテゴリを選んでください(そのままならenter)")
    for i,c in enumerate((categories),1):
        print(f"{i}:{c}")
    choice=input("選択:")
    if choice !="":
        try:
            choice=int(choice)
            if 1<=choice<=len(categories):
                item["category"]=categories[choice-1]
            else:
                print("番号が違います")
        except:
            print("数字を入力してください")
            return

        new_amount_input=input("新しい金額(そのままならenter)")
        
  
        if new_amount_input !="":
            try:
                new_amount_input=to_half_width(new_amount_input)
                new_amount=int(new_amount_input)
                if new_amount<0:
                    print("0以上を入力してください")
                    return
                item["amount"]=new_amount
            except:
                 print("数字を入力してください")
                 return
    print("更新しました")
def summary_by_month(expenses):
    data={}
    for item in expenses:
        month=item["date"][:7]
        category=item["category"]
        amount=item["amount"]
        if month not in data:
             data[month]={}
        if category not in data[month]:
            data[month][category]=0
        data[month][category] +=amount
    return data
def show_ranking(data):
    for month,categories in data.items():
        print(month)
        for i,(key,value) in enumerate(sorted(categories.items(),key=lambda x:x[1],reverse=True),1):
            print(i,"位",key,value,"円")
def show_graph(data):
    target_month=input("月を入力(例:2026-03):")

    if target_month not in data:
        print("データがありません")
        return
    categories=data[target_month]

    labels=list(categories.keys())
    values=list(categories.values())

    plt.figure()
    plt.pie(values,labels=labels,autopct="%1.1f%%",textprops={"fontproperties": font_prop} )
    plt.title(target_month+"の支出割合",fontproperties=font_prop)
    plt.show()

def main():
    init_file()
    expenses=load_data()
    while True:
        print("1:入力  2:削除　3:一覧 4:更新　5:集計  6:グラフ  7:終了")
        choice=input("選択:")
        if choice=="1":
            add_data(expenses)
            save_data(expenses)
        elif choice=="2":
            delete_data(expenses)
            save_data(expenses)
        elif choice=="3":
             show_data(expenses)
        elif choice=="4":
             update_data(expenses)
             save_data(expenses)
        elif choice=="5":
            data=summary_by_month(expenses)
            show_ranking(data)
        elif choice=="6":
            data=summary_by_month(expenses)
            show_graph(data)
        elif choice=="7":
            print("終了します")
            break
        else:
             print("1～7をえらんでください")
    while True:
        download=input("ダウンロードしますか？y/n")
        if download=="y":
            from google.colab import files
            files.download(FILE_NAME)
            print("ダウンロードします")
            break
        elif download=="n":
            print("終了")
            break
        else:
            print("正しく入力してください")
main()

>>>>>>> 8b18163a87c1bfb0b0a7990b7f6974348ae3617b
