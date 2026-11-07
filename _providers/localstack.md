---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Localstack Agentic Access
  operation_count: 27
  slug: localstack-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 1
apis:
- baseURL: http://localhost.localstack.cloud:4566
  baseurl_source: declared
  description: The Aws API from LocalStack — 11 operation(s) for aws.
  name: LocalStack Aws API
  slug: localstack-aws-api
- baseURL: http://localhost.localstack.cloud:4566
  baseurl_source: declared
  description: The localstack API from LocalStack — 8 operation(s) for localstack.
  name: LocalStack API
  slug: localstack-localstack-api
artifact_total: 18
collections:
- collection_type: open
  name: LocalStack REST API for Community Aws API
  slug: open-localstack-aws-api
- collection_type: open
  name: REST API for Community Aws localstack API
  slug: open-localstack-localstack-api
common:
- group: commercial
  href: https://artifacts.apis.io/localstack/plans/localstack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/localstack-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.localstack.cloud/rss.xml
- group: other
  href: https://artifacts.apis.io/localstack/capabilities/localstack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/localstack-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/localstack/overlays/localstack-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/localstack/changelog/localstack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/localstack-changelog.yml
- group: build
  href: https://artifacts.apis.io/localstack/packages/localstack-packages.yml
  title: ''
  type: Packages
  url: packages/localstack-packages.yml
- group: build
  href: https://artifacts.apis.io/localstack/packages/localstack-packages.yml
  title: ''
  type: SDKs
  url: packages/localstack-packages.yml
- group: build
  href: https://artifacts.apis.io/localstack/cli/localstack-cli.yml
  title: ''
  type: CLI
  url: cli/localstack-cli.yml
- group: agent
  href: https://artifacts.apis.io/localstack/mcp/localstack-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/localstack-mcp.yml
- group: agent
  href: https://artifacts.apis.io/localstack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/localstack/well-known/localstack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/localstack-well-known.yml
- group: other
  href: https://artifacts.apis.io/localstack/well-known/localstack-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/localstack-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/localstack/llms/localstack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/localstack-llms.txt
- group: auth
  href: https://artifacts.apis.io/localstack/authentication/localstack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/localstack-authentication.yml
- group: design
  href: https://artifacts.apis.io/localstack/conventions/localstack-conventions.yml
  title: ''
  type: Conventions
  url: conventions/localstack-conventions.yml
- group: design
  href: https://artifacts.apis.io/localstack/errors/localstack-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/localstack-problem-types.yml
- group: design
  href: https://artifacts.apis.io/localstack/conformance/localstack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/localstack-conformance.yml
- group: design
  href: https://artifacts.apis.io/localstack/lifecycle/localstack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/localstack-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/localstack/data-model/localstack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/localstack-data-model.yml
- group: agent
  href: https://artifacts.apis.io/localstack/agentic-access/localstack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/localstack-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/localstack/security/localstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/localstack-domain-security.yml
created: '2026-07-17'
description: LocalStack is a cloud service emulator that runs in a single container on your laptop or in your CI environment, providing a local test and mocking framework for developing cloud applications against AWS, Snowflake, and Azure without provisioning real infrastructure. It ships a CLI, a Docker image, IaC integrations (Terraform, CDK, SAM, CloudFormation, Pulumi), an official MCP server and Agent Skills, and a local REST API for diagnostics, health checks, service introspection, and retrospective access to emulated AWS resources (SES, SNS, SQS, Lambda, DynamoDB, EventBridge, CloudWatch). Backed by GGV Capital.
finops:
- has_sources: true
  method: derived
  name: Localstack Finops
  primary_unit: license
  service_category: ''
  slug: localstack-finops
  template: false
image: https://github.com/localstack.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 11 tools listed.
  name: LocalStack MCP Server
  slug: io-github-localstack-localstack-mcp-server
modified: '2026-10-06'
name: LocalStack
nav: Providers
network: true
overview: 'LocalStack publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aws API, and 1 more. Tagged areas include Company, Developer Tools, Cloud, Amazon Web Services, and Emulator.


  The LocalStack catalog on APIs.io includes 1 Spectral governance ruleset.


  LocalStack''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Localstack Plans Pricing
  plan_count: 8
  slug: localstack-plans-pricing
- name: Localstack Price Estimates
  plan_count: 0
  slug: localstack-price-estimates
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: LocalStack API Rules
  rule_count: 45
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 3
  slug: localstack-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 38.3
    developer_ergonomics: 78.6
    discoverability: 63.3
    operational_transparency: 34.2
  previous_composite: 53.2
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/localstack/localstack-2026-07-25T225424.png
security:
- kind: authentication
  name: Localstack Authentication
  slug: localstack-authentication
  summary_line: none/auth-token · 2 schemes
- kind: domain-security
  name: Localstack Domain Security
  slug: localstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: localstack-extensions
  slug: localstack-extensions
- name: localstack-deploy
  slug: localstack-iac-deployment
- name: localstack-iam
  slug: localstack-iam-policy-analyzer
- name: localstack
  slug: localstack-lifecycle
- name: localstack-logs
  slug: localstack-logs-analysis
- name: localstack-state
  slug: localstack-state-management
slug: localstack
tags:
- Company
- Developer Tools
- Cloud
- Amazon Web Services
- Emulator
- Testing
- DevOps
- Serverless
- Infrastructure
website: https://www.localstack.cloud/
---
