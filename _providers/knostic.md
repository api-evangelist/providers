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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Knostic Agentic Access
  operation_count: 12
  slug: knostic-agentic-access
  summary_line: 12 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://agentmesh.knostic.ai/api
  baseurl_source: declared
  description: VS Code / IDE marketplace extensions with risk assessment
  name: Knostic extensions API
  slug: knostic-extensions-api
- baseURL: https://agentmesh.knostic.ai/api
  baseurl_source: declared
  description: Model Context Protocol servers discovered and scanned by AgentMesh
  name: Knostic mcp API
  slug: knostic-mcp-api
- baseURL: https://agentmesh.knostic.ai/api
  baseurl_source: declared
  description: On-demand security scans and scan history (API key required)
  name: Knostic scans API
  slug: knostic-scans-api
- baseURL: https://agentmesh.knostic.ai/api
  baseurl_source: declared
  description: AI agent skills (SKILL.md) discovered and scanned by AgentMesh
  name: Knostic skills API
  slug: knostic-skills-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knostic AgentMesh extensions API
  slug: open-knostic-extensions-api
- collection_type: open
  name: Knostic AgentMesh extensions mcp API
  slug: open-knostic-mcp-api
- collection_type: open
  name: Knostic AgentMesh extensions scans API
  slug: open-knostic-scans-api
- collection_type: open
  name: Knostic AgentMesh extensions skills API
  slug: open-knostic-skills-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/knostic-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/knostic-agentmesh-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/knostic-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.knostic.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentmesh.knostic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agentmesh.knostic.ai/api
- group: docs
  title: ''
  type: APIReference
  url: https://agentmesh.knostic.ai/api
- group: start
  title: ''
  type: Login
  url: https://agentmesh.knostic.ai/console
- group: operate
  title: ''
  type: Support
  url: https://www.knostic.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.knostic.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knostic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.knostic.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.knostic.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.knostic.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://security.knostic.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/knostic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knostic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knostic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knostic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knostic-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/knostic-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knostic-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knostic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/knostic-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knostic-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/knostic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/knostic-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/knostic-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knostic-llms.txt
- group: build
  title: ''
  type: Examples
  url: examples/knostic-list-skills-response.json
created: '2026-07-17'
description: 'Knostic secures the AI agent supply chain inside the enterprise. Its platform discovers shadow AI, coding assistants, MCP servers and IDE extensions in use across an organization, then scans them for prompt injection, data exfiltration, secret and PII leakage, and destructive commands. Knostic runs AgentMesh, a public reputation and threat-intelligence service that continuously discovers, tracks and scans AI agent skills, Model Context Protocol servers, and VS Code / IDE marketplace extensions — roughly 80,500 skills, 4,800 MCP servers and 59,900 extensions as of July 2026 — and exposes that catalog with per-version scan verdicts through a REST API whose read endpoints answer anonymous callers. Knostic also ships a substantial open-source portfolio: AgentSonar (shadow-AI network detection), OpenAnt (LLM-based vulnerability discovery), MCP-Scanner, and security and telemetry plugins for OpenClaw agents.'
examples:
- key_count: 4
  name: Knostic List Extensions Response
  slug: knostic-list-extensions-response
- key_count: 4
  name: Knostic List Mcp Response
  slug: knostic-list-mcp-response
- key_count: 4
  name: Knostic List Skills Response
  slug: knostic-list-skills-response
image: https://www.knostic.ai/og-image.png
layout: provider
modified: '2026-07-19'
name: Knostic
nav: Providers
network: true
overview: 'Knostic publishes 4 APIs on the [APIs.io](https://apis.io/) network, including extensions API, mcp API, scans API, and 1 more. Tagged areas include Company, Security, Artificial Intelligence, AI Agents, and Agent Security.


  Knostic''s developer surface includes documentation, API reference, support, engineering blog, authentication, changelog, CLI, and 24 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 3
  name: Knostic Rate Limits
  slug: knostic-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 62.6
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 60.5
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knostic/refs/heads/main/screenshots/knostic-2026-07-25T224003.png
security:
- kind: authentication
  name: Knostic Authentication
  slug: knostic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knostic Domain Security
  slug: knostic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Knostic Trust Center
  slug: knostic-trust-center
  summary_line: SOC 2 Type 2
slug: knostic
tags:
- Company
- Security
- Artificial Intelligence
- AI Agents
- Agent Security
- Supply Chain Security
- MCP
- Threat Intelligence
- Developer Tools
- Shadow AI
website: https://www.knostic.ai/
---
