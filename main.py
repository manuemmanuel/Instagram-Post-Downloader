import instaloader

def download_instagram_photos(profile_name):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {profile_name} does not exist.")
        return
    except instaloader.exceptions.ConnectionException as e:
        print(f"Connection error: {e}")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    for post in profile.get_posts():
        try:
            L.download_post(post, target=profile_name)
        except instaloader.exceptions.InstaloaderException as e:
            print(f"Error downloading post {post.shortcode}: {e}")

if __name__ == "__main__":
    profile_name = '_preethiasokan_'
    download_instagram_photos(profile_name)
