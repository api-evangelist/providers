---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 105
  human_in_the_loop: 1
  name: Emnify Agentic Access
  operation_count: 214
  slug: emnify-agentic-access
  summary_line: 214 operations · 105 acting · 1 human-in-the-loop
api_count: 29
apis:
- description: emnify GraphQL API for flexible, single-request queries against the emnify data model with customizable response shapes. An in-browser GraphiQL IDE supports interactive exploration and testing.
  name: emnify GraphQL API
  slug: emnify-graphql-api
- description: Stream event and usage data to outbound destinations (AWS S3, AWS Kinesis, REST/webhook, Datadog, Salesforce, Keen.io). Supports detailed object schemas for data types, traffic types, tariffs, operato
  name: emnify Data Streamer
  slug: emnify-data-streamer
- description: Public MCP server for emnify documentation. Connect Claude Code, Cursor, or any MCP-aware client to query emnify product, developer, and API reference content directly from your AI assistant.
  name: emnify Documentation MCP Server
  slug: emnify-mcp-server
- description: The subpackage_applicationTokens API from emnify — 2 operation(s) for subpackage_applicationtokens.
  name: emnify subpackage_applicationTokens API
  slug: emnify-subpackage-applicationtokens-api
- description: The subpackage_authentication API from emnify — 8 operation(s) for subpackage_authentication.
  name: emnify subpackage_authentication API
  slug: emnify-subpackage-authentication-api
- description: The subpackage_automations API from emnify — 6 operation(s) for subpackage_automations.
  name: emnify subpackage_automations API
  slug: emnify-subpackage-automations-api
- description: The subpackage_cloudConnect API from emnify — 7 operation(s) for subpackage_cloudconnect.
  name: emnify subpackage_cloudConnect API
  slug: emnify-subpackage-cloudconnect-api
- description: The subpackage_customEvents API from emnify — 4 operation(s) for subpackage_customevents.
  name: emnify subpackage_customEvents API
  slug: emnify-subpackage-customevents-api
- description: The subpackage_endpoint API from emnify — 16 operation(s) for subpackage_endpoint.
  name: emnify subpackage_endpoint API
  slug: emnify-subpackage-endpoint-api
- description: The subpackage_euicc API from emnify — 5 operation(s) for subpackage_euicc.
  name: emnify subpackage_euicc API
  slug: emnify-subpackage-euicc-api
- description: The subpackage_euiccOperation API from emnify — 4 operation(s) for subpackage_euiccoperation.
  name: emnify subpackage_euiccOperation API
  slug: emnify-subpackage-euiccoperation-api
- description: The subpackage_events API from emnify — 2 operation(s) for subpackage_events.
  name: emnify subpackage_events API
  slug: emnify-subpackage-events-api
- description: The subpackage_integrations API from emnify — 10 operation(s) for subpackage_integrations.
  name: emnify subpackage_integrations API
  slug: emnify-subpackage-integrations-api
- description: The subpackage_ipAddressSpaces API from emnify — 3 operation(s) for subpackage_ipaddressspaces.
  name: emnify subpackage_ipAddressSpaces API
  slug: emnify-subpackage-ipaddressspaces-api
- description: The subpackage_lookups API from emnify — 8 operation(s) for subpackage_lookups.
  name: emnify subpackage_lookups API
  slug: emnify-subpackage-lookups-api
- description: The subpackage_operator API from emnify — 1 operation(s) for subpackage_operator.
  name: emnify subpackage_operator API
  slug: emnify-subpackage-operator-api
- description: The subpackage_organization API from emnify — 9 operation(s) for subpackage_organization.
  name: emnify subpackage_organization API
  slug: emnify-subpackage-organization-api
- description: The subpackage_passwordManagementAndActivation API from emnify — 4 operation(s) for subpackage_passwordmanagementandactivation.
  name: emnify subpackage_passwordManagementAndActivation API
  slug: emnify-subpackage-passwordmanagementandactivation-api
- description: The subpackage_serviceLookupsAndConfiguration API from emnify — 5 operation(s) for subpackage_servicelookupsandconfiguration.
  name: emnify subpackage_serviceLookupsAndConfiguration API
  slug: emnify-subpackage-servicelookupsandconfiguration-api
- description: The subpackage_serviceProfiles API from emnify — 7 operation(s) for subpackage_serviceprofiles.
  name: emnify subpackage_serviceProfiles API
  slug: emnify-subpackage-serviceprofiles-api
- description: The subpackage_sim API from emnify — 9 operation(s) for subpackage_sim.
  name: emnify subpackage_sim API
  slug: emnify-subpackage-sim-api
- description: The subpackage_simOperation API from emnify — 4 operation(s) for subpackage_simoperation.
  name: emnify subpackage_simOperation API
  slug: emnify-subpackage-simoperation-api
- description: The subpackage_simUnlinkedProductStatistics API from emnify — 1 operation(s) for subpackage_simunlinkedproductstatistics.
  name: emnify subpackage_simUnlinkedProductStatistics API
  slug: emnify-subpackage-simunlinkedproductstatistics-api
- description: The subpackage_systemEvents API from emnify — 2 operation(s) for subpackage_systemevents.
  name: emnify subpackage_systemEvents API
  slug: emnify-subpackage-systemevents-api
- description: The subpackage_tagManagement API from emnify — 8 operation(s) for subpackage_tagmanagement.
  name: emnify subpackage_tagManagement API
  slug: emnify-subpackage-tagmanagement-api
- description: The subpackage_tariffPlans API from emnify — 3 operation(s) for subpackage_tariffplans.
  name: emnify subpackage_tariffPlans API
  slug: emnify-subpackage-tariffplans-api
- description: The subpackage_tariffProfiles API from emnify — 9 operation(s) for subpackage_tariffprofiles.
  name: emnify subpackage_tariffProfiles API
  slug: emnify-subpackage-tariffprofiles-api
- description: The subpackage_userManagement API from emnify — 8 operation(s) for subpackage_usermanagement.
  name: emnify subpackage_userManagement API
  slug: emnify-subpackage-usermanagement-api
- description: The subpackage_workspaces API from emnify — 7 operation(s) for subpackage_workspaces.
  name: emnify subpackage_workspaces API
  slug: emnify-subpackage-workspaces-api
arazzos:
- description: Authenticate, list available operators, then add one to an endpoint's blacklist.
  name: emnify Blacklist Operator for Endpoint
  slug: emnify-blacklist-operator-for-endpoint-workflow
- description: Authenticate, read endpoint details, then read its live connectivity status.
  name: emnify Check Endpoint Connectivity
  slug: emnify-check-endpoint-connectivity-workflow
- description: Authenticate, create a tag, create an endpoint, then assign the tag to it.
  name: emnify Create and Tag Endpoint
  slug: emnify-create-and-tag-endpoint-workflow
- description: Authenticate, read the endpoint, suspend its SIM, then delete the endpoint.
  name: emnify Decommission Endpoint
  slug: emnify-decommission-endpoint-workflow
- description: Authenticate, read endpoint connectivity, then grant a temporary traffic limit extension if blocked.
  name: emnify Extend Traffic Limit When Blocked
  slug: emnify-extend-traffic-limit-when-blocked-workflow
- description: Authenticate, find a SIM by ICCID, then create an endpoint bound to that SIM.
  name: emnify Find SIM and Provision Endpoint
  slug: emnify-find-sim-and-provision-endpoint-workflow
- description: Authenticate, confirm the endpoint, then read its usage and daily usage statistics.
  name: emnify Get Endpoint Usage Statistics
  slug: emnify-get-endpoint-usage-stats-workflow
- description: Authenticate, confirm the endpoint, then retrieve its cell-tower-based location.
  name: emnify Locate Endpoint
  slug: emnify-locate-endpoint-workflow
- description: Authenticate, read organization details, then read active inclusive volumes and daily stats.
  name: emnify Organization Volume Report
  slug: emnify-organization-volume-report-workflow
- description: Authenticate, create an endpoint with a SIM, then activate that SIM.
  name: emnify Provision and Activate Endpoint
  slug: emnify-provision-and-activate-endpoint-workflow
- description: Authenticate, validate a SIM batch by its BIC, then register the batch to the workspace.
  name: emnify Register SIM Batch by BIC
  slug: emnify-register-sim-batch-workflow
- description: Authenticate, read connectivity status, then reset connectivity only when the device is stuck.
  name: emnify Reset Endpoint Connectivity When Blocked
  slug: emnify-reset-endpoint-connectivity-when-blocked-workflow
- description: Authenticate, send an SMS to an endpoint, then list the endpoint's SMS to confirm it.
  name: emnify Send SMS and Track Delivery
  slug: emnify-send-sms-and-track-delivery-workflow
- description: Authenticate, confirm the endpoint exists, then send a mobile-terminated SMS to it.
  name: emnify Send SMS to Endpoint
  slug: emnify-send-sms-to-endpoint-workflow
- description: Authenticate, read the current data quota, then set a new data quota on an endpoint.
  name: emnify Set Endpoint Data Quota
  slug: emnify-set-endpoint-data-quota-workflow
- description: Authenticate, read the current SMS quota, then assign a new SMS quota to an endpoint.
  name: emnify Set Endpoint SMS Quota
  slug: emnify-set-endpoint-sms-quota-workflow
- description: Authenticate, read a SIM, and suspend it only when it is currently Activated.
  name: emnify Suspend SIM When Active
  slug: emnify-suspend-sim-when-active-workflow
artifact_total: 96
collections:
- collection_type: postman
  name: emnify REST API
  slug: postman-emnify-api
- collection_type: open
  name: emnify REST API
  slug: open-emnify-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emnify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emnify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emnify-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/emnify/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-blacklist-operator-for-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-check-endpoint-connectivity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-create-and-tag-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-decommission-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-extend-traffic-limit-when-blocked-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-find-sim-and-provision-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-get-endpoint-usage-stats-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-locate-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-organization-volume-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-provision-and-activate-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-register-sim-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-reset-endpoint-connectivity-when-blocked-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-send-sms-and-track-delivery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-send-sms-to-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-set-endpoint-data-quota-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-set-endpoint-sms-quota-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/emnify-suspend-sim-when-active-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.emnify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.emnify.com/quickstart
- group: start
  title: ''
  type: Signup
  url: https://www.emnify.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.emnify.com/plans-and-packages
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EMnify
- group: build
  title: ''
  type: SDKs
  url: https://github.com/emnify/emnify-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/emnify/emnify-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/emnify-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://emnify.github.io/emnify-sdk-python/autoapi/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/sdks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/sdks/python/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/sdks/java/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/auth/application-tokens
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/auth/user-credentials
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/auth/multi-factor-authentication
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emnify.com/developers/auth/jwts
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.emnify.com/developers/api-guidelines/rate-limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.emnify.com/developers/api-guidelines/errors
- group: design
  title: ''
  type: Pagination
  url: https://docs.emnify.com/developers/api-guidelines/collections-pagination
- group: design
  title: ''
  type: Conventions
  url: https://docs.emnify.com/developers/api-guidelines/conventions
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.emnify.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.emnify.com/hc/en-us/requests/new
- group: operate
  title: ''
  type: Forums
  url: https://www.emnify.com/iot-blog
- group: company
  title: ''
  type: Blog
  url: https://www.emnify.com/iot-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.emnify.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emnify.com/legal/privacy-statement
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.emnify.com/iot-security
- group: build
  title: ''
  type: Tools
  url: https://github.com/emnify/grafana-pcapextractor-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/emnify/akamai-insights-datasource
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emnify
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/emnify
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/emnify
- group: commercial
  title: ''
  type: Plans
  url: plans/emnify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emnify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emnify-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: emnify is a cloud-native global IoT cellular connectivity provider operating its own mobile core and SuperNetwork across 540+ MNOs in 190+ countries. emnify supplies SIMs, eUICC-enabled multi-form-factor cards, and Consumer/Advanced eSIM (SGP.32) profiles to enterprise IoT deployments — fleet tracking, EV charging, point-of-sale, smart buildings, micromobility, airline crew tablets, and more. The emnify REST API, GraphQL API, and Data Streamer give programmatic control over SIMs, endpoints, service and tariff profiles, eUICC profile operations, events, SMS, callbacks, and outbound usage/event streaming to S3, Kinesis, and webhooks. NTN-IoT satellite connectivity via Skylo extends coverage beyond terrestrial cellular.
examples:
- key_count: 2
  name: Emnify Authenticate Example
  slug: emnify-authenticate-example
- key_count: 2
  name: Emnify List Endpoints Example
  slug: emnify-list-endpoints-example
- key_count: 2
  name: Emnify List Events Example
  slug: emnify-list-events-example
- key_count: 2
  name: Emnify Send Sms Example
  slug: emnify-send-sms-example
features:
- Global cellular IoT connectivity across 540+ MNOs in 190+ countries via the emnify SuperNetwork
- Multi-form-factor SIMs (2FF, 3FF, 4FF, MFF2) all eUICC-enabled by default
- Advanced IoT eSIM (SGP.32) for remote profile management on enterprise devices
- Consumer eSIM profiles deployable via MDM or QR code
- SGP.32 IoT eSIM operations — eUICC management, scheduled profile download/install/enable/disable/delete
- NTN-IoT satellite connectivity via Skylo (NB-IoT over GEO satellite, RAT 17) — SatPlus, SatSolo, CellSolo plans
- REST API with 200+ operations across 150+ paths spanning SIM, Endpoint, eUICC, SMS, Event, Service Profile, Tariff Profile, Organization, User, IP, Tag, Operator, and System resources
- GraphQL API with interactive GraphiQL IDE for flexible single-request queries
- Data Streamer for outbound event/usage streaming to AWS S3, AWS Kinesis, REST/webhook, Datadog, Salesforce, and Keen.io
- API callbacks for asynchronous Data Streamer delivery; SMS callbacks for mobile-originated SMS with JWT auth
- Application token authentication (M2M) plus user-credential auth for cross-workspace operations
- Multi-factor authentication with trusted device fingerprinting (90-day skip window)
- JWT short-lived bearer tokens with refresh-token rotation
- Workspaces — multi-tenant logical containers under one organization for complex business structures
- Single sign-on (SSO) for enterprise user administration
- Service profiles — traffic limits, operator blacklists, IMEI lock, callback configuration per device class
- Tariff profiles — geographic rate plans with per-MB, per-SMS, and per-SIM lifecycle fees
- Device policies — service and coverage policies applied at the fleet level
- Bulk endpoint operations (/api/v2/endpoint/multi) for fleet-scale create/update/delete
- Factory Test Mode (FTM) — 100 KB data and 10 SMS free per SIM for pre-production validation
- Data plans — fixed allowance, pooled allowance, pay-per-use, and volume commitment
- Automations and no-code workflows in the Portal (Zapier, event/SMS/application triggers)
- 30+ Portal reports including CDRs, daily usage, live usage, monthly invoiced SIMs, satellite, network activity, global distribution
- AWS Transit Gateway Cloud Connect for private VPC breakout; VPN breakout option
- LTE-M and NB-IoT LPWAN support with Power Save Mode (PSM) and eDRX
- Two officially supported SDKs (Python and Java) plus public MCP documentation server
- Documentation MCP server at docs.emnify.com/_mcp/server for AI client integration (Claude Code, Cursor)
- Public llms.txt and llms-full.txt feeds with inline OpenAPI fragments for AI-friendly documentation
- Standard, Business, and Enterprise support tiers with 24/7 options
finops:
- name: Emnify Finops
  service_category: Networking
  slug: emnify-finops
graphqls:
- description: emnify provides a GraphQL API alongside its REST API, enabling flexible single-request queries against the emnify IoT connectivity data model. Clients can select exactly the fields they need, traverse
  name: emnify GraphQL API
  slug: emnify-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emnify.png
json_schemas:
- name: emnify Endpoint
  property_count: 15
  slug: emnify-endpoint
- name: emnify Event
  property_count: 12
  slug: emnify-event
- name: emnify SIM
  property_count: 14
  slug: emnify-sim
json_structures:
- name: Emnify Endpoint Structure
  property_count: 12
  slug: emnify-endpoint-structure
- name: Emnify Sim Structure
  property_count: 13
  slug: emnify-sim-structure
jsonld:
- class_count: 0
  name: Emnify Context
  property_count: 9
  slug: emnify-context
layout: provider
modified: '2026-05-25'
name: emnify
nav: Providers
network: true
overview: 'emnify publishes 26 APIs on the [APIs.io](https://apis.io/) network, including subpackage_applicationTokens API, subpackage_authentication API, subpackage_automations API, and 23 more. Tagged areas include IoT, Internet of Things, Cellular Connectivity, IoT SIM, and eSIM.


  The emnify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  emnify''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, changelog, and 51 more developer resources.'
plans:
- name: Emnify Plans Pricing
  plan_count: 11
  slug: emnify-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 4
  name: Emnify Rate Limits
  slug: emnify-rate-limits
rules:
- name: emnify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: emnify-jsonschema-spectral-rules
- name: emnify API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: emnify-rules
score:
  band: exemplar
  composite: 66.0
  delta: -2.3
  facets:
    commercial_clarity: 92.1
    contract_quality: 76.1
    developer_ergonomics: 65.2
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 68.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emnify/refs/heads/main/screenshots/emnify-2026-06-20T180637.png
security:
- kind: authentication
  name: Emnify Authentication
  slug: emnify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Emnify Domain Security
  slug: emnify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emnify
tags:
- IoT
- Internet of Things
- Cellular Connectivity
- IoT SIM
- eSIM
- Consumer eSIM
- SGP.32
- M2M
- NTN-IoT
- Satellite
- SuperNetwork
website: https://www.emnify.com
---
