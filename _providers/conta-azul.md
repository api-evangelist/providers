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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Conjunto de recursos para acompanhar e administrar operações relacionadas ao gerenciamento de baixas - esses recursos incluem criar uma nova baixa, retornar as baixas pelo id da parcela, atualizar par
  name: Conta Azul v1 API
  slug: conta-azul-v1-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Baixas v1 API
  slug: open-conta-azul-v1-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/conta-azul-acquittance-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conta-azul-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.contaazul.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.contaazul.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.contaazul.com/docs/financial-apis-openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.contaazul.com/guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/conta-azul-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/conta-azul-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conta-azul-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conta-azul-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conta-azul-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conta-azul-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contaazul.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.contaazul.com/migration
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conta-azul-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conta-azul-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conta-azul-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conta-azul-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/conta-azul-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/conta-azul-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://ajuda.contaazul.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://blog.contaazul.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ContaAzul
- group: commercial
  title: ''
  type: Pricing
  url: https://contaazul.com/planos/
- group: start
  title: ''
  type: SignUp
  url: https://developers-portal.contaazul.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contaazul.com/termos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contaazul.com/termos/privacidade/
- group: company
  title: ''
  type: Website
  url: https://contaazul.com
created: '2026-07-17'
description: 'Conta Azul is a Brazilian cloud accounting, financial-management and ERP platform for small and medium businesses, backed by Ribbit Capital. Its Nova API (v2, api-v2.contaazul.com) exposes the ERP over REST/JSON with OAuth 2.0 (AWS Cognito) authorization: financial events (accounts payable and receivable), installments, cost centers, categories and DRE, financial accounts and balances, sales, charges, products/inventory, proposals, contracts and settlements (baixas). The legacy API was sunset in November 2025 in favor of this versioned, OpenAPI-documented platform.'
image: https://contaazul.com/wp-content/themes/contaazul/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Conta Azul MCP Server
  slug: conta-azul-mcp-server
modified: '2026-07-18'
name: Conta Azul
nav: Providers
network: true
overview: 'Conta Azul publishes 1 API on the [APIs.io](https://apis.io/) network: v1 API. Tagged areas include Company, Fintech, Accounting, ERP, and Brazil.


  Conta Azul''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 22 more developer resources.'
random_paper: 14
scopes:
- name: Conta Azul Scopes
  scope_count: 3
  slug: conta-azul-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 54.4
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 56.7
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 54.4
  provenance:
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
    score: 54.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conta-azul/refs/heads/main/screenshots/conta-azul-2026-07-25T210322.png
security:
- kind: authentication
  name: Conta Azul Authentication
  slug: conta-azul-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Conta Azul Domain Security
  slug: conta-azul-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: conta-azul
tags:
- Company
- Fintech
- Accounting
- ERP
- Brazil
- Small Business
- Financial Management
- Invoicing
- Payments
website: https://contaazul.com
---
