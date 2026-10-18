---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.2
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.presti.ai/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/presti/refs/heads/main/plans/presti-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/presti-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.presti.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/presti/refs/heads/main/security/presti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/presti-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://presti.ai/
- group: start
  title: ''
  type: SignUp
  url: https://scale.presti.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://scale.presti.ai/auth/login
- group: operate
  title: ''
  type: Support
  url: https://presti.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://presti.ai/terms-and-conditions
created: '2026-07-17'
description: Presti (operated by Teker AI SAS, France) is an AI agent platform for automated product image and video production at scale. eCommerce teams, retailers, and brands write plain-language briefs — attaching product images, packshots, CSVs, or inspiration URLs — and Presti generates studio-quality product staging, 360-degree spins, image-to-video, close-ups, variants, dimension overlays, and infographics, then routes them through a collaborative review-and-approval workspace. It orchestrates multiple third-party generative models (Google Gemini and Veo, OpenAI GPT Image, Flux, Kling, Seedance, Grok, Photoroom) and encodes visual identity via reusable Brand Skills. API access is offered on the Enterprise plan but is not publicly documented.
image: https://cdn.prod.website-files.com/69a91c9a68fd25dc91b9ed09/69aec8ad1535208895c1e43c_Generated%20Image%20February%2002%2C%202026%20-%2010_25AM%202%20(1).avif
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.presti.ai over HTTP.
  name: Presti MCP Server
  slug: presti
modified: '2026-10-06'
name: Presti
nav: Providers
network: true
overview: 'Presti is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Artificial Intelligence, Generative AI, and E-Commerce.


  Presti''s developer surface includes pricing, engineering blog, signup flow, support, and 5 more developer resources.'
plans:
- name: Presti Plans Pricing
  plan_count: 4
  slug: presti-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.5
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 51.7
    operational_transparency: 0.0
  previous_composite: 9.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/presti/refs/heads/main/screenshots/presti-2026-09-02T151945.png
security:
- kind: domain-security
  name: Presti Domain Security
  slug: presti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: presti
tags:
- Company
- Applicative Saas
- Artificial Intelligence
- Generative AI
- E-Commerce
- Product Photography
- Image Generation
- Video Generation
- Retail
website: https://presti.ai/
---
