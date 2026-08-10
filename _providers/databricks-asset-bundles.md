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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Databricks Asset Bundles API provides CLI-driven endpoints for initializing, validating, deploying, running, and destroying bundles of Databricks resources. Bundles define infrastructure and works
  name: Databricks Asset Bundles API
  slug: databricks-asset-bundles-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/databricks-asset-bundles-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/databricks-asset-bundles-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.databricks.com/aws/en/dev-tools/bundles
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/jobs-tutorial
- group: docs
  title: ''
  type: Documentation
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/settings
- group: docs
  title: ''
  type: Reference
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/reference
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/tutorials
- group: docs
  title: ''
  type: CLI Reference
  url: https://docs.databricks.com/aws/en/dev-tools/cli/bundle-commands
- group: auth
  title: ''
  type: Authentication
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/authentication
- group: other
  title: ''
  type: Resources
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/resources
- group: other
  title: ''
  type: Templates
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/templates
- group: build
  title: ''
  type: Configuration Examples
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/examples
- group: other
  title: ''
  type: Permissions
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/permissions
- group: other
  title: ''
  type: Variables
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/variables
- group: other
  title: ''
  type: Deployment Modes
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes
- group: build
  title: ''
  type: Library Dependencies
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/library-dependencies
- group: other
  title: ''
  type: Python Wheel
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/python-wheel
- group: other
  title: ''
  type: Python Configuration
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/python
- group: other
  title: ''
  type: CI/CD
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/ci-cd-bundles
- group: docs
  title: ''
  type: Migration Guide
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/migrate-resources
- group: operate
  title: ''
  type: FAQ
  url: https://docs.databricks.com/aws/en/dev-tools/bundles/faqs
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.databricks.com/aws/en/release-notes/dev-tools/bundles
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/databricks/cli
- group: build
  title: ''
  type: GitHub Examples
  url: https://github.com/databricks/bundle-examples
- group: build
  title: ''
  type: GitHub Action
  url: https://github.com/databricks/setup-cli
- group: commercial
  title: ''
  type: Pricing
  url: https://www.databricks.com/product/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.databricks.com/
- group: operate
  title: ''
  type: Support
  url: https://help.databricks.com/
- group: operate
  title: ''
  type: Community
  url: https://community.databricks.com/
- group: company
  title: ''
  type: Blog
  url: https://www.databricks.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.databricks.com/
- group: start
  title: ''
  type: Login
  url: https://login.databricks.com/
- group: start
  title: ''
  type: Signup
  url: https://www.databricks.com/try-databricks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.databricks.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.databricks.com/legal/privacynotice
- group: auth
  title: ''
  type: Security
  url: https://www.databricks.com/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/databricks
- group: learn
  title: ''
  type: Training
  url: https://www.databricks.com/learn/training/home
- group: operate
  title: ''
  type: Contact
  url: https://www.databricks.com/company/contact
- group: design
  title: ''
  type: JSONLD
  url: json-ld/databricks-asset-bundles-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/databricks-asset-bundles-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/databricks-asset-bundles-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.databricks.com/llms.txt
created: '2024-01-01'
description: Databricks Asset Bundles (DABs) provide an infrastructure-as-code approach to managing Databricks data and AI projects. Bundles enable version control, CI/CD, deployment, and management of Databricks resources such as jobs, pipelines, apps, schemas, experiments, and model serving endpoints across workspaces using the Databricks CLI.
finops:
- name: Databricks Asset Bundles Finops
  service_category: API
  slug: databricks-asset-bundles-finops
image: https://www.databricks.com/sites/default/files/2023-05/databricks-logo.png
json_schemas:
- name: Databricks Asset Bundle
  property_count: 14
  slug: bundle
jsonld:
- class_count: 0
  name: Databricks Asset Bundles Context
  property_count: 8
  slug: databricks-asset-bundles-context
layout: provider
modified: '2026-04-28'
name: Databricks Asset Bundles
nav: Providers
network: true
overview: 'Databricks Asset Bundles publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CI/CD, Data Engineering, Databricks, Deployment, and Infrastructure as Code.


  The Databricks Asset Bundles catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Databricks Asset Bundles'' developer surface includes developer portal, getting-started guide, documentation, authentication, FAQ, changelog, pricing, and 36 more developer resources.'
plans:
- name: Databricks Asset Bundles Plans Pricing
  plan_count: 3
  slug: databricks-asset-bundles-plans-pricing
random_paper: 111
rate_limits:
- limit_count: 5
  name: Databricks Asset Bundles Rate Limits
  slug: databricks-asset-bundles-rate-limits
rules:
- name: Databricks Asset Bundles API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: databricks-asset-bundles-jsonschema-spectral-rules
- name: Databricks Asset Bundles API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: databricks-asset-bundles-rules
score:
  band: strong
  composite: 57.1
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 17.7
    developer_ergonomics: 52.2
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 78.9
  previous_composite: 57.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/databricks-asset-bundles/refs/heads/main/screenshots/databricks-asset-bundles-2026-06-20T175631.png
security:
- kind: domain-security
  name: Databricks Asset Bundles Domain Security
  slug: databricks-asset-bundles-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Databricks Asset Bundles Vulnerability Disclosure
  slug: databricks-asset-bundles-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: databricks-asset-bundles
tags:
- CI/CD
- Data Engineering
- Databricks
- Deployment
- Infrastructure as Code
- Jobs
- Machine Learning
- MLOps
- Pipelines
- Workflows
website: https://www.databricks.com/
---
