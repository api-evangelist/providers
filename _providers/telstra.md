---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Telstra Agentic Access
  operation_count: 13
  slug: telstra-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 13
apis:
- description: Send large scale mobile push notification campaigns to Android and iOS devices.
  name: Telstra Mobile Push Notifications API
  slug: telstra-mobile-push-notifications
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Request for access token to make the API request
  name: Telstra Access Token Request API
  slug: telstra-access-token-request-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The Authentication API from Telstra — 2 operation(s) for authentication.
  name: Telstra Authentication API
  slug: telstra-authentication-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: Telstra Check Device Swap API
  slug: telstra-check-device-swap-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The Check Subscriber Tenure API from Telstra — 1 operation(s) for check subscriber tenure.
  name: Telstra Check Subscriber Tenure API
  slug: telstra-check-subscriber-tenure-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The Field Workforce Partners API Operations API from Telstra — 10 operation(s) for field workforce partners api operations.
  name: Telstra Field Workforce Partners API Operations API
  slug: telstra-field-workforce-partners-api-operations-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The free trial numbers API from Telstra — 1 operation(s) for free trial numbers.
  name: Telstra free trial numbers API
  slug: telstra-free-trial-numbers-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The health check API from Telstra — 1 operation(s) for health check.
  name: Telstra health check API
  slug: telstra-health-check-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Operations to match a customer identity against the account data bound to their phone number.
  name: Telstra Match API
  slug: telstra-match-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The messages API from Telstra — 2 operation(s) for messages.
  name: Telstra Messages API
  slug: telstra-messages-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Bandwidth/plan modification operations
  name: Telstra Modify API
  slug: telstra-modify-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Request for access token to make the API request
  name: Telstra OIDC Access Token Request API
  slug: telstra-oidc-access-token-request-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Request authorisation grant
  name: Telstra OIDC Authentication Request API
  slug: telstra-oidc-authentication-request-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The Our website API from Telstra — 1 operation(s) for our website.
  name: Telstra Our website API
  slug: telstra-our-website-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Retrieve the outage status for a specific subu`rb and state
  name: Telstra Outage Service API
  slug: telstra-outage-service-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: Telstra Phone Number Verify API
  slug: telstra-phone-number-verify-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The Pricing API from Telstra — 1 operation(s) for pricing.
  name: Telstra Pricing API
  slug: telstra-pricing-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The reports API from Telstra — 3 operation(s) for reports.
  name: Telstra Reports API
  slug: telstra-reports-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Receive the last date in which the device of the end-user was swapped
  name: Telstra Retrieve Device Swap Date API
  slug: telstra-retrieve-device-swap-date-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The sender names API from Telstra — 1 operation(s) for sender names.
  name: Telstra sender names API
  slug: telstra-sender-names-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Retrieve services
  name: Telstra Services API
  slug: telstra-services-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: Fetch status of requests
  name: Telstra Status API
  slug: telstra-status-api
- baseURL: https://products.api.telstra.com/messaging/v3
  baseurl_source: declared
  description: The virtual numbers API from Telstra — 3 operation(s) for virtual numbers.
  name: Telstra virtual numbers API
  slug: telstra-virtual-numbers-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Send, retrieve, and check status of MMS messages.
  name: Telstra MMS API
  slug: telstra-mms-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Create, retrieve, and delete dedicated number subscriptions.
  name: Telstra Provisioning API
  slug: telstra-provisioning-api
- baseURL: https://tapi.telstra.com/v2
  baseurl_source: declared
  description: Send, retrieve, and check status of SMS messages.
  name: Telstra SMS API
  slug: telstra-sms-api
- baseURL: https://tapi.telstra.com/v1
  baseurl_source: declared
  description: Mobile number verification operations.
  name: Telstra Verification API
  slug: telstra-verification-api
artifact_total: 107
collections:
- collection_type: postman
  name: Telstra Messaging Authentication API
  slug: postman-telstra-authentication-api
- collection_type: postman
  name: Telstra Messaging Authentication HealthCheck API
  slug: postman-telstra-healthcheck-api
- collection_type: postman
  name: Telstra Messaging Authentication MMS API
  slug: postman-telstra-mms-api
- collection_type: postman
  name: Telstra Messaging Authentication Provisioning API
  slug: postman-telstra-provisioning-api
- collection_type: postman
  name: Telstra Messaging Authentication SMS API
  slug: postman-telstra-sms-api
- collection_type: postman
  name: Telstra Messaging Authentication Verification API
  slug: postman-telstra-verification-api
- collection_type: open
  name: Telstra Messaging Authentication API
  slug: open-telstra-authentication-api
- collection_type: open
  name: Telstra Messaging Authentication HealthCheck API
  slug: open-telstra-healthcheck-api
- collection_type: open
  name: Telstra Messaging API
  slug: open-telstra-messaging-api
- collection_type: open
  name: Telstra Messaging Authentication MMS API
  slug: open-telstra-mms-api
- collection_type: open
  name: Telstra Mobile Number Verification API
  slug: open-telstra-mobile-number-verification-api
- collection_type: open
  name: Telstra Messaging Authentication Provisioning API
  slug: open-telstra-provisioning-api
- collection_type: open
  name: Telstra Messaging Authentication SMS API
  slug: open-telstra-sms-api
- collection_type: open
  name: Telstra Messaging Authentication Verification API
  slug: open-telstra-verification-api
common:
- group: auth
  href: https://artifacts.apis.io/telstra/well-known/telstra-tdev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/telstra-tdev-security.txt
- group: other
  href: https://artifacts.apis.io/telstra/capabilities/telstra-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/telstra-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/telstra/well-known/telstra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/telstra-well-known.yml
- group: design
  href: https://artifacts.apis.io/telstra/rules/telstra-rules.yml
  title: ''
  type: Spectral
  url: rules/telstra-rules.yml
- group: design
  href: https://artifacts.apis.io/telstra/rules/telstra-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/telstra-jsonschema-spectral-rules.yml
- group: agent
  href: https://artifacts.apis.io/telstra/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/telstra/data-model/telstra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/telstra-data-model.yml
- group: design
  href: https://artifacts.apis.io/telstra/conventions/telstra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/telstra-conventions.yml
- group: start
  href: https://artifacts.apis.io/telstra/sandbox/telstra-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/telstra-sandbox.yml
- group: design
  href: https://artifacts.apis.io/telstra/lifecycle/telstra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/telstra-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/telstra/errors/telstra-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/telstra-error-codes.yml
- group: design
  href: https://artifacts.apis.io/telstra/errors/telstra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/telstra-problem-types.yml
- group: design
  href: https://artifacts.apis.io/telstra/conformance/telstra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/telstra-conformance.yml
- group: other
  href: https://artifacts.apis.io/telstra/overlays/telstra-bandwidth-and-plan-modification-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/telstra-bandwidth-and-plan-modification-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/telstra/hosts/telstra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telstra-hosts.yml
- group: build
  href: https://artifacts.apis.io/telstra/integrations/telstra-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/telstra-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/telstra/vendors/telstra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telstra-vendors.yml
- group: build
  href: https://artifacts.apis.io/telstra/packages/telstra-packages.yml
  title: ''
  type: Packages
  url: packages/telstra-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.telstra.com.au
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/telstra/overview
- group: agent
  href: https://artifacts.apis.io/telstra/agentic-access/telstra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/telstra-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/telstra/security/telstra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telstra-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/telstra/authentication/telstra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/telstra-authentication.yml
- group: auth
  href: https://artifacts.apis.io/telstra/scopes/telstra-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/telstra-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://dev.telstra.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.telstra.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://dev.telstra.com/apis/messaging-api/Endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.telstra.com/apis/messaging-api/Tutorials
- group: commercial
  title: ''
  type: Pricing
  url: https://dev.telstra.com/apis/messaging-api/Pricing
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/20937769-0dca2b10-fdeb-4508-a655-843f8ad4de15?action=collection%2Fimport
- group: start
  title: ''
  type: Signup
  url: https://dev.telstra.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telstra
- group: operate
  title: ''
  type: StatusPage
  url: https://dev.telstra.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telstra.com.au/customer-terms/business-government
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telstra.com.au/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telstra
- group: company
  title: ''
  type: Blog
  url: https://dev.telstra.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.telstra.com.au/exchange/news
- group: operate
  title: ''
  type: Support
  url: https://dev.telstra.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.telstra.com.au/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/telstra
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-Java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/telstra/MessagingAPI-SDK-Go
- group: commercial
  title: ''
  type: License
  url: https://github.com/telstra/tdev-doc-license
- group: build
  title: ''
  type: Tools
  url: https://github.com/telstra/Cat-1-Development-Kit
- group: build
  title: ''
  type: Tools
  url: https://github.com/telstra/Cat-M1-Dev-Board
- group: commercial
  href: https://artifacts.apis.io/telstra/plans/telstra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/telstra-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/telstra/rate-limits/telstra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/telstra-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/telstra/finops/telstra-finops.yml
  title: ''
  type: FinOps
  url: finops/telstra-finops.yml
- group: design
  href: https://artifacts.apis.io/telstra/rules/telstra-rules.yml
  title: ''
  type: SpectralRuleset
  url: rules/telstra-rules.yml
- group: design
  href: https://artifacts.apis.io/telstra/vocabulary/telstra-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/telstra-vocabulary.yml
created: '2026-05-25T00:00:00.000Z'
description: Telstra is Australia's largest telecommunications and mobile network operator, providing fixed broadband, mobile voice and data, enterprise networking, and IoT connectivity across Australia and into Asia. Telstra exposes a developer programme at dev.telstra.com fronting carrier-grade Messaging (SMS / MMS) and Mobile Number Verification APIs, with official SDKs in Python, Node.js, Java, .NET, and Go, and Arduino libraries for the Telstra Cat-1 and Cat-M1 IoT development kits. The dev.telstra.com catalogue also lists SIM Swap, Device Swap, KYC Match, KYC Tenure, Mobile Push Notifications, Bandwidth and Plan Modification, IoT Connectivity Service and Telstra Cloud Sight APIs, with a public API status page. APIs are reached at tapi.telstra.com behind OAuth 2.0 client credentials with the NSMS or MNV scopes.
examples:
- key_count: 2
  name: Telstra Create Subscription Example
  slug: telstra-create-subscription-example
- key_count: 2
  name: Telstra Oauth Token Example
  slug: telstra-oauth-token-example
- key_count: 2
  name: Telstra Send Sms Example
  slug: telstra-send-sms-example
features:
- SMS messaging (single, multi-recipient) over the Telstra mobile network
- MMS messaging with multipart payloads (image, audio, video, SMIL, vCard)
- Inbound replies on Telstra-provisioned dedicated virtual numbers
- Delivery status notifications via push callbacks (notifyURL) and pull status endpoint
- Scheduled delivery and validity-period controls
- Priority message flag and per-message user reference
- OAuth 2.0 client credentials grant with NSMS scope (3599 second bearer tokens)
- Free Trial tier with Telstra-supplied trial numbers and whitelisted recipients
- Commercial Paid tier with negotiated per-message pricing and SLA
- International SMS reach beyond Australia
- Official SDKs in Python, Node.js, Java, .NET, and Go
- Service healthchecks for SMS and MMS surfaces
- Mobile Number Verification — silent MSISDN match on the Telstra data network (separate API)
- Arduino development kits for Cat-1 and Cat-M1 IoT modules on the Telstra network
finops:
- has_sources: true
  method: derived
  name: Telstra Finops
  primary_unit: ''
  service_category: ''
  slug: telstra-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telstra.png
json_schemas:
- name: AFModifyBandwidthRequest
  property_count: 1
  slug: telstra-afmodify-bandwidth-request
- name: AppointmentSlotEnquiryRequest
  property_count: 2
  slug: telstra-appointment-slot-enquiry-request
- name: CheckDeviceSwapInfo
  property_count: 1
  slug: telstra-check-device-swap-info
- name: CheckSimSwapInfo
  property_count: 1
  slug: telstra-check-sim-swap-info
- name: CreateCheckDeviceSwap
  property_count: 2
  slug: telstra-create-check-device-swap
- name: CreateCheckSimSwap
  property_count: 2
  slug: telstra-create-check-sim-swap
- name: CreateDeviceSwapDate
  property_count: 1
  slug: telstra-create-device-swap-date
- name: CreateSimSwapDate
  property_count: 1
  slug: telstra-create-sim-swap-date
- name: DeviceSwapInfo
  property_count: 2
  slug: telstra-device-swap-info
- name: FetchStatusResponse
  property_count: 8
  slug: telstra-fetch-status-response
- name: GetPartnerSuccessResponse
  property_count: 6
  slug: telstra-get-partner-success-response
- name: GetServiceSimsResponse
  property_count: 2
  slug: telstra-get-service-sims-response
- name: KYC_MatchRequestBody
  property_count: 20
  slug: telstra-kyc-match-request-body
- name: KYC_MatchResponse
  property_count: 32
  slug: telstra-kyc-match-response
- name: ListPriceResponse
  property_count: 2
  slug: telstra-list-price-response
- name: Telstra Message
  property_count: 15
  slug: telstra-message
- name: ModifyBandwidthRequest
  property_count: 1
  slug: telstra-modify-bandwidth-request
- name: ModifyBandwidthResponse
  property_count: 7
  slug: telstra-modify-bandwidth-response
- name: NumberVerificationMatchResponse
  property_count: 1
  slug: telstra-number-verification-match-response
- name: NumberVerificationRequestBody
  property_count: 2
  slug: telstra-number-verification-request-body
- name: OAuthResponse
  property_count: 3
  slug: telstra-oauth-response
- name: OutageStatusResponse
  property_count: 7
  slug: telstra-outage-status-response
- name: RefernceDataSuccessResponse
  property_count: 9
  slug: telstra-refernce-data-success-response
- name: RetrieveTaskListSuccessResponse
  property_count: 9
  slug: telstra-retrieve-task-list-success-response
- name: ServiceSim
  property_count: 38
  slug: telstra-service-sim
- name: ServicesPage
  property_count: 6
  slug: telstra-services-page
- name: SimSwapInfo
  property_count: 1
  slug: telstra-sim-swap-info
- name: Telstra Subscription
  property_count: 5
  slug: telstra-subscription
- name: TaskRetrieveSuccessResponse
  property_count: 9
  slug: telstra-task-retrieve-success-response
- name: TenureInfo
  property_count: 2
  slug: telstra-tenure-info
- name: Tenure
  property_count: 2
  slug: telstra-tenure
- name: UpdateTaskInput
  property_count: 2
  slug: telstra-update-task-input
json_structures:
- name: Telstra Message Structure
  property_count: 0
  slug: telstra-message-structure
jsonld:
- class_count: 0
  name: Telstra Context
  property_count: 5
  slug: telstra-context
layout: provider
modified: '2026-10-20'
name: Telstra
nav: Providers
network: true
overview: 'Telstra publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Token Request API, Authentication API, Check Device Swap API, and 24 more. Tagged areas include Telecommunications, Mobile, Messaging, SMS, and MMS.


  The Telstra catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telstra''s developer surface includes sandbox, authentication, developer portal, documentation, API reference, getting-started guide, pricing, and 47 more developer resources.'
plans:
- name: Telstra Plans Pricing
  plan_count: 11
  slug: telstra-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Telstra Rate Limits
  slug: telstra-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Telstra — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: telstra-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Telstra API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: telstra-rules
scopes:
- name: Telstra Scopes
  scope_count: 12
  slug: telstra-scopes
  summary_line: 12 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 38
    catalog_earned: 82.0
    catalog_earned_first_party: 24.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 65.8
    contract_governance: 45.5
    contract_quality: 64.5
    developer_ergonomics: 69.6
    discoverability: 63.4
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 45.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/telstra/telstra-2026-06-20T195052.png
security:
- kind: authentication
  name: Telstra Authentication
  slug: telstra-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Telstra Domain Security
  slug: telstra-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 6
skills:
- name: book-a-field-appointment
  slug: telstra-book-a-field-appointment
- name: check-sim-and-device-swap-risk
  slug: telstra-check-sim-and-device-swap-risk
- name: match-customer-identity
  slug: telstra-match-customer-identity
- name: modify-service-bandwidth
  slug: telstra-modify-service-bandwidth
- name: send-an-sms-or-mms
  slug: telstra-send-an-sms-or-mms
- name: verify-a-mobile-number
  slug: telstra-verify-a-mobile-number
slug: telstra
tags:
- Telecommunications
- Mobile
- Messaging
- SMS
- MMS
- Networks
- Australia
- Verification
website: https://www.telstra.com.au
---
