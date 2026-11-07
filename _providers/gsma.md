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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 79
  human_in_the_loop: 1
  name: Gsma Agentic Access
  operation_count: 159
  slug: gsma-agentic-access
  summary_line: 159 operations · 79 acting · 1 human-in-the-loop
api_count: 37
apis:
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Accounts** APIs are used to support a range of operations on a financial account resource and associated resources. Types of accounts include mobile wallets, financial institution accounts and u
  name: GSMA Accounts API
  slug: gsma-accounts-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Authorisation** Codes APIs allow a payer to generate a payment code which when presented to the payee, can be redeemed for an amount associated with the code. Authorisation codes can be set to e
  name: GSMA Authorisation Codes API
  slug: gsma-authorisation-codes-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: 'The **Bills** APIs allow a mobile money provider to allow customers to retrieve and pay bills. Specific use cases include: - Retrieving information on service providers (bill companies) that accept bi'
  name: GSMA Bills API
  slug: gsma-bills-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Provides information on Call Forwarding settings for the provided phone number (PhoneNumber).
  name: GSMA Call Forwarding information retrieval API
  slug: gsma-call-forwarding-information-retrieval-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: GSMA Check Device Swap API
  slug: gsma-check-device-swap-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Debit Mandates** APIs allow a mobile money customer to provide prior approval for payments to be taken from their account by a requesting payee. If the amount limit field is not supplied, the pa
  name: GSMA Debit Mandates API
  slug: gsma-debit-mandates-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Find the closest Edge Cloud Zone to the user device.
  name: GSMA Discovery API
  slug: gsma-discovery-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: QoD control operations for home devices
  name: GSMA Home Devices QoD API
  slug: gsma-home-devices-qod-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Links** APIs are used to establish a link between two separate accounts on the client and provider systems. The API can be used for example to link a mobile wallet account to a Microfinance Inst
  name: GSMA Links API
  slug: gsma-links-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Retrieve the location of a device
  name: GSMA Location Retrieval API
  slug: gsma-location-retrieval-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to match a customer identity against the account data bound to their phone number.
  name: GSMA Match API
  slug: gsma-match-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to manage One Step Payment procedure
  name: GSMA One Step Payment API
  slug: gsma-one-step-payment-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: API operations to manage OTP codes
  name: GSMA OTP Management API
  slug: gsma-otp-management-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to obtain information about payments
  name: GSMA Payment API
  slug: gsma-payment-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: API operation to return the phone number associated to the access token.
  name: GSMA Phone Number Share API
  slug: gsma-phone-number-share-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: GSMA Phone Number Verify API
  slug: gsma-phone-number-verify-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Manage QoS sessions
  name: GSMA QoS Sessions API
  slug: gsma-qos-sessions-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Quotations** APIs are used to obtain one or multiple quotes for a mobile money customer who wishes to transfer money. The creation of a quote involves returning any fees that will be levied on t
  name: GSMA Quotations API
  slug: gsma-quotations-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to manage Refund procedure
  name: GSMA Refund API
  slug: gsma-refund-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Receive the last date in which the device of the end-user was swapped
  name: GSMA Retrieve Device Swap Date API
  slug: gsma-retrieve-device-swap-date-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: 'Supporting APIs consist of the following: - **Heartbeat API:** Used for monitoring purposes and establishes whether the system of an API provider is in a state that enables a client to submit a reques'
  name: GSMA Supporting API
  slug: gsma-supporting-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The **Transactions** APIs are used to support mobile money financial transaction use cases. Transactions are used for a wide range of use cases including merchant payments, international transfers, do
  name: GSMA Transactions API
  slug: gsma-transactions-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to manage Two Step Payment procedure
  name: GSMA Two Step Payment API
  slug: gsma-two-step-payment-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Provides information on Unconditional Call Forwarding settings for the provided phone number (PhoneNumber)
  name: GSMA Unconditional Call Forwarding information retrieval API
  slug: gsma-unconditional-call-forwarding-information-retrieval-api
- description: Scam Signal API allows businesses to protect their customers from impersonation scams, particularly Authorized Pushed Payment (APP) fraud.
  name: GSMA Camara Project Scam Signal API
  slug: scam-signal-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations for ApiProduct Resource
  name: GSMA Api Product API
  slug: gsma-api-product-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations for ApiProductOrder Resource
  name: GSMA API Product Order API
  slug: gsma-apiproductorder-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Application and Application Instance Lice Cycle Management
  name: GSMA Application API
  slug: gsma-application-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations to define, read and manage an application's thresholds for network quality (latency, jitter, loss, throughput)
  name: GSMA Application Profiles API
  slug: gsma-application-profiles-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations for ApplicationOwner Resource
  name: GSMA Application Owner API
  slug: gsma-applicationowner-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Check details about the length of tenure of the subscriber
  name: GSMA Check Subscriber Tenure API
  slug: gsma-check-subscriber-tenure-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Create and manage a subscription to receive periodic connectivity insights
  name: GSMA Connectivity Insights Subscriptions API
  slug: gsma-connectivity-insights-subscriptions-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Endpoints to register and terminate an Event Listener
  name: GSMA events subscription API
  slug: gsma-events-subscription-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Retrieve details about the device being used by a mobile subscriber
  name: GSMA Get Device Identifiers API
  slug: gsma-get-device-identifiers-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Operations for Monitor Resource
  name: GSMA Monitor API
  slug: gsma-monitor-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Read the network's level of confidence that it can meet the quality thresholds for a given application profile and end user device.
  name: GSMA Network Quality API
  slug: gsma-network-quality-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Notifications for Resource Lifecycle and event notifications
  name: GSMA notification listener API
  slug: gsma-notification-listener-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Manage QoS Profiles
  name: GSMA QoS Profiles API
  slug: gsma-qos-profiles-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: The Send SMS API from GSMA — 1 operation(s) for send sms.
  name: GSMA Send SMS API
  slug: gsma-send-sms-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Reads existing TrafficInfluence resources
  name: GSMA Traffic Influence API Read API
  slug: gsma-traffic-influence-api-read-api
- baseURL: https://sandbox.mobilemoneyapi.io/simulator/v1.2/passthrough/mm
  baseurl_source: declared
  description: Creates of modifies a TrafficInfluence resource
  name: GSMA Traffic Influence API Write API
  slug: gsma-traffic-influence-api-write-api
artifact_total: 72
asyncapis:
- description: ''
  name: Gsma Webhooks
  slug: gsma-webhooks
collections:
- collection_type: open
  name: Mobile Money API
  slug: open-gsma-mobile-money-api
- collection_type: open
  name: Call Forwarding Signal
  slug: open-gsma-open-gateway-call-forwarding-signal
- collection_type: open
  name: Carrier Billing Refund
  slug: open-gsma-open-gateway-carrier-billing-refund
- collection_type: open
  name: Carrier Billing
  slug: open-gsma-open-gateway-carrier-billing
- collection_type: open
  name: CAMARA Mobile Device Identifier
  slug: open-gsma-open-gateway-device-identifier
- collection_type: open
  name: Device Location Retrieval
  slug: open-gsma-open-gateway-device-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-gsma-open-gateway-device-location-verification
- collection_type: open
  name: Device Reachability Status
  slug: open-gsma-open-gateway-device-reachability-status
- collection_type: open
  name: Device Roaming Status
  slug: open-gsma-open-gateway-device-roaming-status
- collection_type: open
  name: Device Swap
  slug: open-gsma-open-gateway-device-swap
- collection_type: open
  name: Home Devices QoD
  slug: open-gsma-open-gateway-home-devices-quality-on-demand
- collection_type: open
  name: Know Your Customer Match
  slug: open-gsma-open-gateway-know-your-customer
- collection_type: open
  name: Number Verification
  slug: open-gsma-open-gateway-number-verification
- collection_type: open
  name: One Time Password SMS
  slug: open-gsma-open-gateway-otp-validation
- collection_type: open
  name: Population Density Data
  slug: open-gsma-open-gateway-population-density-data
- collection_type: open
  name: Quality-On-Demand
  slug: open-gsma-open-gateway-quality-on-demand
- collection_type: open
  name: SIM Swap
  slug: open-gsma-open-gateway-sim-swap
- collection_type: open
  name: Simple Edge Discovery
  slug: open-gsma-open-gateway-simple-edge-discovery
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.gsma.com/newsroom/feed/
- group: other
  href: https://artifacts.apis.io/gsma/capabilities/gsma-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gsma-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/gsma/overlays/gsma-mobile-money-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gsma-mobile-money-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/gsma/security/gsma-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gsma-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gsma/security/gsma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gsma-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/gsma/agentic-access/gsma-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gsma-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gsma/authentication/gsma-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gsma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gsma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open-gateway.gsma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-gateway.gsma.com/docs
- group: start
  title: ''
  type: Sandbox
  url: https://open-gateway.gsma.com/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mobilemoneyapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-frequently-asked-questions/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/supporters/
- group: other
  title: ''
  type: Dataset
  url: https://d3bj8knxlstxyw.cloudfront.net/assets-map-launches.json
- group: docs
  title: ''
  type: Documentation
  url: https://open-gateway.gsma.com/map
- group: docs
  title: ''
  type: Specification
  url: https://camaraproject.org/api-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSMA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camaraproject
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gsma/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gsma
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/gsma
- group: company
  title: ''
  type: Newsroom
  url: https://www.gsma.com/newsroom/
- group: other
  title: ''
  type: Services
  url: https://www.gsmaservices.com/
- group: other
  title: ''
  type: Membership
  url: https://www.gsma.com/get-involved/gsma-membership/
- group: agent
  href: https://artifacts.apis.io/gsma/well-known/gsma-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gsma-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gsma/well-known/gsma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gsma-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.gsma.com/security/
- group: build
  href: https://artifacts.apis.io/gsma/packages/gsma-packages.yml
  title: ''
  type: Packages
  url: packages/gsma-packages.yml
- group: build
  href: https://artifacts.apis.io/gsma/packages/gsma-packages.yml
  title: ''
  type: SDKs
  url: packages/gsma-packages.yml
- group: agent
  href: https://artifacts.apis.io/gsma/llms/gsma-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gsma-llms.txt
- group: design
  href: https://artifacts.apis.io/gsma/conformance/gsma-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gsma-conformance.yml
- group: design
  href: https://artifacts.apis.io/gsma/errors/gsma-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gsma-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gsma/lifecycle/gsma-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gsma-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/change-list.html
- group: auth
  href: https://artifacts.apis.io/gsma/scopes/gsma-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gsma-scopes.yml
- group: design
  href: https://artifacts.apis.io/gsma/conventions/gsma-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gsma-conventions.yml
- group: design
  href: https://artifacts.apis.io/gsma/conventions/gsma-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gsma-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gsma/changelog/gsma-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gsma-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/change-list.html
- group: start
  href: https://artifacts.apis.io/gsma/sandbox/gsma-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gsma-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gsma/data-model/gsma-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gsma-data-model.yml
- group: agent
  href: https://artifacts.apis.io/gsma/mcp/gsma-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gsma-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gsma/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gsma/asyncapi/gsma-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gsma-webhooks.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/api-service-definition.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mobilemoneyapi.io/sdks/getting-started/introduction.html
- group: operate
  title: ''
  type: Support
  url: https://developer.mobilemoneyapi.io/support/
- group: company
  title: ''
  type: Blog
  url: https://www.gsma.com/newsroom/
- group: start
  title: ''
  type: SignUp
  url: https://developer.mobilemoneyapi.io/signup/
- group: start
  title: ''
  type: Login
  url: https://developer.mobilemoneyapi.io/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gsma.com/aboutus/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsma.com/aboutus/legal/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://developer.mobilemoneyapi.io/faq/
- group: other
  title: ''
  type: Glossary
  url: https://developer.mobilemoneyapi.io/glossary/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mobilemoneyapi.io/
created: '2026-07-25'
description: 'The GSMA (GSM Association) is the London-headquartered global trade body for the mobile industry, representing roughly 750 mobile network operators and around 400 companies in the wider mobile ecosystem, and the organiser of MWC Barcelona. In telecom''s API value chain the GSMA is not a network operator and not an aggregator; it is the standards and commitment layer. Its GSMA Open Gateway initiative is the memorandum of understanding under which 69 operator groups, representing 78% of global mobile connections, commit to exposing a common set of network APIs, while the API specifications themselves are authored in the Linux Foundation''s CAMARA project. The GSMA''s API posture is unusually open for a standards body: its Open Gateway developer portal at open-gateway.gsma.com publishes 17 CAMARA OpenAPI 3.0.3 documents in full, without login, alongside a live public deployment map covering 607 launched API instances across 80 operators and 65 countries, and it runs a separate,
  fully open Mobile Money API developer portal with a downloadable OpenAPI 3.0.0 specification, SDKs, and use-case guides. The gates are real but narrow: the API sandbox requires a GitHub sign-in, the anti-fraud Scam Signal API is held in a private GSMA repository rather than in public CAMARA, and the commercial GSMA Services products (Device Check, IMEI Database, PathFinder, Disposable Number Check) are membership and contract gated with no public documentation. The GSMA runs no production network API endpoints of its own — every Open Gateway API is served by an operator or a channel partner such as Infobip, IPification, TMT iD, XConnect, or Singtel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-10-06'
name: GSMA
nav: Providers
network: true
overview: 'GSMA publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authorisation Codes API, Bills API, and 38 more. Tagged areas include Telecommunications, United Kingdom, Standards, Trade Association, and Network APIs.


  The GSMA catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GSMA''s developer surface includes authentication, documentation, sandbox, YouTube channel, changelog, API reference, getting-started guide, and 50 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: GSMA API Rules
  rule_count: 60
  severity_counts:
    error: 34
    hint: 0
    info: 4
    warn: 22
  slug: gsma-rules
scopes:
- name: Gsma Scopes
  scope_count: 30
  slug: gsma-scopes
  summary_line: 30 scopes
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 78.0
    discoverability: 73.2
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 48.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/gsma/gsma-2026-08-07T165856.png
security:
- kind: authentication
  name: Gsma Authentication
  slug: gsma-authentication
  summary_line: http/openIdConnect/unknown · 3 schemes
- kind: domain-security
  name: Gsma Domain Security
  slug: gsma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gsma Vulnerability Disclosure
  slug: gsma-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 6
skills:
- name: Charge a purchase to the mobile bill and refund it
  slug: gsma-carrier-billing-payment
- name: Verify where a device is and whether the identity behind it matches
  slug: gsma-device-location-and-kyc
- name: Run a mobile money transaction with correlation-id idempotency
  slug: gsma-mobile-money-transaction
- name: Verify a mobile number silently, with an SMS OTP fallback
  slug: gsma-number-verification
- name: Request and manage a prioritised network quality session
  slug: gsma-quality-on-demand-session
- name: Check a subscriber line for SIM-swap and device-swap fraud signals
  slug: gsma-sim-swap-fraud-check
slug: gsma
tags:
- Telecommunications
- United Kingdom
- Standards
- Trade Association
- Network APIs
- CAMARA
- Open Gateway
- Mobile Network Operators
- Identity Verification
- SIM Swap
- Mobile Money
- eSIM
- 5G
- Fraud Prevention
- Specification
- GSMA
website: https://www.gsma.com/
---
