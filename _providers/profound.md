---
access_model:
  confidence: high
  label: Enterprise, on request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.tryprofound.com/pricing
  - https://docs.tryprofound.com/rest-api/introduction
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Profound Agentic Access
  operation_count: 125
  slug: profound-agentic-access
  summary_line: 125 operations · 90 acting
api_count: 2
apis:
- description: 'The programmatic interface to Profound''s Answer Engine Optimization data: brand visibility, citations, sentiment, query fan-outs, FactCheck accuracy, shopping visibility, YouTube social reports, AI cr'
  name: Profound External API
  slug: profound-external-api
- description: The inbound log-ingestion endpoint for Profound Agent Analytics. Customers POST batches of up to 1,000 web-request log entries as JSON (timestamp, method, host, path, status_code, ip, user_agent, plus
  name: Profound Agent Analytics Ingestion API
  slug: profound-agent-analytics-ingestion-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/profound-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryprofound.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryprofound.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryprofound.com/api-reference/organization/get-categories
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tryprofound.com/rest-api/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.tryprofound.com
- group: company
  title: ''
  type: Blog
  url: https://www.tryprofound.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cooper-square-technologies
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryprofound.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tryprofound.com/rest-api/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryprofound.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.tryprofound.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.tryprofound.com/welcome
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryprofound.com/legal/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/profound-external-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/profound-external-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/profound-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/profound-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/profound/
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@profoundai/client
- group: agent
  title: ''
  type: MCPServer
  url: mcp/profound-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/profound-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/profound-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/profound-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/profound-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/profound-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/profound-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/profound-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/profound-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/profound-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/profound-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/profound-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/profound-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profound-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/profound-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/profound-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profound-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/profound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tryprofound.com/vulnerability-reporting
- group: auth
  title: ''
  type: TrustCenter
  url: security/profound-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryprofound.com
created: '2026-07-17'
description: Profound is a marketing platform for the AI era and a leading platform for Answer Engine Optimization (AEO). Operated by Cooper Square Technologies Inc. (dba Profound) in New York, it helps brands measure and improve how they are represented across AI answer engines and assistants — ChatGPT, Perplexity, Claude, Gemini, Google AI Overviews and AI Mode, Copilot, and Grok — through answer-engine insights, agent analytics, prompt volumes, shopping visibility, and content optimization. Profound publishes a 125-operation OpenAPI 3.1 for its External API at api.tryprofound.com, runs a separate Agent Analytics Ingestion API, ships official Python and TypeScript SDKs, and operates a hosted remote MCP server at mcp.tryprofound.com with OAuth 2.1 and a conformant A2A agent card. API access is included on the Enterprise plan on request. Profound is SOC 2 and HIPAA aligned and publishes a responsible-disclosure policy. Backed by Kleiner Perkins.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/profound.png
layout: provider
mcp_servers:
- description: ''
  name: Profound MCP Server
  slug: profound-mcp-server
modified: '2026-08-13'
name: Profound
nav: Providers
network: true
overview: 'Profound publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Artificial Intelligence, Answer Engine Optimization, AEO, and AI Search.


  Profound''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Profound Plans Pricing
  plan_count: 3
  slug: profound-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Profound Rate Limits
  slug: profound-rate-limits
scopes:
- name: Profound Scopes
  scope_count: 4
  slug: profound-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode/refreshToken
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 16.7
    contract_quality: 49.2
    developer_ergonomics: 81.0
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 57.9
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/profound/refs/heads/main/screenshots/profound-2026-08-17T080414.png
security:
- kind: authentication
  name: Profound Authentication
  slug: profound-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Profound Domain Security
  slug: profound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Profound Vulnerability Disclosure
  slug: profound-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Profound Trust Center
  slug: profound-trust-center
  summary_line: SOC 2, HIPAA
slug: profound
tags:
- Company
- Artificial Intelligence
- Answer Engine Optimization
- AEO
- AI Search
- Generative Engine Optimization
- Marketing
- Analytics
- Agent Analytics
- Brand Visibility
- Citations
- MCP
website: https://www.tryprofound.com
---
