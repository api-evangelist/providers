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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The FOSSA REST API lets you build integrations and automate open source management workflows — manage projects, revisions, issues, users and teams, release groups, and reports; initiate binary scans; '
  name: FOSSA REST API
  slug: fossa-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Fossa Webhooks
  slug: fossa-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fossa-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://fossa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fossa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fossa.com/docs/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fossa.com/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fossa.com/docs/get-started/your-first-scan
- group: operate
  title: ''
  type: Support
  url: https://support.fossa.com/
- group: company
  title: ''
  type: Blog
  url: https://fossa.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fossas
- group: commercial
  title: ''
  type: Pricing
  url: https://fossa.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fossa.com/account/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fossa.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fossa.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fossa.com
- group: auth
  title: ''
  type: Compliance
  url: https://fossa.com/trust
- group: auth
  title: ''
  type: Authentication
  url: authentication/fossa-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fossa-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/fossa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fossa-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fossa-cli.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fossa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fossa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fossa-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fossa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fossa-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fossa-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fossa-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fossa-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fossa-domain-security.yml
created: '2026-07-17'
description: FOSSA is a software supply chain security and open source management platform that scans codebases, containers, and binaries to detect open source dependencies, then enforces open source license compliance, vulnerability management, and SBOM (CycloneDX/SPDX) obligations across the software development lifecycle. FOSSA exposes a REST API at app.fossa.com/api plus the language-agnostic FOSSA CLI, integrating with 20+ build systems and CI/CD to surface licensing, security, and quality issues, generate attribution and audit reports, and gate pull requests on policy violations. Backed by Bain Capital Ventures and Norwest Venture Partners.
image: https://fossa.com/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Fossa MCP Server
  slug: fossa-mcp-server
modified: '2026-07-19'
name: Fossa
nav: Providers
network: true
overview: 'Fossa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Software Supply Chain, Open-Source, and License Compliance.


  The Fossa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fossa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 48.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fossa/refs/heads/main/screenshots/fossa-2026-07-25T215032.png
security:
- kind: authentication
  name: Fossa Authentication
  slug: fossa-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fossa Domain Security
  slug: fossa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fossa Trust Center
  slug: fossa-trust-center
  summary_line: SOC 2
slug: fossa
tags:
- Company
- Security
- Software Supply Chain
- Open-Source
- License Compliance
- Vulnerability Management
- SBOM
- Software Composition Analysis
- DevSecOps
website: https://fossa.com/
---
