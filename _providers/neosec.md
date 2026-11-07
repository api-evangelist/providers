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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Customer portal API for XIEM Central platform offering security telemetry and management.
  name: XIEM Central API
  slug: xiem-central-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://neosec.eu/compliance
- group: agent
  href: https://artifacts.apis.io/neosec/llms/neosec-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/neosec-llms.txt
- group: other
  href: https://artifacts.apis.io/neosec/hosts/neosec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/neosec-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://intel.neosec.eu/news
- group: start
  title: ''
  type: Login
  url: https://intel.neosec.eu/signin
- group: auth
  href: https://artifacts.apis.io/neosec/security/neosec-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/neosec-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/neosec/security/neosec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/neosec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://neosec.eu/
coverage:
  checked: '2026-10-21'
  detail: Portal pages return HTML shells for spec URLs, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://portal.neosec.eu/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Neosec is an independent cybersecurity partner based in Germany, founded in 2016. It provides visibility and control over threats, vulnerabilities, and incidents in IT environments through its Radar®, Sonar®, XIEM® and Intel platforms, helping organizations manage security risks effectively.
image: https://neosec.eu/og/site?v=9e6e45dc
layout: provider
modified: '2026-10-21'
name: Neosec
nav: Providers
network: true
overview: Neosec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Germany, Threat Intelligence, and IT Security.
random_paper: 13
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 11.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Neosec Domain Security
  slug: neosec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Neosec Trust Center
  slug: neosec-trust-center
  summary_line: ISO 27001, GDPR
slug: neosec
tags:
- Company
- Cybersecurity
- Germany
- Threat Intelligence
- IT Security
website: https://neosec.eu/
---
