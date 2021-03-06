#: russian

{
    '__full__': 'russian',

    '__maintainer__' : '@KlyaniX',

    'blacklisted' : ''':x: Этот канал в чёрном списке :x:''',

    'help' : '''Пожалуйста, посетите: https://reminder-bot.com/help?lang=RU''',

    'no_perms_webhook' : '''**ВНИМАНИЕ**: Чтобы отправлять напоминания, мне нужны права `Управления вебхуком`.''',

    'no_perms_general' : '''Ошибка доступа. Пожалуйста убедитесь что у бота есть права.''',

    'no_perms_managed' : '''Вы должны иметь права на редактирование сообщений или роль которой дозволено использовать бота. Пожалуйста, обратитесь к администратору и расскажите ему про `{prefix}restrict` команду, которая позволит исправить эту проблему.''',

    'help_raw' : [
        ['''Reminder Commands''', {
            '$natural' : 'Самый простой метод использования напоминаний, напишите эту команду без каких либо агрументов для большей инфомрации.',

            '$del' : 'Удалить напоминание на сервере, если напоминание было направленно вам в лс, напишите эту команду в лс боту.',

            '$look [канал]' : 'Показывает все напоминания в определённом канале.',

            '$remind [пользователь/канал] <время-для-напоминания> <сообщение>' : 'Используйте <code>$natural</code> если это возможно. Устанавливает напоминание. Укажите время таймера [число][s/m/h/d] (секунды/минуты/часы/дни), пример: 10s - 10 секунд или 2s10m - 2 секкунды 10 минут. Так-же можно указать конкретную дату/время <code>day/month/year-hour:minute:second</code>.',

            '$interval [пользователь/канал] <время-для-напоминания> <интервал> <сообщение>' : '<strong><a href="https://patreon.com/jellywx/">Только для Patreon.</a></strong> Используйте <code>$natural</code> если это возможно. Начинает отсылать напоминания начиная с <code>время-для-напоминания</code>. Укажите время в разговорном формате (англ). <code>$interval 0s 20m Сообщение!</code> начнёт отсылать \'Сообщение!\' в канал каждые 20 минут.',

            '$todo' : 'TODO (заметки). Используйте <code>$todo help</code> чтобы вывести все команды взаимодействия с заметками.',

            '$todos' : 'Тоже заметки <code>$todo</code> но привязанные не к пользователю, а к серверу.',

            '$timezone' : 'Устанавливает часовой пояс сервера. ',

            '$offset' : 'Устанавливает летнее/зимнее время (перевод на час вперёд/назад)' }],

        ['''Management Commands''', {
            '$restrict [role mentions]' : 'Добавляет/убирает возможность использование бота определённой роли.',

            '$blacklist [channel-name]' : 'Запрещает/разрешает использовать бота в определённом канале.' }],

        ['''Other Commands''', {
            '$donate' : 'Показывает информацию о донате.',

            '$prefix <string>' : 'Меняет префикс бота. Стандартный $.',

            '$info' : 'Показывает информацию о боте.',

            '$lang <name>' : 'Сменить язык (Change the language).',

            '$clock' : 'Показывает текущее время на сервере',

            }
        ]
    ],


    'info' : '''
Стандартный префикс: `$`
Сбор префикса: `@{user} prefix $`
Помощь: `{prefix}help`

**Встречайте, Reminder Bot!**
Разработчик: <@203532103185465344>
Иконка: <@253202252821430272>
Меня можно найти тут https://discord.jellywx.com и тут https://github.com/JellyWX :)

Пригласить бота: https://discordapp.com/oauth2/authorize?client_id=349920059549941761&scope=bot&permissions=8
Используйте нашу панель управления: https://reminder-bot.com/

*Если у вас есть какие-то предложения о развитии бота, пожалуйста, пишите на сервере бота*
''',

    'donate' : '''
Хотите поддержать сервер (ежемесячная подписка)? Вот ссылка на Patreon и официальный дискорд сервер бота :D
https://www.patreon.com/jellywx

https://discord.jellywx.com

Немного информации:


Если ваш аккаунт в дискорде привязан к аккаунту Patreon, то вы автоматически получите привелегие описанные ниже:
: допступ к `interval` (автоматизированные напоминания)
: ставить напоминаниям красивые разноцветные рамки (доступно только в панели управления)
: использовать разные аватарки для бота (доступно только в панели управления)

Спасибо всем поддержавшим :D Вы делаете бота стабильниее

Обратите внимание, вы должны находиться на сервере дискорда для получения привелегий.
''',

    'prefix' : {
        'no_argument' : '''
Префикс не найдет. Используйте команду `@reminder-bot prefix <prefix>`
''',
        'success' : '''
Префикс изменён {prefix}
''',

        'too_long' : '''Префикс не может быть длиньше 5 символов'''
    },

    'timezone' : {

        'no_argument' : '''
Команда:
    ```{prefix}timezone <Название часового пояса из ссылки ниже>```
Пример:
    ```{prefix}timezone Europe/London```
Все часовые пояса: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Текущая: {timezone}''',

        'no_timezone' : '''Часовой пояс не распознан. Найдите название своего часового пояса тут: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set' : '''Часовой пояс {timezone} установлен. Теперь время сервера: {time}''',
    },

    'restrict' : {

        'disabled' : '''Теперь пользователи с этой ролью _не_ могут использовать бота.''',

        'enabled' : '''Теперь пользователи с этой ролью могут использовать бота.''',

        'allowed' : '''Разрешённые роли: {}''',

        'help' : '''Укажите роль, которой хотите разрешить/запретить использовать бота.'''
    },

    'remind' : {
        'no_argument' : '''
Usage:
    ```{prefix}remind [название канала/имя#тэг пользователя] <время до или конкретная дата/время> <сообщение>```
Example:
    ```{prefix}remind #general 10s Сообщение```
    ```{prefix}remind 10:30 Уже 10:30```''',

        'invalid_tag' : '''Куда отправлять уведомление? Неправильно указан канал/пользователь.''',

        'invalid_time' : '''Неправильно составленное время, будьте уверены что вы используете подобную маску [num][s/m/h/d][num][s/m/h/d] и т.д.. или `day/month/year-hour:minute:second`.

Убедитесь что таймер не превышает 50 лет вперёд.''',

        'success' : '''Новое уведомление будет отослано {location} через {offset}. Если вы хотите отменить, напишите `$del`.''',
    },

    'natural' : {
        'no_argument' : '''
**New** Natural language processing
Examples:
    ```{prefix}natural in 10 minutes send Сообщение! to #general```
    ```{prefix}natural at 18:00 send Большое сообытие началось!```
    ```{prefix}natural on the 16th of july at 14:00 send Сегодня обновятся подписки! to #subs```
    ```{prefix}natural now send 10 минут прошли! every 10 minutes to #timer```
Keywords:
    `send` : после, идёт сообщение
    `every` : устанавливает период отправки сообщения (интервал)
    `tp` : адрессат (пользователь/канал)
Usage:
    ```{prefix}natural <time statement> send <message> [every interval statement] [to #channel/@user]```
    ''',

        'invalid_time' : '''Время указано неверно. Напишите время более чётко, для примера `16th of july` или `in 20 minutes`''',

        'long_time' : '''Убедитесь что таймер не более 50 лет впердёт''',

        'send' : ''' send ''',

        'to' : ''' to ''',

        'every' : ''' every '''

    },

    'interval' : {
        'no_argument' : '''
Usage:
    ```{prefix}interval [канал или пользователь] <таймер или конкретное время> <интервал> <сообщение>```
Example:
    ```{prefix}interval #general 9:30 1d Доброе утро!```
    ```{prefix}interval 0s 10s Это будет очень интересно```''',

        'invalid_interval' : '''Убедитесь что вы указали время по маске [num][s/m/h/d][num][s/m/h/d] и т.д.. Без пробелов, Например: 10s для 10 секунд или 10s12m15h1d для 10 секунд, 12 минут, 15 часов и 1 дне.''',

        'short_interval' : '''Убедитесь что интервал настроен не чаще {min_interval} секунд.''',

        'long_interval': '''Убедитесь что интервал установлен не на 50 лет вперёд''',

        'donor' : '''Вы должны поддержать бота на Patreon (2$ или более) для доступа к этой команде! Напишите `{prefix}donate` для более подробной инфомрации.''',

    },

    'del' : {
        'listing' : '''Список уведомлений на сервере... (there may be a small delay, please wait for the "List (1,2,3...)" message).''',

        'listed' : '''Список (1,2,3...) уведомлений которые вы хотите удалить или напишите что нибудь для отметы.''',

        'count' : '''Удалены {} уведомления!'''
    },

    'look' : {
        'listing' : '''Список уведомлений на этом канале...''',

        'inter' : '''следующие оповещание: ''',

        'no_reminders' : '''На этом канале уведомлений не найдено.''',
    },

    'todo' : {

        'add' : '''*Используйте `{prefix}{command} <message>` добавить заметку, или напишите `{prefix}{command} help` для получения полной информации!*''',

        'added' : '''Заметка \'{name}\' добавлена в список запланированного!''',

        'removed' : '''Заметка \'{}\' удалена из списка запланированного!''',

        'error_value' : '''Удалить заметку можно использовав её порядковый номер. Посмотрите порядковые номера заметок через `{prefix}{command}`''',

        'error_index' : '''Не могу найти заметки под этим номером. Проверьте ещё раз?''',

        'help' : '''Для взаимодействия с списком запланированного, используйте `{prefix}{command} add <message>`, `{prefix}{command} remove <number>`, `{prefix}{command} clear` и `{prefix}{command}` чтобы добавить, удалить, очистить или показать ваш список запланированного.''',

        'cleared' : '''Список запланированного очищен!'''
    },

    'blacklist' : {
        'removed_from' : '''Указанный канал удалён из чёрный список.''',

        'added_from' : '''Указанный канал добавлен в чёрный список.''',

        'removed' : '''Текущий канал удалён из чёрного списка.''',

        'added' : '''Текущий канал добавлен в чёрный список.'''

    },

    'lang' : {

        'invalid' : '''Языки:
{}''',

        'set' : '''Установлен Английский язык.''',
    },

    'clock' : {

        'time' : '''Текущее время {}.''',

    },

    'offset' : {

        'invalid_time' : '''Убедитесь что вы используете максу времени [num][s/m/h/d][num][s/m/h/d]''',

        'success' : '''Все уведомления были смещены на {} секунд(ы)''',

    },
}
