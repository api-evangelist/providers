---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Get Covered platform API — the integration surface that syncs resident, lease, policy, vendor certificate and invoice data two-way with property management systems (Yardi, Entrata, RealPage OneSit
  name: Get Covered Platform API
  slug: get-covered-platform-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/get-covered-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getcovered.io/
- group: start
  title: ''
  type: Portal
  url: https://www.getcovered.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getcovered.io/ai
- group: company
  title: ''
  type: About
  url: https://www.getcovered.io/about
- group: company
  title: ''
  type: Blog
  url: https://www.getcovered.io/blog
- group: company
  title: ''
  type: Careers
  url: https://www.getcovered.io/careers
- group: other
  title: ''
  type: Customers
  url: https://www.getcovered.io/customers
- group: other
  title: ''
  type: SignIn
  url: https://renters.getcoveredinsurance.com/auth/login
- group: operate
  title: ''
  type: Support
  url: https://www.getcovered.io/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getcovered.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getcovered.io/privacy
- group: commercial
  title: ''
  type: License
  url: https://www.getcoveredinsurance.com/licenses
- group: auth
  title: ''
  type: Security
  url: https://www.getcovered.io/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/get-covered-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getcovered.io/ai-disclosure
- group: auth
  title: ''
  type: AIDisclosure
  url: https://www.getcovered.io/ai-disclosure
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/get-covered_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/get-covered-inc
- group: build
  title: ''
  type: Packages
  url: packages/get-covered-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/get-covered-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/get-covered-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/get-covered-lifecycle.yml
created: '2026-08-04'
description: 'GetCovered, Inc. (Get Covered) is a New York-headquartered insurtech and property-risk technology company, founded in 2017, that consolidates fragmented insurance and compliance workflows for multifamily property management portfolios into a single platform. Its six verticals are renters insurance (HO4, master policy and TLL programs), security deposits (cash, surety and alternative deposits), animal and ESA screening, vendor certificate-of-insurance compliance, Spend IQ procurement and invoice validation, and review monitoring — layered with an AI tier branded GetHub (portfolio data and claims) and Cora (a conversational resident agent). The company reports 3M+ units live across 42 licensed states (NAIC #18224), with insurance services offered through GetCovered Insurance Services, LLC. Its platform API syncs resident, policy, vendor and invoice data two-way at the lease level with property management systems including Yardi, Entrata, RealPage OneSite, AppFolio, MRI and ResMan.
  The API itself is a partner/integration surface: the API reference at api.getcoveredinsurance.com/api-docs is behind HTTP Basic authentication and no OpenAPI, llms.txt or /.well-known documents are published publicly.'
image: https://www.getcovered.io/logo.svg
layout: provider
modified: '2026-08-04'
name: Get Covered
nav: Providers
network: true
overview: 'Get Covered publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Renters Insurance, and Property Management.


  Get Covered''s developer surface includes developer portal, documentation, engineering blog, support, and 19 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 24.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/get-covered/refs/heads/main/screenshots/get-covered-2026-08-07T165653.png
security:
- kind: authentication
  name: Get Covered Authentication
  slug: get-covered-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Get Covered Domain Security
  slug: get-covered-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Get Covered Vulnerability Disclosure
  slug: get-covered-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: get-covered
tags:
- Company
- Insurance
- Insurtech
- Renters Insurance
- Property Management
- Real-Estate
- Compliance
- Risk Management
- Embedded Insurance
- Artificial Intelligence
website: https://www.getcovered.io/
---
