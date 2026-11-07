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
- description: Wallbox developer portal providing API documentation and resources.
  name: Wallbox API
  slug: wallbox-api
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/wallbox/changelog/wallbox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wallbox-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://wallbox.com/.well-known/security-policy.html
- group: auth
  href: https://artifacts.apis.io/wallbox/well-known/wallbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wallbox-security.txt
- group: agent
  href: https://artifacts.apis.io/wallbox/well-known/wallbox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wallbox-well-known.yml
- group: other
  href: https://artifacts.apis.io/wallbox/hosts/wallbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wallbox-hosts.yml
- group: other
  href: https://artifacts.apis.io/wallbox/vendors/wallbox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wallbox-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.wallbox.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.wallbox.com/en/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.wallbox.com/en/release-notes/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wallbox.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wallbox
- group: auth
  href: https://artifacts.apis.io/wallbox/security/wallbox-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wallbox-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/wallbox/security/wallbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wallbox.com
coverage:
  checked: '2026-10-13'
  detail: Developer portals return HTML shells for spec endpoints, no machine-readable OpenAPI found.
  evidence:
  - status: 200
    url: https://developer.wallbox.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Wallbox designs and manufactures smart electric vehicle (EV) charging solutions for homes, businesses, and public spaces. Their platform includes hardware chargers, a mobile app, and energy management services, emphasizing fast, sustainable, and connected charging experiences.
layout: provider
modified: '2026-10-13'
name: Wallbox
nav: Providers
network: true
overview: 'Wallbox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, Smart Hardware, Energy Management, and Software-as-a-Service.


  Wallbox''s developer surface includes changelog, support, documentation, and 11 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 15.8
  previous_composite: 14.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wallbox/wallbox-2026-11-03T145951.png
security:
- kind: domain-security
  name: Wallbox Domain Security
  slug: wallbox-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Wallbox Vulnerability Disclosure
  slug: wallbox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wallbox
tags:
- Company
- EV Charging
- Smart Hardware
- Energy Management
- Software-as-a-Service
website: https://wallbox.com
---
