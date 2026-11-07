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
- description: Data integration API for transport and logistics
  name: Adabt API
  slug: adabt-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/adabt/hosts/adabt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adabt-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adabt
- group: auth
  href: https://artifacts.apis.io/adabt/security/adabt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adabt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adabt.com/
- group: operate
  title: ''
  type: Support
  url: https://adabt.com/contact
- group: company
  title: ''
  type: Blog
  url: https://adabt.com/blog
coverage:
  checked: '2026-10-15'
  detail: OpenAPI spec at https://app.adabt.com/openapi.json redirects to a login page, blocking access.
  evidence:
  - status: 307
    url: https://app.adabt.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-15'
description: Adabt provides data integration solutions for the transport and logistics sector, enabling automated data exchange between shippers, carriers, and partners. Their platform offers no-code development, real-time monitoring, and AI-powered document processing to streamline workflows and accelerate digital transformation for logistics companies.
image: https://www.adabt.com/social/og-home-nl.png
layout: provider
modified: '2026-10-15'
name: Adabt
nav: Providers
network: true
overview: 'Adabt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, Transport, Logistics, and Software-as-a-Service.


  Adabt''s developer surface includes support, engineering blog, and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 6.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/adabt/adabt-2026-11-03T120228.png
security:
- kind: domain-security
  name: Adabt Domain Security
  slug: adabt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adabt
tags:
- Data Integration
- Transport
- Logistics
- Software-as-a-Service
website: https://adabt.com/
---
