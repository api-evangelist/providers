---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: false
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
  score: 24.8
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: JSON:API-flavored REST endpoints covering accounts, prospects, sequences, mailings, calls, opportunities and tasks.
  name: Outreach REST API
  slug: outreach-rest-api
- description: Embed UI extensions and add custom actions in the Outreach app.
  name: Outreach Client Extensions API
  slug: outreach-client-extensions-api
- description: Bulk data sharing and integration capabilities.
  name: Outreach Data Sharing API
  slug: outreach-data-sharing-api
- description: Event-driven webhook deliveries for accounts, calls, contacts, email addresses, imports, Kaia recordings, mailings, opportunities, opportunity prospect roles, prospects, sequences, sequence states, ta
  name: Outreach Webhooks
  slug: outreach-webhooks
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/outreach-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/outreach-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outreach-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getoutreach
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/outreach-saas
- group: company
  title: ''
  type: Website
  url: https://www.outreach.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/outreach-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outreach-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/outreach-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.outreach.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.outreach.ai/blog
created: '2026-05-08'
description: Outreach is a sales engagement platform unifying email, calling, social, and meetings. APIs expose prospects, opportunities, sequences, mailings, calls, tasks, and analytics.
finops:
- name: Outreach Finops
  service_category: Sales
  slug: outreach-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outreach.png
layout: provider
modified: '2026-05-30'
name: Outreach
nav: Providers
network: true
overview: 'Outreach publishes 1 API on the [APIs.io](https://apis.io/) network: Webhooks. Tagged areas include Sales, Sales Engagement, Sequences, CRM, and Email.


  Outreach''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Outreach Plans Pricing
  plan_count: 1
  slug: outreach-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Outreach Rate Limits
  slug: outreach-rate-limits
score:
  band: emerging
  composite: 25.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.6
    developer_ergonomics: 2.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outreach/refs/heads/main/screenshots/outreach-2026-06-20T191233.png
security:
- kind: domain-security
  name: Outreach Domain Security
  slug: outreach-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Outreach Vulnerability Disclosure
  slug: outreach-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Outreach Trust Center
  slug: outreach-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: outreach
tags:
- Sales
- Sales Engagement
- Sequences
- CRM
- Email
website: https://www.outreach.io/
---
