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
- description: Banyan Infrastructure provides project finance software for infrastructure funds, developers, and green banks.
  name: Banyan Infrastructure API
  slug: banyan-infrastructure-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/banyan-infrastructure/hosts/banyan-infrastructure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banyan-infrastructure-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://banyaninfrastructure.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://banyaninfrastructure.com/news
- group: auth
  href: https://artifacts.apis.io/banyan-infrastructure/security/banyan-infrastructure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banyan-infrastructure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banyaninfrastructure.com/
coverage:
  checked: '2026-09-27'
  detail: OpenAPI endpoint returned HTML page instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://trust.banyaninfrastructure.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Banyan Infrastructure provides project finance software for infrastructure funds, developers, and green banks. Their platform unifies workflow and data across origination, underwriting, portfolio management, and compliance, accelerating capital flow into infrastructure projects. The solution replaces fragmented systems like Salesforce and Excel with a single data layer, supporting owners, operators, and financiers.
image: https://framerusercontent.com/images/SJAtGkO47mbMzfaasv6YXe4auk.png
layout: provider
modified: '2026-09-27'
name: Banyan Infrastructure
nav: Providers
network: true
overview: Banyan Infrastructure is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Infrastructure, Software, Project Finance, and Renewable Energy.
random_paper: 7
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 7.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 6.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/banyan-infrastructure/banyan-infrastructure-2026-10-11T101535.png
security:
- kind: domain-security
  name: Banyan Infrastructure Domain Security
  slug: banyan-infrastructure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banyan-infrastructure
tags:
- Finance
- Infrastructure
- Software
- Project Finance
- Renewable Energy
website: https://banyaninfrastructure.com/
---
