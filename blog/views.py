from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {'author': 'tech-wizard', 'title': 'Blog Post 1', 'content': 'First post content', 'date_posted': 'September 20, 2024'},
    {'author': 'code-master', 'title': 'Python Programming', 'content': 'Learning Python basics', 'date_posted': 'September 21, 2024'},
    {'author': 'data-science-enthusiast', 'title': 'Machine Learning', 'content': 'Exploring ML algorithms', 'date_posted': 'September 22, 2024'},
    {'author': 'web-developer', 'title': 'Building Websites', 'content': 'HTML, CSS, and JavaScript', 'date_posted': 'September 23, 2024'},
    {'author': 'anonymous-oracle', 'title': 'Blog Post 2', 'content': 'Second post content', 'date_posted': 'September 24, 2024'},
    {'author': 'ai-researcher', 'title': 'Deep Learning', 'content': 'Advanced neural networks', 'date_posted': 'September 25, 2024'},
    {'author': 'cyber-security-expert', 'title': 'Network Security', 'content': 'Protecting against threats', 'date_posted': 'September 26, 2024'},
    {'author': 'database-admin', 'title': 'Database Management', 'content': 'Efficient data storage', 'date_posted': 'September 27, 2024'},
    {'author': 'software-engineer', 'title': 'Software Development', 'content': 'Agile methodologies', 'date_posted': 'September 28, 2024'},
    {'author': 'network-architect', 'title': 'Network Architecture', 'content': 'Designing scalable networks', 'date_posted': 'September 29, 2024'},
    {'author': 'cloud-computing-specialist', 'title': 'Cloud Computing', 'content': 'Migration strategies', 'date_posted': 'September 30, 2024'},
    {'author': 'devops-engineer', 'title': 'DevOps Practices', 'content': 'Continuous integration', 'date_posted': 'October 1, 2024'},
    {'author': 'information-security-analyst', 'title': 'Information Security', 'content': 'Risk management', 'date_posted': 'October 2, 2024'},
    {'author': 'computer-vision-engineer', 'title': 'Computer Vision', 'content': 'Image processing', 'date_posted': 'October 3, 2024'},
    {'author': 'natural-language-processing-engineer', 'title': 'NLP Fundamentals', 'content': 'Text analysis', 'date_posted': 'October 4, 2024'},
    {'author': 'robotics-engineer', 'title': 'Robotics and Automation', 'content': 'Machine learning applications', 'date_posted': 'October 5, 2024'},
    {'author': 'data-analyst', 'title': 'Data Analysis', 'content': 'Data visualization', 'date_posted': 'October 6, 2024'},
    {'author': 'business-intelligence-developer', 'title': 'Business Intelligence', 'content': 'Data warehousing', 'date_posted': 'October 7, 2024'},
    {'author': 'full-stack-developer', 'title': 'Full Stack Development', 'content': 'Front-end and back-end development', 'date_posted': 'October 8, 2024'},
    {'author': 'quality-assurance-engineer', 'title': 'Quality Assurance', 'content': 'Testing methodologies', 'date_posted': 'October 9, 2024'}
]
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {'posts': posts} # passing the context for the template so that the data can be used
    return render(request, 'blog/home.html', context=context) # specifying the app directory under which blog specific templates are stored

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')