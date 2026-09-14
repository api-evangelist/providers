---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://18birdies.com/
- group: operate
  title: ''
  type: Support
  url: https://help.18birdies.com/
- group: company
  title: ''
  type: Blog
  url: https://18birdies.com/clubhouse/
- group: commercial
  title: ''
  type: Pricing
  url: https://18birdies.com/premium/
- group: start
  title: ''
  type: SignUp
  url: https://18birdies.com/install/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://18birdies.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://18birdies.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/18Birdies
- group: commercial
  title: ''
  type: Plans
  url: plans/18birdies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/18birdies-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/18birdies-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/18birdies-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/18birdies-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 18Birdies ships only an end-user golf app — its site has no /developers, /developer, /api or /docs page (all 404), its Help Scout knowledge base has no API or integration category, and the mobile backend at api.18birdies.com answers 403 at the root and 404 on every OpenAPI, Swagger, GraphQL and .well-known discovery path.
  evidence:
  - status: 404
    url: https://18birdies.com/developers
  - status: 404
    url: https://18birdies.com/llms.txt
  - status: 404
    url: https://api.18birdies.com/openapi.json
  - status: 404
    url: https://api.18birdies.com/graphql
  - status: 403
    url: https://api.18birdies.com/
  - status: 404
    url: https://18birdies.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 18Birdies is a golf technology company behind the 18Birdies mobile app — a golf GPS rangefinder, digital scorecard, shot- and stat-tracking platform and social network for golfers, founded in 2014. The app combines Google Maps-derived course imagery and elevation with hole-by-hole GPS distances, 3D green maps, wind and slope adjustment, club recommendations, strokes-gained analytics, an AI Swing Analyzer, handicap tracking, side games and tournament/league management across a worldwide golf course database. It operates a freemium consumer subscription (a free tier plus Premium) with companion Apple Watch and Wear OS experiences. 18Birdies runs a production backend at api.18birdies.com that serves its own mobile clients, but as of this profiling pass it publishes no public developer program, no API reference, and no machine-readable contract.
image: https://18birdies.com/public-images/apple-touch-icon.png
layout: provider
modified: '2026-09-05'
name: 18Birdies
nav: Providers
network: true
overview: '18Birdies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Sports, Mobile Applications, Location, and Geolocation.


  18Birdies'' developer surface includes support, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: 18Birdies Plans Pricing
  plan_count: 4
  slug: 18birdies-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: 18Birdies Rate Limits
  slug: 18birdies-rate-limits
security:
- kind: domain-security
  name: 18Birdies Domain Security
  slug: 18birdies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 18birdies
tags:
- Golf
- Sports
- Mobile Applications
- Location
- Geolocation
- Mapping
- Consumer
- Fitness
- Social
- Analytics
- Tournaments
- Subscriptions
website: https://18birdies.com/
---
