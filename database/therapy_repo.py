class TherapyRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, appointment_id: int, name: str, fee: int):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO therapies (appointment_id, name, fee)
            VALUES (?, ?, ?)
        """, (appointment_id, name, fee))
        self.conn.commit()
        return cursor.lastrowid
    
    def get_therapy_by_appointment_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
            Select * from therapies
            Where appointment_id = ?
        """, (id,))
        return cursor.fetchall()