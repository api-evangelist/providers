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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: List, create, delete and merge branches
  name: Testim Io Branches API
  slug: testim-io-branches-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: Get execution results
  name: Testim Io Executions API
  slug: testim-io-executions-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: Execute labels
  name: Testim Io Labels API
  slug: testim-io-labels-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: The Mobile Applications API from Testim Io — 2 operation(s) for mobile applications.
  name: Testim Io Mobile Applications API
  slug: testim-io-mobile-applications-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: Search suites by name, and execute suites
  name: Testim Io Suites API
  slug: testim-io-suites-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: Search test plans by name, and execute test plans
  name: Testim Io Test plans API
  slug: testim-io-test-plans-api
- baseURL: https://api.testim.io
  baseurl_source: declared
  description: List tests by branch, search by test name, and execute tests
  name: Testim Io Tests API
  slug: testim-io-tests-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Testim.io Public Branches API
  slug: open-testim-io-branches-api
- collection_type: open
  name: Testim.io Public Branches Executions API
  slug: open-testim-io-executions-api
- collection_type: open
  name: Testim.io Public Branches Labels API
  slug: open-testim-io-labels-api
- collection_type: open
  name: Testim.io Public Branches Mobile Applications API
  slug: open-testim-io-mobile-applications-api
- collection_type: open
  name: Testim.io Public Branches Suites API
  slug: open-testim-io-suites-api
- collection_type: open
  name: Testim.io Public Branches Test plans API
  slug: open-testim-io-test-plans-api
- collection_type: open
  name: Testim.io Public Branches Tests API
  slug: open-testim-io-tests-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/testim-io-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testim-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testim-io-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tricentis.com/testim/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tricentis.com/testim/content/administration/api-access.htm
- group: docs
  title: ''
  type: APIReference
  url: https://raw.githubusercontent.com/testimio/public-openapi/main/api.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.testim.io/docs/api-access
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/testimio
- group: company
  title: ''
  type: Blog
  url: https://www.testim.io/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tricentis.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.testim.io/changelog
- group: build
  title: ''
  type: Packages
  url: packages/testim-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/testim-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/testim-io-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/testim-io-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/testim-io-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/testim-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/testim-io-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/testim-io-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/testim-io-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/testim-io-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/testim-io-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/testim-io-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/testim-io-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Testim is an AI-powered functional test automation platform for web and mobile applications, using machine learning to author, run, and self-heal UI tests. Acquired by Tricentis in 2022, Testim is offered as part of the Tricentis quality-engineering portfolio. It exposes a public REST API (api.testim.io, with an EU host at api.eu.testim.io) and an official npm CLI (@testim/testim-cli) so teams can manage test branches; look up and execute tests, suites, labels and test plans from CI/CD; read execution and step-level results; and manage mobile application binaries. Testim was backed by Lightspeed Venture Partners prior to acquisition.
image: https://github.com/testimio.png
layout: provider
mcp_servers:
- description: No official hosted/remote Model Context Protocol (MCP) server was found for Testim (Tricentis) as of this pass. This is a CANDIDATE tool surface derived 1:1 from the public REST API operations, showin
  name: Testim Io MCP Server
  slug: testim-io-mcp-server
modified: '2026-07-21'
name: Testim Io
nav: Providers
network: true
overview: 'Testim Io publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Executions API, Labels API, and 4 more. Tagged areas include API Testing, Test Automation, Quality Assurance, CI/CD, and Mobile Testing.


  Testim Io''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, CLI, and 18 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 4.5
    contract_quality: 50.1
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 40.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testim-io/refs/heads/main/screenshots/testim-io-2026-08-17T082328.png
security:
- kind: authentication
  name: Testim Io Authentication
  slug: testim-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Testim Io Domain Security
  slug: testim-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Testim Io Trust Center
  slug: testim-io-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022
slug: testim-io
tags:
- API Testing
- Test Automation
- Quality Assurance
- CI/CD
- Mobile Testing
- Software Testing
- DevOps
- Company
website: https://docs.tricentis.com/testim/
---
