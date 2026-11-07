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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/bydleno-cz/security/bydleno-cz-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bydleno-cz-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bydleno-cz/llms/bydleno-cz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bydleno-cz-llms.txt
- group: auth
  href: https://artifacts.apis.io/bydleno-cz/well-known/bydleno-cz-za-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bydleno-cz-za-security.txt
- group: auth
  href: https://artifacts.apis.io/bydleno-cz/well-known/bydleno-cz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bydleno-cz-security.txt
- group: agent
  href: https://artifacts.apis.io/bydleno-cz/well-known/bydleno-cz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bydleno-cz-well-known.yml
- group: other
  href: https://artifacts.apis.io/bydleno-cz/hosts/bydleno-cz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bydleno-cz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bydleno-cz/security/bydleno-cz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bydleno-cz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bydleno-cz/security/bydleno-cz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bydleno-cz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bydleno.cz/
coverage:
  checked: '2026-11-03'
  detail: Provider's API reference pages return 404 and no machine‑readable spec was found.
  evidence:
  - status: 404
    url: https://bydleno.cz/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: SBíráme pronájmy bytů z českých realitních portálů na jedno místo. Stejné nabídky z různých portálů spojujeme do jedné a přidáváme k nim hodnocení bytu a okolí. Všechno zdarma a bez reklam.
image: https://static.bydleno.cz/images/public/bydleno.png
layout: provider
modified: '2026-11-03'
name: BDLN Data s.r.o.
nav: Providers
network: true
overview: BDLN Data s.r.o. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Rentals, Czech Republic, and Data Aggregation.
random_paper: 7
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 30.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Bydleno Cz Domain Security
  slug: bydleno-cz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bydleno Cz Vulnerability Disclosure
  slug: bydleno-cz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bydleno-cz
tags:
- Real Estate
- Rentals
- Czech Republic
- Data Aggregation
website: https://bydleno.cz/
---
