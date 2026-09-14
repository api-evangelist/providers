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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.stashaway.sg/
- group: operate
  title: ''
  type: Support
  url: https://www.stashaway.sg/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.stashaway.sg/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stashaway.sg/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.stashaway.sg/register
- group: start
  title: ''
  type: Login
  url: https://app.stashaway.sg/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stashaway.sg/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stashaway.sg/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stashaway-engineering
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stashaway-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/stashaway-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stashaway-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/stashaway-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/stashaway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stashaway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stashaway-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stashaway-plans-pricing.yml
coverage:
  checked: '2026-08-29'
  detail: StashAway's only live API host, api.stashaway.sg, is the private mobile-app backend — its root returns a 68-byte company teaser and every other path, including /openapi.json, /graphql, /api-docs and every /.well-known/ path, returns 426 Upgrade Required from a client-version gate — and no developer.stashaway.com or developers.stashaway.com host exists at all, so there is no public API, SDK, webhook or developer portal to profile.
  evidence:
  - status: 426
    url: https://api.stashaway.sg/openapi.json
  - status: 200
    url: https://api.stashaway.sg/
  - status: 0
    url: https://developers.stashaway.com/
  - status: 404
    url: https://www.stashaway.sg/.well-known/api-catalog
  - status: 200
    url: https://www.stashaway.sg/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: 'StashAway is a digital wealth manager and robo-advisor headquartered in Singapore, operating as Asia Wealth Platform Pte Ltd under Monetary Authority of Singapore Capital Markets Services licence CMS100604 (issued May 2017). Founded in 2016, it offers goal-based, globally diversified ETF portfolios driven by its proprietary ERAA (Economic Regime-based Asset Allocation) framework, a self-directed ETF Explorer covering 80+ asset classes, Flexible, Thematic, Income, Responsible and Singapore-focused portfolios, StashAway Simple and Simple Plus cash management, and StashAway Reserve private-market access for accredited investors. It runs consumer web and mobile apps across Singapore, Malaysia, Hong Kong, Thailand and the UAE/MENA, with client assets held in segregated accounts at DBS, HSBC, Saxo Capital Markets and Lion Global. StashAway is an end-user wealth product: it publishes no public developer API, SDK or developer portal, though it does publish an llms.txt for AI agents
  and runs a public vulnerability disclosure programme.'
image: https://cms-assets.stashaway.com/202402_Website_Homepage_SG_b53f4d30db.jpg
layout: provider
modified: '2026-08-29'
name: StashAway
nav: Providers
network: true
overview: 'StashAway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Investing, Robo-Advisor, and Financial-Services.


  StashAway''s developer surface includes support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Stashaway Plans Pricing
  plan_count: 0
  slug: stashaway-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Stashaway Rate Limits
  slug: stashaway-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/stashaway/refs/heads/main/screenshots/stashaway-2026-09-02T160817.png
security:
- kind: domain-security
  name: Stashaway Domain Security
  slug: stashaway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stashaway Vulnerability Disclosure
  slug: stashaway-vulnerability-disclosure
  summary_line: Hackerone
slug: stashaway
tags:
- Company
- Wealth Management
- Investing
- Robo-Advisor
- Financial-Services
- Asset Management
- ETFs
- Cash Management
- Fintech
- Singapore
- Private Markets
website: https://www.stashaway.sg/
---
