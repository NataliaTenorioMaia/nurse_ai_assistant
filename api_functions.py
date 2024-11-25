def get_data(patient_id):
    """ 
    Temporary function to be replaced with real API call.
    """
    if int(patient_id) == 1:
        data = {
            "id": 1,
            "name": "John Doe",
            "dob": "01/01/1975",
            "pcp": "Dr. Meredith Grey",
            "ehrId": "1234abcd",
            "referred_providers": [
                {"provider": "House, Gregory MD", "specialty": "Orthopedics"},
                {"specialty": "Primary Care"},
            ],
            "appointments": [
                {"date": "3/05/18", "time": "9:15am", "provider": "Dr. Meredith Grey", "status": "completed"},
                {"date": "8/12/24", "time": "2:30pm", "provider": "Dr. Gregory House", "status": "completed"},
                {"date": "9/17/24", "time": "10:00am", "provider": "Dr. Meredith Grey", "status": "noshow"},
                {"date": "11/25/24", "time": "11:30am", "provider": "Dr. Meredith Grey", "status": "cancelled"}
            ]
        }
        return data