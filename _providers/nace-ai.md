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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Nace Ai Agentic Access
  operation_count: 13
  slug: nace-ai-agentic-access
  summary_line: 13 operations · 10 acting
api_count: 2
apis:
- description: The health API from Nace Ai — 1 operation(s) for health.
  name: Nace Ai health API
  slug: nace-ai-health-api
- description: The public-api API from Nace Ai — 12 operation(s) for public-api.
  name: Nace Ai public-api API
  slug: nace-ai-public-api-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NDI Service health API
  slug: open-nace-ai-health-api
- collection_type: open
  name: NDI Service health public-api API
  slug: open-nace-ai-public-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nace-ai-ndi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nace-ai-agentic-access.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nace-ai-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nace-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nace-ai-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nace-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nace-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nace-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nace-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nace-ai-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nace-ai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nace-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nace-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://nace.ai
- group: company
  title: ''
  type: Blog
  url: https://nace.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://nace.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nace.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nace.ai/policies/privacy-policy
created: '2026-07-17'
description: 'Nace.AI builds specialized AI models and agents that run enterprise business processes end-to-end on small models customers control. Its NAVI product automates workflows across financial auditing, loan processing, billing, accounts payable, and claims. Nace Document Intelligence (NDI) is its public API: an API-key REST + MCP service that parses documents to high-fidelity markdown, categorizes contents against a taxonomy, grounds values to precise page coordinates, and extracts schema-shaped structured JSON via async jobs.'
image: https://nace.ai
layout: provider
mcp_servers:
- description: ''
  name: nace-ai-mcp.yml
  slug: nace-ai-mcpyml
modified: '2026-07-20'
name: Nace Ai
nav: Providers
network: true
overview: 'Nace Ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: health API and public-api API. Tagged areas include Company, Artificial Intelligence, Document Intelligence, Document Processing, and Data Extraction.


  Nace Ai''s developer surface includes authentication, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 58
rate_limits:
- limit_count: 3
  name: Nace Ai Rate Limits
  slug: nace-ai-rate-limits
score:
  band: thin
  composite: 38.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 53.7
    developer_ergonomics: 23.4
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nace-ai/refs/heads/main/screenshots/nace-ai-2026-08-07T184600.png
security:
- kind: authentication
  name: Nace Ai Authentication
  slug: nace-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nace Ai Domain Security
  slug: nace-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nace-ai
tags:
- Company
- Artificial Intelligence
- Document Intelligence
- Document Processing
- Data Extraction
- OCR
- Machine Learning
- Enterprise Automation
- MCP
website: https://nace.ai
---
