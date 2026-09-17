---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-09-16'
api_count: 34
apis:
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
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Get triggered actions filtered list, details and summary
  name: Aeris Actions API
  slug: aeris-actions-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Consumer and IoT profile activation code management
  name: Aeris Activation codes API
  slug: aeris-activation-codes-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Activities API from Aeris — 2 operation(s) for activities.
  name: Aeris Activities API
  slug: aeris-activities-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Activity Logs
  name: Aeris Activity Logs API
  slug: aeris-activity-logs-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Aggregated traffics API from Aeris — 1 operation(s) for aggregated traffics.
  name: Aeris Aggregated traffics API
  slug: aeris-aggregated-traffics-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Enforcement Applications
  name: Aeris Applications API
  slug: aeris-applications-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Attachments API from Aeris — 4 operation(s) for attachments.
  name: Aeris Attachments API
  slug: aeris-attachments-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for authentication and authorization.
  name: Aeris Auth API
  slug: aeris-auth-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Cell Global Identities API from Aeris — 1 operation(s) for cell global identities.
  name: Aeris Cell Global Identities API
  slug: aeris-cell-global-identities-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Data balances API from Aeris — 1 operation(s) for data balances.
  name: Aeris Data balances API
  slug: aeris-data-balances-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Device API
  name: Aeris Device API
  slug: aeris-device-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Device Groups
  name: Aeris Device Groups API
  slug: aeris-device-groups-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Device Reconnect API from Aeris — 1 operation(s) for device reconnect.
  name: Aeris Device Reconnect API
  slug: aeris-device-reconnect-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: 'Endpoints for Devices (IMEI changes) and per-device deep forensics analytics: Data Transactions, Data Volume, DNS Queries, Destination Endpoints, IP Flow Metrics.'
  name: Aeris Devices API
  slug: aeris-devices-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: eCO eIM order operations and job status
  name: Aeris Eim Eco Operation API
  slug: aeris-eimecooperation-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: eIM information
  name: Aeris Eim Info API
  slug: aeris-eiminfo-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Enforcement Rules
  name: Aeris Enforcement Rules API
  slug: aeris-enforcement-rules-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Enterprise API from Aeris — 6 operation(s) for enterprise.
  name: Aeris Enterprise API
  slug: aeris-enterprise-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The EnterpriseGroup API from Aeris — 1 operation(s) for enterprisegroup.
  name: Aeris Enterprise Group API
  slug: aeris-enterprisegroup-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: eUICC Agreement
  name: Aeris Euicc Agreement API
  slug: aeris-euiccagreement-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Awareness Event Policies
  name: Aeris Event Policies API
  slug: aeris-event-policies-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Signalling events for subscriptions.
  name: Aeris Events API
  slug: aeris-events-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for configuring Security Events
  name: Aeris Events Configuration API
  slug: aeris-events-configuration-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: File Shares APIs are for user to get necessary file share info for creating or modifying a specification
  name: Aeris File Shares API
  slug: aeris-file-shares-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for flows - IP flows/Blocked flows/Allowed traffic
  name: Aeris Flows API
  slug: aeris-flows-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Watchtower Configuration APIs for Gateway management
  name: Aeris Gateway API
  slug: aeris-gateway-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: IMSI Range API
  name: Aeris Imsi Range API
  slug: aeris-imsirange-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Incidents API from Aeris — 5 operation(s) for incidents.
  name: Aeris Incidents API
  slug: aeris-incidents-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Invoices API from Aeris — 2 operation(s) for invoices.
  name: Aeris Invoices API
  slug: aeris-invoices-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Locale
  name: Aeris Locale API
  slug: aeris-locale-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Localization API from Aeris — 19 operation(s) for localization.
  name: Aeris Localization API
  slug: aeris-localization-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Localization table
  name: Aeris Localization Table API
  slug: aeris-localizationtable-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Location Lists
  name: Aeris Location Lists API
  slug: aeris-location-lists-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Login API from Aeris — 3 operation(s) for login.
  name: Aeris Login API
  slug: aeris-login-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Manage rulesets and its life-cycle status
  name: Aeris Management API
  slug: aeris-management-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Monitoring API from Aeris — 1 operation(s) for monitoring.
  name: Aeris Monitoring API
  slug: aeris-monitoring-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: MSISDN Pool API
  name: Aeris Msisdn Pool API
  slug: aeris-msisdnpool-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: MSISDN Range API
  name: Aeris Msisdn Range API
  slug: aeris-msisdnrange-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Network group API from Aeris — 1 operation(s) for network group.
  name: Aeris Network group API
  slug: aeris-network-group-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Number scheme API
  name: Aeris Number Scheme API
  slug: aeris-numberscheme-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Operator network nodes API from Aeris — 1 operation(s) for operator network nodes.
  name: Aeris Operator network nodes API
  slug: aeris-operator-network-nodes-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Operator networks API from Aeris — 1 operation(s) for operator networks.
  name: Aeris Operator networks API
  slug: aeris-operator-networks-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Order API from Aeris — 11 operation(s) for order.
  name: Aeris Order API
  slug: aeris-order-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Order management APIs.
  name: Aeris Order management API
  slug: aeris-order-management-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Organization Signaling Aggregations APIs.
  name: Aeris Organization Signaling Reports API
  slug: aeris-organization-signaling-reports-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Products API from Aeris — 4 operation(s) for products.
  name: Aeris Products API
  slug: aeris-products-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Enforcement Protection Policies
  name: Aeris Protection Policies API
  slug: aeris-protection-policies-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Purchases API from Aeris — 5 operation(s) for purchases.
  name: Aeris Purchases API
  slug: aeris-purchases-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The querySMS API from Aeris — 1 operation(s) for querysms.
  name: Aeris Query SMS API
  slug: aeris-querysms-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Rate Limiters
  name: Aeris Rate Limiters API
  slug: aeris-rate-limiters-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Recurring purchases API from Aeris — 4 operation(s) for recurring purchases.
  name: Aeris Recurring purchases API
  slug: aeris-recurring-purchases-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Reports API from Aeris — 4 operation(s) for reports.
  name: Aeris Reports API
  slug: aeris-reports-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Requests API from Aeris — 2 operation(s) for requests.
  name: Aeris Requests API
  slug: aeris-requests-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Inventory queries for network resources
  name: Aeris Resource Inventory API
  slug: aeris-resource-inventory-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The retrieveSMS API from Aeris — 1 operation(s) for retrievesms.
  name: Aeris Retrieve SMS API
  slug: aeris-retrievesms-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for downloading Scheduled Reports
  name: Aeris Scheduled Reports API
  slug: aeris-scheduled-reports-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoints for Security Reports
  name: Aeris Security Report API
  slug: aeris-security-report-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The SIM specification API from Aeris — 1 operation(s) for sim specification.
  name: Aeris SIM specification API
  slug: aeris-sim-specification-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Specification Management APIs are for user to get specifications info
  name: Aeris Specifications API
  slug: aeris-specifications-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: 'Custom fields are user-defined key-value pairs. They can be used for advanced filtering capabilities on single subscriptions as well as batch jobs. Custom fields can be created, modified and attached '
  name: Aeris Subscription Custom Fields API
  slug: aeris-subscription-custom-fields-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Subscription management - additional functions API from Aeris — 12 operation(s) for subscription management - additional functions.
  name: Aeris Subscription management - additional functions API
  slug: aeris-subscription-management-additional-functions-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Subscription Search API API from Aeris — 1 operation(s) for subscription search api.
  name: Aeris Subscription Search API
  slug: aeris-subscription-search-api-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The SubscriptionInventory API from Aeris — 12 operation(s) for subscriptioninventory .
  name: Aeris Subscription Inventory API
  slug: aeris-subscriptioninventory-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Subscriptions API from Aeris — 2 operation(s) for subscriptions.
  name: Aeris Subscriptions API
  slug: aeris-subscriptions-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The TAC Codes API from Aeris — 2 operation(s) for tac codes.
  name: Aeris TAC Codes API
  slug: aeris-tac-codes-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: Endpoint to Acquire and Revoke Token
  name: Aeris Token API
  slug: aeris-token-api
- baseURL: https://iot-api.aeris.com
  baseurl_source: declared
  description: The Usages API from Aeris — 2 operation(s) for usages.
  name: Aeris Usages API
  slug: aeris-usages-api
- baseURL: https://iot-api.aeris.net
  baseurl_source: declared
  description: The Send SMS API from Aeris — 1 operation(s) for send sms.
  name: Aeris Send SMS API
  slug: aeris-send-sms-api
artifact_total: 80
asyncapis:
- description: ''
  name: Aeris Stomp Notifications
  slug: aeris-stomp-notifications
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/overlays/aeris-iot-accelerator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeris-iot-accelerator-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/security/aeris-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aeris-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/packages/aeris-packages.yml
  title: ''
  type: Packages
  url: packages/aeris-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/packages/aeris-packages.yml
  title: ''
  type: SDKs
  url: packages/aeris-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/conformance/aeris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeris-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/lifecycle/aeris-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aeris-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/lifecycle/aeris-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aeris-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/llms/aeris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeris-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/mcp/aeris-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aeris-mcp.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/plans/aeris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeris-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/security/aeris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeris-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/asyncapi/aeris-stomp-notifications.yml
  title: ''
  type: Webhooks
  url: asyncapi/aeris-stomp-notifications.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aeris/refs/heads/main/skills/_index.yml
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
modified: '2026-09-16'
name: Aeris
nav: Providers
network: true
overview: 'Aeris publishes 68 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Activation codes API, Activities API, and 65 more. Tagged areas include IoT, Cellular Connectivity, M2M, eSIM, and SIM Management.


  The Aeris catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aeris'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Aeris Plans Pricing
  plan_count: 0
  slug: aeris-plans-pricing
random_paper: 4
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
  composite: 64.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 61.5
    developer_ergonomics: 70.8
    discoverability: 55.6
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
      callable: 97.1
      derived: 0
      marker_coverage: 0.0
      total: 68
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
- Machine-to-Machine
website: https://www.aeris.com/
---
