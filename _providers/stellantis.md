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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 107
  human_in_the_loop: 2
  name: Stellantis Agentic Access
  operation_count: 229
  slug: stellantis-agentic-access
  summary_line: 229 operations · 107 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: Stellantis Connected Vehicle API
  name: Connected Vehicle API
  slug: connected-vehicle-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: Allows to organize the vehicles (of the owner) by group(s) according to functional criteria. Groups allow collective action on a set of vehicles, such as subscription to a monitor or a data stream (*r
  name: Stellantis Grouping API
  slug: stellantis-grouping-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: Describe the data stream feature allowing the publication of defined stream data on the associated output channel
  name: Stellantis Data Stream API
  slug: stellantis-data-stream-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: Authentication endpoint for obtaining and refreshing access tokens.
  name: Stellantis Auth API
  slug: stellantis-auth-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Bugs API from Stellantis — 1 operation(s) for bugs.
  name: Stellantis Bugs API
  slug: stellantis-bugs-api
- baseURL: https://server/api/connectedcar/v1
  baseurl_source: declared
  description: Access to attributes and IoT data associated with the vehicle.
  name: Stellantis Vehicles API
  slug: stellantis-cloud-data-treatment-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Cloud Docg Device Management API from Stellantis — 8 operation(s) for cloud docg device management.
  name: Stellantis Cloud Docg Device Management API
  slug: stellantis-cloud-docg-device-management-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Cloud Notification Center API from Stellantis — 49 operation(s) for cloud notification center.
  name: Stellantis Cloud Notification Center API
  slug: stellantis-cloud-notification-center-api
- baseURL: https://api-cert.groupe-psa.com/connectedcar/v3
  baseurl_source: declared
  description: Access to Vehicles details & onboard capabilities
  name: Stellantis Capabilities API
  slug: stellantis-connected-car-b2b-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Connected Car B2C API from Stellantis — 0 operation(s) for connected car b2c.
  name: Stellantis Connected Car B2C API
  slug: stellantis-connected-car-b2c-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Data API from Stellantis — 2 operation(s) for data.
  name: Stellantis Data API
  slug: stellantis-data-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Feedback API from Stellantis — 1 operation(s) for feedback.
  name: Stellantis Feedback API
  slug: stellantis-feedback-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Geofence Breaches API from Stellantis — 1 operation(s) for geofence breaches.
  name: Stellantis Geofence Breaches API
  slug: stellantis-geofence-breaches-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Geofence Collection API from Stellantis — 6 operation(s) for geofence collection.
  name: Stellantis Geofence Collection API
  slug: stellantis-geofence-collection-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Geofencing Notifications API from Stellantis — 6 operation(s) for geofencing notifications.
  name: Stellantis Geofencing Notifications API
  slug: stellantis-geofencing-notifications-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Hackathon Register API from Stellantis — 1 operation(s) for hackathon register.
  name: Stellantis Hackathon Register API
  slug: stellantis-hackathon-register-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Hackathon Unsubscribe API from Stellantis — 1 operation(s) for hackathon unsubscribe.
  name: Stellantis Hackathon Unsubscribe API
  slug: stellantis-hackathon-unsubscribe-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Popup API from Stellantis — 1 operation(s) for popup.
  name: Stellantis Popup API
  slug: stellantis-popup-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Remote API from Stellantis — 1 operation(s) for remote.
  name: Stellantis Remote API
  slug: stellantis-remote-api
- baseURL: https://api.stellantis-developers.com
  baseurl_source: declared
  description: The Stream API from Stellantis — 2 operation(s) for stream.
  name: Stellantis Stream API
  slug: stellantis-stream-api
artifact_total: 36
common:
- group: design
  href: https://artifacts.apis.io/stellantis/errors/stellantis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stellantis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stellantis/rules/stellantis-rules.yml
  title: ''
  type: Spectral
  url: rules/stellantis-rules.yml
- group: design
  href: https://artifacts.apis.io/stellantis/json-ld/stellantis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stellantis-context.jsonld
- group: design
  href: https://artifacts.apis.io/stellantis/vocabulary/stellantis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stellantis-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/stellantis/conformance/stellantis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stellantis-conformance.yml
- group: other
  href: https://artifacts.apis.io/stellantis/hosts/stellantis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stellantis-hosts.yml
- group: other
  href: https://artifacts.apis.io/stellantis/vendors/stellantis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stellantis-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.stellantis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stellantis
- group: auth
  href: https://artifacts.apis.io/stellantis/security/stellantis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stellantis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stellantis.com
created: '2026-10-13'
description: Stellantis is a global automotive manufacturing corporation formed in 2021 through the merger of Fiat Chrysler Automobiles and PSA Group. It designs, manufactures, and sells a wide range of vehicles under 14 iconic brands, including Abarth, Alfa Romeo, Chrysler, Citroën, Dodge, DS Automobiles, Fiat, Jeep, Lancia, Maserati, Opel, Peugeot, Ram, and Vauxhall. The company focuses on innovative mobility solutions, sustainability, and advanced technology platforms, operating worldwide with a strong presence in Europe, North America, and Latin America. Its corporate website provides extensive information on its strategy, governance, brand portfolio, and sustainability initiatives.
json_schemas:
- name: DataStream
  property_count: 3
  slug: stellantis-data-stream
- name: DataStreamStatusSetter
  property_count: 1
  slug: stellantis-data-stream-status-setter
- name: GroupMaintain
  property_count: 3
  slug: stellantis-group-maintain
- name: GroupObj
  property_count: 2
  slug: stellantis-group-obj
- name: MonitorParameter
  property_count: 4
  slug: stellantis-monitor-parameter
- name: Position
  property_count: 3
  slug: stellantis-position
- name: RemoteCallbackSubscribe
  property_count: 5
  slug: stellantis-remote-callback-subscribe
- name: Remote
  property_count: 10
  slug: stellantis-remote
- name: Status
  property_count: 26
  slug: stellantis-status
- name: Vehicle
  property_count: 9
  slug: stellantis-vehicle
jsonld:
- class_count: 86
  name: Stellantis Context
  property_count: 135
  slug: stellantis-context
layout: provider
modified: '2026-10-13'
name: Stellantis
nav: Providers
network: true
overview: 'Stellantis publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Grouping API, Data Stream API, Auth API, and 17 more. Tagged areas include Company, Automotive, Manufacturing, Mobility, and Sustainability.


  The Stellantis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stellantis'' developer surface includes documentation and 10 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Stellantis API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: stellantis-rules
scopes:
- name: Stellantis Scopes
  scope_count: 53
  slug: stellantis-scopes
  summary_line: 53 scopes · implicit
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.7
    developer_ergonomics: 4.8
    discoverability: 67.9
    operational_transparency: 2.6
  previous_composite: 23.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 4.5
      derived: 3
      marker_coverage: 13.0
      total: 23
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stellantis/stellantis-2026-11-03T143813.png
security:
- kind: authentication
  name: Stellantis Authentication
  slug: stellantis-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Stellantis Domain Security
  slug: stellantis-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: stellantis
tags:
- Company
- Automotive
- Manufacturing
- Mobility
- Sustainability
website: https://www.stellantis.com
---
