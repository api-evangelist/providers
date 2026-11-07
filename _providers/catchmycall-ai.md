---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for CatchMyCall AI-powered call handling
  name: CatchMyCall API
  slug: catchmycall-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/catchmycall-ai/plans/catchmycall-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/catchmycall-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/catchmycall-ai/llms/catchmycall-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/catchmycall-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/catchmycall-ai/hosts/catchmycall-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchmycall-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catchmycall.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchmycall.ai/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://catchmycall.ai/pricing
- group: auth
  href: https://artifacts.apis.io/catchmycall-ai/security/catchmycall-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchmycall-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchmycall.ai/
created: '2026-11-04'
description: CatchMyCall provides AI-powered call handling and missed call automation for small businesses, clinics, salons, and professionals across India. It answers every business call 24×7, captures enquiries, and books appointments in multiple Indian languages, reducing missed leads and improving customer engagement.
image: https://catchmycall.ai/main-website/images/catchmycall-logo-horizontal.png
layout: provider
modified: '2026-11-04'
name: CatchMyCall
nav: Providers
network: true
overview: 'CatchMyCall is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Call Automation, Software-as-a-Service, and India.


  CatchMyCall''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Catchmycall Ai Plans Pricing
  plan_count: 4
  slug: catchmycall-ai-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catchmycall Ai Domain Security
  slug: catchmycall-ai-domain-security
  summary_line: TLSv1.3
slug: catchmycall-ai
tags:
- Company
- Artificial Intelligence
- Call Automation
- Software-as-a-Service
- India
- Business
website: https://catchmycall.ai/
---
