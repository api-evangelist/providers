---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 75
  human_in_the_loop: 0
  name: Fixflo Agentic Access
  operation_count: 165
  slug: fixflo-agentic-access
  summary_line: 165 operations · 75 acting
api_count: 1
apis:
- description: The Fixflo v2 REST API, described by a publicly downloadable OpenAPI 3.0 document on the Fixflo Stoplight developer portal. It exposes the repairs and maintenance domain — issues and issue drafts, pro
  name: Fixflo API v2
  slug: fixflo-api-v2
artifact_total: 8
asyncapis:
- description: ''
  name: Fixflo Webhooks
  slug: fixflo-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fixflo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fixflo-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fixflo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fixflo-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fixflo-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/fixflo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fixflo-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fixflo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fixflo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fixflo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fixflo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api-docs.fixflo.com/72b66de24898e-welcome-to-fixflo
- group: design
  title: ''
  type: Conformance
  url: conformance/fixflo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fixflo-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fixflo-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fixflo-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fixflo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fixflo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fixflo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fixflo-api-v2-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fixflo/fixflo-public/collection/glxckcp/fixflo-docs
- group: company
  title: ''
  type: Website
  url: https://www.fixflo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.fixflo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.fixflo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.fixflo.com/72b66de24898e-welcome-to-fixflo
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.fixflo.com/5aaf5f6f6bc52-fixflo
- group: company
  title: ''
  type: Blog
  url: https://www.fixflo.com/blog
- group: operate
  title: ''
  type: SupportKnowledgeBase
  url: https://help.fixflo.com/support/home
- group: operate
  title: ''
  type: Support
  url: https://help.fixflo.com/support/solutions/articles/61000295569-api-faqs-commonly-asked-questions-when-creating-an-integration
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fixflo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fixflo.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.fixflo.com/support/fixflo-login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fixflo.com/legal-and-patents
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fixflo.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fixflo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fixflo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Fixflo
created: '2026-07-26'
description: Fixflo (a trading name of Tactile Limited, London, United Kingdom, acquired by Aareon in 2021) is a UK repairs, maintenance and compliance management platform for lettings agents, block managers and commercial property managers. Occupiers report issues through a guided fault tree, and Fixflo routes the work to contractors, tracks jobs, service programmes, warranties and invoices, and syncs the resulting records back into the agency CRM. It sits in the post-tenancy operations layer of the UK property value chain rather than the listings layer — the UK has no MLS and no RESO, so there is no industry-mandated machine-readable listing contract here and Fixflo makes no RESO claim. Its API posture is unusually open for the sector in one respect and closed in another. A genuinely public Stoplight developer portal at api-docs.fixflo.com publishes a complete OpenAPI 3.0 description of the v2 API (135 paths, 164 operations, 25 resource tags) that anyone can read and download without logging
  in, but actually calling it is licensed. Every use of the API is subject to the signed Fixflo Application Developer and API Licence Agreement, keys are issued by support after a review of the use case, and the runtime base URL is the customer's own per-tenant subdomain. Read the contract freely; sign an agreement to use it.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fixflo.png
layout: provider
mcp_servers:
- description: ''
  name: fixflo-mcp.yml
  slug: fixflo-mcpyml
modified: '2026-07-26'
name: Fixflo
nav: Providers
network: true
overview: 'Fixflo publishes 1 API on the [APIs.io](https://apis.io/) network: API v2. Tagged areas include Real Estate, United Kingdom, Property Management, PropTech, and Repairs and Maintenance.


  The Fixflo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fixflo''s developer surface includes authentication, sandbox, documentation, getting-started guide, API reference, engineering blog, support, and 31 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 1
  name: Fixflo Rate Limits
  slug: fixflo-rate-limits
scopes:
- name: Fixflo Scopes
  scope_count: 4
  slug: fixflo-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 56.2
  delta: -1.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.7
    developer_ergonomics: 73.4
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 57.9
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Fixflo Authentication
  slug: fixflo-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Fixflo Domain Security
  slug: fixflo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fixflo
tags:
- Real Estate
- United Kingdom
- Property Management
- PropTech
- Repairs and Maintenance
- Block Management
- Lettings
- Rentals
- Commercial Real Estate
- Contractors
website: https://www.fixflo.com/
---
