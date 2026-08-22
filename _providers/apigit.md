---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apigit Agentic Access
  operation_count: 5
  slug: apigit-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 4
apis:
- description: Manage API definitions and designs.
  name: APIGit APIs API
  slug: apigit-apis-api
- description: Manage dynamic mock servers.
  name: APIGit Mocks API
  slug: apigit-mocks-api
- description: Manage API Git repositories.
  name: APIGit Repositories API
  slug: apigit-repositories-api
- description: Manage API tests.
  name: APIGit Tests API
  slug: apigit-tests-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIGit APIs API
  slug: open-apigit-apis-api
- collection_type: open
  name: APIGit APIs Mocks API
  slug: open-apigit-mocks-api
- collection_type: open
  name: APIGit APIs Repositories API
  slug: open-apigit-repositories-api
- collection_type: open
  name: APIGit APIs Tests API
  slug: open-apigit-tests-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apigit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apigit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apigit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apigit
- group: company
  title: ''
  type: Website
  url: https://apigit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apigit.com/doc
- group: commercial
  title: ''
  type: Pricing
  url: https://apigit.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://apigit.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apigitlabs
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@apigit
created: '2025-01-08'
description: APIGit is a Git-native platform for full lifecycle API development that combines version control, API design, documentation generation, governance, testing, and dynamic mock servers in a single integrated environment. Teams can build, publish, share, and secure APIs through Git-based workflows.
examples:
- key_count: 4
  name: Apigit Mock Server Example
  slug: apigit-mock-server-example
- key_count: 4
  name: Apigit Repository Example
  slug: apigit-repository-example
features:
- description: Version-controlled API repositories with Git-native workflows for teams.
  name: Native Git Repository
- description: Visual OpenAPI designer for designing APIs without writing YAML manually.
  name: API Design
- description: Automatic documentation generation and publishing with custom domains.
  name: API Documentation
- description: Policy management and compliance controls for API standards enforcement.
  name: API Governance
- description: Built-in automated API testing with test case management.
  name: API Testing
- description: Zero-configuration dynamic mock servers generated from API definitions.
  name: Dynamic Mock Server
finops:
- name: Apigit Finops
  service_category: API
  slug: apigit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apigit.png
integrations:
- description: Native OpenAPI specification support for API design and documentation.
  name: OpenAPI
- description: Native Git version control for all API definitions and changes.
  name: Git
json_schemas:
- name: MockServer
  property_count: 4
  slug: apigit-mock-server
- name: Repository
  property_count: 4
  slug: apigit-repository
json_structures:
- name: Apigit Mock Server Structure
  property_count: 4
  slug: apigit-mock-server-structure
- name: Apigit Repository Structure
  property_count: 4
  slug: apigit-repository-structure
jsonld:
- class_count: 4
  name: Apigit Context
  property_count: 3
  slug: apigit-context
layout: provider
modified: '2026-05-19'
name: APIGit
nav: Providers
network: true
overview: 'APIGit publishes 4 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Mocks API, Repositories API, and 1 more. Tagged areas include API Design, API Lifecycle, Documentation, Git, and Governance.


  The APIGit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  APIGit''s developer surface includes authentication, documentation, pricing, engineering blog, YouTube channel, and 5 more developer resources.'
plans:
- name: Apigit Plans Pricing
  plan_count: 3
  slug: apigit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Apigit Rate Limits
  slug: apigit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIGit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apigit-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: APIGit API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 11
  slug: apigit-spectral-rules
score:
  band: thin
  composite: 26.7
  delta: -5.8
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 25.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apigit/refs/heads/main/screenshots/apigit-2026-06-20T172238.png
security:
- kind: authentication
  name: Apigit Authentication
  slug: apigit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apigit Domain Security
  slug: apigit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apigit
solutions:
- description: 1 API repository, mock server, and document publication with up to 1,000 mock calls/month.
  name: Free Plan
- description: $8/user/month with 5 seats, 5 organizations, and 2,000 mock calls/month/seat.
  name: Team Plan
- description: $18/user/month with 20 organizations, custom domains, SSO, webhooks, and 4,000 mock calls/month/seat.
  name: Enterprise Plan
tags:
- API Design
- API Lifecycle
- Documentation
- Git
- Governance
- Mocking
- Platform
- Testing
use_cases:
- description: Design APIs visually before implementation using Git-tracked OpenAPI definitions.
  name: Design-First API Development
- description: Enable frontend teams to develop against mock servers while backends are being built.
  name: Parallel Frontend-Backend Development
- description: Enforce API standards and policies across teams with built-in governance tools.
  name: Team API Governance
website: https://apigit.com/
---
