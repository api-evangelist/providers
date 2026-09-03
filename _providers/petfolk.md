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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petfolk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://petfolk.com/
- group: start
  title: ''
  type: Login
  url: https://petfolk.com/login
- group: start
  title: ''
  type: SignUp
  url: https://petfolk.com/book
- group: operate
  title: ''
  type: Support
  url: https://petfolk.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://petfolk.com/faq
- group: company
  title: ''
  type: Blog
  url: https://petfolk.com/petfolklore
- group: commercial
  title: ''
  type: Pricing
  url: https://petfolk.com/services/pricing
- group: company
  title: ''
  type: PressRoom
  url: https://petfolk.com/pressroom
- group: company
  title: ''
  type: Careers
  url: https://petfolk.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://petfolk.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://petfolk.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/petfolk-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/petfolk-well-known.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/petfolk_stock/
created: '2026-08-02'
description: 'Petfolk is a Charlotte, North Carolina based veterinary care company that operates a network of modern, company-owned pet care centers across the US Southeast and Texas, paired with a consumer mobile app. Founded and led by veterinarian Dr. Audrey Wystrach, Petfolk provides primary and wellness care, sick and urgent care, dentistry, surgery, spay and neuter, vaccinations and diagnostics for dogs and cats, delivered under a "gentle handling" clinical model with seven-day-a-week hours and published, transparent pricing. The Petfolk iOS and Android app lets pet parents book in-person or virtual appointments, message their care team around the clock, request medications and access their pet''s medical records; a paid PetfolkCare membership layers on 24/7 veterinary support and per-visit savings. The company raised a $40M Series B in October 2023 led by Movendo Capital, with White Star Capital and Idea Farm Ventures participating. Petfolk is a consumer veterinary services operator,
  not an API provider: as of this profiling pass it publishes no public developer portal, API documentation, OpenAPI/GraphQL contract, SDKs or MCP server. It does publish a hand-authored llms.txt at the site root, which is the company''s only machine-readable, agent-facing surface.'
image: https://images.ctfassets.net/hivti1x80euy/69WzFpgg5SgRxcyeM6VeRP/5d82cdb7cf00e502733318a0125f3816/social_og_72369bd6-c9fe-4947-bb69-891c1daf2cb5.webp
layout: provider
modified: '2026-08-02'
name: Petfolk
nav: Providers
network: true
overview: 'Petfolk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, veterinary-care, Animal Health, Pet Care, and Pet Health.


  Petfolk''s developer surface includes signup flow, support, FAQ, engineering blog, pricing, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/petfolk/refs/heads/main/screenshots/petfolk-2026-09-02T151114.png
security:
- kind: domain-security
  name: Petfolk Domain Security
  slug: petfolk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: petfolk
tags:
- Veterinary
- veterinary-care
- Animal Health
- Pet Care
- Pet Health
- Healthcare
- Telehealth
- Virtual Care
- Urgent Care
- Clinics
- Membership
- Consumer Health
- Mobile App
- North Carolina
website: https://petfolk.com/
---
