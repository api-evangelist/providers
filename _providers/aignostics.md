---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-09-17'
api_count: 1
apis:
- baseURL: https://platform.aignostics.com/api/v1
  baseurl_source: declared
  description: The Public API from Aignostics — 21 operation(s) for public.
  name: Aignostics Public API
  slug: aignostics-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Aignostics Event Surface
  slug: aignostics-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.aignostics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aignostics.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://aignostics.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://aignostics.readthedocs.io/en/latest/api_explorer_v1.html
- group: start
  title: ''
  type: GettingStarted
  url: https://aignostics.readthedocs.io/en/latest/get_started_api.html
- group: start
  title: ''
  type: SignUp
  url: https://platform.aignostics.com/
- group: operate
  title: ''
  type: Support
  url: https://www.aignostics.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.aignostics.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aignostics
- group: start
  title: ''
  type: Console
  url: https://platform.aignostics.com/api/v1/docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aignostics/python-sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aignostics.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aignostics.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/lifecycle/aignostics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aignostics-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/changelog/aignostics-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aignostics-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/packages/aignostics-packages.yml
  title: ''
  type: Packages
  url: packages/aignostics-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/packages/aignostics-packages.yml
  title: ''
  type: SDKs
  url: packages/aignostics-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/cli/aignostics-cli.yml
  title: ''
  type: CLI
  url: cli/aignostics-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/authentication/aignostics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aignostics-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/scopes/aignostics-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aignostics-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/conventions/aignostics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aignostics-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/errors/aignostics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aignostics-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/data-model/aignostics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aignostics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/conformance/aignostics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aignostics-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/rate-limits/aignostics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aignostics-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/plans/aignostics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aignostics-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/security/aignostics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aignostics-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/security/aignostics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aignostics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/security/aignostics-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aignostics-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/mcp/aignostics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aignostics-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/mcp/aignostics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aignostics-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/llms/aignostics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aignostics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aignostics/refs/heads/main/overlays/aignostics-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aignostics-platform-api-overlay.yaml
created: '2026-09-14'
description: 'Aignostics GmbH is a Berlin-based computational pathology company, spun out of Charite Universitaetsmedizin Berlin, that builds AI foundation models and analysis applications for whole slide images (WSI). Its commercial surface is the Aignostics Platform, a cloud service that runs computational pathology applications - Atlas H&E-TME tumor-microenvironment profiling is the flagship - on dedicated NVIDIA GPU infrastructure, with a per-organization Google Cloud Storage bucket and Auth0-backed enterprise SSO. The Platform is reachable three ways: a browser Console, an open-source Python SDK (Launchpad desktop app, CLI, client library and an in-development MCP server), and a public REST contract - the Aignostics Platform API, an OpenAPI 3.1.0 document with 26 operations served unauthenticated at https://platform.aignostics.com/api/v1/openapi.json. The API covers application and version discovery, run submission and cancellation, per-item result and artifact retrieval, custom metadata
  with checksum-guarded writes, and an access-grant / share-token sharing model. Access is organization-scoped: there is no anonymous access and no organization-wide API key.'
image: https://cdn.prod.website-files.com/67adb01f31489469b513304a/67eec0230902714317f91424_ag-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Central Aignostics MCP Server
  slug: central-aignostics-mcp-server
modified: '2026-09-14'
name: Aignostics
nav: Providers
network: true
overview: 'Aignostics publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Health, and Healthcare.


  The Aignostics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aignostics'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, developer console, and 27 more developer resources.'
plans:
- name: Aignostics Plans Pricing
  plan_count: 0
  slug: aignostics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Aignostics Rate Limits
  slug: aignostics-rate-limits
scopes:
- name: Aignostics Scopes
  scope_count: 0
  slug: aignostics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 80.4
    discoverability: 68.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 56.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Aignostics Authentication
  slug: aignostics-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Aignostics Domain Security
  slug: aignostics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aignostics Vulnerability Disclosure
  slug: aignostics-vulnerability-disclosure
  summary_line: Hackerone
slug: aignostics
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Health
- Healthcare
- Life Sciences
- Pathology
- Medical Imaging
- Digital Pathology
- Oncology
- Biotechnology
- Research
- Germany
website: https://www.aignostics.com/
---
