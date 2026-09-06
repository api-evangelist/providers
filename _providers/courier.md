---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Courier Agentic Access
  operation_count: 103
  slug: courier-agentic-access
  summary_line: 103 operations · 60 acting
api_count: 1
apis:
- baseURL: wss://realtime.courier.io
  baseurl_source: declared
  description: WebSocket service that delivers Inbox messages and message-state events (read, unread, opened, archived, clicked, mark-all-read, archive-all, archive-read) to authenticated users in real time.
  name: Courier Inbox Real-Time API
  slug: courier-inbox-real-time-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Audiences API from Courier — 3 operation(s) for audiences.
  name: Courier Audiences API
  slug: courier-audiences-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Audit Events API from Courier — 2 operation(s) for audit events.
  name: Courier Audit Events API
  slug: courier-audit-events-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Authentication API from Courier — 1 operation(s) for authentication.
  name: Courier Authentication API
  slug: courier-authentication-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Automations API from Courier — 3 operation(s) for automations.
  name: Courier Automations API
  slug: courier-automations-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Brands API from Courier — 2 operation(s) for brands.
  name: Courier Brands API
  slug: courier-brands-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Bulk API from Courier — 4 operation(s) for bulk.
  name: Courier Bulk API
  slug: courier-bulk-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Courier Create API from Courier — 4 operation(s) for courier create.
  name: Courier Courier Create API
  slug: courier-courier-create-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Device Tokens API from Courier — 2 operation(s) for device tokens.
  name: Courier Device Tokens API
  slug: courier-device-tokens-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Inbound API from Courier — 1 operation(s) for inbound.
  name: Courier Inbound API
  slug: courier-inbound-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Journeys API from Courier — 2 operation(s) for journeys.
  name: Courier Journeys API
  slug: courier-journeys-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Lists API from Courier — 5 operation(s) for lists.
  name: Courier Lists API
  slug: courier-lists-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Notification Templates API from Courier — 8 operation(s) for notification templates.
  name: Courier Notification Templates API
  slug: courier-notification-templates-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Providers API from Courier — 3 operation(s) for providers.
  name: Courier Providers API
  slug: courier-providers-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Routing Strategies API from Courier — 3 operation(s) for routing strategies.
  name: Courier Routing Strategies API
  slug: courier-routing-strategies-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Send API from Courier — 1 operation(s) for send.
  name: Courier Send API
  slug: courier-send-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Sent Messages API from Courier — 6 operation(s) for sent messages.
  name: Courier Sent Messages API
  slug: courier-sent-messages-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Tenants API from Courier — 4 operation(s) for tenants.
  name: Courier Tenants API
  slug: courier-tenants-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The Translations API from Courier — 1 operation(s) for translations.
  name: Courier Translations API
  slug: courier-translations-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The User Preferences API from Courier — 2 operation(s) for user preferences.
  name: Courier User Preferences API
  slug: courier-user-preferences-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The User Profiles API from Courier — 2 operation(s) for user profiles.
  name: Courier User Profiles API
  slug: courier-user-profiles-api
- baseURL: https://api.courier.com
  baseurl_source: declared
  description: The User Tenants API from Courier — 2 operation(s) for user tenants.
  name: Courier User Tenants API
  slug: courier-user-tenants-api
artifact_total: 55
asyncapis:
- description: AsyncAPI definition for Courier's Inbox WebSocket service used by the Courier client SDKs (JS, React, React Native, iOS, Android, Flutter, Web Components) to receive real-time, in-app notification eve
  name: Courier Inbox Real-Time API
  slug: courier-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Courier Audiences API
  slug: open-courier-audiences-api
- collection_type: open
  name: Courier Audiences Audit Events API
  slug: open-courier-audit-events-api
- collection_type: open
  name: Courier Audiences Authentication API
  slug: open-courier-authentication-api
- collection_type: open
  name: Courier Audiences Automations API
  slug: open-courier-automations-api
- collection_type: open
  name: Courier Audiences Brands API
  slug: open-courier-brands-api
- collection_type: open
  name: Courier Audiences Bulk API
  slug: open-courier-bulk-api
- collection_type: open
  name: Courier Audiences Courier Create API
  slug: open-courier-courier-create-api
- collection_type: open
  name: Courier Audiences Device Tokens API
  slug: open-courier-device-tokens-api
- collection_type: open
  name: Courier Audiences Inbound API
  slug: open-courier-inbound-api
- collection_type: open
  name: Courier Audiences Journeys API
  slug: open-courier-journeys-api
- collection_type: open
  name: Courier Audiences Lists API
  slug: open-courier-lists-api
- collection_type: open
  name: Courier Audiences Notification Templates API
  slug: open-courier-notification-templates-api
- collection_type: open
  name: Courier Audiences Providers API
  slug: open-courier-providers-api
- collection_type: open
  name: Courier Audiences Routing Strategies API
  slug: open-courier-routing-strategies-api
- collection_type: open
  name: Courier Audiences Send API
  slug: open-courier-send-api
- collection_type: open
  name: Courier Audiences Sent Messages API
  slug: open-courier-sent-messages-api
- collection_type: open
  name: Courier Audiences Tenants API
  slug: open-courier-tenants-api
- collection_type: open
  name: Courier Audiences Translations API
  slug: open-courier-translations-api
- collection_type: open
  name: Courier Audiences User Preferences API
  slug: open-courier-user-preferences-api
- collection_type: open
  name: Courier Audiences User Profiles API
  slug: open-courier-user-profiles-api
- collection_type: open
  name: Courier Audiences User Tenants API
  slug: open-courier-user-tenants-api
- collection_type: open
  name: Courier
  slug: open-courier
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/courier-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/courier-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/courier-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/courier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/courier-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trycourier
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trycourier
- group: company
  title: ''
  type: Website
  url: https://www.courier.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/courier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/courier-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/courier-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.courier.com/blog/feed
created: '2026-05-08'
description: Courier is a multi-channel notification API offering routing across email, SMS, push, chat, and in-app, with templates, preferences, and a no-code studio.
finops:
- name: Courier Finops
  service_category: Notifications
  slug: courier-finops
graphqls:
- description: Courier provides a native GraphQL API in addition to its REST API. The GraphQL endpoint is available at `https://api.courier.com/graphql` and supports querying and mutating notifications, messages, re
  name: Courier GraphQL API
  slug: courier-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/courier.png
layout: provider
modified: '2026-05-29'
name: Courier
nav: Providers
network: true
overview: 'Courier publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Inbox Real-Time API, Audiences API, Audit Events API, and 19 more. Tagged areas include Notification, Email, SMS, and Push.


  The Courier catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Courier''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Courier Plans Pricing
  plan_count: 1
  slug: courier-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Courier Rate Limits
  slug: courier-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Courier API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: courier-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 38.5
    catalog_earned_first_party: 0.0
    catalog_gap: 76.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 68.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/courier/refs/heads/main/screenshots/courier-2026-06-20T175109.png
security:
- kind: authentication
  name: Courier Authentication
  slug: courier-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Courier Domain Security
  slug: courier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Courier Trust Center
  slug: courier-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: courier
tags:
- Notification
- Email
- SMS
- Push
website: https://www.courier.com/
---
