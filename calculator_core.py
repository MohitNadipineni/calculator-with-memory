import sqlite3

class Calculate():

    def __init__(self):
        self.conn = sqlite3.connect("calculator.db" , check_same_thread= False)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                expression TEXT NOT NULL,
                result REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


    def operation(self,a,op,b):
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            try:
                result = a / b
            except ZeroDivisionError:
                 return "Can't divide by zero"
        else:
                return "Invalid operator"     

        self.conn.execute(
            "INSERT INTO history (expression, result) VALUES (?, ?)",
            (f"{a} {op} {b}", result)
        )
        self.conn.commit()
        return result
    def show_history(self):
        rows = self.conn.execute(
            "SELECT expression, result FROM history ORDER BY id"
        ).fetchall()
        for i, (expression, result) in enumerate(rows, start=1):
            print(f"{i}. {expression} = {result}")

    def get_history(self):
        rows = self.conn.execute(
            "SELECT expression, result FROM history ORDER BY id"
        ).fetchall()
        items = []
        for expression, result in rows:
            items.append({"expression": expression, "result": result})
        return items       

    def clear_history(self):
        self.conn.execute("DELETE FROM history")
        self.conn.commit()

    def close(self):
       self.conn.close()       
