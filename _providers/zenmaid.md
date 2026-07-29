---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  trial: true
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenmaid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zenmaid.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenmaid
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenmaid
- group: docs
  title: ''
  type: Documentation
  url: https://answers.zenmaid.com/en/collections/39144-integrations
- group: operate
  title: ''
  type: HelpCenter
  url: https://answers.zenmaid.com
- group: commercial
  title: ''
  type: Plans
  url: plans/zenmaid-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zenmaid.com/feed/
created: '2026-07-04'
description: ZenMaid is scheduling and business-management software for maid and house cleaning services - booking, calendar/dispatch, automated SMS and email communication, GPS-verified clock-in/out on a cleaner mobile app, online payments and invoicing, payroll, and reporting. ZenMaid has no public, self-service developer portal, no published REST/GraphQL API reference, and no OpenAPI specification of its own. Its only documented programmatic surface is a Zapier integration (triggers - New Customer Created, Appointment Booked, Appointment Cancelled, Appointment Updated, Contact Created/Updated, One-Time Service Created/Updated, Recurring Service Created/Updated/Cancelled, Invoice Created, Invoice Paid; actions - Create Appointment, Create Booking, Create Cleaner, Create Customer) built and maintained by ZenMaid against a private, undocumented backend API. No API keys, base URL, endpoint reference, payload schema, or SDK are published for third-party developers; the public GitHub organization
  (github.com/zenmaid) has no public repositories. This entry is documented as a stub because there is no public API to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenmaid.png
layout: provider
modified: '2026-07-04'
name: ZenMaid
nav: Providers
network: true
overview: 'ZenMaid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Maid Service, Cleaning Business Software, Field Service, Scheduling, and Zapier.


  ZenMaid''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Zenmaid Plans Pricing
  plan_count: 3
  slug: zenmaid-plans-pricing
random_paper: 51
score:
  band: emerging
  composite: 15.0
  delta: -1.8
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Zenmaid Domain Security
  slug: zenmaid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zenmaid
tags:
- Maid Service
- Cleaning Business Software
- Field Service
- Scheduling
- Zapier
- No Public API
website: https://www.zenmaid.com
---
