# main_app/views.py
from django.shortcuts import render
from django.db import connection


def execute_queries():
    queries = [
        {
            "query": """
                SELECT last_name, first_name, birth_year 
                FROM clinic_patient 
                WHERE birth_year > 1998 
                ORDER BY last_name;
            """,
            "description": "Пацієнти, народжені після 1998 року"
        },
        {
            "query": """
                SELECT category, COUNT(*) AS patient_count 
                FROM clinic_patient 
                GROUP BY category;
            """,
            "description": "Кількість пацієнтів за категоріями"
        },
        {
            "query": """
                SELECT 
                    p.last_name, p.first_name, s.stay_days, 
                    s.stay_days * s.daily_cost AS total_cost,
                    s.stay_days * s.daily_cost * (1 - s.discount_percent) AS discounted_cost
                FROM clinic_stay s
                JOIN clinic_patient p ON s.patient_id = p.patient_id;
            """,
            "description": "Сума лікування і сума з урахуванням пільги"
        },
        {
            "query": """
                SELECT 
                    p.last_name AS patient_last_name, 
                    d.last_name AS doctor_last_name, 
                    s.admission_date, s.stay_days
                FROM clinic_stay s
                JOIN clinic_doctor d ON s.doctor_id = d.doctor_id
                JOIN clinic_patient p ON s.patient_id = p.patient_id
                WHERE d.specialization = 'therapist';
            """,
            "description": "Звернення до лікаря-терапевта"
        },
        {
            "query": """
                SELECT 
                    d.last_name, 
                    COUNT(s.stay_id) AS total_visits
                FROM clinic_stay s
                JOIN clinic_doctor d ON s.doctor_id = d.doctor_id
                GROUP BY d.doctor_id;
            """,
            "description": "Кількість звернень пацієнтів до кожного лікаря"
        },
        {
            "query": """
                SELECT 
                    d.specialization, 
                    p.category, 
                    COUNT(s.stay_id) AS patient_count
                FROM clinic_stay s
                JOIN clinic_doctor d ON s.doctor_id = d.doctor_id
                JOIN clinic_patient p ON s.patient_id = p.patient_id
                GROUP BY d.specialization, p.category;
            """,
            "description": "Кількість пацієнтів за категоріями і спеціалізаціями лікарів"
        }
    ]

    results = []
    with connection.cursor() as cursor:
        for query in queries:
            cursor.execute(query["query"])
            columns = [col[0] for col in cursor.description]
            results.append({
                "description": query["description"],
                "data": cursor.fetchall(),
                "columns": columns
            })

        # Додати запит для отримання всіх таблиць
        cursor.execute("show tables;")
        tables = cursor.fetchall()

        # Додати запит для отримання вмісту кожної таблиці
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT * FROM {table_name};")
            table_data = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            results.append({
                "columns": columns,
                "description": f"Вміст таблиці {table_name}",
                "data": table_data
            })

    return results


def project_info(request):
    project_name = "Django project"
    student_info = {"name": "Недобиткін Михайло", "group": "кн21003б"}
    query_results = execute_queries()  # Виконуємо запити

    return render(request, 'project_info.html', {
        'project_name': project_name,
        'student_info': student_info,
        'query_results': query_results,  # Передаємо результати запитів в шаблон
    })
