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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Generate signed URLs for embedding Zenlytic content in host apps.
  name: Zenlytic Embedding API
  slug: zenlytic-embedding-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.zenlytic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zenlytic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zenlytic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zenlytic.com/embedding/signed_embedding
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zenlytic.com/getting-started/start_here
- group: operate
  title: ''
  type: Support
  url: https://support.zenlytic.com/
- group: company
  title: ''
  type: Blog
  url: https://zenlytic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zenlytic
- group: start
  title: ''
  type: SignUp
  url: https://app.zenlytic.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.zenlytic.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenlytic.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.zenlytic.com/legal-and-support/legal/terms-of-service-agreement
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zenlytic-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenlytic-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/zenlytic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zenlytic-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenlytic-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenlytic-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zenlytic-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/zenlytic-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Zenlytic is an AI-powered business intelligence platform built around Zoë, an autonomous AI data analyst that turns natural-language questions into verified, governed insights and business-ready artifacts (dashboards, decks, models, and reports). It connects to cloud warehouses (Snowflake, BigQuery, Redshift, Databricks, Azure Synapse), builds a semantic context layer from schemas and query history, and answers with full lineage so every result is traceable to its source tables, filters, and metrics. Developers integrate Zenlytic through its open-source metrics-layer Python library, an iframe embedding surface with a signed-URL REST endpoint for external users, SSO (Microsoft Entra, Okta), and experimental MCP connectors that let Zoë call tools in the surrounding data stack. Zenlytic is backed by Bain Capital Ventures.
image: https://zenlytic.com/assets/images/social-card.png
layout: provider
modified: '2026-07-21'
name: Zenlytic
nav: Providers
network: true
overview: 'Zenlytic publishes 1 API on the [APIs.io](https://apis.io/) network: Embedding API. Tagged areas include Company, Commerce, Business Intelligence, Analytics, and Artificial Intelligence.


  Zenlytic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 14 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 45.6
  delta: -2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.3
    developer_ergonomics: 60.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 47.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zenlytic Authentication
  slug: zenlytic-authentication
  summary_line: http-basic/sso-saml-oidc/signed-jwt · 4 schemes
- kind: domain-security
  name: Zenlytic Domain Security
  slug: zenlytic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenlytic
tags:
- Company
- Commerce
- Business Intelligence
- Analytics
- Artificial Intelligence
- Data
- Embedded Analytics
- MCP
website: https://www.zenlytic.com/
---
