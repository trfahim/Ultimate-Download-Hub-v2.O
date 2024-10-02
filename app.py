from flask import Flask, render_template, request
import requests
import time,emoji

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pc-games', methods=['GET', 'POST'])
def pc_games():
    game_found = None
    download_link_1 = None
    download_link_2 = None
    download_link_3 = None

    if request.method == 'POST':
        game_name = request.form['game_name']
        
        search_url_1 = f"https://www.apunkagames.com/{(game_name.replace(' ', '-')).lower()}/"
        response = requests.get(f'{search_url_1}').status_code
        
        search_url_2 = f"https://oceanofgames.com/{(game_name.replace(' ', '-')).lower()}/"
        response_2 = requests.get(f'{search_url_2}').status_code 
        
        search_url_3 = f"https://dodi-repacks.site/{(game_name.replace(' ', '-')).lower()}/"
        response_3 = requests.get(f'{search_url_3}').status_code
        
        
        if response == 404:
            game=0
        else:
            download_link_1 = search_url_1
            game_found = True
        
        if response_2 == 404:
            game=0
        else:
            download_link_2 = search_url_2
            game_found = True
        
        if response_3 == 404:
            game=0
        else:
            download_link_3 = search_url_3
            game_found = True
            
        if response==404 and response_2==404 and response_3==404:
            game_found = False
        else:
            game=0
    
    return render_template('pc_games.html',
                           game_found=game_found, 
                           download_link_1=download_link_1, 
                           download_link_2=download_link_2,
                           download_link_3=download_link_3,
                           )
    
@app.route('/android-games', methods=['GET', 'POST'])
def android_games():
    game_found = None
    download_link_1 = None
    download_link_2 = None
    download_link_3 = None
    
    if request.method == 'POST':
        game_name = request.form['game_name']
        
        search_url_1 = f"https://apkdone.com/{(game_name.replace(' ', '-')).lower()}/"
        response_1 = requests.get(f'{search_url_1}').status_code
        
        search_url_2 = f"https://apkpure.com/search?q={(game_name.replace(' ', '-')).lower()}"
        response_2 = requests.get(f'{search_url_2}').status_code
        
        search_url_3 = f"https://androeed.store/files/{(game_name.replace(' ', '-')).lower()}.html"
        response_3 = requests.get(f"{search_url_3}").status_code
        
        time.sleep(3)
        
        if response_1 == 404:
            game=0
        else:
            download_link_1=search_url_1
            game_found = True
        
        if response_2 == 404:
            game=0
        else:
            download_link_2=search_url_2
            game_found=True
        
        if response_3 == 404:
            game=0
        else:
            download_link_3=search_url_3
            game_found=True
        
        if response_1==404 and response_2==404 and response_3==404:
            game_found=False
        else:
            game=0
        
    return render_template('android_games.html',
                           game_found=game_found,
                           download_link_1=download_link_1,
                           download_link_2=download_link_2,
                           download_link_3=download_link_3)
    
    

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    movie_found = None
    download_link_1 = None
    download_link_2 = None
    download_link_3 = None
    download_link_4 = None
    
    if request.method == 'POST':
        movie_name = request.form['movie-name']
        
        search_url_1 = f"https://cinedoze.com/{(movie_name.replace(' ','-')).lower()}/"
        response_1 = requests.get(f'{search_url_1}').status_code
        
        search_url_2 = f"https://mlsbd.shop/{(movie_name.replace(' ', '-')).lower()}"
        response_2 = requests.get(f"{search_url_2}").status_code
         
        search_url_3 = f"https://hdhub4u.contact/{(movie_name.replace(' ', '-')).lower()}/"
        response_3 = requests.get(f"{search_url_3}").status_code
        
        search_url_4 = f"https://mlwbd.lv/{(movie_name.replace(' ', '-')).lower()}/"
        response_4 = requests.get(f"{search_url_4}").status_code
        
        
        if response_1 == 404:
            movie=0
        else:
            download_link_1=search_url_1
            movie_found=True
        
        if response_2 == 404:
            mmovie=0
        else:
            download_link_2=search_url_2
            movie_found=True
        
        if response_3 == 404:
            movie=0
        else:
            download_link_3=search_url_3
            movie_found=True
        
        if response_4 == 404:
            movie=0
        else:
            download_link_4=search_url_4
            movie_found=True
        
           
        if response_1==404 and response_2==404 and response_3==404 and response_4==404:
            movie_found=False
        else:
            movie=0
            
    return render_template('movies.html',
                           movie_found=movie_found,
                           download_link_1=download_link_1,
                           download_link_2=download_link_2,
                           download_link_3=download_link_3,
                           download_link_4=download_link_4)

@app.route('/software', methods=['GET', 'POST'])
def software():
    sw_found = None
    download_link_1 = None
    download_link_2 = None
    download_link_3 = None
    
    if request.method == 'POST':
        sw_name = request.form['sw_name']

        search_url_1 = f"https://haxnode.net/{(sw_name.replace(' ', '-')).lower()}"
        response_1 = requests.get(f"{search_url_1}").status_code
        
        search_url_2 = f"https://{(sw_name.replace(' ', '-')).lower()}.en.softonic.com" 
        response_2 = requests.get(f"{search_url_2}").status_code
        
        search_url_3 = f"https://getintopc.cc/{(sw_name.replace(' ', '-')).lower()}"
        response_3 = requests.get(f"{search_url_3}").status_code
        
        if response_3 == 404:
            game=0
        else:
            download_link_3=search_url_3
            sw_found=True
            
        if response_2 == 404:
            game=0
        else:
            download_link_2=search_url_2
            sw_found=True
            
        if response_1 == 404:
            game=0
        else:
            download_link_1=search_url_1
            sw_found=True
        
        if response_1==404 and response_2==404:
            sw_found=False
        else:
            game=0

    return render_template('software.html',
                           sw_found=sw_found,
                           download_link_1=download_link_1,
                           download_link_2=download_link_2,
                           download_link_3=download_link_3)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/exit')
def exit():
    return "Thanks for visiting!"

