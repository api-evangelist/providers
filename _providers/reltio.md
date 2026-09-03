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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Tenant-scoped REST API for the Reltio Context Intelligence Platform: entities, relations, interactions, reference data, load/export, data integration, workflow, hierarchy, statistics, and validation. '
  name: Reltio Context Intelligence Platform REST API
  slug: reltio-context-intelligence-platform-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.reltio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reltio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reltio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.reltio.com/en/developer-resources
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reltio.com/en/developer-resources
- group: operate
  title: ''
  type: Support
  url: https://support.reltio.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.reltio.com/home
- group: company
  title: ''
  type: Blog
  url: https://www.reltio.com/resources/?_resource_types=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reltio-ai
- group: start
  title: ''
  type: SignUp
  url: https://www.reltio.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://login.reltio.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reltio.com/reltio-website-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reltio.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reltio.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reltio-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/reltio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reltio-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reltio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reltio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reltio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reltio-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.reltio.com/en/whats-new/release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/reltio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.reltio.com/trust/
- group: auth
  title: ''
  type: TrustCenter
  url: security/reltio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reltio-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reltio-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reltio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Reltio is a cloud-native, AI-native master data management (MDM) and Context Intelligence Platform that unifies, cleanses, harmonizes, governs, and activates enterprise data from many sources in real time. It delivers trusted "golden records" via multidomain MDM, LLM-driven entity resolution, data quality, and data integration (1,000+ connectors), and exposes that governed data to AI agents through AgentFlow and a Model Context Protocol (MCP) server. Founded in 2011 and headquartered in Redwood Shores, CA, Reltio became part of SAP SE in May 2026 and is being integrated into SAP Business Data Cloud while remaining available standalone.
image: https://avatars.githubusercontent.com/u/3045483?v=4
layout: provider
mcp_servers:
- description: ''
  name: Reltio AgentFlow + Developer MCP Server
  slug: reltio-agentflow-developer-mcp-server
modified: '2026-07-21'
name: Reltio
nav: Providers
network: true
overview: 'Reltio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Master Data Management, MDM, and Entity Resolution.


  Reltio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 36.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reltio/refs/heads/main/screenshots/reltio-2026-09-02T153324.png
security:
- kind: authentication
  name: Reltio Authentication
  slug: reltio-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Reltio Domain Security
  slug: reltio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reltio Trust Center
  slug: reltio-trust-center
  summary_line: ISO 27001, HITRUST CSF, NIST 800-53, GDPR
slug: reltio
tags:
- Company
- Data Analytics
- Master Data Management
- MDM
- Entity Resolution
- Data Quality
- Data Integration
- AI Agents
- MCP
- SAP
website: https://www.reltio.com/
---
