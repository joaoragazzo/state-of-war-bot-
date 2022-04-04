import datetime #
import discord #
from discord import channel, colour, reaction #
from discord.ext import commands, tasks #
from discord.ext.commands.core import check, command #
from discord import File #
import discord_components #
from discord_components import DiscordComponents, Select, SelectOption, Button, ButtonStyle, ComponentsBot #
import openpyxl #
from openpyxl import load_workbook #
from openpyxl.utils import get_column_letter #
import time #
import requests #

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['!'], description="Bot", intents=intents)
DiscordComponents(bot)
client = discord.Client(intents=intents)

update_state = "OFF"

@bot.command(name="regras_1")
async def regras_1(ctx):   
    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761)

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    await ctx.message.delete()

    await ctx.send(file=discord.File("images/regras.png"))
    embedVar = discord.Embed(title="**Regras do servidor**", description="É estritamente proibido, dentro das dependências do State of War:",colour=discord.Colour.red())
    embedVar.set_footer(text="As regras estão sujeitas a mudanças. Fique atento!")
    await ctx.send(embed=embedVar)
    await ctx.send("```python\n1・Uso de programas externos que possam oferecer vantagem dentro do jogo (hacks/sem mato);\n2・Uso de glitchs/bugs que ofereçam vantagem por cima de outros jogadores;\n3・Qualquer tipo de preconceito ou discurso de ódio;\n4・Ghost em streamers (caso comprovado, será paassivel de punição);\n5・Qualquer tipo de combatlog (deslogar durante ações de PvP);\n6・Deixar veículos estacionados dentro de Safezones (recomendamos guarda-los dentro de garagens);\n7・Destruir ou arruinar veículos trancados pelo mapa (dentro ou fora de bases);\nObservação・NÃO se responsabilizamos por eventuais bugs nos mods que ocasionem perdas ou prejuízo, pois não temos controle sobre os mesmos```")

    await ctx.send(file=discord.File("images/divisoria.gif"))
    embedVar = discord.Embed(title="**Regras de construção**", description="É necessário atentar-se:",colour=discord.Colour.red())
    embedVar.set_footer(text="As regras estão sujeitas a mudanças. Fique atento!")
    await ctx.send(embed=embedVar)
    await ctx.send("```python\n1・Toda e qualquer construção tem que ser feita a mais de 1000 metros das safe-zones;\n2・Toda e qualquer construção tem que ser feita a mais de 800 metros de Black Markets, caçadores e áreas militares;\n3・Toda base precisa ser raidavel;\n4・É permitido apenas uma FOB por clan;\n5・O tamanho máximo de qualquer base é de 125 cubos (exemplo: 5 x 5 x 5);\n6・É estritamente proibido bugar barracas;\n7・Máximo de 10 codelocks por base; Máximo de 3 codelocks por FOB; Sem limite de barracas com codelock (porém, podem ser destruidas em dia de raid);\n8・Todas as paredes devem ter um distanciamento mínimo de 1 jogador;\n9・Proibido colocar portas encostadas uma nas outras;\n10・Toda base precisa ter física básica (recomendamos o uso de pilares e fundação para isso);\n10.1・Toda base que não possua física, será deletada e os itens não serão reembolsados;\n11・Não é permitido colocar codelocks em cofres, armários e etc. (Caso visto, será deletado e os itens não serão reembolsados)```")

    await ctx.send(file=discord.File("images/divisoria.gif"))
    embedVar = discord.Embed(title="**Regras de raid**", description="É necessário atentar-se:",colour=discord.Colour.red())
    embedVar.set_footer(text="As regras estão sujeitas a mudanças. Fique atento!")
    await ctx.send(embed=embedVar)
    await ctx.send('```python\nOs horários de raid são:\n・Sexta-feira: Das 18:00 às 23:59\n・Sábado: Das 14:00 às 00:59\n・Domingo: Das 18:00 às 23:59\n1・O Raid é permitido apenas com C4 em portas, portões e floor/roof hatches;\n2・Não é permitido uso de helicopteros para raidar (não pouse em cima de base alheia);\n3・Toda ação do Raid deve ser gravada e enviada num prazo de 48 horas;\n4・O jogador ou clan que sofreu o Raid, tem até 5 dias para fechar a base. Caso contrário, a base será deletada;\n5・O raid por falha de construção é proibido;\n6・Não é permitido construir enquanto estiver ocorrendo o Raid;\n7・Técnica do pézinho permitido apenas após explodir o floor/roof hatch para acessar o próximo andar;\n8・Proibido usar itens flutuantes ou bugs para raidar;\n9・Proibido empilhar itens para raidar (Ex: empilhar portas de veiculos, barris...);\n10・Proibido utilização de bugs de textura ou qualquer outro tipo de bug;\n11・Barracas com codelock fora de bases podem ser destruidas 24/7 sem a necessidade de gravação;\n12・Na presença de um administrador, caso ocorra um bug ou invalidade durante o raid, ele será interrompido imediatamente;\n13・Proibido destruir veiculos/helicopteros dentro de bases;\n14・Proibido mandar localização de bases abertas em quaisqueres meios de comunicação;\n15・Não é permitido vandalismo por nenhuma das partes;\n16・Quem está sendo raidado não poderá destruir os itens durante o raid.```')
    await ctx.send("```python\nConstrução Tier 1: uma C4 branca OU uma C4 verde\nConstrução Tier 2: duas C4 brancas OU duas C4 verdes\nConstrução Tier 3: quatro C4 verdes.```")
    return

@bot.command(name="enquete")
async def enquete(ctx, *,conteudotitulo):
    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761)

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    conteudotitulo = conteudotitulo.split("/")
    enquete_titulo = conteudotitulo[0]
    enquete_conteudo = conteudotitulo[1]

    channel = bot.get_channel(960031449199829052)

    cor = discord.Colour.random()

    embedVar = discord.Embed(title=f"🗳️ {enquete_titulo}", description=f"{enquete_conteudo}", colour = cor)
    enquete = await channel.send(embed = embedVar)
    await enquete.add_reaction("✅")
    await enquete.add_reaction("❌")
    return

@bot.command(name="code")  ##ARRUMAR O CÓDIGO
async def code(ctx , code):

    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    authorid = ctx.author.id
    authorid = "`"+str(authorid)+"`"

    ##Configurações iniciais para conexão com a API do discord
    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    def get_info(codex):
        code = codex
        API_ENDPOINT = 'https://discord.com/api/v8'
        CLIENT_ID = '912310660669521921'
        CLIENT_SECRET = 'TJBNOzRyXWWqlRxCLkLgxDOo2147TLe0'
        REDIRECT_URI = 'https://stateofwar.xyz'
        def exchange_code(code):
          data = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI
          }
          headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
          r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
          r.raise_for_status()
          return r.json()
        def get_user_json(acess_token):
          url = f"{API_ENDPOINT}/users/@me/connections"
          headers = {
            "Authorization": "Bearer {}".format(acess_token)
          }
          user_object = requests.get(url=url, headers=headers)
          user_json = user_object.json()
          return user_json
        code = exchange_code(code)["access_token"]
        user_json = get_user_json(code)
        user = str(user_json).split('}')
        for section in user:
            if ("steam") in section:
                data = section
        

        data = data[20:]
        data = data.replace("{","")
        data = data.replace("'","")
        data = data.split(",")
        id, nick, verificed = data[0], data[1], data[5]
        id = id.split(':')
        nick = nick.split(':')
        verificed = verificed.split(':')
        steam_id = id[1]
        nick = nick[1]
        verificed = verificed[1]
        steam_id = steam_id[1:]
        nick = nick[1:]
        return steam_id, nick, verificed
    data = get_info(code)

    id = data[0]
    id = "`"+id+"`"

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == authorid:
                ws[f'{get_column_letter(cell.column + 2)}{cell.row}'] = id
                ws[f'{get_column_letter(cell.column + 3)}{cell.row}'] = data[1]
                ws[f'{get_column_letter(cell.column + 4)}{cell.row}'] = data[2]
                wb.save(file)

    embedVar = discord.Embed(title="✅ Verificado com sucesso", description = "A sua conta Steam está vinculada com o nosso sistema.")
    embedVar.set_footer(text="➝ Se precisar de ajuda com o seu registro, entre em contato com o DEV.")
    warning = await ctx.reply(embed=embedVar)

    time.sleep(8)
    await ctx.message.delete()
    await warning.delete()

@bot.command(name="ficha")
async def ficha(ctx, member:discord.Member):

    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761) #ID DE ADMINISTRADOR SUPREMO

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    member_id = member.id
    member_id = str(member_id)
    member_id = "`"+member_id+"`"
    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                discord_id = ws.cell(row=cell.row, column=1).value
                discord_nick = ws.cell(row=cell.row, column=2).value
                steam_id = ws.cell(row=cell.row, column=3).value
                steam_nick = ws.cell(row=cell.row, column=4).value
                steam_verify = ws.cell(row=cell.row, column=5).value
                rules_broken = ws.cell(row=cell.row, column=6).value
                adv = ws.cell(row=cell.row, column=7).value
                bans = ws.cell(row=cell.row, column=8).value
                clan = ws.cell(row=cell.row, column=9).value
                cars_seguro = ws.cell(row=cell.row, column=10).value
                cars_seguro_days = ws.cell(row=cell.row, column=11).value
                cars_seguro_remain = ws.cell(row=cell.row, column=12).value
                heli_seguro = ws.cell(row=cell.row, column=13).value
                heli_seguro_days = ws.cell(row=cell.row, column=14).value
                heli_seguro_remain = ws.cell(row=cell.row, column=15).value
                construcao = ws.cell(row=cell.row, column=16).value
                construcao_days = ws.cell(row=cell.row, column=17).value
                fila_prioritaria = ws.cell(row=cell.row, column=18).value
                fila_prioritaria_days = ws.cell(row=cell.row, column=19).value

                n += 1
            else:
                n += 0
    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado um registro do usuário em questão!")
        embedVar.set_footer(text="Caso você ache que isso é um engano, contate o DEV!")
        await ctx.send(embed = embedVar)
        return  

    embedVar = discord.Embed(title="📝 Ficha do usuário", description="📝 Segue a ficha detalhada do usuário abaixo\n", colour = discord.Colour.random())
    embedVar.add_field(name="<:steam:958580268581662770> Steam *", value=f"SteamID: {steam_id}\nSteam nick: `{steam_nick}` **\nVerificado: `{steam_verify}`")
    embedVar.add_field(name=":shield: Clã", value=f"{clan}")
    embedVar.add_field(name=":card_box: Histórico", value=f"Infrações: `{rules_broken}`\nAdvertências: `{adv}`\nBanimentos: `{bans}`")
    embedVar.add_field(name="<:discord:958830929810440284> Discord", value=f"Nick: `{discord_nick}`\nID: {discord_id}")
    embedVar.add_field(name=":blue_car: Seguro de carros", value=f"Possui: `{cars_seguro}`\nQuantos restantes: `{cars_seguro_remain}`\nQuantos dias restantes: `{cars_seguro_days}`")
    embedVar.add_field(name=":helicopter: Seguro helicopteros", value=f"Possui: `{heli_seguro}`\nQuantos restantes: `{heli_seguro_remain}`\nQuantos dias restantes: `{heli_seguro_days}`")
    embedVar.add_field(name=":house: Construção", value=f"Possui: `{construcao}`\nDias restantes: `{construcao_days}`")
    embedVar.add_field(name="<:vip:958581319418384395> Fila prioritaria", value=f"Possui: `{fila_prioritaria}`\nDias restantes: `{fila_prioritaria_days}`")
    embedVar.add_field(name="ㅤ", value="ㅤ")
    embedVar.set_footer(text="*Caso as inforamções estejam como 'None', significa que o discord não foi vinculado ao nosso sistema\n** O nick pode ser modificado na Steam e não atualizado no nosso banco de dados.\n➝ Caso tenha alguma dúvida, entre em contato com o DEV.")
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)
    url_antes = f"https://www.steamidfinder.com/lookup/{steam_id}/"

    await ctx.reply(embed=embedVar, components=[Button(label="Mais informações", style = ButtonStyle.URL ,url=url_antes)])
    return

@bot.command(name="perfil")
async def perfil(ctx):

    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return
    
    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    member = ctx.author

    member_id = member.id
    member_id = str(member_id)
    member_id = "`"+member_id+"`"
    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                discord_id = ws.cell(row=cell.row, column=1).value
                discord_nick = ws.cell(row=cell.row, column=2).value
                steam_id = ws.cell(row=cell.row, column=3).value
                steam_nick = ws.cell(row=cell.row, column=4).value
                steam_verify = ws.cell(row=cell.row, column=5).value
                rules_broken = ws.cell(row=cell.row, column=6).value
                adv = ws.cell(row=cell.row, column=7).value
                bans = ws.cell(row=cell.row, column=8).value
                clan = ws.cell(row=cell.row, column=9).value
                cars_seguro = ws.cell(row=cell.row, column=10).value
                cars_seguro_days = ws.cell(row=cell.row, column=11).value
                cars_seguro_remain = ws.cell(row=cell.row, column=12).value
                heli_seguro = ws.cell(row=cell.row, column=13).value
                heli_seguro_days = ws.cell(row=cell.row, column=14).value
                heli_seguro_remain = ws.cell(row=cell.row, column=15).value
                construcao = ws.cell(row=cell.row, column=16).value
                construcao_days = ws.cell(row=cell.row, column=17).value
                fila_prioritaria = ws.cell(row=cell.row, column=18).value
                fila_prioritaria_days = ws.cell(row=cell.row, column=19).value

                n += 1
            else:
                n += 0
    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado um registro do usuário em questão!")
        embedVar.set_footer(text="Caso você ache que isso é um engano, contate o DEV!")
        await ctx.send(embed = embedVar)
        return  

    embedVar = discord.Embed(title="📝 Ficha do usuário", description="📝 Segue a ficha detalhada do usuário abaixo\n", colour = discord.Colour.random())
    embedVar.add_field(name="<:steam:958580268581662770> Steam *", value=f"SteamID: {steam_id}\nSteam nick: `{steam_nick}` **\nVerificado: `{steam_verify}`")
    embedVar.add_field(name=":shield: Clã", value=f"{clan}")
    embedVar.add_field(name=":card_box: Histórico", value=f"Infrações: `{rules_broken}`\nAdvertências: `{adv}`\nBanimentos: `{bans}`")
    embedVar.add_field(name="<:discord:958830929810440284> Discord", value=f"Nick: `{discord_nick}`\nID: {discord_id}")
    embedVar.add_field(name=":blue_car: Seguro de carros", value=f"Possui: `{cars_seguro}`\nQuantos restantes: `{cars_seguro_remain}`\nQuantos dias restantes: `{cars_seguro_days}`")
    embedVar.add_field(name=":helicopter: Seguro helicopteros", value=f"Possui: `{heli_seguro}`\nQuantos restantes: `{heli_seguro_remain}`\nQuantos dias restantes: `{heli_seguro_days}`")
    embedVar.add_field(name=":house: Construção", value=f"Possui: `{construcao}`\nDias restantes: `{construcao_days}`")
    embedVar.add_field(name="<:vip:958581319418384395> Fila prioritaria", value=f"Possui: `{fila_prioritaria}`\nDias restantes: `{fila_prioritaria_days}`")
    embedVar.add_field(name="ㅤ", value="ㅤ")
    embedVar.set_footer(text="*Caso as inforamções estejam como 'None', significa que o discord não foi vinculado ao nosso sistema\n** O nick pode ser modificado na Steam e não atualizado no nosso banco de dados.\n➝ Caso tenha alguma dúvida, entre em contato com o DEV.")
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)
    url_antes = f"https://www.steamidfinder.com/lookup/{steam_id}/"
    await member.send(embed=embedVar, components=[Button(label="Mais informações", style = ButtonStyle.URL ,url=url_antes)])
    return

@bot.command(name="registrarall")
async def registrarall(ctx):

    if update_state == "ON":
        warning = await ctx.send("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761) #ID DE ADMINISTRADOR SUPREMO

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return 

    guild = bot.get_guild(947237264596041728)
    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active
    for member in guild.members:
        id = member.id
        id = str(id)
        id = "`"+id+"`"
        name = member.name
        discriminator = member.discriminator
        nickname = name + "#" + discriminator
        ws[f'{get_column_letter(ws.min_column + 0)}{(ws.max_row + 1)}'] = id
        ws[f'{get_column_letter(ws.min_column + 1)}{(ws.max_row)}'] = nickname
        ws[f'{get_column_letter(ws.min_column + 5)}{(ws.max_row)}'] = "0" #INFRAÇÕES
        ws[f'{get_column_letter(ws.min_column + 6)}{(ws.max_row)}'] = "0" #ADVERTÊNCIAS
        ws[f'{get_column_letter(ws.min_column + 7)}{(ws.max_row)}'] = "0" #BANIMENTOS
        ws[f'{get_column_letter(ws.min_column + 8)}{(ws.max_row)}'] = "Não participante" #CLÃ
        ws[f'{get_column_letter(ws.min_column + 9)}{(ws.max_row)}'] = "❌" #SEGURO DE VEICULOS
        ws[f'{get_column_letter(ws.min_column + 10)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
        ws[f'{get_column_letter(ws.min_column + 11)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE VEICULOS
        ws[f'{get_column_letter(ws.min_column + 12)}{(ws.max_row)}'] = "❌" #SEGURO DE HELICOPTEROS
        ws[f'{get_column_letter(ws.min_column + 13)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
        ws[f'{get_column_letter(ws.min_column + 14)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE HELICOPTEROS
        ws[f'{get_column_letter(ws.min_column + 15)}{(ws.max_row)}'] = "❌" #POSSUI ALGUMA CONSTRUÇÃO
        ws[f'{get_column_letter(ws.min_column + 16)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES DA CONSTRUÇÃO
        ws[f'{get_column_letter(ws.min_column + 17)}{(ws.max_row)}'] = "❌" #POSSUI FILA PRIORITARIA
        ws[f'{get_column_letter(ws.min_column + 18)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES 
        wb.save(file)
    print('done')
    return

@bot.command(name="vipadd")
async def vipadd(ctx, member:discord.Member):

    if update_state == "ON":
        warning = await ctx.send("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761) #ID DE ADMINISTRADOR SUPREMO

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return 

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    member_id = member.id
    member_id = str(member_id)
    member_id = "`"+member_id+"`"
    n = 0


    embedVar = discord.Embed(title=f"<:vip:958581319418384395> Adicionar VIP para **{member.name}**", description="Selecione o VIP que você deseja adicionar.", colour = discord.Colour.random())
    embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá adicionar o VIP.\n・O comando deixará de funcionar em 10 segundos.\n・O tempo padrão de qualquer doação é de 30 dias.\n・Ignore a mensagem _'interação falhou'_, é um bug do Discord.")
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)
    embedVar.set_footer(text="➝ Caso tenha alguma dúvida, entre em contato com o DEV.")
    
    await ctx.send(embed=embedVar, components=[Select(
        placeholder="Adicionar tipo de doação",
        options=[
            SelectOption(label="Fila prioritária", value="filaprioritaria", emoji="⭐"),
            SelectOption(label="Seguro de veículos", value="seguro_de_veiculos", emoji="🚘"),
            SelectOption(label="Seguro de helicopteros", value="seguro_de_heli", emoji="🚁"),
            SelectOption(label="Bunker menor", value="bunker_menor", emoji="🏠"),
            SelectOption(label="Bunker maior", value="bunker_maior", emoji="🏠"),
            SelectOption(label="Prédio", value="predio", emoji="🏠")

        ],
        custom_id='VIP_List'
    )])

    interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'VIP_List' and inter.user == ctx.author, timeout = 10)
    
    if interaction.values[0] == "filaprioritaria":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 17)}{(cell.row)}'] = "✅" #POSSUI FILA PRIORITARIA
                    ws[f'{get_column_letter(cell.column + 18)}{(cell.row)}'] = "31" #TEMPO RESTANTE DA VILA PRIORITARIA
                    wb.save(file)
                    n += 1
                    id = "fila prioritária"
                else:
                    n += 0
    elif interaction.values[0] == "seguro_de_veiculos":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 9)}{(cell.row)}'] = "✅" #POSSUI FILA PRIORITARIA
                    ws[f'{get_column_letter(cell.column + 10)}{(cell.row)}'] = "31" #TEMPO RESTANTE DA VILA PRIORITARIA
                    ws[f'{get_column_letter(cell.column + 11)}{(cell.row)}'] = "Indefinido" #SEGUROS RESTANTES
                    wb.save(file)
                    n += 1
                    id = "seguro de veículos"
                else:
                    n += 0
    elif interaction.values[0] == "seguro_de_heli":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 12)}{(cell.row)}'] = "✅" #POSSUI FILA PRIORITARIA
                    ws[f'{get_column_letter(cell.column + 13)}{(cell.row)}'] = "31" #TEMPO RESTANTE DA VILA PRIORITARIA
                    ws[f'{get_column_letter(cell.column + 14)}{(cell.row)}'] = "Indefinido" #SEGUROS RESTANTES
                    wb.save(file)
                    n += 1
                    id = "seguro de helicopteros"
                else:
                    n += 0
    elif interaction.values[0] == "bunker_menor":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 15)}{(cell.row)}'] = "Bunker menor" #CONSTRUÇÃO EM POSSE
                    ws[f'{get_column_letter(cell.column + 16)}{(cell.row)}'] = "31" #TEMPO DE POSSE DA CONSTRUÇÃO
                    wb.save(file)
                    n += 1
                    id = "bunker menor"
                else:
                    n += 0
    elif interaction.values[0] == "bunker_maior":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 15)}{(cell.row)}'] = "Bunker maior" #CONSTRUÇÃO EM POSSE
                    ws[f'{get_column_letter(cell.column + 16)}{(cell.row)}'] = "31" #TEMPO DE POSSE DA CONSTRUÇÃO
                    wb.save(file)
                    n += 1
                    id = "bunker maior"
                else:
                    n += 0
    elif interaction.values[0] == "predio":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    ws[f'{get_column_letter(cell.column + 15)}{(cell.row)}'] = "Prédio" #CONSTRUÇÃO EM POSSE
                    ws[f'{get_column_letter(cell.column + 16)}{(cell.row)}'] = "31" #TEMPO DE POSSE DA CONSTRUÇÃO
                    wb.save(file)
                    n += 1
                    id = "prédio"
                else:
                    n += 0
    
    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado um registro do usuário em questão!")
        embedVar.set_footer(text="Caso você ache que isso é um engano, contate o DEV!")
        await ctx.send(embed = embedVar)
        return

    confirmacao = discord.Embed(title="✅ Adicionado com sucesso!", description=f"Foi adicionado a vantagem `{id}` com sucesso ao jogador {member.name}!", colour=discord.Colour.random())
    confirmacao.set_footer(text="Caso tenha alguma dúvida, entre em contato com o DEV.")

    await ctx.send(embed=confirmacao)

@bot.command(name="vipmod")
async def vipmod(ctx, member:discord.Member):

    if update_state == "ON":
        warning = await ctx.send("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761)

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar esse comando!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    await ctx.message.delete()

    def check_message(msg):
        return msg.author == ctx.author

    member_id = "`" + str(member.id) + "`"

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                n += 1
                embedVar = discord.Embed(title=f"<:vip:958581319418384395> Modificação de benefícios do {member.name}", description="Por favor, selecione o benefício que deseja modificar.", colour=discord.Colour.random())
                embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・O comando deixará de funcionar em 10 segundos.\n・Ignore a mensagem _'interação falhou'_, é um bug do Discord.")
                embedVar.set_author(name=member.name, icon_url=member.avatar_url)
                embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
                mensagem_select = await ctx.send(embed=embedVar, components=[Select(
        placeholder="Adicionar tipo de doação",
        options=[
            SelectOption(label="Fila prioritária (dias)", value="filaprioritaria", emoji="⭐"),
            SelectOption(label="Seguro de veículos (dias)", value="seguro_de_veiculos_dias", emoji="🚘"),
            SelectOption(label="Seguro de veículos (quantidade)", value="seguro_de_veiculos_quantidade", emoji="🚘"),
            SelectOption(label="Seguro de helicopteros (dias)", value="seguro_de_heli_dias", emoji="🚁"),
            SelectOption(label="Seguro de helicopteros (quantidade)", value="seguro_de_heli_quantidade", emoji="🚁"),
            SelectOption(label="Tipo de construção", value="tipo_de_construcao", emoji="🏠"),
            SelectOption(label="Dias da construção", value="dias_de_construcao", emoji="🏠")
        ],
        custom_id='MOD_List'
    )])

    interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'MOD_List' and inter.user == ctx.author, timeout=10)
    await mensagem_select.delete()


    if interaction.values[0] == "filaprioritaria":
        embedVar = discord.Embed(title=f"Alterar fila prioritária de {member.name}", description=f"Por favor, digite a quantidade de dias que você deseja colocar para a fila prioritária de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.\n・Caso você modifique os dias para 0, a fila prioritária será automaticamente desativada no banco de dados.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        if message.content == '0':
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 17)}{cell.row}'] = '❌'
                        ws[f'{get_column_letter(cell.column + 18)}{cell.row}'] = '0'
                        wb.save(file)

        else:
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 17)}{cell.row}'] = '✅'
                        ws[f'{get_column_letter(cell.column + 18)}{cell.row}'] = str(message.content)
                        wb.save(file) 

    elif interaction.values[0] == "seguro_de_veiculos_dias":
        embedVar = discord.Embed(title=f"Alterar seguro de veículos de {member.name}", description=f"Por favor, digite a quantidade de dias que você deseja colocar para o seguro de veículos de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.\n・Caso você modifique os dias para 0, o seguro de veículos será automaticamente desativado no banco de dados.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        if message.content == '0':
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 9)}{cell.row}'] = '❌'
                        ws[f'{get_column_letter(cell.column + 10)}{cell.row}'] = '0'
                        wb.save(file)
        else:
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 9)}{cell.row}'] = '✅'
                        ws[f'{get_column_letter(cell.column + 10)}{cell.row}'] = str(message.content)
                        wb.save(file)
    
    elif interaction.values[0] == "seguro_de_veiculos_quantidade":
        embedVar = discord.Embed(title=f"Alterar seguro de veículos de {member.name}", description=f"Por favor, digite a quantidade de seguros que você deseja colocar para o seguro de veículos de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 11)}{cell.row}'] = str(message.content)
                        wb.save(file)

    elif interaction.values[0] == "seguro_de_heli_dias":
        embedVar = discord.Embed(title=f"Alterar o seguro de helicopteros de {member.name}", description=f"Por favor, digite a quantidade de dias que você deseja colocar para o seguro de helicopteros de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.\n・Caso você modifique os dias para 0, o seguro de helicopteros será automaticamente desativado do nosso banco de dados.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        if message.content == '0':
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 12)}{cell.row}'] = '❌'
                        ws[f'{get_column_letter(cell.column + 13)}{cell.row}'] = '0'
                        wb.save(file)
        else:
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 12)}{cell.row}'] = '✅'
                        ws[f'{get_column_letter(cell.column + 13)}{cell.row}'] = str(message.content)
                        wb.save(file)

    elif interaction.values[0] == "seguro_de_heli_quantidade":
        embedVar = discord.Embed(title=f"Alterar seguro de helicopteros de {member.name}", description=f"Por favor, digite a quantidade de seguros que você deseja colocar para o seguro de helicopteros de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 14)}{cell.row}'] = str(message.content)
                        wb.save(file)
    
    elif interaction.values[0] == "tipo_de_construcao":
        embedVar = discord.Embed(title=f"Mudar tipo de construção em posse de {member.name}", description=f"Por favor, selecione a nova construção a ser colocada em posse de {member.mention}", colour=discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar, components=[Select(
        placeholder="Tipo de construção",
        options=[
            SelectOption(label="Bunker pequeno", value="bunker_pequeno", emoji="🏠"),
            SelectOption(label="Bunker médio", value="bunker_medio", emoji="🏠"),
            SelectOption(label="Prédio", value="predio", emoji="🏠")
        ],
        custom_id='MOD_List_Cons'
        )])

        interaction_ = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'MOD_List_Cons' and inter.user == ctx.author)

        if interaction_.values[0] == "bunker_pequeno":
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 15)}{cell.row}'] = "Bunker pequeno"
                        wb.save(file)
        
        elif interaction_.values[0] == "bunker_medio":
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 15)}{cell.row}'] = "Bunker médio"
                        wb.save(file)
        
        elif interaction_.values[0] == "predio":
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 15)}{cell.row}'] = "Prédio"
                        wb.save(file)
        
    elif interaction.values[0] == "dias_de_construcao":
        embedVar = discord.Embed(title=f"Alterar tempo de construção {member.name}", description=f"Por favor, digite a quantidade de dias que você deseja colocar para a construção em posse de {member.name}", colour = discord.Colour.random())
        embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá modificar os benefícios.\n・Caso tenha se equivocado no comando, apenas ignore **POR 15 SEGUNDOS**.\n・Caso você modifique os dias para 0, a posse da construção será automaticamente desativada do nosso banco de dados.")
        embedVar.set_author(name=member.name, icon_url=member.avatar_url)
        embedVar.set_footer(text="Caso tenha algum problema com esse comando, contate o DEV.")
        mensagem = await ctx.send(embed=embedVar)
        message = await bot.wait_for("message", timeout=15, check=check_message)
        if message.content == '0':
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 15)}{cell.row}'] = '❌'
                        ws[f'{get_column_letter(cell.column + 16)}{cell.row}'] = '0'
                        wb.save(file)
        else:
            for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
                for cell in row:
                    if cell.value == member_id:
                        ws[f'{get_column_letter(cell.column + 16)}{cell.row}'] = str(message.content)
                        wb.save(file)

    embedVar = discord.Embed(title="✅ Alterado com sucesso", description=f"Os benefícios de {member.name} foram alterados com sucesso do nosso banco de dados")
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)
    embedVar.set_footer(text="Caso tenha alguma dúvida, entre em contato com o DEV.")

    await mensagem.delete()
    mensagem = await ctx.send(embed=embedVar)
    await message.delete()
    time.sleep(8)
    await mensagem.delete()
    
@bot.command(name="da")
async def doacoesanuncios(ctx):
    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761)

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    await ctx.message.delete()
    await ctx.send(file=discord.File('images/doacoes.png'))

    embedVar = discord.Embed(title="DOAÇÕES PARA O STATE OF WAR", description="Aprenda aqui como doar para o servidor!", colour = discord.Colour.random())
    embedVar.add_field(name="Porque doar?", value="Doar é uma maneira de ajudar o nosso servidor se manter ativo. Todo dinheiro recebido será investido em melhoras de equipamentos, host e qualidade do servidor.", inline=False)
    embedVar.add_field(name="Qual quantia eu posso doar?", value="Nós aceitamos doações de valores dentro de uma tabela de preços, para melhor administração do dinheiro.", inline=False)
    embedVar.add_field(name="Como posso doar?", value="Para ter mais informações sobre como ajudar nosso servidor, clique no botão abaixo!")
    embedVar.set_footer(text="➝ Caso o Bot estiver offline, esse comando não vai funcionar!")

    inicio = discord.Embed(title="Obrigado!", description="Obrigado por considerar faze uma doação ao nosso servidor!\nSegue abaixo uma lista com todos as vantagens das doações!", colour= discord.Colour.random())
    inicio.add_field(name="Mas... Como eu posso doar?", value="Abra um ticket e entre em contato com um Administrador, enviado o tipo de doação e o comprovante de pagamento.")
    inicio.set_footer(text="©️ Todos os direitos reservados.")

    await ctx.send(embed=embedVar, components=[Button(label="Saiba mais!", style=ButtonStyle.green, custom_id="more_info_vip")])

    while True:
        interaction = await bot.wait_for('button_click', check=lambda i: i.custom_id == "more_info_vip")
        await interaction.user.send(embed=inicio)
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send("```diff\n-DOAÇÃO FILA PRIORITÁRIA       (R$30,00 MENSAL)\n-DOAÇÃO SEGURO DE VEÍCULOS     (R$30,00 MENSAL)\n-DOAÇÃO SEGURO DE HELICOPTEROS (R$50,00 MENSAL)\n-DOAÇÃO CARLOCKPICK            (R$50,00)```")
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send("```diff\n-DOAÇÃO PACK DE ARMAS 1\n-5 ARMAS DE RUSH\n-VALOR: R$10,00```")
        await interaction.user.send("```diff\n-DOAÇÃO PACK DE ARMAS 2\n-5 SNIPERS .338\n-VALOR: R$10,00```")
        await interaction.user.send("```diff\n-DOAÇÃO PACK DE ARMAS 3\n-10 ARMAS DE RUSH\n-VALOR: R$20,00```")
        await interaction.user.send("```diff\n-DOAÇÃO PACK DE ARMAS 4\n-10 SNIPERS .338\n-VALOR: R$20,00```")
        await interaction.user.send("```diff\n-DOAÇÃO PACK DE ARMAS CABULOSO\n-20 ARMAS DA SUA ESCOLHA\n-VALOR: R$50,00```")
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/1milhao.png"))
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/2milhoes.png"))
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/4milhoes.png"))
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/BUNKER PEQUENO.png"))
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/BUNKER GRANDE.png"))
        await interaction.user.send(file=discord.File("images/divisoria.gif"))
        await interaction.user.send(file=discord.File("images/PREDIO.png"))
    return

@bot.command(name="punir")
async def punir(ctx, member:discord.Member):
    
    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761) #ID DE ADMINISTRADOR SUPREMO

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    await ctx.message.delete() 

    member_id = member.id
    member_id = str(member_id)
    member_id = "`"+member_id+"`"
    n = 0

    embedVar = discord.Embed(title=f"🚨 Punir {member.name}", description=f"Selecione o tipo de punição que você deseja adicionar ao jogador {member.name}", colour = discord.Colour.random())
    embedVar.add_field(name="Observações:", value="・Por questões de segurança, apenas o autor do comando poderá adicionar a punição.\n・Caso tenha se equivocado no comando, apenas ignore.\n・Ignore o erro _Esta interação falhou_, isso é apenas um erro do Discord.")
    embedVar.set_footer(text="Caso tenha alguma duvida, entre em contato com o DEV.")
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)

    mensagem = await ctx.send(embed=embedVar, components=[Select(placeholder="Punição", custom_id="punicao", options=[
        SelectOption(label="Infração", value="infracao", emoji="🚨"),
        SelectOption(label="Advertência", value="advertencia", emoji="🚨"),
        SelectOption(label="Banimento", value="banimento", emoji="🚨")
    ])])
    interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'punicao' and inter.user == ctx.author)

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    if interaction.values[0] == "infracao":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    antigo = ws.cell(row=cell.row, column=6).value
                    antigo = int(antigo)
                    novo = antigo + 1
                    novo = str(novo)
                    ws[f'{get_column_letter(cell.column + 5)}{(cell.row)}'] = novo #POSSUI FILA PRIORITARIA
                    wb.save(file)
                    n += 1
                else:
                    n += 0
    
    elif interaction.values[0] == "advertencia":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    antigo = ws.cell(row=cell.row, column=7).value
                    antigo = int(antigo)
                    novo = antigo + 1
                    novo = str(novo)
                    ws[f'{get_column_letter(cell.column + 6)}{(cell.row)}'] = novo #POSSUI FILA PRIORITARIA
                    wb.save(file)
                    n += 1
                else:
                    n += 0
    
    elif interaction.values[0] == "banimento":
        for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
            for cell in row:
                if cell.value == member_id:
                    antigo = ws.cell(row=cell.row, column=8).value
                    antigo = int(antigo)
                    novo = antigo + 1
                    novo = str(novo)
                    ws[f'{get_column_letter(cell.column + 7)}{(cell.row)}'] = novo #POSSUI FILA PRIORITARIA
                    wb.save(file)
                    n += 1
                else:
                    n += 0

    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado um registro do usuário em questão!")
        embedVar.set_footer(text="Caso você ache que isso é um engano, contate o DEV!")
        await ctx.send(embed = embedVar)
        return
    
    await mensagem.delete()

    embedVar = discord.Embed(title="🚨 Punição concedida", description=f"Foi adicionado com sucesso a punição ao jogador {member.name}", colour=discord.Colour.random())
    embedVar.set_author(name=member.name, icon_url=member.avatar_url)
    embedVar.set_footer(text="Caso tenha alguma dúvida, entre em contato com o DEV.")

    mensagem = await ctx.send(embed=embedVar)
    time.sleep(8)
    await mensagem.delete()
    return

@bot.command(name="clan_criar")
async def clan_criar(ctx, tag, r=0, g=0, b=0):

    if r == 0 or r == '0':
        if g == 0 or g == '0':
            if b == 0 or b == '0':
                no_colour = True
    
    else:
        r,g,b = int(r), int(g), int(b)

    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    id = ctx.author.id
    member_id = "`" + str(id) + "`"

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active
    n = 0

    for row in wsr.iter_cols(min_col=9, max_col=9, min_row=1):
        for cell in row:
            if cell.value == f'{tag}' and cell.value != None:
                warning = await ctx.send("⚠️ Já existe um clan com esse nome!\n⚠️ Por favor, tente outro nome.")
                time.sleep(8)
                await warning.delete()
                return
            elif cell.value == (f"{tag} " + "(Líder)") and cell.value != None:
                warning = await ctx.send("⚠️ Já existe um clan com esse nome!\n⚠️ Por favor, tente outro nome.")
                time.sleep(8)
                await warning.delete()
                return

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                clan = ws.cell(row=cell.row, column=9).value
                n += 1
            else:
                n += 0 
                
    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Você não foi encontrado em nosso banco de dados!", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="Por favor, entre em contato urgentemente com o DEV.")
        await ctx.reply(embed = embedVar)
        return

    if clan != "Não participante":
        embedVar = discord.Embed(title=f"⚠️ Você já pertence ao clan {clan}!", description="Não foi possível criar um novo clan pois você já pertence a um!", colour=discord.Colour.random())
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.reply(embed = embedVar)
        return
    else:
        pass

    if no_colour:
        role = await ctx.guild.create_role(name=f"{tag}", colour=discord.Colour.random(), hoist = True)
    else:
        role = await ctx.guild.create_role(name=f"{tag}", colour=discord.Colour.from_rgb(r, g, b), hoist=True)

    await ctx.author.add_roles(role)

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                ws[f'{get_column_letter(cell.column + 8)}{(cell.row)}'] = f"{tag}" + " (Líder)"
                wb.save(file)
    

    embedVar = discord.Embed(title=f"O clan {tag} foi criado com sucesso!", description=f"O líder do mais novo clan {tag} é o {ctx.author.name}", colour=discord.Colour.random())
    embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embedVar.add_field(name="Observações:", value="・Somente o líder do clan poderá convidar e expulsar membros do clan.\n・Para modificar a TAG ou a cor do clan, entre em contato com um ADM.\n・Usar `!clan_excluir` irá deletar o clan permanentemente.")
    embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
    await ctx.reply(embed=embedVar)
    await role.edit(position=6)
    return

@bot.command(name="clan_sair")
async def clan_sair(ctx):
      
    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    id = ctx.author.id
    member_id = "`" + str(id) + "`"

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active
    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                clan = ws.cell(row=cell.row, column=9).value
                n += 1
            else:
                n += 0

    clan_ = clan

    if clan == "Não participante":
        embedVar = discord.Embed(title="⚠️Error 401", description="Você não participa de um clan", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
        return
    
    if "Líder" in clan:
        embedVar = discord.Embed(title="⚠️Error 403", description="Você é líder do seu clan!\nVocê não pode abandonar o seu clan, mas você pode excluí-lo.", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed=embedVar)
        return

    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado o seu registro em nosso servidor!", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="Por favor, entre em contato com o DEV.")
        await ctx.send(embed = embedVar)
        return

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                ws[f'{get_column_letter(cell.column + 8)}{(cell.row)}'] = "Não participante"
                wb.save(file)

    for role in ctx.guild.roles:
        if role.name == f"{clan_}":
            await ctx.author.remove_roles(role)

    embedVar = discord.Embed(title="✔️ Você saiu do clan com sucesso!", description = f"Agora você nao faz mais parte do clan {clan_}")
    embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
    await ctx.message.reply(embed = embedVar)

    return

@bot.command(name="clan_expulsar")
async def clan_expulsar(ctx, member:discord.Member):

    if update_state == "ON":
        warning = await ctx.reply("Estamos atualizando o nosso banco de dados. Por favor, tente novamente mais tarde\n_Esse processo não costuma demorar muito_\nCaso você ache que isso seja um erro, entre em contato com o DEV.")
        time.sleep(10)
        await warning.delete()
        await ctx.message.delete()
        return

    id = ctx.author.id
    member_id = "`" + str(id) + "`"

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active
    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                clan = ws.cell(row=cell.row, column=9).value
                n += 1
            else:
                n += 0

    if clan == "Não participante":
        embedVar = discord.Embed(title="⚠️Error 401", description="Você não participa de um clan", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
        return
    
    if not "Líder" in clan:
        embedVar = discord.Embed(title="⚠️Error 403", description="Você não é líder do seu clan", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed=embedVar)
        return

    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado o seu registro em nosso servidor!", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="Por favor, entre em contato com o DEV.")
        await ctx.send(embed = embedVar)
        return
    
    clan_ = clan[:-8]

    member_id = "`" + str(member.id) + "`"

    n = 0

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                clan = ws.cell(row=cell.row, column=9).value
                n += 1
            else:
                n += 0

    if clan == "Não participante":
        embedVar = discord.Embed(title="⚠️Error 401", description="O usuário em questão não participa de nenhum clan", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
        return
    
    if clan != clan_:
        embedVar = discord.Embed(title="⚠️Error 401", description="O usuário em questão não participa do seu clan", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
        return
    
    if n == 0:
        embedVar = discord.Embed(title="⚠️Error 404", description="Não foi encontrado o registro do usuário em questão em nosso servidor!", colour=discord.Colour.random())
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="Por favor, entre em contato com o DEV.")
        await ctx.send(embed = embedVar)
        return

    for row in wsr.iter_rows(wsr.min_row, wsr.max_row):
        for cell in row:
            if cell.value == member_id:
                ws[f'{get_column_letter(cell.column + 8)}{(cell.row)}'] = "Não participante"
                wb.save(file)
    
    for role in ctx.guild.roles:
        if role.name == f"{clan_}":
            await member.remove_roles(role)
    
    embedVar = discord.Embed(title=f"✔️ Você expulsou o {member.name} com sucesso", colour = discord.Colour.random())
    embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embedVar.set_footer(text="Por favor, entre em contato com o DEV.")
    await ctx.send(embed = embedVar)
    return

@bot.command(name="ajuda")
async def ajuda(ctx):
    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761)
    if check_1 in ctx.author.roles:
        embedVar = discord.Embed(title="🤖 Ajuda do Bot State of War", description="Uma lista de ajuda feita para administradores do State of War\nSelecione o tipo de ajuda que você deseja receber nas opções abaixo!", colour=discord.Colour.random())
        embedVar.add_field(name="`!ajuda`", value="Mostra uma tabela de como usar os comandos disponiveis do bot.")
        embedVar.add_field(name="`!code [CODIGO]`", value="Vincula a sua Steam ao nosso sistema. Isso nos ajudará a otimizar o nosso suporte dinâmico. Recomendamos a todos vincularem suas contas.")
        embedVar.add_field(name="`!perfil`", value="Mostra como está a sua ficha em nosso servidor")
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        mensagem = await ctx.reply(embed=embedVar, components=[Select(placeholder="Ajudas", custom_id="help", options=[
            SelectOption(label="Administração", value="adm", emoji="⚙️"),
            SelectOption(label="Clan", value="clan", emoji="🛡️")
        ])])

        interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'help' and inter.user == ctx.author)
        if interaction.values[0] == "adm":
            embedVar = discord.Embed(title="⚙️ Administração", description="Uma lista com comandos administrativos.", colour=discord.Colour.random())
            embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embedVar.add_field(name="`!ficha [@usuario]`", value="Mostra a ficha administrativa do usuário em questão.")
            embedVar.add_field(name="`!vipadd [@usuario]`", value="Adiciona uma vantagem para o usuário em questão.")
            embedVar.add_field(name="`!vipmod [@usuario]`", value="Modifica alguma vantagem do usuário em questão.")
            embedVar.add_field(name="`!punir [@usuario]`", value="Adiciona uma punição para o usuário em questão (infração, advertência ou banimento)")
            embedVar.add_field(name="`!enquete [TITULO]/[CONTEUDO]`", value="Cria uma enquete dinâmica. Os parametros Titulo/Conteudo são obrigatórios. **O Título e o Conteudo devem ser separados por '/'.**")
            embedVar.add_field(name="`!registrarall`", value="Registra todos os usuários novamente no banco de dados **(consulte o DEV antes de usar esse comando, pode gerar problemas em todo o banco de dados)**.")
            embedVar.add_field(name="`!da`", value="Anuncia a mensagem de doação do servidor. Usar quando o botão 'Saiba mais' apresentar alguma falha.")
            embedVar.add_field(name="`!regras_1`", value="Anuncia as regras que estão na memória do bot.", inline=True)
            embedVar.add_field(name="ㅤ", value="ㅤ")
            embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
            await mensagem.edit(embed=embedVar)
        elif interaction.values[0] == "clan":
            embedVar = discord.Embed(title="🛡️ Clan", description="Uma lista com comandos para clan.", colour=discord.Colour.random())
            embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embedVar.add_field(name="`!clan_criar [TAG] [R] [G] [B]`", value="Cria um clã com a sua TAG. Os parametros R,G,B podem são opcionais e, caso deixados em branco, a cor do seu clan será alatória.", inline=False)
            embedVar.add_field(name="`!clan_excluir`", value="Exclui o clan ao qual você possuí cargo de líder.", inline=False)
            embedVar.add_field(name="`!clan_convidar [@usuario]`", value="Envia um covite no privado do usuário em questão ao qual você deseja convidar para o seu clan.\nÉ importante que esse usuário em questão permita, nas configurações do Discord, receber mensagens de bots.",inline=False)
            embedVar.add_field(name="`!clan_sair`", value="Sai do clan em que você está participando. Líderes não podem sair do próprio clan.", inline=False)
            embedVar.add_field(name="`!clan_expulsar [@usuario]`", value="Expulsa o usuário em questão. Comando disponível apenas para os líderes de clan.", inline=False)
            embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
            await mensagem.edit(embed=embedVar)
    else:
        embedVar = discord.Embed(title="🤖 Ajuda do Bot State of War", description="Uma lista de ajuda feita para administradores do State of War\nSelecione o tipo de ajuda que você deseja receber nas opções abaixo!", colour=discord.Colour.random())
        embedVar.add_field(name="`!ajuda`", value="Mostra uma tabela de como usar os comandos disponiveis do bot.")
        embedVar.add_field(name="`!code [CODIGO]`", value="Vincula a sua Steam ao nosso sistema. Isso nos ajudará a otimizar o nosso suporte dinâmico. Recomendamos a todos vincularem suas contas.")
        embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        mensagem = await ctx.reply(embed=embedVar, components=[Select(placeholder="Ajudas", custom_id="help", options=[
            SelectOption(label="Clan", value="clan", emoji="🛡️")
        ])])
        interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'help' and inter.user == ctx.author)
        if interaction.values[0] == "clan":
            embedVar = discord.Embed(title="🛡️ Clan", description="Uma lista com comandos para clan.", colour=discord.Colour.random())
            embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embedVar.add_field(name="`!clan_criar [TAG] [R] [G] [B]`", value="Cria um clã com a sua TAG. Os parametros R,G,B podem são opcionais e, caso deixados em branco, a cor do seu clan será alatória.", inline=False)
            embedVar.add_field(name="`!clan_excluir`", value="Exclui o clan ao qual você possuí cargo de líder.", inline=False)
            embedVar.add_field(name="`!clan_convidar [@usuario]`", value="Envia um covite no privado do usuário em questão ao qual você deseja convidar para o seu clan.\nÉ importante que esse usuário em questão permita, nas configurações do Discord, receber mensagens de bots.", inline=False)
            embedVar.add_field(name="`!clan_sair`", value="Sai do clan em que você está participando. Líderes não podem sair do próprio clan.", inline=False)
            embedVar.add_field(name="`!clan_expulsar [@usuario]`", value="Expulsa o usuário em questão. Comando disponível apenas para os líderes de clan.", inline=False)
            embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
            await mensagem.edit(embed=embedVar)
    return

@bot.command(name="registrar")
async def registrar(ctx, member:discord.Member):

    check_1 = discord.utils.get(ctx.guild.roles, id=947242380040478761) #ID DE ADMINISTRADOR SUPREMO

    if check_1 in ctx.author.roles:
        pass
    else:
        warning = await ctx.reply("Você não tem permissão para usar isso!")
        time.sleep(8)
        await warning.delete()
        await ctx.message.delete()
        return

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    id = member.id
    id = str(id)
    id = "`"+id+"`"
    name = member.name
    discriminator = member.discriminator
    nickname = name + "#" + discriminator
    ws[f'{get_column_letter(ws.min_column + 0)}{(ws.max_row + 1)}'] = id
    ws[f'{get_column_letter(ws.min_column + 1)}{(ws.max_row)}'] = nickname
    ws[f'{get_column_letter(ws.min_column + 5)}{(ws.max_row)}'] = "0" #INFRAÇÕES
    ws[f'{get_column_letter(ws.min_column + 6)}{(ws.max_row)}'] = "0" #ADVERTÊNCIAS
    ws[f'{get_column_letter(ws.min_column + 7)}{(ws.max_row)}'] = "0" #BANIMENTOS
    ws[f'{get_column_letter(ws.min_column + 8)}{(ws.max_row)}'] = "Não participante" #CLÃ
    ws[f'{get_column_letter(ws.min_column + 9)}{(ws.max_row)}'] = "❌" #SEGURO DE VEICULOS
    ws[f'{get_column_letter(ws.min_column + 10)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
    ws[f'{get_column_letter(ws.min_column + 11)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE VEICULOS
    ws[f'{get_column_letter(ws.min_column + 12)}{(ws.max_row)}'] = "❌" #SEGURO DE HELICOPTEROS
    ws[f'{get_column_letter(ws.min_column + 13)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
    ws[f'{get_column_letter(ws.min_column + 14)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE HELICOPTEROS
    ws[f'{get_column_letter(ws.min_column + 15)}{(ws.max_row)}'] = "❌" #POSSUI ALGUMA CONSTRUÇÃO
    ws[f'{get_column_letter(ws.min_column + 16)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES DA CONSTRUÇÃO
    ws[f'{get_column_letter(ws.min_column + 17)}{(ws.max_row)}'] = "❌" #POSSUI FILA PRIORITARIA
    ws[f'{get_column_letter(ws.min_column + 18)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES 
    wb.save(file)

@bot.event
async def on_message(message):

    await bot.process_commands(message)
    
    if message.channel.id == 960055351833677875:
        interaction = await bot.fetch_user(id)

    if message.author.id == 912310660669521921:
        return

    sugestao_banidas = ['inclinado','pescoço torto','torto','inclinar','inclinação','inclinacao','perninha quebrada','enclinadinha','enclinada','enclinacao','enclinação','pescoço','pescosso','cabeçinha','cabessinha','cabesinha','deitar para o lado','deitar pro lado','deitar de lado']
    if message.channel.id == 957398409319440494:

        for word in sugestao_banidas:
            if word in message.content:
                warning = await message.reply("Nos não iremos colocar inclinação no servidor!")
                await message.delete()
                time.sleep(10)
                await warning.delete()
                return

        await message.add_reaction('✅')
        await message.add_reaction('❌')

@bot.event
async def on_member_remove(member):
    guild = bot.get_guild(947237264596041728)
    member_count = guild.member_count
    activity = discord.Activity(name="Sobreviventes ➝ ({})".format(member_count), type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)

    channel = bot.get_channel(959881836241248276)

    author = member.name
    pic = member.avatar_url

    embedVar = discord.Embed(title=f"🧟‍♂️|**{author}**| foi mordido por um zumbi!", description=f"Infelizmente, {author} não está mais conosco. Agora somos {member_count} sobreviventes.", colour = discord.Colour.random())
    embedVar.set_author(name=author, icon_url=pic)
    embedVar.set_thumbnail(url=pic)
    embedVar.set_image(url="https://i.imgur.com/1td2WQv.png")
    embedVar.set_footer(text="©️ Todos os direitos reservados.")

    await channel.send(embed=embedVar)
    return

@bot.event
async def on_member_join(member):

    if update_state == "ON":
        time.sleep(1000)

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    role = discord.utils.get(member.guild.roles, name='Sobreviventes')

    await member.add_roles(role)
    guild = bot.get_guild(947237264596041728)
    member_count = guild.member_count
    activity = discord.Activity(name="Sobreviventes ➝ ({})".format(member_count), type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)

    ID_REGRAS = 947238415013916692
    channel = bot.get_channel(947237264596041730) 
    guild = bot.get_guild(947237264596041728)
    member_count = guild.member_count
    author = member.name
    pic = member.avatar_url

    embedVar = discord.Embed(title="<a:welcome:958517359667187783> | Bem-vindo(a)! | <a:welcome:958517359667187783>", description="__**{}**__, seja bem-vindo ao State of War! Você é {}º membro a entrar na comunidade!".format((author),(member_count)), colour = discord.Colour.random())
    embedVar.set_author(name=author, icon_url=pic)
    embedVar.set_footer(text="©️ Todos os direitos reservados.")
    embedVar.set_image(url="https://i.imgur.com/pNBsQTi.jpg")
    embedVar.add_field(name="Evite punições :rotating_light:", value="Leia as regras em <#{}> e fique por dentro das diretrizes da nossa comunidade.".format(ID_REGRAS), inline=False)
    embedVar.set_thumbnail(url=pic)
    await channel.send(embed=embedVar)

    id = member.id
    id = str(id)
    id = "`"+id+"`"
    name = member.name
    discriminator = member.discriminator
    nickname = name + "#" + discriminator

    ws[f'{get_column_letter(ws.min_column + 0)}{(ws.max_row + 1)}'] = id
    ws[f'{get_column_letter(ws.min_column + 1)}{(ws.max_row)}'] = nickname
    ws[f'{get_column_letter(ws.min_column + 5)}{(ws.max_row)}'] = "0" #INFRAÇÕES
    ws[f'{get_column_letter(ws.min_column + 6)}{(ws.max_row)}'] = "0" #ADVERTÊNCIAS
    ws[f'{get_column_letter(ws.min_column + 7)}{(ws.max_row)}'] = "0" #BANIMENTOS
    ws[f'{get_column_letter(ws.min_column + 8)}{(ws.max_row)}'] = "Não participante" #CLAN
    ws[f'{get_column_letter(ws.min_column + 9)}{(ws.max_row)}'] = "❌" #SEGURO DE VEICULOS
    ws[f'{get_column_letter(ws.min_column + 10)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
    ws[f'{get_column_letter(ws.min_column + 11)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE VEICULOS
    ws[f'{get_column_letter(ws.min_column + 12)}{(ws.max_row)}'] = "❌" #SEGURO DE HELICOPTEROS
    ws[f'{get_column_letter(ws.min_column + 13)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES
    ws[f'{get_column_letter(ws.min_column + 14)}{(ws.max_row)}'] = "Indefinido" #QUANTOS SEGUROS RESTANTES DE HELICOPTEROS
    ws[f'{get_column_letter(ws.min_column + 15)}{(ws.max_row)}'] = "❌" #POSSUI ALGUMA CONSTRUÇÃO
    ws[f'{get_column_letter(ws.min_column + 16)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES DA CONSTRUÇÃO
    ws[f'{get_column_letter(ws.min_column + 17)}{(ws.max_row)}'] = "❌" #POSSUI FILA PRIORITARIA
    ws[f'{get_column_letter(ws.min_column + 18)}{(ws.max_row)}'] = "0" #QUANTOS DIAS RESTANTES 
    wb.save(file)
    return
    
@bot.event
async def on_ready():
    print("Bot online")
    guild = bot.get_guild(947237264596041728)
    member_count = guild.member_count
    activity = discord.Activity(name="Sobreviventes ➝ ({})".format(member_count), type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    update_days.start()
    return

n = 0
@tasks.loop(hours=24)
async def update_days():

    global update_state

    file = "banco de dados.xlsx"
    wb = openpyxl.load_workbook(filename=file)
    ws = wb.worksheets[0]
    wsr = wb.active

    global n

    if n != 1: #IF para não permitir que desconte 1 dia dos VIPs só por ligar o bot
        n += 1
        return 
    
    update_state = "ON"

    channel = bot.get_channel(960022037794025522)

    async def update(coluna):
        if coluna == 11:
            beneficio = "Seguro de Veiculos"
        if coluna == 14:
            beneficio = "Seguro de Helicopteros"
        if coluna == 17:
            beneficio = "Base VIP"
        if coluna == 19:
            beneficio = "Fila prioritária"

        status = "normal"

        for row in wsr.iter_cols(min_col=coluna, max_col=coluna, min_row=1):
                for cell in row:
                    if cell.value != '0' and cell.value != None:
                        idd = ws.cell(row=cell.row, column=1).value
                        idd = idd.replace("`","")
                        antigo = int(cell.value)
                        novo = antigo - 1
                        ws[f'{get_column_letter(cell.column)}{(cell.row)}'] = str(novo) #TEMPO RESTANTE DA VILA PRIORITARIA
                        if str(novo) == '0':
                            ws[f'{get_column_letter(cell.column -1)}{(cell.row)}'] = '❌'
                            status = "acabou"
                        wb.save(file)
                        if str(novo) == '3':
                            status = "quase"

        if status == "quase":
            user = await bot.fetch_user(idd)
            embedVar = discord.Embed(title="⚠️ Atenção!", description=f"O benefício de `{beneficio}` de {user.name}, portador do Discord ID {idd} está a 3 dias do seu fim", colour=discord.Colour.random())
            embedVar.set_footer(text="Se precisar de ajuda, entre em contato com o DEV.")
            await channel.send(embed = embedVar)

            embedVar = discord.Embed(title="⚠️ Atenção!", description=f"Faltam 3 dias para seu benefício de `{beneficio}` acabar! Você pode renovar criando um ticket na aba de Financeiro!", colour=discord.Colour.random())
            embedVar.set_footer(text="Se precisar de ajuda, entre em contato com o DEV.")
            await user.send(embed = embedVar)
        
        if status == "acabou":
            user = await bot.fetch_user(idd)
            embedVar = discord.Embed(title="⚠️ Atenção!", description=f"O benefício de `{beneficio}` de {user.name}, portador do Discord ID {idd} **acabou**!", colour=discord.Colour.random())
            embedVar.set_footer(text="Se precisar de ajuda, entre em contato com o DEV.")
            await channel.send(embed = embedVar)

            embedVar = discord.Embed(title="⚠️ Atenção!", description=f"O seu beneficio de `{beneficio}` acabou! Você pode renovar criando um ticket na aba de Financeiro!", colour=discord.Colour.random())
            embedVar.set_footer(text="Se precisar de ajuda, entre em contato com o DEV.")
            await user.send(embed = embedVar)
        


    await update(11)
    await update(14)
    await update(17)
    await update(19)

    update_state = "OFF"
    return

@clan_criar.error
async def clan_criarerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="⚠️ Erro na formatação do comando", colour=discord.Colour.random())
        embedVar.add_field(name="Atenção!", value="・Para criar um clan é necessário seguir estritamente o comando `!clan_criar [TAG] [R] [G] [B]`.\n**・A cor precisa estar em formato RGB!**\n・Caso não saiba o que é HEX, clique no link abaixo!\n・Por definição do Discord, a cor RGB(0,0,0) não será aceita, gernado uma cor aleatória para o clan")
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed=embedVar, components=[Button(label="Cores em formato RGB", style=ButtonStyle.URL, url="https://www.google.com/search?q=hex+color")])
    return

@code.error
async def code(ctx, error):
    if isinstance(error, UnboundLocalError):
        embedVar = discord.Embed(title="⚠️ Erro para vincular!", colour = discord.Colour.random())
        embedVar.add_field(name="Atenção:", value="Tenha certeza que a sua conta Steam está vinculada com o seu Discord, através da aba de Configurações > Minha conta > Conexões.")
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
        time.sleep(8)
        await ctx.message.delete()
    return

@doacoesanuncios.error
async def da(ctx, error):
    if isinstance(error, discord.errors.Forbidden):
        embedVar = discord.Embed(title="⚠️ Erro ao enviar as mensagens!", colour = discord.Colour.random())
        embedVar.add_field(name="Atenção:", value=f"<@{ctx.author.id}>, as configurações do seu Discord não permitem que eu te envie as inforamções no seu privado.")
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        message = await ctx.reply(embed=embedVar)
        time.sleep(20)
        await message.delete()
    return

@perfil.error
async def perfil(ctx, error):
    if isinstance(error, discord.errors.Forbidden):
        embedVar = discord.Embed(title="⚠️ As suas configuração não nos permitem te enviar mensagem no privado!", colour = discord.Colour.random())
        embedVar.add_field(name="Atenção:", value="O usuário que você estava tentando convidar não permite receber mensagens privadas de Bots no Discord. Entretanto, não consegui convida-lo!")
        embedVar.set_footer(text="➝ Se precisar de ajuda, entre em contato com o DEV.")
        await ctx.reply(embed = embedVar)
    return

bot.load_extension('cogs.Clan')
bot.run('OTEyMzEwNjYwNjY5NTIxOTIx.YZuFgw.dYqfKMJiRNDKAHJMPQVDRU3hxRk')
