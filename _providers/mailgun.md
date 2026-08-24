---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mailgun Agentic Access
  operation_count: 17
  slug: mailgun-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 8
apis:
- description: REST API for verifying email addresses in real time, bulk list validation, and deliverability scoring to reduce bounces and improve sender reputation.
  name: Mailgun Email Validation API
  slug: validate-api
- description: The Domains API from Mailgun — 2 operation(s) for domains.
  name: Mailgun Domains API
  slug: mailgun-domains-api
- description: The Events API from Mailgun — 1 operation(s) for events.
  name: Mailgun Events API
  slug: mailgun-events-api
- description: The Mailing Lists API from Mailgun — 1 operation(s) for mailing lists.
  name: Mailgun Mailing Lists API
  slug: mailgun-mailing-lists-api
- description: The Messages API from Mailgun — 2 operation(s) for messages.
  name: Mailgun Messages API
  slug: mailgun-messages-api
- description: The Routes API from Mailgun — 1 operation(s) for routes.
  name: Mailgun Routes API
  slug: mailgun-routes-api
- description: The Suppressions API from Mailgun — 3 operation(s) for suppressions.
  name: Mailgun Suppressions API
  slug: mailgun-suppressions-api
- description: The Webhooks API from Mailgun — 2 operation(s) for webhooks.
  name: Mailgun Webhooks API
  slug: mailgun-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mailgun Domains API
  slug: open-mailgun-domains-api
- collection_type: open
  name: Mailgun Domains Events API
  slug: open-mailgun-events-api
- collection_type: open
  name: Mailgun Domains Mailing Lists API
  slug: open-mailgun-mailing-lists-api
- collection_type: open
  name: Mailgun Domains Messages API
  slug: open-mailgun-messages-api
- collection_type: open
  name: Mailgun Domains Routes API
  slug: open-mailgun-routes-api
- collection_type: open
  name: Mailgun Domains Suppressions API
  slug: open-mailgun-suppressions-api
- collection_type: open
  name: Mailgun Domains Webhooks API
  slug: open-mailgun-webhooks-api
- collection_type: open
  name: Mailgun Webhooks
  slug: open-mailgun-webhooks-asyncapi
- collection_type: open
  name: Mailgun API
  slug: open-mailgun
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailgun-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mailgun-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailgun-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailgun-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailgun
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailgun
- group: company
  title: ''
  type: Website
  url: https://www.mailgun.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.mailgun.com/
- group: start
  title: ''
  type: Signup
  url: https://signup.mailgun.com/new/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailgun.com/pricing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.mailgun.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mailgun.com/blog/feed/
created: '2026-05-11'
description: Mailgun (by Sinch) is a transactional email API service for developers to send, receive, validate, and track emails at scale. The platform provides SMTP and HTTP APIs for sending email, inbound message routing, deliverability analytics, suppression management, and email validation with regional endpoints for US and EU data residency.
graphqls:
- description: Mailgun is a REST-only email delivery API platform. No native GraphQL endpoint is publicly offered. This document describes a conceptual GraphQL layer derived from Mailgun's REST API data model, suita
  name: Mailgun GraphQL
  slug: mailgun-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailgun.png
layout: provider
modified: '2026-05-30'
name: Mailgun
nav: Providers
network: true
overview: 'Mailgun publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Domains API, Events API, Mailing Lists API, and 4 more. Tagged areas include Email, Transactional Email, SMTP, Email Validation, and Email Delivery.


  Mailgun''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailgun/refs/heads/main/screenshots/mailgun-2026-06-20T184856.png
security:
- kind: authentication
  name: Mailgun Authentication
  slug: mailgun-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailgun Domain Security
  slug: mailgun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mailgun Trust Center
  slug: mailgun-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: mailgun
tags:
- Email
- Transactional Email
- SMTP
- Email Validation
- Email Delivery
- Messaging
website: https://www.mailgun.com
---
