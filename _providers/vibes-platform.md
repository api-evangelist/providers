---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Vibes Platform Agentic Access
  operation_count: 22
  slug: vibes-platform-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 10
apis:
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
artifact_total: 31
collections:
- collection_type: open
  name: Vibes Connect HTTP Message API
  slug: open-vibes-connect
- collection_type: open
  name: Vibes Platform API
  slug: open-vibes-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vibes-platform-agentic-access.yml
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
modified: '2026-05-19'
name: Vibes Platform
nav: Providers
network: true
overview: 'Vibes Platform publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Acquisition Campaigns API, Broadcasts API, Callbacks API, and 7 more. Tagged areas include Mobile Marketing, Mobile Messaging, Push Notifications, SMS, and MMS.


  The Vibes Platform catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vibes Platform''s developer surface includes authentication, developer portal, documentation, and 6 more developer resources.'
plans:
- name: Vibes Platform Plans Pricing
  plan_count: 3
  slug: vibes-platform-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
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
score:
  band: developing
  composite: 51.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 66.2
    developer_ergonomics: 28.3
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 51.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vibes-platform/refs/heads/main/screenshots/vibes-platform-2026-06-20T201014.png
security:
- kind: authentication
  name: Vibes Platform Authentication
  slug: vibes-platform-authentication
  summary_line: http · 1 scheme
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
