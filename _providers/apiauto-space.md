---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read-only REST API aggregating used‑car listings from Korea, China, and US markets.
  name: apiauto.space API
  slug: apiauto-space-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/apiauto-space/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/apiauto-space/changelog/apiauto-space-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apiauto-space-changelog.yml
- group: design
  href: https://artifacts.apis.io/apiauto-space/conventions/apiauto-space-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiauto-space-conventions.yml
- group: auth
  href: https://artifacts.apis.io/apiauto-space/authentication/apiauto-space-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiauto-space-authentication.yml
- group: design
  href: https://artifacts.apis.io/apiauto-space/conformance/apiauto-space-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiauto-space-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiauto-space/llms/apiauto-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiauto-space-llms.txt
- group: other
  href: https://artifacts.apis.io/apiauto-space/hosts/apiauto-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiauto-space-hosts.yml
- group: build
  href: https://artifacts.apis.io/apiauto-space/packages/apiauto-space-packages.yml
  title: ''
  type: SDKs
  url: packages/apiauto-space-packages.yml
- group: build
  href: https://artifacts.apis.io/apiauto-space/packages/apiauto-space-packages.yml
  title: ''
  type: Packages
  url: packages/apiauto-space-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiauto.space/en/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiauto-space
- group: operate
  title: ''
  type: ChangeLog
  url: https://apiauto.space/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://apiauto.space/en/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.apiauto.space/docs/redoc
- group: auth
  href: https://artifacts.apis.io/apiauto-space/security/apiauto-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiauto-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiauto.space/en/
- group: docs
  title: ''
  type: Documentation
  url: https://apiauto.space/en/docs/
created: '2026-11-05'
description: 'Apiauto Space provides a unified REST API aggregating used‑car listings from three major markets: Korea (Encar), China (Che168), and the United States (Copart and IAAI). The service consolidates data such as vehicle details, photos, pricing, and availability into a single JSON format, enabling importers, dealers, price trackers, and Telegram bots to access comprehensive car catalogs without building individual scrapers. A demo API key offers 100 free requests per day, and the platform updates listings hourly, ensuring fresh market data for automotive businesses and developers.'
image: https://apiauto.space/og/home-en.jpg
layout: provider
modified: '2026-11-05'
name: Apiauto Space
nav: Providers
network: true
overview: 'Apiauto Space is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Used Cars, Car Importers, Dealers, Price Trackers, and Auctions.


  Apiauto Space''s developer surface includes changelog, authentication, getting-started guide, API reference, documentation, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.0
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiauto Space Authentication
  slug: apiauto-space-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apiauto Space Domain Security
  slug: apiauto-space-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-cars
  slug: apiauto-space-list-cars
slug: apiauto-space
tags:
- Used Cars
- Car Importers
- Dealers
- Price Trackers
- Auctions
website: https://apiauto.space/en/
---
