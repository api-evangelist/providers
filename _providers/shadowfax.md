---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://shadowfax.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shadowfax.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shadowfax.ai/docs/introduction/getting-started
- group: company
  title: ''
  type: Blog
  url: https://shadowfax.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://shadowfax.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://shadowfax.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shadowfax.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shadowfax.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shadowfax.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/shadowfax-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shadowfax-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/shadowfax-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shadowfax-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shadowfax-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/shadowfax-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shadowfax-llms.txt
coverage:
  checked: '2026-08-27'
  detail: 'Shadowfax AI ships its agentic-analytics platform only as an end-user web application: the 35-page Docusaurus documentation site has no API reference section, the pricing tiers name no API allowance, github.com/shadowfax-ai has zero public repositories, and the only HTTP contract on any host is the SPA backend route app.shadowfax.ai/openapi.json, which is not a product API and answers unauthenticated callers with a Clerk session-token 401.'
  evidence:
  - status: 401
    url: https://app.shadowfax.ai/openapi.json
  - status: 200
    url: https://docs.shadowfax.ai/sitemap.xml
  - status: 404
    url: https://shadowfax.ai/api
  - status: 404
    url: https://shadowfax.ai/llms.txt
  - status: 404
    url: https://shadowfax.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-27'
description: 'Shadowfax AI is an AI-native, agentic analytics platform founded in 2025 and based in Menlo Park, California, built by veterans of Snowflake, Palantir, Rubrik and Alteryx and backed by Khosla Ventures and the Snowflake Startup Accelerator. The product combines a spreadsheet, a BI tool, a visual pipeline and a code notebook into one analyst-in-the-loop workflow: users upload CSV, TSV, Excel or Parquet sources, which are held immutable, and every transformation produces a new View with full lineage, inspectable SQL and an auditable node graph. Features include AI Tables, an AI chat interface, schema discovery, slash commands, a reactive dependency system, manual SQL mode and a Vega-based visualization framework. It is in free public beta; live database connections to Snowflake and BigQuery are announced as coming soon. Shadowfax AI publishes no public developer API — the platform is an end-user product and its only HTTP contract sits behind a Clerk-authenticated session on app.shadowfax.ai.'
image: https://docs.shadowfax.ai/img/shadowfax-social-card.png
layout: provider
modified: '2026-08-27'
name: Shadowfax AI
nav: Providers
network: true
overview: 'Shadowfax AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Artificial Intelligence, and Data.


  Shadowfax AI''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Shadowfax Plans Pricing
  plan_count: 3
  slug: shadowfax-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Shadowfax Rate Limits
  slug: shadowfax-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 30.4
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shadowfax/refs/heads/main/screenshots/shadowfax-2026-09-02T155100.png
security:
- kind: domain-security
  name: Shadowfax Domain Security
  slug: shadowfax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shadowfax Trust Center
  slug: shadowfax-trust-center
  summary_line: SOC 2, HIPAA
slug: shadowfax
tags:
- Company
- Analytics
- Business Intelligence
- Artificial Intelligence
- Data
- Agentic Analytics
- Data Engineering
- Software-as-a-Service
website: https://shadowfax.ai/
---
