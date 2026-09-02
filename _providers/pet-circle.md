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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.petcircle.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PawsForLife
- group: operate
  title: ''
  type: Support
  url: https://www.petcircle.com.au/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.petcircle.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.petcircle.com.au/privacy
- group: build
  title: ''
  type: Packages
  url: packages/pet-circle-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pet-circle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pet-circle-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pet-circle-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pet-circle-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Pet Circle runs a headless commerce stack (commercetools + Vue Storefront/Alokai on Vercel) entirely for its own consumer storefront — no api., developer. or docs. subdomain resolves in DNS, every /.well-known/ path on www.petcircle.com.au returns a real 404, and the only first-party code it has ever published is two single-release internal npm libraries from January 2024; partner integration is arranged out of band via EDI and affiliate networks rather than a developer program.
  evidence:
  - status: 404
    url: https://www.petcircle.com.au/.well-known/api-catalog
  - status: 404
    url: https://www.petcircle.com.au/.well-known/agent-card.json
  - status: 404
    url: https://www.petcircle.com.au/.well-known/security.txt
  - status: 0
    url: https://api.petcircle.com.au/openapi.json
  - status: 429
    url: https://www.petcircle.com.au/robots.txt
  - status: 200
    url: https://github.com/PawsForLife
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Pet Circle is Australia''s largest online pet-supplies retailer, selling pet food, flea and worming treatments, toys, bedding and prescription veterinary products direct to consumers across Australia. Founded in mid-2011 in Sydney by Mike Frizell and James Edwards as Paws for Life and rebranded to Pet Circle in early 2014, the company reached unicorn status with a valuation above AU$1 billion after a $125 million Series C in December 2021, and extended into adjacent lines with Pet Circle Pharmacy (petcirclepharma.com.au) and Pet Circle Insurance (petcircleinsurance.com.au, launched May 2023). Its storefront is a headless commerce stack — a commercetools back end fronted by a Vue Storefront / Alokai layer on Vercel, with Google Cloud Functions gluing SaaS services together — but Pet Circle operates that architecture internally: it publishes no public developer portal, no API reference, and no machine-readable API contract. Trading-partner integration is handled out of band through
  EDI, and consumer-side partner traffic runs through third-party affiliate networks rather than a first-party API program.'
image: https://avatars.githubusercontent.com/u/5011331?v=4
layout: provider
modified: '2026-08-26'
name: Pet Circle
nav: Providers
network: true
overview: 'Pet Circle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Pets, and Consumer.


  Pet Circle''s developer surface includes support and 9 more developer resources.'
plans:
- name: Pet Circle Plans Pricing
  plan_count: 0
  slug: pet-circle-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Pet Circle Rate Limits
  slug: pet-circle-rate-limits
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pet Circle Domain Security
  slug: pet-circle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pet-circle
tags:
- Company
- Retail
- E-Commerce
- Pets
- Consumer
- Australia
- Direct to Consumer
- Pet Supplies
- Headless Commerce
website: https://www.petcircle.com.au/
---
