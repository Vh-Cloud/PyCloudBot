import random

class EmbedFunction:
    def __init__(self, ctx):
        self.context = ctx
    
    async def embedCreate(self, discord):
        color = int(random.randrange(1, 2) - 1)
        colors = [0x005EFF, 0xFFFF00]
        info = """
            **💻 Infornações detalhadas**

            **👨‍💻Desenvolvedor:**  `Marcos Paulo (mr-soulfox)`

            **🏢Empresa:** `VH'Cloud`

            **🤖 Meu prefixo:** `%` 

            **💻 Host:** `Heroku`

            **🐍Linguagem:** `Python`

            **📖Biblioteca:** `Discord.py`

            **Ver todos os comandos:** `%help`
        """
        embed = discord.message.Embed(color=colors[color], title="PyCloud info", description=info)
        await self.context.message.channel.send(embed=embed)

        