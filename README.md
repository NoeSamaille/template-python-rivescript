# Template Python Rivescript

Python starter kit for building chatbot with Rivescript.

## Requirements

1. Create a [Discord application](https://discord.com/developers/applications).
2. Add a bot to your application by clicking **Add Bot** in **Bot** section.
3. Save the Bot token and add it to the `DISCORD_TOKEN` environment variable of your terminal before running `script.py`.
4. Generate an invite URL for your bot by going to **URL Generator** in **OAuth2** section, then give your bot the required permissions:
  1. Select `bot` scope.
  2. Select `Read Messages/View Channels` in **GENERAL PERMISSIONS**.
  3. Select `Send Messages`, `Embed Links`, `Attach Files` in **TEXT PERMISSIONS**.
  4. Optionnally, add any other permissions that you want.
5. Copy the generated URL and open it to invite your bot to the required Discord server.

```sh
export DISCORD_TOKEN="<DISCORD_BOT_TOKEN>"
python script.py
```
