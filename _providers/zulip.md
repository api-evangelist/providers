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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 113
  human_in_the_loop: 2
  name: Zulip Agentic Access
  operation_count: 161
  slug: zulip-agentic-access
  summary_line: 161 operations · 113 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Zulip REST API powers the Zulip web and mobile apps. It provides programmatic access to messages, streams, users, organizations, and all other Zulip functionality. Anything you can do in Zulip, yo
  name: Zulip REST API
  slug: rest-api
- description: The Zulip Events API delivers real-time updates from a Zulip server to a client via an HTTPS long-poll. Clients register an event queue via POST /api/v1/register, then call GET /api/v1/events with the
  name: Zulip Events API
  slug: events-api
- description: Zulip supports both incoming webhooks (allowing third-party services to push data to Zulip) and outgoing webhooks (allowing Zulip to send HTTP POST payloads to external services when messages are sent
  name: Zulip Webhooks
  slug: webhooks
- description: The authentication API from Zulip — 4 operation(s) for authentication.
  name: Zulip authentication API
  slug: zulip-authentication-api
- description: The bots API from Zulip — 1 operation(s) for bots.
  name: Zulip bots API
  slug: zulip-bots-api
- description: The channels API from Zulip — 23 operation(s) for channels.
  name: Zulip channels API
  slug: zulip-channels-api
- description: The drafts API from Zulip — 4 operation(s) for drafts.
  name: Zulip drafts API
  slug: zulip-drafts-api
- description: The invites API from Zulip — 5 operation(s) for invites.
  name: Zulip invites API
  slug: zulip-invites-api
- description: The messages API from Zulip — 16 operation(s) for messages.
  name: Zulip messages API
  slug: zulip-messages-api
- description: The mobile API from Zulip — 6 operation(s) for mobile.
  name: Zulip mobile API
  slug: zulip-mobile-api
- description: The navigation_views API from Zulip — 2 operation(s) for navigation_views.
  name: Zulip navigation_views API
  slug: zulip-navigation-views-api
- description: The real_time_events API from Zulip — 4 operation(s) for real_time_events.
  name: Zulip real_time_events API
  slug: zulip-real-time-events-api
- description: The reminders API from Zulip — 2 operation(s) for reminders.
  name: Zulip reminders API
  slug: zulip-reminders-api
- description: The scheduled_messages API from Zulip — 2 operation(s) for scheduled_messages.
  name: Zulip scheduled_messages API
  slug: zulip-scheduled-messages-api
- description: The server_and_organizations API from Zulip — 16 operation(s) for server_and_organizations.
  name: Zulip server_and_organizations API
  slug: zulip-server-and-organizations-api
- description: The users API from Zulip — 29 operation(s) for users.
  name: Zulip users API
  slug: zulip-users-api
- description: The webhooks API from Zulip — 1 operation(s) for webhooks.
  name: Zulip webhooks API
  slug: zulip-webhooks-api
artifact_total: 43
asyncapis:
- description: The Zulip Events API delivers real-time updates from a Zulip server to a client via an HTTPS long-poll. Clients first register an event queue by calling POST /api/v1/register, then repeatedly call GET
  name: Zulip Events API
  slug: zulip-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zulip REST authentication API
  slug: open-zulip-authentication-api
- collection_type: open
  name: Zulip REST authentication bots API
  slug: open-zulip-bots-api
- collection_type: open
  name: Zulip REST authentication channels API
  slug: open-zulip-channels-api
- collection_type: open
  name: Zulip REST authentication drafts API
  slug: open-zulip-drafts-api
- collection_type: open
  name: Zulip REST authentication invites API
  slug: open-zulip-invites-api
- collection_type: open
  name: Zulip REST authentication messages API
  slug: open-zulip-messages-api
- collection_type: open
  name: Zulip REST authentication mobile API
  slug: open-zulip-mobile-api
- collection_type: open
  name: Zulip REST authentication navigation_views API
  slug: open-zulip-navigation-views-api
- collection_type: open
  name: Zulip REST authentication real_time_events API
  slug: open-zulip-real-time-events-api
- collection_type: open
  name: Zulip REST authentication reminders API
  slug: open-zulip-reminders-api
- collection_type: open
  name: Zulip REST authentication scheduled_messages API
  slug: open-zulip-scheduled-messages-api
- collection_type: open
  name: Zulip REST authentication server_and_organizations API
  slug: open-zulip-server-and-organizations-api
- collection_type: open
  name: Zulip REST authentication users API
  slug: open-zulip-users-api
- collection_type: open
  name: Zulip REST authentication webhooks API
  slug: open-zulip-webhooks-api
- collection_type: open
  name: Zulip REST API
  slug: open-zulip
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zulip-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zulip-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zulip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zulip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zulip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zulip-by-kandra-labs
- group: company
  title: ''
  type: Website
  url: https://zulip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zulip.com/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zulip
created: '2026-01-02'
description: Zulip is an open-source team chat application with a unique topic-based threading model. Zulip's APIs power the web and mobile apps and provide REST endpoints, incoming webhooks, outgoing webhooks, and event-driven integrations to connect Zulip with external services.
finops:
- name: Zulip Finops
  service_category: API
  slug: zulip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zulip.png
layout: provider
modified: '2026-05-29'
name: Zulip
nav: Providers
network: true
overview: 'Zulip publishes 16 APIs on the [APIs.io](https://apis.io/) network, including REST API, Events API, authentication API, and 13 more. Tagged areas include Collaboration, Messaging, Team Chat, and Webhook.


  The Zulip catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Zulip''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Zulip Plans Pricing
  plan_count: 3
  slug: zulip-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Zulip Rate Limits
  slug: zulip-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Zulip API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: zulip-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 63.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    governance: 11.4
    operational_transparency: 13.2
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zulip/refs/heads/main/screenshots/zulip-2026-06-20T201957.png
security:
- kind: authentication
  name: Zulip Authentication
  slug: zulip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zulip Domain Security
  slug: zulip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zulip Vulnerability Disclosure
  slug: zulip-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Zulip Trust Center
  slug: zulip-trust-center
  summary_line: HIPAA, GDPR
slug: zulip
tags:
- Collaboration
- Messaging
- Team Chat
- Webhook
website: https://zulip.com/
---
