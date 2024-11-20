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

@commands.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        if ctx.author.top_role > member.top_role:
            try:
                if reason is None:
                    reason = "Sem razão fornecida para o ban."
                await member.ban(reason=None)
                await ctx.send(f"{member} foi expulso do servidor. O motivo foi {reason}\n\n")
            except discord.Forbidden:
                await ctx.send("Não é possível expulsar esse membro.\n\n")
            except discord.HTTPException:
                await ctx.send("Houve um erro ao expulsar o membro.\n\n")   
        else:
            await ctx.send("Você não tem permissão para expulsar membros.")
            
@commands.command()
async def unban(ctx, member: discord.User, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        try:
            await ctx.guild.unban(member, reason = reason)
            await ctx.send(f"{member} foi desbanido do servidor.")
        except discord.Forbidden:
            await ctx.send("Não é possível desbanir esse membro.")
        except discord.HTTPException:
            await ctx.send("Houve um erro ao tentar desbanir o membro.")
    else:
        await ctx.send("Você não tem permissão para desbanir membros.")