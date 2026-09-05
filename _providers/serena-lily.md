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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.serenaandlily.com/
- group: company
  title: ''
  type: About
  url: https://www.serenaandlily.com/about-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.serenaandlily.com/help-center
- group: operate
  title: ''
  type: Support
  url: https://www.serenaandlily.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.serenaandlily.com/createaccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.serenaandlily.com/CS-termsconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.serenaandlily.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serenaandlily
- group: company
  title: ''
  type: Careers
  url: https://www.serenaandlily.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.serenaandlily.com/press
- group: other
  title: ''
  type: Accessibility
  url: https://www.serenaandlily.com/accessibility
- group: other
  title: ''
  type: Locations
  url: https://www.serenaandlily.com/stores
- group: company
  title: ''
  type: Partners
  url: https://www.serenaandlily.com/trade
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/serenaandlily
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/serenaandlily
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/serenaandlily/
- group: other
  title: ''
  type: Pinterest
  url: https://www.pinterest.com/serenaandlily/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serena-lily-domain-security.yml
- group: other
  title: ''
  type: ContractDiscovery
  url: well-known/serena-lily-contract-discovery.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/serena-lily_stock/
coverage:
  checked: '2026-08-05'
  detail: 'Serena & Lily runs real API infrastructure for its own storefront — an AWS AppSync GraphQL endpoint at /graphql that answers anonymous queries but has introspection deliberately disabled, and an api.serenaandlily.com API Gateway that returns "Missing Authentication Token" on every path — yet it operates no developer program at all: no developer subdomain resolves, both agent-card paths return a clean 404, the only public repo in its GitHub org is a fork of an Amplience CMS extension, and no OpenAPI, SDL, SDK or llms.txt is published anywhere.'
  evidence:
  - status: 200
    url: https://www.serenaandlily.com/graphql
  - status: 403
    url: https://api.serenaandlily.com/openapi.json
  - status: 404
    url: https://www.serenaandlily.com/openapi.json
  - status: 404
    url: https://www.serenaandlily.com/.well-known/agent-card.json
  - status: 404
    url: https://www.serenaandlily.com/.well-known/agent.json
  - status: 200
    url: https://github.com/serenaandlily
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: Serena & Lily is a California home furnishings and lifestyle brand founded in 2003 in Sausalito by textile designer Serena Dugan and entrepreneur Lily Kanter. It sells furniture, custom upholstery, bedding, rugs, lighting, wallpaper, art and home decor direct to consumers through its e-commerce site, a printed catalog, and a network of physical Design Shops, alongside a Designer Circle trade program for interior designers. The storefront runs on a headless, composable commerce stack — Elastic Path for commerce and Amplience for content, served from a Vercel-hosted front end in front of AWS AppSync and Amazon API Gateway — but Serena & Lily publishes no developer program, no public API documentation, and no machine-readable specification of any kind. The GraphQL endpoint backing the storefront answers anonymous requests with introspection disabled, and the api.serenaandlily.com gateway rejects every unauthenticated path.
image: https://cdn.media.amplience.net/s/serenaandlily/SVG_Logo_Footer
layout: provider
modified: '2026-08-05'
name: Serena & Lily
nav: Providers
network: true
overview: 'Serena & Lily is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Home Furnishings, and Furniture.


  Serena & Lily''s developer surface includes support, signup flow, and 18 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Serena Lily Domain Security
  slug: serena-lily-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: serena-lily
tags:
- Company
- Retail
- E-Commerce
- Home Furnishings
- Furniture
- Interior Design
- Home Decor
- Direct to Consumer
website: https://www.serenaandlily.com/
---
