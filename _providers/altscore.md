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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Alternative-data aggregation for credit underwriting and scoring. Aggregates over 50 data sources into on-demand data requests that feed borrower enrichment and decisioning.
  name: AltData API
  slug: altdata-api
- description: Onboarding, KYC/KYB, identities, documents, deals, forms, workflows (v1 + v2), credit decisioning, evaluators, and policy rules. The default module of the AltScore SDK and CLI.
  name: Borrower Central API
  slug: borrower-central-api
- description: The loan lifecycle system — partners, clients, credit accounts, debts, disbursements, disbursement accounts, payment accounts, payment orders, and DPAs (payment agreements). Includes the webhooks surf
  name: Credit Management System API
  slug: credit-management-system-api
artifact_total: 9
asyncapis:
- description: ''
  name: Altscore Webhooks
  slug: altscore-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/altscore-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://altscore.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.altscore.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.altscore.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.altscore.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.altscore.ai/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AltScore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altscore.ai/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altscore.ai/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.altscore.ai/en/#contacto
- group: auth
  title: ''
  type: Compliance
  url: https://www.altscore.ai/en/security
- group: build
  title: ''
  type: Postman
  url: https://docs.altscore.ai/
- group: build
  title: ''
  type: Packages
  url: packages/altscore-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/altscore-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/altscore-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/altscore-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/altscore-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/altscore-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/altscore-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altscore-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altscore-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/altscore-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/altscore-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/altscore-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/altscore-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/altscore-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/altscore-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altscore-domain-security.yml
created: '2026-07-17'
description: 'AltScore is a B2B credit infrastructure platform for Latin America — the "Rails of Lending" that lets any company build, embed, and deploy credit products in weeks instead of years. Its API surface spans three products: AltData, an aggregation layer over 50+ alternative and traditional data sources for underwriting and scoring; Borrower Central, an onboarding, KYC/KYB, identity, document, and workflow/decisioning engine; and a Credit Management System for the full loan lifecycle — disbursements, credit accounts, debts, payment orders, and DPAs. Access is through first-party Python and TypeScript SDKs, a Go CLI, and a Frontegg-backed OAuth/OIDC identity layer, with a dedicated sandbox environment and an in-production test mode (isTest) for UAT.'
image: https://altscore.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: altscore-mcp.yml
  slug: altscore-mcpyml
modified: '2026-07-17'
name: AltScore
nav: Providers
network: true
overview: 'AltScore publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Credit, Lending, Fintech, and Credit Scoring.


  The AltScore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AltScore''s developer surface includes documentation, API reference, engineering blog, support, CLI, authentication, sandbox, and 22 more developer resources.'
random_paper: 14
scopes:
- name: Altscore Scopes
  scope_count: 3
  slug: altscore-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 51.1
  delta: 3.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.6
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 47.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altscore/refs/heads/main/screenshots/altscore-2026-07-25T195844.png
security:
- kind: authentication
  name: Altscore Authentication
  slug: altscore-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Altscore Domain Security
  slug: altscore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Altscore Trust Center
  slug: altscore-trust-center
  summary_line: ISO 27001:2022, SOC 2
slug: altscore
tags:
- Company
- Credit
- Lending
- Fintech
- Credit Scoring
- Underwriting
- KYC
- Financial Services
- Latin America
- Data Aggregation
- Workflows
- Decisioning
website: https://altscore.ai/
---
