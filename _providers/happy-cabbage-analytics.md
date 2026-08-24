---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: External REST API for Happy Buyers organization metadata and inventory data. Requests are authenticated with an API key sent in the hca-api-key header and results are scoped to the organization attach
  name: Happy Buyers External API
  slug: happy-buyers-external-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.happycabbage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://cabbage.pub/swagger-ui/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://cabbage.pub/swagger-ui/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.happycabbage.io/the-patch
- group: operate
  title: ''
  type: Support
  url: https://www.happycabbage.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.happycabbage.io/buyers-free-trial
- group: start
  title: ''
  type: Login
  url: https://restock.happycabbage.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lrn.mobi/hca_privacy_policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happycabbage
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.happycabbage.io/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/happy-cabbage-analytics-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/happy-cabbage-analytics-happy-buyers-external-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/happy-cabbage-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/happy-cabbage-analytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/happy-cabbage-analytics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/happy-cabbage-analytics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/happy-cabbage-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/happy-cabbage-analytics-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/happy-cabbage-analytics-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/happy-cabbage-analytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/happy-cabbage-analytics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/happy-cabbage-analytics-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/happy-cabbage-analytics-happy-buyers-external-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/happy-cabbage-analytics-domain-security.yml
created: '2026-08-22'
description: Happy Cabbage Analytics is a cannabis retail software company founded in 2019 and headquartered in San Francisco, California, whose Happy Buyers platform gives dispensary buyers AI-assisted inventory management, demand forecasting, replenishment and purchase-order workflows on top of data pulled from their point-of-sale system. The platform reads live sell-through from POS integrations (Dutchie, Flowhub, Blaze, Treez, Meadow) and wholesale menus (Distru, Apex Trading), then scores inventory health by store, category and brand, predicts days-on-hand, groups SKUs into product lines, and drafts vendor orders with invoices attached. Happy Cabbage sold its Happy Marketers text-marketing suite to Alpine IQ in June 2025 and now focuses on Happy Buyers. A public Happy Buyers External API entered beta in June 2026 and is documented with a Swagger UI, exposing organization metadata, inventory health, product/product-line inventory, packages, daily sales metadata and full order management
  to API-key holders — the same API the company's own published AI-agent workflows are built on.
image: https://cdn.prod.website-files.com/5d46254e52d2932dcbc10ee9/65cba367661e3aebedb84daf_HCA_Logo_primary.png
layout: provider
modified: '2026-08-22'
name: Happy Cabbage Analytics
nav: Providers
network: true
overview: 'Happy Cabbage Analytics publishes 1 API on the [APIs.io](https://apis.io/) network: Happy Buyers External API. Tagged areas include Cannabis, Retail, Inventory Management, Analytics, and Purchasing.


  Happy Cabbage Analytics'' developer surface includes documentation, API reference, engineering blog, support, signup flow, changelog, authentication, and 18 more developer resources.'
plans:
- name: Happy Cabbage Analytics Plans Pricing
  plan_count: 0
  slug: happy-cabbage-analytics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Happy Cabbage Analytics Rate Limits
  slug: happy-cabbage-analytics-rate-limits
score:
  band: developing
  composite: 41.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 30.3
    contract_quality: 54.3
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 18.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Happy Cabbage Analytics Authentication
  slug: happy-cabbage-analytics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Happy Cabbage Analytics Domain Security
  slug: happy-cabbage-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: happy-cabbage-analytics
tags:
- Cannabis
- Retail
- Inventory Management
- Analytics
- Purchasing
- Point of Sale
- Wholesale
- Demand Forecasting
- Supply Chain
- agent-native
website: https://www.happycabbage.io/
---
