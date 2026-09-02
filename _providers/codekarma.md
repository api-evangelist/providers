---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 3.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://codekarma.ai
- group: company
  title: ''
  type: Blog
  url: https://codekarma.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codekarma.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codekarma.ai/terms
- group: auth
  title: ''
  type: Compliance
  url: https://codekarma.ai/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codekarma-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codekarma-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codekarma-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codekarma-domain-security.yml
created: '2026-07-17'
description: CodeKarma is a production intelligence platform that maps 100% of production traffic directly to source code, giving engineering teams and AI agents code-level visibility into how software actually behaves in production. Its products include KarmaLens (an IDE plugin for JetBrains and VS Code surfacing dead code, method frequency, and performance hotspots), KarmaDomain (live API-level dependency graphs across microservices, databases, and async systems), KarmaPulse (an operations command center with API health, error drift, and AI root cause analysis), and KarmaIQ (an MCP server that feeds production context to AI coding agents such as Cursor, Windsurf, GitHub Copilot, and Claude). Deployed as managed SaaS or bring-your-own-cloud (AWS, Azure, GCP), CodeKarma is SOC 2 Type 2 certified and collects only behavioral telemetry — no PII, payloads, or request bodies. Founded by Anantharam Vanchi Prakash and Priyanka Nahata, based in Bengaluru, India, and backed by Prosus, Accel, Xeed
  Ventures, SenseAI Ventures, and Stargazer Ventures.
image: https://codekarma.ai/og-default.png
layout: provider
mcp_servers:
- description: KarmaIQ is CodeKarma's MCP (Model Context Protocol) server that provides production context to AI coding agents for deterministic debugging and root cause analysis. It exposes a blended, production-gr
  name: KarmaIQ
  slug: karmaiq
modified: '2026-07-18'
name: CodeKarma
nav: Providers
network: true
overview: 'CodeKarma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Production Intelligence, Observability, and AI Agents.


  CodeKarma''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codekarma/refs/heads/main/screenshots/codekarma-2026-07-25T205918.png
security:
- kind: domain-security
  name: Codekarma Domain Security
  slug: codekarma-domain-security
  summary_line: TLSv1.3
slug: codekarma
tags:
- Company
- Artificial Intelligence
- Production Intelligence
- Observability
- AI Agents
- MCP
- Developer Tools
- Code Analysis
website: https://codekarma.ai
---
