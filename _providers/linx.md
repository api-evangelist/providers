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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.linx.security/
- group: company
  title: ''
  type: Blog
  url: https://www.linx.security/blog
- group: start
  title: ''
  type: Login
  url: https://app.linxsecurity.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linx-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linx.security/docs/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linx.security/docs/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.linx.security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.linx.security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linx-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linx-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/linx-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linx-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linx-domain-security.yml
created: '2026-07-17'
description: Linx Security is an AI-native identity security and governance platform covering the full identity lifecycle across human, non-human, and AI-agent identities. The platform builds an Identity Graph that normalizes identity data across SaaS, cloud, and on-prem systems, then layers identity security posture management (dormant accounts, admin sprawl, SSO bypass, missing MFA), modern IGA (access requests, approvals, provisioning, access certification), just-in-time access in place of standing privileges, automated joiner-mover-leaver lifecycle management, and an autonomous remediation agent called Autopilot. Linx also ships an MCP Server that exposes the Identity Graph and governed identity actions to LLM agents, plus an MCP Gateway for controlling AI agent traffic. Founded by Israel Duanis, Niv Goldenberg, and Sarit Reiner Frumkes, the company is headquartered in New York and has raised $85M from Cyberstarts, Index Ventures, and Insight Partners. Linx does not publish a public
  developer portal, API reference, or API specification — the API referenced in its Master Services Agreement is documented to customers only.
image: https://cdn.prod.website-files.com/69529b4327b8e0f645d9edff/6994d775451e099494971ae4_OG.png
layout: provider
mcp_servers:
- description: ''
  name: Linx MCP Server
  slug: linx-mcp-server
modified: '2026-07-19'
name: Linx
nav: Providers
network: true
overview: 'Linx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Identity Security, Identity Governance, and IGA.


  Linx''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linx/refs/heads/main/screenshots/linx-2026-07-25T225303.png
security:
- kind: domain-security
  name: Linx Domain Security
  slug: linx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Linx Trust Center
  slug: linx-trust-center
  summary_line: SOC 2 Type II, SOC 1, ISO 27001:2022, ISO 42001, HIPAA, GDPR
slug: linx
tags:
- Company
- Cybersecurity
- Identity Security
- Identity Governance
- IGA
- Access Management
- Non-Human Identity
- Agentic Identity
- Just-In-Time Access
- MCP
website: https://www.linx.security/
---
