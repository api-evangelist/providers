---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 105
  human_in_the_loop: 1
  name: Emnify Agentic Access
  operation_count: 214
  slug: emnify-agentic-access
  summary_line: 214 operations · 105 acting · 1 human-in-the-loop
api_count: 1
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
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of application tokens for API access
  name: emnify Application Tokens API
  slug: emnify-applicationtokens-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Mechanisms for API authentication
  name: emnify Authentication API
  slug: emnify-authentication-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Cloud connection services and their configuration
  name: emnify Cloud Connect API
  slug: emnify-cloudconnect-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: API endpoints for enterprise resources
  name: emnify Endpoint API
  slug: emnify-endpoint-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Event logging and management
  name: emnify Events API
  slug: emnify-events-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Network Flow Log records for device traffic observability
  name: emnify Flow Logs API
  slug: emnify-flowlogs-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Integration of external services and systems
  name: emnify Integrations API
  slug: emnify-integrations-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of IP address spaces
  name: emnify Ip Address Spaces API
  slug: emnify-ipaddressspaces-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Lookup services for various resources
  name: emnify Lookups API
  slug: emnify-lookups-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of network operators and their data
  name: emnify Operator API
  slug: emnify-operator-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of organizations and their data
  name: emnify Organization API
  slug: emnify-organization-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Password management and activation services
  name: emnify Password Management And Activation API
  slug: emnify-passwordmanagementandactivation-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of permissions, roles, and role assignments
  name: emnify Permission And Role Management API
  slug: emnify-permissionandrolemanagement-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Lookup and configuration services for API resources
  name: emnify Service Lookups And Configuration API
  slug: emnify-servicelookupsandconfiguration-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Profiles for services and their configuration
  name: emnify Service Profiles API
  slug: emnify-serviceprofiles-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of SIM cards and their data
  name: emnify Sim API
  slug: emnify-sim-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of endpoint tags
  name: emnify Tag Management API
  slug: emnify-tagmanagement-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of tariff plans
  name: emnify Tariff Plans API
  slug: emnify-tariffplans-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Profiles for tariffs and their configuration
  name: emnify Tariff Profiles API
  slug: emnify-tariffprofiles-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of workspaces and their data
  name: emnify Workspaces API
  slug: emnify-workspaces-api
- baseURL: https://cdn.emnify.net
  baseurl_source: spec
  description: Management of users and their roles
  name: emnify User Management API
  slug: emnify-user-management-api
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
artifact_total: 116
collections:
- collection_type: postman
  name: emnify REST API
  slug: postman-emnify-api
- collection_type: open
  name: emnify REST API
  slug: open-emnify-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens API
  slug: open-emnify-subpackage-applicationtokens-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_authentication API
  slug: open-emnify-subpackage-authentication-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_automations API
  slug: open-emnify-subpackage-automations-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_cloudConnect API
  slug: open-emnify-subpackage-cloudconnect-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_customEvents API
  slug: open-emnify-subpackage-customevents-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_endpoint API
  slug: open-emnify-subpackage-endpoint-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_euicc API
  slug: open-emnify-subpackage-euicc-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_euiccOperation API
  slug: open-emnify-subpackage-euiccoperation-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_events API
  slug: open-emnify-subpackage-events-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_integrations API
  slug: open-emnify-subpackage-integrations-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_ipAddressSpaces API
  slug: open-emnify-subpackage-ipaddressspaces-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_lookups API
  slug: open-emnify-subpackage-lookups-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_operator API
  slug: open-emnify-subpackage-operator-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_organization API
  slug: open-emnify-subpackage-organization-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_passwordManagementAndActivation API
  slug: open-emnify-subpackage-passwordmanagementandactivation-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_serviceLookupsAndConfiguration API
  slug: open-emnify-subpackage-servicelookupsandconfiguration-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_serviceProfiles API
  slug: open-emnify-subpackage-serviceprofiles-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_sim API
  slug: open-emnify-subpackage-sim-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_simOperation API
  slug: open-emnify-subpackage-simoperation-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_simUnlinkedProductStatistics API
  slug: open-emnify-subpackage-simunlinkedproductstatistics-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_systemEvents API
  slug: open-emnify-subpackage-systemevents-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_tagManagement API
  slug: open-emnify-subpackage-tagmanagement-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_tariffPlans API
  slug: open-emnify-subpackage-tariffplans-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_tariffProfiles API
  slug: open-emnify-subpackage-tariffprofiles-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_userManagement API
  slug: open-emnify-subpackage-usermanagement-api
- collection_type: open
  name: emnify REST subpackage_applicationTokens subpackage_workspaces API
  slug: open-emnify-subpackage-workspaces-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.emnify.com/
- group: other
  href: https://artifacts.apis.io/emnify/capabilities/emnify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/emnify-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/emnify/agentic-access/emnify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emnify-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/emnify/security/emnify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emnify-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/emnify/authentication/emnify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emnify-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/emnify/overview
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-blacklist-operator-for-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-blacklist-operator-for-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-check-endpoint-connectivity-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-check-endpoint-connectivity-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-create-and-tag-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-create-and-tag-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-decommission-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-decommission-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-extend-traffic-limit-when-blocked-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-extend-traffic-limit-when-blocked-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-find-sim-and-provision-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-find-sim-and-provision-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-get-endpoint-usage-stats-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-get-endpoint-usage-stats-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-locate-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-locate-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-organization-volume-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-organization-volume-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-provision-and-activate-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-provision-and-activate-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-register-sim-batch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-register-sim-batch-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-reset-endpoint-connectivity-when-blocked-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-reset-endpoint-connectivity-when-blocked-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-send-sms-and-track-delivery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-send-sms-and-track-delivery-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-send-sms-to-endpoint-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-send-sms-to-endpoint-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-set-endpoint-data-quota-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-set-endpoint-data-quota-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-set-endpoint-sms-quota-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/emnify-set-endpoint-sms-quota-workflow.yml
- group: design
  href: https://artifacts.apis.io/emnify/arazzo/emnify-suspend-sim-when-active-workflow.yml
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
  href: https://artifacts.apis.io/emnify/plans/emnify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/emnify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/emnify/rate-limits/emnify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/emnify-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/emnify/finops/emnify-finops.yml
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
- has_sources: true
  method: derived
  name: Emnify Finops
  primary_unit: ''
  service_category: ''
  slug: emnify-finops
  template: true
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
modified: '2026-09-16'
name: emnify
nav: Providers
network: true
overview: 'emnify publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Application Tokens API, Authentication API, Cloud Connect API, and 21 more. Tagged areas include IoT, Cellular Connectivity, IoT SIM, eSIM, and Consumer eSIM.


  The emnify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  emnify''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, changelog, and 53 more developer resources.'
plans:
- name: Emnify Plans Pricing
  plan_count: 0
  slug: emnify-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Emnify Rate Limits
  slug: emnify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: emnify — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: emnify-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: emnify API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: emnify-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 31.6
    contract_governance: 27.3
    contract_quality: 69.3
    developer_ergonomics: 68.6
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 43.8
      total: 48
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 18.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/emnify/emnify-2026-06-20T180637.png
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
- Cellular Connectivity
- IoT SIM
- eSIM
- Consumer eSIM
- SGP.32
- M2M
- NTN-IoT
- Satellite
- SuperNetwork
- Machine-to-Machine
website: https://www.emnify.com/
---
