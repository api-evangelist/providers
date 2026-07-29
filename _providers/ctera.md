---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful management API for the CTERA Portal. Exposes a uniform object namespace (users, devices, folders, and more) where each object is addressed by a unique URI, using GET/PUT/POST/DELETE verbs. Aut
  name: CTERA Portal RESTful API
  slug: ctera-portal-restful-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ctera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ctera.com/help/portal/6.0/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.ctera.com/help/portal/6.0/api/CTERA%20Portal%20APIs.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ctera.com/help/portal/6.0/api/CTERA%20Portal%20APIs/CTERA_Portal_API_Developer_Guide2.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://kb.ctera.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ctera.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.ctera.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ctera
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ctera.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ctera.com/privacy-policy/
- group: learn
  title: ''
  type: Training
  url: https://www.ctera.com/ctera-training/
- group: build
  title: ''
  type: Packages
  url: packages/ctera-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ctera-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ctera-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ctera-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ctera-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ctera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ctera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ctera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ctera-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ctera-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ctera-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ctera-domain-security.yml
created: '2026-07-17'
description: CTERA operates the CTERA Intelligent Data Platform, a unified edge-to-cloud global file system and data fabric for managing unstructured file data across distributed enterprises. The platform combines secure file collaboration, cyber protection and ransomware defense, global file locking, enterprise search, data classification, and AI-readiness (InsightAI) over a single global namespace spanning edge, data center, and public cloud. CTERA is programmable through a RESTful Portal management API (uniform object namespace addressed by URIs), an official Apache-2.0 Python SDK (cterasdk), a CLI toolbox (ctools), and two official Model Context Protocol servers (mcp-ctera-core and mcp-ctera-edge) that give AI agents file-and-folder operations over the Portal and Edge Filer. CTERA was surfaced as a portfolio company of Bessemer Venture Partners.
image: https://www.ctera.com/wp-content/uploads/2021/03/ctera-logo.png
layout: provider
mcp_servers:
- description: ''
  name: ctera-mcp.yml
  slug: ctera-mcpyml
modified: '2026-07-18'
name: CTERA
nav: Providers
network: true
overview: 'CTERA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Storage, File Storage, and Global File System.


  CTERA''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, training material, CLI, and 17 more developer resources.'
random_paper: 53
score:
  band: thin
  composite: 29.4
  delta: -1.2
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 30.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ctera/refs/heads/main/screenshots/ctera-2026-07-25T210844.png
security:
- kind: authentication
  name: Ctera Authentication
  slug: ctera-authentication
  summary_line: session-cookie · 1 scheme
- kind: domain-security
  name: Ctera Domain Security
  slug: ctera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ctera
tags:
- Company
- Cloud
- Storage
- File Storage
- Global File System
- Data Management
- Edge Computing
- Cyber Protection
- Hybrid Cloud
- Unstructured Data
website: https://www.ctera.com/
---
