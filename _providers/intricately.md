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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Cloud Dynamics API (formerly the Intricately API) provides access to cloud adoption, usage, and spend data on companies, products, applications, and domains. Requests authenticate with an X-API-KE
  name: Cloud Dynamics API (Intricately)
  slug: cloud-dynamics-api-intricately
artifact_total: 7
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.intricately.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.intricately.com/
- group: operate
  title: ''
  type: Support
  url: https://help.intricately.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.intricately.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://help.intricately.com/articles/5366497774-request-an-api-key
- group: start
  title: ''
  type: SignUp
  url: https://content.intricately.com/demo
- group: start
  title: ''
  type: Login
  url: https://my.intricately.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hginsights.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hginsights.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kb.intricately.com/llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intricately-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intricately-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/intricately-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/intricately-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/intricately-trust-center.yml
created: '2026-07-17'
description: Intricately is a cloud and technology spend intelligence platform that tracks the adoption, usage, and spend of more than 15,000 cloud products across millions of companies worldwide, giving sales and marketing teams the signals they need to find accounts, spot active sales cycles, and predict churn. Founded in 2014 in San Francisco and backed by Bloomberg Beta, GitHub, Susa Ventures, and Singtel Innov8, Intricately was acquired by HG Insights in March 2022 and its data product is now delivered as the Cloud Dynamics API. The REST API (https://api.intricately.com/api/v2) authenticates with an X-API-KEY header and centers on asynchronous Bulk Jobs that enrich lists of domains with cloud adoption, product signatures, revenue, and digital-relationship data. API access is available on Enterprise plans.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intricately.png
layout: provider
mcp_servers:
- description: ''
  name: Intricately MCP Server
  slug: intricately-mcp-server
modified: '2026-08-14'
name: Intricately
nav: Providers
network: true
overview: 'Intricately publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Intelligence, Cloud Intelligence, Technographics, and Data Enrichment.


  Intricately''s developer surface includes documentation, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Intricately Plans Pricing
  plan_count: 0
  slug: intricately-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Intricately Rate Limits
  slug: intricately-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 30.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intricately/refs/heads/main/screenshots/intricately-2026-07-25T222720.png
security:
- kind: authentication
  name: Intricately Authentication
  slug: intricately-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Intricately Domain Security
  slug: intricately-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Intricately Trust Center
  slug: intricately-trust-center
  summary_line: SOC 2 Type 2
slug: intricately
tags:
- Company
- Sales Intelligence
- Cloud Intelligence
- Technographics
- Data Enrichment
- Cloud Spend
- Market Intelligence
website: https://developers.intricately.com/
---
