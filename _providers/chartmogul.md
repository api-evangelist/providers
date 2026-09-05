---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Chartmogul Agentic Access
  operation_count: 28
  slug: chartmogul-agentic-access
  summary_line: 28 operations · 9 acting
api_count: 1
apis:
- description: REST API for ChartMogul providing endpoints for importing customers, subscriptions, plans, invoices, and transactions, plus reading SaaS metrics (MRR, ARR, ARPA, churn, LTV), customer attributes, segm
  name: ChartMogul REST API
  slug: rest-api
- description: Outbound webhook destination for ChartMogul. ChartMogul POSTs JSON event bodies to a subscriber-configured HTTPS endpoint whenever a customer-level MRR movement is recorded. Only the `mrr_movement` ev
  name: ChartMogul Webhooks
  slug: webhooks
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Account API from ChartMogul — 1 operation(s) for account.
  name: ChartMogul Account API
  slug: chartmogul-account-api
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Customers API from ChartMogul — 5 operation(s) for customers.
  name: ChartMogul Customers API
  slug: chartmogul-customers-api
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Invoices API from ChartMogul — 2 operation(s) for invoices.
  name: ChartMogul Invoices API
  slug: chartmogul-invoices-api
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Metrics API from ChartMogul — 8 operation(s) for metrics.
  name: ChartMogul Metrics API
  slug: chartmogul-metrics-api
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Plans API from ChartMogul — 2 operation(s) for plans.
  name: ChartMogul Plans API
  slug: chartmogul-plans-api
- baseURL: https://api.chartmogul.com
  baseurl_source: declared
  description: The Subscriptions API from ChartMogul — 1 operation(s) for subscriptions.
  name: ChartMogul Subscriptions API
  slug: chartmogul-subscriptions-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ChartMogul REST Account API
  slug: open-chartmogul-account-api
- collection_type: open
  name: ChartMogul Webhooks AsyncAPI
  slug: open-chartmogul-asyncapi
- collection_type: open
  name: ChartMogul REST Account Customers API
  slug: open-chartmogul-customers-api
- collection_type: open
  name: ChartMogul REST Account Invoices API
  slug: open-chartmogul-invoices-api
- collection_type: open
  name: ChartMogul REST Account Metrics API
  slug: open-chartmogul-metrics-api
- collection_type: open
  name: ChartMogul REST Account Plans API
  slug: open-chartmogul-plans-api
- collection_type: open
  name: ChartMogul REST Account Subscriptions API
  slug: open-chartmogul-subscriptions-api
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
random_paper: 7
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 60.7
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
