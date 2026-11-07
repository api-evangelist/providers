---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/dokumendiregister-ee/security/dokumendiregister-ee-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dokumendiregister-ee-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dokumendiregister-ee/llms/dokumendiregister-ee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokumendiregister-ee-llms.txt
- group: auth
  href: https://artifacts.apis.io/dokumendiregister-ee/well-known/dokumendiregister-ee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dokumendiregister-ee-security.txt
- group: agent
  href: https://artifacts.apis.io/dokumendiregister-ee/well-known/dokumendiregister-ee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokumendiregister-ee-well-known.yml
- group: other
  href: https://artifacts.apis.io/dokumendiregister-ee/hosts/dokumendiregister-ee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dokumendiregister-ee-hosts.yml
- group: other
  href: https://artifacts.apis.io/dokumendiregister-ee/vendors/dokumendiregister-ee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dokumendiregister-ee-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dokumendiregister-ee/security/dokumendiregister-ee-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dokumendiregister-ee-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dokumendiregister-ee/security/dokumendiregister-ee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokumendiregister-ee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokumendiregister.ee/
coverage:
  checked: '2026-11-05'
  detail: No public API contract was found; attempts to fetch common OpenAPI URLs returned HTML pages.
  evidence:
  - status: 200
    url: https://dokumendiregister.ee/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-05'
description: Dokumendi Register provides a free public search service for Estonian public institution document registers, including letters, orders, contracts, and information requests. Users can search across all registered entities without registration, offering transparent access to governmental documents.
image: https://dokumendiregister.ee/api/dokreg-og?title=Eesti+asutuste+dokumendiregistrid&sub=Tasuta+otsing%2C+seotud+ettev%C3%B5tetega&eyebrow=Dokumendiregister
layout: provider
modified: '2026-11-05'
name: Dokumendi Register
nav: Providers
network: true
overview: Dokumendi Register is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Estonia, Public Data, Search, and Free.
random_paper: 12
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dokumendiregister Ee Domain Security
  slug: dokumendiregister-ee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Dokumendiregister Ee Vulnerability Disclosure
  slug: dokumendiregister-ee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dokumendiregister-ee
tags:
- Government
- Estonia
- Public Data
- Search
- Free
website: https://dokumendiregister.ee/
---
