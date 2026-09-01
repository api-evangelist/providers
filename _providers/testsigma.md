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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API to manage Testsigma entities (projects, applications, environments, elements, uploads, test plans) and to trigger and poll test-plan executions remotely. Authenticated with a Bearer API Key.
  name: Testsigma REST API
  slug: testsigma-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://testsigma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://testsigma.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://testsigma.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://testsigma.com/docs/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://testsigma.com/tutorials/getting-started/automate-rest-apis/
- group: operate
  title: ''
  type: Support
  url: https://support.testsigma.com/
- group: company
  title: ''
  type: Blog
  url: https://testsigma.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/testsigmahq
- group: commercial
  title: ''
  type: Pricing
  url: https://testsigma.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://testsigma.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://testsigma.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://testsigma.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.testsigma.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/testsigma-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/testsigma-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testsigma-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/testsigma-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/testsigma-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/testsigma-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/testsigma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/testsigma-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/testsigma-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/testsigma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/testsigma-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/testsigma-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.testsigma.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/testsigma-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testsigma-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/testsigma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://testsigma.com/security
created: '2026-07-17'
description: Testsigma is an agentic, GenAI-powered codeless test automation platform. AI co-workers work alongside QA teams to author and maintain automated tests in natural language across web, mobile, desktop, API, and packaged applications like Salesforce and SAP. Testsigma exposes a REST API (app.testsigma.com/api/v1, Bearer API-Key authentication) to manage projects, applications, environments, elements, uploads, and test plans, and to trigger and poll test-plan executions remotely from CI/CD pipelines. A Community Edition is open source under Apache 2.0. Testsigma is backed by Accel.
image: https://website-static.testsigma.com/website-next/nextjs/6d1168/favicons/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Testsigma MCP Server
  slug: testsigma-mcp-server
modified: '2026-07-21'
name: Testsigma
nav: Providers
network: true
overview: 'Testsigma publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Testing, Test Automation, and QA.


  Testsigma''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 41.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Testsigma Authentication
  slug: testsigma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Testsigma Domain Security
  slug: testsigma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Testsigma Vulnerability Disclosure
  slug: testsigma-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Testsigma Trust Center
  slug: testsigma-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: testsigma
tags:
- Company
- Artificial Intelligence
- Testing
- Test Automation
- QA
- DevOps
- Continuous Integration
- Software Quality
- Agentic AI
website: https://testsigma.com/
---
