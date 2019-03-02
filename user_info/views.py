from django.shortcuts import render

def user_details(request):
	print("request data:", request.POST)
	if request.method=='POST':
		u_s_value=request.POST["user_name"]
		context={"name": u_s_value}
		return render(request,'info/user_info.html',context)
	return render(request,'info/user_info.html')



	

# Create your views here.
