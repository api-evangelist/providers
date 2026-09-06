---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Simetrik''s hosted remote Model Context Protocol server. An MCP client adds one URL and signs in with a Simetrik account over OAuth 2.1 (authorization code + PKCE, dynamic client registration) - there '
  name: Simetrik MCP Server
  slug: simetrik-mcp-server
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simetrik-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://simetrik.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.simetrik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simetrik.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simetrik.com/cli/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simetrik.com/cli/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://simetrik.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://simetrik.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simetrik-inc
- group: start
  title: ''
  type: SignUp
  url: https://simetrik.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://app.simetrik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simetrik.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simetrik.com/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simetrik.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.simetrik.com/
- group: auth
  title: ''
  type: Compliance
  url: https://simetrik.com/security/
- group: auth
  title: ''
  type: Security
  url: https://simetrik.com/information-security-privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simetrik-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/simetrik-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/simetrik-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simetrik-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simetrik-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simetrik-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/simetrik-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simetrik-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/simetrik-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simetrik-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simetrik-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simetrik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simetrik-rate-limits.yml
created: '2026-08-27'
description: 'Simetrik is an AI-powered financial control and reconciliation platform, founded in Bogota, Colombia, that sits underneath a company''s finance stack and reconciles transactions across payment gateways, banks, card networks, ERPs, internal ledgers and operational systems. The platform pairs a no-code reconciliation engine (native sources, segments, calculated columns, unions, joins, groups, standard and advanced reconciliations, sweeps, compensations, consolidations, opening records and data exports) with an Accounting Translator, an Operation Center, scheduling, alarms and approvals. Its developer surface is deliberately agent-first rather than REST-first: Simetrik publishes a cross-platform `simetrik` CLI, a versioned Claude Agent Skill bundle shipped in lockstep with that CLI, and a hosted remote MCP server at https://mcp.us.simetrik.com/mcp that an MCP client connects to with a single URL and an OAuth sign-in, with no API key to create or rotate. Customers are concentrated
  in payments and financial services: PSPs, acquirers, issuers, marketplaces, neobanks, banks and retailers.'
image: https://simetrik.com/wp-content/uploads/2026/07/cropped-simetrik_logo-192x192.png
layout: provider
mcp_servers:
- description: Simetrik's first-party hosted MCP server. The provider's own framing is "connect Claude - or any MCP client - to Simetrik with one URL. No install, no terminal, no API key." The server acts as the sig
  name: Simetrik MCP Server
  slug: simetrik-mcp-server
modified: '2026-08-27'
name: Simetrik
nav: Providers
network: true
overview: 'Simetrik publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reconciliation, Financial Operations, Payments, and Accounting.


  Simetrik''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Simetrik Plans Pricing
  plan_count: 0
  slug: simetrik-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Simetrik Rate Limits
  slug: simetrik-rate-limits
scopes:
- name: Simetrik Scopes
  scope_count: 0
  slug: simetrik-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 48.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simetrik/refs/heads/main/screenshots/simetrik-2026-09-02T155523.png
security:
- kind: authentication
  name: Simetrik Authentication
  slug: simetrik-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Simetrik Domain Security
  slug: simetrik-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Simetrik Trust Center
  slug: simetrik-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 27018, SOC 1 Type 2, SOC 2 Type 2, SOC 3, PCI DSS
slug: simetrik
tags:
- Company
- Reconciliation
- Financial Operations
- Payments
- Accounting
- Fintech
- Financial Close
- Data Integration
- Agents
- MCP
- Latin America
website: https://simetrik.com/
---
