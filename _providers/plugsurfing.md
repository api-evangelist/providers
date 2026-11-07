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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 3
  name: Plugsurfing Agentic Access
  operation_count: 59
  slug: plugsurfing-agentic-access
  summary_line: 59 operations · 29 acting · 3 human-in-the-loop
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
artifact_total: 28
asyncapis:
- description: ''
  name: Plugsurfing Webhooks
  slug: plugsurfing-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/plugsurfing/agentic-access/plugsurfing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plugsurfing-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/plugsurfing/well-known/plugsurfing-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/plugsurfing-status-security.txt
- group: design
  href: https://artifacts.apis.io/plugsurfing/rules/plugsurfing-rules.yml
  title: ''
  type: Spectral
  url: rules/plugsurfing-rules.yml
- group: design
  href: https://artifacts.apis.io/plugsurfing/json-ld/plugsurfing-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plugsurfing-context.jsonld
- group: design
  href: https://artifacts.apis.io/plugsurfing/vocabulary/plugsurfing-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plugsurfing-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/plugsurfing/conformance/plugsurfing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plugsurfing-conformance.yml
- group: design
  href: https://artifacts.apis.io/plugsurfing/asyncapi/plugsurfing-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/plugsurfing-webhooks.yml
- group: design
  href: https://artifacts.apis.io/plugsurfing/data-model/plugsurfing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plugsurfing-data-model.yml
- group: operate
  href: https://artifacts.apis.io/plugsurfing/changelog/plugsurfing-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plugsurfing-changelog.yml
- group: auth
  href: https://artifacts.apis.io/plugsurfing/authentication/plugsurfing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plugsurfing-authentication.yml
- group: design
  href: https://artifacts.apis.io/plugsurfing/errors/plugsurfing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plugsurfing-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/plugsurfing/llms/plugsurfing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plugsurfing-llms.txt
- group: other
  href: https://artifacts.apis.io/plugsurfing/a2a/plugsurfing-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/plugsurfing-a2a.yml
- group: agent
  href: https://artifacts.apis.io/plugsurfing/well-known/plugsurfing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plugsurfing-well-known.yml
- group: other
  href: https://artifacts.apis.io/plugsurfing/hosts/plugsurfing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plugsurfing-hosts.yml
- group: other
  href: https://artifacts.apis.io/plugsurfing/vendors/plugsurfing-vendors.yml
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
  href: https://artifacts.apis.io/plugsurfing/security/plugsurfing-domain-security.yml
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
overview: 'Plugsurfing publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Charging Key Orders API, Charging Keys API, Drive API, and 13 more. Tagged areas include Company, EV Charging, Roaming, and Europe.


  The Plugsurfing catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Plugsurfing''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Plugsurfing API Rules
  rule_count: 63
  severity_counts:
    error: 45
    hint: 0
    info: 5
    warn: 13
  slug: plugsurfing-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 74.6
    developer_ergonomics: 34.5
    discoverability: 60.7
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/plugsurfing/plugsurfing-2026-11-03T141319.png
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
- EV Charging
- Roaming
- Europe
website: https://www.plugsurfing.com
---
