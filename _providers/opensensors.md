---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Opensensors Agentic Access
  operation_count: 7
  slug: opensensors-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- description: OpenSensors provides workplace occupancy analytics and scenario modelling via its platform.
  name: OpenSensors API
  slug: opensensors-api
- baseURL: https://api.opensensors.com/
  baseurl_source: declared
  description: A collection of methods used to retrieve sensor data for your project
  name: OpenSensors Analytics API
  slug: opensensors-analytics-api
- baseURL: https://api.opensensors.com/
  baseurl_source: declared
  description: To make request to our API you will need to an API key, which you can get from the "Get Api Key" section in app.opensensors.com. Then use auth/login api to get a refresh token and a token which has ex
  name: OpenSensors Authentication API
  slug: opensensors-authentication-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/opensensors/agentic-access/opensensors-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opensensors-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/opensensors/rules/opensensors-rules.yml
  title: ''
  type: Spectral
  url: rules/opensensors-rules.yml
- group: design
  href: https://artifacts.apis.io/opensensors/vocabulary/opensensors-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opensensors-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/opensensors/data-model/opensensors-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opensensors-data-model.yml
- group: design
  href: https://artifacts.apis.io/opensensors/conformance/opensensors-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opensensors-conformance.yml
- group: agent
  href: https://artifacts.apis.io/opensensors/llms/opensensors-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opensensors-llms.txt
- group: agent
  href: https://artifacts.apis.io/opensensors/well-known/opensensors-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opensensors-well-known.yml
- group: other
  href: https://artifacts.apis.io/opensensors/hosts/opensensors-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opensensors-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opensensors.com/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://opensensors.com/resources/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.opensensors.com/
- group: auth
  href: https://artifacts.apis.io/opensensors/security/opensensors-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opensensors-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opensensors.com/
coverage:
  checked: '2026-10-29'
  detail: OpenSensors publishes human‑readable documentation but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://opensensors.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: OpenSensors delivers workplace occupancy analytics and scenario modelling, helping commercial real‑estate teams cut costs and plan hybrid workplaces with confidence. Their platform provides sensor‑driven data, analytics, and decision‑making tools for space utilization.
image: https://i0.wp.com/opensensors.com/wp-content/uploads/2026/08/Featured-Image-Home.png
layout: provider
modified: '2026-10-29'
name: OpenSensors
nav: Providers
network: true
overview: 'OpenSensors publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, and 1 more. Tagged areas include Company, WorkplaceAnalytics, RealEstateTech, IoT, and DataAnalytics.


  The OpenSensors catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenSensors'' developer surface includes engineering blog, API reference, and 11 more developer resources.'
plans:
- name: Opensensors Plans Pricing
  plan_count: 0
  slug: opensensors-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Opensensors Rate Limits
  slug: opensensors-rate-limits
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: OpenSensors API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: opensensors-rules
scopes:
- name: Opensensors Scopes
  scope_count: 0
  slug: opensensors-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 40.4
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Opensensors Authentication
  slug: opensensors-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Opensensors Domain Security
  slug: opensensors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-booking-reservations
  slug: opensensors-get-booking-reservations
slug: opensensors
tags:
- Company
- WorkplaceAnalytics
- RealEstateTech
- IoT
- DataAnalytics
website: https://opensensors.com/
---
