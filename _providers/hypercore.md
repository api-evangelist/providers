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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Hypercore's production GraphQL API for private-credit loan management — a single GraphQL endpoint covering loans, equities, clients, funding sources, documents, statements, data tables, deal onboardin
  name: Hypercore GraphQL API
  slug: hypercore-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hypercore-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.hypercore.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hypercore.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hypercore.ai/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hypercore.ai/docs/api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/hypercore-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hypercore-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hypercore.ai/resources
- group: auth
  title: ''
  type: Security
  url: https://www.hypercore.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/hypercore-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.hypercore.ai/security
- group: design
  title: ''
  type: Conformance
  url: conformance/hypercore-conformance.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hypercore.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hypercore.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.hypercore.ai/contact-us
- group: design
  title: ''
  type: DataModel
  url: data-model/hypercore-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hypercore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hypercore-error-codes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypercore-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hypercore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hypercore-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Hypercore is a loan management and servicing platform built for private credit lenders, venture debt funds, and commercial real estate financiers. It manages loans end to end — from pipeline and deal onboarding through origination, funding-source allocation, servicing, and maturity — with automation, portfolio business intelligence, and an AI admin agent for loan workflows. The platform exposes a production GraphQL API (single endpoint at api.hypercore.ai/graphql, Docusaurus-documented at docs.hypercore.ai) covering loans, equities, clients, funding sources, documents, statements, data tables, notifications, imports, and a maker/checker change-request approval workflow. Hypercore is a Y Combinator and Insight Partners backed company headquartered in Tel Aviv, Israel, and is SOC 2 Type II certified.
image: https://cdn.prod.website-files.com/657c16376a943cd358275fbf/65b8e695eeb2a467898bbd02_Open%20graph.png
layout: provider
mcp_servers:
- description: ''
  name: Hypercore MCP Server
  slug: hypercore-mcp-server
modified: '2026-07-19'
name: Hypercore
nav: Providers
network: true
overview: 'Hypercore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loan Management, Private Credit, Lending, and Venture Debt.


  Hypercore''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, and 16 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 8.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hypercore/refs/heads/main/screenshots/hypercore-2026-07-25T221846.png
security:
- kind: authentication
  name: Hypercore Authentication
  slug: hypercore-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hypercore Domain Security
  slug: hypercore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hypercore Vulnerability Disclosure
  slug: hypercore-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Hypercore Trust Center
  slug: hypercore-trust-center
  summary_line: SOC 2 Type II
slug: hypercore
tags:
- Company
- Loan Management
- Private Credit
- Lending
- Venture Debt
- Commercial Real Estate
- Loan Servicing
- Fintech
- Financial-Services
- GraphQL
website: https://www.hypercore.ai/
---
