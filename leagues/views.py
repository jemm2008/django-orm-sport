from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

#from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"Baseball_Leagues": League.objects.filter(sport='Baseball'),					# 1
		"women_leagues": League.objects.filter(name__icontains='women'),				# 2
		"any_hockey": League.objects.filter(sport__icontains='hockey'),					# 3
		"sport_not_football": League.objects.exclude(name__icontains="football"),		# 4
		"named_conference": League.objects.all().filter(name__icontains='conference'),	# 5
		"atlantic_leagues": League.objects.all().filter(name__icontains='atlantic'),	# 6

		"teams": Team.objects.all(),
		"dallas_teams": Team.objects.filter(location='Dallas'),							# 7
		"raptors_teams": Team.objects.all().filter(team_name__icontains='raptors'),		# 8
		"city_in_location_teams": Team.objects.filter(location__icontains='city'),		# 9
		"t_teams": Team.objects.filter(team_name__startswith='T'),						#10
		"teams_loc_alphab_order": Team.objects.all().order_by('location', 'team_name'),	#11
		"teams_name_rev_ord": Team.objects.all().order_by('-team_name'),				#12

		"players": Player.objects.all(),
		"cooper_last_name": Player.objects.filter(last_name__contains='Cooper'),		#13
		"joshua_first_name": Player.objects.filter(first_name__contains='Joshua'),		#14
		"cooper_not_joshua": Player.objects.filter(last_name__contains='Cooper').exclude(first_name='Joshua'),				#15
		"alexander_or_wyatt": Player.objects.filter(Q(first_name__contains='Alexander')|Q(first_name__contains='Wyatt')), 	#16
	}
	return render(request, "leagues/index.html", context)




#def make_data(request):
#	team_maker.gen_leagues(10)
#	team_maker.gen_teams(50)
#	team_maker.gen_players(200)
#
#	return redirect("index")