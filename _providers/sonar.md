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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sonar Agentic Access
  operation_count: 8
  slug: sonar-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: REST API for interacting with SonarQube Server, enabling management of projects, quality gates, issues, rules, users, and CI/CD integrations. Uses token-based authentication.
  name: SonarQube Web API
  slug: sonarqube-web-api
- description: Code issue search and management
  name: Sonar Issues API
  slug: sonar-issues-api
- description: Component metrics and measurement data
  name: Sonar Measures API
  slug: sonar-measures-api
- description: Organization management and discovery
  name: Sonar Organizations API
  slug: sonar-organizations-api
- description: Project search and management within organizations
  name: Sonar Projects API
  slug: sonar-projects-api
- description: Quality gate configuration and status
  name: Sonar Quality Gates API
  slug: sonar-quality-gates-api
- description: API token generation and management
  name: Sonar User Tokens API
  slug: sonar-user-tokens-api
artifact_total: 36
collections:
- collection_type: postman
  name: SonarCloud Issues API
  slug: postman-sonar-issues-api
- collection_type: postman
  name: SonarCloud Issues Measures API
  slug: postman-sonar-measures-api
- collection_type: postman
  name: SonarCloud Issues Organizations API
  slug: postman-sonar-organizations-api
- collection_type: postman
  name: SonarCloud Issues Projects API
  slug: postman-sonar-projects-api
- collection_type: postman
  name: SonarCloud Issues Quality Gates API
  slug: postman-sonar-quality-gates-api
- collection_type: postman
  name: SonarCloud Issues User Tokens API
  slug: postman-sonar-user-tokens-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SonarCloud Issues API
  slug: open-sonar-issues-api
- collection_type: open
  name: SonarCloud Issues Measures API
  slug: open-sonar-measures-api
- collection_type: open
  name: SonarCloud Issues Organizations API
  slug: open-sonar-organizations-api
- collection_type: open
  name: SonarCloud Issues Projects API
  slug: open-sonar-projects-api
- collection_type: open
  name: SonarCloud Issues Quality Gates API
  slug: open-sonar-quality-gates-api
- collection_type: open
  name: SonarCloud API
  slug: open-sonar-sonarcloud-api
- collection_type: open
  name: SonarCloud Issues User Tokens API
  slug: open-sonar-user-tokens-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sonar/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sonar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonar-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonarsource
- group: company
  title: ''
  type: Website
  url: https://www.sonarsource.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sonarsource.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SonarSource
- group: operate
  title: ''
  type: Support
  url: https://community.sonarsource.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonarsource.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sonarsource.com/plans-and-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonarsource.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonarsource.com/privacy/
- group: design
  title: Sonar Vocabulary
  type: Vocabulary
  url: vocabulary/sonar-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SonarSource/sonarqube-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sonarsource.com/llms.txt
created: '2024-01-01'
description: Sonar (SonarSource) provides code quality and security analysis tools for developers. Products include SonarQube (self-hosted), SonarCloud (cloud-hosted), and SonarLint (IDE plugin), offering continuous inspection through static code analysis across 30+ programming languages.
examples:
- key_count: 1
  name: Sonar Quality Gate Status Example
  slug: sonar-quality-gate-status-example
- key_count: 2
  name: Sonar Search Organizations Example
  slug: sonar-search-organizations-example
finops:
- name: Sonar Finops
  service_category: API
  slug: sonar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonar.png
json_schemas:
- name: Issue
  property_count: 17
  slug: sonar-issue
- name: Organization
  property_count: 6
  slug: sonar-organization
json_structures:
- name: Sonar Sonarcloud Structure
  property_count: 0
  slug: sonar-sonarcloud-structure
jsonld:
- class_count: 0
  name: Sonar Context
  property_count: 5
  slug: sonar-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Sonar
nav: Providers
network: true
overview: 'Sonar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Issues API, Measures API, Organizations API, and 3 more. Tagged areas include CI/CD, Code Quality, DevOps, Security, and SonarCloud.


  The Sonar catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sonar''s developer surface includes authentication, engineering blog, support, pricing, and 12 more developer resources.'
plans:
- name: Sonar Plans Pricing
  plan_count: 3
  slug: sonar-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Sonar Rate Limits
  slug: sonar-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sonar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sonar-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: Sonar API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: sonar-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 70.7
    developer_ergonomics: 52.4
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 18.4
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sonar/refs/heads/main/screenshots/sonar-2026-06-20T194158.png
security:
- kind: authentication
  name: Sonar Authentication
  slug: sonar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sonar Domain Security
  slug: sonar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonar
tags:
- CI/CD
- Code Quality
- DevOps
- Security
- SonarCloud
- SonarQube
- Static Analysis
website: https://www.sonarsource.com/
---
