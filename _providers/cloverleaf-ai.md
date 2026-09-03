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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 27.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: A remote, OAuth-protected Model Context Protocol server that exposes Cloverleaf AI's government meeting intelligence to AI agents and assistants. Found by host discovery (mcp.cloverleaf.ai) rather tha
  name: Cloverleaf AI MCP Server
  slug: cloverleaf-ai-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloverleaf-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloverleaf.ai/
- group: other
  title: ''
  type: HowItWorks
  url: https://www.cloverleaf.ai/how-it-works/
- group: start
  title: ''
  type: SignUp
  url: https://www.cloverleaf.ai/get-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cloverleaf.ai/get-started/
- group: start
  title: ''
  type: Demo
  url: https://www.cloverleaf.ai/get-a-demo/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cloverleaf.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloverleaf.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloverleaf.ai/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloverleaf-ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@cloverleaf.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloverleaf-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloverleaf-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloverleaf-ai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloverleaf-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloverleaf-ai-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloverleaf-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloverleaf.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/cloverleaf-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloverleaf-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloverleaf-ai-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloverleaf-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloverleaf-ai-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://app.cloverleaf.ai/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cloverleaf.ai/feed/
created: '2026-07-17'
description: Cloverleaf AI is a business-to-government (B2G) sales intelligence platform, headquartered in Denver, Colorado, that monitors 45,000+ government organizations across federal, state, local, and education (SLED) agencies and turns 1.5 million public government meetings into pre-RFP buying signals. It analyzes committee meetings, budget discussions, and procurement activity, applies custom speech-to-text and speaker "vocal fingerprinting" (70,000+ verified speakers) to attribute officials' positions, and delivers a prioritized, territory-specific daily brief to each seller, synced to Salesforce, so government contractors reach buyers before the RFP is published. Products include the Opportunity Database and Vocal Fingerprinting. Cloverleaf AI is Techstars-backed and raised seed funding led by Jackson Square Ventures. It publishes no REST API, OpenAPI, SDK or developer portal, but it does operate a remote, OAuth-protected Model Context Protocol (MCP) server at mcp.cloverleaf.ai
  that exposes the platform to AI agents — an agent surface the company documents nowhere on its own site. The platform is otherwise delivered as a SaaS product with a Salesforce integration and a demo-request sales motion.
image: https://www.cloverleaf.ai/wp-content/uploads/cloverleaf-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Cloverleaf AI MCP Server
  slug: cloverleaf-ai-mcp-server
modified: '2026-08-14'
name: Cloverleaf AI
nav: Providers
network: true
overview: 'Cloverleaf AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, B2G, Sales Intelligence, and Public Sector.


  Cloverleaf AI''s developer surface includes signup flow, getting-started guide, support, authentication, and 21 more developer resources.'
plans:
- name: Cloverleaf Ai Plans Pricing
  plan_count: 0
  slug: cloverleaf-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Cloverleaf Ai Rate Limits
  slug: cloverleaf-ai-rate-limits
scopes:
- name: Cloverleaf Ai Scopes
  scope_count: 4
  slug: cloverleaf-ai-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 64.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloverleaf-ai/refs/heads/main/screenshots/cloverleaf-ai-2026-07-25T205722.png
security:
- kind: authentication
  name: Cloverleaf Ai Authentication
  slug: cloverleaf-ai-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cloverleaf Ai Domain Security
  slug: cloverleaf-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cloverleaf Ai Trust Center
  slug: cloverleaf-ai-trust-center
  summary_line: trust center published
slug: cloverleaf-ai
tags:
- Company
- Government
- B2G
- Sales Intelligence
- Public Sector
- GovTech
- Procurement
- RFP
- Legislative Intelligence
- Speech-to-Text
- Artificial Intelligence
website: https://www.cloverleaf.ai/
---
