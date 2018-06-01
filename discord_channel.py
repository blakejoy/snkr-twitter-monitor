from discord_hooks import Webhook
from config import HOOK_URL

def send_embed(tweet):
    '''
    (str, str, list, str, str, str) -> None
    Sends a discord alert based on info provided.
    '''
    # Set webhook
    url = HOOK_URL

    # Create embed to send to webhook
    embed = Webhook(url, color=123123)

    # Set author info
    embed.set_author(name='TWEET FROM: {}'.format(tweet.username),
                     icon='https://cdn2.iconfinder.com/data/icons/minimalism/128/twitter.png')

    embed.set_desc(tweet.username)

    embed.add_field(name="Tweet", value=tweet.text)

    embed.add_field(name="Link to Tweet", value=tweet.link_to_tweet)

    print(tweet.text)
    if len(tweet.url_list) > 0:
        for url in tweet.url_list:
            embed.add_field(name="Links in Tweet", value=url["expanded_url"])

    embed.set_thumbnail(tweet.profile_img_url)

    # Set product image
    if tweet.image_url != "":
        embed.set_image(tweet.image_url)
    else:
        embed.set_image(tweet.profile_img_url)


    # Set footer
    embed.set_footer(text='TWITTER MONITOR by BGRIMEY247 & HYPEWARDROBE',
                     icon='https://pbs.twimg.com/profile_images/991746098556530688/C4QmWno8_400x400.jpg', ts=True)

    # Send Discord alert
    embed.post()