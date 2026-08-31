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
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Shopify-native Universal Commerce Protocol (UCP) shopping surface for the Outlier storefront. Agents discover capabilities at /.well-known/ucp and transact via the hosted MCP endpoint (search_catalog,
  name: Outlier UCP Agent Commerce (MCP)
  slug: outlier-ucp-agent-commerce-mcp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outlier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.outlier.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.outlier.org/agents.md
- group: start
  title: ''
  type: Login
  url: https://www.outlier.org/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outlier.org/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outlier.org/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outlier-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outlier-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/outlier-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outlier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outlier-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outlier-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outlier-lifecycle.yml
created: '2026-07-17'
description: 'Outlier is a consumer online-education company that delivers college-level, for-credit courses (Calculus, Psychology, Financial Accounting, Computer Science, Astronomy, Business, and Professional Communication) to high-school and independent learners through dual-enrollment partnerships, offering transferable credit from an accredited university. Outlier was surfaced as a portfolio company of GV (Google Ventures). Its public storefront at www.outlier.org runs on Shopify and exposes a real agent-commerce surface: an llms.txt / agents.md instruction file, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a hosted UCP shopping MCP endpoint at /api/ucp/mcp, and Shopify Customer Account OpenID Connect discovery at /.well-known/openid-configuration. This profile was enriched from those publicly served surfaces; there is no first-party developer/API program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outlier.png
layout: provider
mcp_servers:
- description: ''
  name: Outlier MCP Server
  slug: outlier-mcp-server
modified: '2026-07-20'
name: Outlier
nav: Providers
network: true
overview: 'Outlier publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, Online Learning, and Dual Enrollment.


  Outlier''s developer surface includes documentation, authentication, and 11 more developer resources.'
random_paper: 16
scopes:
- name: Outlier Scopes
  scope_count: 4
  slug: outlier-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outlier/refs/heads/main/screenshots/outlier-2026-08-07T191059.png
security:
- kind: authentication
  name: Outlier Authentication
  slug: outlier-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Outlier Domain Security
  slug: outlier-domain-security
  summary_line: TLSv1.3 · HSTS
slug: outlier
tags:
- Company
- Consumer
- Education
- Online Learning
- Dual Enrollment
- E-Commerce
- Shopify
- Agent Commerce
- MCP
website: https://www.outlier.org
---
