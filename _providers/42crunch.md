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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: 42Crunch Agentic Access
  operation_count: 6
  slug: 42crunch-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 6
apis:
- description: 'The 42Crunch API Security Audit performs automated static analysis of API definitions (OpenAPI 2, 3.0, 3.1 and GraphQL), running over 200 checks across format validation, data definition quality, and '
  name: 42Crunch API Security Audit
  slug: 42crunch-api-security-audit
- description: 42Crunch API Scan performs dynamic API security testing (DAST) that evaluates runtime API behavior against its OpenAPI specification. It tests how well an API adheres to its contract and identifies vu
  name: 42Crunch API Scan
  slug: 42crunch-api-scan
- description: 42Crunch API Protection deploys an API-native micro firewall (API Firewall) that provides runtime defense against API attacks. The firewall is tailor-made for each API based on its OpenAPI specificati
  name: 42Crunch API Protection
  slug: 42crunch-api-protection
- description: Service health check
  name: 42Crunch Health API
  slug: 42crunch-health-api
- description: Manage API conformance scan jobs on Kubernetes
  name: 42Crunch Jobs API
  slug: 42crunch-jobs-api
- description: Access job execution logs
  name: 42Crunch Logs API
  slug: 42crunch-logs-api
artifact_total: 45
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/42crunch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/42crunch-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/42crunch
- group: company
  title: ''
  type: Website
  url: https://42crunch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.42crunch.com/latest/content/home.htm
- group: company
  title: ''
  type: Blog
  url: https://42crunch.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.42crunch.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://42crunch.com/pricing/
- group: learn
  title: ''
  type: Tutorials
  url: https://42crunch.com/tutorials/
- group: learn
  title: ''
  type: Webinars
  url: https://42crunch.com/webinars/
- group: company
  title: ''
  type: Partners
  url: https://42crunch.com/partners/
- group: start
  title: ''
  type: Login
  url: https://platform.42crunch.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/42Crunch
- group: operate
  title: ''
  type: IDESupport
  url: https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi
- group: operate
  title: ''
  type: IDESupport
  url: https://plugins.jetbrains.com/plugin/14837-openapi-swagger-editor
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/vscode-openapi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/api-security-audit-action
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/api-security-audit-action-freemium
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/api-security-scan-action-freemium
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/cicd-github-actions
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/scand-manager
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/42Crunch/resources
- group: design
  title: ''
  type: SpectralRules
  url: rules/42crunch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/42crunch-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/42crunch-scand-manager-context.jsonld
created: '2025-01-08'
description: 42Crunch is a leading API security company that specializes in protecting and securing APIs. They provide innovative solutions that help organizations safeguard their sensitive data and critical assets from potential cyber threats. With their comprehensive API security platform, 42Crunch offers a range of services such as API scanning, traffic monitoring, and runtime protection to ensure that APIs are secure and compliant with industry standards. Their platform covers the full API security lifecycle from design and audit through dynamic testing and runtime firewall protection.
examples:
- key_count: 1
  name: Scand Manager Error Example
  slug: scand-manager-error-example
- key_count: 0
  name: Scand Manager Job Name Example
  slug: scand-manager-job-name-example
- key_count: 5
  name: Scand Manager Job Spec Example
  slug: scand-manager-job-spec-example
- key_count: 1
  name: Scand Manager Job Status Example
  slug: scand-manager-job-status-example
- key_count: 1
  name: Scand Manager Jobs Example
  slug: scand-manager-jobs-example
features:
- description: Automated static analysis of OpenAPI and GraphQL definitions running over 200 security checks, scoring APIs 0-100 for vulnerability and compliance issues.
  name: API Security Audit
- description: Dynamic API Security Testing that evaluates runtime API behavior against its OpenAPI contract, identifying vulnerabilities that appear only at runtime.
  name: API Scan (DAST)
- description: API-native micro firewall that enforces OpenAPI contract compliance at runtime, blocking malformed requests, unauthorized access, and API attacks.
  name: API Firewall
- description: Identifies and catalogs APIs across environments to provide full visibility into the API attack surface.
  name: API Discovery
- description: GitHub Actions and other CI/CD pipeline integrations for automated security scanning in deployment workflows.
  name: CI/CD Integration
- description: Plugins for VS Code and IntelliJ/JetBrains IDEs that provide real-time OpenAPI editing, validation, and security feedback during API design.
  name: IDE Integration
- description: Enforces security best practices in OpenAPI specifications covering authentication, data validation, input/output schemas, and transport security.
  name: OpenAPI Contract Security
- description: Scand Manager provides a Kubernetes wrapper for running 42Crunch API Scan in containerized environments.
  name: Kubernetes Support
finops:
- name: 42Crunch Finops
  service_category: API Security
  slug: 42crunch-finops
graphqls:
- description: ''
  name: 42Crunch GraphQL API
  slug: 42crunch-graphql
image: /assets/icons/42crunch.png
json_schemas:
- name: Error
  property_count: 1
  slug: scand-manager-error
- name: JobName
  property_count: 0
  slug: scand-manager-job-name
- name: JobSpec
  property_count: 6
  slug: scand-manager-job-spec
- name: JobStatus
  property_count: 2
  slug: scand-manager-job-status
- name: Jobs
  property_count: 1
  slug: scand-manager-jobs
json_structures:
- name: Scand Manager Error Structure
  property_count: 1
  slug: scand-manager-error-structure
- name: Scand Manager Job Name Structure
  property_count: 0
  slug: scand-manager-job-name-structure
- name: Scand Manager Job Spec Structure
  property_count: 6
  slug: scand-manager-job-spec-structure
- name: Scand Manager Job Status Structure
  property_count: 2
  slug: scand-manager-job-status-structure
- name: Scand Manager Jobs Structure
  property_count: 1
  slug: scand-manager-jobs-structure
jsonld:
- class_count: 5
  name: 42Crunch Scand Manager Context
  property_count: 8
  slug: 42crunch-scand-manager-context
layout: provider
modified: '2026-05-19'
name: 42Crunch
nav: Providers
network: true
overview: '42Crunch publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, Jobs API, and Logs API. Tagged areas include API Security, Platform, Scanning, Security, and OpenAPI.


  The 42Crunch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  42Crunch''s developer surface includes documentation, engineering blog, support, pricing, and 21 more developer resources.'
plans:
- name: 42Crunch Plans Pricing
  plan_count: 4
  slug: 42crunch-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 3
  name: 42Crunch Rate Limits
  slug: 42crunch-rate-limits
rules:
- name: 42Crunch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: 42crunch-jsonschema-spectral-rules
- name: 42Crunch API Rules
  rule_count: 47
  severity_counts:
    error: 12
    hint: 0
    info: 11
    warn: 24
  slug: 42crunch-spectral-rules
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 27.7
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/42crunch/refs/heads/main/screenshots/42crunch-2026-06-20T162707.png
security:
- kind: domain-security
  name: 42Crunch Domain Security
  slug: 42crunch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 42crunch
tags:
- API Security
- Platform
- Scanning
- Security
- OpenAPI
- DevSecOps
use_cases:
- description: Embed automated API security scanning into CI/CD pipelines via GitHub Actions to catch vulnerabilities before they reach production.
  name: API Security Testing in CI/CD
- description: Audit OpenAPI definitions for security flaws, missing authentication, weak data validation, and schema gaps before API deployment.
  name: OpenAPI Specification Review
- description: Deploy the API Firewall in front of production APIs to enforce contract compliance and block attacks in real time.
  name: Runtime API Protection
- description: Provide development, security, and operations teams with shared visibility into API security posture throughout the API lifecycle.
  name: DevSecOps API Governance
- description: Systematically identify and remediate OWASP API Security Top 10 vulnerabilities in API definitions and runtime behavior.
  name: OWASP API Top 10 Compliance
- description: Address regulatory and compliance requirements for API security in banking, financial services, and insurance sectors.
  name: API Security for Financial Services
- description: Secure healthcare APIs handling sensitive patient data against unauthorized access and data exposure vulnerabilities.
  name: Healthcare API Security
website: https://42crunch.com/
---
