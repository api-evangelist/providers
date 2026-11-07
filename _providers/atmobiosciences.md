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
- description: API for Atmobiosciences (no public contract discovered)
  name: Atmobiosciences API
  slug: atmobiosciences-api
artifact_total: 2
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.atmobiosciences.com/feed/
- group: other
  href: https://artifacts.apis.io/atmobiosciences/hosts/atmobiosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atmobiosciences-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atmobiosciences.com/terms-and-conditions-clinical-research/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atmobiosciences.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.atmobiosciences.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.atmobiosciences.com/team/
- group: auth
  href: https://artifacts.apis.io/atmobiosciences/security/atmobiosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atmobiosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atmobiosciences.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract found at the API host (api.atmobiosciences.com)
  evidence:
  - status: failed
    url: https://api.atmobiosciences.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atmobiosciences (Atmo Biosciences) develops ingestible gas‑sensing capsules that measure gastrointestinal gases in real time. The Atmo Gas Capsule System provides clinicians with direct, localized data on gas production throughout the GI tract, enabling improved diagnosis and monitoring of motility disorders. The company’s platform integrates hardware, software, and data analytics to deliver actionable insights for research and clinical care.
layout: provider
modified: '2026-10-06'
name: Atmobiosciences
nav: Providers
network: true
overview: Atmobiosciences is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bioscience, Medical Devices, Gastroenterology, and Diagnostics.
random_paper: 8
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/atmobiosciences/atmobiosciences-2026-10-11T100735.png
security:
- kind: domain-security
  name: Atmobiosciences Domain Security
  slug: atmobiosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atmobiosciences
tags:
- Company
- Bioscience
- Medical Devices
- Gastroenterology
- Diagnostics
- Data Analytics
website: https://www.atmobiosciences.com
---
