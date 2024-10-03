from django.shortcuts import render

from django.views.generic import View

# Create your views here.

class AdditionView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"addition_form.html")
    
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("box1")
        num2=request.POST.get("box2")

        result=int(num1)+int(num2)
        print(result)
        data={"output":result}

        return render(request,"addition_form.html",data)

class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")
    
    def post(self,request,*args,**kwargs):
        height_in_cm=request.POST.get("heightbox")
        weight=request.POST.get("weightbox")
        height_in_meter=(int(height_in_cm)/100)**2
        result=(int(weight)/height_in_meter)
        data={"output":result}
        return render(request,"bmi.html",data)


class MultiplicationView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"multiplication.html")
    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        result=int(num1)*int(num2)
        data={"output":result}

        return render(request,"multiplication.html",data)

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"substraction.html")

    def post(self,request,*args,**kwargs):
        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        if (int(num1)>int(num2)):
            result=int(num1)-int(num2)
        else:
            result=int(num2)-int(num1)

        data={"output":result}

        return render(request,"substraction.html",data)

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"division.html")
    def post(self,request,*args,**kwargs):

        num1=request.POST.get("num1")
        num2=request.POST.get("num2")
        if(int(num1)>int(num2)):
            result=int(num1)/int(num2)
        else:
            result=int(num2)/int(num1)
        data={"output":result}
        return render(request,"division.html",data)

class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"factorail.html")
    def post(self,request,*args,**kwargs):
        num=request.POST.get("num")
        fact=1
        result=1
        for i in range(1,int(num)+1):
            result*=fact*i
            
        data={"output":result}
        return render(request,"factorail.html",data)

class CalorieView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"calorie.html")

    def post(self,request,*args,**kwargs):
        age=request.POST.get("agebox")
        height=request.POST.get("heightBox")
        weight=request.POST.get("weightBox")
        gender=request.POST.get("genderBox")
        activity=request.POST.get("activityBox")

        # print(f"age={age},w={weight},h={height},g={gender},a={activity}")
        if gender=="male":
            BMR=10*int(weight)+ 6.25*int(height) -5*int(age) +5
        else:
            BMR=10*int(weight)+ 6.25*int(height) -5*int(age) -161

        CALORIE=BMR*float(activity)
        data={"calorie":CALORIE}


        return render(request,"calorie.html",data)

class EmiCalculatorView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emi_calc.html")
    def post(self,request,*args,**kwargs):
        loan=request.POST.get("loan")
        interest=request.POST.get("interest")
        tenure=request.POST.get("tenure")

        p=int(loan)
        i_r=float(interest)
        n=int(tenure)
        r=float(i_r/12/100)
        
        EMI=p*r*(1+r)**n//((1+r)**n-1)
        # EMI=result
        p_a=p
        t_i=EMI*n-p_a
        print(r)
        data={
            "emi":EMI,
            "principal":p_a,
            "total_interest":t_i
        }

        return render(request,"emi_calc.html",data)

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
        
class WeightTargetView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"weight_target.html")
    def post(self,request,*args,**kwargs):
        age=request.POST.get("agebox")
        height=request.POST.get("heightbox")
        weight=request.POST.get("weightbox")
        gender=request.POST.get("genderbox")
        activity=request.POST.get("activitybox")

        
        if gender=="male":
            BMR=10*int(weight)+ 6.25*int(height) -5*int(age) +5
        else:
            BMR=10*int(weight)+ 6.25*int(height) -5*int(age) -161

        CALORIE=BMR*float(activity)
        data={"calorie":CALORIE}


        return render(request,"weight_target.html",data)





    





