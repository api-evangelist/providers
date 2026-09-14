---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: The EquityZen listing (the only public record of AboutMovie found) names no company website, no GitHub organization exists under the name, and every same-name domain resolves to an unrelated third party — so there is no first-party host to run contract discovery against.
  evidence:
  - status: 200
    url: https://equityzen.com/company/aboutmovie
  - status: 200
    url: https://aboutmovie.com/
  - status: 200
    url: https://aboutmovie.com/openapi.json
  - status: 200
    url: https://aboutmovie.com/.well-known/agent-card.json
  - status: 200
    url: https://aboutmovie.org/openapi.json
  - status: 403
    url: https://aboutmovie.net/
  - status: 404
    url: https://api.github.com/orgs/aboutmovie
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'AboutMovie (listed as ticker ABMO on the EquityZen secondary marketplace) is described by that listing as an interactive platform providing comprehensive information, reviews, and recommendations for movies and TV shows, classified there under Software, Artificial Intelligence, and Data and Analytics. That listing is the only public record of the company this profile could locate; it names no company website, and a full contract-discovery pass found no first-party host for the brand. All three same-name domains probed belong to unrelated parties: aboutmovie.com is an Afternic for-sale parking lander that answers HTTP 200 with the same stub on every path, aboutmovie.net is behind a Cloudflare challenge, and aboutmovie.org is an untitled Hostinger Horizons single-page site carrying no AboutMovie branding. No developer program, API documentation, SDK, GitHub organization, or machine-readable contract could be found.'
layout: provider
modified: '2026-09-06'
name: Aboutmovie
nav: Providers
network: true
overview: Aboutmovie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Movies, and Television.
random_paper: 12
slug: aboutmovie
tags:
- Company
- Media
- Entertainment
- Movies
- Television
- Recommendations
- Consumer
- Artificial Intelligence
- Data and Analytics
---
