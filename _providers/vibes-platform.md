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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 73.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Vibes Platform Agentic Access
  operation_count: 22
  slug: vibes-platform-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 12
apis:
- description: The complete Vibes Platform REST API as Vibes publishes it — 48 paths and 75 operations across the Acquisition Campaign, Broadcast, Callback, Event, Event-Triggered Campaign, Incentive Code, Incentive
  name: Vibes Platform API
  slug: vibes-platform-api
- description: Vibes RCS for Business (RBM) API — check a device's RCS capabilities, send RCS agent messages and events, revoke an undelivered message, and manage agent tester devices. Authenticated with OAuth 2.0 c
  name: Vibes RCS Business Messaging API
  slug: vibes-rcs-business-messaging-api
- description: Manage acquisition campaigns for adding new subscribers.
  name: Vibes Platform Acquisition Campaigns API
  slug: vibes-platform-acquisition-campaigns-api
- description: Manage SMS and push notification broadcasts (message sends).
  name: Vibes Platform Broadcasts API
  slug: vibes-platform-broadcasts-api
- description: Register and manage callback endpoints for opt-in and delivery notifications.
  name: Vibes Platform Callbacks API
  slug: vibes-platform-callbacks-api
- description: Retrieve carrier information for mobile numbers.
  name: Vibes Platform Carrier Lookup API
  slug: vibes-platform-carrier-lookup-api
- description: Submit events that trigger SMS messages and push notifications.
  name: Vibes Platform Events API
  slug: vibes-platform-events-api
- description: Manage inbound message callbacks.
  name: Vibes Platform Inbound Messages API
  slug: vibes-platform-inbound-messages-api
- description: Send SMS and MMS messages.
  name: Vibes Platform Messages API
  slug: vibes-platform-messages-api
- description: Manage persons (subscribers) in the mobile contact book.
  name: Vibes Platform Persons API
  slug: vibes-platform-persons-api
- description: Manage subscription lists and subscriber memberships.
  name: Vibes Platform Subscription Lists API
  slug: vibes-platform-subscription-lists-api
- description: Manage mobile wallet passes (Apple Wallet, Google Pay).
  name: Vibes Platform Wallet Passes API
  slug: vibes-platform-wallet-passes-api
artifact_total: 47
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
- description: ''
  name: vibes-platform-mcp.yml
  slug: vibes-platform-mcpyml
modified: '2026-08-13'
name: Vibes Platform
nav: Providers
network: true
overview: 'Vibes Platform publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Vibes RCS Business Messaging API, Acquisition Campaigns API, and 10 more. Tagged areas include Mobile Marketing, Mobile Messaging, Push Notifications, SMS, and MMS.


  The Vibes Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Vibes Platform''s developer surface includes changelog, authentication, developer portal, documentation, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Vibes Platform Plans Pricing
  plan_count: 4
  slug: vibes-platform-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 4
  name: Vibes Platform Rate Limits
  slug: vibes-platform-rate-limits
rules:
- name: Vibes Platform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vibes-platform-jsonschema-spectral-rules
- name: Vibes Platform API Rules
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
  composite: 67.3
  delta: 26.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 75.2
    developer_ergonomics: 73.9
    discoverability: 81.5
    governance: 79.2
    operational_transparency: 52.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 59.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
