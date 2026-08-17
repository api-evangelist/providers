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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Localstack Agentic Access
  operation_count: 27
  slug: localstack-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 2
apis:
- description: The Aws API from LocalStack — 11 operation(s) for aws.
  name: LocalStack Aws API
  slug: localstack-aws-api
- description: The localstack API from LocalStack — 8 operation(s) for localstack.
  name: LocalStack localstack API
  slug: localstack-localstack-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LocalStack REST API for Community Aws API
  slug: open-localstack-aws-api
- collection_type: open
  name: REST API for Community Aws localstack API
  slug: open-localstack-localstack-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/localstack-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.localstack.cloud/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.localstack.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.localstack.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.localstack.cloud/references/internal-endpoints/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.localstack.cloud/aws/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.localstack.cloud/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/localstack
- group: operate
  title: ''
  type: Support
  url: https://www.localstack.cloud/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.localstack.cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.localstack.cloud/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.localstack.cloud/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.localstack.cloud/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.localstack.cloud
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/localstack-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/localstack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/localstack-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/localstack-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/localstack-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/localstack-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/localstack-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/localstack-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/localstack-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/localstack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/localstack-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/localstack-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/localstack-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/localstack-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/localstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localstack-domain-security.yml
created: '2026-07-17'
description: LocalStack is a cloud service emulator that runs in a single container on your laptop or in your CI environment, providing a local test and mocking framework for developing cloud applications against AWS, Snowflake, and Azure without provisioning real infrastructure. It ships a CLI, a Docker image, IaC integrations (Terraform, CDK, SAM, CloudFormation, Pulumi), an official MCP server and Agent Skills, and a local REST API for diagnostics, health checks, service introspection, and retrospective access to emulated AWS resources (SES, SNS, SQS, Lambda, DynamoDB, EventBridge, CloudWatch). Backed by GGV Capital.
image: https://github.com/localstack.png
layout: provider
mcp_servers:
- description: ''
  name: localstack-mcp.yml
  slug: localstack-mcpyml
modified: '2026-07-20'
name: LocalStack
nav: Providers
network: true
overview: 'LocalStack publishes 2 APIs on the [APIs.io](https://apis.io/) network: Aws API and localstack API. Tagged areas include Company, Developer Tools, Cloud, Emulator, and Testing.


  LocalStack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 41.0
    developer_ergonomics: 80.4
    discoverability: 77.8
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/localstack/refs/heads/main/screenshots/localstack-2026-07-25T225424.png
security:
- kind: authentication
  name: Localstack Authentication
  slug: localstack-authentication
  summary_line: none/auth-token · 2 schemes
- kind: domain-security
  name: Localstack Domain Security
  slug: localstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: localstack
tags:
- Company
- Developer Tools
- Cloud
- Emulator
- Testing
- DevOps
- Serverless
- Infrastructure
website: https://www.localstack.cloud/
---
