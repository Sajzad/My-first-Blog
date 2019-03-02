from django.shortcuts import render

def my_info(request):
	print("request data: ", request.POST)
	if request.method=='POST':
		x=request.POST["user"]
		y={"name":x}
	return render(request,'my_form/u_s_form.html',y)
# Create your views here.
