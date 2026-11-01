---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/testmart/hosts/testmart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/testmart-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.testmart.com/terms-of-use.cfm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.testmart.com/privacy.cfm
- group: auth
  href: https://artifacts.apis.io/testmart/security/testmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/testmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.testmart.com
coverage:
  checked: '2026-10-23'
  detail: The provider's website offers product listings but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.testmart.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: TestMart is a leading government procurement platform specializing in test and measurement equipment. It connects agencies with a wide range of products such as cable and antenna analyzers, digital multimeters, oscilloscopes, and signal generators. The site offers detailed product listings, pricing, and support contacts, serving as a comprehensive resource for public sector buyers seeking reliable testing tools.
layout: provider
modified: '2026-10-22'
name: TestMart
nav: Providers
network: true
overview: TestMart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Procurement, TestEquipment, and Marketplace.
random_paper: 20
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Testmart Domain Security
  slug: testmart-domain-security
  summary_line: TLSv1.2 · DMARC
slug: testmart
tags:
- Company
- Government
- Procurement
- TestEquipment
- Marketplace
website: https://www.testmart.com
---
