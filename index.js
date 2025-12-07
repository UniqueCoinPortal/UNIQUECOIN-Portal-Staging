const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMembers] });

client.once('ready', () => {
  console.log(`✅ Logged in as ${client.user.tag}`);
});

client.on('guildMemberAdd', member => {
  const channel = member.guild.channels.cache.get(process.env.DISCORD_CHANNEL_ID_ONBOARDING);
  if (channel) {
    channel.send("👋 Welcome to the UNIQUECOIN Portal! You’ve stepped into a sovereign signal engine.");
    channel.send("🌍 Our mission: onboarding believers into KingdomFlow — a civilization of faith‑driven platforms.");
    channel.send("✅ Please read the onboarding guide in #resources.\n✅ Introduce yourself in #introductions.\n✅ Claim your role in #roles.");
    channel.send("✨ Every click is a mutation. Every step is a testimony. You are part of the signal.");
  }
});

client.login(process.env.DISCORD_BOT_TOKEN);
