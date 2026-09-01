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
  band: human-only
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API (OpenAPI 3.0.1, "Governor External API" v1.0.0) for the self-hosted Synthesized Governor. Trigger TDK masking/generation workflows, list workers, and check health. Authenticated with an X-Acc
  name: Governor External API
  slug: governor-external-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.synthesized.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synthesized.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synthesized.io/tdk/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.synthesized.io/tdk/latest/user_guide/090_cicd/external_api_reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synthesized.io/tdk/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synthesized-io
- group: company
  title: ''
  type: Blog
  url: https://www.synthesized.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.synthesized.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synthesized.io/synthesized-software-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthesized.io/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/synthesized-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synthesized-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthesized-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthesized-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/synthesized-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthesized-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/synthesized-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synthesized-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synthesized-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/synthesized-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synthesized-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthesized-domain-security.yml
created: '2026-07-17'
description: Synthesized is an AI-native test data management (TDM) platform that automates the provisioning of production-realistic, privacy-preserving data for software testing, database migrations, CI/CD pipelines, and AI/ML validation. Its Test Data Kit (TDK) masks, subsets, and generates data across databases including PostgreSQL, MySQL, Oracle, SQL Server, SAP HANA and Db2, and enterprise applications like SAP, Oracle Fusion, Workday, Microsoft D365, ServiceNow and Salesforce. The Governor External API and first-party Python SDK (published to PyPI) let teams trigger masking and generation workflows programmatically and embed compliant synthetic data into their pipelines, with policy-driven masking aligned to GDPR, CCPA and CPRA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/synthesized.png
layout: provider
mcp_servers:
- description: ''
  name: Synthesized MCP Server
  slug: synthesized-mcp-server
modified: '2026-07-21'
name: Synthesized
nav: Providers
network: true
overview: 'Synthesized publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Test Data, Synthetic Data, Data Masking, and Data Privacy.


  Synthesized''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 15 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 29.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Synthesized Authentication
  slug: synthesized-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Synthesized Domain Security
  slug: synthesized-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synthesized
tags:
- Company
- Test Data
- Synthetic Data
- Data Masking
- Data Privacy
- Test Data Management
- Compliance
- Machine-Learning
- Databases
- Developer Tools
website: https://www.synthesized.io
---
