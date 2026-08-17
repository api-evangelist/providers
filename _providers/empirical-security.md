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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Empirical Security Agentic Access
  operation_count: 9
  slug: empirical-security-agentic-access
  summary_line: 9 operations
api_count: 3
apis:
- description: Saved CVE queries and their execution.
  name: Empirical Security CVE Groups API
  slug: empirical-security-cve-groups-api
- description: Retrieve CVE detail, scores, malware hashes and history.
  name: Empirical Security CVEs API
  slug: empirical-security-cves-api
- description: Query CVEs using Empirical search syntax.
  name: Empirical Security Search API
  slug: empirical-security-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Empirical Security CVE Groups API
  slug: open-empirical-security-cve-groups-api
- collection_type: open
  name: Empirical Security CVE Groups CVEs API
  slug: open-empirical-security-cves-api
- collection_type: open
  name: Empirical Security CVE Groups Search API
  slug: open-empirical-security-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/empirical-security-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.empiricalsecurity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.empiricalsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.empiricalsecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.empiricalsecurity.com/api_reference/cves
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.empiricalsecurity.com/authentication
- group: company
  title: ''
  type: Blog
  url: https://research.empiricalsecurity.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.empiricalsecurity.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.empiricalsecurity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.empiricalsecurity.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.empiricalsecurity.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/empirical-security-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/empirical-security-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/empirical-security-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/empirical-security-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/empirical-security-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/empirical-security-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/empirical-security-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/empirical-security-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/empirical-security-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/empirical-security-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/empirical-security-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/empirical-security-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Empirical Security builds data-driven models that predict which vulnerabilities will actually be exploited, so security teams can prioritize remediation by real-world risk instead of raw CVSS severity. It operates the Foundation (global) model, which combines real-time internet exploitation telemetry with EPSS and monitors 18,000+ exploited CVEs; hourly-updated EPSS models (epss_v3, epss_v4, epss_v5); and Radiant, an organization-specific model that layers your local assets, configurations and internal telemetry on top of the Foundation data. The read-only REST API exposes CVE detail, per-model scores and percentiles, malware hashes, critical indicators, score history, change history, full dataset export, search, and saved CVE groups, secured with OAuth 2.0 client credentials (JWT bearer). Empirical Security is backed by Costanoa Ventures.
image: https://www.empiricalsecurity.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: empirical-security-mcp.yml
  slug: empirical-security-mcpyml
modified: '2026-07-19'
name: Empirical Security
nav: Providers
network: true
overview: 'Empirical Security publishes 3 APIs on the [APIs.io](https://apis.io/) network: CVE Groups API, CVEs API, and Search API. Tagged areas include Company, Security, Cybersecurity, Vulnerability Management, and Vulnerability Prioritization.


  Empirical Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 95
scopes:
- name: Empirical Security Scopes
  scope_count: 1
  slug: empirical-security-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 15.7
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/empirical-security/refs/heads/main/screenshots/empirical-security-2026-07-25T213247.png
security:
- kind: authentication
  name: Empirical Security Authentication
  slug: empirical-security-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Empirical Security Domain Security
  slug: empirical-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: empirical-security
tags:
- Company
- Security
- Cybersecurity
- Vulnerability Management
- Vulnerability Prioritization
- CVE
- EPSS
- Exploit Prediction
- Threat Intelligence
website: https://www.empiricalsecurity.com
---
