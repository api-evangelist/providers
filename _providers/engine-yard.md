---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.engineyard.com
  baseurl_source: declared
  description: 'Engine Yard API as documented publicly: 45 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Engine Yard API
  slug: engine-yard-api
artifact_total: 11
common:
- group: operate
  title: ''
  type: Support
  url: https://support.engineyard.com
- group: commercial
  href: https://artifacts.apis.io/engine-yard/plans/engine-yard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/engine-yard-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/engine-yard/rules/engine-yard-rules.yml
  title: ''
  type: Spectral
  url: rules/engine-yard-rules.yml
- group: design
  href: https://artifacts.apis.io/engine-yard/json-ld/engine-yard-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/engine-yard-context.jsonld
- group: design
  href: https://artifacts.apis.io/engine-yard/vocabulary/engine-yard-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/engine-yard-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/engine-yard/data-model/engine-yard-data-model.yml
  title: ''
  type: DataModel
  url: data-model/engine-yard-data-model.yml
- group: design
  href: https://artifacts.apis.io/engine-yard/conformance/engine-yard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/engine-yard-conformance.yml
- group: auth
  href: https://artifacts.apis.io/engine-yard/well-known/engine-yard-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/engine-yard-status-security.txt
- group: agent
  href: https://artifacts.apis.io/engine-yard/well-known/engine-yard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/engine-yard-well-known.yml
- group: other
  href: https://artifacts.apis.io/engine-yard/hosts/engine-yard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/engine-yard-hosts.yml
- group: other
  href: https://artifacts.apis.io/engine-yard/vendors/engine-yard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/engine-yard-vendors.yml
- group: build
  href: https://artifacts.apis.io/engine-yard/packages/engine-yard-packages.yml
  title: ''
  type: SDKs
  url: packages/engine-yard-packages.yml
- group: build
  href: https://artifacts.apis.io/engine-yard/packages/engine-yard-packages.yml
  title: ''
  type: Packages
  url: packages/engine-yard-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.engineyard.com/policies/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.engineyard.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.engineyard.com/policies/privacy/
- group: start
  title: ''
  type: Login
  url: https://login.engineyard.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://developer.engineyard.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/engineyard
- group: auth
  href: https://artifacts.apis.io/engine-yard/security/engine-yard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/engine-yard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.engineyard.com
- group: company
  title: ''
  type: Blog
  url: https://www.engineyard.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.engineyard.com/pricing/
coverage:
  checked: '2026-10-26'
  detail: The developer pages return only HTML with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.engineyard.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Engine Yard provides a managed Ruby on Rails hosting platform, offering a PaaS solution that simplifies deployment, scaling, and management of web applications. Founded in 2006, the company focuses on delivering reliable, secure, and performant infrastructure for developers, with features like automated backups, monitoring, and support for multiple environments. Engine Yard serves enterprises and startups seeking to accelerate their application delivery while reducing operational overhead.
image: https://www.engineyard.com/wp-content/uploads/2021/10/homepage.jpg
json_schemas:
- name: GetAlertsAlertResponse
  property_count: 16
  slug: engine-yard-get-alerts-alert-response
- name: GetNetworksNetworkResponse
  property_count: 8
  slug: engine-yard-get-networks-network-response
- name: PostDatabaseServersDatabaseserveridAlertsRequest
  property_count: 5
  slug: engine-yard-post-database-servers-databaseserverid-alerts-request
- name: PostDatabaseServersDatabaseserveridAlertsResponse
  property_count: 16
  slug: engine-yard-post-database-servers-databaseserverid-alerts-response
- name: PostServersServeridAlertsResponse
  property_count: 16
  slug: engine-yard-post-servers-serverid-alerts-response
- name: PutAlertsAlertidResponse
  property_count: 16
  slug: engine-yard-put-alerts-alertid-response
jsonld:
- class_count: 53
  name: Engine Yard Context
  property_count: 63
  slug: engine-yard-context
layout: provider
modified: '2026-10-26'
name: Engine Yard
nav: Providers
network: true
overview: 'Engine Yard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PaaS, Ruby, Rails, and CloudHosting.


  The Engine Yard catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Engine Yard''s developer surface includes support, documentation, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Engine Yard Plans Pricing
  plan_count: 3
  slug: engine-yard-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Engine Yard API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: engine-yard-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Engine Yard Domain Security
  slug: engine-yard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: engine-yard
tags:
- Company
- PaaS
- Ruby
- Rails
- CloudHosting
website: https://www.engineyard.com
---
