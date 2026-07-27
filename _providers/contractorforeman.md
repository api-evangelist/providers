---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: A private, account-scoped REST API reached with an API key generated under Settings > Integration > Zapier, used to power Contractor Foreman's official Zapier app rather than published for general dev
  name: Contractor Foreman Zapier Automation API
  slug: contractorforeman-zapier-automation-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contractorforeman-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contractor-foreman
- group: company
  title: ''
  type: Website
  url: https://contractorforeman.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.contractorforeman.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/contractorforeman-plans-pricing.yml
created: '2026-07-03'
description: Contractor Foreman is all-in-one construction management software for contractors - estimates, invoicing, scheduling, time cards, daily logs, change orders, and job costing - used by contractors in more than 75 countries. There is no self-serve public developer API or public API reference; the company's dedicated API subdomain (api.contractorforeman.net) displays only a "Coming soon" placeholder as of this review. The one confirmed API capability is a private, account-scoped API key (generated under Settings > Integration > Zapier) that powers Contractor Foreman's official Zapier app, exposing Customer and Lead create/archive/delete triggers and actions plus a File Uploaded trigger. That key and its underlying endpoints are not documented or published for direct third-party use outside the Zapier integration; broader third-party connectivity otherwise runs through native integrations (QuickBooks, Gusto, Google Calendar/Outlook, Stripe, Angi Leads, CompanyCam, MS Project, SweetPay)
  and Zapier/webhook automation rather than an open API.
finops:
- name: Contractorforeman Finops
  service_category: Construction Management Software
  slug: contractorforeman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contractorforeman.png
layout: provider
modified: '2026-07-03'
name: Contractor Foreman
nav: Providers
network: true
overview: 'Contractor Foreman publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Construction Management, Contractor Software, Estimating, and Invoicing.


  Contractor Foreman''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Contractorforeman Plans Pricing
  plan_count: 5
  slug: contractorforeman-plans-pricing
random_paper: 63
score:
  band: emerging
  composite: 17.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contractorforeman/refs/heads/main/screenshots/contractorforeman-2026-07-25T210341.png
security:
- kind: domain-security
  name: Contractorforeman Domain Security
  slug: contractorforeman-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contractorforeman
tags:
- Construction
- Construction Management
- Contractor Software
- Estimating
- Invoicing
- Scheduling
website: https://contractorforeman.com/
---
