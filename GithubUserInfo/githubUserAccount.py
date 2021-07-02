def set(username):
    import requests
    from bs4 import BeautifulSoup
    global user
    global url
    global response
    global soup
    user = username
    url = "https://github.com/"+user
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    user_tg = soup.find('span', class_='p-nickname vcard-username d-block')
    if user_tg == None:
        return "invalid username "+username

def name():
    full_name = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
    return full_name.text.strip()

def username():
    user = soup.find('span', class_='p-nickname vcard-username d-block')
    return user.text.strip()

def bio():
    bio = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
    if bio != None and bio.div != None:
        return bio.div.text

def followers():
    people = soup.find_all('span', class_='text-bold color-text-primary')
    if len(people) != 0:
        return people[0].text
    
def following():
    people = soup.find_all('span', class_='text-bold color-text-primary')
    if len(people) != 0:
        return people[1].text
    
def star():
    people = soup.find_all('span', class_='text-bold color-text-primary')
    if len(people) != 0:
        return people[2].text

def organization():
    org = soup.find('span', class_='p-org')
    if org != None:
        return org.text

def location():
    loc = soup.find('span', class_='p-label')
    if loc != None:
        return loc.text

def website():
    website = soup.find('li', class_='vcard-detail pt-1 css-truncate css-truncate-target')
    if website != None:
        return website.a['href']

def count_repositories():
    repo = soup.find('div', class_='UnderlineNav width-full box-shadow-none').find_all('span')
    return repo[0].text

def count_projects():
    proj = soup.find('div', class_='UnderlineNav width-full box-shadow-none').find_all('span')
    return proj[1].text

def info():
    print("Name:",name())
    print("Username:",username())
    print("Bio:",bio())
    print("Followers:",followers())
    print("Following:",following())
    print("Stars:",star())
    print("Organization:",organization())
    print("Location:",location())
    print("Website:",website())
    print("Repositories:",count_repositories())
    print("Projects:",count_projects())

def get(username):
    try:
        import requests
        from bs4 import BeautifulSoup

        url = 'https://github.com/'+username
    
        response = requests.get(url)
        if response.status_code != 200:
            print("Searching Failed!")
        
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            user_tg = soup.find('span', class_='p-nickname vcard-username d-block')

            if user_tg != None:
                user =  user_tg.text.strip()

                name_tg = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
                name = name_tg.text.strip()
    
                bio_tg = soup.find('div', class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
                bio = ''
                if bio_tg != None and bio_tg.div != None:
                    bio = bio_tg.div.text
    
                public_tg = soup.find_all('span', class_='text-bold color-text-primary')
                followers = 0
                followings = 0
                stars = 0
                if len(public_tg) != 0:
                    followers = public_tg[0].text
                    followings = public_tg[1].text
                    stars = public_tg[2].text
    
                org_tg = soup.find('span', class_='p-org')
                organization = ''
                if org_tg != None:
                    organization = org_tg.text
    
                loc_tg = soup.find('span', class_='p-label')
                location = ''
                if loc_tg != None:
                    location = loc_tg.text
    
                web_tg = soup.find('li', class_='vcard-detail pt-1 css-truncate css-truncate-target')
                website = ''
                if web_tg != None:
                    website = web_tg.a['href']
    
                repo_proj_tg = soup.find('div', class_='UnderlineNav width-full box-shadow-none').find_all('span')
                repositories = repo_proj_tg[0].text
                projects = repo_proj_tg[1].text

                return {
                    "name": name,
                    "username": user,
                    "bio": bio,
                    "followers": followers,
                    "followings": followings,
                    "stars": stars,
                    "organization": organization,
                    "location": location,
                    "website": website,
                    "repositories": repositories,
                    "projects": projects
                }
            else:
                return "invalid username "+username
            
    except requests.exceptions.RequestException:
        print("Connection Error")