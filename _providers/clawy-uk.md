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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/clawy-uk/security/clawy-uk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clawy-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clawy-uk/well-known/clawy-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clawy-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/clawy-uk/well-known/clawy-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawy-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawy-uk/hosts/clawy-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawy-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/clawy-uk/vendors/clawy-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clawy-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/clawy-uk/security/clawy-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clawy-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clawy-uk/security/clawy-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawy-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawy.uk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawy.uk/datenschutz.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawy.uk/impressum.html
coverage:
  checked: '2026-11-04'
  detail: No machine‑readable API contract (OpenAPI/GraphQL/AsyncAPI) was discovered despite probing known hosts.
  evidence:
  - status: 405
    url: https://clawy.uk/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Clawy provides AI‑assisted control of Windows, Linux and Android nodes. The Clawy Direct Beta platform connects compatible AI assistants with devices, allowing the master AI to retrieve and translate handheld recordings. It offers a free Node version and paid Memory add‑on, targeting developers and power users seeking seamless AI‑node integration.
layout: provider
modified: '2026-11-03'
name: Clawy
nav: Providers
network: true
overview: Clawy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Node, and Beta.
random_paper: 21
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawy Uk Domain Security
  slug: clawy-uk-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Clawy Uk Vulnerability Disclosure
  slug: clawy-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clawy-uk
tags:
- Company
- Artificial Intelligence
- Automation
- Node
- Beta
- Control
website: https://clawy.uk/
---
