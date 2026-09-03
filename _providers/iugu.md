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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: RESTful API providing 140+ endpoints for payment processing, customer management, invoicing, subscriptions, marketplace split payments, Pix, boleto bancário, credit card tokenization, webhooks, and fi
  name: Iugu API
  slug: iugu-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iugu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iugu.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.iugu.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/iugu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iugu
- group: company
  title: ''
  type: Blog
  url: https://www.iugu.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.iugu.com/planos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iugu.com/
- group: other
  title: ''
  type: X
  url: https://x.com/iugu
- group: commercial
  title: ''
  type: Plans
  url: plans/iugu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iugu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iugu-finops.yml
created: '2026-06-13'
description: Iugu is a Brazilian payment infrastructure platform offering REST APIs for invoicing, subscriptions, payment splits, boleto bancário generation, credit card processing, and marketplace payments. The platform enables businesses to automate financial operations including recurring billing, split payments for marketplaces, Pix instant payments, and sub-account management. Iugu operates as a Bacen-licensed Payment Institution and is PCI DSS compliant, serving e-commerce, SaaS, and marketplace companies across Brazil.
finops:
- name: Iugu Finops
  service_category: ''
  slug: iugu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iugu.png
layout: provider
modified: '2026-06-13'
name: Iugu
nav: Providers
network: true
overview: 'Iugu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Brazil, Invoicing, Subscription, and Boleto.


  Iugu''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Iugu Plans Pricing
  plan_count: 3
  slug: iugu-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Iugu Rate Limits
  slug: iugu-rate-limits
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 27.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iugu/refs/heads/main/screenshots/iugu-2026-06-20T183637.png
security:
- kind: domain-security
  name: Iugu Domain Security
  slug: iugu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iugu
tags:
- Payments
- Brazil
- Invoicing
- Subscription
- Boleto
- Pix
- Credit Card
- Marketplace
- Split Payments
- Financial Infrastructure
- Fintech
website: https://www.iugu.com
---
