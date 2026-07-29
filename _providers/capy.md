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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Capy Agentic Access
  operation_count: 37
  slug: capy-agentic-access
  summary_line: 37 operations · 19 acting · 1 human-in-the-loop
api_count: 12
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
artifact_total: 18
common:
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
  name: capy-mcp.yml
  slug: capy-mcpyml
modified: '2026-07-18'
name: Capy
nav: Providers
network: true
overview: 'Capy publishes 12 APIs on the [APIs.io](https://apis.io/) network, including automations API, browser-snapshots API, environment-variables API, and 9 more. Tagged areas include Company, Ai, AI Coding Agent, Software Engineering, and Developer Tools.


  Capy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 34
score:
  band: developing
  composite: 51.5
  delta: -0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 10.5
  previous_composite: 51.6
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Ai
- AI Coding Agent
- Software Engineering
- Developer Tools
- Automation
- Code Review
- DevOps
website: https://capy.ai/
---
