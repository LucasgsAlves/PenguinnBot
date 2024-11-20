import discord
from discord.ext import commands

# Comando de kick
@commands.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        if ctx.author.top_role > member.top_role:
            try:
                if reason is None:
                    reason = "Sem razão fornecida para o kick."
                await member.kick(reason=None)
                await ctx.send(f"{member} foi expulso do servidor. O motivo foi {reason}\n\n")
            except discord.Forbidden:
                await ctx.send("Não é possível expulsar esse membro.\n\n")
            except discord.HTTPException:
                await ctx.send("Houve um erro ao expulsar o membro.\n\n")   
        else:
            await ctx.send("Você não tem permissão para expulsar membros.")
            