---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Bharti Airtel Agentic Access
  operation_count: 68
  slug: bharti-airtel-agentic-access
  summary_line: 68 operations · 35 acting
api_count: 8
apis:
- description: Airtel's original partner developer programme, launched in 2017 and now an unmaintained legacy portal (the site still carries a 2017 copyright). Its public documentation still describes real OAuth 2.0
  name: Airtel Smart API (legacy)
  slug: airtel-smart-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs shall allow user to generate Access Token and refresh Access Token to perform any action on CMP via the API gateway.
  name: Bharti Airtel Account Authorization API
  slug: bharti-airtel-account-authorization-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs fetch various details about a Billable Customer Account including Customer Profile, Plan details, User details and so on.
  name: Bharti Airtel Account Details API
  slug: bharti-airtel-account-details-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: <strong>Call Detail Record (CDR)</strong> is the detailed record of the call, which contains various call details such as Time, Date, Duration, Caller_ID, Destination_Number, Status, recording URL, et
  name: Bharti Airtel Airtel IQ Sample CDR(Call Data Record) API
  slug: bharti-airtel-airtel-iq-sample-cdr-call-data-record-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This API will help you to generate token from the client credentials shared upon subscription to location services. In case you have not yet subscribed to location service, email us to locate.support@
  name: Bharti Airtel Authorization API
  slug: bharti-airtel-authorization-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: These APIs can be used to send Bulk SMS in different ways as documented below
  name: Bharti Airtel Bulk SMS APIs API
  slug: bharti-airtel-bulk-sms-apis-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: To data usage on a specific SIM, this API will allow user to get total data allocation, available data, used data, device information & session information for the SIM.
  name: Bharti Airtel Device & Session Information API
  slug: bharti-airtel-device-session-information-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: These APIs can be used to send a single SMS in a single request as documented below
  name: Bharti Airtel Individual SMS APIs API
  slug: bharti-airtel-individual-sms-apis-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs fetch various details about Sim details, Basket details and so on in the account.
  name: Bharti Airtel Inventory Management API
  slug: bharti-airtel-inventory-management-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This API will allow user to fetch Job details for any operations being performed in that Billable account.
  name: Bharti Airtel Job Status API
  slug: bharti-airtel-job-status-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs to manage SIM KYC details.
  name: Bharti Airtel KYC Manager API
  slug: bharti-airtel-kyc-manager-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This API will return location of MSISDN including Latitude and Longitude.
  name: Bharti Airtel Location API
  slug: bharti-airtel-location-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: These set of APIs allow lifecycle management of the Messaging Centre functionality
  name: Bharti Airtel Messaging Centre API
  slug: bharti-airtel-messaging-centre-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs allow customer initiate consent, fetch consent details, delete resource, fetch list of msisdn for consent was initiated and various other API to handle consumer msisdn's and their con
  name: Bharti Airtel Resource Consent API
  slug: bharti-airtel-resource-consent-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This API shall allow user to change the state of SIMs.
  name: Bharti Airtel SIM LifeCycle API
  slug: bharti-airtel-sim-lifecycle-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This API shall allow user to change the state of SIMs.
  name: Bharti Airtel SIM LifeCycle Bulk API
  slug: bharti-airtel-sim-lifecycle-bulk-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: These set of Tenant APIs allow customer to initiate consent, fetch consent details, delete consent, fetch list of msisdn for consent was initiated and various other API to handle tenant msisdn's and t
  name: Bharti Airtel Tenant API
  slug: bharti-airtel-tenant-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: These set of APIs allow customer to validate a physical address against network fetched live location. To get access to these API's please email to locate.support@airtel.com
  name: Bharti Airtel Validation API
  slug: bharti-airtel-validation-api-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: This set of APIs to manage whitelisting numbers on Airtel IoT portal in Batch
  name: Bharti Airtel Whitelisting API
  slug: bharti-airtel-whitelisting-api
- baseURL: https://iqsms.airtel.in/api/v1
  baseurl_source: declared
  description: The Whitelisting APIs API from Bharti Airtel — 1 operation(s) for whitelisting apis.
  name: Bharti Airtel Whitelisting APIs API
  slug: bharti-airtel-whitelisting-apis-api
artifact_total: 31
asyncapis:
- description: ''
  name: Bharti Airtel Webhooks
  slug: bharti-airtel-webhooks
collections:
- collection_type: open
  name: Airtel IoT
  slug: open-bharti-airtel-iot
- collection_type: open
  name: Airtel IQ API Documentation
  slug: open-bharti-airtel-iq-reporting
- collection_type: open
  name: Airtel IQ SMS Core APIs
  slug: open-bharti-airtel-iq-sms
- collection_type: open
  name: Locate API Catalog
  slug: open-bharti-airtel-locate
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bharti-airtel-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bharti-airtel-iq-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bharti-airtel-iq-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bharti-airtel-iot-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bharti-airtel-locate-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bharti-airtel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bharti-airtel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bharti-airtel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bharti-airtel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bharti-airtel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bharti-airtel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bharti-airtel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bharti-airtel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bharti-airtel-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bharti-airtel-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bharti-airtel-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bharti-airtel-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bharti-airtel-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/bharti-airtel-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bharti-airtel-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bharti-airtel-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bharti-airtel-apis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-send-compliant-sms.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-locate-device-with-consent.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-manage-iot-sim-lifecycle.md
- group: company
  title: ''
  type: Website
  url: https://www.airtel.in/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/sms/overview
- group: docs
  title: ''
  type: APIReference
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/sms/sms-utility
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/voice/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.airtel.in/
- group: start
  title: ''
  type: SignUp
  url: https://www.airtel.in/business/b2b/airtel-ccp/dashboard/#/signup
- group: start
  title: ''
  type: Console
  url: https://www.airtel.in/business/b2b/airtel-ccp/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://www.airtel.in/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.airtel.in/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airtel.in/business/b2b/cpaas
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airtel.in/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airtel.in/mobile/terms-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airtel-business/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/airtelindia/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC62RQR1TkP_945zTN6Jwecg
- group: other
  title: ''
  type: Email
  url: mailto:iqsalessupport@airtel.com
created: '2026-07-25'
description: 'Bharti Airtel Limited is an Indian multinational telecommunications operator headquartered in New Delhi, and one of the two dominant mobile network operators in its home market of India alongside Reliance Jio. It runs mobile (2G/4G/5G), fixed broadband, DTH television, enterprise connectivity, data centre (Nxtra) and payments-bank businesses across India, South Asia and — through the separately listed Airtel Africa — fourteen African countries. In the telecom value chain Airtel is an access-network owner: it holds the spectrum, the SIM estate, the subscriber identity and the network signalling that the rest of the industry resells. Its API posture is split in two, and the split is the whole story. The connectivity-product side is genuinely API-native and publicly documented: Airtel IQ, the operator''s CPaaS suite, publishes open Swagger for its SMS and CDR reporting APIs and offers a self-serve trial account, while the Airtel IoT and Airtel Locate developer portals publish
  complete OpenAPI 3.0 catalogues (43 and 19 operations) as Redoc pages that need no login. The network-API side — the CAMARA and GSMA Open Gateway surface that defines this sector — is the opposite: Airtel is a GSMA Open Gateway signatory, a founding operator shareholder in Aduna (the Ericsson-led network-API joint venture), and has commercially launched a CAMARA SIM Swap API to Indian banks through a federated Jio/Vi/Airtel channel, yet it publishes no CAMARA endpoint, no CAMARA specification, no CIBA authorization surface and no network-API developer portal of its own. Developers reach Airtel''s network capabilities only through aggregators — Aduna, and Nokia''s Network as Code platform — never directly. Its own "Airtel API Marketplace" at developers.airtel.in is a login wall, and its original 2017 Smart API partner programme at openapi.airtel.in/smartapi survives as an unmaintained legacy portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Bharti Airtel MCP Server
  slug: bharti-airtel-mcp-server
modified: '2026-07-25'
name: Bharti Airtel
nav: Providers
network: true
overview: 'Bharti Airtel publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Account Authorization API, Account Details API, Airtel IQ Sample CDR(Call Data Record) API, and 16 more. Tagged areas include Telecommunications, India, Mobile Network Operator, Network APIs, and CAMARA.


  The Bharti Airtel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bharti Airtel''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, developer console, and 35 more developer resources.'
random_paper: 18
scopes:
- name: Bharti Airtel Scopes
  scope_count: 4
  slug: bharti-airtel-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode/implicit
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 56.5
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 81.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bharti-airtel/refs/heads/main/screenshots/bharti-airtel-2026-08-07T162406.png
security:
- kind: authentication
  name: Bharti Airtel Authentication
  slug: bharti-airtel-authentication
  summary_line: http-basic/oauth2 · 4 schemes
- kind: domain-security
  name: Bharti Airtel Domain Security
  slug: bharti-airtel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bharti Airtel Vulnerability Disclosure
  slug: bharti-airtel-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: bharti-airtel
tags:
- Telecommunications
- India
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- CPaaS
- Messaging
- SMS
- RCS
- Voice
- IoT
- M2M
- Device Location
- Broadband
- 5G
- Identity Verification
- Carrier Billing
- Consent Management
website: https://www.airtel.in/
---
