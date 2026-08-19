---
access_model:
  confidence: high
  label: Free tier, then self-serve checkout
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - authentication
  - https://www.exec.com/pricing
  - https://docs.exec.com/platform/plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Exec Agentic Access
  operation_count: 32
  slug: exec-agentic-access
  summary_line: 32 operations · 11 acting
api_count: 9
apis:
- description: The Collections API from Exec — 1 operation(s) for collections.
  name: Exec Collections API
  slug: exec-collections-api
- description: The Knowledge Hub - Folders API from Exec — 2 operation(s) for knowledge hub - folders.
  name: Exec Knowledge Hub - Folders API
  slug: exec-knowledge-hub-folders-api
- description: The Knowledge Hub - Pages API from Exec — 3 operation(s) for knowledge hub - pages.
  name: Exec Knowledge Hub - Pages API
  slug: exec-knowledge-hub-pages-api
- description: The Knowledge Hub - Sources API from Exec — 2 operation(s) for knowledge hub - sources.
  name: Exec Knowledge Hub - Sources API
  slug: exec-knowledge-hub-sources-api
- description: The Scenario Studio API from Exec — 3 operation(s) for scenario studio.
  name: Exec Scenario Studio API
  slug: exec-scenario-studio-api
- description: The Scenarios API from Exec — 6 operation(s) for scenarios.
  name: Exec Scenarios API
  slug: exec-scenarios-api
- description: The Sessions API from Exec — 2 operation(s) for sessions.
  name: Exec Sessions API
  slug: exec-sessions-api
- description: The Skills API from Exec — 2 operation(s) for skills.
  name: Exec Skills API
  slug: exec-skills-api
- description: The Workspace API from Exec — 3 operation(s) for workspace.
  name: Exec Workspace API
  slug: exec-workspace-api
artifact_total: 27
asyncapis:
- description: ''
  name: Exec Webhooks
  slug: exec-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exec Collections API
  slug: open-exec-collections-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Folders API
  slug: open-exec-knowledge-hub-folders-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Pages API
  slug: open-exec-knowledge-hub-pages-api
- collection_type: open
  name: Exec Collections Knowledge Hub - Sources API
  slug: open-exec-knowledge-hub-sources-api
- collection_type: open
  name: Exec Collections Scenario Studio API
  slug: open-exec-scenario-studio-api
- collection_type: open
  name: Exec Collections Scenarios API
  slug: open-exec-scenarios-api
- collection_type: open
  name: Exec Collections Sessions API
  slug: open-exec-sessions-api
- collection_type: open
  name: Exec Collections Skills API
  slug: open-exec-skills-api
- collection_type: open
  name: Exec Collections Workspace API
  slug: open-exec-workspace-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/exec-openapi-original.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exec-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exec-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/exec-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/exec-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exec-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exec-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.exec.com
- group: design
  title: ''
  type: Conformance
  url: conformance/exec-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.exec.com/enterprise-privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/exec.com/trust/j0xkhh5zesxvojinovqlpm
- group: design
  title: ''
  type: DataModel
  url: data-model/exec-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/exec-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/exec-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exec-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/exec-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/exec-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/exec-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exec-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.exec.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exec.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.exec.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.exec.com/api-reference/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.exec.com
- group: company
  title: ''
  type: Blog
  url: https://www.exec.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exec.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.exec.com/start
- group: start
  title: ''
  type: Login
  url: https://www.exec.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exec.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exec.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.exec.com
created: '2026-07-17'
description: 'Exec is an AI-powered roleplay and sales-training platform (exec.com) for practicing high-stakes conversations. Teams run voice-based AI roleplays, automatically score real calls, build structured programs and certifications, coach one-on-one, and manage training content in a Knowledge Hub. The Exec REST API gives programmatic access to a workspace: members and groups, scenarios and collections, roleplay sessions and analytics, skills and proficiency, Scenario Studio job creation, and Knowledge Hub pages and sources. Backed by a16z.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exec.png
layout: provider
mcp_servers:
- description: ''
  name: exec-mcp.yml
  slug: exec-mcpyml
modified: '2026-08-14'
name: Exec
nav: Providers
network: true
overview: 'Exec publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Knowledge Hub - Folders API, Knowledge Hub - Pages API, and 6 more. Tagged areas include Company, Artificial Intelligence, Sales Enablement, Training, and Roleplay.


  The Exec catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Exec''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Exec Plans Pricing
  plan_count: 4
  slug: exec-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 3
  name: Exec Rate Limits
  slug: exec-rate-limits
score:
  band: exemplar
  composite: 68.2
  delta: 3.2
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 69.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exec/refs/heads/main/screenshots/exec-2026-07-25T213855.png
security:
- kind: authentication
  name: Exec Authentication
  slug: exec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exec Domain Security
  slug: exec-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Exec Trust Center
  slug: exec-trust-center
  summary_line: SOC 2 Type II, SOC 3
slug: exec
tags:
- Company
- Artificial Intelligence
- Sales Enablement
- Training
- Roleplay
- Coaching
- Learning
- Knowledge Management
- LMS
website: https://www.exec.com
---
