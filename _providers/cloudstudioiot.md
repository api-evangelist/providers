---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cloudstudioiot Agentic Access
  operation_count: 15
  slug: cloudstudioiot-agentic-access
  summary_line: 15 operations · 2 acting
api_count: 1
apis:
- baseURL: https://{host}
  baseurl_source: declared
  description: Create and delete the persistent access tokens the rest of the API uses.
  name: Cloud Studio IoT Access tokens API
  slug: cloudstudioiot-access-tokens-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Alarms recorded by the platform, open and closed.
  name: Cloud Studio IoT Alarms API
  slug: cloudstudioiot-alarms-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Alert definitions (the rules that open alarms).
  name: Cloud Studio IoT Alerts API
  slug: cloudstudioiot-alerts-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Readings reported by endpoints (sensors and actuators).
  name: Cloud Studio IoT Endpoint data API
  slug: cloudstudioiot-endpoint-data-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Geozones of a client and the vehicles inside them.
  name: Cloud Studio IoT Geozones API
  slug: cloudstudioiot-geozones-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Map of clients, facilities, devices and endpoints.
  name: Cloud Studio IoT Instance API
  slug: cloudstudioiot-instance-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/agentic-access/cloudstudioiot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudstudioiot-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/plans/cloudstudioiot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudstudioiot-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/rules/cloudstudioiot-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudstudioiot-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/json-ld/cloudstudioiot-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudstudioiot-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/vocabulary/cloudstudioiot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudstudioiot-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/data-model/cloudstudioiot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudstudioiot-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/errors/cloudstudioiot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudstudioiot-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/conformance/cloudstudioiot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudstudioiot-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/llms/cloudstudioiot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudstudioiot-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/hosts/cloudstudioiot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudstudioiot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/vendors/cloudstudioiot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudstudioiot-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudstudioiot.com/
- group: auth
  title: ''
  type: Security
  url: https://cloudstudioiot.com/hub/topics/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloudstudioiot.com/docs/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/authentication/cloudstudioiot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudstudioiot-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudstudioiot/refs/heads/main/security/cloudstudioiot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudstudioiot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudstudioiot.com
- group: docs
  title: ''
  type: Documentation
  url: https://cloudstudioiot.com/docs/apis-de-extraccion-de-datos
- group: start
  title: ''
  type: GettingStarted
  url: https://cloudstudioiot.com/docs/apis-de-extraccion-de-datos
- group: operate
  title: ''
  type: Support
  url: https://cloudstudioiot.com/contact
- group: company
  title: ''
  type: Blog
  url: https://cloudstudioiot.com/hub
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudStudioIoT
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudstudioiot.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloudstudioiot.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudstudioiot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudstudioiot.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cloudstudioiot/workspace
created: '2026-10-05'
description: Cloud Studio IoT provides an Industrial AI IoT platform delivering end‑to‑end solutions for verticals such as smart cities, energy management, agriculture and manufacturing. Their cloud‑based services include data extraction APIs, AI‑driven analytics, device connectivity (LoRaWAN, MQTT, NB‑IoT) and a low‑code scripting environment. The company emphasizes real‑time telemetry, AI‑powered insights and a comprehensive suite of tools for developers to integrate, monitor and manage IoT deployments.
image: https://cloudstudioiot.com/og?title=Industrial+AI+Software+for+IoT&subtitle=Industrial+AI+software+on+your+IoT+platform%3A+an+AI+Copilot+that+answers+questions+about+your+real-time+telemetry%2C+under+your+own%E2%80%A6
json_schemas:
- name: Alarm
  property_count: 11
  slug: cloudstudioiot-alarm
- name: Alert
  property_count: 16
  slug: cloudstudioiot-alert
- name: ClientAccessToken
  property_count: 6
  slug: cloudstudioiot-client-access-token
- name: CreateAccessTokenRequest
  property_count: 3
  slug: cloudstudioiot-create-access-token-request
- name: EndpointData
  property_count: 11
  slug: cloudstudioiot-endpoint-data
- name: Geozone
  property_count: 8
  slug: cloudstudioiot-geozone
jsonld:
- class_count: 8
  name: Cloudstudioiot Context
  property_count: 49
  slug: cloudstudioiot-context
layout: provider
modified: '2026-10-05'
name: Cloud Studio IoT
nav: Providers
network: true
overview: 'Cloud Studio IoT publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access tokens API, Alarms API, Alerts API, and 3 more. Tagged areas include Company, IoT, Artificial Intelligence, Industrial, and Platform.


  The Cloud Studio IoT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloud Studio IoT''s developer surface includes changelog, authentication, documentation, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Cloudstudioiot Plans Pricing
  plan_count: 2
  slug: cloudstudioiot-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Cloud Studio IoT API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: cloudstudioiot-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 19.7
    contract_quality: 55.3
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudstudioiot Authentication
  slug: cloudstudioiot-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cloudstudioiot Domain Security
  slug: cloudstudioiot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudstudioiot
tags:
- Company
- IoT
- Artificial Intelligence
- Industrial
- Platform
website: https://cloudstudioiot.com
---
