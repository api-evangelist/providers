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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Windfall Data Agentic Access
  operation_count: 1
  slug: windfall-data-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.windfalldata.com/v1
  baseurl_source: declared
  description: The Windfall API API from Windfall Data — 1 operation(s) for windfall api.
  name: Windfall Data Windfall API API
  slug: windfall-data-windfall-api-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windfall Windfall API API
  slug: open-windfall-data-windfall-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/windfall-data-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://windfall.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.windfall.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.windfall.com/quickstart/
- group: auth
  title: ''
  type: Authentication
  url: authentication/windfall-data-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/windfall-data-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/windfall-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windfall-data-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/windfall-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/windfall-data-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/windfall-data-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/windfall-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/windfall-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.windfall.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/windfall-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windfall-data-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windfall-data-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/windfall-data-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/windfall-data-examples.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/windfall-data-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windfalldata
- group: operate
  title: ''
  type: Support
  url: https://www.windfall.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.windfall.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.windfall.com/blog/rss.xml
- group: start
  title: ''
  type: Login
  url: https://login.windfalldata.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.windfall.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.windfall.com/privacy
created: '2026-07-17'
description: 'Windfall (windfall.com, formerly windfalldata.com) is a people-intelligence and AI platform that personalizes go-to-market workflows with wealth and career data. Its developer-facing Windfall API delivers enriched household and career data on a single-record basis in real time: submit a person record with basic PII and receive that individual''s household net worth, a stable Windfall ID, and career signals such as a LinkedIn URL and title, returned as JSON in one sub-second request. Coverage is United States, data is refreshed weekly, and the API is used for real-time lead routing and grading, marketing enrichment, and analytics scoring. Authentication is a Windfall-issued header token with a dedicated sandbox environment of deterministic test personas. Windfall is SOC 2 Type 2 certified.'
image: https://api-docs.windfall.com/logo.svg
layout: provider
modified: '2026-08-13'
name: Windfall Data
nav: Providers
network: true
overview: 'Windfall Data publishes 1 API on the [APIs.io](https://apis.io/) network: Windfall API API. Tagged areas include Company, Data, Data Enrichment, Wealth Data, and People Intelligence.


  Windfall Data''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, code examples, support, and 23 more developer resources.'
plans:
- name: Windfall Data Plans Pricing
  plan_count: 0
  slug: windfall-data-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Windfall Data Rate Limits
  slug: windfall-data-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windfall-data/refs/heads/main/screenshots/windfall-data-2026-08-17T082922.png
security:
- kind: authentication
  name: Windfall Data Authentication
  slug: windfall-data-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windfall Data Domain Security
  slug: windfall-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Windfall Data Trust Center
  slug: windfall-data-trust-center
  summary_line: SOC 2 Type 2
slug: windfall-data
tags:
- Company
- Data
- Data Enrichment
- Wealth Data
- People Intelligence
- Net Worth
- Identity Resolution
- Marketing
- Sales
website: https://windfall.com
---
