# अपनी दीवार · Apni Deewar

> **"Ghar nahi le sakte? Deewar ki ek eent le lo."** 🧱

A digital wall of 10,000 eent (bricks). One eent costs ₹101 shagun, and the rate rises as the wall fills: ₹101 → ₹151 → ₹251 → ₹501 → ₹1,100. If every eent sells, that's about ₹37.6 lakh. Payment is by UPI, orders come in on WhatsApp, and hosting on GitHub Pages is free.

## Why would a middle-class Indian pay? (the core insight)
| Feeling | How it shows up on the wall |
|---|---|
| **Owning a house feels impossible** | "Ghar nahi, toh deewar sahi." Satire about a shared frustration, the same way the Cockroach Janta Party turned an insult into an identity, but with **zero politics**. |
| **Shagun culture** | ₹101 / ₹151 / ₹251 / ₹501 / ₹1,100 are the amounts everyone already gives in an envelope, so paying one feels like a blessing, not a purchase. |
| **Newspaper wishes and tribute ads** | Birthday wishes and *shraddhanjali* ads in the Times of India cost thousands of rupees. Here it's ₹101, and it stays up forever. |
| **Mannat** (tying a thread at a temple or dargah) | 🙏 Mannat eent: "Visa lag jaaye", "Placement ho jaaye", "Shaadi fix ho". |
| **Bhadaas** (venting) | 😤 "Boss ne Diwali pe leave nahi di." Relatable and funny, which makes it highly shareable. |
| **Izzat** (city, college and mohalla pride) | A city leaderboard plus a "Shehar walon ko lalkaaro" WhatsApp challenge button. |
| **Wall ads everywhere in India** | Painted wall aesthetic, *Yahan thookna mana hai*, *Horn OK Please*, and nimbu-mirchi hanging for nazar. |
| **Parents' approval** | Certificate line: "Papa, ab main property owner hoon." |

## Virality mechanics already built
1. **Identity badge:** buyers become "Deewardar" (a pun on zamindar) and get a downloadable **Deewardar Certificate** (1080×1080, sized for Insta and WhatsApp Status).
2. **Free hook with FOMO:** *"Aapki lucky eent"* turns your name and birthday into an eent number. It's either "Abhi khaali hai!" or "😱 Bunty le gaya!" Anyone can play for free, and every result is a WhatsApp forward.
3. **Tribal rivalry:** the city leaderboard, plus a pre-written taunt message aimed at other cities.
4. **Scarcity:** a live rate ladder shows "X eent baad rate ₹151."
5. **Content worth scrolling:** category filters, "Koi bhi eent padho" (random story), and a live feed. Reading other people's mannat and bhadaas is the scroll-bait, like the writing on a college bench.
6. **Built for WhatsApp:** share buttons everywhere, with orders going to your WhatsApp.
7. **Easter eggs:** tapping the nimbu-mirchi shows "Buri nazar wale tera munh kaala."

## Launch plan (Diwali is the trigger)
- **Now → Oct 20:** buy the first 5 eent yourself (mannat, papa, bhadaas, city, Rupaya Files) so the wall isn't empty. Film it.
- **Rupaya Files series:** "Maine ₹101 mein property kharidi" → "Day N: X Deewardar." Every funny bhadaas gets a Short.
- **Diwali week:** a "Diwali Diya eent" category and a "Dhanteras pe property kharido 😏" campaign. Pull forward the rate increase at ₹151 for urgency.
- **1st of the month (salary day):** "Salary aayi? Eent lo."
- **Seed rivalries:** IIT vs NIT, Pune vs Bangalore, CSK vs RCB fan pages. Offer the first college or fan club to hit 100 eent a free 5×5 block.
- **Meme accounts and press:** "Indian YouTuber sells a wall, one brick at a time, for ₹101." Pitch it to r/india, YourStory and Inc42.

## Go live (your part, 15 minutes)
1. In `index.html`, set `CONFIG`: `upiId` and `whatsapp` (for example `919876543210`).
2. Merge to `main`, then **Settings → Pages → Deploy from branch `main`**. The site will be at `https://<user>.github.io/<repo>/deewar/`.
3. Optional: buy `apnideewar.in` (about ₹500 a year; availability not checked).

## Fulfilling an order (2 minutes, or paste the WhatsApp order to Claude)
1. Match the UTR against your UPI app.
2. Add a line to `deewar.json`:
   `{ "x": 10, "y": 10, "w": 16, "h": 5, "name": "Bunty Sharma", "city": "Kanpur", "kind": "badhai", "msg": "Papa, ab main property owner hoon", "color": "#d9480f", "url": "" }`
3. Commit. It goes live in about a minute.

## Rules
No politics, no religious hate, no abuse, no betting, no adult content. Refund anything rejected. Keep a UTR sheet, because this is taxable income. The certificate says "sirf masti ke liye", because this isn't real property and we don't pretend otherwise.
