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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sonar Agentic Access
  operation_count: 8
  slug: sonar-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 7
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
artifact_total: 23
collections:
- collection_type: open
  name: SonarCloud API
  slug: open-sonar-sonarcloud-api
common:
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


  Sonar''s developer surface includes authentication, engineering blog, support, pricing, and 11 more developer resources.'
plans:
- name: Sonar Plans Pricing
  plan_count: 3
  slug: sonar-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Sonar Rate Limits
  slug: sonar-rate-limits
rules:
- name: Sonar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sonar-jsonschema-spectral-rules
- name: Sonar API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: sonar-rules
score:
  band: strong
  composite: 63.8
  delta: 4.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 73.5
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 59.6
  schema_version: 0.5
  scored_at: '2026-07-27'
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
