from django.db.models.aggregates import Count
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

		"teams_atlantic_soccer": Team.objects.filter(league__name='Atlantic Soccer Conference'),											#01B
		"act_players_bostonpenguins": Player.objects.filter(Q(curr_team__location='Boston')&Q(curr_team__team_name='Penguins')), 			#02B
		"act_players_intcoll_baseballconf": Player.objects.filter(curr_team__league__name='International Collegiate Baseball Conference'),	#03B
		"lopez_player":  Player.objects.filter(curr_team__league__name='American Conference of Amateur Football').filter(last_name__icontains='lopez'),	#04B
		"football_players": Player.objects.filter(curr_team__league__sport__icontains='football'),		#05B
		"sophia_teams": Team.objects.filter(curr_players__first_name='Sophia'),        					#06B
		"sophia_leagues": League.objects.filter(teams__curr_players__first_name='Sophia'),      		#07B
		"flores_not_in_wa_rriders": Player.objects.filter(last_name='Flores').exclude(curr_team__location='Washington',curr_team__team_name='Roughriders'), #08B
		"samevans_all_teams": Team.objects.filter(all_players__first_name='Samuel',all_players__last_name='Evans'),						#09B
		"allplayers_manitoba_tigercats": Player.objects.filter(all_teams__location='Manitoba', all_teams__team_name='Tiger-Cats'),		#10B
		"past_players_wichita_vikings": Player.objects.filter(all_teams__location='Wichita',all_teams__team_name='Vikings').exclude(curr_team__location='Wichita', curr_team__team_name='Vikings'), #11B
		"jgray_teams_before_ocolts": Team.objects.filter(all_players__first_name='Jacob', all_players__last_name='Gray').exclude(location="Oregon", team_name="Colts" ),	#12B
		"alljoshua_fed_atl_baseball": Player.objects.filter(all_teams__league__name='Atlantic Federation of Amateur Baseball Players',first_name='Joshua'),				#13B
		"teams_more12players": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte = 12),	#14B
		"allplayers_with_teams": Player.objects.annotate(num_teams=Count('all_teams')).order_by('-num_teams'),


	}
	return render(request, "leagues/index.html", context)




#def make_data(request):
#	team_maker.gen_leagues(10)
#	team_maker.gen_teams(50)
#	team_maker.gen_players(200)
#
#	return redirect("index")