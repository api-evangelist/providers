---
access_model:
  confidence: high
  label: Paid · Sales-assisted onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.vibes.com/pricing
  - plans
  - authentication
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Vibes Platform Agentic Access
  operation_count: 22
  slug: vibes-platform-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 5
apis:
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage acquisition campaigns for adding new subscribers.
  name: Vibes Platform Acquisition Campaigns API
  slug: vibes-platform-acquisition-campaigns-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage SMS and push notification broadcasts (message sends).
  name: Vibes Platform Broadcasts API
  slug: vibes-platform-broadcasts-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Register and manage callback endpoints for opt-in and delivery notifications.
  name: Vibes Platform Callbacks API
  slug: vibes-platform-callbacks-api
- baseURL: https://messageapi.vibesapps.com
  baseurl_source: declared
  description: Retrieve carrier information for mobile numbers.
  name: Vibes Platform Carrier Lookup API
  slug: vibes-platform-carrier-lookup-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Submit events that trigger SMS messages and push notifications.
  name: Vibes Platform Events API
  slug: vibes-platform-events-api
- baseURL: https://messageapi.vibesapps.com
  baseurl_source: declared
  description: Manage inbound message callbacks.
  name: Vibes Platform Inbound Messages API
  slug: vibes-platform-inbound-messages-api
- baseURL: https://messageapi.vibesapps.com
  baseurl_source: declared
  description: Send SMS and MMS messages.
  name: Vibes Platform Messages API
  slug: vibes-platform-messages-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage persons (subscribers) in the mobile contact book.
  name: Vibes Platform Persons API
  slug: vibes-platform-persons-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage subscription lists and subscriber memberships.
  name: Vibes Platform Subscription Lists API
  slug: vibes-platform-subscription-lists-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage mobile wallet passes (Apple Wallet, Google Pay).
  name: Vibes Platform Wallet Passes API
  slug: vibes-platform-wallet-passes-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Acquisition Campaign API API from Vibes Platform — 3 operation(s) for acquisition campaign api.
  name: Vibes Platform Acquisition Campaign API
  slug: vibes-platform-acquisition-campaign-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Define the design and content of the Google Wallet (Android) pass for a wallet campaign. Each campaign has a single Google Wallet template whose fields map to Google Wallet pass concepts. See the Goog
  name: Vibes Platform Android Wallet Templates API
  slug: vibes-platform-android-wallet-templates-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Authentication API from Vibes Platform — 1 operation(s) for authentication.
  name: Vibes Platform Authentication API
  slug: vibes-platform-authentication-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Broadcast API API from Vibes Platform — 3 operation(s) for broadcast api.
  name: Vibes Platform Broadcast API
  slug: vibes-platform-broadcast-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Callback API API from Vibes Platform — 3 operation(s) for callback api.
  name: Vibes Platform Callback API
  slug: vibes-platform-callback-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Event API API from Vibes Platform — 1 operation(s) for event api.
  name: Vibes Platform Event API
  slug: vibes-platform-event-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Event-Triggered Campaign API API from Vibes Platform — 2 operation(s) for event-triggered campaign api.
  name: Vibes Platform Event-Triggered Campaign API
  slug: vibes-platform-event-triggered-campaign-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Incentive Code API API from Vibes Platform — 4 operation(s) for incentive code api.
  name: Vibes Platform Incentive Code API
  slug: vibes-platform-incentive-code-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Incentive Pool API API from Vibes Platform — 2 operation(s) for incentive pool api.
  name: Vibes Platform Incentive Pool API
  slug: vibes-platform-incentive-pool-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Define the design and content of the Apple Wallet (iOS) pass for a wallet campaign. Each campaign has a single Apple Wallet (passbook) template whose fields map to PassKit pass concepts. See the Apple
  name: Vibes Platform iOS Wallet Templates API
  slug: vibes-platform-ios-wallet-templates-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Person API API from Vibes Platform — 4 operation(s) for person api.
  name: Vibes Platform Person API
  slug: vibes-platform-person-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Push Device Manager API API from Vibes Platform — 4 operation(s) for push device manager api.
  name: Vibes Platform Push Device Manager API
  slug: vibes-platform-push-device-manager-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The RCS Business Messaging API from Vibes Platform — 6 operation(s) for rcs business messaging.
  name: Vibes Platform RCS Business Messaging API
  slug: vibes-platform-rcs-business-messaging-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Source Code API API from Vibes Platform — 1 operation(s) for source code api.
  name: Vibes Platform Source Code API
  slug: vibes-platform-source-code-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Subscription API API from Vibes Platform — 4 operation(s) for subscription api.
  name: Vibes Platform Subscription API
  slug: vibes-platform-subscription-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: The Subscription List API API from Vibes Platform — 4 operation(s) for subscription list api.
  name: Vibes Platform Subscription List API
  slug: vibes-platform-subscription-list-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: 'Manage mobile wallet campaigns and the individual wallet items (passes) issued from them. A wallet campaign is the container for a single offer, loyalty card, or event ticket program; it owns the iOS '
  name: Vibes Platform Wallet Campaign API
  slug: vibes-platform-wallet-campaign-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Configure the branded "Add to Wallet" landing page shown to end users for a wallet campaign, including its image, heading, colors, and language.
  name: Vibes Platform Wallet Location Selector API
  slug: vibes-platform-wallet-location-selector-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Send push-style messages to the holders of a wallet campaign's passes and review messages that have already been sent. Messages can be targeted to specific recipients with filters (for example, by tok
  name: Vibes Platform Wallet Messaging API
  slug: vibes-platform-wallet-messaging-api-api
- baseURL: https://public-api.vibescm.com
  baseurl_source: declared
  description: Manage the store locations attached to a wallet campaign. Locations drive geofenced lock-screen notifications that remind pass holders about a nearby store.
  name: Vibes Platform Wallet Store Locations API
  slug: vibes-platform-wallet-store-locations-api-api
artifact_total: 65
asyncapis:
- description: ''
  name: Vibes Platform Webhooks
  slug: vibes-platform-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vibes Connect HTTP Message API
  slug: open-vibes-connect
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns API
  slug: open-vibes-platform-acquisition-campaigns-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Broadcasts API
  slug: open-vibes-platform-broadcasts-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Callbacks API
  slug: open-vibes-platform-callbacks-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Carrier Lookup API
  slug: open-vibes-platform-carrier-lookup-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Events API
  slug: open-vibes-platform-events-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Inbound Messages API
  slug: open-vibes-platform-inbound-messages-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Messages API
  slug: open-vibes-platform-messages-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Persons API
  slug: open-vibes-platform-persons-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Subscription Lists API
  slug: open-vibes-platform-subscription-lists-api
- collection_type: open
  name: Vibes Connect HTTP Message Acquisition Campaigns Wallet Passes API
  slug: open-vibes-platform-wallet-passes-api
- collection_type: open
  name: Vibes Platform API
  slug: open-vibes-platform
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vibes-platform-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vibes-platform-platform-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vibes-platform-rcs-business-messaging-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vibes-platform-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vibes-platform-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/vibes-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vibes-platform-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vibes-platform-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/vibes-platform-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vibes-platform-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vibes-platform-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vibes-platform-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vibes-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vibes-platform-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vibes-platform-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vibes-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vibes-platform-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vibes-platform-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/vibes-platform-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vibes-platform-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vibes-platform-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vibes-platform-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vibes-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vibes-platform-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer-platform.vibes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-platform.vibes.com/reference/our-apis
- group: start
  title: ''
  type: Portal
  url: https://developer-aggregation.vibes.com
- group: start
  title: ''
  type: Portal
  url: https://developer-rbm.vibes.com/
- group: company
  title: ''
  type: Website
  url: https://www.vibes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-platform.vibes.com/reference/our-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-platform.vibes.com/docs/terminology
- group: operate
  title: ''
  type: Support
  url: https://developer-aggregation.vibes.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://www.vibes.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vibes.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vibes.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vibes.com/company/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vibes
created: '2024-11-14'
description: Vibes is a mobile engagement platform that provides APIs for SMS messaging, push notifications, RCS for Business, and mobile marketing campaigns. The platform APIs support broadcast messaging, event-triggered messages, acquisition workflows, subscription list management, wallet pass management, and callback notifications for opt-ins and delivery status. Vibes operates as a Tier 1 provider with direct carrier connections in the US and Canada.
examples:
- key_count: 2
  name: Vibes Connect Sendsmsmessage Example
  slug: vibes-connect-sendSmsMessage-example
- key_count: 2
  name: Vibes Platform Addparticipant Example
  slug: vibes-platform-addParticipant-example
- key_count: 2
  name: Vibes Platform Createbroadcast Example
  slug: vibes-platform-createBroadcast-example
- key_count: 2
  name: Vibes Platform Createevent Example
  slug: vibes-platform-createEvent-example
- key_count: 2
  name: Vibes Platform Listbroadcasts Example
  slug: vibes-platform-listBroadcasts-example
finops:
- name: Vibes Platform Finops
  service_category: API
  slug: vibes-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vibes-platform.png
json_schemas:
- name: Broadcast
  property_count: 10
  slug: vibes-platform-broadcast
- name: Person
  property_count: 5
  slug: vibes-platform-person
- name: Subscription List
  property_count: 5
  slug: vibes-platform-subscription-list
json_structures:
- name: Vibes Platform Broadcast Structure
  property_count: 0
  slug: vibes-platform-broadcast-structure
jsonld:
- class_count: 38
  name: Vibes Platform Context
  property_count: 4
  slug: vibes-platform-context
layout: provider
mcp_servers:
- description: Vibes publishes NO Model Context Protocol server. This file is a DERIVED CANDIDATE tool surface, computed from the operations in Vibes' own published OpenAPI so the shape of an agent-facing Vibes is l
  name: Vibes Platform MCP Server
  slug: vibes-platform-mcp-server
modified: '2026-08-13'
name: Vibes Platform
nav: Providers
network: true
overview: 'Vibes Platform publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Acquisition Campaigns API, Broadcasts API, Callbacks API, and 27 more. Tagged areas include Mobile Marketing, Mobile Messaging, Push Notifications, SMS, and MMS.


  The Vibes Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Vibes Platform''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, support, and 31 more developer resources.'
plans:
- name: Vibes Platform Plans Pricing
  plan_count: 4
  slug: vibes-platform-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Vibes Platform Rate Limits
  slug: vibes-platform-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vibes Platform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vibes-platform-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Vibes Platform API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 11
  slug: vibes-platform-rules
scopes:
- name: Vibes Platform Scopes
  scope_count: 1
  slug: vibes-platform-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 32
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 67.5
    developer_ergonomics: 61.3
    discoverability: 57.4
    governance: 31.8
    operational_transparency: 76.3
  previous_composite: 68.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vibes-platform/refs/heads/main/screenshots/vibes-platform-2026-06-20T201014.png
security:
- kind: authentication
  name: Vibes Platform Authentication
  slug: vibes-platform-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vibes Platform Domain Security
  slug: vibes-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vibes Platform Trust Center
  slug: vibes-platform-trust-center
  summary_line: SOC 2, GDPR
slug: vibes-platform
tags:
- Mobile Marketing
- Mobile Messaging
- Push Notifications
- SMS
- MMS
- Broadcast Messaging
- Acquisition Campaigns
- Subscription Management
- Wallet Passes
- RCS
website: https://www.vibes.com/
---
