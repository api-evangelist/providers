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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ai-church/well-known/ai-church-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-church-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai-church/hosts/ai-church-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-church-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai-church/vendors/ai-church-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-church-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ai-church/security/ai-church-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-church-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai.church/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcp.ai.church
- group: company
  title: ''
  type: Blog
  url: https://ai.church/
- group: operate
  title: ''
  type: Support
  url: https://ai.church/#contact
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: no-response
    url: https://api.ai.church/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI Church provides production AI engineering and consulting services, helping teams automate workflows with AI agents, retrieval-augmented generation, and cloud infrastructure. Based in Kent, UK, founder Vadim offers end‑to‑end AI system design, building and shipping AI products to production. The company emphasizes no‑lock‑in engagements, free assessments, and tailored solutions for repetitive tasks, aiming to free teams from manual work and accelerate AI adoption.
image: https://ai.church/images/og.png
layout: provider
modified: '2026-11-01'
name: AI Church
nav: Providers
network: true
overview: 'AI Church is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Engineering, Consulting, Automation, and Machine Learning.


  AI Church''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 7.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Church Domain Security
  slug: ai-church-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ai-church
tags:
- Artificial Intelligence
- Engineering
- Consulting
- Automation
- Machine Learning
website: https://ai.church/
---
