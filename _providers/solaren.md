---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solaren-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.solarenspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.solarenspace.com/news-events/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.solarenspace.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.solarenspace.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarenspace.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarenspace.com/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solaren-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/solaren-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solaren-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: Solaren generates and sells electricity from orbiting space solar power plants under utility power purchase agreements, and its single public site is a WordPress marketing brochure with no developer section — every OpenAPI, GraphQL and /.well-known/ path probed returned the theme's HTTP 500 error page, and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/ (wp/v2 and friends, no company namespace).
  evidence:
  - status: 200
    url: https://www.solarenspace.com/
  - status: 500
    url: https://www.solarenspace.com/openapi.json
  - status: 500
    url: https://www.solarenspace.com/graphql
  - status: 500
    url: https://www.solarenspace.com/.well-known/agent-card.json
  - status: 200
    url: https://www.solarenspace.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: 'Solaren is a combination energy and aerospace company headquartered in Manhattan Beach, California, founded in 2001 by a team of satellite engineers and space scientists. Solaren designs, develops, integrates, deploys and operates space solar power (SSP) plants: solar arrays on a patented lightweight solar power satellite in geosynchronous orbit convert sunlight to electricity, convert that electricity to radio-frequency power, and beam it to an earth receiving station that returns it to the grid as baseload power. The company''s business model is to own and operate its SSP plants and sell continuous, zero-emission electricity to utility and government customers; it signed the world''s first power purchase agreement for space solar electricity, with Pacific Gas & Electric. Solaren is a hardware and energy-generation company and publishes no public developer program, API, or machine-readable API contract.'
image: https://www.solarenspace.com/wp-content/themes/solaren/img/logo.png
layout: provider
modified: '2026-08-28'
name: Solaren
nav: Providers
network: true
overview: 'Solaren is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Renewable Energy, and Space.


  Solaren''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Solaren Plans Pricing
  plan_count: 0
  slug: solaren-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Solaren Rate Limits
  slug: solaren-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/solaren/refs/heads/main/screenshots/solaren-2026-09-02T160110.png
security:
- kind: domain-security
  name: Solaren Domain Security
  slug: solaren-domain-security
  summary_line: TLSv1.3
slug: solaren
tags:
- Company
- Energy
- Electricity
- Renewable Energy
- Space
- Aerospace
- Satellites
- Solar Power
- Utilities
website: https://www.solarenspace.com/
---
