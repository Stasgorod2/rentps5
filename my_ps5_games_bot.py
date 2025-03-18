from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = "7665158890:AAGGdXgefYkLFduK2OOuG8_enwes4cbzJX8"

# Полный список всех игр
all_games = [
     "11-11 Memories Retold", "A Hat in Time", "A Space for the Unbound", "A Way Out",
    "Adventure Time: Pirates of the Enchiridion", "After Us", "Age of Wonders: Planetfall",
    "Alex Kidd in Miracle World DX", "ALIENATION", "ANIMAL WELL", "ANNO: Mutationem",
    "Anodyne", "AO Tennis 2", "Aragami", "Assassin's Creed Valhalla", "Assassin's Creed Odyssey",
    "Assassin's Creed Origins", "Assassin's Creed Syndicate", "Assassin's Creed Unity",
    "Assassin's Creed Rogue Remastered", "Assassin's Creed IV Black Flag", "Assassin's Creed III Remastered",
    "Assassin's Creed The Ezio Collection", "Assetto Corsa Competizione", "Atlas Fallen",
    "Back 4 Blood", "Bad North", "Batman: Arkham Knight", "Battle Chasers: Nightwar", "Battlefield 1",
    "Battlefield 2042", "Battlefield V", "Bee Simulator", "Ben 10", "Ben 10: Power Trip", "Biped",
    "Blood Bowl 3", "Bloodborne", "Bloodstained: Ritual of the Night", "Bomber Crew", "Bound",
    "Brawlout", "Bubsy: The Woolies Strike Back", "Bugsnax", "Bus Simulator 21", "Call of Cthulhu",
    "Call of The Sea", "Car Mechanic Simulator", "Carto", "Cartoon Network: Battle Crashers",
    "Cat Quest", "Cat Quest II", "Celeste", "Chernobylite", "Chess Ultra", "Child of Light",
    "Children of Morta", "Chivalry 2", "Circus Electrique", "Cities: Skylines", "Citizen Sleeper",
    "Clash: Artifacts of Chaos", "Coffee Talk", "Coffee Talk Episode 2: Hibiscus & Butterfly",
    "Conan Exiles", "Concrete Genie", "Construction Simulator", "CONTRA: ROGUE CORPS",
    "Control: Ultimate Edition", "Cricket 24", "Crime Boss: Rockay City", "Cris Tales",
    "CRISIS CORE –FINAL FANTASY VII– REUNION", "Crusader Kings III", "Crysis Remastered",
    "Cult of the Lamb", "Cursed to Golf", "Dandara: Trials of Fear Edition", "DAVE THE DIVER",
    "Days Gone", "Dead by Daylight", "Dead Cells", "Dead Island 2", "DEAD OR ALIVE 5 Last Round",
    "DEADCRAFT", "Death end reQuest", "Death Squared", "DEATH STRANDING", "DEATH STRANDING DIRECTOR’S CUT",
    "Deceive Inc.", "Deliver Us Mars", "Deliver Us The Moon", "Demon's Souls", "Desperados III",
    "Destruction AllStars", "Detroit: Become Human", "Deus Ex: Mankind Divided", "Digimon Survive",
    "DIRT 5", "Disaster Report 4: Summer Memories", "Disco Elysium - The Final Cut",
    "DISGAEA 5: ALLIANCE OF VENGEANCE", "Dishonored 2", "Dishonored: Death of the Outsider",
    "DOOM", "DOOM Eternal", "DRAGON BALL FighterZ", "DRAGON BALL Z: KAKAROT", "Dragon Star Varnir",
    "Dreams", "DREDGE", "Dying Light 2 Stay Human", "DYNASTY WARRIORS 8 Empires", "DYNASTY WARRIORS 9",
    "EA SPORTS FC 24", "EA Sports NHL 24", "Earth Defense Force 4.1: The Shadow of New Despair",
    "EARTH DEFENSE FORCE 5", "EARTH DEFENSE FORCE: IRON RAIN", "EARTH DEFENSE FORCE: WORLD BROTHERS",
    "Eldest Souls", "Elite Dangerous", "Embr", "Empire of Sin", "Enter the Gungeon", "Entwined",
    "Erica", "Everybody’s Golf", "F.I.S.T.: Forged In Shadow Torch", "Fade to Silence", "Fallout 4",
    "Fallout 76", "FAR CRY 3: BLOOD DRAGON", "FAR CRY 6", "FAR CRY New Dawn", "FAR CRY Primal",
    "FAR: Changing Tides", "FIA European Truck Racing Championship", "FINAL FANTASY TYPE-0 HD",
    "FINAL FANTASY VII REMAKE", "FINAL FANTASY VII REMAKE INTERGRADE", "Firefighting Simulator - The Squad",
    "Football Manager 2024", "For Honor", "For The King", "Forager", "Forspoken", "Frostpunk: Console Edition",
    "Fury Unleashed", "Get Even", "Ghost of Tsushima DIRECTOR’S CUT", "Ghost Recon Breakpoint",
    "Ghostbusters: Spirits Unleashed", "Ghostrunner", "Gigantosaurus The Game", "God of War Ragnarök",
    "God of War", "Golf With Your Friends", "Grand Ages: Medieval", "Grand Theft Auto V", "Gravity Rush 2",
    "GRID Legends", "GRIS", "Hello Neighbor", "Hollow Knight: Voidheart Edition", "Hotel Transylvania: Scary-Tale Adventures",
    "Hotline Miami", "Hotline Miami 2: Wrong Number", "Hotshot Racing", "Human: Fall Flat", "HUMANITY",
    "Hundred Days - Winemaking Simulator", "I am Bread", "Ice Age: Scrat's Nutty Adventure", "Immortals Fenyx Rising",
    "Immortals of Aveum", "inFAMOUS Second Son", "inFAMOUS First Light", "Infinite Minigolf", "Inscryption",
    "It Takes Two", "Journey To The Savage Planet: Employee Of The Month", "JUMANJI: The Video Game",
    "Jurassic World Evolution 2", "Kena: Bridge of Spirits", "Killer Frequency", "Killing Floor 2",
    "KILLZONE Shadow Fall", "Kingdom: New Lands", "KNACK", "Lake", "Lawn Mowing Simulator", "LEGO Batman 3: Beyond Gotham",
    "LEGO CITY Undercover", "LEGO DC Super-Villains", "LEGO Jurassic World", "LEGO Marvel Super Heroes 2",
    "LEGO Marvel's Avengers", "LEGO NINJAGO Movie Video Game", "LEGO The Hobbit", "LEGO The Incredibles",
    "LEGO Worlds", "Life is Strange 2 Complete Season", "Life is Strange: True Colors", "Like a Dragon Gaiden: The Man Who Erased His Name",
    "Like a Dragon: Ishin!", "Little Big Workshop", "Lost Records: Bloom & Rage", "Madden NFL 23", "Magicka 2",
    "Mahjong", "Malicious Fallen", "Maneater", "Marvel's Guardians of the Galaxy", "Marvel's Spider-Man: Miles Morales",
    "MATTERFALL", "MediEvil", "Megadimension Neptunia VII", "MELTY BLOOD: TYPE LUMINA", "Miasma Chronicles",
    "Mirror's Edge Catalyst", "Monopoly Madness", "Monopoly Plus", "Monster Boy and the Cursed Kingdom",
    "Monster Energy Supercross - The Official Videogame 6", "Monster Hunter Rise", "Monster Truck Championship",
    "Moonlighter", "MORDHAU", "Mortal Kombat 11", "Mortal Shell", "MotoGP 24", "Mount & Blade II: Bannerlord",
    "MudRunner", "My Friend Peppa Pig", "Mystic Pillars - Remastered", "NARUTO TO BORUTO: SHINOBI STRIKER",
    "Need for Speed", "Need for Speed Heat", "Need for Speed Hot Pursuit Remastered", "Need for Speed Payback",
    "NHL 23", "Night in the Woods", "Nioh", "No More Heroes 3", "NOBUNAGA'S AMBITION: Taishi", "Nour: Play With Your Food",
    "Observer: System Redux", "Oddworld: New 'n' Tasty", "Oddworld: Soulstorm Enhanced Edition", "Odin Sphere Leifthrasir",
    "Omega Quintet", "Onee Chanbara Origin", "Orcs Must Die! 3", "Outlast 2", "Overcooked! All You Can Eat", "Overpass",
    "Paradise Killer", "Pathfinder: Wrath of the Righteous - Enhanced Edition", "PAW Patrol Mighty Pups Save Adventure Bay",
    "PAW Patrol The Movie: Adventure City Calls", "Paw Patrol: On a Roll!", "PAYDAY 2: CRIMEWAVE EDITION", "PHOGS!",
    "Pile Up! Box by Box", "PJ Masks: Heroes of the Night", "Plants vs. Zombies: Battle for Neighborville", "Poker Club",
    "Police Simulator: Patrol Officers", "Portal Knights", "Power Rangers: Battle For The Grid", "Prey", "Prison Architect",
    "Pure Pool", "RAGE 2", "Rainbow Six Extraction", "Rainbow Six Siege", "Rain World", "Raji: An Ancient Epic",
    "Rapala Fishing: Pro Series", "Ratchet & Clank: Rift Apart", "Rayman Legends", "ReadySet Heroes", "Rebel Galaxy",
    "Redout 2", "Remnant II", "RESIDENT EVIL 3", "RESOGUN", "Return to Monkey Island", "Returnal", "Rez Infinite",
    "Riders Republic", "RIDE 5", "Rise of the Tomb Raider: 20 Year Celebration", "River City Melee Mach!!", "Road 96",
    "Rock of Ages 3: Make & Break", "Rogue Legacy 2", "Rogue Lords", "Roguebook", "Romance of The Three Kingdoms 13",
    "Rune Factory 4 Special", "Röki", "Sackboy: A Big Adventure", "SaGa Frontier Remastered", "Sakuna: Of Rice and Ruin",
    "Salt and Sacrifice", "SAMURAI WARRIORS 5", "Sayonara Wild Hearts", "Scott Pilgrim vs. The World The Game - Complete Edition",
    "SD GUNDAM BATTLE ALLIANCE", "Secret Neighbor", "Session: Skate Sim", "Shadow of the Beast", "Shadow of the Colossus",
    "Shadow of the Tomb Raider", "Shadow Tactics: Blades of the Shogun", "Shadow Warrior 2", "Shadowrun Returns",
    "Shadowrun: Dragonfall - Director's Cut", "Shadowrun: Hong Kong - Extended Edition", "Slay the Spire", "Sniper Elite 4",
    "Sniper Elite 5", "Somerville", "Sonic Frontiers", "South Park: The Fractured But Whole", "South Park: The Stick of Truth",
    "Source of Madness", "Space Crew: Legendary Edition", "Space Engineers", "Space Hulk: Deathwing - Enhanced Edition",
    "Spirit of the North: Enhanced Edition", "Spitlings", "STAR WARS Battlefront II", "STAR WARS Jedi: Survivor",
    "STAR WARS: Squadrons", "Stellaris: Console Edition", "Stick Fight: The Game", "STORY OF SEASONS: Friends of Mineral Town",
    "STORY OF SEASONS: Pioneers of Olive Town", "Stranded Deep", "Stranded: Alien Dawn", "Stray Blade", "Street Fighter V",
    "Super Neptunia RPG", "Surviving Mars", "Surviving the Aftermath", "SWORD ART ONLINE Alicization Lycoris",
    "SWORD ART ONLINE Last Recollection", "Sword Art Online: Fatal Bullet", "Sword Art Online: Hollow Realization",
    "Tails Noir", "Tales of Kenzera: ZAU", "Tearaway Unfolded", "Teenage Mutant Ninja Turtles: Shredder's Revenge",
    "Tennis World Tour 2", "Terraria", "Tetris Effect: Connected", "The Ascent", "The Dark Pictures Anthology: House of Ashes",
    "The Dark Pictures Anthology: Little Hope", "The Dark Pictures Anthology: Man of Medan", "The Dark Pictures Anthology: The Devil in Me",
    "The Division", "The Division 2", "The Elder Scrolls Online", "The Elder Scrolls V: Skyrim Special Edition", "The Evil Within 2",
    "The Forgotten City", "The Gardens Between", "The Jackbox Party Pack 9", "The Last Guardian", "The Last of Us Part I",
    "The LEGO Movie 2 Videogame", "The LEGO Movie Videogame", "The Long Dark", "The Pedestrian", "The Plucky Squire",
    "The Sims 4 Island Living", "The Surge", "The Surge 2", "The Technomancer", "The Witch and the Hundred Knight: Revival Edition",
    "The Witcher 3: Wild Hunt", "Thief", "This War of Mine: Final Cut", "Thymesia", "Tin Hearts", "Titanfall 2",
    "Tomb Raider: Definitive Edition", "TopSpin 2K25", "Toukiden 2", "Tour De France 2023", "TowerFall Ascension",
    "Townsmen - A Kingdom Rebuilt", "Travis Strikes Again: No More", "Tricky Towers", "Trine 4: The Nightmare Prince",
    "TRON RUN/r", "Tropico 5", "Two Point Campus", "Two Point Hospital: JUMBO Edition", "UFC 4", "UFC 5",
    "UNCHARTED: Legacy of Thieves Collection", "UNO", "Uncharted: The Lost Legacy", "Under The Waves", "Undertale",
    "Until Dawn", "Untitled Goose Game", "Unravel Two", "Vampire: The Masquerade - Swansong", "Vampyr",
    "Vikings - Wolves of Midgard", "Warhammer 40,000: Inquisitor - Martyr", "Warhammer: Chaosbane",
    "Warhammer: Chaosbane Slayer Edition", "Warhammer: Vermintide 2", "Watch Dogs Legion", "Werewolf: The Apocalypse – Earthblood",
    "West of Dead", "WILD HEARTS", "Wolfenstein: The New Order", "Wolfenstein: The Old Blood", "Wolfenstein: Youngblood",
    "Wolfenstein II: The New Colossus", "World War Z", "Worms W.M.D", "WRC Generations", "XCOM 2", "Yet Another Zombie Defense HD",
    "Ys IX: Monstrum Nox", "Ys VIII: Lacrimosa of DANA", "Zombie Army 4: Dead War"
    # ... (остальные игры)
]

# Список установленных игр
installed_games = [
    "✅🔥 EA FC 24",
    "✅🔥 UFC 5",
    "✅🔥 Need for Speed Unbound",
    "✅🔥 GTA 5",
    "✅🔥 The Witcher 3: Wild Hunt",
    "✅🔥 Spider-Man",
    "✅🔥 Assassin's Creed Valhalla",
    "✅🔥 Mortal Kombat 11",
    "✅🔥 The Last of Us Part I",
    "✅🔥 Assassin's Creed Valhalla",
    "✅🔥 Assassin's Creed Valhalla"
]

# Пагинация для всех игр
def get_games_page(page: int, games_per_page: int = 15) -> list:
    start_index = (page - 1) * games_per_page
    end_index = start_index + games_per_page
    return all_games[start_index:end_index]

# Функция для отображения главного меню
async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Приветственное сообщение
    welcome_message = (
        "🎮 **PlayStation 5**\n"
        "✅ Высокая производительность и потрясающая графика\n"
        "✅ Поддержка 4K и 120 FPS для плавного геймплея\n"
        "✅ Огромная библиотека игр, включая эксклюзивы\n"
        "✅ Удобный контроллер DualSense с тактильной отдачей\n"
        
        "📌 **Аренда консоли на удобных условиях!**\n"
        "Доступные цены, популярные игры, всё необходимое для комфортного гейминга!"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 Установленные игры", callback_data="installed_games")],
        [InlineKeyboardButton("💰 Условия аренды", callback_data="rental")],
        [InlineKeyboardButton("📦 Все игры", callback_data="all_games_1")],
        [InlineKeyboardButton("📹 Видеоинструкция", callback_data="video_instructions")],
        [InlineKeyboardButton("🆘 Поддержка", url="https://t.me/chernysgh")],  # Новая кнопка
        [InlineKeyboardButton("📩 Забронировать", url="https://t.me/MikhailBat")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:  # Если это команда /start
        await update.message.reply_text(
            welcome_message,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    else:  # Если это callback (нажатие кнопки "🔙 Назад")
        await update.callback_query.edit_message_text(
            welcome_message,
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await show_main_menu(update, context)

# Обработка кнопок меню
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "installed_games":
        installed_games_text = "\n".join(installed_games)
        await query.edit_message_text(
            text=f"🎮 **Установленные игры**:\n\n{installed_games_text}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")],
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/MikhailBat")]
            ])
        )
    elif query.data == "rental":
        await query.edit_message_text(
            text="💰 **Тарифы и цены на аренду PS5**\n"
                 "📅** 1 сутки — 1000₽ самовывоз (+ 200₽ доставка)\n"
                 "📅 🔥🔥🔥3 дня — 2500₽ (доставка включена) ✅Выгодно✅\n"
                 "📅 Неделя — 5000₽ (доставка включена) 🔥\n\n"
                 "📦 В комплекте:\n"
                 "✅ Консоль PS5\n"
                 "✅ 2 геймпада DualSense\n"
                 "✅ Все необходимые кабели\n"
                 
                 "🔹 **Доставка и залог обсуждаются индивидуально.**\n"
                 "🔹 **При долгосрочной аренде – скидки!**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/MikhailBat")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ])
        )
    elif query.data.startswith("all_games_"):
        page = int(query.data.split("_")[2])
        games_page = get_games_page(page)
        games_text = "\n".join([f"🎮 {game}" for game in games_page])
        keyboard = []

        # Кнопки пагинации
        
        if len(all_games) > page * 15:
            keyboard.append([InlineKeyboardButton("➡️ Следующая страница", callback_data=f"all_games_{page + 1}")])
        if page > 1:
            keyboard.append([InlineKeyboardButton("⬅️ Предыдущая страница", callback_data=f"all_games_{page - 1}")])    

        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_main")])
        keyboard.append([InlineKeyboardButton("📩 Забронировать", url="https://t.me/MikhailBat")])
        keyboard.append([InlineKeyboardButton("🔍 Поиск игры", callback_data="search_game")])

        await query.edit_message_text(
            text=f"📦 **Все игры (страница {page})**:\n\n{games_text}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif query.data == "search_game":
        await query.edit_message_text(
            text="🔍 Введите название игры для поиска:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="all_games_1")]
            ])
        )
    elif query.data == "video_instructions":
        # Меню с видеоинструкциями (два столбца и три строки)
        keyboard = [
            [
                InlineKeyboardButton("1. Включение консоли", callback_data="video_power_on"),
                InlineKeyboardButton("2. Выбор пользователя", callback_data="video_select_user")
            ],
            [
                InlineKeyboardButton("3. Создание пользователя", callback_data="video_create_user"),
                InlineKeyboardButton("4. Запуск игры", callback_data="video_start_game")
            ],
            [
                InlineKeyboardButton("5. Выключение игры", callback_data="video_stop_game"),
                InlineKeyboardButton("6. Выключение консоли", callback_data="video_power_off")
            ],
            [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
        ]
        await query.edit_message_text(
            text="📹 **Видеоинструкции**\nВыберите нужный пункт:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif query.data.startswith("video_"):
        # Отправка видео в зависимости от выбранной кнопки
        video_mapping = {
            "video_power_on": "https://t.me/stasgorod1video/94",  # Укажите путь к видео
            "video_select_user": "https://t.me/stasgorod1video/95",
            "video_create_user": "https://t.me/stasgorod1video/96",
            "video_start_game": "https://t.me/stasgorod1video/97",
            "video_stop_game": "https://t.me/stasgorod1video/98",
            "video_power_off": "https://t.me/stasgorod1video/99"
        }
        # Соответствие callback_data и русских подписей
        caption_mapping = {
            "video_power_on": "Включение консоли",
            "video_select_user": "Выбор пользователя",
            "video_create_user": "Создание пользователя",
            "video_start_game": "Запуск игры",
            "video_stop_game": "Выключение игры",
            "video_power_off": "Выключение консоли"
        }
        video_path = video_mapping.get(query.data)
        if video_path:
            # Получаем русскую подпись из mapping
            caption = caption_mapping.get(query.data, "Видеоинструкция")
            # Отправляем видео с подписью
            await query.message.reply_video(
                video=video_path,
                caption=caption  # Подпись на русском
            )
            # Отправляем кнопку "Назад" (возврат в меню видеоинструкций)
            await query.message.reply_text(
                text="Выберите действие:",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 Назад", callback_data="video_instructions")]
                ])
            )
        else:
            await query.message.reply_text("❌ Видео не найдено.")
    elif query.data == "back_main":
        # Возврат в главное меню
        await show_main_menu(update, context)

# Обработка текстовых сообщений (поиск игр)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    search_query = update.message.text.lower()
    found_games = [game for game in all_games if search_query in game.lower()]

    if found_games:
        games_text = "\n".join([f"🎮 {game}" for game in found_games])
        await update.message.reply_text(
            text=f"🔍 **Найденные игры**:\n\n{games_text}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="all_games_1")],
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/MikhailBat")]
            ])
        )
    else:
        await update.message.reply_text(
            text="❌ Игра не найдена. Попробуйте ещё раз.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Назад", callback_data="all_games_1")]
            ])
        )

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()