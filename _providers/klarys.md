---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 20.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The API surface behind the Klarys tenant application at klarys.app. Klarys markets API and EDI integration with customer ERP, accounting and product-reference systems, and the application serves an an
  name: Klarys Platform API
  slug: klarys-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klarys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.klarys.io/
- group: operate
  title: ''
  type: Support
  url: https://www.klarys.io/en/service-client
- group: operate
  title: ''
  type: Contact
  url: https://www.klarys.io/en/contact
- group: company
  title: ''
  type: Blog
  url: https://www.klarys.io/en/resources
- group: company
  title: ''
  type: Press
  url: https://www.klarys.io/en/press
- group: other
  title: ''
  type: CaseStudies
  url: https://www.klarys.io/en/case-studies
- group: company
  title: ''
  type: About
  url: https://www.klarys.io/en/who-are-we
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procsea
- group: start
  title: ''
  type: Login
  url: https://klarys.app/fr/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klarys.io/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klarys.io/en/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.klarys.io/en/legal-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klarys.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klarys/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/klarys_io
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/@klarys_io
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klarys-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klarys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/klarys-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klarys-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klarys-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klarys-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klarys-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/klarys-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klarys-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/klarys-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klarys-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: Klarys runs a Django REST Framework API with a live OpenAPI schema endpoint, but https://klarys.app/api/schema/?format=json answers HTTP 401 {"code":1003,"error":"User is unauthenticated"} with Content-Type application/vnd.oai.openapi+json — the spec is real and served only to an authenticated tenant, and there is no developer portal, API reference or pricing page anywhere on www.klarys.io (all 134 sitemap URLs walked).
  evidence:
  - status: 401
    url: https://klarys.app/api/schema/?format=json
  - status: 200
    url: https://klarys.app/.well-known/oauth-authorization-server
  - status: 404
    url: https://www.klarys.io/llms.txt
  - status: 404
    url: https://klarys.app/.well-known/oauth-protected-resource
  reason: customer-only-docs
  state: gated
created: '2026-08-17'
description: 'Klarys — formerly ProcSea, renamed in 2023 — is a French SaaS eProcurement platform built for the fresh-food supply chain: seafood, fruit and vegetables, meat and dairy. It connects retail, wholesale and foodservice buyers with their suppliers, wholesalers and mareyeurs through a standardized fresh-food product catalog, a supplier sales interface, a centralized purchasing interface, a central purchasing module for store networks, a supplier invoicing module and a business-intelligence module. Klarys states that the platform "integrates with all your business systems and applications via API and EDI" — ERP, accounting tools and product reference systems. Founded in 2016 in Rennes, France with operations in Switzerland, it is a Serena portfolio company, a member of the SAP.iO acceleration program and listed on the SAP Store. The tenant application runs at klarys.app and publishes an RFC 8414 OAuth 2.0 authorization-server metadata document anonymously — including mcp:read and
  mcp:write scopes — but no public API reference, OpenAPI, or developer portal: the schema endpoint requires an authenticated tenant account.'
image: https://cdn.prod.website-files.com/645262ac6eca60aef2a6ff24/6487761d3ac838e6ec321735_klarys%20the%20fresh%20food%20platform.webp
layout: provider
modified: '2026-08-17'
name: Klarys
nav: Providers
network: true
overview: 'Klarys publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, eProcurement, Procurement, and Supply Chain.


  Klarys'' developer surface includes support, engineering blog, legal docs, YouTube channel, authentication, and 23 more developer resources.'
plans:
- name: Klarys Plans Pricing
  plan_count: 0
  slug: klarys-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Klarys Rate Limits
  slug: klarys-rate-limits
scopes:
- name: Klarys Scopes
  scope_count: 6
  slug: klarys-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 20.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Klarys Authentication
  slug: klarys-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Klarys Domain Security
  slug: klarys-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: klarys
tags:
- Company
- Software-as-a-Service
- eProcurement
- Procurement
- Supply Chain
- Food and Beverage
- Seafood
- Fresh Food
- Retail
- EDI
- Invoicing
- France
website: https://www.klarys.io/
---
