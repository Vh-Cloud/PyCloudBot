import random

class EmbedFunction:
    def __init__(self, ctx):
        self.context = ctx
    
    async def embedCreate(self, discord, type):
        color = int(random.randrange(1, 2) - 1)
        colors = [0x005EFF, 0xFFFF00]
        
        if type == 'info':
            info = """
                **💻 Infornações detalhadas**

                **👨‍💻Desenvolvedor:**  `Marcos Paulo (mr-soulfox)`

                **🏢Empresa:** `Vh'Cloud`

                **🤖 Meu prefixo:** `%` 

                **💻 Host:** `Heroku`

                **🐍Linguagem:** `Python`

                **📖Biblioteca:** `Discord.py`

                **Ver todos os comandos:** `%help`
            """
            embed = discord.message.Embed(color=colors[color], title="PyCloud info", description=info)
            await self.context.message.channel.send(embed=embed)
        
        elif type == 'help':
            commands = """
                **Prefixo(%)**
                
                Comandos:
                    **%ping - Retorna a latencia do PyCloud**
                    **%say [palavra] - O PyCloud digita essa palavra**
                    **%create [nome] - Cria um canal**
                    **%delete [nome] - Deleta um canal**
                    **%dice [valor inicial] [valor final] - Gera um numero aleatorio entre `valor inicial` ate `valor final`**
                    **%info - Traz informações sobre o PyCloud**
                    **%help - Traz os comandos do PyCloud**
                """
            embed = discord.message.Embed(color=0xFFFF00, title="PyCloud Commands", description=commands)
            await self.context.message.channel.send(embed=embed)
        
        else:
            print('Nenhuma opção de ajuda escolhido')
