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
- description: Obseva provides a monitoring and analytics platform for enterprises.
  name: Obseva API
  slug: obseva-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/obseva/vendors/obseva-vendors.yml
  title: ''
  type: Vendors
  url: vendors/obseva-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://90phutzav.tv/security-policy
- group: auth
  href: https://artifacts.apis.io/obseva/well-known/obseva-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/obseva-security.txt
- group: agent
  href: https://artifacts.apis.io/obseva/well-known/obseva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/obseva-well-known.yml
- group: other
  href: https://artifacts.apis.io/obseva/hosts/obseva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/obseva-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.obseva.com
- group: auth
  href: https://artifacts.apis.io/obseva/security/obseva-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/obseva-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/obseva/security/obseva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/obseva-domain-security.yml
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract could be found despite probing documented hosts.
  evidence:
  - status: 404
    url: https://api.obseva.com/openapi.json
  - status: 404
    url: https://api.obseva.com/swagger.json
  - status: 404
    url: https://api.obseva.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Obseva is a technology company focused on providing advanced monitoring and analytics solutions for enterprise environments. It offers a platform that aggregates data from various sources, applies AI-driven insights, and delivers actionable dashboards to improve operational efficiency and decision-making across industries.
image: https://cdn.90phutzav.tv/2022/10/logo-90phut-tv-truc-tiep-bong-da.jpg
layout: provider
modified: '2026-10-26'
name: Obseva
nav: Providers
network: true
overview: Obseva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Analytics, Artificial Intelligence, and Enterprise.
random_paper: 16
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 6.4
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/obseva/obseva-2026-11-03T140447.png
security:
- kind: domain-security
  name: Obseva Domain Security
  slug: obseva-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Obseva Vulnerability Disclosure
  slug: obseva-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: obseva
tags:
- Company
- Monitoring
- Analytics
- Artificial Intelligence
- Enterprise
website: https://www.obseva.com
---
