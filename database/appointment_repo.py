# appointment_repo.py
class AppointmentRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, patient_id, appointment_no, consultation_fee):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO appointments
            (patient_id, appointment_no, consultation_fee)
            VALUES (?, ?, ?)
        """, (patient_id, appointment_no, consultation_fee))
        self.conn.commit()
        return cursor.lastrowid
    
    
    def get_appointment_by_patient_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute("""
            Select * from appointments
            Where patient_id = ?
        """, (id,))
        return cursor.fetchall()
