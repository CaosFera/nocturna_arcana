


from account.decorators import check_user_able_to_see_page
from .models import Profile


def profile_exists(request):
    profile_exists = None
    try:
        if Profile.objects.filter(user=request.user).exists(): 
            profile_exists = True
        else:
            profile_exists = False        
    except:
        pass
    return {'profile_exists': profile_exists}



def group_exists(request):
    try:
        user_groups = request.user.groups.filter(name='NOCTURNA ARCANA')
        group_exists = user_groups.exists()
    except:
        pass    
    return {'group_exists': group_exists}


    