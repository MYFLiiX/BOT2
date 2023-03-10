import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>๐ Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>๐I Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>๐ฅ </b><b><u>How To Download Any Movie, Series, Anime etc., For Free???</u></b> \n\n <b>๐</b> <b>Join Any Of The Above Groups</b>๐"""
    ABOUT_TXT = """<i><u>๐งถ </u></i><i><u><b>Follow These Steps To Connect Me To Your Group</b>๐</u>

1. Click on This [</i><a href="http://telegram.me/heroriderbot?startgroup=true"><i>Blue Text</i></a><i>]
2. Select Your Group
3. Make Me Admin in Your Group</i>"""    
    SOURCE_TXT = """<i><b><u>AutoFilter + UrlShortner Bot</u></b>

๐ Want An </i><i><b>'AutoFilter + UrlShortner Bot'</b> Like Me For Your Group &amp; Earn Money Using It?

๐ฒ </i><i><b>Contact ยป</b> </i><i>@Irfan50786</i>"""    
    MANUELFILTER_TXT = """Help: <b>FILTERS ยป</b>

ยป <b>Filter is A Feature Where Users can Set Automated Reply to a Specific Word</b>

<b>Important Notes:</b>
1.<i> I Have To Be Admin </i>
2.<i> Only admins can add Filters in Chat</i>
3.<i> Buttons have a limit of 64 Characters</i>

<b>Commands and Usage:</b>
โข <i> /filter - Add a Filter</i>
โข <i> /filters - List of All Filters</i>
โข <i> /del - Delete a Filter</i>
โข <i> /delall - Delete All Filters</i> """
    BUTTON_TXT = """Help: <b>BUTTONS ยป</b>

ยป Supports both url and alert inline buttons.

<b>NOTE:</b>
1. <i>Telegram will not allows you to send buttons without any content, so content is mandatory.</i>
2. <i>Supports buttons with any telegram media type</i>
3. <i>Buttons should be properly parsed as markdown format</i>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/HeroRiderbot)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>AUTO FILTER ยป</b>

Add Me In Your Group as Admin & I Will Provide Any Movie, Series, Animation etc.,"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. <i>Only Admins Can Add Connection</i>
2. <i>Send <code>/connect</code> To Connect Me to Your PM</i>

<b>Commands and Usage:</b>
โข<i> /connect  - Connect a Chat to your PM</i>
โข<i> /disconnect  - Disconnect from a Chat</i>
โข<i> /connections - List Of All Connections</i>"""
    EXTRAMOD_TXT = """Help: <b>Extra Features of Me ยป</b>

<b>Commands and Usage:</b>
โข<i> /id - Get ID Of A User</i>
โข<i> /imdb  - Get Movie/Series Info from IMDb</i>"""
    ADMIN_TXT = """Help: <b>ADMIN MODS ยป</b>

<b>NOTE:</b>
This Works Only For Admins!

<b>Commands and Usage:</b>
โข<i> /stats - Get Status of DataBase</i>
โข<i> /delete - Delete A File</i>
โข<i> /users - List of My Users </i>
โข<i> /chats - Get List Of My Chats </i>
โข<i> /leave  - Leave from a chat</i>
โข<i> /disable  - Disable a Chat</i>
โข<i> /ban  - Ban a User</i>
โข<i> /unban  - Unban a User</i>
โข<i> /channel - List of All Connected Channels</i>
โข<i> /broadcast - Broadcast a Message to All Users</i>"""
    STATUS_TXT = """<b>๐๏ธ My Statistics ๐ฒ</b>

โ <b>Total Files :</b> {}
โ <b>Total Users :</b> {}
โ <b>Total Chats :</b> {}
โ <b>Used Storage :</b> {} 
โ <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>Group ยป</b> {} (<code>{}</code>)
<b>Total Members ยป</b> <code>{}</code>
<b>Added By ยป</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
โ ID - <code>{}</code>
โ Name - {}
"""
