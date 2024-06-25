def create_product(self):
        self.edit_product_page = QWidget()
        self.edit_product_page.setObjectName("main_page")
        self.stackedWidget.addWidget(self.edit_product_page)
       
        # ===========================================
        #            product PAGE LABELS
        # ===========================================

        self.product_text_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(280, 50, 430, 40),
            text = "Register Product",
            font = font4,
            style = "font: bold"
        )

        self.product_id_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 150, 160, 40),
            text = "Product ID:",
            font = font1,
            style = ""
        )

        self.product_name_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 210, 170, 40),
            text = "Product Name",
            font = font1,
            style = ""
        )

        self.product_brand_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 210, 170, 40),
            text = "Brand",
            font = font1,
            style = ""
        )

        self.product_sku_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 310, 130, 40),
            text = "SKU",
            font = font1,
            style = ""
        )

        self.product_quantity_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 310, 170, 40),
            text = "Quantity",
            font = font1,
            style = ""
        )

        self.product_supplier_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 420, 130, 40),
            text = "Supplier",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 420, 160, 40),
            text = "Price",
            font = font1,
            style = ""
        )

        self.product_purchase_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(40, 530, 180, 40),
            text = "Purchase Date",
            font = font1,
            style = ""
        )

        self.product_price_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(380, 530, 160, 40),
            text = "Expiry Date",
            font = font1,
            style = ""
        )

        self.product_id_output_label = createLabel(
            parent = self.edit_product_page,
            name = "product_text",
            geometry = QRect(210, 150, 360, 40),
            text = "",
            font = font1,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # =================================================================

        self.name_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.brand_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 260, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.sku_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 360, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.quantity_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 360, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.supplier_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(40, 470, 330, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.price_input = createLineInput(
            parent = self.edit_product_page,
            name = "name_input",
            geometry = QRect(380, 470, 200, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ===================================================

        self.purchase_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(40, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        self.expiry_date = createDate(
            parent = self.edit_product_page,
            name = "purchase_date",
            geometry = QRect(380, 580, 230, 40),
            font = font2,
            style = "background-color: #F9F7FF; border: 1px solid black"
        )

        # ====================================================
        self.back_button = createButton(
            parent = self.edit_product_page,
            name = "back_button",
            geometry = QRect(40, 50, 70, 50),
            text = "Back",
            font = font3,
            style = "background-color: #004F9A"
        )

        self.clear_button = createButton(
            parent = self.edit_product_page,
            name = "clear_button",
            geometry = QRect(510, 730, 170, 50),
            text = "Clear",
            font = font3,
            style = "background-color: #882400"
        )

        # REGISTER BUTTON
        self.register_butotn = createButton(
            parent = self.edit_product_page,
            name = "register_button",
            geometry = QRect(690, 730, 250, 50),
            text = "Register Product",
            font = font3,
            style = "background-color: #006646"
        )