---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobile-premier-league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mplgames.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mplgames.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.mplgames.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mplgames.com/blog/feed
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mplgames.com/about-us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mplgames.com/about-us/privacy-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobile-premier-league-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobile-premier-league-llms.txt
coverage:
  checked: '2026-08-25'
  detail: MPL's game-developer program is gone at the DNS layer — docs.developer.mpl.live returns NXDOMAIN and developer.mpl.live is a dangling CNAME to a deleted AWS load balancer (dualstack.prod-developer-dashboard-2060818981.ap-south-1.elb.amazonaws.com, itself NXDOMAIN) — and the surviving hosts publish nothing machine-readable, with api.mpl.live returning a JSON 404 to every spec, GraphQL and /.well-known/ path probed.
  evidence:
  - status: 0
    url: https://docs.developer.mpl.live/docs
  - status: 0
    url: https://developer.mpl.live/
  - status: 404
    url: https://api.mpl.live/openapi.json
  - status: 404
    url: https://www.mplgames.com/.well-known/api-catalog
  - status: 200
    url: https://www.mplgames.com/about-us
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Mobile Premier League (MPL) is a mobile skill-gaming and esports platform founded in 2018 and headquartered in Bengaluru, India, operated by Galactus Funware Technology. It distributes a catalog of casual, card, board and fantasy-sports titles inside a single app and runs tournaments and contests around them, reporting more than 100 million registered users across Asia, Europe and North America. MPL historically ran a game-developer program — a Developer Dashboard and a publish-and-monetize SDK at developer.mpl.live, documented at docs.developer.mpl.live — that let third-party studios ship a single build to the MPL app under a revenue-share agreement. That program's hosts no longer resolve, and MPL publishes no public REST, GraphQL, MCP or event API today. Following India's Promotion and Regulation of Online Gaming Act, 2025, MPL discontinued real-money gaming in India; www.mplgames.com is the live consumer surface, principally serving the United States.
image: https://cms-origin.mpl.live/cms-latest-env/images/MPL_logo_13457e45ff_c5f37df2e8.webp
layout: provider
modified: '2026-08-25'
name: Mobile Premier League
nav: Providers
network: true
overview: 'Mobile Premier League is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Mobile Gaming, Esports, and Skill Gaming.


  Mobile Premier League''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 5
screenshot: https://raw.githubusercontent.com/api-evangelist/mobile-premier-league/refs/heads/main/screenshots/mobile-premier-league-2026-09-02T150557.png
security:
- kind: domain-security
  name: Mobile Premier League Domain Security
  slug: mobile-premier-league-domain-security
  summary_line: TLSv1.3
slug: mobile-premier-league
tags:
- Company
- Gaming
- Mobile Gaming
- Esports
- Skill Gaming
- Games
- Consumer
- Entertainment
- Tournaments
- India
website: https://www.mplgames.com/
---
