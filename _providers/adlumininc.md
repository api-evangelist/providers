---
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Adlumininc Agentic Access
  operation_count: 11
  slug: adlumininc-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 2
apis:
- baseURL: https://api.adlumin.com/v1
  baseurl_source: declared
  description: Tenant-scoped REST API over the Adlumin security operations platform. Eleven v1 endpoints return security detections (with bulk acknowledgement), at-risk Active Directory groups, network shares and sy
  name: Adlumin XDR/MDR API
  slug: adlumin-xdrmdr-api
- description: First-party Model Context Protocol server distributed by N-able as a downloadable Python package. Wraps the eleven Adlumin v1 REST endpoints as thirteen MCP tools (including two firewall aggregation t
  name: Adlumin MCP Server
  slug: adlumin-mcp-server
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adlumininc-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.n-able.com/products/adlumin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.n-able.com/adlumin
- group: docs
  title: ''
  type: Documentation
  url: https://developer.n-able.com/adlumin/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.n-able.com/adlumin/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.n-able.com/adlumin/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.n-able.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.n-able.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Adlumin
- group: start
  title: ''
  type: Login
  url: https://portal.adlumin.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.n-able.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.n-able.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.n-able.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://status.n-able.com/release-notes/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.n-able.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.n-able.com/
- group: auth
  title: ''
  type: Security
  url: https://www.n-able.com/security-and-privacy/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adlumininc-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adlumininc-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adlumininc-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adlumininc-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/adlumininc-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adlumininc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adlumininc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/adlumininc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adlumininc-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adlumininc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adlumininc-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adlumininc-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adlumininc-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adlumininc-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adlumininc-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adlumininc-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adlumininc-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adlumininc-api-overlay.yaml
created: '2026-09-07'
description: Adlumin is an N-able company providing a cloud-native security operations platform for mid-market organizations, financial institutions, government agencies and managed service providers. One license combines XDR, 24/7 expert-led MDR, SIEM log management, in-platform SOAR response actions, UEBA, darknet exposure monitoring, honeypots, identity threat detection and response, vulnerability management and audit-ready compliance reporting. Adlumin publishes a public developer portal on N-able's developer site carrying an OpenAPI 3.0.3 description of the Adlumin XDR/MDR v1 REST API (detections, at-risk assets, endpoint and device telemetry, network health, firewall events and compliance insights) plus a downloadable Python MCP server that exposes those same endpoints to AI assistants as thirteen agent tools.
image: https://files.readme.io/c620a71e287577ffddb7a699ae4af380b1058444317a4e596f65ceacddea83f4-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: Adlumin MCP Server
  slug: adlumin-mcp-server
modified: '2026-09-07'
name: Adlumin
nav: Providers
network: true
overview: 'Adlumin publishes 1 API on the [APIs.io](https://apis.io/) network: XDR/MDR API. Tagged areas include Security, Cybersecurity, Managed Detection and Response, Extended Detection and Response, and SIEM.


  Adlumin''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 29 more developer resources.'
plans:
- name: Adlumininc Plans Pricing
  plan_count: 0
  slug: adlumininc-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Adlumininc Rate Limits
  slug: adlumininc-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Adlumininc Authentication
  slug: adlumininc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adlumininc Domain Security
  slug: adlumininc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adlumininc Vulnerability Disclosure
  slug: adlumininc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adlumininc
tags:
- Security
- Cybersecurity
- Managed Detection and Response
- Extended Detection and Response
- SIEM
- SOAR
- Threat Detection
- Endpoint Security
- Compliance
- Managed Service Providers
- MCP
- agent-native
website: https://www.n-able.com/products/adlumin
---
