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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Create, list, retrieve, and continue investigation sessions.
  name: Traversal Sessions API
  slug: traversal-sessions-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Traversal Sessions API
  slug: open-traversal-sessions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.traversal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.traversal.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.traversal.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.traversal.com/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.traversal.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@traversal.com
- group: start
  title: ''
  type: SignUp
  url: https://app.traversal.com/login
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/traversal-sessions-openapi.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/traversal-sessions-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/traversal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/traversal-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/traversal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/traversal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/traversal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/traversal-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/traversal-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.traversal.com
- group: design
  title: ''
  type: Conformance
  url: conformance/traversal-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/traversal-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/traversal-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/traversal-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/traversal-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/traversal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/traversal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/traversal-domain-security.yml
created: '2026-07-17'
description: Traversal is an AI SRE (Site Reliability Engineering) platform that autonomously triages alerts, performs root-cause analysis, and helps prevent production incidents across an enterprise's entire observability stack. Founded in 2023 by AI researchers from MIT, Columbia, Berkeley, and Cornell and based in New York City, Traversal created the "AI SRE" category using causal machine learning and agentic AI. Its V1 Sessions API and hosted MCP server let teams launch investigations programmatically and from AI clients (Claude, Cursor, and others). Backed by Sequoia and Kleiner Perkins (~$53M raised).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traversal.png
layout: provider
mcp_servers:
- description: Traversal operates an official hosted (remote) MCP server that lets any streamable-http MCP client — Claude Code, Claude Desktop, Cursor, OpenCode, ChatGPT, Windsurf, VS Code — run investigations agai
  name: Traversal
  slug: traversal
modified: '2026-07-21'
name: Traversal
nav: Providers
network: true
overview: 'Traversal publishes 1 API on the [APIs.io](https://apis.io/) network: Sessions API. Tagged areas include Company, Artificial Intelligence, AI SRE, Site Reliability Engineering, and Observability.


  Traversal''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 19 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 57.8
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 41.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/traversal/refs/heads/main/screenshots/traversal-2026-08-17T082630.png
security:
- kind: authentication
  name: Traversal Authentication
  slug: traversal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Traversal Domain Security
  slug: traversal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Traversal Vulnerability Disclosure
  slug: traversal-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Traversal Trust Center
  slug: traversal-trust-center
  summary_line: SOC 2 Type II, GDPR, HIPAA
slug: traversal
tags:
- Company
- Artificial Intelligence
- AI SRE
- Site Reliability Engineering
- Observability
- Incident Management
- Root Cause Analysis
- DevOps
- MCP
website: https://www.traversal.com
---
