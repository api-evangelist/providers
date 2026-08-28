---
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
    error_semantics: documented
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
  score: 28.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Malt Agentic Access
  operation_count: 13
  slug: malt-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 1
apis:
- description: Malt's publicly documented API surface, served from api.malt.com and documented with Stoplight Elements against a single unified OpenAPI 3.0.3 document ("Malt - API Guidelines", 13 operations). Two ca
  name: Malt Exposed APIs
  slug: malt-exposed-apis
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.malt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.malt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.malt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.malt.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.malt.com/
- group: operate
  title: ''
  type: Support
  url: https://help.malt.com/kb/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.malt.com/kb/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.malt.engineering/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.malt.engineering/feed
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.malt.com/fr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Maltcommunity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.malt.com/c/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.malt.com/who-are-you
- group: start
  title: ''
  type: Login
  url: https://www.malt.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.malt.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.malt.com/about/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.malt.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.malt.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/malt-exposed-apis-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/malt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/malt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/malt-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/malt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/malt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/malt-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/malt-exposed-apis-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/malt-packages.yml
- group: design
  title: ''
  type: Components
  url: components/malt-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/malt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/malt-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/malt-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/malt-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/malt-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/malt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/malt-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/malt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/malt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/malt-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/malt-agentic-access.yml
created: '2026-08-17'
description: 'Malt is a European freelance marketplace and Freelance Management System (FMS) founded in 2013 in Paris by Vincent Huguet and Hugo Lassiege, connecting more than a million independent consultants across tech, data, AI, design, marketing and management with enterprise buyers. Beyond matching, the platform handles the administrative spine of freelance engagement: quotes, automated contracts and NDAs, timesheets, invoicing, insured payments and compliance checks, plus an enterprise tier that consolidates an existing freelance roster (Malt Open) and plugs into 85+ ERP, procurement and HR systems including SAP Fieldglass, Coupa and Workday. Malt publishes a small, credential-gated public API surface at api.malt.com documented with Stoplight Elements: a freelancer billing API (invoices, service charge invoices, payments, invoice PDFs) and a SCIM 2.0 user-provisioning endpoint for enterprise identity lifecycle management.'
image: https://dam.malt.com/rebranding2020/malt-logo/malt-brew-only
layout: provider
mcp_servers:
- description: ''
  name: Malt MCP Server
  slug: malt-mcp-server
modified: '2026-08-17'
name: Malt
nav: Providers
network: true
overview: 'Malt publishes 1 API on the [APIs.io](https://apis.io/) network: Exposed APIs. Tagged areas include Company, Marketplace, Freelance Marketplace, Freelance Management System, and Talent Marketplace.


  Malt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Malt Plans Pricing
  plan_count: 3
  slug: malt-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Malt Rate Limits
  slug: malt-rate-limits
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 65.6
    developer_ergonomics: 58.9
    discoverability: 79.6
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 59.5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Malt Authentication
  slug: malt-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Malt Domain Security
  slug: malt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Malt Vulnerability Disclosure
  slug: malt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: malt
tags:
- Company
- Marketplace
- Freelance Marketplace
- Freelance Management System
- Talent Marketplace
- Workforce Management
- Contingent Workforce
- Invoicing
- Payments
- SCIM
- Identity Provisioning
- Procurement
- Future Of Work
- France
- Europe
website: https://www.malt.com/
---
