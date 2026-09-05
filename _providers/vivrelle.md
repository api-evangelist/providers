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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.vivrelle.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vivrelle.com/join-the-club
- group: start
  title: ''
  type: SignUp
  url: https://www.vivrelle.com/apply/account
- group: start
  title: ''
  type: Login
  url: https://www.vivrelle.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vivrelle.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vivrelle.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.vivrelle.com/contact-us
- group: commercial
  title: ''
  type: Plans
  url: plans/vivrelle-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vivrelle-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vivrelle-llms.txt
coverage:
  checked: '2026-09-04'
  detail: 'Vivrelle is a direct-to-consumer luxury-accessory rental membership club that clearly builds software — a Next.js storefront, an iOS/Android app, and the "Ella AI" styling tool built with Revolve and FWRD — but ships all of it strictly as an end-user product: api.vivrelle.com does not resolve at all, every contract path on www.vivrelle.com (/openapi.json, /swagger.json, /graphql, /api-docs, /developers, /llms.txt) returns a genuine Next.js 404, all nine well-known paths 404 on every reachable host, no first-party package exists on npm, PyPI, RubyGems or crates.io, and the company''s own GitHub organization has zero public repositories, so the only backend is the private Next.js /api namespace that robots.txt disallows and that serves Vivrelle''s own clients.'
  evidence:
  - status: 404
    url: https://www.vivrelle.com/openapi.json
  - status: 404
    url: https://www.vivrelle.com/graphql
  - status: 404
    url: https://www.vivrelle.com/developers
  - status: 404
    url: https://www.vivrelle.com/llms.txt
  - status: 404
    url: https://www.vivrelle.com/.well-known/agent-card.json
  - status: 200
    url: https://www.vivrelle.com/robots.txt
  - status: 200
    url: https://github.com/Vivrelle
  - status: 200
    url: https://www.vivrelle.com/faqs
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'Vivrelle is a New York City based members-only club, founded in 2018, that lends luxury accessories — designer handbags, fine and designer jewelry, watches and diamonds from houses including Chanel, Hermès, Louis Vuitton, Gucci, Dior and Van Cleef & Arpels — to members for a recurring monthly fee rather than selling them. Membership is sold in published consumer tiers (Classique, Couture, Classique+, Couture+, plus the Premier and invite-only Réservé add-ons), and the product reaches members through vivrelle.com and a first-party iOS/Android app that includes "Ella AI", an AI styling tool built with Revolve and FWRD. Vivrelle is a direct-to-consumer subscription retail business, not a software vendor: it publishes no developer portal, no API documentation, no OpenAPI/GraphQL/AsyncAPI contract, no SDK in any public package registry, and no webhook or MCP surface. Its GitHub organization exists but carries zero public repositories, and its application backend is private to its
  own web and mobile clients.'
image: https://www.vivrelle.com/opengraph-image.jpg
layout: provider
modified: '2026-09-04'
name: Vivrelle
nav: Providers
network: true
overview: 'Vivrelle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Luxury, Retail, and Ecommerce.


  Vivrelle''s developer surface includes pricing, signup flow, support, and 7 more developer resources.'
plans:
- name: Vivrelle Plans Pricing
  plan_count: 6
  slug: vivrelle-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Vivrelle Rate Limits
  slug: vivrelle-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Vivrelle Domain Security
  slug: vivrelle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vivrelle
tags:
- Company
- Fashion
- Luxury
- Retail
- Ecommerce
- Subscription
- Membership
- Rental
- Jewelry
- Accessories
website: https://www.vivrelle.com/
---
