---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trengo Agentic Access
  operation_count: 21
  slug: trengo-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 1
apis:
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: List connected channels.
  name: Trengo Channels API
  slug: trengo-channels-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Manage contacts and contact profiles.
  name: Trengo Contacts API
  slug: trengo-contacts-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Manage labels and custom fields.
  name: Trengo Labels and Custom Fields API
  slug: trengo-labels-and-custom-fields-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: List and send text and media messages on a ticket.
  name: Trengo Messages API
  slug: trengo-messages-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Manage teams and list agents.
  name: Trengo Teams and Users API
  slug: trengo-teams-and-users-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Create, list, assign, label, and close conversations.
  name: Trengo Tickets API
  slug: trengo-tickets-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Register and manage webhook subscriptions.
  name: Trengo Webhooks API
  slug: trengo-webhooks-api
- baseURL: https://app.trengo.com/api/v2
  baseurl_source: declared
  description: Send approved WhatsApp Business templates.
  name: Trengo Whats App API
  slug: trengo-whats-app-api
artifact_total: 27
collections:
- collection_type: open
  name: Trengo Channels API
  slug: open-trengo-channels-api
- collection_type: open
  name: Trengo Channels Contacts API
  slug: open-trengo-contacts-api
- collection_type: open
  name: Trengo Channels Labels and Custom Fields API
  slug: open-trengo-labels-and-custom-fields-api
- collection_type: open
  name: Trengo Channels Messages API
  slug: open-trengo-messages-api
- collection_type: open
  name: Trengo Channels Teams and Users API
  slug: open-trengo-teams-and-users-api
- collection_type: open
  name: Trengo Channels Tickets API
  slug: open-trengo-tickets-api
- collection_type: open
  name: Trengo Channels Webhooks API
  slug: open-trengo-webhooks-api
- collection_type: open
  name: Trengo Channels WhatsApp API
  slug: open-trengo-whatsapp-api
- collection_type: open
  name: Trengo API
  slug: open-trengo
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://trengo.com/prices
- group: other
  href: https://artifacts.apis.io/trengo/capabilities/trengo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trengo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/trengo/agentic-access/trengo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trengo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trengo/security/trengo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trengo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/trengo/security/trengo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trengo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/trengo/security/trengo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trengo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/trengo/authentication/trengo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trengo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trengo
- group: company
  title: ''
  type: Website
  url: https://trengo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trengo.com/docs/welcome
- group: commercial
  href: https://artifacts.apis.io/trengo/plans/trengo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trengo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/trengo/rate-limits/trengo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trengo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trengo/finops/trengo-finops.yml
  title: ''
  type: FinOps
  url: finops/trengo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://trengo.com/blog
created: '2026-06-20'
description: Trengo is an omnichannel customer-engagement and shared-inbox platform that unifies email, WhatsApp, live chat, voice, SMS, and social channels into one team inbox with AI agents. The Trengo REST API (app.trengo.com/api/v2) lets you create and manage tickets, contacts, messages, channels, teams, users, labels, custom fields, webhooks, and WhatsApp templates programmatically with Bearer-token authentication.
finops:
- has_sources: true
  method: generated
  name: Trengo Finops
  primary_unit: ''
  service_category: Customer Engagement and Communications
  slug: trengo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trengo.png
layout: provider
modified: '2026-06-20'
name: Trengo
nav: Providers
network: true
overview: 'Trengo publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Labels and Custom Fields API, and 5 more. Tagged areas include Customer Engagement, Omnichannel, Shared Inbox, Messaging, and WhatsApp.


  The Trengo catalog on APIs.io includes 1 Spectral governance ruleset.


  Trengo''s developer surface includes pricing, authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Trengo Plans Pricing
  plan_count: 8
  slug: trengo-plans-pricing
- name: Trengo Price Estimates
  plan_count: 0
  slug: trengo-price-estimates
random_paper: 7
rate_limits:
- limit_count: 1
  name: Trengo Rate Limits
  slug: trengo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Trengo API Rules
  rule_count: 61
  severity_counts:
    error: 57
    hint: 0
    info: 2
    warn: 2
  slug: trengo-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.5
    catalog_earned_first_party: 12.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 49.9
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trengo/trengo-2026-06-20T195707.png
security:
- kind: authentication
  name: Trengo Authentication
  slug: trengo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trengo Domain Security
  slug: trengo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Trengo Vulnerability Disclosure
  slug: trengo-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Trengo Trust Center
  slug: trengo-trust-center
  summary_line: PCI DSS, GDPR
slug: trengo
tags:
- Customer Engagement
- Omnichannel
- Shared Inbox
- Messaging
- WhatsApp
- Customer Service
website: https://trengo.com/
---
