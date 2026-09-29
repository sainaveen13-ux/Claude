# The Million Rupee Homepage: launch playbook

10,000 blocks × ₹100 = **₹10,00,000**. Payment is by UPI, and the whole thing runs as a static site on GitHub Pages, so it costs ₹0 to run.

## Go live in 15 minutes (your part)
1. Edit `CONFIG` at the top of the `<script>` in `index.html`: `upiId`, `email`, and optionally `formUrl`.
2. Merge this branch into `main`. Then go to repo **Settings → Pages → Deploy from branch `main`**. The site will be at `https://<user>.github.io/<repo>/pixels/`.
3. Buy the first block yourself for ₹100. It's proof the system works, and it makes the first Short.

## Fulfilling an order (2 minutes each)
1. Check that the UTR in the email matches a payment received in your UPI app.
2. Save their image to `ads/`, then add one line to `pixels.json` (x, y, w, h are in **blocks**, i.e. pixel coordinates ÷ 10):
   `{ "x": 10, "y": 10, "w": 10, "h": 5, "img": "ads/foo.png", "url": "https://…", "title": "Hover text" }`
3. Commit. The block is live about a minute later. Claude can do this step for you: paste in the order email.

## The unhinged growth plan
- **Make the stunt the content.** Run a Rupaya Files Shorts series called *"Day N: ₹X of ₹10,00,000"* and post every sale as an episode. The counter is the cliffhanger.
- **Price rises as it fills.** Add a rule: every 1,000 blocks sold raises the price by ₹10, which pushes people to buy early. Announce each price rise as an event.
- **The centre block auction.** Hold back the 10×10 block area in the exact centre, run a live auction for it on YouTube, and let bids come in through comments.
- **Pixel wars.** Invite rival brands, colleges or IPL fan clubs to buy territory. RCB vs CSK fighting it out on a pixel map is guaranteed drama.
- **Time capsule angle.** Promote it as "Your message, preserved on the internet for 20 years." It works for proposals, a baby's first ad, a tribute to your late grandfather. It's emotional, and those stories make the best Shorts.
- **Local business blitz.** Pitch 10 local shops with: "₹100 = your logo on a viral page + a shout-out Short."
- **Press hook.** "Indian YouTuber revives the Million Dollar Homepage with UPI." Pitch it to YourStory, Inc42 and r/india.

## Rules (read before launch)
- Reject betting, adult, scam, hateful and political content, and refund those payments. This rule is also shown on the site.
- This money is taxable income, so keep a sheet of UTRs.
- Don't promise "forever" beyond what you can maintain. GitHub Pages is free and permanent as long as the repo exists.
