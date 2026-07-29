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
- acting_count: 10
  human_in_the_loop: 0
  name: Mailjet Agentic Access
  operation_count: 20
  slug: mailjet-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 8
apis:
- description: Manage campaigns and drafts
  name: Mailjet Campaigns API
  slug: mailjet-campaigns-api
- description: Manage contact lists and recipients
  name: Mailjet Contact Lists API
  slug: mailjet-contact-lists-api
- description: Manage contacts and properties
  name: Mailjet Contacts API
  slug: mailjet-contacts-api
- description: Retrieve real-time event data
  name: Mailjet Event API
  slug: mailjet-event-api
- description: Send transactional and marketing emails
  name: Mailjet Send API
  slug: mailjet-send-api
- description: Manage verified sender addresses
  name: Mailjet Senders API
  slug: mailjet-senders-api
- description: Retrieve aggregated sending statistics
  name: Mailjet Statistics API
  slug: mailjet-statistics-api
- description: Manage reusable email templates
  name: Mailjet Templates API
  slug: mailjet-templates-api
artifact_total: 16
collections:
- collection_type: open
  name: Mailjet Email API
  slug: open-mailjet-email-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailjet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailjet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailjet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mailjet
- group: start
  title: ''
  type: Portal
  url: https://dev.mailjet.com/
- group: start
  title: ''
  type: Signup
  url: https://app.mailjet.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.mailjet.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailjet
- group: operate
  title: ''
  type: Support
  url: https://documentation.mailjet.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailjet.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://mailjetstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mailjet.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailjet.com/legal/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.mailjet.com/blog/feed/
created: '2026-03-16'
description: Mailjet is an email service provider offering a powerful REST API for sending transactional and marketing emails. It provides an easy-to-integrate API with support for PHP, Python, Ruby, Java, Node.js, C#, and Go, along with SMTP relay and real-time email tracking.
finops:
- name: Mailjet Finops
  service_category: API
  slug: mailjet-finops
graphqls:
- description: This conceptual GraphQL schema models the Mailjet Email API (v3), covering the full surface of Mailjet's REST API at https://dev.mailjet.com/email/reference/. The schema represents email sending, cont
  name: Mailjet GraphQL Schema
  slug: mailjet-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailjet.png
layout: provider
modified: '2026-05-19'
name: Mailjet
nav: Providers
network: true
overview: 'Mailjet publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contact Lists API, Contacts API, and 5 more. Tagged areas include Email, Email Delivery, Marketing Email, SMTP, and Transactional Email.


  Mailjet''s developer surface includes authentication, developer portal, signup flow, support, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Mailjet Plans Pricing
  plan_count: 3
  slug: mailjet-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Mailjet Rate Limits
  slug: mailjet-rate-limits
score:
  band: developing
  composite: 50.8
  delta: -1.2
  facets:
    commercial_clarity: 84.2
    contract_quality: 57.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailjet/refs/heads/main/screenshots/mailjet-2026-06-20T184859.png
security:
- kind: authentication
  name: Mailjet Authentication
  slug: mailjet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mailjet Domain Security
  slug: mailjet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mailjet
tags:
- Email
- Email Delivery
- Marketing Email
- SMTP
- Transactional Email
website: https://dev.mailjet.com/
---
