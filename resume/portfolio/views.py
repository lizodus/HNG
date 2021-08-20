from django.http.response import BadHeaderError, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail





def home_page(request):
    template_name = "portfolio/homepage.html"
    return render(request, template_name)


def about_me(request):
    template_name = "portfolio/about.html"
    return render(request, template_name)


def project_view(request):
    template_name = "portfolio/project.html"
    return render(request, template_name)



def contact_me(request):
    template_name = "portfolio/contact_us.html"
    if request.method == "POST":
        sender_email = request.POST.get("sender-email",)
        subject = request.POST.get("subject-body",)
        message = request.POST.get("message-body",)
        

        if sender_email and subject and message:
            try:
                send_mail(from_email=sender_email, subject=subject, message=message, recipient_list=[str("aayobam@gmail.com")], fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            messages.success(request, f"Mail sent successfuly")
            return redirect("home-page")
        else:
            return HttpResponse("Make sure all the fields enterred are valid")
    else:
        template_name = "portfolio/contact_us.html"
    return render(request, template_name)
                
