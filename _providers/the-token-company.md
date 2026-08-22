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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Prompt and conversation compression
  name: The Token Company Compression API
  slug: the-token-company-compression-api
- description: Compressed web search
  name: The Token Company Search API
  slug: the-token-company-search-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Token Company Compression API
  slug: open-the-token-company-compression-api
- collection_type: open
  name: The Token Company Compression Search API
  slug: open-the-token-company-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/the-token-company-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-token-company-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thetokencompany.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://thetokencompany.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://thetokencompany.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thetokencompany.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://thetokencompany.com/blog
- group: operate
  title: ''
  type: Support
  url: https://thetokencompany.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheTokenCompany
- group: commercial
  title: ''
  type: Pricing
  url: https://thetokencompany.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.thetokencompany.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thetokencompany.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thetokencompany.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thetokencompany.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.thetokencompany.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.thetokencompany.com
- group: build
  title: ''
  type: Packages
  url: packages/the-token-company-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/the-token-company-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-token-company-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-token-company-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-token-company-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-token-company-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/the-token-company-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-token-company-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-token-company-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/the-token-company-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-token-company-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: The Token Company builds LLM input-compression middleware. A single API call runs a prompt, a full chat conversation, or web-search results through their bear compression models (bear-2 latest, plus bear-1.2/1.1/1) to strip low-signal tokens before the text reaches a language model, cutting cost and latency while preserving output quality. It ships drop-in Python and Node.js SDKs that wrap the OpenAI, Anthropic, Vercel AI SDK, and OpenRouter clients so existing apps compress automatically, plus content-protection (ttc_safe) tags, per-app usage tagging, and a zero-data-retention policy. A Y Combinator (W26) company based in San Francisco.
image: https://thetokencompany.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: the-token-company-mcp.yml
  slug: the-token-company-mcpyml
modified: '2026-07-21'
name: The Token Company
nav: Providers
network: true
overview: 'The Token Company publishes 2 APIs on the [APIs.io](https://apis.io/) network: Compression API and Search API. Tagged areas include Company, LLM, Artificial Intelligence, Prompt Compression, and Tokens.


  The Token Company''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 41.1
  delta: -1.2
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 16.7
    contract_quality: 15.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-token-company/refs/heads/main/screenshots/the-token-company-2026-08-17T082339.png
security:
- kind: authentication
  name: The Token Company Authentication
  slug: the-token-company-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Token Company Domain Security
  slug: the-token-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: The Token Company Trust Center
  slug: the-token-company-trust-center
  summary_line: HIPAA
slug: the-token-company
tags:
- Company
- LLM
- Artificial Intelligence
- Prompt Compression
- Tokens
- Cost Optimization
- Developer Tools
- Middleware
- API
website: https://thetokencompany.com/docs
---
