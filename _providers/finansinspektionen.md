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
- description: Public API information not found; the website provides financial supervisory data but no machine-readable API spec.
  name: Finansinspektionen API
  slug: finansinspektionen-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/finansinspektionen/security/finansinspektionen-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/finansinspektionen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/finansinspektionen/well-known/finansinspektionen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/finansinspektionen-security.txt
- group: agent
  href: https://artifacts.apis.io/finansinspektionen/well-known/finansinspektionen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finansinspektionen-well-known.yml
- group: other
  href: https://artifacts.apis.io/finansinspektionen/hosts/finansinspektionen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finansinspektionen-hosts.yml
- group: auth
  href: https://artifacts.apis.io/finansinspektionen/security/finansinspektionen-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/finansinspektionen-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/finansinspektionen/security/finansinspektionen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finansinspektionen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fi.se/
coverage:
  checked: '2026-10-15'
  detail: The Finansinspektionen website provides information but no machine-readable API specification was found after probing common spec locations.
  evidence:
  - status: 404
    url: https://fi.se/openapi.json
  - status: 404
    url: https://api.fi.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Finansinspektionen is Sweden’s financial supervisory authority, responsible for overseeing banks, insurance companies, securities firms and other financial institutions. It works to ensure market stability, protect consumers, enforce regulations, and promote transparency in the financial sector. The agency publishes reports, guidelines, and registers, and provides public data and resources related to financial supervision and compliance.
layout: provider
modified: '2026-10-15'
name: Finansinspektionen
nav: Providers
network: true
overview: Finansinspektionen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Supervision, Regulations, Sweden, and Government.
random_paper: 22
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 6.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/finansinspektionen/finansinspektionen-2026-11-03T132018.png
security:
- kind: domain-security
  name: Finansinspektionen Domain Security
  slug: finansinspektionen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Finansinspektionen Vulnerability Disclosure
  slug: finansinspektionen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: finansinspektionen
tags:
- Finance
- Supervision
- Regulations
- Sweden
- Government
website: https://fi.se/
---
