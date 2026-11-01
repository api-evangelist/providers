---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Home Connect Agentic Access
  operation_count: 46
  slug: home-connect-agentic-access
  summary_line: 46 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Enumerate your home appliances
  name: Home Connect (BSH appliances) Appliances API
  slug: home-connect-appliances-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Send commands
  name: Home Connect (BSH appliances) Commands API
  slug: home-connect-commands-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Get value changes via SSE
  name: Home Connect (BSH appliances) Events API
  slug: home-connect-events-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Access the camera in the fridge
  name: Home Connect (BSH appliances) Images API
  slug: home-connect-images-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: 'Get information from Cleaning Robot: maps, rooms, zones, robot position, cleaning summaries'
  name: Home Connect (BSH appliances) Map API
  slug: home-connect-map-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Start, select, monitor and stop programs
  name: Home Connect (BSH appliances) Programs API
  slug: home-connect-programs-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Get and set settings
  name: Home Connect (BSH appliances) Settings API
  slug: home-connect-settings-api
- baseURL: https://api.home-connect.com
  baseurl_source: declared
  description: Get status
  name: Home Connect (BSH appliances) Status API
  slug: home-connect-status-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/home-connect/vendors/home-connect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/home-connect-vendors.yml
- group: agent
  href: https://artifacts.apis.io/home-connect/agentic-access/home-connect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/home-connect-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/home-connect/rules/home-connect-rules.yml
  title: ''
  type: Spectral
  url: rules/home-connect-rules.yml
- group: design
  href: https://artifacts.apis.io/home-connect/vocabulary/home-connect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/home-connect-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/home-connect/data-model/home-connect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/home-connect-data-model.yml
- group: design
  href: https://artifacts.apis.io/home-connect/errors/home-connect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/home-connect-problem-types.yml
- group: design
  href: https://artifacts.apis.io/home-connect/conformance/home-connect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/home-connect-conformance.yml
- group: other
  href: https://artifacts.apis.io/home-connect/hosts/home-connect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/home-connect-hosts.yml
- group: build
  href: https://artifacts.apis.io/home-connect/packages/home-connect-packages.yml
  title: ''
  type: SDKs
  url: packages/home-connect-packages.yml
- group: build
  href: https://artifacts.apis.io/home-connect/packages/home-connect-packages.yml
  title: ''
  type: Packages
  url: packages/home-connect-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.home-connect.com/global/service/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.home-connect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.home-connect.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.home-connect.com/general
- group: auth
  href: https://artifacts.apis.io/home-connect/scopes/home-connect-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/home-connect-scopes.yml
- group: auth
  href: https://artifacts.apis.io/home-connect/authentication/home-connect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/home-connect-authentication.yml
- group: auth
  href: https://artifacts.apis.io/home-connect/security/home-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/home-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home-connect.com/
created: '2026-10-28'
description: Home Connect, part of BSH Hausgeräte, offers a platform that connects smart home appliances to users via mobile apps and services. Their website describes a solution that lets you monitor and control appliances such as ovens, dishwashers, and coffee machines from anywhere, providing status updates, remote operation, and integration with smart home ecosystems. The service supports multiple brands under the BSH group and focuses on energy efficiency and convenience for consumers.
layout: provider
modified: '2026-10-28'
name: Home Connect (BSH appliances)
nav: Providers
network: true
overview: 'Home Connect (BSH appliances) publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appliances API, Commands API, Events API, and 5 more. Tagged areas include smart home, appliances, and connected devices.


  The Home Connect (BSH appliances) catalog on APIs.io includes 1 Spectral governance ruleset.


  Home Connect (BSH appliances)''s developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Home Connect (BSH appliances) API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: home-connect-rules
scopes:
- name: Home Connect Scopes
  scope_count: 63
  slug: home-connect-scopes
  summary_line: 63 scopes · authorizationCode
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 45.9
    developer_ergonomics: 45.2
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Home Connect Authentication
  slug: home-connect-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Home Connect Domain Security
  slug: home-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: home-connect
tags:
- smart home
- appliances
- connected devices
website: https://home-connect.com/
---
