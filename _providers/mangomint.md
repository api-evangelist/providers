---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mangomint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mangomint.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mangomint
- group: docs
  title: ''
  type: Documentation
  url: https://www.mangomint.com/learn/help-articles/integrations/
- group: design
  title: ''
  type: WebhooksHelp
  url: https://www.mangomint.com/learn/webhooks-integration/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.mangomint.com/learn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mangomint
- group: commercial
  title: ''
  type: Plans
  url: plans/mangomint-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mangomint.com/blog
created: '2026-07-03'
description: Mangomint is salon and spa business management software covering scheduling, point of sale, payroll, marketing, memberships, and forms. Mangomint has no public, self-service developer portal, no published REST/GraphQL API reference, and no OpenAPI specification. Its only documented programmatic surface is outbound webhooks (appointment booked/updated/canceled, sale completed, form submitted) that Mangomint staff configure by hand over chat support once a customer supplies a receiving endpoint URL; payload schemas and authentication are not published. A small set of one-off, vendor-built integrations (Shopify, Mailchimp, Docovia, Doxy.me, WaiverForever, Gift Up!) are toggled on from the Mangomint dashboard, and there is no listed Zapier app. This entry is documented as a stub because there is no public API to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mangomint.png
layout: provider
modified: '2026-07-03'
name: Mangomint
nav: Providers
network: true
overview: 'Mangomint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Salon Software, Spa Software, Scheduling, Point of Sale, and Business Management.


  Mangomint''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Mangomint Plans Pricing
  plan_count: 4
  slug: mangomint-plans-pricing
random_paper: 66
score:
  band: emerging
  composite: 15.0
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mangomint/refs/heads/main/screenshots/mangomint-2026-07-25T230043.png
security:
- kind: domain-security
  name: Mangomint Domain Security
  slug: mangomint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mangomint
tags:
- Salon Software
- Spa Software
- Scheduling
- Point of Sale
- Business Management
- Webhooks
- No Public API
website: https://www.mangomint.com
---
