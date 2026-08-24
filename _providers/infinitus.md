---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The customer-gated Infinitus backend API. Infinitus' own AI Agent Security Guide instructs customers to allowlist https://api.infinitusai.com on TCP 443 for "portal and backend API access". Probing co
  name: Infinitus Platform API
  slug: platform-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.infinitus.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.infinitus.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.infinitus.ai/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.infinitus.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infinitus.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infinitus.ai/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.infinitus.ai/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.infinitus.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/infinitus-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infinitus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infinitus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infinitus-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://support.infinitus.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infinitusai
- group: start
  title: ''
  type: Login
  url: https://customer.infinitusai.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infinitus-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infinitus-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infinitus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infinitus-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infinitus-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infinitus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infinitus-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/infinitus-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/infinitus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infinitus-rate-limits.yml
created: '2026-07-17'
description: 'Infinitus Systems is a safety-first healthcare voice AI platform that automates outbound and inbound phone calls to patients, payors, and providers for clinical and administrative tasks including benefit verification, prior authorization, prescription follow-up, and patient engagement. Its products include AI Agents (autonomous call handling), AI Copilots (human-assisted tools), Studio (a no-code agent builder), and Lens (conversation analysis and real-time clinical risk detection), backed by a healthcare knowledge graph. Benefit verifications are submitted individually or in bulk through the customer portal, CSV upload, or a customer-gated REST and GraphQL API at api.infinitusai.com, with a packaged Salesforce Life Sciences Cloud, Health Cloud, and Agentforce integration. Infinitus operates no public developer portal and publishes no OpenAPI: every API endpoint requires an authenticated customer account. It is SOC 2 Type II certified and signs HIPAA Business Associate Agreements.
  The company is backed by GV and Kleiner Perkins.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infinitus.png
layout: provider
mcp_servers:
- description: ''
  name: Infinitus MCP Server
  slug: infinitus-mcp-server
modified: '2026-08-15'
name: Infinitus
nav: Providers
network: true
overview: 'Infinitus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Voice AI, and Benefit Verification.


  Infinitus'' developer surface includes pricing, engineering blog, support, documentation, authentication, and 20 more developer resources.'
plans:
- name: Infinitus Plans Pricing
  plan_count: 0
  slug: infinitus-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Infinitus Rate Limits
  slug: infinitus-rate-limits
scopes:
- name: Infinitus Scopes
  scope_count: 1
  slug: infinitus-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 36.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infinitus/refs/heads/main/screenshots/infinitus-2026-07-25T222407.png
security:
- kind: authentication
  name: Infinitus Authentication
  slug: infinitus-authentication
  summary_line: oauth2/openIdConnect/saml2/http · 0 schemes
- kind: domain-security
  name: Infinitus Domain Security
  slug: infinitus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Infinitus Vulnerability Disclosure
  slug: infinitus-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Infinitus Trust Center
  slug: infinitus-trust-center
  summary_line: SOC 2 Type II, HIPAA Business Associate, CCPA
slug: infinitus
tags:
- Company
- Artificial Intelligence
- Healthcare
- Voice AI
- Benefit Verification
- Prior Authorization
- HIPAA
website: https://www.infinitus.ai
---
