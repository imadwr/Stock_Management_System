from tkinter import *
from tkinter import ttk, messagebox


class POS:
    def __init__(self, root_win):
        self.root = root_win
        self.root.geometry("1350x700+0+0")
        self.root.title("Système de Gestion de Stock")
        self.root.config(bg="white")

        # screen Title
        title = Label(self.root, text="Point de Vente", font=("Lato", 26, "bold"), bg="white", fg="#343A40", anchor="w", padx=20) # may add anchor here to center left
        title.place(x=10, y=0, relwidth=1, height=70)

        # logout button
        logout_btn = Button(self.root, text="déconnexion", font=("Lato", 11, "bold"), bd=0, bg="#F66B0E", fg="white")
        logout_btn.place(x=1180, y=10, height=40, width=120)

        # product Frame ----------------------------------

        # produt search variable
        self.search_var = StringVar()

        product_frame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        product_frame.place(x=10, y=110, width=410, height=550)

        product_title = Label(product_frame, text="Section des Produits", font=("Lato", 14, "normal"),  bg="#2EB086", fg="white")
        product_title.pack(side=TOP, fill=X)

        product_search_frame = Frame(product_frame, bd=1, relief=RIDGE, bg="white")
        product_search_frame.place(x=2, y=36, width=399, height=90)

        search_label = Label(product_search_frame, text="Recherche de Produit", font=("Lato", 14, "normal"), bg="white", fg="#2EB086")
        search_label.place(x=2, y=5)
        pd_name_label = Label(product_search_frame, text="Nom de produit", font=("Lato", 13, "normal"), bg="white")
        pd_name_label.place(x=2, y=40)
        pd_name_txt = Entry(product_search_frame, textvariable=self.search_var, font=("Lato", 13, "normal"), bg="#EEE6CE")
        pd_name_txt.place(x=125, y=40, width=150, height=22)
        search_btn = Button(product_search_frame, text="Chercher", font=("Lato", 13, "normal"), bg="#2EB086", fg="white")
        search_btn.place(x=280, y=40, width=110, height=22)
        show_all_btn = Button(product_search_frame, text="Afficher tout", font=("Lato", 13, "normal"), bg="#313552",fg="white")
        show_all_btn.place(x=280, y=65, width=110, height=22)

        # product list
        product_list_frame = Frame(product_frame, bd=3, relief=RIDGE)
        product_list_frame.place(x=2, y=130, width=399, height=385)

        scroll_y = Scrollbar(product_list_frame, orient=VERTICAL)
        scroll_x = Scrollbar(product_list_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        list_columns = ("id", "nom", "prix", "qte", "status")
        self.product_list_table = ttk.Treeview(product_list_frame, columns=list_columns, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.product_list_table.pack(fill=BOTH, expand=1)
        scroll_x.config(command=self.product_list_table.xview)
        scroll_y.config(command=self.product_list_table.yview)

        self.product_list_table.heading("id", text="ID")
        self.product_list_table.heading("nom", text="Nom")
        self.product_list_table.heading("prix", text="Prix")
        self.product_list_table.heading("qte", text="QTE")
        self.product_list_table.heading("status", text="Status")

        self.product_list_table["show"] = "headings"

        self.product_list_table.column("id", width=90)
        self.product_list_table.column("nom", width=100)
        self.product_list_table.column("prix", width=100)
        self.product_list_table.column("qte", width=100)
        self.product_list_table.column("status", width=100)
        # self.product_list_table.bind("<ButtonRelease-1>", self.get_data)
        note_label = Label(product_frame, text="Note: Entrez 0 pour enlever le produit du panier", font=("Lato", 12, "normal"), fg="#B22727", bg="white")
        note_label.pack(side=BOTTOM, fill=X)

        # customer frame

        # variables customer
        self.cust_name_var = StringVar()
        self.cust_contact_var = StringVar()
        customer_frame = Frame(self.root, bd=3, relief=RIDGE, background="white")
        customer_frame.place(x=420, y=110, width=530, height=70)

        cust_title = Label(customer_frame, text="Information du client", font=("Lato", 14, "normal"), bg="#2EB086", fg="white")
        cust_title.pack(side=TOP, fill=X)

        cust_name_label = Label(customer_frame, text="Nom", font=("Lato", 14, "normal"), bg="white")
        cust_name_label.place(x=5, y=35)
        cust_name_txt = Entry(customer_frame, textvariable=self.cust_name_var, font=("Lato", 14, "normal"), bg="#EEE6CE")
        cust_name_txt.place(x=80, y=35, width=180)

        cust_contact_label = Label(customer_frame, text="Contact No.", font=("Lato", 14, "normal"), bg="white")
        cust_contact_label.place(x=270, y=35)
        cust_contact_txt = Entry(customer_frame, textvariable=self.cust_contact_var, font=("Lato", 14, "normal"), bg="#EEE6CE")
        cust_contact_txt.place(x=380, y=35, width=140)

        # cart frame ---------------------------------------
        cal_cart_frame = Frame(self.root, bd=2, relief=RIDGE)
        cal_cart_frame.place(x=420, y=190, width=530, height=360)

        cart_frame = Frame(cal_cart_frame, bd=2, relief=RIDGE)
        cart_frame.place(x=2, y=3, relwidth=1, height=340)
        cust_title = Label(cart_frame, text="Panier   | \tTotal des Produits: [ 0 ]", font=("Lato", 14, "normal"), bg="#2EB086", fg="white")
        cust_title.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(cart_frame, orient=VERTICAL)
        scroll_x = Scrollbar(cart_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        list_columns_cart = ("id", "nom", "prix", "qte", "status")
        self.cart_list_table = ttk.Treeview(cart_frame, columns=list_columns_cart, yscrollcommand=scroll_y.set,
                                            xscrollcommand=scroll_x.set)
        self.cart_list_table.pack(fill=BOTH, expand=1)
        scroll_x.config(command=self.cart_list_table.xview)
        scroll_y.config(command=self.cart_list_table.yview)

        self.cart_list_table.heading("id", text="ID")
        self.cart_list_table.heading("nom", text="Nom")
        self.cart_list_table.heading("prix", text="Prix")
        self.cart_list_table.heading("qte", text="QTE")
        self.cart_list_table.heading("status", text="Status")
        self.cart_list_table["show"] = "headings"

        self.cart_list_table.column("id", width=90)
        self.cart_list_table.column("nom", width=100)
        self.cart_list_table.column("prix", width=100)
        self.cart_list_table.column("qte", width=100)
        self.cart_list_table.column("status", width=100)

        # self.cart_list_table.bind("<ButtonRelease-1>", self.get_data)

        # cart widgets
        self.p_id_var = StringVar()
        self.p_name_var = StringVar()
        self.p_price_var = StringVar()
        self.p_qty_var = StringVar()
        self.p_stock_var = StringVar()
        cart_widgets_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        cart_widgets_frame.place(x=420, y=550, width=530, height=110)

        p_name_label = Label(cart_widgets_frame, text="Nom de produit", font=("Lato", 13, "normal"), bg="white")
        p_name_label.place(x=5, y=5)
        p_name_text = Entry(cart_widgets_frame, textvariable=self.p_name_var, font=("Lato", 13, "normal"), state="readonly", bg="#EEE6CE")
        p_name_text.place(x=5, y=35, width=190, height=22)

        p_price_label = Label(cart_widgets_frame, text="Prix par Qte", font=("Lato", 13, "normal"), bg="white")
        p_price_label.place(x=230, y=5)
        p_price_text = Entry(cart_widgets_frame, textvariable=self.p_price_var, font=("Lato", 13, "normal"), state="readonly", bg="#EEE6CE")
        p_price_text.place(x=230, y=35, width=150, height=22)

        p_qty_label = Label(cart_widgets_frame, text="Quantité", font=("Lato", 13, "normal"), bg="white")
        p_qty_label.place(x=400, y=5)
        p_qty_text = Entry(cart_widgets_frame, textvariable=self.p_qty_var, font=("Lato", 13, "normal"), bg="#EEE6CE")
        p_qty_text.place(x=400, y=35, width=120, height=22)

        p_stock_label = Label(cart_widgets_frame, text="En Stock [999]", font=("Lato", 13, "normal"), bg="white")
        p_stock_label.place(x=5, y=70)

        add_cart_btn = Button(cart_widgets_frame, text="Ajouter au Panier", font=("Lato", 12, "normal"), bg="#0AA1DD", fg="white")
        add_cart_btn.place(x=180, y=70, width=150, height=30)
        clear_cart_btn = Button(cart_widgets_frame, text="Vider Panier", font=("Lato", 12, "normal"), bg="#313552", fg="white")
        clear_cart_btn.place(x=340, y=70, width=150, height=30)

        # billing frame -----------------------------------------------------
        bill_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        bill_frame.place(x=953, y=110, width=390, height=410)

        cust_title = Label(cart_frame, text="Panier   | \tTotal des Produits: [ 0 ]", font=("Lato", 14, "normal"), bg="#2EB086", fg="white")
        cust_title.pack(side=TOP, fill=X)

if __name__ == "__main__":
    root = Tk()
    system = POS(root)
    root.mainloop()
