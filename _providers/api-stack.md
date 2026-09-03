---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: 'The API Stack Directory is a searchable catalog of 213+ API tools and services organized into 50+ categories. Each listing includes descriptions, features, pricing, screenshots, and external links to '
  name: API Stack Directory
  slug: api-stack-directory
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-stack-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/api-stack-conformance.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/api-stack-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/api-stack-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/api-stack-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compliance.apideck.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.apistack.io/partner/request
- group: start
  title: ''
  type: Login
  url: https://www.apistack.io/partner/login
- group: company
  title: ''
  type: Website
  url: https://www.apistack.io/
- group: other
  title: ''
  type: Categories
  url: https://www.apistack.io/categories/all
- group: other
  title: ''
  type: APIGateways
  url: https://www.apistack.io/category/api-gateways
- group: other
  title: ''
  type: APIManagement
  url: https://www.apistack.io/category/api-management
- group: other
  title: ''
  type: APIDesign
  url: https://www.apistack.io/category/api-design
- group: auth
  title: ''
  type: APIAuthentication
  url: https://www.apistack.io/category/api-authentication
- group: docs
  title: ''
  type: DeveloperDocumentationCategory
  url: https://www.apistack.io/category/developer-documentation
- group: other
  title: ''
  type: APIDirectories
  url: https://www.apistack.io/category/directories
- group: docs
  title: ''
  type: APISpecifications
  url: https://www.apistack.io/category/api-specifications
coverage:
  checked: '2026-09-02'
  detail: apistack.io is a 213-listing directory website with no developer surface of its own — /docs, /api-docs and /pricing all return 404, the 268-URL sitemap contains no developer, reference or pricing page, and no /.well-known/ document is served; the one machine-readable endpoint on the host, /api/graphql, is the Apideck Ecosystem platform backend that apistack.io runs on as a tenant (its schema is Marketplace/Listing/Partner plus Unify/Vault/Connection types), is disallowed in robots.txt, and is therefore catalogued under Apideck rather than credited to API Stack.
  evidence:
  - status: 404
    url: https://www.apistack.io/docs
  - status: 404
    url: https://www.apistack.io/api-docs
  - status: 404
    url: https://www.apistack.io/pricing
  - status: 404
    url: https://www.apistack.io/.well-known/api-catalog
  - status: 200
    url: https://www.apistack.io/sitemap.xml
  - status: 200
    url: https://www.apistack.io/api/graphql
  reason: no-developer-program
  state: none
created: '2025-01-08'
description: 'API Stack is a free, public directory and discovery platform for third-party API tooling, built and operated by Apideck B.V. as a tenant of its own Apideck Ecosystem marketplace platform. It catalogs 213 API tools and services across 46 published category pages spanning the whole API lifecycle: gateways, management, design, authentication, developer portals, documentation, specifications, testing, mocking, security, monitoring, analytics, billing, frameworks, linters and directories, with per-tool listing pages carrying descriptions, screenshots and outbound links so developers can shortlist and compare tooling. API Stack is a discovery surface rather than an API product: it publishes no developer portal, API reference, machine-readable contract, SDK, pricing page or terms of service of its own, and sits alongside Apideck''s API Tracker, Open Banking Tracker and SaaS Blocks properties.'
features:
- description: Comprehensive listing of API tools and services across 50+ categories with descriptions, features, and pricing.
  name: 213+ Tools Catalog
- description: Organized categories for browsing by API lifecycle stage including design, development, testing, security, and monitoring.
  name: Category Browsing
- description: Full-text search to find specific API tools matching developer requirements.
  name: Search and Discovery
- description: Detailed listing pages with features, pricing, and screenshots to help compare similar tools.
  name: Tool Comparison
- description: Built and maintained by Apideck as part of the broader API ecosystem alongside API Tracker and Open Banking Tracker.
  name: Powered by Apideck
finops:
- name: Api Stack Finops
  service_category: API
  slug: api-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-stack.png
layout: provider
modified: '2026-09-02'
name: API Stack
nav: Providers
network: true
overview: 'API Stack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Directory, API Gateways, API Management, and API Monitoring.


  API Stack''s developer surface includes signup flow and 16 more developer resources.'
plans:
- name: Api Stack Plans Pricing
  plan_count: 0
  slug: api-stack-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Api Stack Rate Limits
  slug: api-stack-rate-limits
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.4
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-stack/refs/heads/main/screenshots/api-stack-2026-06-20T172221.png
security:
- kind: domain-security
  name: Api Stack Domain Security
  slug: api-stack-domain-security
  summary_line: TLSv1.3 · HSTS
slug: api-stack
tags:
- API Design
- API Directory
- API Gateways
- API Management
- API Monitoring
- API Security
- API Testing
- API Tools
- Apideck
- Developer Tools
- Directory
- Discovery
use_cases:
- description: Developers and architects find and evaluate API tools across all stages of the API lifecycle.
  name: API Tooling Discovery
- description: Compare API gateway options from open source to enterprise to find the right solution for infrastructure needs.
  name: API Gateway Selection
- description: Discover API security testing, authentication, and monitoring tools for securing API programs.
  name: API Security Tool Research
- description: Explore API design tools, editors, and specification validators to improve API development workflows.
  name: API Design Tool Evaluation
- description: Research developer portal platforms and documentation tools for publishing API programs.
  name: Developer Portal Platforms
website: https://www.apistack.io/
---
