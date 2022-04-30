from pytube import Playlist
import os

DWNNLD_PATH = 'C:\\Users\\pastu\\from_youtube'

# channel = Channel('https://www.youtube.com/channel/UC-sAMvDe7gTmBbub-rWljZg')
playlist_terraform_rus = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYujWDTYb-Zbofdl44Jxb2l8')
playlist_jenkins = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYvQbMrSuOjTL1HOiDhUE_5a')
playlist_mossad = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYs1j6nUQsgn6Atxti390S9c')
playlist_github = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYstwxTEOU05E0URTHnbtA0l')
playlist_ansible = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYufspdPupdynbMQTBnZd31N')
playlist_kubernetes = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYvN1RqaVesof8KAf-02fJSi')
playlist_linux_beg = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYuE4z-3BgLYGkZrs-cF4Tep')
playlist_linux_adv = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYsgy5qLYZtvoaV34zn5iKPe')
playlist_python_beg = Playlist('https://www.youtube.com/watch?v=gJfYu1R8TL8&list=PLg5SS_4L6LYtHCActBzbuGVYlWpLYqXC6')
playlist_python_adv = Playlist('https://www.youtube.com/watch?v=JADUD_JyRbM&list=PLg5SS_4L6LYt7Wmh8zBKjZ_ltaoDXSEmk')
playlist_aws = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYsxrZ_4xE_U95AtGsIB96k9')
playlist_google_cloud = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYs5IZZSY0viHRQFPa2P-R8H')
playlist_it = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYsRPYsxOzDnEynpuQVEjUPy')
playlist_devops = Playlist('https://www.youtube.com/playlist?list=PLg5SS_4L6LYuu1RAT4l1tCkZrJzkIaNgL')

playlists = [playlist_terraform_rus,
            playlist_jenkins,
            playlist_mossad,
            playlist_github,
            playlist_ansible,
            playlist_kubernetes,
            playlist_linux_beg,
            playlist_linux_adv,
            playlist_python_beg,
            playlist_python_adv,
            playlist_aws,
            playlist_google_cloud,
            playlist_it,
            playlist_devops]

for playlist in playlists:

    folder_name = playlist.title
    folder_path = os.path.join(DWNNLD_PATH, folder_name)
    print(folder_path)
    try:
        print('Creating directory {}'.format(folder_name))
        os.mkdir(folder_path)
    except:
        print('Already have one {}'.format(folder_name))

    for video in playlist.videos:
        title = video.title
        file_exists = os.path.exists(os.path.join(folder_path, title+'.mp4'))
        if file_exists:
            print('{} already exists'.format(title))
        else:
            print('Dowloading {}'.format(title))
            video.streams.filter().get_highest_resolution().download(folder_path)
