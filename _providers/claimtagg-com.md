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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/claimtagg-com/llms/claimtagg-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claimtagg-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claimtagg-com/well-known/claimtagg-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claimtagg-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claimtagg-com/hosts/claimtagg-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claimtagg-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claimtagg-com/vendors/claimtagg-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claimtagg-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.claimtagg.com/trust
- group: auth
  href: https://artifacts.apis.io/claimtagg-com/security/claimtagg-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claimtagg-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.claimtagg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.claimtagg.com/ueber-uns
- group: operate
  title: ''
  type: FAQ
  url: https://www.claimtagg.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.claimtagg.com/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.claimtagg.com/datenschutz
- group: company
  title: ''
  type: Blog
  url: https://www.claimtagg.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.claimtagg.com/kontakt
coverage:
  checked: '2026-11-03'
  detail: All attempted OpenAPI spec URLs on api.claimtagg.com returned HTTP 401, indicating the API is gated behind authentication.
  evidence:
  - status: 401
    url: https://api.claimtagg.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-03'
description: ClaimTagg is a Swiss‑based company offering smart NFC‑enabled luggage tags and related travel accessories. Their ecosystem includes ClaimyApp, ClaimyBox, ClaimyTracker, ClaimyCard, ClaimyWorld and ClaimyCoin, providing tracking, secure storage and digital rewards. The platform emphasizes data privacy under GDPR, 24/7 support, and multi‑language availability across Europe. Products are sold via their online store and B2B solutions, with a focus on secure, worry‑free travel.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/3c2468ba-e7d9-427b-a12c-e5b1dd867c05/id-preview-3bc64d5d--e9590161-a58b-4a3e-95a7-4fa77161be2e.lovable.app-1780212037750.png
layout: provider
modified: '2026-11-03'
name: ClaimTagg
nav: Providers
network: true
overview: 'ClaimTagg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Luggage, NFC, Smart Devices, and Swiss.


  ClaimTagg''s developer surface includes documentation, FAQ, engineering blog, support, and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claimtagg Com Domain Security
  slug: claimtagg-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claimtagg-com
tags:
- Travel
- Luggage
- NFC
- Smart Devices
- Swiss
website: https://www.claimtagg.com/
---
