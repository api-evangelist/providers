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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Luminary Agentic Access
  operation_count: 31
  slug: luminary-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 6
apis:
- description: The Documents API from Luminary — 8 operation(s) for documents.
  name: Luminary Documents API
  slug: luminary-documents-api
- description: The Entities API from Luminary — 4 operation(s) for entities.
  name: Luminary Entities API
  slug: luminary-entities-api
- description: The Households API from Luminary — 5 operation(s) for households.
  name: Luminary Households API
  slug: luminary-households-api
- description: The Individuals API from Luminary — 3 operation(s) for individuals.
  name: Luminary Individuals API
  slug: luminary-individuals-api
- description: The Users API from Luminary — 2 operation(s) for users.
  name: Luminary Users API
  slug: luminary-users-api
- description: The Valuations API from Luminary — 1 operation(s) for valuations.
  name: Luminary Valuations API
  slug: luminary-valuations-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://withluminary.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withluminary
- group: company
  title: ''
  type: Blog
  url: https://withluminary.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://withluminary.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.withluminary.com
- group: operate
  title: ''
  type: Support
  url: https://withluminary.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withluminary.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withluminary.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://withluminary.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/luminary-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luminary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/luminary-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/luminary-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/luminary-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/luminary-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/luminary-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/luminary-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luminary-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/luminary-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luminary-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luminary-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luminary-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/luminary-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/luminary-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Luminary is AI-powered estate planning software for wealth advisors, family offices, attorneys, and professional services firms. It turns static estate planning documents into organized, digital records — with AI document digitization and summarization, dynamic estate flowcharts and waterfalls, scenario modeling, and role-based collaboration. Its public REST API (v1) exposes households, individuals, entities, documents, AI document summaries, and entity valuations so estate data can sync with CRMs, client portals, and planning tools. First-party TypeScript and Go SDKs are published on GitHub. OAuth2-secured (authorizationCode + clientCredentials) and SOC 2 Type II audited. Backed by 8vc.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luminary.png
layout: provider
mcp_servers:
- description: ''
  name: luminary-mcp.yml
  slug: luminary-mcpyml
modified: '2026-07-20'
name: Luminary
nav: Providers
network: true
overview: 'Luminary publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Entities API, Households API, and 3 more. Tagged areas include Company, Estate Planning, Wealth Management, Financial Services, and Legal Tech.


  Luminary''s developer surface includes engineering blog, pricing, support, authentication, and 21 more developer resources.'
random_paper: 69
scopes:
- name: Luminary Scopes
  scope_count: 4
  slug: luminary-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.3
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luminary/refs/heads/main/screenshots/luminary-2026-07-25T225714.png
security:
- kind: authentication
  name: Luminary Authentication
  slug: luminary-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Luminary Domain Security
  slug: luminary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Luminary Trust Center
  slug: luminary-trust-center
  summary_line: SOC 2
slug: luminary
tags:
- Company
- Estate Planning
- Wealth Management
- Financial Services
- Legal Tech
- Document AI
- Family Office
- OAuth2
website: https://withluminary.com
---
