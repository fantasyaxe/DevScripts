<img src="https://raw.githubusercontent.com/Delta-Factory/.github/refs/heads/main/profile/img/Project_Void.png" alt="Project~Void background">

<H1 align="center">-== DevScripts ==-</H1>

<p align="center" style="font-size: 15px">
    <b>
   		Скрипты для создания проекта разработки для майнкрафта.
      <br> Зеркало (Откуда качается всё нужное) меняется в config.py
      <br><br> Т.к мне влом возиться с лицензиями, легализацией проекта и тому подобной хренью - Всё, что может быть нарушением каких либо Лицензий - Висит на вас. Я предоставляю лишь скрипты.
    </b>
</p>

<H2 align="center">-==[ How to ]==-</H2>

<p align="center" style="font-size: 15px">
    <b>
      Для работы достаточно запустить <code>INIT.py</code>.
      <br> Если что-то идет не так (Например нет нужных зависимостей - Меняете зеркало в <code>config.py</code>)
      <br> Если всё прям совсем плохо - IDK, @б#т$сь сами.
    </b>
</p>

<H2 align="center">-==[ Mirrors? What? ]==-</H2>

<p align="center" style="font-size: 15px">
    <b>
      <a href="https://github.com/MCRebooted/MirrorsList">MirrorsList</a>
      - Короче есть этот репозиторий. В нем лежит зеркало этого проекта (Пример будет снизу).
      <br> Нас интересует конкретно <code>decompiler</code> часть этого зеркала.
      <br> Там должны быть указаны ссылки на клиент игры, сервер игры, SpecialSource и CFR. Всё.
      <br> Зачем это нужно? Нууу... Не люблю хардкод ссылок.. А ещё это делает проект хоть сколько-то неубиваемым..
    </b>
</p>

<H2 align="center">-==[ Mirror Example ]==-</H2>

```json
{
  "version": {
    "0.0.0-DEV": {
      "decompiler": {
        "client": "https://launcher.mojang.com/v1/objects/465378c9dc2f779ae1d6e8046ebc46fb53a57968/client.jar",
        "server": "https://launcher.mojang.com/v1/objects/f9ae3f651319151ce99a0bfad6b34fa16eb6775f/server.jar",
        "CFR": "https://www.benf.org/other/cfr/cfr-0.152.jar",
        "SpecialSource": "https://github.com/MCRebooted/SpecialSource/releases/download/1.11.5/SpecialSource.jar"
      },
      "game": {
        "client": {},
        "server": {},
        "both": {}
      }
    }
  }
}
```

<H2 align="center">-==[ File Structure ]==-</H2>

```
root/
├── jars/
│   ├── client/
│   │   └── client.jar
│   ├── server/
│   │   ├── server.jar
│   ├── SpecialSource.jar
│   └── CFR.jar
├── mappings/
│   ├── packaged.srg
│   ├── fields.csv
│   ├── newids.csv
│   └── methods.csv
├── patches/ (Dont need on this time)
│   ├── client/... (Patches there...)
│   ├── server/... (Patches there...)
│   ├── apply_patches.sh
│   └── generate_patches.sh
├── src/
│   ├── client/... (Your source there...)
│   └── server/... (Your source there...)
├── RecreateMappings.py
├── PostDecompile.py
├── MirrorHandler.py
├── config.py
└── INIT.py
```

<H1 align="center">-==[ Socials ]==-</H1>

<p align="center">
  <a href="https://discord.gg/MEBkvJbe4P" target="_blank">
    <img alt="My Server" src="https://img.shields.io/badge/P._Violette-white?style=for-the-badge&logo=discord&logoColor=white&logoSize=64&label=%20&labelColor=5c32a8&color=242323&link=https%3A%2F%2Fdiscord.gg%2FMEBkvJbe4P"></a>
  <a href="https://boosty.to/nionim" target="_blank">
    <img alt="My Boosty" src="https://img.shields.io/badge/DeltaCion-white?style=for-the-badge&logo=boosty&logoColor=white&logoSize=64&label=%20&labelColor=ed7315&color=242323&link=https%3A%2F%2Fboosty.to%2Fnionim"></a>
  <a href="https://t.me/LOWcitory" target="_blank">
    <img alt="My Telegram" src="https://img.shields.io/badge/P._Violette-white?style=for-the-badge&logo=telegram&logoColor=white&logoSize=64&label=%20&labelColor=00aeff&color=242323&link=https%3A%2F%2Ft.me%2FLOWcitory"></a>
</p>

