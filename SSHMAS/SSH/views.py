import json, traceback, re, random
from datetime import datetime
from django.contrib import messages
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from SSH.models import *


def patient_portal(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            pat_user = request.session['user']
            try:
                user = patient.objects.get(username=pat_user)
            except:
                user = None
            if user:
                context = {
                    'name': user.username,
                }
                templates = 'patient_portal.html'
                return render(request, templates, context)
            else:
                context = {
                    'errmsg': "You must be loggedIn",
                }
                return redirect('/pat_login/', context)
        else:
            context = {
                'errmsg': "You must be loggedIn",
            }
            return redirect('/pat_login/', context)


def doctor_portal(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            doc_user = request.session['user']
            try:
                user = doctor.objects.get(username=doc_user)
            except:
                user = None
            if user:
                context = {
                    'name': user.username,
                }
                templates = 'doctor_portal.html'
                return render(request, templates, context)
            else:
                context = {
                    'errmsg': "You must be loggedIn",
                }
                return redirect('/doc_login/', context)
        else:
            context = {
                'errmsg': "You must be loggedIn",
            }
            return redirect('/doc_login/', context)


def patient_reg(request):
    # understood
    assert isinstance(request, HttpRequest)
    # this will load a blank form for GEt method.
    if request.method == 'GET':
        context = locals()
        templates = "patient_reg.html"
        return render(request, templates, context)
    # this will load collects the post data from the form into the database
    elif request.method == 'POST':
        pat_fname = request.POST.get('firstname')
        pat_lname = request.POST.get('lastname')
        pat_email = request.POST.get('email')
        pat_gender = request.POST.get('gender')
        pat_phone = request.POST.get('phone')
        pat_age = request.POST.get('age')
        pat_state = request.POST.get('state')
        pat_local = request.POST.get('local')
        pat_address = request.POST.get('address')
        pat_user = request.POST.get('username')
        pat_password = request.POST.get('password')
            # the below did not work.....
        if pat_state == "Abuja":
            pat_local = request.POST.get('a')
        elif pat_state == "Abia":
            pat_local = request.POST.get('b')
        elif pat_state == "Adamawa":
            pat_local = request.POST.get('c')
        elif pat_state == "AkwaIbom":
            pat_local = request.POST.get('d')
        elif pat_state == "Anambra":
            pat_local = request.POST.get('e')
        elif pat_state == "Bauchi":
            pat_local = request.POST.get('f')
        elif pat_state == "Bayelsa":
            pat_local = request.POST.get('g')
        elif pat_state == "Benue":
            pat_local = request.POST.get('h')
        elif pat_state == "Bornu":
            pat_local = request.POST.get('i')
        elif pat_state == "CrossRiver":
            pat_local = request.POST.get('j')
        elif pat_state == "Delta":
            pat_local = request.POST.get('k')
        elif pat_state == "Ebonyi":
            pat_local = request.POST.get('l')
        elif pat_state == "Edo":
            pat_local = request.POST.get('m')
        elif pat_state == "Ekiti":
            pat_local = request.POST.get('n')
        elif pat_state == "Enugu":
            pat_local = request.POST.get('o')
        elif pat_state == "Gombe":
            pat_local = request.POST.get('p')

        elif pat_state == "Imo":
            pat_local = request.POST.get('q')
        elif pat_state == "Jigawa":
            pat_local = request.POST.get('r')
        elif pat_state == "Kaduna":
            pat_local = request.POST.get('s')
        elif pat_state == "Kano":
            pat_local = request.POST.get('t')
        elif pat_state == "Katsina":
            pat_local = request.POST.get('u')
        elif pat_state == "Kebbi":
            pat_local = request.POST.get('v')
        elif pat_state == "Kogi":
            pat_local = request.POST.get('w')
        elif pat_state == "Kwara":
            pat_local = request.POST.get('x')

        elif pat_state == "Lagos":
            pat_local = request.POST.get('y')
        elif pat_state == "Nasarawa":
            pat_local = request.POST.get('z')
        elif pat_state == "Niger":
            pat_local = request.POST.get('ab')
        elif pat_state == "Ogun":
            pat_local = request.POST.get('ac')
        elif pat_state == "Ondo":
            pat_local = request.POST.get('ad')
        elif pat_state == "Osun":
            pat_local = request.POST.get('ae')
        elif pat_state == "Oyo":
            pat_local = request.POST.get('af')
        elif pat_state == "Plateau":
            pat_local = request.POST.get('ag')

        elif pat_state == "Rivers":
            pat_local = request.POST.get('ah')
        elif pat_state == "Sokoto":
            pat_local = request.POST.get('ai')
        elif pat_state == "Taraba":
            pat_local = request.POST.get('aj')
        elif pat_state == "Yobe":
            pat_local = request.POST.get('ak')
        elif pat_state == "Zamfara":
            pat_local = request.POST.get('al')

        pat_password = request.POST.get('password')
        # this try method is to get the email and the phone numbers into variable
        try:
            rst = patient.objects.get(email=pat_email)
            rstp = patient.objects.get(email=pat_phone)
        except:
            rst = None
            rstp = None
            # the re used here was imported...for matching the regular expression with the email
            # collected from the user for proper validation.
        match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                         + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", pat_email)
        if not rst and match is not None:
            # if the email and match is not empty and existing in the database before.
            # the the patient table is assigned to a sup variable for saving the data collecting
            # the bio data saved from the form of the patients.
            sup = patient()
            sup.firstname = pat_fname
            sup.lastname = pat_lname
            sup.email = pat_email
            # if the phone number is not existing in the dB before then save the below data also...
            if not rstp:
                sup.phone = pat_phone
                sup.address = pat_address
                sup.state = pat_state
                sup.age = pat_age
                sup.local_govt = pat_local
                sup.username = pat_user
                sup.password = pat_password
                sup.gender = pat_gender
                sup.save()
                context = {
                    'successmsg': "Registration successfull Continue to login",
                    'user': request.POST.get('email'),
                }
                templates = 'patient_reg.html'
                return render(request, templates, context)
            else:
                # this section means the phone number exists so the form will not valid...
                print("false")
                context = {
                    'errmsg': "Phone Number Already Exit or Invalid Phone Number",
                }
                templates = 'patient_reg.html'
                return render(request, templates, context)
        else:
            # remember we have already checked for the validation of the email above and for its existence...
            print("damn")
            context = {
                'errmsg': "Email Already Exit or Invalid Email",
            }
            templates = 'patient_reg.html'
            return render(request, templates, context)


def doctor_reg(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = "doctor_reg.html"
        return render(request, templates, context)
    elif request.method == 'POST':
        doc_fname = request.POST.get('firstname')
        doc_lname = request.POST.get('lastname')
        doc_email = request.POST.get('email')
        doc_gender = request.POST.get('gender')
        doc_phone = request.POST.get('phone')
        doc_age = request.POST.get('age')
        doc_state = request.POST.get('state')
        doc_local = request.POST.get('local')
        doc_specialty = request.POST.get('specialty')
        doc_address = request.POST.get('address')
        doc_user = request.POST.get('username')
        doc_password = request.POST.get('password')

        if doc_state == "Abuja":
            doc_local = request.POST.get('a')
        elif doc_state == "Abia":
            doc_local = request.POST.get('b')
        elif doc_state == "Adamawa":
            doc_local = request.POST.get('c')
        elif doc_state == "AkwaIbom":
            doc_local = request.POST.get('d')
        elif doc_state == "Anambra":
            doc_local = request.POST.get('e')
        elif doc_state == "Bauchi":
            doc_local = request.POST.get('f')
        elif doc_state == "Bayelsa":
            doc_local = request.POST.get('g')
        elif doc_state == "Benue":
            doc_local = request.POST.get('h')
        elif doc_state == "Bornu":
            doc_local = request.POST.get('i')
        elif doc_state == "CrossRiver":
            doc_local = request.POST.get('j')
        elif doc_state == "Delta":
            doc_local = request.POST.get('k')
        elif doc_state == "Ebonyi":
            doc_local = request.POST.get('l')
        elif doc_state == "Edo":
            doc_local = request.POST.get('m')
        elif doc_state == "Ekiti":
            doc_local = request.POST.get('n')
        elif doc_state == "Enugu":
            doc_local = request.POST.get('o')
        elif doc_state == "Gombe":
            doc_local = request.POST.get('p')

        elif doc_state == "Imo":
            doc_local = request.POST.get('q')
        elif doc_state == "Jigawa":
            doc_local = request.POST.get('r')
        elif doc_state == "Kaduna":
            doc_local = request.POST.get('s')
        elif doc_state == "Kano":
            doc_local = request.POST.get('t')
        elif doc_state == "Katsina":
            doc_local = request.POST.get('u')
        elif doc_state == "Kebbi":
            doc_local = request.POST.get('v')
        elif doc_state == "Kogi":
            doc_local = request.POST.get('w')
        elif doc_state == "Kwara":
            doc_local = request.POST.get('x')

        elif doc_state == "Lagos":
            doc_local = request.POST.get('y')
        elif doc_state == "Nasarawa":
            doc_local = request.POST.get('z')
        elif doc_state == "Niger":
            doc_local = request.POST.get('ab')
        elif doc_state == "Ogun":
            doc_local = request.POST.get('ac')
        elif doc_state == "Ondo":
            doc_local = request.POST.get('ad')
        elif doc_state == "Osun":
            doc_local = request.POST.get('ae')
        elif doc_state == "Oyo":
            doc_local = request.POST.get('af')
        elif doc_state == "Plateau":
            doc_local = request.POST.get('ag')

        elif doc_state == "Rivers":
            doc_local = request.POST.get('ah')
        elif doc_state == "Sokoto":
            doc_local = request.POST.get('ai')
        elif doc_state == "Taraba":
            doc_local = request.POST.get('aj')
        elif doc_state == "Yobe":
            doc_local = request.POST.get('ak')
        elif doc_state == "Zamfara":
            doc_local = request.POST.get('al')

        doc_password = request.POST.get('password')
        try:
            rst = doctor.objects.filter(email=doc_email)
            rstp = doctor.objects.filter(phone=doc_phone)
            res = doctor.objects.filter(username=doc_user)
            rs = doctor.objects.filter(password=createHash(doc_password))
        except:
            rst = None
            rstp = None
            res = None
            rs = None
        match = re.match("^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@"
                         + "[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$", doc_email)
        if not rst and match is not None:
            sup = doctor()
            sup.firstname = doc_fname
            sup.lastname = doc_lname
            sup.email = doc_email
            if not res:
                if not rs:
                    if not rstp:
                        sup.phone = doc_phone
                        sup.address = doc_address
                        sup.state = doc_state
                        sup.age = doc_age
                        sup.status = "Unavailable" # saving unvailable as the default here...
                        sup.local_govt = doc_local
                        sup.speciality = doc_specialty
                        sup.username = doc_user
                        sup.password = doc_password
                        sup.gender = doc_gender
                        sup.save()
                        print('here to stay')
                        context = {
                            'successmsg': "Registration successfull Continue to login",
                            'user': request.POST.get('email'),
                        }
                        templates = 'doctor_reg.html'
                        return render(request, templates, context)
                    else:
                        print("false")
                        context = {
                            'errmsg': "Phone Number Already Exist or Invalid Phone Number",
                        }
                        templates = 'doctor_reg.html'
                        return render(request, templates, context)
                else:
                    print("false")
                    context = {
                        'errmsg': "Password Already Exist or Invalid Password",
                    }
                    templates = 'doctor_reg.html'
                    return render(request, templates, context)
            else:
                print("false")
                context = {
                    'errmsg': "Username Already Exist",
                }
                templates = 'doctor_reg.html'
                return render(request, templates, context)
        else:
            print("damn")
            context = {
                'errmsg': "Email Already Exit or Invalid Email",
            }
            templates = 'doctor_reg.html'
            return render(request, templates, context)


def pat_upload(request, pat_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if request.FILES['image']:
            pat_image = request.FILES['image']
            prof = patient.objects.get(username=request.session['user'])
            pat_user = request.session['user']

            # if pat_image condition exists then carry out the try method.
            if pat_image:
                try:
                    d = patient.objects.get(id=pat_id)
                except:
                    d = None
                # an error occurred here there is no field as image for the patient.
                # d.upload = pat_image. that is the current function here...
                d.image = pat_image
                d.save()
                context = {
                    'msg': "image uploaded successfully"
                }
                templates = 'user_profile.html'
                return render(request, templates, context)
        else:
            context = {
                'msg': "Image can't be empty"
            }
            templates = 'user_profile.html'
            return render(request, templates, context)
    else:
        redirect('/user_profile/')


def doc_login(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'doc_login.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        try:
            user = request.POST.get('username')
            sql = doctor.objects.get(username=user)
        except:
            print(traceback.print_exc())
            sql = None
        if sql:
            pass1 = request.POST.get('password')
            if sql.password == createHash(pass1):
                request.session['email'] = sql.email
                request.session['user'] = sql.username
                request.session['userid'] = sql.id
                context = {
                    'mail': sql.email,
                    'name': sql.firstname,
                }
                templates = 'doctor_portal.html'
                return render(request, templates, context)
            else:
                context = {
                    'errmsg': "Sorry!! Invalid Password or Password doesn't Exist",
                }
                templates = 'doc_login.html'
                return render(request, templates, context)
        else:
            context = {
                'errmsg': "Sorry!! Invalid Username or Username doesn't Exist",
            }
            templates = 'doc_login.html'
            return render(request, templates, context)


def pat_login(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'pat_login.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        try:
            user = request.POST.get('username')
            sql = patient.objects.get(username=user)
        except:
            print(traceback.print_exc())
            sql = None
        if sql:
            if sql.password == createHash(request.POST.get('password')):
                request.session['email'] = sql.email
                request.session['user'] = sql.username
                request.session['userid'] = sql.id
                context = {
                    'mail': sql.email,
                    'name': sql.username,
                }
                templates = 'patient_portal.html'
                return render(request, templates, context)
            else:
                context = {
                    'errmsg': "Sorry!! Invalid Password or Password doesn't Exist",
                }
                templates = 'pat_login.html'
                return render(request, templates, context)
        else:
            context = {
                'errmsg': "Sorry!! Invalid Username or Username doesn't Exist",
            }
            templates = 'pat_login.html'
            return render(request, templates, context)


def user_profile(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                prof = patient.objects.get(username=request.session['user'])
            except:
                prof = None
            pat_user = request.session['user']
            if prof:
                context = {
                    'profile': prof,
                    'name': pat_user,
                }
                templates = 'user_profile.html'
                return render(request, templates, context)
            else:
                # after checking the user's username in the session as a means of authentication with
                # the one in the database then its means the users is not authenticated.
                return redirect('/pat_login/')
        else:
            # if user is not authenticated then go back to login to get verified first.
            return redirect('/pat_login/')

    # this Post method below is used to to collect another form's data for editing profile...
    if request.method == 'POST':
        if 'user' in request.session:
            pat_image = request.FILES['image']
            pat_fname = request.POST.get('firstname')
            pat_lname = request.POST.get('lastname')
            pat_email = request.POST.get('email')
            pat_gender = request.POST.get('gender')
            pat_phone = request.POST.get('phone')
            pat_age = request.POST.get('age')
            pat_state = request.POST.get('state')
            pat_local = request.POST.get('local')
            pat_address = request.POST.get('address')
            prof = patient.objects.get(username=request.session['user'])
            pat_user = request.session['user']

            if pat_image:
                try:
                    d = patient.objects.get(username=pat_user)
                except:
                    d = None
                if d:
                    d.upload = pat_image
                    d.save()
                    print('am here')
                    context = {
                        'msg': "image uploaded successfully",
                        'profile': prof,
                    }
                    return redirect('/user_profile', context)
                else:
                    context = {
                        'msg': "image uploaded not successful",
                        'profile': prof,
                    }
                    return redirect('/user_profile/', context)

            # this else supposed to mean if the pat_image is not set.....then do the following below.
            else:
                try:
                    d = patient.objects.get(username=pat_user)
                except:
                    d = None

                # if the username is gotten...then the patient information is re-assigned.
                if d:
                    d.firstname = pat_fname
                    d.lastname = pat_lname
                    d.email = pat_email
                    d.phone = pat_phone
                    d.address = pat_address
                    d.state = pat_state
                    d.age = pat_age
                    d.local_govt = pat_local
                    d.gender = pat_gender
                    d.save()
                    print('am here')
                    context = {
                        'msg': "Profile successfully Updated",
                        'profile': prof,
                    }
                    templates = 'user_profile.html'
                    return render(request, templates, context)
                else:
                    context = {
                        'msg': "Profile Update not successful",
                        'profile': prof,
                    }
                    templates = 'user_profile.html'
                    return render(request, templates, context)
        else:
            prof = patient.objects.get(username=request.session['user'])
            context = {
                'msg': "Image can't be empty",
                'profile': prof,
            }
            templates = 'user_profile.html'
            return render(request, templates, context)


def doc_profile(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                prof = doctor.objects.get(username=request.session['user'])
            except:
                prof = None
            doc_user = request.session['user']
            if prof:
                context = {
                    'profile': prof,
                    'name': doc_user,
                }
                templates = 'doc_profile.html'
                return render(request, templates, context)
            else:
                return redirect('/doc_log/')
        else:
            return redirect('/doc_log/')

   # this condition is use for editing and updating the doctor's profile.

    elif request.method == 'POST':
        if 'user' in request.session:
            doc_user = request.session['user']
            prof = doctor.objects.get(username=request.session['user'])
            doc_fname = request.POST.get('firstname')
            doc_lname = request.POST.get('lastname')
            doc_email = request.POST.get('email')
            doc_gender = request.POST.get('gender')
            doc_phone = request.POST.get('phone')
            doc_age = request.POST.get('age')
            doc_state = request.POST.get('state')
            doc_local = request.POST.get('local')
            doc_address = request.POST.get('address')
            doc_specialty = request.POST.get('specialty')
            try:
                d = doctor.objects.get(username=doc_user)
            except:
                d = None
            # now the information edited/updated above is being saved into the database...
            if d:
                d.firstname = doc_fname
                d.lastname = doc_lname
                d.email = doc_email
                d.phone = doc_phone
                d.address = doc_address
                d.state = doc_state
                d.age = doc_age
                d.local_govt = doc_local
                d.gender = doc_gender
                d.specialty = doc_specialty
                d.save()
                print('am here')
                context = {
                    'msg': "Profile successfully Updated",
                    'profile': prof,
                }
                templates = 'doc_profile.html'
                return render(request, templates, context)
            else:
                context = {
                    'msg': "Profile Update not successful",
                    'profile': prof,
                }
                templates = 'doc_profile.html'
                return render(request, templates, context)
        else:
            context = {
                'msg': "You must be loggedIn",
            }
            return redirect('/doc_log/', context)


def doc_upload(request):
    if request.method == 'POST':
        if 'user' in request.session:
            doc_user = request.session['user']
            prof = doctor.objects.get(username=request.session['user'])
            doc_image = request.FILES['image']
            if doc_image:
                try:
                    d = doctor.objects.get(username=doc_user)
                except:
                    d = None
                if d:
                    d.image1 = doc_image
                    d.save()
                    print('am here')
                    context = {
                        'msg': "image uploaded successfully",
                        'profile': prof,
                    }
                    return redirect('/doc_profile/', context)
            else:
                context = {
                    'msg': "image uploaded not successful",
                    'profile': prof,
                }
                return redirect('/doc_profile/', context)


def doc_status(request):
    if request.method == 'POST':
        # we first need to authenticate the user username trying to access the page..
        if 'user' in request.session:
            doc_user = request.session['user']
            prof = doctor.objects.get(username=request.session['user'])
            doc_status = request.POST.get('status')
            if doc_status:
                try:
                    d = doctor.objects.get(username=doc_user)
                except:
                    d = None
                if d:
                    d.status = doc_status
                    d.save()
                    print('am here')
                    # first don't know the fuck why is printing everything out here ...
                    # second error error error!!! it should be status updated successfully not image...
                    context = {
                        'msg': "image uploaded successfully",
                        'profile': prof,
                    }
                    return redirect('/doc_profile/', context)
            else:
                context = {
                    'msg': "image uploaded not successful",
                    'profile': prof,
                }
                return redirect('/doc_profile/', context)


def book(request, doc_id):
    if request.method == 'GET':
        # authenticating the doctor in the request session.
        if 'user' in request.session:
            try:
                details = doctor.objects.get(id=doc_id)
            except:
                details = None
            if details:
                context = {
                    'i': details,
                }
                templates = 'book.html'
                return render(request, templates, context)
    # if the patient is booking here using form.....
    elif request.method == 'POST':
        if 'user' in request.session:
            today = str(datetime.now())[:10]  # slicing the datetime format and reducing it to just the date...smart
            print(today)
            # authenticating the user...
            pat_user = request.session['user']
            f = patient.objects.get(username=pat_user)
            pfirst = f.firstname
            plast = f.lastname

            # my assumption is here is that this are this name of post parameters..in python strings.
            name = request.POST.get('doc')
            fname = request.POST.get('first')
            lname = request.POST.get('last')
            print(name)
            bk_date = request.POST.get('date_name')
            bk_time = request.POST.get('time_name')
            bk_message = request.POST.get('app_message')
            try:
                con1 = appointment.objects.get(docname=name, apptime=bk_time, appdate=bk_date)
            except:
                con1 = None
            if bk_date == today:
                if con1:
                    try:
                        details = doctor.objects.get(id=doc_id)
                    except:
                        details = None
                    if details:
                        context = {
                            'i': details,
                            'success': "This time schedule has been fixed for an appointment",
                        }
                        templates = 'book.html'
                        return render(request, templates, context)
                    else:
                        context = {
                            'success': "Error",
                        }
                        templates = 'book.html'
                        return render(request, templates, context)
                elif not con1:
                    dot = appointment()
                    # saving the appointment posted data into the DB
                    dot.apptime = bk_time
                    dot.appdate = bk_date
                    dot.patname = pat_user
                    dot.docname = name
                    dot.patfirst = pfirst
                    dot.patlast = plast
                    dot.docfirst = fname
                    dot.doclast = lname
                    dot.appmessage = bk_message
                    dot.save()
                    print('am here')
                    try:
                        details = doctor.objects.get(id=doc_id)
                    except:
                        details = None
                    if details:
                        context = {
                            'i': details,
                            'success': "Your appointment has been submitted successfully,Kindly wait for doctor approval",
                        }
                        templates = 'book.html'
                        return render(request, templates, context)
                    else:
                        context = {
                            'i': details,
                            'success': "Error",
                        }
                        templates = 'book.html'
                        return render(request, templates, context)
            else:
                try:
                    details = doctor.objects.get(id=doc_id)
                except:
                    details = None
                if details:
                    context = {
                        'i': details,
                        'success': "Appointment date is not correct,Kindly choose today's date",
                    }
                    templates = 'book.html'
                    return render(request, templates, context)


def doc_confirm(request, con_id):
    assert isinstance(request, HttpResponse)
    if request.method == 'POST':
        if 'email' in request.session['email']:
            try:
                con = appointment.objects.get(id=con_id)
            except:
                con = None
            st_con = request.POST.get('confirm')
            if con:
                con.status = st_con
                con.save()
                context = {
                    'success': "Your have successfully confirmed the appointment",
                }
                templates = 'booking.html'
                return render(request, templates, context)
            else:
                context = {
                    'success': "Invalid Data",
                }
                templates = 'booking.html'
                return render(request, templates, context)


def delete_app(request, del_id):
    assert isinstance(request, HttpResponse)
    if request.method == 'GET':
        try:
            app = appointment.objects.get(id=del_id)
        except:
            app = None
        del app
        context = {
            'success': "Invalid Data",
        }
        templates = 'myappointment.html'
        return render(request, templates, context)


def forget_pass(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'forget_pass.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        user_name = request.POST.get('username')
        try:
            user = patient.objects.get(username=user_name)
        except:
            user = None
        if user is not None:
            request.session['user'] = user.username
            request.session['userid'] = user.id
            messages.error(request, 'Username Verified ,Kindly Enter Your New Password')
            return redirect('/change_pass/', request.session['user'], request.session['userid'])
        else:
            context = {
                'msg': "Username not verified",
            }
            return redirect('/forget_pass/', context)


def change_pass(request):
    if request.method == 'GET':
        context = locals()
        templates = 'change_pass.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        rest_pass = request.POST.get('pass')
        user = request.session['user']
        userid = request.session['userid']
        try:
            u_pass = patient.objects.get(username=user)
        except:
            u_pass = None
        if u_pass:
            u_pass.password = createHash(rest_pass)
            i = u_pass.password
            u_pass.save()
            context = {
                'success': "Password Reset Successfully"
            }
            templates = 'success.html'
            return render(request, templates, context)
        else:
            context = {
                'errmsg': "Password Reset Not Successfully try Again",
            }
            return redirect('/forget_pass/', context)


def new_appointment(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        # this checks if the doctor is still active in its own session.....i.e if he/she is login.
        if 'user' in request.session:
            sel = doctor.objects.filter(status="Available")
            if sel:
                context = {
                    'avail': sel,
                }
                templates = 'new_appointment.html'
                return render(request, templates, context)
            else:
                context = {
                    'notavail': "Doctors Are currently on leave",
                }
                templates = 'new_appointment.html'
                return render(request, templates, context)
        else:
            return redirect('/pat_login/')


def success(request):
    if request.method == 'GET':
        context = locals()
        templates = 'success.html'
        return render(request, templates, context)


def view_appointment(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                # this returns a queryset of online patients that book appointments...
                view = appointment.objects.filter(patname=request.session['user'])
            except:
                view = None
            if view:
                context = {
                    'v': view,
                }
                templates = 'view_appointment.html'
                return render(request, templates, context)
            else:
                context = {
                    'b': "No appointment booked",
                }
                templates = 'view_appointment.html'
                return render(request, templates, context)
        else:
            return redirect('/pat_login/')


def doc_view(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            try:
                vid = appointment.objects.filter(docname=request.session['user'])
                details = doctor.objects.get(username=request.session['user'])
            except:
                vid = None
                details = None
            if vid:
                context = {
                    'v': vid,
                    'i': details,
                }
                templates = 'doc_view.html'
                return render(request, templates, context)
            else:
                context = {
                    'b': "No Appointment Booked",
                    'i': details,
                }
                templates = 'doc_view.html'
                return render(request, templates, context)
        else:
            return redirect('/doc_login/')


def confirm(request, con_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        if 'user' in request.session:
            c = request.POST.get('con')
            try:
                vid = appointment.objects.filter(docname=request.session['user'])
                p = appointment.objects.get(id=con_id)
                details = doctor.objects.get(username=request.session['user'])
            except:
                vid = None
                p = None
                details = None
            if p:
                p.status = c
                p.save()
                context = {
                    'v': vid,
                    'i': details,
                    'd': "APPROVED"
                }
                templates = 'doc_view.html'
                return render(request, templates, context)
            else:
                context = {
                    'i': details,
                    'b': "Error",
                }
                templates = 'doc_view.html'
                return render(request, templates, context)
        else:
            return redirect('/doc_login/')


def del_app(request, del_id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if 'user' in request.session:
            user = request.session['user']
            try:
                details = patient.objects.get(username=user)
            except:
                details = None
            if details:
                k = appointment.objects.get(id=del_id)
                k.delete()
                context = {
                    'b': "No Appointment Booked",
                    'i': details,
                    'name': request.session['user'],
                }
                templates = 'view_appointment.html'
                return render(request, templates, context)
            else:
                print('am here')
                return redirect('/pat_login/')
        else:
            return redirect('/pat_login/')


def pat_logout(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        del request.session['user']
        del request.session['userid']
        del request.session['email']
        return redirect('/pat_login/')


def doc_logout(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        del request.session['user']
        del request.session['userid']
        del request.session['email']
        return redirect('/doc_login/')
