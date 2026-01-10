# appointment_repo.py
class MedicineRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, appointment_id: int, name: str, fee: int):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO medicines (appointment_id, name, fee)
            VALUES (?, ?, ?)
        """, (appointment_id, name, fee))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_medicine_by_appointment_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
            Select * from medicines
            Where appointment_id = ?
        """, (id,))
        return cursor.fetchall()

