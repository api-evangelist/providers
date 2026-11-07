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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only catalog and MCP discovery endpoints for Alt eSIM.
  name: Alt eSIM Public API
  slug: alt-esim-public-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/altesim-com/llms/altesim-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altesim-com-llms.txt
- group: other
  href: https://artifacts.apis.io/altesim-com/hosts/altesim-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altesim-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/altesim-com/vendors/altesim-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altesim-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altesim.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altesim.com/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://altesim.com/en/blog
- group: auth
  href: https://artifacts.apis.io/altesim-com/security/altesim-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altesim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altesim.com/
created: '2026-11-01'
description: Alt eSIM is a Hong Kong‑based travel eSIM provider offering prepaid mobile data plans for travelers in over 70 destinations worldwide. Customers can purchase eSIM data instantly online, receive a QR code via email within seconds, and activate on‑device without SIM swaps. The service emphasizes transparent USD pricing, secure Stripe payments, and end‑to‑end TLS 1.3 encryption. Alt eSIM supports major carriers such as KDDI, SoftBank, SK Telecom, Vodafone, and Orange, and provides multilingual support via WhatsApp.
image: https://altesim.com/og.png
layout: provider
modified: '2026-11-01'
name: Alt eSIM
nav: Providers
network: true
overview: 'Alt eSIM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, eSIM, Hong Kong, and Mobile Data.


  Alt eSIM''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altesim Com Domain Security
  slug: altesim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altesim-com
tags:
- Company
- Travel
- eSIM
- Hong Kong
- Mobile Data
- Prepaid
website: https://altesim.com/
---
