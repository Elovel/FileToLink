import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://domaincheker.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 لینک دانلود"
    st_link = "🎞 پخش آنلاین"
    generating_link = "**⏳ درحال ساخت لینک...**"
    bot_channel = "📢 کانال دیزیمیز"
    dev_channel = "🤖"
    fast = "⚡️**لینک بروزرسانی شد**"
    update_link = "⚡ بروزرسانی لینک"
    update_limited = (f"⛔ You can update just {Config.Max_Fast_Processes} link in one time, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 بروزرسانی مجدد  لینک"
    already_updated = "مجددا بروز رسانی شد"
    wait_update = "⏳ درحال بروزرسانی..."
    wait = "⏳ لطفا صبر کنید ..."
    progress = "⏳ درحال پردازش"
    file_not_found = "⚠️فایل یافت نشد، لطفا دوباره آن را دوباره بفرستید "
    delete_manually_button = "⚠️حذف کردن"
    delete_forbidden = "ربات نمی تواند پیام های قدیمی تر از 48 ساعت را حذف کند، شما می توانید این پیام را به صورت دستی حذف کنید"
    force_join = "⚠برای استفاده از ربات باید در کانال @dizimizcf عضو شوید "
