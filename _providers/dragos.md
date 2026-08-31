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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dragos Agentic Access
  operation_count: 9
  slug: dragos-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Customer-gated Dragos Platform SiteStore v2 API for tenants to read OT assets and alerts from their monitoring platform. Per-tenant host of the form https://<company>.platform.dragos.cloud. Authentica
  name: Dragos Platform SiteStore API
  slug: dragos-platform-sitestore-api
- description: The Indicators API from Dragos — 3 operation(s) for indicators.
  name: Dragos Indicators API
  slug: dragos-indicators-api
- description: The Products API from Dragos — 4 operation(s) for products.
  name: Dragos Products API
  slug: dragos-products-api
- description: The Tags API from Dragos — 2 operation(s) for tags.
  name: Dragos Tags API
  slug: dragos-tags-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dragos WorldView Indicators API
  slug: open-dragos-indicators-api
- collection_type: open
  name: Dragos WorldView Indicators Products API
  slug: open-dragos-products-api
- collection_type: open
  name: Dragos WorldView Indicators Tags API
  slug: open-dragos-tags-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dragos-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.dragos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dragos.com/
- group: docs
  title: ''
  type: APIReference
  url: https://portal.dragos.com/api/v1/doc/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.dragos.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dragos.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dragosinc
- group: operate
  title: ''
  type: Support
  url: https://www.dragos.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dragos.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dragos.com/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/dragos-worldview-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/dragos-worldview-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/dragos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dragos-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dragos-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dragos-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dragos-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dragos-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/dragos-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dragos.com/security-program/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dragos-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dragos-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/dragos-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dragos-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dragos-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dragos-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dragos-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dragos-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dragos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dragos.com/reporting-security-issues-to-dragos/
created: '2026-07-17'
description: Dragos is an industrial (OT/ICS) cybersecurity company whose platform delivers OT asset visibility, threat detection, vulnerability management, and investigation and response purpose-built for industrial control system environments, supporting 600+ ICS protocols. Its public developer surface is the WorldView threat-intelligence API, which exposes Dragos WorldView reports and indicators of compromise (IP, domain, hostname, filename, MD5/SHA1/SHA256) for OT/ICS threats, with STIX 2.0 and CSV exports and tag-based classification. The Dragos Platform additionally offers a customer-gated SiteStore v2 API for tenants to read assets and alerts from the OT monitoring platform. Dragos is ISO/IEC 27001:2022 certified and provides SOC 2 Type II reports under NDA.
image: https://www.dragos.com/wp-content/uploads/2021/06/dragos-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Dragos MCP Server
  slug: dragos-mcp-server
modified: '2026-07-18'
name: Dragos
nav: Providers
network: true
overview: 'Dragos publishes 3 APIs on the [APIs.io](https://apis.io/) network: Indicators API, Products API, and Tags API. Tagged areas include Company, Cybersecurity, OT Security, ICS, and Threat Intelligence.


  Dragos'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 24 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 48.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dragos/refs/heads/main/screenshots/dragos-2026-07-25T212343.png
security:
- kind: authentication
  name: Dragos Authentication
  slug: dragos-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Dragos Domain Security
  slug: dragos-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dragos Vulnerability Disclosure
  slug: dragos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dragos
tags:
- Company
- Cybersecurity
- OT Security
- ICS
- Threat Intelligence
- Industrial Control Systems
- Indicators of Compromise
- STIX
- Vulnerability Management
- Security
website: https://portal.dragos.com/
---
