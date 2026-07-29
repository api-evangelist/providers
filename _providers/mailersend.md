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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Mailersend Agentic Access
  operation_count: 16
  slug: mailersend-agentic-access
  summary_line: 16 operations · 7 acting
api_count: 8
apis:
- description: MailerSend API v1 provides RESTful endpoints for sending emails (single, bulk, scheduled), templates, domains, recipients, suppression lists, webhooks, analytics, SMS, and inbound routing.
  name: MailerSend API
  slug: mailersend-api
- description: The Bulk Email API from MailerSend — 2 operation(s) for bulk email.
  name: MailerSend Bulk Email API
  slug: mailersend-bulk-email-api
- description: The Domains API from MailerSend — 2 operation(s) for domains.
  name: MailerSend Domains API
  slug: mailersend-domains-api
- description: The Email API from MailerSend — 1 operation(s) for email.
  name: MailerSend Email API
  slug: mailersend-email-api
- description: The Messages API from MailerSend — 2 operation(s) for messages.
  name: MailerSend Messages API
  slug: mailersend-messages-api
- description: The Sender Identities API from MailerSend — 1 operation(s) for sender identities.
  name: MailerSend Sender Identities API
  slug: mailersend-sender-identities-api
- description: The Templates API from MailerSend — 2 operation(s) for templates.
  name: MailerSend Templates API
  slug: mailersend-templates-api
- description: The Webhooks API from MailerSend — 2 operation(s) for webhooks.
  name: MailerSend Webhooks API
  slug: mailersend-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: MailerSend API
  slug: open-mailersend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailersend-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailersend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailersend-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailersend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailersend
- group: company
  title: ''
  type: Website
  url: https://www.mailersend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.mailersend.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mailersend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mailersend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mailersend-finops.yml
created: '2026-05-08'
description: MailerSend is a transactional email and SMS platform built for developers, with email API, SMTP relay, templates, and analytics.
finops:
- name: Mailersend Finops
  service_category: Email
  slug: mailersend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailersend.png
layout: provider
modified: '2026-05-08'
name: MailerSend
nav: Providers
network: true
overview: 'MailerSend publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk Email API, Domains API, Email API, and 4 more. Tagged areas include Email, Transactional Email, SMTP, Marketing, and Communications.


  MailerSend''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Mailersend Plans Pricing
  plan_count: 1
  slug: mailersend-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 1
  name: Mailersend Rate Limits
  slug: mailersend-rate-limits
score:
  band: thin
  composite: 33.4
  delta: -1.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.1
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailersend/refs/heads/main/screenshots/mailersend-2026-06-20T184858.png
security:
- kind: authentication
  name: Mailersend Authentication
  slug: mailersend-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailersend Domain Security
  slug: mailersend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mailersend
tags:
- Email
- Transactional Email
- SMTP
- Marketing
- Communications
website: https://www.mailersend.com/
---
