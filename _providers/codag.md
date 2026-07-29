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
    consent_identity: true
    dry_run_mode: true
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 3
  name: Codag Agentic Access
  operation_count: 70
  slug: codag-agentic-access
  summary_line: 70 operations · 39 acting · 3 human-in-the-loop
api_count: 19
apis:
- description: The Activate API from Codag — 2 operation(s) for activate.
  name: Codag Activate API
  slug: codag-activate-api
- description: The Admin API from Codag — 2 operation(s) for admin.
  name: Codag Admin API
  slug: codag-admin-api
- description: The Anonymous API from Codag — 1 operation(s) for anonymous.
  name: Codag Anonymous API
  slug: codag-anonymous-api
- description: The Auth API from Codag — 4 operation(s) for auth.
  name: Codag Auth API
  slug: codag-auth-api
- description: The billing API from Codag — 4 operation(s) for billing.
  name: Codag billing API
  slug: codag-billing-api
- description: The Capsule API from Codag — 1 operation(s) for capsule.
  name: Codag Capsule API
  slug: codag-capsule-api
- description: The Cli API from Codag — 2 operation(s) for cli.
  name: Codag Cli API
  slug: codag-cli-api
- description: The Compact API from Codag — 3 operation(s) for compact.
  name: Codag Compact API
  slug: codag-compact-api
- description: The Free API from Codag — 1 operation(s) for free.
  name: Codag Free API
  slug: codag-free-api
- description: The Health API from Codag — 1 operation(s) for health.
  name: Codag Health API
  slug: codag-health-api
- description: The Incident Memory API from Codag — 3 operation(s) for incident memory.
  name: Codag Incident Memory API
  slug: codag-incident-memory-api
- description: The Install.sh API from Codag — 1 operation(s) for install.sh.
  name: Codag Install.sh API
  slug: codag-install-sh-api
- description: The Internal API from Codag — 2 operation(s) for internal.
  name: Codag Internal API
  slug: codag-internal-api
- description: The Oauth API from Codag — 2 operation(s) for oauth.
  name: Codag Oauth API
  slug: codag-oauth-api
- description: The Onboard API from Codag — 2 operation(s) for onboard.
  name: Codag Onboard API
  slug: codag-onboard-api
- description: The Org API from Codag — 14 operation(s) for org.
  name: Codag Org API
  slug: codag-org-api
- description: The Orgs API from Codag — 13 operation(s) for orgs.
  name: Codag Orgs API
  slug: codag-orgs-api
- description: The Parse API from Codag — 1 operation(s) for parse.
  name: Codag Parse API
  slug: codag-parse-api
- description: The Whoami API from Codag — 1 operation(s) for whoami.
  name: Codag Whoami API
  slug: codag-whoami-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codag-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://codag.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://codag.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://codag.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://codag.ai/docs/rest-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://codag.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://codag.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://codag.ai/support
- group: commercial
  title: ''
  type: Pricing
  url: https://codag.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.codag.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codag.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codag.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codag-megalith
- group: build
  title: ''
  type: Packages
  url: packages/codag-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/codag-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/codag-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codag-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codag-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codag-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/codag-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/codag-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codag-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/codag-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codag-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codag-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/codag-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/codag-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codag-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codag-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://codag.ai/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codag-domain-security.yml
created: '2026-07-17'
description: Codag is a Y Combinator (Summer 2026) developer-tools company building drop-in log compression for AI agents. It takes oversized infrastructure logs — from Kubernetes, Docker, AWS CloudWatch, Vercel, Railway, Datadog, Sentry, syslog and unstructured sources — and returns only the lines that matter as schema-valid JSON, ranked into patterns where every kept line cites a real log line number so nothing is summarized away or invented. This lets coding agents like Claude, Codex and Cursor debug from the evidence that matters at roughly 95% fewer tokens without exhausting their context window. Codag ships as a hosted HTTPS API (/v1/compact), an open-source Go CLI, and an MCP server, with a deterministic Rust log-templating engine (codag-drain) as the free/fallback path.
image: https://codag.ai/socialpreview.png
layout: provider
mcp_servers:
- description: ''
  name: codag-mcp.yml
  slug: codag-mcpyml
modified: '2026-07-18'
name: Codag
nav: Providers
network: true
overview: 'Codag publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Activate API, Admin API, Anonymous API, and 16 more. Tagged areas include Company, Developer Tools, Logging, Observability, and Log Compression.


  Codag''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 50.7
  delta: -0.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 42.2
    developer_ergonomics: 82.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codag/refs/heads/main/screenshots/codag-2026-07-25T205856.png
security:
- kind: authentication
  name: Codag Authentication
  slug: codag-authentication
  summary_line: http/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Codag Domain Security
  slug: codag-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Codag Vulnerability Disclosure
  slug: codag-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: codag
tags:
- Company
- Developer Tools
- Logging
- Observability
- Log Compression
- AI Agents
- MCP
- LLM Tooling
- Debugging
- Y Combinator
website: https://codag.ai/
---
