---
access_model:
  confidence: medium
  label: Sales-gated with self-service trial
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.deepip.ai/trial
  - https://www.deepip.ai/self-service-payment
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 25.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'A remote Model Context Protocol server operated by DeepIP at https://app.deepip.ai/mcp, letting an MCP-capable agent act inside a DeepIP tenant on behalf of a signed-in user. It is protected by OAuth '
  name: DeepIP MCP Server
  slug: deepip-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.deepip.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.deepip.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.deepip.ai/contact
- group: auth
  title: ''
  type: TrustCenter
  url: security/deepip-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.deepip.ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/deepip-conformance.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepip.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepip.ai/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.deepip.ai/trial
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepip-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deepip.ai
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deepip-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deepip-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepip-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deepip-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deepip-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deepip-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepip-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deepip-plans-pricing.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/deepip-app-robots.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deepip-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deepip-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepip-domain-security.yml
created: '2026-07-17'
description: DeepIP is an AI-powered patent intelligence platform that streamlines the full patent lifecycle for intellectual-property professionals, automating repetitive work while keeping a human in the loop. It supports invention capture, patentability assessment, patent drafting and drawings generation, AI review, prosecution support, freedom-to-operate (FTO) and invalidity searches, portfolio and landscape intelligence, and agentic prior-art search. DeepIP embeds directly into Microsoft Word, IP management systems, and the web browser, and works across chemistry, biology, software, mechanical, and electronic domains and multiple patent jurisdictions (USPTO, EPO, PCT, UKIPO, CNIPA, KIPO, and others). The company operates a zero-data-retention policy on Microsoft Azure across separate EU and US stacks, and holds SOC 2 Type II, ISO 27001, ISO 42001, HIPAA, and GDPR compliance. DeepIP runs a remote, OAuth-protected Model Context Protocol server at app.deepip.ai/mcp; its REST API reference
  sits behind a ReadMe login. DeepIP is backed by Balderton Capital.
image: https://cdn.prod.website-files.com/655793df06a490569c80c9da/656dfeb7474277cde1d95475_Webclip.png
layout: provider
mcp_servers:
- description: ''
  name: DeepIP MCP Server
  slug: deepip-mcp-server
modified: '2026-08-17'
name: DeepIP
nav: Providers
network: true
overview: 'DeepIP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Intellectual Property, Patents, Legal Tech, and Artificial Intelligence.


  DeepIP''s developer surface includes engineering blog, support, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Deepip Plans Pricing
  plan_count: 0
  slug: deepip-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Deepip Rate Limits
  slug: deepip-rate-limits
scopes:
- name: Deepip Scopes
  scope_count: 14
  slug: deepip-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepip/refs/heads/main/screenshots/deepip-2026-07-25T211555.png
security:
- kind: authentication
  name: Deepip Authentication
  slug: deepip-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Deepip Domain Security
  slug: deepip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Deepip Trust Center
  slug: deepip-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 42001, HIPAA, GDPR
slug: deepip
tags:
- Company
- Intellectual Property
- Patents
- Legal Tech
- Artificial Intelligence
- Patent Drafting
- IP Management
- Document Automation
- Security
- MCP
- Agents
- Prior Art Search
website: https://www.deepip.ai/
---
