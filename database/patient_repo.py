# # patient_repo.py
# class PatientRepository:
#     def __init__(self, conn):
#         self.conn = conn

#     def add(self, data):
#         cursor = self.conn.cursor()
#         my_data = (
#             data['name'],
#             data['age'],
#             data['gender'],
#             data['dob'],
#             data['phone'],
#             data['address'],
#             data['first_appointment'],
#             data['major_complain'],
#             data['followup_date'],
#             data['total_followups'],
            
#         )
        
#         cursor.execute("""
#             INSERT INTO patients
#             (name, age, gender, dob, phone, address,
#              first_appointment, major_complain, followup_date, total_followups)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, my_data)
#         self.conn.commit()
#         return cursor.lastrowid
    
#     def update(self, patient_id, data):
#         cursor = self.conn.cursor()
#         my_data = (
#             data['name'],
#             data['age'],
#             data['gender'],
#             data['dob'],
#             data['phone'],
#             data['address'],
#             data['first_appointment'],
#             data['major_complain'],
#             data['followup_date'],
#             data['total_followups'],
            
#         )
#         cursor.execute('''
#             UPDATE patients SET name=?, age=?, gender=?, dob=?, phone=?, 
#                               address=?, first_appointment=?, major_complain=?, 
#                               followup_date=?, total_followups=?
#             WHERE id=?
#         ''', (*my_data, patient_id))
#         self.conn.commit()

#     def get_all(self):
#         cursor = self.conn.cursor()
#         cursor.execute("SELECT * FROM patients ORDER BY id DESC")
#         return cursor.fetchall()

from data_validation import Patient


class PatientRepository:
    def __init__(self, conn):
        self.conn = conn

    def add(self, patient: Patient) -> int:
        cursor = self.conn.cursor()

        # data = patient.model_dump()
        data = patient.model_dump(exclude_none=False)

        my_data = (
            data["name"],
            data["age"],
            data["gender"],
            data["dob"],
            data["phone"],
            data["address"],
            data["first_appointment"],
            data["major_complain"],
            data["followup_date"],
            data["total_followups"],
        )

        cursor.execute(
            """
            INSERT INTO patients
            (name, age, gender, dob, phone, address,
             first_appointment, major_complain, followup_date, total_followups)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            my_data
        )

        self.conn.commit()
        return cursor.lastrowid

    def update(self, patient_id: int, patient: Patient) -> None:
        cursor = self.conn.cursor()
        data = patient.model_dump(exclude_none=False)

        my_data = (
            data["name"],
            data["age"],
            data["gender"],
            data["dob"],
            data["phone"],
            data["address"],
            data["first_appointment"],
            data["major_complain"],
            data["followup_date"],
            data["total_followups"],
        )

        cursor.execute(
            """
            UPDATE patients
            SET name=?, age=?, gender=?, dob=?, phone=?,
                address=?, first_appointment=?, major_complain=?,
                followup_date=?, total_followups=?
            WHERE id=?
            """,
            (*my_data, patient_id)
        )

        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM patients ORDER BY id DESC")
        return cursor.fetchall()
