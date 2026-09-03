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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trope-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trope-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trope-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/trope-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/trope-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trope-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trope-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://trope.ai
- group: start
  title: ''
  type: Login
  url: https://trope.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trope.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trope.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:founders@trope.ai
- group: company
  title: ''
  type: Blog
  url: https://trope.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tropeai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/trope_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tropeai
created: '2026-07-17'
description: Trope is an AI-native platform that helps ERP implementation partners deliver successful implementations faster, deploying AI agents across discovery, requirements, fit-gap analysis, data migration, approval workflows, UAT scripts, training guides, documentation, and go-live readiness — built for Microsoft Dynamics 365 Business Central consultancies and other implementation teams. Trope also maintains Trope CUA, an open-source MCP-native computer-use agent for background desktop automation on Windows and macOS. Y Combinator Summer 2026 batch, based in San Francisco.
image: https://trope.ai/images/og-image-trope-preview.png
layout: provider
mcp_servers:
- description: 'Trope publishes Trope CUA, an open-source (MIT) MCP-native computer-use agent for background desktop automation on Windows and macOS. It exposes target-window screenshots, accessibility trees, action '
  name: Trope MCP Server
  slug: trope-mcp-server
modified: '2026-07-21'
name: Trope
nav: Providers
network: true
overview: 'Trope is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, ERP, and Enterprise Software.


  Trope''s developer surface includes CLI, changelog, support, engineering blog, and 12 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 18.1
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trope/refs/heads/main/screenshots/trope-2026-09-02T164314.png
security:
- kind: domain-security
  name: Trope Domain Security
  slug: trope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trope Trust Center
  slug: trope-trust-center
  summary_line: trust center published
slug: trope
tags:
- Company
- Artificial Intelligence
- Agents
- ERP
- Enterprise Software
- Computer Use
- MCP
- Automation
website: https://trope.ai
---
