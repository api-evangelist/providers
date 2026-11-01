---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Freighthub Com Agentic Access
  operation_count: 25
  slug: freighthub-com-agentic-access
  summary_line: 25 operations · 9 acting
api_count: 1
apis:
- baseURL: https://public-api.forto.io
  baseurl_source: spec
  description: The Booking Request API from Forto — 5 operation(s) for booking request.
  name: Forto Booking Request API
  slug: freighthub-com-booking-request-api
- baseURL: https://public-api.forto.io
  baseurl_source: spec
  description: The Reports API from Forto — 1 operation(s) for reports.
  name: Forto Reports API
  slug: freighthub-com-reports-api
- baseURL: https://public-api.forto.io
  baseurl_source: spec
  description: The Shipment API from Forto — 11 operation(s) for shipment.
  name: Forto Shipment API
  slug: freighthub-com-shipment-api
- baseURL: https://public-api.forto.io
  baseurl_source: spec
  description: The Subscriptions API from Forto — 3 operation(s) for subscriptions.
  name: Forto Subscriptions API
  slug: freighthub-com-subscriptions-api
- baseURL: https://public-api.forto.io
  baseurl_source: spec
  description: The Tokens API from Forto — 2 operation(s) for tokens.
  name: Forto Tokens API
  slug: freighthub-com-tokens-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/freighthub-com/agentic-access/freighthub-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freighthub-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/rules/freighthub-com-rules.yml
  title: ''
  type: Spectral
  url: rules/freighthub-com-rules.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/json-ld/freighthub-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/freighthub-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/freighthub-com/vocabulary/freighthub-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/freighthub-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/freighthub-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/data-model/freighthub-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/freighthub-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/conventions/freighthub-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/freighthub-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/freighthub-com/security/freighthub-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/freighthub-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/freighthub-com/authentication/freighthub-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/freighthub-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/errors/freighthub-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/freighthub-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/freighthub-com/conformance/freighthub-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/freighthub-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/freighthub-com/llms/freighthub-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/freighthub-com-llms.txt
- group: other
  href: https://artifacts.apis.io/freighthub-com/hosts/freighthub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freighthub-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/freighthub-com/vendors/freighthub-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/freighthub-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://forto.com/en/privacy-notice/
- group: start
  title: ''
  type: GettingStarted
  url: https://forto.com/en/get-started/
- group: company
  title: ''
  type: Blog
  url: https://forto.com/en/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.forto.com/
- group: auth
  href: https://artifacts.apis.io/freighthub-com/security/freighthub-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/freighthub-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/freighthub-com/security/freighthub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freighthub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://freighthub.com
coverage:
  checked: '2026-10-23'
  detail: Developer portal at https://developers.forto.com returns errors and appears to be JavaScript‑rendered without a static OpenAPI spec.
  evidence:
  - status: error
    url: https://developers.forto.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Forto provides global B2B transportation services, offering sea freight (full container load and less than container load), air freight, rail freight, and additional logistics services. It operates a digital platform that gives customers visibility and management tools for shipments, supported by AI‑powered operations and sustainability options such as biofuel transport and emissions visibility. The company serves businesses in over 100 countries through a network of offices and partners.
jsonld:
- class_count: 67
  name: Freighthub Com Context
  property_count: 246
  slug: freighthub-com-context
layout: provider
modified: '2026-10-22'
name: Forto
nav: Providers
network: true
overview: 'Forto publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Booking Request API, Reports API, Shipment API, and 2 more. Tagged areas include Sea Freight, Air Freight, Rail Freight, Logistics, and Sustainability.


  The Forto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Forto''s developer surface includes authentication, getting-started guide, engineering blog, documentation, and 17 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Forto API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 2
  slug: freighthub-com-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 37.5
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Freighthub Com Authentication
  slug: freighthub-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Freighthub Com Domain Security
  slug: freighthub-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Freighthub Com Vulnerability Disclosure
  slug: freighthub-com-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: freighthub-com-booking-request-flow
  slug: freighthub-com-booking-request-flow
- name: freighthub-com-manage-subscriptions
  slug: freighthub-com-manage-subscriptions
- name: freighthub-com-manage-tokens
  slug: freighthub-com-manage-tokens
- name: freighthub-com-retrieve-shipment-transport-plan
  slug: freighthub-com-retrieve-shipment-transport-plan
slug: freighthub-com
tags:
- Sea Freight
- Air Freight
- Rail Freight
- Logistics
- Sustainability
- AI
- Platform
website: http://freighthub.com
---
