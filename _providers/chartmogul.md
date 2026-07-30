---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Chartmogul Agentic Access
  operation_count: 28
  slug: chartmogul-agentic-access
  summary_line: 28 operations · 9 acting
api_count: 8
apis:
- description: REST API for ChartMogul providing endpoints for importing customers, subscriptions, plans, invoices, and transactions, plus reading SaaS metrics (MRR, ARR, ARPA, churn, LTV), customer attributes, segm
  name: ChartMogul REST API
  slug: rest-api
- description: Outbound webhook destination for ChartMogul. ChartMogul POSTs JSON event bodies to a subscriber-configured HTTPS endpoint whenever a customer-level MRR movement is recorded. Only the `mrr_movement` ev
  name: ChartMogul Webhooks
  slug: webhooks
- description: The Account API from ChartMogul — 1 operation(s) for account.
  name: ChartMogul Account API
  slug: chartmogul-account-api
- description: The Customers API from ChartMogul — 5 operation(s) for customers.
  name: ChartMogul Customers API
  slug: chartmogul-customers-api
- description: The Invoices API from ChartMogul — 2 operation(s) for invoices.
  name: ChartMogul Invoices API
  slug: chartmogul-invoices-api
- description: The Metrics API from ChartMogul — 8 operation(s) for metrics.
  name: ChartMogul Metrics API
  slug: chartmogul-metrics-api
- description: The Plans API from ChartMogul — 2 operation(s) for plans.
  name: ChartMogul Plans API
  slug: chartmogul-plans-api
- description: The Subscriptions API from ChartMogul — 1 operation(s) for subscriptions.
  name: ChartMogul Subscriptions API
  slug: chartmogul-subscriptions-api
artifact_total: 16
collections:
- collection_type: open
  name: ChartMogul Webhooks AsyncAPI
  slug: open-chartmogul-asyncapi
- collection_type: open
  name: ChartMogul REST API
  slug: open-chartmogul
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chartmogul-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chartmogul-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chartmogul-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chartmogul-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chartmogul-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chartmogul
- group: company
  title: ''
  type: Website
  url: https://chartmogul.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.chartmogul.com/docs/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://chartmogul.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.chartmogul.com/sign_up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chartmogul
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/chartmogul/chartmogul-mcp-server
- group: company
  title: ''
  type: Blog
  url: https://chartmogul.com/blog/feed.xml
created: '2026-05-11'
description: ChartMogul is a subscription analytics platform for SaaS companies that unifies billing data, customer information, and revenue analytics into one real-time view of MRR, churn, LTV, cohorts, and growth trends. The ChartMogul REST API provides programmatic access to import customers, subscriptions, invoices, transactions, and plans, and to read metrics, customer segments, and forecasts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chartmogul.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: ChartMogul
nav: Providers
network: true
overview: 'ChartMogul publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, Customers API, and 4 more. Tagged areas include Subscription Analytics, SaaS Metrics, Revenue Analytics, MRR, and Churn.


  ChartMogul''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 32.7
  delta: -2.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 63.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chartmogul/refs/heads/main/screenshots/chartmogul-2026-06-20T174231.png
security:
- kind: authentication
  name: Chartmogul Authentication
  slug: chartmogul-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chartmogul Domain Security
  slug: chartmogul-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chartmogul Vulnerability Disclosure
  slug: chartmogul-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Chartmogul Trust Center
  slug: chartmogul-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: chartmogul
tags:
- Subscription Analytics
- SaaS Metrics
- Revenue Analytics
- MRR
- Churn
- Cohorts
- Billing
website: https://chartmogul.com
---
