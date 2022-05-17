# Retrieve Free Games from websites

This script retrieves free games posted on selected sites (e.g here `PC gamer`) and send it to a discord bot provided

## env variables:

```bash
* WEBHOOK=Your Discord webhook
* URL_PCGAMER=https://www.pcgamer.com/epic-games-store-free-games-list/#section-epic-store-free-games-right-now
```

## Improvements
* Get epicgames weekly free games directly from the site (need to find a way to retrieve data from Javascript-generated pages using python-html)
* Or find a site that list free games from multiple sources (like PS Plus, Ubisoft..)