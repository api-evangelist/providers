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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/datacommenter-com/hosts/datacommenter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datacommenter-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datacommenter.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datacommenter.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/datacommenter-com/security/datacommenter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datacommenter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datacommenter.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host.
  evidence:
  - status: error
    url: https://api.datacommenter.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: The Data Commenter is a media platform covering data markets, alternative data, and the AI training‑data economy. It publishes news, analysis, and resources for data professionals, investors, and AI developers, offering insights into data licensing, market trends, and emerging data products.
image: https://datacommenter.com/wp-content/uploads/2026/07/DC-Commenter-Favicon-e1783300260359.png
layout: provider
modified: '2026-11-04'
name: The Data Commenter
nav: Providers
network: true
overview: The Data Commenter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data Markets, AI Training Data, News, Journalism, and Data Economy.
random_paper: 16
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datacommenter Com Domain Security
  slug: datacommenter-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: datacommenter-com
tags:
- Data Markets
- AI Training Data
- News
- Journalism
- Data Economy
website: https://datacommenter.com/
---
