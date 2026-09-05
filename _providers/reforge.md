---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Reforge Launch delivers feature flags, live configuration, dynamic log levels, and experiments through first-party SDKs and a CLI. SDKs fetch configuration from a global delivery network and evaluate '
  name: Reforge Launch
  slug: reforge-launch
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reforge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reforge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reforge.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reforge.com/docs/tutorials/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReforgeHQ
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reforge.com/
- group: company
  title: ''
  type: Blog
  url: https://www.reforge.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reforge.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.reforge.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reforge.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reforge.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/reforge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reforge-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/reforge-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reforge-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reforge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reforge-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reforge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reforge-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reforge-llms.txt
created: '2026-07-17'
description: Reforge is the company behind Reforge Launch, a developer platform for feature flags, live configuration, dynamic log levels, and experimentation delivered as a service (the product formerly known as Prefab). Applications integrate Reforge through first-party SDKs for Node, JavaScript, React, Python, Ruby, Go, and Java plus a command-line interface, evaluating flags and configuration against user context with server- and client-side SDK keys. Configuration is delivered over a global content network (primary/secondary.reforge.com) with server-sent events and polling for real-time updates, while telemetry flows to api.reforge.com. Reforge is backed by a16z and Insight Partners.
image: https://avatars.githubusercontent.com/u/24498216?v=4
layout: provider
mcp_servers:
- description: 'The Reforge CLI ships an MCP server that connects an AI assistant to a Reforge workspace. `reforge mcp` configures the server for a supported editor/assistant (e.g. Claude Code, Codeium), letting the '
  name: Reforge MCP Server
  slug: reforge-mcp-server
modified: '2026-07-21'
name: Reforge
nav: Providers
network: true
overview: 'Reforge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Feature Flags, Feature Management, Dynamic Configuration, and Live Config.


  Reforge''s developer surface includes documentation, getting-started guide, engineering blog, pricing, CLI, authentication, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.0
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reforge/refs/heads/main/screenshots/reforge-2026-09-02T153231.png
security:
- kind: authentication
  name: Reforge Authentication
  slug: reforge-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Reforge Domain Security
  slug: reforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reforge
tags:
- Company
- Feature Flags
- Feature Management
- Dynamic Configuration
- Live Config
- Experimentation
- Developer Tools
- SDK
- Observability
website: https://www.reforge.com/
---
