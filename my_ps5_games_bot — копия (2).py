from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

TOKEN = "7665158890:AAGGdXgefYkLFduK2OOuG8_enwes4cbzJX8"

# Полный список всех игр
all_games = [
    "11-11 Memories Retold", "A Hat in Time", "A Space for the Unbound", "A Way Out",
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
        "✅ Возможность играть онлайн и получать бесплатные игры по подписке\n\n"
        "📌 **Аренда консоли на удобных условиях!**\n"
        "Доступные цены, популярные игры, всё необходимое для комфортного гейминга!"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 Установленные игры", callback_data="installed_games")],
        [InlineKeyboardButton("💰 Условия аренды", callback_data="rental")],
        [InlineKeyboardButton("📦 Все игры", callback_data="all_games_1")],
        [InlineKeyboardButton("📹 Видеоинструкция", callback_data="video_instructions")],
        [InlineKeyboardButton("📩 Забронировать", url="https://t.me/chernysgh")]
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
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/chernysgh")]
            ])
        )
    elif query.data == "rental":
        await query.edit_message_text(
            text="💰 **Тарифы и цены на аренду PS5**\n"
                 "🎮 **1 день** – 1000₽\n"
                 "🎮 **3 дня** – 2500₽\n"
                 "🎮 **Неделя** – 5000₽\n\n"
                 "📦 В комплекте:\n"
                 "✅ Консоль PS5\n"
                 "✅ 2 геймпада DualSense\n"
                 "✅ Все необходимые кабели\n"
                 "✅ Доступ к каталогу игр\n\n"
                 "🔹 **Доставка и залог обсуждаются индивидуально.**\n"
                 "🔹 **При долгосрочной аренде – скидки!**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/chernysgh")],
                [InlineKeyboardButton("🔙 Назад", callback_data="back_main")]
            ])
        )
    elif query.data.startswith("all_games_"):
        page = int(query.data.split("_")[2])
        games_page = get_games_page(page)
        games_text = "\n".join([f"🎮 {game}" for game in games_page])
        keyboard = []

        # Кнопки пагинации
        if page > 1:
            keyboard.append([InlineKeyboardButton("⬅️ Предыдущая страница", callback_data=f"all_games_{page - 1}")])
        if len(all_games) > page * 15:
            keyboard.append([InlineKeyboardButton("➡️ Следующая страница", callback_data=f"all_games_{page + 1}")])

        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_main")])
        keyboard.append([InlineKeyboardButton("📩 Забронировать", url="https://t.me/chernysgh")])
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
        # Меню с видеоинструкциями
        keyboard = [
            [InlineKeyboardButton("1. Включение консоли", callback_data="video_power_on")],
            [InlineKeyboardButton("2. Выбор пользователя", callback_data="video_select_user")],
            [InlineKeyboardButton("3. Создание пользователя", callback_data="video_create_user")],
            [InlineKeyboardButton("4. Запуск игры", callback_data="video_start_game")],
            [InlineKeyboardButton("5. Выключение игры", callback_data="video_stop_game")],
            [InlineKeyboardButton("6. Выключение консоли", callback_data="video_power_off")]
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
        video_path = video_mapping.get(query.data)
        if video_path:
            await query.message.reply_video(
                video=video_path,
                caption=f"🎥 Вот видео по запросу: {query.data.replace('video_', '').replace('_', ' ')}"
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
                [InlineKeyboardButton("📩 Забронировать", url="https://t.me/chernysgh")]
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