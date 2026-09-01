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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: LeoLabs catalog of tracked LEO objects, their measurements, states and propagations.
  name: LeoLabs catalog API
  slug: leo-labs-catalog-api
- description: LeoLabs radar instruments and their tasking.
  name: LeoLabs instruments API
  slug: leo-labs-instruments-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LeoLabs Platform catalog API
  slug: open-leo-labs-catalog-api
- collection_type: open
  name: LeoLabs Platform catalog instruments API
  slug: open-leo-labs-instruments-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/leo-labs-platform-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leo-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leolabs.space/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.leolabs.space/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leolabs.space/
- group: start
  title: ''
  type: SignUp
  url: https://platform.leolabs.space/
- group: company
  title: ''
  type: Blog
  url: https://www.leolabs.space/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.leolabs.space/newsroom/feed/
- group: operate
  title: ''
  type: Support
  url: mailto:support@leolabs.space
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leolabs.space/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leolabs.space/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.leolabs.space/vulnerability-disclosure/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leo-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leo-labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leo-labs-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leo-labs-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/leo-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leo-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/leo-labs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/leo-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leo-labs-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leo-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leo-labs-conformance.yml
created: '2026-07-17'
description: LeoLabs is a commercial space situational awareness company that operates a global network of phased-array radars and a cloud analytics platform delivering what it calls Persistent Orbital Intelligence for low Earth orbit. It independently tracks more than 23,000 objects in LEO and turns those radar observations into a commercial catalog, orbital state vectors, conjunction alerts, maneuver detection, pattern-of-life analysis and launch support for satellite operators, insurers, defense and civil space agencies. Customers reach the data either through the LeoLabs Platform web interface or, as LeoLabs describes it, "a suite of full-featured RESTful APIs for ground system integration and automation at scale" — the v1 Platform API over the catalog, radar measurements, state vectors, TLEs, ephemeris propagation and radar tasking. The company is backed by Insight Partners.
image: https://leolabs.space/wp-content/uploads/2025/12/leolabs-badge-scaled.png
layout: provider
mcp_servers:
- description: ''
  name: LeoLabs MCP Server
  slug: leolabs-mcp-server
modified: '2026-07-19'
name: LeoLabs
nav: Providers
network: true
overview: 'LeoLabs publishes 2 APIs on the [APIs.io](https://apis.io/) network: catalog API and instruments API. Tagged areas include Company, Space, Satellites, Space Situational Awareness, and Space Traffic Management.


  LeoLabs'' developer surface includes documentation, signup flow, engineering blog, support, authentication, CLI, and 18 more developer resources.'
random_paper: 6
scopes:
- name: Leo Labs Scopes
  scope_count: 0
  slug: leo-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.1
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 28.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leo-labs/refs/heads/main/screenshots/leo-labs-2026-07-25T224917.png
security:
- kind: authentication
  name: Leo Labs Authentication
  slug: leo-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Leo Labs Domain Security
  slug: leo-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leo Labs Vulnerability Disclosure
  slug: leo-labs-vulnerability-disclosure
  summary_line: disclosure policy published
slug: leo-labs
tags:
- Company
- Space
- Satellites
- Space Situational Awareness
- Space Traffic Management
- Orbital Data
- Radar
- Aerospace
- Defense
- Geospatial
website: https://www.leolabs.space/
---
