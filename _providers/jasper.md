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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Jasper Agentic Access
  operation_count: 50
  slug: jasper-agentic-access
  summary_line: 50 operations · 30 acting
api_count: 1
apis:
- description: The Jasper API brings generative AI into your platform — generate on-brand content via commands and templates, run marketing Agent Tasks, manage documents, projects, tones, and audiences, augment gene
  name: Jasper API
  slug: jasper-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jasper-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jasper-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jasper.ai/security
- group: company
  title: ''
  type: Website
  url: https://www.jasper.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jasper.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jasper.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jasper.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.jasper.ai/docs/getting-started-1
- group: company
  title: ''
  type: Blog
  url: https://www.jasper.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://community.jasper.ai/c/help-center/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.jasper.ai/contact-support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jasper.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.jasper.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.jasper.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jasper.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jasper.ai/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.jasper.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://security.jasper.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gojasper
- group: build
  title: ''
  type: Postman
  url: https://developers.jasper.ai/docs/jaspers-api-postman-collection
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jasper-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jasper-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/jasper-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jasper-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jasper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jasper-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jasper-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jasper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jasper-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jasper-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jasper-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jasper-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jasper-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jasper-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/jasper-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/jasper-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/jasper-examples.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/jasper-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jasper-plans-pricing.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jasper.ai/
created: '2026-07-17'
description: Jasper is an AI platform purpose-built for marketing teams that orchestrates 100+ specialized AI agents and connected content pipelines to run end-to-end marketing workflows — content creation, campaign execution, personalization, and SEO/GEO optimization — while holding brand consistency at scale. Jasper IQ is the governance layer that embeds brand voice, style guides, and marketing context into every output. The Jasper API (https://api.jasper.ai/v1) exposes commands, agent tasks, documents, projects, tones, audiences, knowledge/retrieval, and a full image-editing suite, secured with workspace API keys (X-API-Key) or OAuth 2.0 (authorization code + PKCE, Dynamic Client Registration). Jasper also ships a hosted, remote Model Context Protocol (MCP) server at https://mcp.jasper.ai so agents in Claude, ChatGPT, Copilot Studio, OpenAI Agent Builder, and n8n can create on-brand content. API access is available on the Jasper Business plan.
image: https://cdn.prod.website-files.com/6807ee8d73c233fb82842313/681e121f9445a06741087852_Webclip.png
layout: provider
mcp_servers:
- description: ''
  name: jasper-mcp.yml
  slug: jasper-mcpyml
modified: '2026-08-13'
name: Jasper
nav: Providers
network: true
overview: 'Jasper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Artificial Intelligence, Content Generation, and Marketing.


  Jasper''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Jasper Plans Pricing
  plan_count: 2
  slug: jasper-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Jasper Rate Limits
  slug: jasper-rate-limits
scopes:
- name: Jasper Scopes
  scope_count: 6
  slug: jasper-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 57.4
  delta: -4.8
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 30.3
    contract_quality: 54.0
    developer_ergonomics: 47.0
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 44.7
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jasper/refs/heads/main/screenshots/jasper-2026-07-25T223101.png
security:
- kind: authentication
  name: Jasper Authentication
  slug: jasper-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Jasper Domain Security
  slug: jasper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jasper Vulnerability Disclosure
  slug: jasper-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Jasper Trust Center
  slug: jasper-trust-center
  summary_line: SOC 2, GDPR
slug: jasper
tags:
- Company
- Ai Ml
- Artificial Intelligence
- Content Generation
- Marketing
- Generative AI
- Agents
- MCP
website: https://www.jasper.ai/
---
