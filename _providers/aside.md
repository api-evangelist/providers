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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aside-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aside.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aside.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aside.com/help/get-started
- group: operate
  title: ''
  type: Support
  url: https://aside.com/community
- group: company
  title: ''
  type: Blog
  url: https://aside.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aside.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aside.com/policy/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aside.com/policy/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aside.com/changelog/native
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aside-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aside-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/aside-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/aside-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aside-llms.txt
created: '2026-07-17'
description: Aside is an AI-powered browser from a Y Combinator (Fall 2025) startup that runs an autonomous browser agent to complete real work across the logged-in websites you already use — email, dashboards, internal tools, documents, and spreadsheets — without relying on per-service API integrations. It pairs browsing history used as local memory with the first password manager designed for AI agents (hardware-backed encryption, audit logging), keeps data local-first and end-to-end encrypted, and gates sensitive actions like payments and messages behind human approval. For developers, Aside ships a command-line interface, a Model Context Protocol (MCP) server, and a browser-automation REPL so other agents and coding tools can drive the browser, plus bring-your-own-key support for OpenAI and Anthropic models.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aside.png
layout: provider
mcp_servers:
- description: Aside ships a first-party Model Context Protocol server exposed through its CLI (`aside mcp`). Any MCP-capable agent or coding tool can connect to it to drive the Aside AI browser as a browser-automat
  name: Aside MCP server
  slug: aside-mcp-server
modified: '2026-07-18'
name: Aside
nav: Providers
network: true
overview: 'Aside is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Browser, Browser Agent, Automation, and MCP.


  Aside''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, changelog, CLI, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 21.3
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aside/refs/heads/main/screenshots/aside-2026-07-25T201426.png
security:
- kind: domain-security
  name: Aside Domain Security
  slug: aside-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aside
tags:
- Company
- AI Browser
- Browser Agent
- Automation
- MCP
- CLI
- Password Manager
- Agentic
- Web Automation
- Developer Tools
- Y Combinator
website: https://aside.com
---
