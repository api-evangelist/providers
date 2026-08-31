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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The OpenCTI platform exposes a full GraphQL API on the /graphql endpoint for programmatic access to cyber threat intelligence knowledge modeled on STIX 2.1. Authentication uses a per-user bearer API t
  name: OpenCTI GraphQL API
  slug: opencti-graphql-api
- description: OpenAEV (formerly OpenBAS) is an ISO 22398-aligned platform for planning and running crisis exercises, adversary simulations, and breach-and-attack simulation. It ships a RESTful API and a UX-oriented
  name: OpenAEV REST API
  slug: openaev-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Filigran Opencti Webhooks
  slug: filigran-opencti-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filigran-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://filigran.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.opencti.io/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opencti.io/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opencti.io/latest/reference/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opencti.io/latest/usage/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://filigran.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FiligranHQ
- group: operate
  title: ''
  type: Support
  url: https://academy.filigran.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://filigran.io/terms-of-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://filigran.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.filigran.io/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.opencti.io/latest/administration/product-life-cycle/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/filigran-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/filigran-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/filigran-packages.yml
- group: design
  title: ''
  type: Components
  url: components/filigran-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/filigran-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/filigran-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/filigran-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/filigran-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/filigran-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/filigran-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/filigran-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/filigran-opencti-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/filigran-llms.txt
created: '2026-07-17'
description: Filigran is a cybersecurity company founded in 2022 that builds the eXtended Threat Management (XTM) suite of open-source and enterprise products for cyber threat intelligence, adversary simulation, and crisis management. Its flagship OpenCTI platform exposes a full GraphQL API for structuring, storing, and disseminating STIX 2.1 threat-intelligence knowledge, while OpenAEV (formerly OpenBAS) provides a RESTful API for breach-and-attack simulation and adversarial exposure validation. Filigran maintains official Python clients (pycti, pyobas), a native embedded Model Context Protocol (MCP) server, TAXII 2.1 and SSE live-stream data sharing, webhooks, and a React component / design-system library. The company is SOC 2 Type 2 and ISO/IEC 27001:2022 certified and is backed by Accel and Insight Partners.
image: https://avatars.githubusercontent.com/u/91369524?v=4
layout: provider
mcp_servers:
- description: ''
  name: Filigran MCP Server
  slug: filigran-mcp-server
modified: '2026-07-19'
name: Filigran
nav: Providers
network: true
overview: 'Filigran publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Threat Intelligence, OpenCTI, and OpenAEV.


  The Filigran catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Filigran''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 19 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 45.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filigran/refs/heads/main/screenshots/filigran-2026-07-25T214447.png
security:
- kind: authentication
  name: Filigran Authentication
  slug: filigran-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Filigran Domain Security
  slug: filigran-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: filigran
tags:
- Company
- Cybersecurity
- Threat Intelligence
- OpenCTI
- OpenAEV
- STIX
- GraphQL
- Breach and Attack Simulation
- Open-Source
- Security
website: https://filigran.io/
---
