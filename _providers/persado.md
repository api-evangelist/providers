---
access_model:
  confidence: high
  label: Enterprise Contract
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.persado.com/contact
  - https://api.persado.com/.well-known/oauth-protected-resource
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'A production remote Model Context Protocol server operated by Persado at https://api.persado.com/mcp. Discovered by probing the API host: the RFC 9728 protected-resource document names the resource ve'
  name: Persado MCP Gateway
  slug: persado-mcp-gateway
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.persado.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/persado-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/persado-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/persado-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/persado-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/persado-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/persado-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/persado-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/persado-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/persado-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/persado-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/persado-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/persado-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/persado-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.persado.com/platform
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/persado
- group: company
  title: ''
  type: Blog
  url: https://www.persado.com/articles
- group: start
  title: ''
  type: Login
  url: https://myaccount.persado.com/realms/persado-portal/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.persado.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.persado.com/legal/privacy-policy
created: '2026-07-17'
description: Persado is an enterprise AI platform for regulated brands that generates, scores, and deploys compliant marketing and customer-communication language at scale, serving banking, credit cards, credit unions, fintech, insurance, and mortgage. Its products — Create, Optimize, and Automate — combine domain-specific language models with a multi-agent performance, brand, and compliance review, and deploy through native connectors for Salesforce Marketing Cloud, Adobe Campaign, Adobe Target, Braze, Responsys, and Optimizely. Persado runs a production remote Model Context Protocol server, the "Persado MCP Gateway", at https://api.persado.com/mcp, protected by OAuth 2.1 with PKCE, dynamic client registration, and an mcp:tools scope issued by a Keycloak realm on myaccount.persado.com. That agent surface is undocumented — Persado publishes no developer portal, API reference, OpenAPI, or pricing — and was found by probing the API host directly. Persado also ships a first-party Enterprise
  API Mobile SDK for iOS and Android, though neither build is installable from a public package registry. This profile was surfaced as a portfolio company of bain-capital-ventures and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/persado.png
layout: provider
mcp_servers:
- description: ''
  name: Persado MCP Gateway (Production)
  slug: persado-mcp-gateway-production
modified: '2026-08-13'
name: Persado
nav: Providers
network: true
overview: 'Persado publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Artificial Intelligence, Generative AI, and Marketing.


  Persado''s developer surface includes authentication, engineering blog, and 18 more developer resources.'
plans:
- name: Persado Plans Pricing
  plan_count: 0
  slug: persado-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Persado Rate Limits
  slug: persado-rate-limits
scopes:
- name: Persado Scopes
  scope_count: 3
  slug: persado-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/persado/refs/heads/main/screenshots/persado-2026-09-02T151105.png
security:
- kind: authentication
  name: Persado Authentication
  slug: persado-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Persado Domain Security
  slug: persado-domain-security
  summary_line: TLSv1.3 · DMARC
slug: persado
tags:
- Company
- Ai Apps
- Artificial Intelligence
- Generative AI
- Marketing
- Customer Engagement
- Content Generation
- Personalization
- Agents
- MCP
- Compliance
- Financial-Services
website: https://www.persado.com/
---
