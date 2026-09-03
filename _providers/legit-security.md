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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Legit Security Webhooks
  slug: legit-security-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legit-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.legitsecurity.com/
- group: start
  title: ''
  type: Login
  url: https://www.legitsecurity.co/app/login
- group: company
  title: ''
  type: Blog
  url: https://www.legitsecurity.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.legitsecurity.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Legit-Labs
- group: operate
  title: ''
  type: Support
  url: mailto:support@legitsecurity.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.legitsecurity.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.legitsecurity.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/legit-security-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/legit-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/legit-security-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/legit-security-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/legit-security-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/legit-security-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legit-security-llms.txt
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.legitsecurity.com/aspm-knowledge-base
- group: operate
  title: ''
  type: ContactUs
  url: https://www.legitsecurity.com/contact-us
- group: start
  title: ''
  type: Demo
  url: https://info.legitsecurity.com/request-a-demo
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Legit-Labs/legitify
created: '2026-07-17'
description: 'Legit Security is an AI-native Application Security Posture Management (ASPM) platform that gives security and engineering teams a unified view of everything being built across the software factory — source code management, CI/CD pipelines, artifact registries, cloud platforms and AI coding assistants — then discovers, correlates, prioritizes and helps remediate application security findings from that one place. The platform spans code security (SAST and SCA), enterprise secrets detection and prevention, software supply chain security, advanced code change management, and continuous compliance and SBOM. Legit also ships an agent-facing surface: the Legit MCP Server, which delivers security intelligence into AI code assistants such as Cursor, GitHub Copilot, Claude Code and Windsurf, and VibeGuard / AI Guard, a Claude Code plugin that blocks secrets leakage, prompt injection, hidden characters and disallowed MCP tools in real time. The company also maintains the open source
  legitify scanner for GitHub and GitLab misconfiguration detection. Legit Security integrates with more than 100 AppSec, SCM, CI, registry, cloud, identity and ticketing tools, including outbound webhook notifications for custom integrations. Backed by Bessemer Venture Partners and CRV.'
image: https://www.legitsecurity.com/hubfs/Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Legit MCP Server
  slug: legit-mcp-server
modified: '2026-07-19'
name: Legit Security
nav: Providers
network: true
overview: 'Legit Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Application Security, ASPM, and DevSecOps.


  The Legit Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Legit Security''s developer surface includes engineering blog, support, CLI, changelog, and 17 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 21.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.9
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legit-security/refs/heads/main/screenshots/legit-security-2026-07-25T224837.png
security:
- kind: domain-security
  name: Legit Security Domain Security
  slug: legit-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Legit Security Trust Center
  slug: legit-security-trust-center
  summary_line: trust center published
slug: legit-security
tags:
- Company
- Cybersecurity
- Application Security
- ASPM
- DevSecOps
- Software Supply Chain Security
- Secrets Detection
- SAST
- SCA
- Compliance
- AI Security
- MCP
website: https://www.legitsecurity.com/
---
