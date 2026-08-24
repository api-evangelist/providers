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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poplin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poplin.co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/poplin-co
- group: start
  title: ''
  type: LaundryProPortal
  url: https://laundry-pro.poplin.co
- group: operate
  title: ''
  type: HelpCenter
  url: https://poplin.zendesk.com/hc/en-us
- group: other
  title: ''
  type: Business
  url: https://poplin.co/business
- group: commercial
  title: ''
  type: Plans
  url: plans/poplin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/poplin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/poplin-finops.yml
- group: company
  title: ''
  type: About
  url: https://poplin.co/about
created: '2026-07-03'
description: Poplin (formerly SudShare) is a nationwide on-demand laundry pickup and delivery marketplace connecting customers with independent, work-from-home "Laundry Pros" who wash, dry, and fold laundry, serving 500+ cities and 150,000+ customers. Poplin operates two consumer-facing mobile apps - the customer app and the Laundry Pro app - plus a Laundry Pro web portal (laundry-pro.poplin.co), but it does not expose a public or partner developer API. No developer portal or API reference was found at poplin.co, and the api.poplin.co subdomain resolves but returns a bare 404 with no documentation, indicating internal-only use. Business/SMB accounts (property managers, hospitality) are onboarded through sales and an account manager rather than through self-service API keys.
finops:
- name: Poplin Finops
  service_category: Laundry / Gig Marketplace
  slug: poplin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poplin.png
layout: provider
modified: '2026-07-25'
name: Poplin
nav: Providers
network: true
overview: Poplin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Laundry, On-Demand, Gig Economy, Marketplace, and Delivery.
plans:
- name: Poplin Plans Pricing
  plan_count: 4
  slug: poplin-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Poplin Rate Limits
  slug: poplin-rate-limits
score:
  band: emerging
  composite: 16.6
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Poplin Domain Security
  slug: poplin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: poplin
tags:
- Laundry
- On-Demand
- Gig Economy
- Marketplace
- Delivery
- Consumer
website: https://poplin.co
---
