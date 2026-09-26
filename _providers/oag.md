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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: Access flight schedules and status per individual flight, including on-time performance indicators and diversion and recovery flight information.
  name: Flight Info API
  slug: flight-info-api
- baseURL: https://api.oag.com
  baseurl_source: declared
  description: 'OAG API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-09-23); not the provider''s own document.'
  name: OAG API
  slug: oag-api
artifact_total: 11
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oag.com/legal-notices
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/rules/oag-rules.yml
  title: ''
  type: Spectral
  url: rules/oag-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/json-ld/oag-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oag-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/vocabulary/oag-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/oag-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/data-model/oag-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oag-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/changelog/oag-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oag-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/conformance/oag-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oag-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/llms/oag-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oag-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/hosts/oag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oag-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/vendors/oag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oag-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oag/refs/heads/main/security/oag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oag.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.oag.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.oag.com/flight-info-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.oag.com/flight-info-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.oag.com/flight-info-api
- group: operate
  title: ''
  type: Support
  url: https://www.oag.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.oag.com/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oag.com/privacy-notice
coverage:
  checked: 2026-09-23
  detail: Developer portal pages are rendered with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.oag.com/apis/flight-info-v2
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: OAG provides comprehensive aviation data and analytics, delivering real‑time flight schedules, status, fares, historical records, and passenger booking information. Their platform powers airlines, airports, travel tech, and finance firms with APIs that enable data‑driven decisions across the global travel ecosystem.
image: https://www.oag.com/hubfs/Podcast/2022%20Featured%20Images/OAG_Podcast%20%287%29.jpg
json_schemas:
- name: GetDeparturedateScheduleinstancekeyResponse
  property_count: 30
  slug: oag-get-departuredate-scheduleinstancekey-response
- name: GetFlightInstancesDeparturedateScheduleinstancekeyResponse
  property_count: 30
  slug: oag-get-flight-instances-departuredate-scheduleinstancekey-response
- name: PatchAlertsRequest
  property_count: 29
  slug: oag-patch-alerts-request
- name: PatchFlightInfoAlertsAlertsRequest
  property_count: 29
  slug: oag-patch-flight-info-alerts-alerts-request
- name: PostAlertsRequest
  property_count: 22
  slug: oag-post-alerts-request
- name: PostFlightInfoAlertsFlightinfoalertidRequest
  property_count: 22
  slug: oag-post-flight-info-alerts-flightinfoalertid-request
jsonld:
- class_count: 25
  name: Oag Context
  property_count: 72
  slug: oag-context
layout: provider
modified: '2026-09-23'
name: OAG
nav: Providers
network: true
overview: 'OAG publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Data, Analytics, and Travel.


  The OAG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OAG''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, and 13 more developer resources.'
random_paper: 3
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: OAG API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: oag-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.6
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 29.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oag Domain Security
  slug: oag-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: oag
tags:
- Company
- Aviation
- Data
- Analytics
- Travel
website: https://www.oag.com/
---
