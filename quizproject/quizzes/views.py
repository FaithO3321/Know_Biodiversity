import requests
from django.shortcuts import render
from django.http import HttpResponse

def fetch_quiz_questions(request):
    species_name = "Panthera tigris"  # Example species; you can make this dynamic if you want
    url = f'https://api.gbif.org/v1/species?name={species_name}'
    
    try:
        # Fetch data from GBIF API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        species_info = data.get('results', [])[:5]  # Limit to 5 questions

        # Prepare quiz questions
        questions = []
        for species in species_info:
            if species.get('scientificName') and species.get('kingdom'):
                question = {
                    "question": f"What kingdom does {species['scientificName']} belong to?",
                    "correct_answer": species['kingdom'],
                    "options": ["Animalia", "Plantae", "Fungi", "Protista"],  # Example options
                }
                questions.append(question)

    except requests.RequestException as e:
        print(f"Error fetching data from GBIF: {e}")
        questions = []

    return render(request, 'quizzes/quiz_list.html', {'questions': questions})

def submit_quiz(request):
    if request.method == 'POST':
        questions = request.POST  # Get posted data

        # Here, you can calculate the score based on the correct answers.
        # In this example, we're simply counting correct answers for simplicity.

        correct_answers = {
            "question_1": "Animalia",  # Example correct answers, replace with dynamic data
            "question_2": "Plantae",
            "question_3": "Fungi",
            "question_4": "Protista",
            "question_5": "Animalia",
        }

        score = 0
        for key, correct_answer in correct_answers.items():
            if questions.get(key) == correct_answer:
                score += 1

        return HttpResponse(f"You scored {score} out of 5!")
    return HttpResponse("Invalid request.")
