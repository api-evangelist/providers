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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Sendpulse Agentic Access
  operation_count: 31
  slug: sendpulse-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 10
apis:
- description: Account balance.
  name: SendPulse Account API
  slug: sendpulse-account-api
- description: Mailing lists and their subscribers.
  name: SendPulse Address Books API
  slug: sendpulse-address-books-api
- description: OAuth2 token issuance.
  name: SendPulse Authorization API
  slug: sendpulse-authorization-api
- description: Event-triggered automation flows.
  name: SendPulse Automation 360 API
  slug: sendpulse-automation-360-api
- description: Global email blacklist management.
  name: SendPulse Email Blacklist API
  slug: sendpulse-email-blacklist-api
- description: Bulk email campaign creation and reporting.
  name: SendPulse Email Campaigns API
  slug: sendpulse-email-campaigns-api
- description: Email sender addresses.
  name: SendPulse Senders API
  slug: sendpulse-senders-api
- description: SMS phone management and campaigns.
  name: SendPulse SMS API
  slug: sendpulse-sms-api
- description: Transactional email sending and tracking.
  name: SendPulse SMTP API
  slug: sendpulse-smtp-api
- description: Web push websites, subscriptions, and campaigns.
  name: SendPulse Web Push API
  slug: sendpulse-web-push-api
artifact_total: 17
collections:
- collection_type: open
  name: SendPulse API
  slug: open-sendpulse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendpulse-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendpulse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendpulse-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendpulse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendpulse
- group: company
  title: ''
  type: Website
  url: https://sendpulse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sendpulse.com/integrations/api
- group: commercial
  title: ''
  type: Plans
  url: plans/sendpulse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendpulse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendpulse-finops.yml
created: '2026-06-25'
description: SendPulse is a multichannel marketing platform with a unified REST API for email campaigns and address books, SMTP transactional email, SMS, web push notifications, chatbots across messengers, and Automation 360 flows. The API uses OAuth2 client_credentials to issue short-lived Bearer tokens against https://api.sendpulse.com.
finops:
- name: Sendpulse Finops
  service_category: Marketing and Communications
  slug: sendpulse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendpulse.png
layout: provider
modified: '2026-06-25'
name: SendPulse
nav: Providers
network: true
overview: 'SendPulse publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Address Books API, Authorization API, and 7 more. Tagged areas include Marketing, Email, SMS, Web Push, and Chatbots.


  SendPulse''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Sendpulse Plans Pricing
  plan_count: 8
  slug: sendpulse-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Sendpulse Rate Limits
  slug: sendpulse-rate-limits
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.8
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
    score: 16.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sendpulse Authentication
  slug: sendpulse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendpulse Domain Security
  slug: sendpulse-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sendpulse
tags:
- Marketing
- Email
- SMS
- Web Push
- Chatbots
- Transactional Email
- Multichannel
website: https://sendpulse.com/
---
