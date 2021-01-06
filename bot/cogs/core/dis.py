from dis import dis
from discord.ext import commands

from bot.bot import Bot
from bot.utils.paginator import paginate
from bot.utils.stdoutcap import STDRedirect


class Disassembler(commands.Cog):
    """A cog for showing Python bytecode disassemblies"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="dis")
    @commands.is_owner()
    async def py_dis(self, ctx: commands.Context, *, code: str):
        code = code[6:-3]
        cap = STDRedirect()
        dis(code)
        cap.exit()
        pages = paginate(cap.data.split("\n"))
        for page in pages[:5]:
            await ctx.send(page)


def setup(bot: Bot):
    bot.add_cog(Disassembler(bot))
