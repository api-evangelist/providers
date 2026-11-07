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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aivonic-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aivonic-ai/llms/aivonic-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aivonic-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/aivonic-ai/hosts/aivonic-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aivonic-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aivonic-ai/vendors/aivonic-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aivonic-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.aivonic.ai/login
- group: auth
  href: https://artifacts.apis.io/aivonic-ai/security/aivonic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivonic-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aivonic.ai/
- group: company
  title: ''
  type: Blog
  url: https://aivonic.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aivonic.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aivonic.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aivonic.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://aivonic.ai/contact
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine-readable spec was found on any owned host.
  evidence:
  - status: 200
    url: https://aivonic.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Aivonic Labs is a Swedish AI development company founded in 2025. We build AI agents, voice AI agents, automation solutions, and custom AI systems for businesses worldwide, offering platforms with voice capabilities in 29 languages, infinite memory, and the SAGE protocol for trust-based autonomy.
image: https://aivonic.ai/images/aivonic_logo_white_transparent.png
layout: provider
modified: '2026-11-01'
name: Aivonic Labs
nav: Providers
network: true
overview: 'Aivonic Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Voice AI, Software-as-a-Service, and Sweden.


  Aivonic Labs'' developer surface includes engineering blog, pricing, support, and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 16.1
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aivonic Ai Domain Security
  slug: aivonic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aivonic-ai
tags:
- Artificial Intelligence
- Automation
- Voice AI
- Software-as-a-Service
- Sweden
website: https://aivonic.ai/
---
