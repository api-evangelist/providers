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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ai-orchestration-jp/hosts/ai-orchestration-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-orchestration-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-orchestration-jp/vendors/ai-orchestration-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-orchestration-jp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-orchestration.jp/terms/
- group: operate
  title: ''
  type: Support
  url: https://ai-orchestration.jp/products/hojokin-ai/support/
- group: auth
  title: ''
  type: Security
  url: https://ai-orchestration.jp/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-orchestration.jp/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://ai-orchestration.jp/news/
- group: auth
  href: https://artifacts.apis.io/ai-orchestration-jp/security/ai-orchestration-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-orchestration-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-orchestration.jp/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://ai-orchestration.jp/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: AI Orchestration is a Japanese AI consultancy and integration studio that designs and implements enterprise AI solutions. They offer AI infrastructure, ChatGPT plugin development, public grant search automation, and AI orchestration services, helping companies turn AI concepts into usable products. The team, led by founder Masaki Yamamoto, brings experience from Fujitsu, Dentsu, and Nomura Research Institute.
image: https://ai-orchestration.jp/images/ai-orchestration-logo.png
layout: provider
modified: '2026-11-01'
name: AI Orchestration
nav: Providers
network: true
overview: 'AI Orchestration is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Consulting, Japan, Enterprise AI, and Integration.


  AI Orchestration''s developer surface includes support and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 11.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Orchestration Jp Domain Security
  slug: ai-orchestration-jp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ai-orchestration-jp
tags:
- Artificial Intelligence
- Consulting
- Japan
- Enterprise AI
- Integration
website: https://ai-orchestration.jp/
---
