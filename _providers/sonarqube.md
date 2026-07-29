---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: HTTP API for programmatic interaction with SonarQube Server, enabling management of projects, quality gates, issues, rules, users, and integrations with external tools.
  name: SonarQube Web API
  slug: web-api
artifact_total: 16
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sonarqube/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonarqube-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonarsource
- group: start
  title: ''
  type: Portal
  url: https://www.sonarsource.com/products/sonarqube/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonarsource.com/sonarqube-server/
- group: docs
  title: ''
  type: Reference
  url: https://api-docs.sonarsource.com/
- group: company
  title: ''
  type: Website
  url: https://www.sonarsource.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SonarSource
- group: company
  title: ''
  type: Blog
  url: https://www.sonarsource.com/blog/
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
  title: SonarQube Vocabulary
  type: Vocabulary
  url: vocabulary/sonarqube-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SonarSource/sonarqube-mcp-server
created: '2026-03-16'
description: SonarQube is a leading code quality and security platform that provides Web APIs for managing projects, quality gates, issues, and integrations with CI/CD pipelines to deliver clean, secure code.
examples:
- key_count: 1
  name: Sonarqube Component Measures Example
  slug: sonarqube-component-measures-example
- key_count: 1
  name: Sonarqube Quality Gate Status Example
  slug: sonarqube-quality-gate-status-example
- key_count: 3
  name: Sonarqube Search Issues Example
  slug: sonarqube-search-issues-example
finops:
- name: Sonarqube Finops
  service_category: API
  slug: sonarqube-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonarqube.png
json_schemas:
- name: Issue
  property_count: 21
  slug: sonarqube-issue
- name: Project
  property_count: 8
  slug: sonarqube-project
- name: QualityGate
  property_count: 5
  slug: sonarqube-quality-gate
json_structures:
- name: Sonarqube Web Api Structure
  property_count: 0
  slug: sonarqube-web-api-structure
jsonld:
- class_count: 0
  name: Sonarqube Context
  property_count: 7
  slug: sonarqube-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: SonarQube
nav: Providers
network: true
overview: 'SonarQube publishes 1 API on the [APIs.io](https://apis.io/) network: Web API. Tagged areas include Code Quality, DevOps, Security, and Static Analysis.


  The SonarQube catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SonarQube''s developer surface includes developer portal, documentation, engineering blog, support, pricing, and 11 more developer resources.'
plans:
- name: Sonarqube Plans Pricing
  plan_count: 3
  slug: sonarqube-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Sonarqube Rate Limits
  slug: sonarqube-rate-limits
rules:
- name: SonarQube API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sonarqube-jsonschema-spectral-rules
- name: SonarQube API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: sonarqube-rules
score:
  band: strong
  composite: 56.2
  delta: -5.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 56.5
    developer_ergonomics: 43.5
    discoverability: 40.7
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 61.3
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sonarqube/refs/heads/main/screenshots/sonarqube-2026-06-20T194159.png
security:
- kind: domain-security
  name: Sonarqube Domain Security
  slug: sonarqube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonarqube
tags:
- Code Quality
- DevOps
- Security
- Static Analysis
website: https://www.sonarsource.com/
---
