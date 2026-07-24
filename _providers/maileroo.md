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
- acting_count: 4
  human_in_the_loop: 0
  name: Maileroo Agentic Access
  operation_count: 5
  slug: maileroo-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 2
apis:
- description: Send transactional and bulk emails
  name: Maileroo Emails API
  slug: maileroo-emails-api
- description: Manage scheduled email deliveries
  name: Maileroo Scheduled API
  slug: maileroo-scheduled-api
artifact_total: 9
collections:
- collection_type: open
  name: Maileroo Email API
  slug: open-maileroo-email-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maileroo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maileroo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maileroo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maileroo
- group: start
  title: ''
  type: Portal
  url: https://maileroo.com/email-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://maileroo.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://app.maileroo.com/register
- group: start
  title: ''
  type: Login
  url: https://app.maileroo.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maileroo
- group: commercial
  title: ''
  type: Pricing
  url: https://maileroo.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://maileroo.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://maileroo.com/blog/feed
created: '2025-02-06'
description: Maileroo provides transactional and marketing email delivery via a developer-friendly REST API with high deliverability, SMTP relay support, email tracking, and SDKs for popular programming languages. Trusted by businesses of all sizes to handle millions of emails every month.
finops:
- name: Maileroo Finops
  service_category: API
  slug: maileroo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maileroo.png
layout: provider
modified: '2026-05-19'
name: Maileroo
nav: Providers
network: true
overview: 'Maileroo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Emails API and Scheduled API. Tagged areas include Email, Email Delivery, Marketing Email, SMTP, and Transactional Email.


  Maileroo''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Maileroo Plans Pricing
  plan_count: 3
  slug: maileroo-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Maileroo Rate Limits
  slug: maileroo-rate-limits
score:
  band: thin
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 60.2
    developer_ergonomics: 30.4
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maileroo/refs/heads/main/screenshots/maileroo-2026-06-20T184856.png
security:
- kind: authentication
  name: Maileroo Authentication
  slug: maileroo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Maileroo Domain Security
  slug: maileroo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maileroo
tags:
- Email
- Email Delivery
- Marketing Email
- SMTP
- Transactional Email
website: https://maileroo.com/email-for-developers
---
