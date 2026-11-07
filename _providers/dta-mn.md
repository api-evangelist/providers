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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Data Terminal & Archive provides a signed source‑bound archive of Mongolia's macroeconomic data via its API.
  name: DTA API
  slug: dta-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://dta.mn/about
- group: agent
  href: https://artifacts.apis.io/dta-mn/llms/dta-mn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dta-mn-llms.txt
- group: auth
  href: https://artifacts.apis.io/dta-mn/well-known/dta-mn-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dta-mn-security.txt
- group: agent
  href: https://artifacts.apis.io/dta-mn/well-known/dta-mn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dta-mn-well-known.yml
- group: other
  href: https://artifacts.apis.io/dta-mn/hosts/dta-mn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dta-mn-hosts.yml
- group: other
  href: https://artifacts.apis.io/dta-mn/vendors/dta-mn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dta-mn-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://dta.mn/news
- group: auth
  href: https://artifacts.apis.io/dta-mn/security/dta-mn-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dta-mn-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dta-mn/security/dta-mn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dta-mn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dta.mn/
coverage:
  checked: '2026-11-06'
  detail: LLMS.txt provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are published.
  evidence:
  - status: 200
    url: https://dta.mn/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Data Terminal & Archive (DTA) is a Mongolian data platform providing real‑time economic indicators, market rates, and archival information. The site offers currency exchange rates, market data, political news, and comparative analytics, serving analysts, businesses, and the public with up‑to‑date economic statistics and historical archives.
image: https://dta.mn/system/share-card.png
layout: provider
modified: '2026-11-06'
name: Data Terminal & Archive
nav: Providers
network: true
overview: Data Terminal & Archive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Mongolia, Economics, and OpenArchive.
random_paper: 1
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dta Mn Domain Security
  slug: dta-mn-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dta Mn Vulnerability Disclosure
  slug: dta-mn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dta-mn
tags:
- Company
- Data
- Mongolia
- Economics
- OpenArchive
website: https://dta.mn/
---
