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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Capy Agentic Access
  operation_count: 37
  slug: capy-agentic-access
  summary_line: 37 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The automations API from Capy — 3 operation(s) for automations.
  name: Capy automations API
  slug: capy-automations-api
- description: The browser-snapshots API from Capy — 2 operation(s) for browser-snapshots.
  name: Capy browser-snapshots API
  slug: capy-browser-snapshots-api
- description: The environment-variables API from Capy — 2 operation(s) for environment-variables.
  name: Capy environment-variables API
  slug: capy-environment-variables-api
- description: The models API from Capy — 1 operation(s) for models.
  name: Capy models API
  slug: capy-models-api
- description: The projects API from Capy — 2 operation(s) for projects.
  name: Capy projects API
  slug: capy-projects-api
- description: The sessions API from Capy — 1 operation(s) for sessions.
  name: Capy sessions API
  slug: capy-sessions-api
- description: The setup API from Capy — 1 operation(s) for setup.
  name: Capy setup API
  slug: capy-setup-api
- description: The snapshots API from Capy — 1 operation(s) for snapshots.
  name: Capy snapshots API
  slug: capy-snapshots-api
- description: The tags API from Capy — 2 operation(s) for tags.
  name: Capy tags API
  slug: capy-tags-api
- description: The tasks API from Capy — 2 operation(s) for tasks.
  name: Capy tasks API
  slug: capy-tasks-api
- description: The threads API from Capy — 8 operation(s) for threads.
  name: Capy threads API
  slug: capy-threads-api
- description: The usage API from Capy — 1 operation(s) for usage.
  name: Capy usage API
  slug: capy-usage-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capy automations API
  slug: open-capy-automations-api
- collection_type: open
  name: Capy automations browser-snapshots API
  slug: open-capy-browser-snapshots-api
- collection_type: open
  name: Capy automations environment-variables API
  slug: open-capy-environment-variables-api
- collection_type: open
  name: Capy automations models API
  slug: open-capy-models-api
- collection_type: open
  name: Capy automations projects API
  slug: open-capy-projects-api
- collection_type: open
  name: Capy automations sessions API
  slug: open-capy-sessions-api
- collection_type: open
  name: Capy automations setup API
  slug: open-capy-setup-api
- collection_type: open
  name: Capy automations snapshots API
  slug: open-capy-snapshots-api
- collection_type: open
  name: Capy automations tags API
  slug: open-capy-tags-api
- collection_type: open
  name: Capy automations tasks API
  slug: open-capy-tasks-api
- collection_type: open
  name: Capy automations threads API
  slug: open-capy-threads-api
- collection_type: open
  name: Capy automations usage API
  slug: open-capy-usage-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/capy-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://capy.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.capy.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.capy.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.capy.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.capy.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.capy.ai/support
- group: company
  title: ''
  type: Blog
  url: https://capy.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://capy.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://capy.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capy.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capy.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/capy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/capy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/capy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/capy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.capy.ai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/capy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capy-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/capy-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://capy.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/capy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capy-domain-security.yml
created: '2026-07-17'
description: Capy is an AI software-engineering platform that orchestrates a fleet of cloud coding agents inside the apps a team already uses (Slack, Linear, GitHub). Each task runs in its own isolated Ubuntu VM where a captain agent plans and build agents execute — writing code, running end-to-end browser tests, migrating codebases, generating docs, triaging and fixing bugs, and opening pull requests for review. Capy supports multiple frontier models (GPT, Claude, Grok, Gemini) and exposes a REST API (bearer capy_ token) plus scheduled and webhook-triggered automations. Backed by CRV; SOC 2 Type II certified.
image: https://capy.ai/_marketing/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Capy MCP Server
  slug: capy-mcp-server
modified: '2026-07-18'
name: Capy
nav: Providers
network: true
overview: 'Capy publishes 12 APIs on the [APIs.io](https://apis.io/) network, including automations API, browser-snapshots API, environment-variables API, and 9 more. Tagged areas include Company, Artificial Intelligence, AI Coding Agent, Software Engineering, and Developer Tools.


  Capy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capy/refs/heads/main/screenshots/capy-2026-07-25T204458.png
security:
- kind: authentication
  name: Capy Authentication
  slug: capy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Capy Domain Security
  slug: capy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Capy Vulnerability Disclosure
  slug: capy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Capy Trust Center
  slug: capy-trust-center
  summary_line: SOC 2 Type II
slug: capy
tags:
- Company
- Artificial Intelligence
- AI Coding Agent
- Software Engineering
- Developer Tools
- Automation
- Code Review
- DevOps
website: https://capy.ai/
---
