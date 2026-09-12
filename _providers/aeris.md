---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-12'
api_count: 28
apis:
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The primary REST API of the Aeris IoT Accelerator platform (acquired from Ericsson in 2023), covering subscription and SIM inventory, subscription search and change history, device and eUICC inventory
  name: Aeris IoT Accelerator REST API
  slug: aeris-iot-accelerator-rest-api
- baseURL: https://sms.iot-api.aeris.com/dcpapi/smsmessaging/v1
  baseurl_source: declared
  description: RESTful SMS messaging API for sending mobile-terminated SMS to devices, retrieving delivery status, and retrieving inbound mobile-originated messages for a registration. The contract states it is base
  name: Aeris IoT Accelerator SMS Messaging API
  slug: aeris-iot-accelerator-sms-messaging-api
- baseURL: https://watchtower-api-prd.aeriscloud.com
  baseurl_source: declared
  description: 'IoT security API for the Aeris IoT Watchtower product: device groups, applications, gateways, flows and activity logs, event configuration and policies, enforcement rules, protection policies, rate li'
  name: Aeris IoT Watchtower API
  slug: aeris-iot-watchtower-api
- description: The legacy SOAP/WSDL service portal API of the IoT Accelerator platform, covering subscription management, trigger and bundle package management, aggregated and subscription traffic, usage data downlo
  name: Aeris IoT Accelerator SOAP API
  slug: aeris-iot-accelerator-soap-api
- description: The Aeris-native SOAP web service used to provision, activate, suspend, cancel, retire and re-provision devices on the Aeris network, change rate plans and service profiles, update device attributes a
  name: Aeris AerAdmin Device Management API
  slug: aeris-aeradmin-device-management-api
- description: 'RESTful SMS and device-control API on the Aeris network: send mobile-terminated SMS, receive delivery notifications, receive and acknowledge mobile-originated SMS, reset network registration, retrieve'
  name: Aeris AerFrame Device Communication and Control API
  slug: aeris-aerframe-device-communication-and-control-api
- description: 'Web service interface for retrieving device traffic and billing data from the Aeris AerTraffic system: create online and scheduled report templates, poll report status, download online, scheduled and '
  name: Aeris AerTraffic Reports API
  slug: aeris-aertraffic-reports-api
artifact_total: 15
asyncapis:
- description: ''
  name: Aeris Stomp Notifications
  slug: aeris-stomp-notifications
common:
- group: company
  title: ''
  type: Website
  url: https://www.aeris.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://iotdeveloper.aeris.net/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://iotdeveloper.aeris.net/hc/en-us/articles/25348533091228-IoT-Accelerator-REST-API
- group: docs
  title: ''
  type: APIReference
  url: https://iotdeveloper.aeris.net/hc/en-us/sections/25346615432988-IoT-Accelerator-APIs
- group: start
  title: ''
  type: GettingStarted
  url: https://iotdeveloper.aeris.net/hc/en-us/articles/25348523998748-API-Quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://support.aeris.net/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.aeris.com/resource-library/?_types=blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeristhings
- group: start
  title: ''
  type: SignUp
  url: https://iot.aeris.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeris.com/legal/services-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeris.com/legal/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://storage.googleapis.com/iota_devportal/assets/dev_app_pmcoll_iota_rest_api.zip
- group: auth
  title: ''
  type: Compliance
  url: https://www.aeris.com/trust-center/aeris-certifications/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aeris-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/aeris-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aeris-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aeris-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aeris-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/aeris-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeris-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aeris-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aeris-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeris-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aeris-stomp-notifications.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-10'
description: Aeris is a cellular IoT connectivity company, founded in 1992 and headquartered in San Jose, California, that operates a global network and connectivity management platform purpose-built for machines rather than phones. Aeris provides SIM and eSIM/eUICC lifecycle management, device provisioning and activation, rate-plan and bundle management, usage and signalling analytics, SMS messaging, and IoT security monitoring to automotive, utilities, logistics, medical-device and industrial customers. In February 2023 Aeris acquired Ericsson's IoT Accelerator and Connected Vehicle Cloud businesses, and the IoT Accelerator platform now runs under the Aeris name and serves the bulk of its published API surface alongside the older Aeris-native AerAdmin, AerFrame and AerTraffic connectivity APIs and the Aeris IoT Watchtower security API.
image: https://www.aeris.com/wp-content/uploads/cropped-Favicon-16x16-1-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Aeris MCP Server
  slug: aeris-mcp-server
modified: '2026-09-10'
name: Aeris
nav: Providers
network: true
overview: 'Aeris publishes 3 APIs on the [APIs.io](https://apis.io/) network: IoT Accelerator REST API, IoT Accelerator SMS Messaging API, and IoT Watchtower API. Tagged areas include IoT, Cellular Connectivity, M2M, eSIM, and SIM Management.


  The Aeris catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aeris'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 19 more developer resources.'
plans:
- name: Aeris Plans Pricing
  plan_count: 0
  slug: aeris-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 44
  name: Aeris Rate Limits
  slug: aeris-rate-limits
scopes:
- name: Aeris Scopes
  scope_count: 71
  slug: aeris-scopes
  summary_line: 71 scopes · password/clientCredentials
score:
  band: strong
  composite: 63.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 70.8
    discoverability: 74.1
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 63.7
  provenance:
    conformance: first-party
    contracts:
      callable: 96.3
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 50.0
security:
- kind: authentication
  name: Aeris Authentication
  slug: aeris-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Aeris Domain Security
  slug: aeris-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aeris Trust Center
  slug: aeris-trust-center
  summary_line: ISO/IEC 27001:2022, ISO 9001:2015, M2M Service Provider Registration
slug: aeris
tags:
- IoT
- Cellular Connectivity
- M2M
- eSIM
- SIM Management
- Telecom
- Device Management
- IoT Security
- Connectivity Management Platform
- SMS Messaging
- eUICC
- Fleet Telematics
website: https://www.aeris.com/
---
