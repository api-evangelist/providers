---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upequity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upequity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.upequity.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://www.upequity.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.upequity.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upequity
- group: other
  title: ''
  type: Licensing
  url: https://www.upequity.com/licensing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upequity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/upequity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upequity-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: UpEquity is a HubSpot-hosted mortgage lender marketing site with no developer channel at all — /openapi.json, /swagger.json, /graphql and every /.well-known/ path return the HubSpot 404 page, and api./docs./developers./developer./app./portal.upequity.com do not resolve in DNS, so there was no host to probe beyond www.
  evidence:
  - status: 404
    url: https://www.upequity.com/openapi.json
  - status: 404
    url: https://www.upequity.com/.well-known/agent-card.json
  - status: 0
    url: https://api.upequity.com/
  - status: 200
    url: https://www.upequity.com/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'UpEquity is an Austin, Texas based, veteran-owned proptech mortgage lender and title company founded in 2019 that operates a "Buy Before You Sell" / Trade Up program for homeowners who are purchasing and selling at the same time. The company advances the equity trapped in a client''s existing home so the client can make a non-contingent — effectively all-cash — offer on a new home, move once, and sell the old home afterward, with UpEquity making a backup offer on the departing residence. It also runs UpEquity Title and originates mortgages directly under NMLS #2101265, licensed across roughly twenty US states. Distribution is through real-estate agents and loan officers rather than a developer channel: as of this profiling pass UpEquity publishes no developer portal, no API reference, and no machine-readable API contract of any kind on any host it controls.'
image: https://20424362.fs1.hubspotusercontent-na1.net/hubfs/20424362/UpEquity%20Brand%20Assets/UpEquityLogo-01.svg
layout: provider
modified: '2026-09-02'
name: UpEquity
nav: Providers
network: true
overview: 'UpEquity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Mortgage, Lending, and Financial Services.


  UpEquity''s developer surface includes support and 9 more developer resources.'
plans:
- name: Upequity Plans Pricing
  plan_count: 0
  slug: upequity-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Upequity Rate Limits
  slug: upequity-rate-limits
security:
- kind: domain-security
  name: Upequity Domain Security
  slug: upequity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: upequity
tags:
- Company
- Real Estate
- Mortgage
- Lending
- Financial Services
- Proptech
- Home Buying
- Title Insurance
- Fintech
website: https://www.upequity.com/
---
