---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://thrivemarket.com/
- group: company
  title: ''
  type: About
  url: https://thrivemarket.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://thrivemarket.com/blog
- group: operate
  title: ''
  type: Support
  url: https://thrivemarket.com/faq/index/contactus
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.thrivemarket.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://thrivemarket.com/join
- group: start
  title: ''
  type: Login
  url: https://thrivemarket.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thrivemarket.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thrivemarket.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThriveMarket
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrive-market-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrive-market-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: Thrive Market is a direct-to-consumer grocery retailer with no developer program at all — developer.thrivemarket.com and developers.thrivemarket.com are NXDOMAIN, and its own 2,785-entry llms.txt, which indexes the entire public site, contains zero occurrences of "API", "developer", "SDK" or "webhook"; api.thrivemarket.com is the mobile/web app backend and returns the same NotFoundHttpException JSON for every path including a control path, so no spec is exposed there.
  evidence:
  - status: 200
    url: https://thrivemarket.com/llms.txt
  - status: 0
    url: https://developers.thrivemarket.com/
  - status: 200
    url: https://api.thrivemarket.com/openapi.json
  - status: 200
    url: https://api.thrivemarket.com/kin-control-9931
  - status: 200
    url: https://thrivemarket.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'Thrive Market is a membership-based online grocery retailer headquartered in Marina del Rey, California, selling organic and natural food, pantry staples, frozen meat and seafood, beauty and personal care, baby, pet and household products directly to consumers across the United States. Members pay an annual or monthly fee in exchange for below-retail pricing, and the company operates its own Thrive Market private label alongside thousands of third-party brands. It filters its catalog by diet, ingredient, certification and social value, accepts EBT/SNAP for grocery purchases, and funds free memberships for lower-income families through its Thrive Gives program. Thrive Market is a direct-to-consumer commerce company: it ships a website and mobile apps to shoppers, but publishes no public developer program, API reference, or machine-readable API contract.'
image: https://img.thrivemarket.com/custom_assets/bee32e3256b3db07765c2a3881fc7da8.jpg
layout: provider
modified: '2026-08-05'
name: Thrive Market
nav: Providers
network: true
overview: 'Thrive Market is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Grocery, and Food and Beverage.


  Thrive Market''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Thrive Market Domain Security
  slug: thrive-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thrive-market
tags:
- Company
- E-Commerce
- Retail
- Grocery
- Food and Beverage
- Consumer Goods
- Direct to Consumer
- Membership
- Health and Wellness
website: https://thrivemarket.com/
---
