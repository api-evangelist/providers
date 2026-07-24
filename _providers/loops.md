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
- acting_count: 10
  human_in_the_loop: 0
  name: Loops Agentic Access
  operation_count: 24
  slug: loops-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 11
apis:
- description: The API key API from Loops — 1 operation(s) for api key.
  name: Loops API key API
  slug: loops-api-key-api
- description: Create and manage email campaigns
  name: Loops Campaigns API
  slug: loops-campaigns-api
- description: View email components
  name: Loops Components API
  slug: loops-components-api
- description: Manage contact properties
  name: Loops Contact properties API
  slug: loops-contact-properties-api
- description: Manage contacts in your audience
  name: Loops Contacts API
  slug: loops-contacts-api
- description: View dedicated sending IP addresses
  name: Loops Dedicated sending IPs API
  slug: loops-dedicated-sending-ips-api
- description: Manage email message content for campaigns
  name: Loops Email messages API
  slug: loops-email-messages-api
- description: Trigger email sending with events
  name: Loops Events API
  slug: loops-events-api
- description: View mailing lists
  name: Loops Mailing lists API
  slug: loops-mailing-lists-api
- description: View email themes
  name: Loops Themes API
  slug: loops-themes-api
- description: Send and view transactional emails
  name: Loops Transactional emails API
  slug: loops-transactional-emails-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loops-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loops-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loops-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Loops-so
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendwithloops
- group: company
  title: ''
  type: Website
  url: https://loops.so/
- group: docs
  title: ''
  type: Documentation
  url: https://loops.so/docs/api-reference/intro
- group: commercial
  title: ''
  type: Plans
  url: plans/loops-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loops-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loops-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://loops.so/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://loops.so/changelog
created: '2026-05-08'
description: Loops is an email platform for SaaS companies, combining marketing campaigns, transactional emails, and contact management with a developer-first API.
finops:
- name: Loops Finops
  service_category: Email Marketing
  slug: loops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loops.png
layout: provider
modified: '2026-05-19'
name: Loops
nav: Providers
network: true
overview: 'Loops publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API key API, Campaigns API, Components API, and 8 more. Tagged areas include Email, Marketing Automation, Transactional Email, SaaS, and Communications.


  Loops'' developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Loops Plans Pricing
  plan_count: 1
  slug: loops-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Loops Rate Limits
  slug: loops-rate-limits
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.2
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loops/refs/heads/main/screenshots/loops-2026-06-20T184718.png
security:
- kind: authentication
  name: Loops Authentication
  slug: loops-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Loops Domain Security
  slug: loops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loops
tags:
- Email
- Marketing Automation
- Transactional Email
- SaaS
- Communications
website: https://loops.so/
---
