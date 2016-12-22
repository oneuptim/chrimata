from django.shortcuts import render, redirect
from django.contrib import messages
from . import models


# def welcome(request):
#     return render(request, 'chrimata_app/index.html')

def index(request):
    if not 'active_user' in request.session:
        request.session['active_user'] = ""
    return render(request, 'chrimata_app/index.html')

def login_and_reg(request):
    return render(request, 'chrimata_app/login_and_registration.html')

def gold_detail_view(request):
    return render (request, 'chrimata_app/gold_detail_view.html')

def dashboard(request, methods='POST'):
    if not 'active_user' in request.session or request.session['active_user']=="":
        messages.add_message(request, messages.ERROR, "Please Login to Continue")
        return redirect('/auth')
    favorites_list = models.Favorite.objects.filter(user_id=request.session['active_user']['id'])
    investments_list = models.Investment.objects.exclude(favorite__user_id=request.session['active_user']['id'])
    initial_investment = request.POST.get('initial_investment', False)
    print initial_investment, "000"*100
    if not favorites_list:
        context = {
            'investments_list': investments_list,
        }
        return render(request, 'chrimata_app/dashboard.html', context)
    sum = 0
    sum_volatility = 0
    sum_min = 0
    for fav in favorites_list:
        sum += int(fav.investment.total_gain_loss)
        sum_volatility += int(fav.investment.total_volatility)
        sum_min += int(fav.investment.min_investment)
    avg = sum/len(favorites_list)
    avg_volatility = sum_volatility/len(favorites_list)
    fiveyearreturn = avg * int(initial_investment)
    context = {
        'investments_list': investments_list,
        'favorites_list': favorites_list,
        'avg': avg,
        'fiveyearreturn': fiveyearreturn,
        'initial_investment': initial_investment,
        'avg_volatility': avg_volatility,
        'sum_min':sum_min
    }
    return render (request, 'chrimata_app/dashboard.html', context)

def markets(request):
    return render (request, 'chrimata_app/markets.html')

def stocks(request):
    return render (request, 'chrimata_app/stocks.html')

def commodities(request):
    return render (request, 'chrimata_app/commodities.html')

def cryptocurrencies(request):
    return render (request, 'chrimata_app/cryptocurrencies.html')

def crypto(request):
    return render (request, 'chrimata_app/crypto.html')

def real_estate(request):
    return render (request, 'chrimata_app/real_estate.html')

def apple(request):
    return render (request, 'chrimata_app/apple.html')

def google(request):
    return render (request, 'chrimata_app/google.html')

def berkshire(request):
    return render (request, 'chrimata_app/berkshire.html')

def gold(request):
    return render (request, 'chrimata_app/gold.html')

def natural_gas(request):
    return render (request, 'chrimata_app/natural_gas.html')

def corn(request):
    return render (request, 'chrimata_app/corn.html')

def bitcoin(request):
    return render (request, 'chrimata_app/bitcoin.html')

def ethereum(request):
    return render (request, 'chrimata_app/ethereum.html')

def monero(request):
    return render (request, 'chrimata_app/monero.html')

def bonds(request):
    return render (request, 'chrimata_app/bonds.html')

def supersecret(request):
    investments_list = models.Investment.objects.all()
    context = {
        'investments_list': investments_list
    }
    return render (request, 'chrimata_app/secret.html', context)

def add_user(request):
    result = models.User.objects.register(request.POST)
    if result[0] == False:
        for i in result[1]:
            messages.add_message(request, messages.ERROR, i)
        return redirect('/auth')
    else:
        return log_user_in(request, result[1])

def login(request):
    result = models.User.objects.login(request.POST)
    if result[0] == False:
        for i in result[1]:
            messages.add_message(request, messages.ERROR, i)
        return redirect('/auth')
    else:
        return log_user_in(request, result[1])

def log_user_in(request, user):
    request.session['active_user'] = {
        'id' : user.id,
        'name' : user.name,
        'alias' : user.alias,
        'email' : user.email,
    }
    return redirect ('/dashboard')

def logout(request):
    del request.session['active_user']
    return redirect('/')

# End of Login ***************

def add_investment(request):
    result = models.Investment.objects.add_investment(request.POST)
    if result[0] == False:
        for i in result[1]:
            messages.add_message(request, messages.ERROR, i)
    return redirect('/supersecret')

def add_favorite(request, id):
    result = models.Favorite.objects.add_favorite(request.session['active_user']['id'],id)
    return redirect('/dashboard')

def remove_favorite(request, id):
    result = models.Favorite.objects.remove_favorite(request.session['active_user']['id'],id)
    result[1].delete()
    return redirect('/dashboard')
