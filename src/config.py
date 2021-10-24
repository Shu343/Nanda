import configparser
from logging import warning

class WhitespaceFriendlyConfigParser(configparser.ConfigParser):
	def get(self, section, option, *args, **kwargs):
		val = super().get(section, option, *args, **kwargs)

[data]
database = database.sqlite

[connection]
useragent = 

[reddit]
subreddit = u/Shu301
username = Shu301
password = ItsShu3
oauth_key = nhBIilWEs3I9PA-a4qp3fg
oauth_secret = PhP9iG5WvF7ljOITR4Ln3hD6GY_jDQ

[service.mal]
username = 
password = 

[service.anidb]
client = 

[service.nyaa]
domain = nyaa.si
excluded_users = 
filter = 0

[service.youtube]
api_key = 

[options]
# Valid options, separated with a space: tv, movie, ova
new_show_types = tv
record_scores = true

[options.discovery]
# Service used 
primary_source = mal
# Services for additional data/links
secondary_sources = anidb
# Stream services
stream_sources = crunchyroll

[post]
title = {show_name} - Episode {episode} discussion
title_postfix_final = - FINAL
flair_id = 
flair_text = 

body = 
	*{show_name}*, episode {episode}{episode_alt_number}{episode_name}

	{aliases}

	{poll}
	
	{spoiler}
	
	---
	
	**Streams**
	
	{streams}
	
	**Show information**
	
	{links}
	
	---
	
	**All discussions**
	
	{discussions}
		
	---
	
	*This post was created by a bot. Message the mod team for feedback and comments.*
	*The original source code can be found on [GitHub](https://github.com/r-anime/holo).*

format_spoiler = **Reminder:** Please do not discuss plot points not yet seen or skipped in the show. Failing to follow the rules may result in a ban.
format_stream = * [{service_name}]({stream_link})
format_link = * [{site_name}]({link})
format_link_reddit = * **{link}**
format_discussion_header = Episode|Link|Score
format_discussion_align = :-:|:-:|:-:
format_discussion = {episode}|[Link]({link})|[{score}]({poll_link})
format_discussion_none = *No discussions yet!*
format_aliases = Alternative names: *{aliases}*
poll_title = {show} - Episode {episode}
format_poll = # [Rate this episode here.]({poll_url})
