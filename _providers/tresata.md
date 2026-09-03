---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tresata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tresata.ai/
- group: other
  title: ''
  type: Products
  url: https://tresata.ai/products
- group: commercial
  title: ''
  type: Pricing
  url: https://tresata.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://tresata.ai/perspective
- group: operate
  title: ''
  type: Support
  url: https://community.tresata.com/
- group: start
  title: ''
  type: Login
  url: https://app-azure.tresata.com/web/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tresata.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tresata.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tresata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tresata/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tresatalife/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/tresata_stock/
- group: build
  title: ''
  type: Packages
  url: packages/tresata-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tresata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tresata-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tresata-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Tresata's entire public surface is a ten-page Next.js marketing site plus a Discourse community — its own sitemap.xml lists no developer, docs, or API page, docs.tresata.com and developer.tresata.com do not resolve, and /openapi.json, /swagger.json, /api-docs, /graphql and every /.well-known/* path 404 on both tresata.ai and community.tresata.com; the only product entry point is the login-gated tenant app at app-azure.tresata.com, whose TCP connection timed out on a single bounded probe.
  evidence:
  - status: 200
    url: https://tresata.ai/sitemap.xml
  - status: 404
    url: https://tresata.ai/openapi.json
  - status: 404
    url: https://tresata.ai/.well-known/api-catalog
  - status: 404
    url: https://community.tresata.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: 'Tresata is a Charlotte, North Carolina enterprise software company building what it describes as the foundational data layer for agentic AI. Its platform is marketed under the product names AB (Asset Builder), AU (Unreal Data Engine) and AF (Agent Foundation), alongside the Deduce and Discover surfaces, and automates data accuracy, entity resolution and enrichment across AWS, Azure and Google Cloud with a low-code interface. Pricing is usage-based, metered in Tresata Transaction Units (TTUs). Tresata publishes first-party open-source Scala/Spark libraries under the com.tresata group on Maven Central and co-authors the NANDini research effort with MIT on decentralised agentic data architectures. As of this profile it operates no public developer program: the platform is reached only through a login-gated tenant application, and no API reference, OpenAPI, GraphQL SDL, AsyncAPI or other machine-readable contract is published on any Tresata host.'
image: https://tresata.ai/logo.svg
layout: provider
modified: '2026-08-30'
name: Tresata
nav: Providers
network: true
overview: 'Tresata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Artificial Intelligence, and Machine-Learning.


  Tresata''s developer surface includes pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Tresata Plans Pricing
  plan_count: 2
  slug: tresata-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Tresata Rate Limits
  slug: tresata-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.6
  provenance:
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tresata/refs/heads/main/screenshots/tresata-2026-09-02T164212.png
security:
- kind: domain-security
  name: Tresata Domain Security
  slug: tresata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tresata
tags:
- Company
- Data
- Analytics
- Artificial Intelligence
- Machine-Learning
- Data Management
- Entity Resolution
- Big Data
- Enterprise Software
- Agents
website: https://tresata.ai/
---
