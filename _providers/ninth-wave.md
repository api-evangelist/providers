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
- description: Open finance API platform for secure data exchange, supporting open banking and embedded finance.
  name: Ninth Wave API
  slug: ninth-wave-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ninth-wave/llms/ninth-wave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ninth-wave-llms.txt
- group: other
  href: https://artifacts.apis.io/ninth-wave/hosts/ninth-wave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ninth-wave-hosts.yml
- group: other
  href: https://artifacts.apis.io/ninth-wave/vendors/ninth-wave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ninth-wave-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ninth-wave.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://ninth-wave.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://ninth-wave.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://ninth-wave.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ninth-wave.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ninth-wave
- group: auth
  href: https://artifacts.apis.io/ninth-wave/security/ninth-wave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ninth-wave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ninth-wave.com/
coverage:
  checked: '2026-10-21'
  detail: Docs page renders a JavaScript shell with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.ninth-wave.com/register
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Ninth Wave provides open finance software solutions that enable secure data exchange through a single integration point. Their platform connects financial institutions, fintechs, and developers to streamline data connectivity, compliance, and API-driven services, supporting open banking, data aggregation, and secure transaction processing.
image: https://ninth-wave.com/wp-content/uploads/2024/05/9W_compliance-graphics-01-1024x1014.png
layout: provider
modified: '2026-10-21'
name: Ninth Wave
nav: Providers
network: true
overview: 'Ninth Wave is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Open Banking, Data Integration, and API Platform.


  Ninth Wave''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 10.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ninth-wave/ninth-wave-2026-11-03T140226.png
security:
- kind: domain-security
  name: Ninth Wave Domain Security
  slug: ninth-wave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ninth-wave
tags:
- Company
- Finance
- Open Banking
- Data Integration
- API Platform
- Fintech
website: https://ninth-wave.com/
---
