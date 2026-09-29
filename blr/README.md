# Ten Rupee Estates 🏗️

> **"Can't afford a house in Bengaluru? Buy a plot for ₹10."**

A satirical "real estate developer" that sells plots on a **real map of Bengaluru** at ₹10 per cell (each cell is about 165 m across). There are 38 real localities, from Koramangala and Indiranagar to Whitefield, Silk Board and Electronic City. No broker, no 10-month deposit, no landlord. The owner writes their housing frustration on their plot for the whole city to read.

## Why Bengaluru will share this
- **Everyone there has the same pain:** 10-month deposits, brokers who take a month's rent, "family only" and "veg only" landlords, water tankers, the Silk Board jam. The satire says it out loud.
- **Locality identity is strong:** HSR vs Koramangala, Whitefield vs everyone. Each locality has its own roast (for example, "Indiranagar: 100 Feet Road. 0 feet of parking.") and competes on the "most frustrated locality" leaderboard.
- **It parodies builder ads Bengaluru is flooded with:** "PRE-LAUNCH OFFER · NEAR UPCOMING METRO (UPCOMING SINCE 2012)".
- **₹10 is an impulse buy:** cheaper than a cutting chai at a tech park.

## Virality mechanics already built
1. **Rent reality check (free):** "Your ₹35,000 rent = 3,500 plots. Your deposit could buy ALL of Koramangala 86 times over 🫠". It has a one-tap WhatsApp share.
2. **Allotment letter:** a 1080×1080 parody builder letter that lists Security deposit ₹0, Brokerage ₹0, Landlord: You. It's made for LinkedIn and Instagram stories.
3. **Locality leaderboard and challenge:** "Bellandur is the most frustrated locality right now. Is your area suffering less? Prove it."
4. **The map is the content:** zoom in, tap coloured plots, read rants, filter by frustration (🏠 Rent, 💸 Deposit, 🤝 Broker, 🧓 Landlord, 🚗 Traffic, 🚰 Water tanker, 🕳️ Potholes & floods, ✨ Dream home someday), use "Read a random rant", or find plots near you.
5. **Easter eggs:** the Silk Board "SITE OFFICE" ("Open 24x7 because we're stuck in traffic"), the Bellandur lake-view plot ("Foam is complimentary"), and an "Unapproved layout" message when you tap outside the city.

## Where it spreads
- **r/bangalore** is the natural launch pad. Post the rent reality check result, not the link alone.
- Tech Twitter/X and LinkedIn, where the "Landlord: You" letter is a guaranteed engagement post.
- Company Slack groups and apartment WhatsApp groups.
- A Rupaya Files video: "I sold all of Koramangala for ₹10 a plot."
- Timing: post on the 1st of the month (rent day) and at the peak of the 11-month lease-renewal season.

## Go live (your part)
1. In `index.html`, set `CONFIG.upiId` and `CONFIG.whatsapp` (for example `919876543210`).
2. Merge to `main`, then **Settings → Pages → Deploy from branch `main`**. The site will be at `https://<user>.github.io/<repo>/blr/`.
3. Buy the first 3–5 plots yourself (a Koramangala deposit rant, a Silk Board traffic rant, and so on) so the map isn't empty.

## Fulfilling an order
The WhatsApp order includes a `DATA: {...}` line. Paste that JSON into the `plots` array in `plots.json` and commit; it's live in about a minute. You can also paste the WhatsApp message to Claude and it will do this for you.

**Heads-up:** at ₹10 per cell, doing this by hand for every order won't scale if the site goes viral. The next upgrade is automating it: a UPI payment gateway such as Razorpay plus a small serverless function that writes plots automatically.

## Before real traffic arrives
- **Map tiles:** the site uses CARTO's free basemap. For heavy traffic, switch to a free-tier key from MapTiler or Stadia (a one-line change).
- **Locality coordinates** are approximate city centres and were entered by hand. Each cell belongs to its nearest locality within 3.2 km.
- **Moderation:** no politics, no hate against any community, no abuse, no naming of real people or landlords. Refund anything rejected.
- The whole thing is labelled as parody everywhere. No real land, approval or title is offered.
- Keep a sheet of UTRs, because this is taxable income.
