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
api_count: 1
apis:
- description: Developer portal for SEKO Logistics offering API documentation and integration guides.
  name: SEKO Logistics Developer API
  slug: seko-logistics-developer-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/seko-logistics/vendors/seko-logistics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seko-logistics-vendors.yml
- group: other
  href: https://artifacts.apis.io/seko-logistics/hosts/seko-logistics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seko-logistics-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sekologistics.com/en/resources/terms-and-conditions-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sekologistics.com/en/privacy-center/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sekologistics.com/en/resource-hub/news/?tag=9758
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sekologistics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sekologistics
- group: auth
  href: https://artifacts.apis.io/seko-logistics/security/seko-logistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seko-logistics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sekologistics.com/
coverage:
  checked: '2026-10-28'
  detail: Developer portal pages are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://developer.sekologistics.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: SEKO Logistics is a global logistics provider offering freight forwarding, customs clearance, warehousing, and last‑mile delivery services. It serves customers worldwide across multiple regions, providing integrated supply‑chain solutions, e‑commerce fulfillment, and specialized logistics for industries such as healthcare and technology. The company emphasizes technology‑driven visibility, sustainability, and compliance with international trade regulations.
image: https://www.sekologistics.com/media/pejh2vx2/seko-social-share-logo.png?width=1200&height=630&v=1db0eb01f58ae20
layout: provider
modified: '2026-10-28'
name: SEKO Logistics
nav: Providers
network: true
overview: 'SEKO Logistics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, SupplyChain, and ECommerce.


  SEKO Logistics'' developer surface includes documentation and 8 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seko Logistics Domain Security
  slug: seko-logistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seko-logistics
tags:
- Company
- Logistics
- Freight
- SupplyChain
- ECommerce
website: https://www.sekologistics.com/
---
