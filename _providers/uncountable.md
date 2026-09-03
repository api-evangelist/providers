---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Uncountable External API is the authenticated REST surface of the Uncountable R&D platform. Its documented entry point is the list_entities endpoint, which returns rows from a Listing Configuratio
  name: Uncountable External API
  slug: uncountable-external-api
- description: Uncountable ships a first-party hosted Model Context Protocol server at the /mcp path of each customer environment (https://app.uncountable.com/mcp for the US deployment, https://appeu.uncountable.com
  name: Uncountable MCP Server
  slug: uncountable-mcp
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.uncountable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.support.uncountable.com/knowledge-base/
- group: docs
  title: ''
  type: APIReference
  url: https://app.uncountable.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.support.uncountable.com/
- group: company
  title: ''
  type: Blog
  url: https://www.uncountable.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.support.uncountable.com/article-categories/getting-started/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uncountable-changelog.yml
- group: start
  title: ''
  type: Login
  url: https://app.uncountable.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uncountable.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uncountable.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.uncountable.com/uncountable-security
- group: auth
  title: ''
  type: Compliance
  url: https://www.uncountable.com/uncountable-security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uncountable-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uncountable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uncountable-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uncountable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uncountable-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/uncountable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uncountable-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uncountable-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uncountable-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uncountable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/uncountable-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uncountable-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uncountable-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uncountable-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uncountable-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/uncountable-packages.yml
created: '2026-09-01'
description: Uncountable is a unified laboratory informatics and R&D data platform for enterprise research organizations, replacing disconnected LIMS, ELN, QMS and PLM tools with a single cloud system that centralizes experimental data, accelerates formulation work, and supports AI-driven discovery across chemicals, advanced materials, batteries, plastics, coatings, food and life sciences. The platform is delivered as a multi-region SaaS application (US and EU deployments) and exposes an authenticated External API plus a hosted, OAuth-protected Model Context Protocol (MCP) server so agents and integration tooling can read platform data, alongside SFTP and instrument/ERP connectors.
image: https://cdn.prod.website-files.com/5dd1e506c5a7edfbd95f37e2/64138d793d519dafccc6295f_opengraph.png
layout: provider
mcp_servers:
- description: A first-party, hosted Model Context Protocol server exposed at the /mcp path of every Uncountable environment. It is a remote endpoint an MCP client POSTs to directly — there is no npx/pip package and
  name: Uncountable MCP Server
  slug: uncountable-mcp-server
modified: '2026-09-01'
name: Uncountable
nav: Providers
network: true
overview: 'Uncountable publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Laboratory Informatics, LIMS, Electronic Lab Notebook, and R&D Data Management.


  Uncountable''s developer surface includes documentation, API reference, support, engineering blog, getting-started guide, changelog, authentication, and 22 more developer resources.'
plans:
- name: Uncountable Plans Pricing
  plan_count: 0
  slug: uncountable-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Uncountable Rate Limits
  slug: uncountable-rate-limits
scopes:
- name: Uncountable Scopes
  scope_count: 0
  slug: uncountable-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uncountable/refs/heads/main/screenshots/uncountable-2026-09-02T164847.png
security:
- kind: authentication
  name: Uncountable Authentication
  slug: uncountable-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Uncountable Domain Security
  slug: uncountable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uncountable Vulnerability Disclosure
  slug: uncountable-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Uncountable Trust Center
  slug: uncountable-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO 22301:2019, GDPR, 21 CFR Part 11, EU GMP Annex 11, ISO/IEC 17025
slug: uncountable
tags:
- Company
- Laboratory Informatics
- LIMS
- Electronic Lab Notebook
- R&D Data Management
- Product Lifecycle Management
- Quality Management
- Materials Science
- Chemicals
- Artificial Intelligence
- Model Context Protocol
website: https://www.uncountable.com/
---
