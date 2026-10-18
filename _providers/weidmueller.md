---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 23
  human_in_the_loop: 5
  name: Weidmueller Agentic Access
  operation_count: 53
  slug: weidmueller-agentic-access
  summary_line: 53 operations · 23 acting · 5 human-in-the-loop
api_count: 4
apis:
- description: A fast asynchronous, event-based NATS API for providing and consuming variables within the u-OS Data Hub; not accessible to clients outside the device (AsyncAPI 2.6.0, 10 channels, NATS server at 127.
  name: Weidmüller u-OS Data Hub Variable-NATS API
  slug: u-os-data-hub-variable-nats-api
- baseURL: /u-os-hub/api/v1
  baseurl_source: spec
  description: A consumer may - list/get available providers - list/get/update variables published by providers.
  name: Weidmüller Consumer API
  slug: weidmueller-consumer-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for firewall settings of u-OS
  name: Weidmüller Firewall API
  slug: weidmueller-firewall-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: Centralized system logging, capture and reporting API for u-OS
  name: Weidmüller Logging API
  slug: weidmueller-logging-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for network settings and state of u-OS
  name: Weidmüller Network API
  slug: weidmueller-network-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for u-OS long running operations
  name: Weidmüller Operations API
  slug: weidmueller-operations-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for checking the availability of u-os-adm
  name: Weidmüller Ping API
  slug: weidmueller-ping-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for u-OS realtime settings
  name: Weidmüller Realtime API
  slug: weidmueller-realtime-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for recovery of u-OS
  name: Weidmüller Recovery API
  slug: weidmueller-recovery-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for u-OS security settings
  name: Weidmüller Security API
  slug: weidmueller-security-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for u-OS serial interface settings
  name: Weidmüller Serial Interfaces API
  slug: weidmueller-serial-interfaces-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for syslog forwarding configuration
  name: Weidmüller Syslog API
  slug: weidmueller-syslog-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for general system informations & actions of u-OS
  name: Weidmüller System API
  slug: weidmueller-system-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for time settings and time state of u-OS
  name: Weidmüller Time API
  slug: weidmueller-time-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for u-OS update settings
  name: Weidmüller Update API
  slug: weidmueller-update-api
- baseURL: /u-os-adm/api/v1
  baseurl_source: spec
  description: API for reading the OpenAPI specification
  name: Weidmüller Open API
  slug: weidmueller-open-api-api
artifact_total: 31
asyncapis:
- description: This document describes all endpoints and payloads of the Variable-NATS-API in the u-OS Data Hub. The endpoints refer to NATS subjects and the payloads are encoded as FlatBuffers binary blobs. For thi
  name: u-os-hub-api
  slug: weidmueller-variable-nats-asyncapi
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/agentic-access/weidmueller-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/weidmueller-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/rules/weidmueller-u-os-hub-api-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/weidmueller-u-os-hub-api-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/rules/weidmueller-rules.yml
  title: ''
  type: Spectral
  url: rules/weidmueller-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/json-ld/weidmueller-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/weidmueller-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/vocabulary/weidmueller-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weidmueller-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/data-model/weidmueller-data-model.yml
  title: ''
  type: DataModel
  url: data-model/weidmueller-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/changelog/weidmueller-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/weidmueller-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/conventions/weidmueller-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weidmueller-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/lifecycle/weidmueller-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/weidmueller-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/lifecycle/weidmueller-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/weidmueller-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/errors/weidmueller-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/weidmueller-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/conformance/weidmueller-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weidmueller-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/overlays/weidmueller-administration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/weidmueller-administration-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/hosts/weidmueller-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weidmueller-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/vendors/weidmueller-vendors.yml
  title: ''
  type: Vendors
  url: vendors/weidmueller-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/packages/weidmueller-packages.yml
  title: ''
  type: SDKs
  url: packages/weidmueller-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/packages/weidmueller-packages.yml
  title: ''
  type: Packages
  url: packages/weidmueller-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/scopes/weidmueller-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/weidmueller-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/authentication/weidmueller-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weidmueller-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/security/weidmueller-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weidmueller-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.weidmueller.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/weidmueller/u-os-hub-api/blob/8bde3db7245954ea6ee1a638d6bd3c939b292efc/tools/spectral/asyncapi-rules.json
- group: docs
  title: ''
  type: Documentation
  url: https://support.weidmueller.com/online-documentation/latest/312416/en-GB/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://support.weidmueller.com/online-documentation/latest/312416/en-GB/142279051.html
- group: operate
  title: ''
  type: Support
  url: https://support.weidmueller.com/support-center/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weidmueller
- group: company
  title: ''
  type: Blog
  url: https://www.weidmueller.com/int/company/press/company_news/index.jsp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weidmueller.com/int/other/privacy_statement.jsp
created: '2026-10-09'
description: 'Weidmüller (Weidmueller Interface GmbH & Co. KG, headquartered in Detmold, Germany) is a provider of smart industrial connectivity and automation: terminal blocks, PCB connectors, electronics, I/O systems, controls and industrial Ethernet. Its u-OS edge operating system for automation devices (UC20 controllers) exposes a Data Hub with documented Variable-HTTP and Variable-NATS APIs, whose OpenAPI and AsyncAPI specifications are published in the weidmueller GitHub organization.'
image: https://avatars.githubusercontent.com/u/45368059?v=4
json_schemas:
- name: ResponseSingleProvider
  property_count: 1
  slug: weidmueller-response-single-provider
- name: ResponseSingleRead
  property_count: 5
  slug: weidmueller-response-single-read
- name: TaskDescription
  property_count: 2
  slug: weidmueller-task-description-v1.schema
- name: Recipe
  property_count: 4
  slug: weidmueller-u-os-lum-recipe-v1.schema
- name: VariableUpdatePostPayload
  property_count: 2
  slug: weidmueller-variable-update-post-payload
jsonld:
- class_count: 120
  name: Weidmueller Context
  property_count: 133
  slug: weidmueller-context
layout: provider
modified: '2026-10-09'
name: Weidmüller
nav: Providers
network: true
overview: 'Weidmüller publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including u-OS Data Hub Variable-NATS API, Consumer API, Firewall API, and 13 more. Tagged areas include Company, Industrial Automation, Industrial Connectivity, Edge Computing, and Industrial IoT.


  The Weidmüller catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Weidmüller''s developer surface includes changelog, authentication, documentation, API reference, support, engineering blog, and 23 more developer resources.'
plans:
- name: Weidmueller Plans Pricing
  plan_count: 0
  slug: weidmueller-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Weidmueller Rate Limits
  slug: weidmueller-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Weidmüller API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 1
  slug: weidmueller-rules
- authorship: provider
  effective_rule_count: 68
  extends:
  - spectral:oas
  - spectral:asyncapi
  - https://unpkg.com/@stoplight/spectral-owasp-ruleset@2.0.1/dist/ruleset.mjs
  name: Weidmüller — u os hub api rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: weidmueller-u-os-hub-api-spectral-rules
scopes:
- name: Weidmueller Scopes
  scope_count: 22
  slug: weidmueller-scopes
  summary_line: 22 scopes · clientCredentials
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.3
    catalog_earned_first_party: 8.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 10.5
    contract_governance: 46.2
    contract_quality: 64.1
    developer_ergonomics: 44.6
    discoverability: 62.5
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/weidmueller/refs/heads/main/screenshots/weidmueller-2026-10-11T194640.png
security:
- kind: authentication
  name: Weidmueller Authentication
  slug: weidmueller-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Weidmueller Domain Security
  slug: weidmueller-domain-security
  summary_line: TLSv1.3 · DMARC
slug: weidmueller
tags:
- Company
- Industrial Automation
- Industrial Connectivity
- Edge Computing
- Industrial IoT
- u-OS
- Manufacturing
website: https://www.weidmueller.com/
---
