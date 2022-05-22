from tkinter import *
from tkinter import messagebox
from employee import Employee
from supplier import Supplier
from category import Category
from product import Product
from sales import Sales
import sqlite3
import os
import threading


class StockManager:
    def __init__(self, root_win):
        self.root = root_win
        self.root.geometry("1350x700+0+0")
        self.root.title("Système de Gestion de Stock")
        self.root.config(bg="white")

        # screen Title
        title = Label(self.root, text="Tableau de Bord", font=("Lato", 26, "bold"), bg="white", fg="#343A40", anchor="w", padx=20) # may add anchor here to center left
        title.place(x=200, y=0, relwidth=1, height=70)

        # logout button
        logout_btn = Button(self.root, text="déconnexion", font=("Lato", 11, "bold"), bd=0, bg="#F66B0E", fg="white")
        logout_btn.place(x=1180, y=10, height=40, width=120)

        # Menu
        menu_frame = Frame(self.root, bd=0, bg="#23282c", relief=RIDGE)
        menu_frame.place(x=0, y=0, width=200, height=400, relheight=1)

        menu_label = Label(menu_frame, text="Menu", font=("Lato", 15, "bold"), fg="#313552", bg="#23ba9b")
        menu_label.pack(side=TOP, fill=X)

        employee_btn = Button(menu_frame, text="Employés", command=self.employee, font=("Lato", 14, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        employee_btn.pack(side=TOP, fill=X)
        supplier_btn = Button(menu_frame, text="Fournisseurs", command=self.supplier, bg="#23282c", font=("Lato", 14, "normal"), fg="#a7acb2", bd=0, cursor="hand2")
        supplier_btn.pack(side=TOP, fill=X)
        product_btn = Button(menu_frame, text="Produits", command=self.product, font=("Lato", 14, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        product_btn.pack(side=TOP, fill=X)
        category_btn = Button(menu_frame, text="Catégories", command=self.category, font=("Lato", 14, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        category_btn.pack(side=TOP, fill=X)
        sales_btn = Button(menu_frame, text="Ventes", command=self.sales, font=("Lato", 14, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        sales_btn.pack(side=TOP, fill=X)
        quit_btn = Button(menu_frame, text="Quitter", font=("Lato", 14, "normal"), bg="#23282c", fg="#a7acb2", bd=0, cursor="hand2")
        quit_btn.pack(side=TOP, fill=X)

        # dashboard content
        self.employee_label = Label(self.root, text="Total des Employés\n0", font=("Lato", 15, "bold"), fg="white", bg="#f27b53", bd=5)
        self.employee_label.place(x=300, y=80, width=300, height=100)
        self.supplier_label = Label(self.root, text="Total des Fournisseurs\n0", font=("Lato", 15, "bold"), fg="white", bg="#dc587d", bd=5)
        self.supplier_label.place(x=650, y=80, width=300, height=100)
        self.product_label = Label(self.root, text="Total des Produits\n0", font=("Lato", 15, "bold"), fg="white", bg="#847cc5", bd=5)
        self.product_label.place(x=1000, y=80, width=300, height=100)
        self.category_label = Label(self.root, text="Total des Catégories\n0", font=("Lato", 15, "bold"), fg="white", bg="#fbb168", bd=5)
        self.category_label.place(x=300, y=200, width=300, height=100)
        self.sales_label = Label(self.root, text="Total des Ventes\n0", font=("Lato", 15, "bold"), fg="white", bg="#23ba9b", bd=5)
        self.sales_label.place(x=650, y=200, width=300, height=100)

        # footer
        footer = Label(self.root, text="will write footer here later", font=("Lato", 15, "normal"), bg="#2EB086", fg="#313552") # may add anchor here to center left
        footer.place(x=0, y=670, relwidth=1, height=30)

        self.update_content()

        # ========================================================

    def employee(self):
        self.new_window = Toplevel(self.root)
        self.emp_manager = Employee(self.new_window)

    def supplier(self):
        self.new_window = Toplevel(self.root)
        self.supp_manager = Supplier(self.new_window)

    def category(self):
        self.new_window = Toplevel(self.root)
        self.category_manager = Category(self.new_window)

    def product(self):
        self.new_window = Toplevel(self.root)
        self.product_manager = Product(self.new_window)

    def sales(self):
        self.new_window = Toplevel(self.root)
        self.sales_manager = Sales(self.new_window)

    def update_content(self):
        con = sqlite3.connect("system.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM product")
            p = cur.fetchone()[0]
            self.employee_label.config(text=f"Total des Employés\n{p}")

            cur.execute("SELECT COUNT(*) FROM supplier")
            supp = cur.fetchone()[0]
            self.supplier_label.config(text=f"Total des Fournisseurs\n{supp}")

            cur.execute("SELECT COUNT(*) FROM product")
            prd = cur.fetchone()[0]
            self.product_label.config(text=f"Total des Produits\n{prd}")

            cur.execute("SELECT COUNT(*) FROM category")
            cat = cur.fetchone()[0]
            self.category_label.config(text=f"Total des Catégories\n{cat}")

            self.sales_label.config(text=f"Total des Ventes\n{str(len(os.listdir('bills')))}")

            threading.Timer(1.0, self.update_content).start()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    system = StockManager(root)
    root.mainloop()
