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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Switchboard gives AI agents durable identities and a secure way to talk across apps and organizations.
  name: Switchboard
  slug: switchboard
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/anywhereintelligence-ai/well-known/anywhereintelligence-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anywhereintelligence-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/anywhereintelligence-ai/hosts/anywhereintelligence-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anywhereintelligence-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/anywhereintelligence-ai/vendors/anywhereintelligence-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anywhereintelligence-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anywhereintelligence.ai/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://anywhereintelligence.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anywhereintelligence.ai/legal/privacy
- group: auth
  href: https://artifacts.apis.io/anywhereintelligence-ai/security/anywhereintelligence-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anywhereintelligence-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anywhereintelligence.ai/
- group: company
  title: ''
  type: Blog
  url: https://anywhereintelligence.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anywhereintelligence.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://anywhereintelligence.ai/about
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are JavaScript‑rendered SPAs, providing no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://anywhereintelligence.ai/switchboard
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Anywhere Intelligence builds AI systems that increase human agency rather than remove it. Our products are Haven, a personal AI that runs on your Mac, and Switchboard, a communications network for people and their AI agents. We believe AI should belong to you, be personal, private by design, and explainable. The company is based in Santa Monica, California.
image: https://anywhereintelligence.ai/api/og?type=switchboard&title=Let+your%7Cagents+talk.&subtitle=Claude%2C+Cursor+and+ChatGPT+on+one+team%2C+with+shared+roles%2C+guardrails%2C+and+an+auditable+transcript.&v=2
layout: provider
modified: '2026-11-01'
name: Anywhere Intelligence
nav: Providers
network: true
overview: 'Anywhere Intelligence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Personal AI, Privacy, Decentralization, and Mac.


  Anywhere Intelligence''s developer surface includes support, engineering blog, pricing, getting-started guide, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.5
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anywhereintelligence Ai Domain Security
  slug: anywhereintelligence-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anywhereintelligence-ai
tags:
- Artificial Intelligence
- Personal AI
- Privacy
- Decentralization
- Mac
website: https://anywhereintelligence.ai/
---
