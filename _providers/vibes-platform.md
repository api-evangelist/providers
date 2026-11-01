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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 53
  human_in_the_loop: 1
  name: Vibes Platform Agentic Access
  operation_count: 106
  slug: vibes-platform-agentic-access
  summary_line: 106 operations · 53 acting · 1 human-in-the-loop
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
artifact_total: 68
asyncapis:
- description: ''
  name: Vibes Platform Webhooks
  slug: vibes-platform-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/vibes-platform/finops/vibes-platform-finops.yml
  title: ''
  type: FinOps
  url: finops/vibes-platform-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vibes.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/vibes-platform/capabilities/vibes-platform-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vibes-platform-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/vibes-platform/overlays/vibes-platform-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vibes-platform-platform-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/vibes-platform/overlays/vibes-platform-rcs-business-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vibes-platform-rcs-business-messaging-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/vibes-platform/scopes/vibes-platform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vibes-platform-scopes.yml
- group: agent
  href: https://artifacts.apis.io/vibes-platform/agentic-access/vibes-platform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vibes-platform-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/vibes-platform/packages/vibes-platform-packages.yml
  title: ''
  type: Packages
  url: packages/vibes-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/vibes-platform/packages/vibes-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/vibes-platform-packages.yml
- group: agent
  href: https://artifacts.apis.io/vibes-platform/llms/vibes-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vibes-platform-llms.txt
- group: design
  href: https://artifacts.apis.io/vibes-platform/conventions/vibes-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vibes-platform-conventions.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/conventions/vibes-platform-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vibes-platform-conventions.yml
- group: operate
  href: https://artifacts.apis.io/vibes-platform/rate-limits/vibes-platform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vibes-platform-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vibes-platform/plans/vibes-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vibes-platform-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/errors/vibes-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vibes-platform-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/lifecycle/vibes-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vibes-platform-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/vibes-platform/changelog/vibes-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vibes-platform-changelog.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/conformance/vibes-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vibes-platform-conformance.yml
- group: auth
  href: https://artifacts.apis.io/vibes-platform/conformance/vibes-platform-conformance.yml
  title: ''
  type: Compliance
  url: conformance/vibes-platform-conformance.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/data-model/vibes-platform-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vibes-platform-data-model.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/components/vibes-platform-components.yml
  title: ''
  type: Components
  url: components/vibes-platform-components.yml
- group: design
  href: https://artifacts.apis.io/vibes-platform/asyncapi/vibes-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vibes-platform-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/vibes-platform/mcp/vibes-platform-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vibes-platform-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vibes-platform/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/vibes-platform/security/vibes-platform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vibes-platform-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vibes-platform/security/vibes-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vibes-platform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vibes-platform/authentication/vibes-platform-authentication.yml
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
- has_sources: true
  method: derived
  name: Vibes Platform Finops
  primary_unit: subscription
  service_category: ''
  slug: vibes-platform-finops
  template: false
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
modified: '2026-10-06'
name: Vibes Platform
nav: Providers
network: true
overview: 'Vibes Platform publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Acquisition Campaigns API, Broadcasts API, Callbacks API, and 27 more. Tagged areas include Mobile Marketing, Mobile Messaging, Push Notifications, SMS, and MMS.


  The Vibes Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Vibes Platform''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, support, and 33 more developer resources.'
plans:
- name: Vibes Platform Plans Pricing
  plan_count: 4
  slug: vibes-platform-plans-pricing
- name: Vibes Platform Price Estimates
  plan_count: 0
  slug: vibes-platform-price-estimates
random_paper: 11
rate_limits:
- limit_count: 4
  name: Vibes Platform Rate Limits
  slug: vibes-platform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Vibes Platform — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vibes-platform-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 54
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
  composite: 67.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 79.5
    catalog_earned_first_party: 24.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 63.7
    developer_ergonomics: 66.1
    discoverability: 71.4
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.0
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
    score: 35.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vibes-platform/vibes-platform-2026-06-20T201014.png
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
skill_count: 4
skills:
- name: vibes-platform-manage-subscriber
  slug: vibes-platform-manage-subscriber
- name: vibes-platform-register-callbacks
  slug: vibes-platform-register-callbacks
- name: vibes-platform-send-broadcast
  slug: vibes-platform-send-broadcast
- name: vibes-platform-wallet-campaign
  slug: vibes-platform-wallet-campaign
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
