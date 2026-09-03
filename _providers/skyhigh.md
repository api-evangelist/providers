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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Skyhigh Agentic Access
  operation_count: 4
  slug: skyhigh-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://www.myshn.net/shnapi/rest/external/api
  baseurl_source: declared
  description: The Tenant API from Skyhigh Security — 4 operation(s) for tenant.
  name: Skyhigh Security Tenant API
  slug: skyhigh-tenant-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Skyhigh Networks External APIs Tenant API
  slug: open-skyhigh-tenant-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/skyhigh-incidents-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.skyhighsecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://success.skyhighsecurity.com/Skyhigh_SSE_APIs/Skyhigh_Security_SSE_APIs
- group: docs
  title: ''
  type: Documentation
  url: https://success.skyhighsecurity.com/Skyhigh_SSE_APIs/Skyhigh_Security_SSE_APIs
- group: docs
  title: ''
  type: APIReference
  url: https://success.skyhighsecurity.com/Skyhigh_SSE_APIs/Incidents_API/Incidents_API_Definitions
- group: start
  title: ''
  type: GettingStarted
  url: https://success.skyhighsecurity.com/Skyhigh_SSE_APIs/User_Management_API/User_Creation_API
- group: operate
  title: ''
  type: Support
  url: https://www.skyhighsecurity.com/support.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SkyhighSecurity
- group: company
  title: ''
  type: Blog
  url: https://www.skyhighsecurity.com/about/resources/resource-center.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skyhighsecurity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.skyhighsecurity.com/about/certification.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.skyhighsecurity.com/about/certification.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyhigh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skyhigh-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyhigh-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skyhigh-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skyhigh-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skyhigh-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skyhigh-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyhigh-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skyhigh-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skyhigh-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skyhigh-llms.txt
created: '2026-07-17'
description: Skyhigh Security is a cloud-native Security Service Edge (SSE) platform that protects enterprise data across web, cloud, and private applications. Its portfolio spans Cloud Access Security Broker (CASB), Secure Web Gateway (SWG), Data Loss Prevention (DLP and Advanced DLP), Zero Trust Network Access (ZTNA), and Data Security Posture Management (DSPM). Skyhigh exposes REST "SSE APIs" (served from regional myshn.net hosts) for user management, querying and modifying DLP/policy incidents, and forensics reporting, secured with IAM bearer tokens. Formerly the cloud business of McAfee Enterprise / MVISION Cloud, Skyhigh Security is a Greylock-backed cybersecurity company holding FedRAMP High, SOC 2 Type II, and ISO/IEC 27001 authorizations.
image: https://www.skyhighsecurity.com/content/dam/skyhigh/global/logos/skyhigh-security-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Skyhigh Security MCP Server
  slug: skyhigh-security-mcp-server
modified: '2026-07-21'
name: Skyhigh Security
nav: Providers
network: true
overview: 'Skyhigh Security publishes 1 API on the [APIs.io](https://apis.io/) network: Tenant API. Tagged areas include Company, Cybersecurity, Security Service Edge, CASB, and Secure Web Gateway.


  Skyhigh Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 3
scopes:
- name: Skyhigh Scopes
  scope_count: 3
  slug: skyhigh-scopes
  summary_line: 3 scopes · implicit
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyhigh/refs/heads/main/screenshots/skyhigh-2026-09-02T155807.png
security:
- kind: authentication
  name: Skyhigh Authentication
  slug: skyhigh-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Skyhigh Domain Security
  slug: skyhigh-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Skyhigh Trust Center
  slug: skyhigh-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, FedRAMP High, DoD Impact Level (IL2 & IL4), CSA STAR Level 1, IRAP PROTECTED, BSI C5, GDPR, DPDPA, DORA
slug: skyhigh
tags:
- Company
- Cybersecurity
- Security Service Edge
- CASB
- Secure Web Gateway
- Data Loss Prevention
- Cloud Security
- Zero Trust
- SASE
website: https://www.skyhighsecurity.com/
---
