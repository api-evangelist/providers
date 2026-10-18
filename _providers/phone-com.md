---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 171
  human_in_the_loop: 1
  name: Phone Com Agentic Access
  operation_count: 333
  slug: phone-com-agentic-access
  summary_line: 333 operations · 171 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 10 DLC registration is required for SMS messaging
  name: Phone Com 10 DLC API
  slug: phone-com-10-dlc-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Allows you to manage access tokens issued for your account.
  name: Phone Com Access Tokens API
  slug: phone-com-access-tokens-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Contact which can be used for different needs, such as ordering devices
  name: Phone Com Account Contacts API
  slug: phone-com-account-contacts-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: This page gives an overview of how to interact with your accounts.
  name: Phone Com Accounts API
  slug: phone-com-accounts-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Information about API usage statics.
  name: Phone Com API Endpoint Statistics API
  slug: phone-com-api-endpoint-statistics-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: We save API errors related to your account so you can analyze issues if for some reason you don't log error responses in your application
  name: Phone Com API Errors API
  slug: phone-com-api-errors-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Phone.com created the async-call-logs API endpoint to allow customers to download large amounts of call logs without encountering the normal Phone.com API Rate Limits. This service needs to be activat
  name: Phone Com Asynchronous Call Logs API
  slug: phone-com-asynchronous-call-logs-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: This service lists phone numbers that are available for purchase through Phone.com.
  name: Phone Com Available Phone Numbers API
  slug: phone-com-available-phone-numbers-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The Blocked Calls API allows users block incoming calls from specific phone numbers. If only a part of a telephone number is provided, calls with callers ID matching the pattern will be blocked. For e
  name: Phone Com Blocked Calls API
  slug: phone-com-blocked-calls-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The Call Logs API returns a list of call detail records for the account. The result includes the id, start time, creation time, caller ID, called number, direction of call, and duration in seconds. If
  name: Phone Com Call Logs API
  slug: phone-com-call-logs-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Aggregated calls statistics
  name: Phone Com Call Reports API
  slug: phone-com-call-reports-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: API users with Extension scope access token does not have access to the Phone Number API. This API helps user to retrieve available account phone numbers to be used as caller id via the /Calls API.
  name: Phone Com Caller IDs API
  slug: phone-com-caller-ids-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: This API places a call to the caller phone number (or caller extension ID). If that number (or extension) answers within the timeout period, then the callee DID (or extension) will be connected to the
  name: Phone Com Calls API
  slug: phone-com-calls-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Phone.com API supports OAuth 2.0 Authorization Framework, which enables a third-party application (client) to obtain limited access to HTTP API requests. This page describes how to use the /oauth/clie
  name: Phone Com Clients API
  slug: phone-com-clients-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Represents overview of your messaging history in messenger-like format.
  name: Phone Com Conversations API
  slug: phone-com-conversations-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Extension on your Phone.com account may have SIP devices associated with them. The Device API provides information about those SIP devices, such as the SIP credentials required.
  name: Phone Com Devices API
  slug: phone-com-devices-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Callbacks represent URLs on your side which will be called by our system when event occurs. Read more: https://github.com/phonedotcom/events-integration-doc'
  name: Phone Com Events Callbacks API
  slug: phone-com-events-callbacks-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Callback invocations statistics
  name: Phone Com Events Callbacks Health Status API
  slug: phone-com-events-callbacks-health-status-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Combined representation of listeners, callbacks, profiles and subscriptions. Read more: https://github.com/phonedotcom/events-integration-doc'
  name: Phone Com Events Integrations Overview API
  slug: phone-com-events-integrations-overview-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Listener is an entity that associates subscriptions with callbacks. Read more: https://github.com/phonedotcom/events-integration-doc'
  name: Phone Com Events Listeners API
  slug: phone-com-events-listeners-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Filters functionality. If no filters defined, than all events will be processed. If filters defined, events should match all of them.
  name: Phone Com Events Listeners Filters API
  slug: phone-com-events-listeners-filters-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Defines what kind of events should generate a callback. Read more: https://github.com/phonedotcom/events-integration-doc'
  name: Phone Com Events Listeners Subscriptions API
  slug: phone-com-events-listeners-subscriptions-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: A Profile allows to specify a notifications email for a callback. Notifications are emitted when there is a need to notify the callback owner of some issues like timeouts, or de-registration of the ca
  name: Phone Com Events Profiles API
  slug: phone-com-events-profiles-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: An Express Service Code is required when a customer calls Phone.com for support. With the following services, customer may retrieve the Express Service Code associated with his/her account
  name: Phone Com Express Service Codes API
  slug: phone-com-express-service-codes-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The entries in an extension's address book can be divided into any number of groups. This page gives an overview.
  name: Phone Com Extension Contact Groups API
  slug: phone-com-extension-contact-groups-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Each extension at Phone.com can have an address book with any number of contacts.
  name: Phone Com Extension Contacts API
  slug: phone-com-extension-contacts-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Your Phone.com account will have one or more extensions.
  name: Phone Com Extensions API
  slug: phone-com-extensions-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Phone.com customers can fax outbound documents via the Control Panel or API; They can also receive incoming fax into one of the Extension mailbox. The Fax API service allows users send a fax, list all
  name: Phone Com Fax API
  slug: phone-com-fax-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: AI-based help system
  name: Phone Com Help Requests API
  slug: phone-com-help-requests-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Invoices also knows as billing statements. "billing-api" scope is required for the token
  name: Phone Com Invoices API
  slug: phone-com-invoices-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: '[DEPRECATED; use Events Listeners] At the heart of every telephony system is the Events Engine. At Phone.com, our customers (and their call traffic) emit millions of events per day. These events play '
  name: Phone Com Listeners API
  slug: phone-com-listeners-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: With Live Receptionist and Phone.com, your business can now have its very own live answering service, adding versatility, flexibility, and availability to your company no matter the size.
  name: Phone Com Live Answer API
  slug: phone-com-live-answer-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Usage of live answer script by other Phone.com resources.
  name: Phone Com Live Answer Usage API
  slug: phone-com-live-answer-usage-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Information about available Live Answer vendors
  name: Phone Com Live Answer Vendor API
  slug: phone-com-live-answer-vendor-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Live Answer Vendor Tokens are required for some integrations
  name: Phone Com Live Answer Vendor Token API
  slug: phone-com-live-answer-vendor-token-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Your Phone.com account has two kinds of media that can be used in various ways: Hold Music and Greetings. Hold Music can be used in routes, queues, and anywhere the caller might be placed on hold. You'
  name: Phone Com Media API
  slug: phone-com-media-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Usage of media file by other Phone.com resources.
  name: Phone Com Media Usage API
  slug: phone-com-media-usage-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: We've all been on the consuming side of a phone menu before. You call a company and hear, 'Press '1' for Sales. Press '2' for Support. Press '0' for the operator.' With Phone.com you can create your o
  name: Phone Com Menus API
  slug: phone-com-menus-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Phone.com’s standard phone service lets you send and receive SMS/MMS messages using your Phone.com numbers. The Phone.com API extends this functionality, letting you send SMS/MMS messages from your ap
  name: Phone Com Messages API
  slug: phone-com-messages-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The OAuth 2.0 Authorization Framework enables a third-party application to obtain limited access to HTTP API requests which require an access token. This page describes how to use the /oauth/authoriza
  name: Phone Com OAuth API
  slug: phone-com-oauth-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: History of the orders of physical devices
  name: Phone Com Orders API
  slug: phone-com-orders-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Phone.com accepts credit card payment, and the Account Payment Methods API allows users to add, list, get, update and delete a credit card payment method. "billing-api" scope is required for the token
  name: Phone Com Payment Methods API
  slug: phone-com-payment-methods-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: API for payments
  name: Phone Com Payments API
  slug: phone-com-payments-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Allows to manage phone numbers reservations.
  name: Phone Com Phone Number Reservation API
  slug: phone-com-phone-number-reservation-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Your Phone.com account has one or more phone numbers registered to it.
  name: Phone Com Phone Numbers API
  slug: phone-com-phone-numbers-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: '[DEPRECATED] This interface allows you to try to obtain basic information about any phone number (CNAME, line type, etc)'
  name: Phone Com Phone Numbers Meta Information API
  slug: phone-com-phone-numbers-meta-information-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Price List
  name: Phone Com Price List API
  slug: phone-com-price-list-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Prices and taxes
  name: Phone Com Prices API
  slug: phone-com-prices-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Profile
  name: Phone Com Profile API
  slug: phone-com-profile-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Queues are used when you want to direct calls to a pool of phone numbers and/or extensions. A common utilization of queues is for Customer Service call centers. When a queue is configured on your phon
  name: Phone Com Queue Members API
  slug: phone-com-queue-members-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Queues are used when you want to direct calls to a pool of phone numbers and/or extensions. A common utilization of queues is for Customer Service call centers. When a queue is configured on your phon
  name: Phone Com Queues API
  slug: phone-com-queues-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The Account OAuth Clients API supports redirect-uri. Since an OAuth Client is created by a Phone.com admin who does not know what redirect uris should be assigned, API users may use the OAuth Client R
  name: Phone Com Redirect URIs API
  slug: phone-com-redirect-uris-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Routes, a.k.a. 'Call Handling Rules' or 'Presets', are used to tell Phone.com how to handle incoming phone calls. They can be used to connect your Phone.com phone number to an extension, a menu, a cal
  name: Phone Com Routes API
  slug: phone-com-routes-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: API for managing postponed (scheduled) API requests. "scheduled-requests" scope is required for the token.
  name: Phone Com Scheduled Requests API
  slug: phone-com-scheduled-requests-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Schedules are used at various places in your Phone.com account. A schedule can specify a recurring weekly pattern such as ''Monday through Friday'' or a single time period such as ''Thanksgiving Weekend '
  name: Phone Com Schedules API
  slug: phone-com-schedules-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: '[DEPRECATED; use Messages] Phone.com’s standard phone service lets you send and receive SMS messages using your Phone.com numbers. The Phone.com API extends this functionality, letting you send SMS me'
  name: Phone Com SMS API
  slug: phone-com-sms-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Account snapshots
  name: Phone Com Snapshots API
  slug: phone-com-snapshots-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: This page gives an overview of how to interact with your subaccounts. Subaccounts are the same as master accounts in terms of the functionality Phone.com supports. The main difference is that subaccou
  name: Phone Com Subaccounts API
  slug: phone-com-subaccounts-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: You can submit support request via API, it will be delivered to our API team
  name: Phone Com Support Requests API
  slug: phone-com-support-requests-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The System endpoints API from Phone Com — 2 operation(s) for system endpoints.
  name: Phone Com System endpoints API
  slug: phone-com-system-endpoints-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Transactions (charges, taxes, payments, etc.). "billing-api" scope is required for the token.
  name: Phone Com Transactions API
  slug: phone-com-transactions-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'SIP Trunks are used to connect your Phone.com account to your PBX. NOTE: SIP Trunking Customers Only -- Your Phone.com account must have SIP Trunking enabled in order to use any of our trunking featur'
  name: Phone Com Trunks API
  slug: phone-com-trunks-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Users functionality
  name: Phone Com User API
  slug: phone-com-user-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Endpoints for managing scheduled video conferences
  name: Phone Com Video Conferences API
  slug: phone-com-video-conferences-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: The Phone.com Video API allows an integrator to automate provisioning a complete cloud-based video conferencing system for a Phone.com account.
  name: Phone Com Video Config API
  slug: phone-com-video-config-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Token for integration with Video Conference service
  name: Phone Com Video Token API
  slug: phone-com-video-token-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: Video-users are associated with Phone.com extensions. A video user is a collection of a domain name for the bridge id, a business name, and a plan which affects the bridge capabilities in terms of max
  name: Phone Com Video Users API
  slug: phone-com-video-users-api
- baseURL: https://api.phone.com/v4
  baseurl_source: declared
  description: 'Phone.com’s standard phone service allows callers to leave a voicemail if the incoming call was not answered. The /voicemail services show a history of voicemail and allow users to download voicemail '
  name: Phone Com Voicemail API
  slug: phone-com-voicemail-api
artifact_total: 82
asyncapis:
- description: ''
  name: Phone Com Events Webhooks
  slug: phone-com-events-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/capabilities/phone-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/phone-com-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/agentic-access/phone-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/phone-com-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/rules/phone-com-rules.yml
  title: ''
  type: Spectral
  url: rules/phone-com-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/json-ld/phone-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/phone-com-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/vocabulary/phone-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/phone-com-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/errors/phone-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phone-com-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/hosts/phone-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phone-com-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/integrations/phone-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/phone-com-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/vendors/phone-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phone-com-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.phone.com/leadership/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.phone.com/feed/
- group: company
  title: ''
  type: Website
  url: https://phone.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.phone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phone.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.phone.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phone.com/aboutdevenv/aboutdevenvhome.html
- group: operate
  title: ''
  type: Support
  url: https://support.phone.com/
- group: company
  title: ''
  type: Blog
  url: https://www.phone.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phonedotcom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.phone.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.phone.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://my.phone.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phone.com/general-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phone.com/privacy-statement/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/packages/phone-com-packages.yml
  title: ''
  type: Packages
  url: packages/phone-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/packages/phone-com-packages.yml
  title: ''
  type: SDKs
  url: packages/phone-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/llms/phone-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phone-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/authentication/phone-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phone-com-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/scopes/phone-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/phone-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/conventions/phone-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phone-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/lifecycle/phone-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phone-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/lifecycle/phone-com-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/phone-com-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/security/phone-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phone-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/security/phone-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/phone-com-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/security/phone-com-trust-center.yml
  title: ''
  type: Compliance
  url: security/phone-com-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/well-known/phone-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phone-com-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/conformance/phone-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phone-com-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/mcp/phone-com-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/phone-com-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/asyncapi/phone-com-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/phone-com-events-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/data-model/phone-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phone-com-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Phone.com is a cloud business phone and unified communications provider for small and mid-sized businesses, offering VoIP calling, SMS/MMS, video conferencing, fax, and virtual phone numbers. Its developer platform is the JSON REST v4 API (codenamed "Phoenix") at api.phone.com, which gives programmatic control over accounts, extensions, devices, phone numbers, call routing (routes, menus, queues, schedules), media, messaging, and an event callback/listener webhook system. Authentication is OAuth 2.0. First-party SDKs are published for Go, Python, PHP, Android, and JavaScript. Surfaced as a portfolio company of Lightspeed Venture Partners and enriched into the API Evangelist network.
image: https://github.com/phonedotcom.png
json_schemas:
- name: Account
  property_count: 10
  slug: phone-com-account
- name: EventsOverview
  property_count: 6
  slug: phone-com-events-overview
- name: ExtensionContact
  property_count: 11
  slug: phone-com-extension-contact
- name: Extension
  property_count: 17
  slug: phone-com-extension
- name: LiveAnswer
  property_count: 14
  slug: phone-com-live-answer
- name: Route
  property_count: 3
  slug: phone-com-route
jsonld:
- class_count: 49
  name: Phone Com Context
  property_count: 184
  slug: phone-com-context
layout: provider
modified: '2026-10-06'
name: Phone Com
nav: Providers
network: true
overview: 'Phone Com publishes 68 API contracts indexed on the [APIs.io](https://apis.io/) network, including 10 DLC API, Access Tokens API, Account Contacts API, and 65 more. Tagged areas include Company, VoIP, Telephony, Business Phone, and SMS.


  The Phone Com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Phone Com''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Phone Com API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: phone-com-rules
scopes:
- name: Phone Com Scopes
  scope_count: 4
  slug: phone-com-scopes
  summary_line: 4 scopes · oauth2
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.9
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 68.4
    developer_ergonomics: 47.0
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 68
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/phone-com/refs/heads/main/screenshots/phone-com-2026-08-17T081209.png
security:
- kind: authentication
  name: Phone Com Authentication
  slug: phone-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Phone Com Domain Security
  slug: phone-com-domain-security
  summary_line: no transport/DNS hardening detected
- kind: trust-center
  name: Phone Com Trust Center
  slug: phone-com-trust-center
  summary_line: SOC 2 Type 2, HIPAA, PCI DSS
slug: phone-com
tags:
- Company
- VoIP
- Telephony
- Business Phone
- SMS
- Video Conferencing
- Communications
website: https://phone.com
---
