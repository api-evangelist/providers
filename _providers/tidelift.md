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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 33
  human_in_the_loop: 2
  name: Tidelift Agentic Access
  operation_count: 66
  slug: tidelift-agentic-access
  summary_line: 66 operations · 33 acting · 2 human-in-the-loop
api_count: 15
apis:
- description: The Alignments API from Tidelift — 4 operation(s) for alignments.
  name: Tidelift Alignments API
  slug: tidelift-alignments-api
- description: The Attestations API from Tidelift — 2 operation(s) for attestations.
  name: Tidelift Attestations API
  slug: tidelift-attestations-api
- description: A [Tidelift API key](https://docs.tidelift.com/article/79-api-authentication) is required for all endpoints. If a particular type of API key is required it will be noted on the path. <SecurityDefiniti
  name: Tidelift Authentication API
  slug: tidelift-authentication-api
- description: '* curl ``` curl -H "Accept: application/json" \ -H "Authorization: bearer <your Tidelift API key>" \ https://api.tidelift.com/external-api/v1/packages/pypi/urllib3 ``` More detailed examples can be fo'
  name: Tidelift Basic Examples API
  slug: tidelift-basic-examples-api
- description: The Catalog Releases API from Tidelift — 7 operation(s) for catalog releases.
  name: Tidelift Catalog Releases API
  slug: tidelift-catalog-releases-api
- description: The Catalogs API from Tidelift — 9 operation(s) for catalogs.
  name: Tidelift Catalogs API
  slug: tidelift-catalogs-api
- description: The CatalogStandards API from Tidelift — 3 operation(s) for catalogstandards.
  name: Tidelift CatalogStandards API
  slug: tidelift-catalogstandards-api
- description: The Groups API from Tidelift — 5 operation(s) for groups.
  name: Tidelift Groups API
  slug: tidelift-groups-api
- description: The Licenses API from Tidelift — 5 operation(s) for licenses.
  name: Tidelift Licenses API
  slug: tidelift-licenses-api
- description: The Packages API from Tidelift — 6 operation(s) for packages.
  name: Tidelift Packages API
  slug: tidelift-packages-api
- description: The Projects API from Tidelift — 6 operation(s) for projects.
  name: Tidelift Projects API
  slug: tidelift-projects-api
- description: The Releases API from Tidelift — 5 operation(s) for releases.
  name: Tidelift Releases API
  slug: tidelift-releases-api
- description: The Reports API from Tidelift — 3 operation(s) for reports.
  name: Tidelift Reports API
  slug: tidelift-reports-api
- description: The Users API from Tidelift — 1 operation(s) for users.
  name: Tidelift Users API
  slug: tidelift-users-api
- description: The Vulnerabilities API from Tidelift — 2 operation(s) for vulnerabilities.
  name: Tidelift Vulnerabilities API
  slug: tidelift-vulnerabilities-api
arazzos:
- description: Validate the API key, look up a package and a release, and pull the release's vulnerabilities.
  name: Tidelift — package vulnerability check
  slug: tidelift-package-vulnerability-check.arazzo
artifact_total: 38
asyncapis:
- description: ''
  name: Tidelift Webhooks
  slug: tidelift-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tidelift External Alignments API
  slug: open-tidelift-alignments-api
- collection_type: open
  name: Tidelift External Alignments Attestations API
  slug: open-tidelift-attestations-api
- collection_type: open
  name: Tidelift External Alignments Authentication API
  slug: open-tidelift-authentication-api
- collection_type: open
  name: Tidelift External Alignments Basic Examples API
  slug: open-tidelift-basic-examples-api
- collection_type: open
  name: Tidelift External Alignments Catalog Releases API
  slug: open-tidelift-catalog-releases-api
- collection_type: open
  name: Tidelift External Alignments Catalogs API
  slug: open-tidelift-catalogs-api
- collection_type: open
  name: Tidelift External Alignments CatalogStandards API
  slug: open-tidelift-catalogstandards-api
- collection_type: open
  name: Tidelift External Alignments Groups API
  slug: open-tidelift-groups-api
- collection_type: open
  name: Tidelift External Alignments Licenses API
  slug: open-tidelift-licenses-api
- collection_type: open
  name: Tidelift External Alignments Packages API
  slug: open-tidelift-packages-api
- collection_type: open
  name: Tidelift External Alignments Projects API
  slug: open-tidelift-projects-api
- collection_type: open
  name: Tidelift External Alignments Releases API
  slug: open-tidelift-releases-api
- collection_type: open
  name: Tidelift External Alignments Reports API
  slug: open-tidelift-reports-api
- collection_type: open
  name: Tidelift External Alignments Users API
  slug: open-tidelift-users-api
- collection_type: open
  name: Tidelift External Alignments Vulnerabilities API
  slug: open-tidelift-vulnerabilities-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/tidelift-subscriber-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tidelift.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://support.tidelift.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://api.tidelift.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tidelift.com/article/79-api-authentication
- group: operate
  title: ''
  type: Support
  url: https://support.tidelift.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://tidelift.com/subscription/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tidelift
- group: build
  title: ''
  type: Postman
  url: https://github.com/tidelift/tidelift-api-postman
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tidelift.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/tidelift-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tidelift-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tidelift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tidelift.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tidelift-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tidelift-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tidelift-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/tidelift-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tidelift-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tidelift-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tidelift-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tidelift-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/tidelift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tidelift-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tidelift-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tidelift-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tidelift-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tidelift-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tidelift-package-vulnerability-check.arazzo.yml
created: '2026-07-17'
description: Tidelift provides open-source software supply-chain management for enterprises. Its platform combines package intelligence (maintenance, quality, end-of-life, and vulnerability signals) with catalogs of approved dependencies, policy and license standards enforcement, SBOM import/export, and "alignment" of projects against an organization's standards. Tidelift is distinctive for paying the open-source maintainers ("lifters") behind the packages enterprises rely on. The Tidelift External API (OpenAPI 3.0, Bearer API-key auth) exposes catalogs, violations, projects, groups, packages, releases, vulnerabilities, licenses, and reporting. Tidelift was acquired by Sonar in 2025; the API and developer surface remain active.
image: https://api.tidelift.com/docs/assets/tidelift_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Tidelift MCP Server
  slug: tidelift-mcp-server
modified: '2026-07-21'
name: Tidelift
nav: Providers
network: true
overview: 'Tidelift publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Alignments API, Attestations API, Authentication API, and 12 more. Tagged areas include Company, Open-Source, Software Supply Chain, Dependency Management, and Application Security.


  The Tidelift catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tidelift''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, CLI, and 23 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 59.2
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tidelift/refs/heads/main/screenshots/tidelift-2026-08-17T082353.png
security:
- kind: authentication
  name: Tidelift Authentication
  slug: tidelift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tidelift Domain Security
  slug: tidelift-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tidelift Vulnerability Disclosure
  slug: tidelift-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tidelift
tags:
- Company
- Open-Source
- Software Supply Chain
- Dependency Management
- Application Security
- SBOM
- License Compliance
- Vulnerability Management
- Developer Tools
website: https://api.tidelift.com/docs/
---
