---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 132
  human_in_the_loop: 4
  name: Criteo Agentic Access
  operation_count: 219
  slug: criteo-agentic-access
  summary_line: 219 operations · 132 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: 'The Criteo Retail Media API lets retailers, brands, agencies and partners build retail media programmatically. 115 operations across eight tags cover accounts and brand/seller hierarchies, campaigns, '
  name: Criteo Retail Media API
  slug: criteo-retail-media-api
- description: 'The Criteo Marketing Solutions API gives advertisers and agencies programmatic access to Criteo''s commerce media platform for acquisition and retention. 96 operations cover advertisers, campaigns, ad '
  name: Criteo Marketing Solutions API
  slug: criteo-marketing-solutions-api
- description: The Criteo Commerce Grid API manages audience segments for Commerce Grid, Criteo's sell-side platform. Eight operations create, update, delete and search audience segments and manage contact-list memb
  name: Criteo Commerce Grid API
  slug: criteo-commerce-grid-api
- description: 'Criteo operates two remote Model Context Protocol servers. The documentation server at developers.criteo.com/mcp is anonymous and was introspected live: three tools (search_criteo_docs, query_docs_fil'
  name: Criteo MCP Servers
  slug: criteo-mcp
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Criteo API
  slug: open-criteo-commerce-grid-api
- collection_type: open
  name: Criteo API
  slug: open-criteo-marketing-solutions-api
- collection_type: open
  name: Criteo API
  slug: open-criteo-retail-media-api
- collection_type: open
  name: Criteo Retail Media API
  slug: open-criteo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/criteo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/criteo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/criteo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/criteo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/criteo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/criteo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criteo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/criteo
- group: company
  title: ''
  type: Website
  url: https://www.criteo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.criteo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.criteo.com/retail-media/docs/welcome-to-criteo
- group: company
  title: ''
  type: Blog
  url: https://www.criteo.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteo.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.criteo.com/legal/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.criteo.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/criteo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/criteo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/criteo-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/criteo-security.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/criteo-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/criteo-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/criteo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.criteo.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/criteo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/criteo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.criteo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.criteo.com/criteo-apis/docs/versioning-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/criteo-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/criteo-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/criteo-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/criteo-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/criteo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/criteo-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://www.criteo.com/.well-known/security.txt
- group: commercial
  title: ''
  type: FinOps
  url: finops/criteo-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/realcriteo/workspace/criteo/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.criteo.com/criteo-apis/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.criteo.com/criteo-apis/docs/connect-to-the-api
- group: operate
  title: ''
  type: Support
  url: https://help.criteo.com/
- group: start
  title: ''
  type: Login
  url: https://partners.criteo.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/criteo-retail-media-overlay.yaml
created: '2025-03-01'
description: 'Criteo is a global commerce media company whose Retail Media, Marketing Solutions and Commerce Grid platforms let retailers, brands, agencies and partners create, launch and measure onsite and offsite commerce advertising. Criteo publishes three live OpenAPI 3.0.1 documents at api.criteo.com covering 219 operations: campaign and line-item management, keyword and promoted-product targeting, audience segments and contact lists, retailer catalogs, account and brand hierarchies, balances and billing, creative and product-boost management, and demand-side and supply-side analytics. Authentication is OAuth 2.0 with client-credentials and authorization-code grants and 22 scopes of the form <Service>_<Domain>_<Level>. Criteo ships officially supported Python, PHP and Java SDKs, a public Postman workspace, an llms.txt docs index, an A2A agent card, a published Agent Skill, and two remote MCP servers — an anonymous documentation server and an OAuth-protected API server at mcp.criteo.com.'
finops:
- name: Criteo Finops
  service_category: API
  slug: criteo-finops
graphqls:
- description: '> **Read this first.** Criteo publishes **no GraphQL endpoint.** The schema in'
  name: Criteo GraphQL — NOT A CRITEO CONTRACT
  slug: criteo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/criteo.png
layout: provider
mcp_servers:
- description: ''
  name: criteo-mcp.yml
  slug: criteo-mcpyml
modified: '2026-08-13'
name: Criteo
nav: Providers
network: true
overview: 'Criteo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Retail Media API, Marketing Solutions API, and Commerce Grid API. Tagged areas include Advertising, Agent Skills, Analytics, Audiences, and Campaigns.


  Criteo''s developer surface includes authentication, documentation, engineering blog, changelog, API reference, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Criteo Plans Pricing
  plan_count: 0
  slug: criteo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Criteo Rate Limits
  slug: criteo-rate-limits
scopes:
- name: Criteo Scopes
  scope_count: 22
  slug: criteo-scopes
  summary_line: 22 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 59.3
  delta: -0.1
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 30.3
    contract_quality: 54.7
    developer_ergonomics: 61.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 78.9
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/criteo/refs/heads/main/screenshots/criteo-2026-06-20T175235.png
security:
- kind: authentication
  name: Criteo Authentication
  slug: criteo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Criteo Domain Security
  slug: criteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Criteo Vulnerability Disclosure
  slug: criteo-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Criteo Trust Center
  slug: criteo-trust-center
  summary_line: SOC 2, SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001
slug: criteo
tags:
- Advertising
- Agent Skills
- Analytics
- Audiences
- Campaigns
- Catalog
- Commerce
- Commerce Media
- Display Advertising
- Marketing
- MCP
- Media
- OAuth 2.0
- OpenAPI
- Reporting
- Retail
- Retail Media
- Sponsored Products
website: https://www.criteo.com/
---
