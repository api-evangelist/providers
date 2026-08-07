---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Emailengine Agentic Access
  operation_count: 15
  slug: emailengine-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 13
apis:
- description: The Account API from EmailEngine — 3 operation(s) for account.
  name: EmailEngine Account API
  slug: emailengine-account-api
- description: The Accounts API from EmailEngine — 1 operation(s) for accounts.
  name: EmailEngine Accounts API
  slug: emailengine-accounts-api
- description: The Autoconfig API from EmailEngine — 1 operation(s) for autoconfig.
  name: EmailEngine Autoconfig API
  slug: emailengine-autoconfig-api
- description: The Deliverytest API from EmailEngine — 1 operation(s) for deliverytest.
  name: EmailEngine Deliverytest API
  slug: emailengine-deliverytest-api
- description: The Gateways API from EmailEngine — 1 operation(s) for gateways.
  name: EmailEngine Gateways API
  slug: emailengine-gateways-api
- description: The License API from EmailEngine — 1 operation(s) for license.
  name: EmailEngine License API
  slug: emailengine-license-api
- description: The Logs API from EmailEngine — 1 operation(s) for logs.
  name: EmailEngine Logs API
  slug: emailengine-logs-api
- description: The Oauth2 API from EmailEngine — 1 operation(s) for oauth2.
  name: EmailEngine Oauth2 API
  slug: emailengine-oauth2-api
- description: The Outbox API from EmailEngine — 1 operation(s) for outbox.
  name: EmailEngine Outbox API
  slug: emailengine-outbox-api
- description: The Stats API from EmailEngine — 1 operation(s) for stats.
  name: EmailEngine Stats API
  slug: emailengine-stats-api
- description: The Templates API from EmailEngine — 1 operation(s) for templates.
  name: EmailEngine Templates API
  slug: emailengine-templates-api
- description: The Tokens API from EmailEngine — 1 operation(s) for tokens.
  name: EmailEngine Tokens API
  slug: emailengine-tokens-api
- description: The Webhookroutes API from EmailEngine — 1 operation(s) for webhookroutes.
  name: EmailEngine Webhookroutes API
  slug: emailengine-webhookroutes-api
artifact_total: 19
collections:
- collection_type: open
  name: EmailEngine API
  slug: open-emailengine
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emailengine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emailengine-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://learn.emailengine.app/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.emailengine.app/docs/api/emailengine-api
- group: design
  title: ''
  type: Webhooks
  url: https://emailengine.app/webhooks
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/postalsys/emailengine
- group: company
  title: ''
  type: Blog
  url: https://blog.emailengine.app/
- group: operate
  title: ''
  type: FAQ
  url: https://emailengine.app/#faq
- group: commercial
  title: ''
  type: Pricing
  url: https://postalsys.com/plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postalsys.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailengine.app/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://emailengine.app/support
created: '2025-02-06'
description: EmailEngine is a self-hosted email automation platform that provides a unified REST API for accessing email accounts via IMAP, SMTP, the Gmail API, and the Microsoft Graph API. It exposes JSON payloads, real-time webhooks, OAuth2 integration, an IMAP/SMTP proxy, hosted authentication forms, low-code custom integrations, Prometheus monitoring, and bounce detection so developers can build modern email functionality without paying per-account fees.
finops:
- name: Emailengine Finops
  service_category: API
  slug: emailengine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emailengine.png
layout: provider
modified: '2026-05-19'
name: EmailEngine
nav: Providers
network: true
overview: 'EmailEngine publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Autoconfig API, and 10 more. Tagged areas include Email, Email API, IMAP, SMTP, and Webhooks.


  EmailEngine''s developer surface includes documentation, API reference, engineering blog, FAQ, pricing, support, and 6 more developer resources.'
plans:
- name: Emailengine Plans Pricing
  plan_count: 3
  slug: emailengine-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Emailengine Rate Limits
  slug: emailengine-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 48.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emailengine/refs/heads/main/screenshots/emailengine-2026-06-20T180623.png
security:
- kind: domain-security
  name: Emailengine Domain Security
  slug: emailengine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emailengine
tags:
- Email
- Email API
- IMAP
- SMTP
- Webhooks
---
