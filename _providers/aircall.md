---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Aircall Agentic Access
  operation_count: 35
  slug: aircall-agentic-access
  summary_line: 35 operations · 18 acting
api_count: 16
apis:
- description: List, transfer, comment, tag and archive calls.
  name: Aircall Calls API
  slug: aircall-calls-api
- description: Create, retrieve, update and delete users and organize them into teams.
  name: Aircall Users & Teams API
  slug: aircall-users-teams-api
- description: Configure phone numbers and SMS settings.
  name: Aircall Numbers API
  slug: aircall-numbers-api
- description: Manage customer contacts shared across the workspace.
  name: Aircall Contacts API
  slug: aircall-contacts-api
- description: Register, list and manage event subscriptions.
  name: Aircall Webhooks API
  slug: aircall-webhooks-api
- description: Send and receive SMS/MMS and group messages.
  name: Aircall Messaging API
  slug: aircall-messaging-api
- description: Access transcriptions, sentiment analysis, summaries and action items.
  name: Aircall Conversation Intelligence API
  slug: aircall-conversation-intelligence-api
- description: Create and manage outbound dialer campaigns.
  name: Aircall Dialer Campaign API
  slug: aircall-dialer-campaign-api
- description: The Calls API from Aircall — 7 operation(s) for calls.
  name: Aircall Calls API
  slug: aircall-calls-api
- description: The Contacts API from Aircall — 2 operation(s) for contacts.
  name: Aircall Contacts API
  slug: aircall-contacts-api
- description: The Conversation Intelligence API from Aircall — 2 operation(s) for conversation intelligence.
  name: Aircall Conversation Intelligence API
  slug: aircall-conversation-intelligence-api
- description: The Numbers API from Aircall — 2 operation(s) for numbers.
  name: Aircall Numbers API
  slug: aircall-numbers-api
- description: The Tags API from Aircall — 2 operation(s) for tags.
  name: Aircall Tags API
  slug: aircall-tags-api
- description: The Teams API from Aircall — 2 operation(s) for teams.
  name: Aircall Teams API
  slug: aircall-teams-api
- description: The Users API from Aircall — 2 operation(s) for users.
  name: Aircall Users API
  slug: aircall-users-api
- description: The Webhooks API from Aircall — 2 operation(s) for webhooks.
  name: Aircall Webhooks API
  slug: aircall-webhooks-api
artifact_total: 27
asyncapis:
- description: AsyncAPI description of Aircall's outbound webhook surface. Aircall delivers event notifications by issuing HTTP POST requests with a JSON body to a subscriber `url` that is registered through the Web
  name: Aircall Webhooks
  slug: aircall-webhooks-asyncapi
collections:
- collection_type: open
  name: Aircall Public API
  slug: open-aircall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aircall-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aircall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aircall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aircall-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aircall-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aircall
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aircall
- group: company
  title: ''
  type: Website
  url: https://aircall.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/aircall-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aircall-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aircall-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.aircall.io/llms.txt
created: '2026-05-08'
description: Aircall is a cloud-based phone system for sales and support teams with deep CRM integrations. APIs for users, calls, numbers, contacts, tags, webhooks, and Aircall AI.
finops:
- name: Aircall Finops
  service_category: Communications
  slug: aircall-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aircall.png
layout: provider
modified: '2026-05-30'
name: Aircall
nav: Providers
network: true
overview: 'Aircall publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Numbers API, Contacts API, and 10 more. Tagged areas include Communications, Voice, Cloud Phone, CRM, and Sales.


  The Aircall catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aircall''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Aircall Plans Pricing
  plan_count: 1
  slug: aircall-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 1
  name: Aircall Rate Limits
  slug: aircall-rate-limits
rules:
- name: Aircall API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: aircall-asyncapi-spectral-rules
scopes:
- name: Aircall Scopes
  scope_count: 1
  slug: aircall-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.4
  delta: -2.1
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.6
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 47.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aircall/refs/heads/main/screenshots/aircall-2026-06-20T171433.png
security:
- kind: authentication
  name: Aircall Authentication
  slug: aircall-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Aircall Domain Security
  slug: aircall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aircall Trust Center
  slug: aircall-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR
slug: aircall
tags:
- Communications
- Voice
- Cloud Phone
- CRM
- Sales
website: https://aircall.io/
---
