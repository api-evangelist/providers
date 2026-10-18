---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Drive API provides comprehensive access to Plugsurfing's charging infrastructure network.
  name: Drive API
  slug: drive-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Handle the ordering and fulfillment process for physical charging keys
  name: Plugsurfing Charging Key Orders API
  slug: plugsurfing-charging-key-orders-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Manage physical and virtual charging keys including creation, activation, updates, and status management. Essential for user access to charging stations.
  name: Plugsurfing Charging Keys API
  slug: plugsurfing-charging-keys-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: The Drive API API from Plugsurfing — 0 operation(s) for drive api.
  name: Plugsurfing Drive API
  slug: plugsurfing-drive-api-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: E-Mobility Provider specific endpoints for managing charging keys
  name: Plugsurfing EMP Charging Keys API
  slug: plugsurfing-emp-charging-keys-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: E-Mobility Provider specific endpoints for managing fleets
  name: Plugsurfing EMP Fleets API
  slug: plugsurfing-emp-fleets-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: E-Mobility Provider specific endpoints for location search and information
  name: Plugsurfing EMP Geosearch API
  slug: plugsurfing-emp-geosearch-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: E-Mobility Provider specific endpoints for managing orders
  name: Plugsurfing EMP Orders API
  slug: plugsurfing-emp-orders-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: E-Mobility Provider specific endpoints for managing charging sessions
  name: Plugsurfing EMP Sessions API
  slug: plugsurfing-emp-sessions-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Search and retrieve detailed information about charging locations and stations
  name: Plugsurfing Geosearch API
  slug: plugsurfing-geosearch-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Manage payment methods and handle transaction processing for charging services
  name: Plugsurfing Payment Options API
  slug: plugsurfing-payment-options-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Control charging sessions remotely including starting and stopping sessions, and monitoring session status
  name: Plugsurfing Remote Charging API
  slug: plugsurfing-remote-charging-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Access and manage charging session data including history, status, and detailed session information
  name: Plugsurfing Sessions API
  slug: plugsurfing-sessions-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Manage user group memberships
  name: Plugsurfing User Groups API
  slug: plugsurfing-user-groups-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Manage user accounts including creation, retrieval, updates, and deletion. Handles user-specific data and preferences.
  name: Plugsurfing Users API
  slug: plugsurfing-users-api
- baseURL: https://{environment}.plugsurfing.com
  baseurl_source: declared
  description: Redeem vouchers
  name: Plugsurfing Vouchers API
  slug: plugsurfing-vouchers-api
artifact_total: 27
asyncapis:
- description: ''
  name: Plugsurfing Webhooks
  slug: plugsurfing-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/rules/plugsurfing-rules.yml
  title: ''
  type: Spectral
  url: rules/plugsurfing-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/json-ld/plugsurfing-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plugsurfing-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/vocabulary/plugsurfing-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plugsurfing-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/conformance/plugsurfing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plugsurfing-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/asyncapi/plugsurfing-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/plugsurfing-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/data-model/plugsurfing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plugsurfing-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/changelog/plugsurfing-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plugsurfing-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/authentication/plugsurfing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plugsurfing-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/errors/plugsurfing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plugsurfing-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/llms/plugsurfing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plugsurfing-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/a2a/plugsurfing-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/plugsurfing-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/well-known/plugsurfing-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/plugsurfing-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/well-known/plugsurfing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plugsurfing-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/hosts/plugsurfing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plugsurfing-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/vendors/plugsurfing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plugsurfing-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plugsurfing.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.plugsurfing.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plugsurfing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plugsurfing/refs/heads/main/security/plugsurfing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plugsurfing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plugsurfing.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plugsurfing.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plugsurfing.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://plugsurfing.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plugsurfing.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.plugsurfing.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://plugsurfing.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plugsurfing.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plugsurfing.com/legal/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developer.plugsurfing.com/mcp
  - status: 401
    url: https://partnersupport.plugsurfing.com/mcp
  - status: 200
    url: https://www.plugsurfing.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Plugsurfing provides a seamless EV charging experience across Europe, offering drivers access to a large network of charging stations through its mobile app and white‑label solutions for businesses. The platform supports roaming via the OCPI 2.2.1 protocol, enabling operators to connect to the Plugsurfing network with real‑time charger data, tariffs, and availability. It also offers APIs for developers to embed charging functionality into apps, in‑car navigation, and other digital services, fostering a more integrated electric mobility ecosystem.
json_schemas:
- name: ChargingKey
  property_count: 11
  slug: plugsurfing-charging-key
- name: EmpChargingKeyOrdersProduct
  property_count: 10
  slug: plugsurfing-emp-charging-key-orders-product
- name: EmpChargingKeyPostRequest
  property_count: 8
  slug: plugsurfing-emp-charging-key-post-request
- name: Location
  property_count: 17
  slug: plugsurfing-location
- name: PrepaidBalance
  property_count: 2
  slug: plugsurfing-prepaid-balance
- name: Session
  property_count: 15
  slug: plugsurfing-session
jsonld:
- class_count: 103
  name: Plugsurfing Context
  property_count: 189
  slug: plugsurfing-context
layout: provider
modified: '2026-10-14'
name: Plugsurfing
nav: Providers
network: true
overview: 'Plugsurfing publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charging Key Orders API, Charging Keys API, Drive API, and 13 more. Tagged areas include Company, EVCharging, Roaming, and Europe.


  The Plugsurfing catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Plugsurfing''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Plugsurfing API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: plugsurfing-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 73.3
    developer_ergonomics: 57.1
    discoverability: 60.7
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Plugsurfing Authentication
  slug: plugsurfing-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Plugsurfing Domain Security
  slug: plugsurfing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plugsurfing
tags:
- Company
- EVCharging
- Roaming
- Europe
website: https://www.plugsurfing.com
---
