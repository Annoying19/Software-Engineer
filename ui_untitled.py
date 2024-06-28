def search_employees(self, table_widget, input_text):
        search_term = input_text.text()
        query = """
            SELECT employee_id,
                    first_name || ' ' || last_name AS full_name,
                    position,
                    phone,
                    hire_date
            FROM Users
            WHERE employee_id LIKE ? OR first_name LIKE ? OR last_name LIKE ?;
        """
        try:
            cursor.execute(query, (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

            table_widget.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                view_button = QPushButton("View")
                view_button.clicked.connect(partial(self.show_view_employee_temp, row_idx))
                table_widget.setCellWidget(row_idx, len(row_data), view_button)

            self.add_employee_view_button(table_widget)  # Call the function to add view buttons

        except Exception as e:
            print(f"Error executing query for Employees: {e}")