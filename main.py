import os
from os import system
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib.request import urlopen
import json
import urllib.parse
from keep_alive import keep_alive
from flask import Flask
from threading import Thread
from itertools import cycle



load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="_", case_insensitive=True, intents=intents)


def is_int(val):
  if type(val) == int:
    return True
  else:
    if int(val) == val:
      return True
    else:
      return False


@bot.event
async def on_ready():
  print('Connected to bot: {}'.format(bot.user.name))
  print('Bot ID: {}'.format(bot.user.id))
  print("Your bot is ready")


# @bot.command()
# async def test(ctx, arg):
#   await ctx.send(arg)


@bot.command()
async def title(ctx, arg):
  id = arg
  url = "https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/creations/" + id
  response = urlopen(url)
  data_json = json.loads(response.read())
  title = str(data_json['title'])
  await ctx.send(title)


@bot.command()
async def search(ctx, num, *string):
  if is_int(num) == False:
    search = urllib.parse.quote_plus(''.join(string).encode('utf-8'))
    url = "https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/creations?title=" + search
    response = urlopen(url)
    data_json = json.loads(response.read())
    try:
      if num == None:
        entries = data_json[0]
      else:
        entries = data_json[int(num)]
      ttl = entries["data"]["title"]
      id = entries["data"]["id"]
      tid = entries["id"]  #trimmed id
      vts = str(entries["data"]["score"])
      pid = str(entries["data"]["parent_id"])
      chld = str(entries["data"]["children"])
      ts = entries["data"]["timestamp"]
      url = "https://sandspiel.club/#" + tid
      thmb = "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F" + id + ".png?alt=media"
      embed = discord.Embed(title=ttl, url=url, description=ts)
      embed.set_author(name="Sandspiel Post")
      embed.set_thumbnail(
        url=
        "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F"
        + id + ".png?alt=media#.png")
      embed.add_field(name="Title", value=ttl, inline=True)
      embed.add_field(name="ID", value=id, inline=True)
      embed.add_field(name="Trimmed ID", value=tid, inline=True)
      embed.add_field(name="Score", value=vts, inline=True)
      embed.add_field(name="Parent ID", value=pid, inline=True)
      embed.add_field(name="Children", value=chld, inline=True)
      await ctx.send(embed=embed)
    except IndexError:
      await ctx.send("No results!")


@bot.command()
async def trending(ctx):
  final = ""
  print("test")
  url = "https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/trending/"
  response = urlopen(url)
  data_json = json.loads(response.read())
  print(data_json)
  for i in range(len(data_json)):
    print()
    entries = data_json[i]
    trending = entries["hashtag"] + ": " + entries["htcount"] + " posts" + "\n"
    final = final + trending
  await ctx.send("**trending hashtags**\n" + final)
 #Trending Hashtags
@bot.command()
async def top(ctx, num):
  if is_int(num) == False:
    url = "https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/creations?q=score"
    response = urlopen(url)
    data_json = json.loads(response.read())
    try:
      if num == None:
        entries = data_json[0]
      else:
        entries = data_json[int(num)]
      ttl = entries["data"]["title"]
      id = entries["data"]["id"]
      tid = entries["id"]  #trimmed id
      vts = str(entries["data"]["score"])
      pid = str(entries["data"]["parent_id"])
      chld = str(entries["data"]["children"])
      ts = entries["data"]["timestamp"]
      url = "https://sandspiel.club/#" + tid
      thmb = "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F" + id + ".png?alt=media"
      embed = discord.Embed(title=ttl, url=url, description=ts)
      embed.set_author(name="Sandspiel Post")
      embed.set_thumbnail(
        url=
        "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F"
        + id + ".png?alt=media#.png")
      embed.add_field(name="Title", value=ttl, inline=True)
      embed.add_field(name="ID", value=id, inline=True)
      embed.add_field(name="Trimmed ID", value=tid, inline=True)
      embed.add_field(name="Score", value=vts, inline=True)
      embed.add_field(name="Parent ID", value=pid, inline=True)
      embed.add_field(name="Children", value=chld, inline=True)
      await ctx.send(embed=embed)
    except IndexError:
      await ctx.send("No results!") #Top Posts
@bot.command()
async def recent(ctx, num):
  if is_int(num) == False:
    url = "https://us-central1-sandtable-8d0f7.cloudfunctions.net/api/creations"
    response = urlopen(url)
    data_json = json.loads(response.read())
    try:
      if num == None:
        entries = data_json[0]
      else:
        entries = data_json[int(num)]
      ttl = entries["data"]["title"]
      id = entries["data"]["id"]
      tid = entries["id"]  #trimmed id
      vts = str(entries["data"]["score"])
      pid = str(entries["data"]["parent_id"])
      chld = str(entries["data"]["children"])
      ts = entries["data"]["timestamp"]
      url = "https://sandspiel.club/#" + tid
      thmb = "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F" + id + ".png?alt=media"
      embed = discord.Embed(title=ttl, url=url, description=ts)
      embed.set_author(name="Sandspiel Post")
      embed.set_thumbnail(
        url=
        "https://firebasestorage.googleapis.com/v0/b/sandtable-8d0f7.appspot.com/o/creations%2F"
        + id + ".png?alt=media#.png")
      embed.add_field(name="Title", value=ttl, inline=True)
      embed.add_field(name="ID", value=id, inline=True)
      embed.add_field(name="Trimmed ID", value=tid, inline=True)
      embed.add_field(name="Score", value=vts, inline=True)
      embed.add_field(name="Parent ID", value=pid, inline=True)
      embed.add_field(name="Children", value=chld, inline=True)
      await ctx.send(embed=embed)
    except IndexError:
      await ctx.send("No results!")

 #Recent Posts
      
keep_alive()  # Starts a webserver to be pinged.

try:
  bot.run(os.getenv("TOKEN"))
#Bot Restarter
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  system("restarter.py")
  system('kill 1')
