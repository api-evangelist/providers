---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.7
  scored_at: '2026-09-20'
api_count: 2
apis:
- baseURL: https://api.getemboss.ai
  baseurl_source: declared
  description: 'The authenticated developer API on api.getemboss.ai: create fillable forms (or start from the public library of US federal forms), fill them from data with a standard-fill session or from documents wi'
  name: Emboss Account API
  slug: emboss-account-api
- baseURL: https://api.getemboss.ai/pay
  baseurl_source: declared
  description: 'The anonymous pay door at api.getemboss.ai/pay: make fillable, fill from data, fill with context, read a filled form back, and fax, each priced per job by page count, plus a free stateless quote. No a'
  name: Emboss Pay-per-call API
  slug: emboss-pay-per-call-api
- description: 'Remote Model Context Protocol server at https://api.getemboss.ai/mcp (Streamable HTTP) exposing twenty form-filling tools under forms:read / forms:write scopes. OAuth 2.1 with PKCE and dynamic client '
  name: Emboss MCP Server
  slug: emboss-mcp-server
- description: Agent2Agent interface at https://api.getemboss.ai/a2a (JSON-RPC, A2A 1.0) discovered through a signed agent card served at /.well-known/agent-card.json on both getemboss.ai and api.getemboss.ai. Twent
  name: Emboss A2A Agent
  slug: emboss-a2a-agent
artifact_total: 13
asyncapis:
- description: ''
  name: Getemboss Ai Callbacks
  slug: getemboss-ai-callbacks
common:
- group: company
  title: ''
  type: Website
  url: https://getemboss.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getemboss.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://getemboss.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://getemboss.ai/docs/reference/create-form
- group: start
  title: ''
  type: GettingStarted
  url: https://getemboss.ai/docs/quickstart
- group: start
  title: ''
  type: Console
  url: https://api.getemboss.ai/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetEmboss-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://getemboss.ai/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://api.getemboss.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://getemboss.ai/signup
- group: start
  title: ''
  type: Login
  url: https://getemboss.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getemboss.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getemboss.ai/privacy
- group: other
  title: ''
  type: Glossary
  url: https://getemboss.ai/glossary
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/llms/getemboss-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getemboss-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://getemboss.ai/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api.getemboss.ai/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/packages/getemboss-ai-packages.yml
  title: ''
  type: Packages
  url: packages/getemboss-ai-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/well-known/getemboss-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getemboss-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/well-known/getemboss-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getemboss-ai-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://getemboss.ai/.well-known/security.txt
- group: other
  title: ''
  type: AICatalog
  url: https://getemboss.ai/.well-known/ard.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/mcp/getemboss-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/getemboss-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/mcp/getemboss-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/getemboss-ai-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/a2a/getemboss-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getemboss-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/conformance/getemboss-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getemboss-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/authentication/getemboss-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getemboss-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/scopes/getemboss-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getemboss-ai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/conventions/getemboss-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getemboss-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/conventions/getemboss-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/getemboss-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/errors/getemboss-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getemboss-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/lifecycle/getemboss-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getemboss-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/changelog/getemboss-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getemboss-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/data-model/getemboss-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getemboss-ai-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/plans/getemboss-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getemboss-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/rate-limits/getemboss-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getemboss-ai-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/sandbox/getemboss-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/getemboss-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/asyncapi/getemboss-ai-callbacks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getemboss-ai-callbacks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/overlays/getemboss-ai-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getemboss-ai-account-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/overlays/getemboss-ai-pay-per-call-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getemboss-ai-pay-per-call-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/security/getemboss-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getemboss-ai-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://getemboss.ai/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/security/getemboss-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getemboss-ai-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getemboss-ai/refs/heads/main/regulatory/getemboss-ai-regulatory-posture.yml
  title: ''
  type: Regulatory
  url: regulatory/getemboss-ai-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://getemboss.ai/subprocessors
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://getemboss.ai/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://getemboss.ai/subprocessors
- group: other
  title: ''
  type: AITransparency
  url: https://getemboss.ai/docs/ephemeral-processing
created: '2026-09-19'
description: 'Emboss is a PDF form-filling API for developers and agents. Hand it a flat or scanned PDF and it detects the fields and returns a fillable AcroForm, fills the form from structured values or from supporting documents (proposing every answer with its source, asking about what is missing), verifies the result, reads a filled form back into labelled values, batch-fills one copy per spreadsheet row, packages the filled form with its attachments and a receipt, and faxes the result to any US, Canadian or Mexican fax number. Usage-based pricing in cents with a monthly free allowance and no subscription. The same engine is exposed through four doors on api.getemboss.ai: a 115-operation authenticated REST API (OpenAPI 3.1, Bearer API key or OAuth 2.1 with dynamic client registration), a remote MCP server (20 tools, OAuth-protected, listed in the MCP registry), a signed A2A 1.0 agent card with 23 skills, and an anonymous pay-per-call door priced per job over x402 (USDC on Base) or MPP
  (Tempo stablecoin or card). Every document is deleted 60-70 minutes after the last activity under ephemeral processing.'
image: https://getemboss.ai/emboss-logo-512.png
layout: provider
mcp_servers:
- description: ''
  name: Emboss MCP Server
  slug: emboss-mcp-server
- description: ''
  name: Emboss MCP Server
  slug: emboss-mcp-server-2
modified: '2026-09-19'
name: Emboss
nav: Providers
network: true
overview: 'Emboss publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Pay-per-call API. Tagged areas include PDF, Forms, Document Processing, Form Filling, and Fax.


  The Emboss catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Emboss'' developer surface includes documentation, API reference, getting-started guide, developer console, pricing, signup flow, authentication, and 42 more developer resources.'
plans:
- name: Getemboss Ai Plans Pricing
  plan_count: 3
  slug: getemboss-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Getemboss Ai Rate Limits
  slug: getemboss-ai-rate-limits
scopes:
- name: Getemboss Ai Scopes
  scope_count: 2
  slug: getemboss-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 67.9
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 59.0
    developer_ergonomics: 58.9
    discoverability: 87.0
    operational_transparency: 60.5
  previous_composite: 2.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 75.9
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Getemboss Ai Authentication
  slug: getemboss-ai-authentication
  summary_line: http/oauth2/payment · 6 schemes
- kind: domain-security
  name: Getemboss Ai Domain Security
  slug: getemboss-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getemboss Ai Vulnerability Disclosure
  slug: getemboss-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getemboss-ai
tags:
- PDF
- Forms
- Document Processing
- Form Filling
- Fax
- Data Extraction
- agent-native
- MCP
- A2A
- x402
- pay-per-call
- Government Forms
- Company
website: https://getemboss.ai/
---
