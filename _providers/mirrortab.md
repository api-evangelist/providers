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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Mirrortab Agentic Access
  operation_count: 3
  slug: mirrortab-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: Create, list, and remove MirrorTab browser sessions.
  name: MirrorTab Sessions API
  slug: mirrortab-sessions-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MirrorTab Sessions API
  slug: open-mirrortab-sessions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mirrortab-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mirrortab-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.mirrortab.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/MirrorTab/api_v1
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/MirrorTab/api_v1
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MirrorTab
- group: start
  title: ''
  type: Login
  url: https://mirrortab.com/API
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mirrortab.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mirrortab.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mirrortab-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirrortab-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mirrortab-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mirrortab-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirrortab-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mirrortab-authentication.yml
created: '2026-07-17'
description: MirrorTab is a cybersecurity company that stops automated attacks against web applications and APIs by serving the application through an isolated, server-side rendered browser session so the DOM, code, and data are never exposed to the end browser. Rather than detecting bots, it removes the surface they operate on, blocking credential stuffing, agentic-AI automation, man-in-the-browser attacks, malicious extensions, XSS, formjacking, clickjacking, and CSRF without endpoint agents or application code changes. MirrorTab is edge-driven and integrates alongside existing CDNs, WAFs, and fraud platforms. Founded by the CTO and co-founder of Honey (acquired by PayPal), the company also publishes a public v1 REST API to programmatically create, list, and remove MirrorTab browser sessions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mirrortab.png
layout: provider
mcp_servers:
- description: ''
  name: mirrortab-mcp.yml
  slug: mirrortab-mcpyml
modified: '2026-07-20'
name: MirrorTab
nav: Providers
network: true
overview: 'MirrorTab publishes 1 API on the [APIs.io](https://apis.io/) network: Sessions API. Tagged areas include Company, Enterprise, Security, Cybersecurity, and Bot Mitigation.


  MirrorTab''s developer surface includes documentation, API reference, authentication, and 13 more developer resources.'
random_paper: 84
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 59.0
    developer_ergonomics: 29.9
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mirrortab/refs/heads/main/screenshots/mirrortab-2026-08-07T183736.png
security:
- kind: authentication
  name: Mirrortab Authentication
  slug: mirrortab-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mirrortab Domain Security
  slug: mirrortab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mirrortab
tags:
- Company
- Enterprise
- Security
- Cybersecurity
- Bot Mitigation
- Fraud Prevention
- Browser Isolation
- Anti-Automation
website: https://www.mirrortab.com
---
