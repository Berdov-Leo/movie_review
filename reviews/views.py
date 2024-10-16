from django.shortcuts import render
from .forms import ReviewForm
import joblib
from .models import Review

# Загрузка обученной модели
model = joblib.load('reviews/models/logistic_model.pkl')
tfidf = joblib.load('reviews/models/tfidf.pkl')

def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['text']
            # Преобразование текста
            review_vector = tfidf.transform([review_text])
            # Предсказание
            prediction = model.predict(review_vector)[0]
            sentiment = 'positive' if prediction == 1 else 'negative'
            # Сохранение результата
            Review.objects.create(text=review_text, rating=prediction, sentiment=sentiment)
            return render(request, 'result.html', {'sentiment': sentiment, 'rating': prediction})
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})
