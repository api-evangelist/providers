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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Systems Manager Agentic Access
  operation_count: 7
  slug: amazon-systems-manager-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 5
apis:
- description: Operations for managing automation executions.
  name: Amazon Systems Manager Automation API
  slug: amazon-systems-manager-automation-api
- description: Operations for managing SSM documents.
  name: Amazon Systems Manager Documents API
  slug: amazon-systems-manager-documents-api
- description: Operations for managing instance information.
  name: Amazon Systems Manager Managed Instances API
  slug: amazon-systems-manager-managed-instances-api
- description: Operations for managing parameters.
  name: Amazon Systems Manager Parameter Store API
  slug: amazon-systems-manager-parameter-store-api
- description: Operations for running commands on managed instances.
  name: Amazon Systems Manager Run Command API
  slug: amazon-systems-manager-run-command-api
artifact_total: 27
collections:
- collection_type: postman
  name: Amazon Systems Manager Automation API
  slug: postman-amazon-systems-manager-automation-api
- collection_type: postman
  name: Amazon Systems Manager Automation Documents API
  slug: postman-amazon-systems-manager-documents-api
- collection_type: postman
  name: Amazon Systems Manager Automation Managed Instances API
  slug: postman-amazon-systems-manager-managed-instances-api
- collection_type: postman
  name: Amazon Systems Manager Automation Parameter Store API
  slug: postman-amazon-systems-manager-parameter-store-api
- collection_type: postman
  name: Amazon Systems Manager Automation Run Command API
  slug: postman-amazon-systems-manager-run-command-api
- collection_type: open
  name: Amazon Systems Manager
  slug: open-amazon-systems-manager
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-systems-manager/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-systems-manager-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-systems-manager-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-systems-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-systems-manager-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/systems-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/systems-manager/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/systems-manager/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-systems-manager/refs/heads/main/rules/amazon-systems-manager-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-systems-manager/refs/heads/main/vocabulary/amazon-systems-manager-vocabulary.yaml
created: '2024-01-15'
description: AWS Systems Manager is an operational management service that provides a unified interface for managing AWS resources and on-premises infrastructure. It enables automation of operational tasks, configuration management, patch management, parameter storage, and run command execution across your hybrid cloud environment at scale.
examples:
- key_count: 2
  name: Amazon Systems Manager Example
  slug: amazon-systems-manager-example
features:
- description: Automate operational tasks with Amazon Systems Manager.
  name: Automation
- description: Programmatic access to Amazon Systems Manager resources.
  name: API Access
finops:
- name: Amazon Systems Manager Finops
  service_category: API
  slug: amazon-systems-manager-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Parameter
  property_count: 9
  slug: amazon-systems-manager-parameter
json_structures:
- name: Amazon Systems Manager Parameter Structure
  property_count: 0
  slug: amazon-systems-manager-parameter-structure
jsonld:
- class_count: 0
  name: Amazon Systems Manager Context
  property_count: 5
  slug: amazon-systems-manager-context
layout: provider
modified: '2026-05-19'
name: Amazon Systems Manager
nav: Providers
network: true
overview: 'Amazon Systems Manager publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Automation API, Documents API, Managed Instances API, and 2 more. Tagged areas include Automation, Management, and Operations.


  The Amazon Systems Manager catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Systems Manager''s developer surface includes developer portal, documentation, support, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Systems Manager Plans Pricing
  plan_count: 3
  slug: amazon-systems-manager-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 5
  name: Amazon Systems Manager Rate Limits
  slug: amazon-systems-manager-rate-limits
rules:
- name: Amazon Systems Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-systems-manager-jsonschema-spectral-rules
- name: Amazon Systems Manager API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 8
  slug: amazon-systems-manager-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 56.7
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-systems-manager/refs/heads/main/screenshots/amazon-systems-manager-2026-06-20T171837.png
security:
- kind: domain-security
  name: Amazon Systems Manager Domain Security
  slug: amazon-systems-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Systems Manager Vulnerability Disclosure
  slug: amazon-systems-manager-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Systems Manager Trust Center
  slug: amazon-systems-manager-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-systems-manager
tags:
- Automation
- Management
- Operations
use_cases:
- description: Use Amazon Systems Manager to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/systems-manager/
---
