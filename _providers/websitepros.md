---
access_model:
  confidence: high
  label: Request Access
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api-docs.intl.web.com/
  - https://nts.developer.azure-api.net
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The partner-facing API for Web.com's International ("NTS") platform, fronted by Azure API Management. Ten documented operations cover the sales-order lifecycle (create, list with paging and filtering,
  name: Web.com International Platform API
  slug: international-platform
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/websitepros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.web.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nts.developer.azure-api.net
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.intl.web.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.intl.web.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.intl.web.com/#getting-started
- group: start
  title: ''
  type: SignUp
  url: https://nts.developer.azure-api.net/signup
- group: build
  title: ''
  type: Postman
  url: https://api-docs.intl.web.com/
- group: build
  title: ''
  type: PostmanCollection
  url: collections/websitepros-international-platform.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/websitepros-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/websitepros-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/websitepros-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/websitepros-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/websitepros-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/websitepros-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/websitepros-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/websitepros-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/websitepros-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/websitepros-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/websitepros-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/websitepros-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/websitepros-international-platform-overlay.yaml
created: '2026-07-17'
description: 'WebsitePros, now operating as Web.com, is an American company that provides website building, web hosting, domain registration, e-commerce, and online marketing services primarily to small and medium-sized businesses. Website Pros, Inc. merged with Web.com in 2007 and adopted the Web.com name, and the business is now part of Newfold Digital, formed in 2021 from Endurance Web Presence and Web.com Group. It offers do-it-yourself and do-it-for-you website builders, managed WordPress hosting, professional email, SEO and digital marketing tools, and is headquartered in Jacksonville, Florida. Behind the retail brand it runs a real partner-facing B2B API — the Web.com International ("NTS") Platform API, fronted by Azure API Management at api.nts.web.com and documented publicly at api-docs.intl.web.com — through which approved resellers and sales partners create and manage sales orders, provision service orders, check domain availability and mint customer single-sign-on URLs. Access
  is not self-service: registration is reviewed and approved by the Web.com International team, separately for the production and development environments.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/websitepros.png
layout: provider
mcp_servers:
- description: ''
  name: WebsitePros MCP Server
  slug: websitepros-mcp-server
modified: '2026-08-13'
name: WebsitePros
nav: Providers
network: true
overview: 'WebsitePros publishes 1 API on the [APIs.io](https://apis.io/) network: Web.com International Platform API. Tagged areas include Company, Website Builder, Web Hosting, Domains, and Small Business.


  WebsitePros'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, sandbox, and 17 more developer resources.'
plans:
- name: Websitepros Plans Pricing
  plan_count: 0
  slug: websitepros-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Websitepros Rate Limits
  slug: websitepros-rate-limits
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 17.8
    developer_ergonomics: 63.7
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 28.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Websitepros Authentication
  slug: websitepros-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Websitepros Domain Security
  slug: websitepros-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: websitepros
tags:
- Company
- Website Builder
- Web Hosting
- Domains
- Small Business
- Digital Marketing
- E-Commerce
- Reseller
- Sales Orders
- Provisioning
- Single Sign-On
- Azure API Management
website: https://www.web.com/
---
