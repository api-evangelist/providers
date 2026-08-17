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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Security Command Center Agentic Access
  operation_count: 7
  slug: google-cloud-security-command-center-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: Operations for listing and managing cloud assets
  name: Google Cloud Security Command Center Assets API
  slug: google-cloud-security-command-center-assets-api
- description: Operations for managing security findings
  name: Google Cloud Security Command Center Findings API
  slug: google-cloud-security-command-center-findings-api
- description: Operations for managing notification configurations
  name: Google Cloud Security Command Center NotificationConfigs API
  slug: google-cloud-security-command-center-notificationconfigs-api
- description: Operations for managing security sources
  name: Google Cloud Security Command Center Sources API
  slug: google-cloud-security-command-center-sources-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud Security Command Center Assets API
  slug: postman-google-cloud-security-command-center-assets-api
- collection_type: postman
  name: Google Cloud Security Command Center Assets Findings API
  slug: postman-google-cloud-security-command-center-findings-api
- collection_type: postman
  name: Google Cloud Security Command Center Assets NotificationConfigs API
  slug: postman-google-cloud-security-command-center-notificationconfigs-api
- collection_type: postman
  name: Google Cloud Security Command Center Assets Sources API
  slug: postman-google-cloud-security-command-center-sources-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Security Command Center Assets API
  slug: open-google-cloud-security-command-center-assets-api
- collection_type: open
  name: Google Cloud Security Command Center Assets Findings API
  slug: open-google-cloud-security-command-center-findings-api
- collection_type: open
  name: Google Cloud Security Command Center Assets NotificationConfigs API
  slug: open-google-cloud-security-command-center-notificationconfigs-api
- collection_type: open
  name: Google Cloud Security Command Center Assets Sources API
  slug: open-google-cloud-security-command-center-sources-api
- collection_type: open
  name: Google Cloud Security Command Center API
  slug: open-security-command-center-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-security-command-center/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-security-command-center-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-security-command-center-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-security-command-center-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-security-command-center-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-security-command-center-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/security-command-center
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/security-command-center/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/security-command-center/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/security-command-center/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/security-command-center/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/security-command-center/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-security-command-center-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/scc-release-notes.xml
created: '2026-03-13'
description: Google Cloud Security Command Center (SCC) is a security and risk management platform for Google Cloud that helps organizations identify misconfigurations, vulnerabilities, and threats across their cloud assets. It provides centralized visibility into cloud resources, security findings, and compliance status, enabling security teams to detect, investigate, and respond to threats.
finops:
- name: Google Cloud Security Command Center Finops
  service_category: API
  slug: google-cloud-security-command-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-security-command-center.png
json_schemas:
- name: Google Cloud Security Command Center Finding
  property_count: 12
  slug: google-cloud-security-command-center-finding
jsonld:
- class_count: 0
  name: Google Cloud Security Command Center Context
  property_count: 4
  slug: google-cloud-security-command-center-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Security Command Center
nav: Providers
network: true
overview: 'Google Cloud Security Command Center publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Findings API, NotificationConfigs API, and 1 more. Tagged areas include Cloud Security, Compliance, Risk Management, Security, and Threat Detection.


  The Google Cloud Security Command Center catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Security Command Center''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Security Command Center Plans Pricing
  plan_count: 3
  slug: google-cloud-security-command-center-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Google Cloud Security Command Center Rate Limits
  slug: google-cloud-security-command-center-rate-limits
rules:
- name: Google Cloud Security Command Center API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-security-command-center-jsonschema-spectral-rules
scopes:
- name: Google Cloud Security Command Center Scopes
  scope_count: 1
  slug: google-cloud-security-command-center-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 68.7
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-security-command-center/refs/heads/main/screenshots/google-cloud-security-command-center-2026-06-20T182136.png
security:
- kind: authentication
  name: Google Cloud Security Command Center Authentication
  slug: google-cloud-security-command-center-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Security Command Center Domain Security
  slug: google-cloud-security-command-center-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Security Command Center Vulnerability Disclosure
  slug: google-cloud-security-command-center-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-security-command-center
tags:
- Cloud Security
- Compliance
- Risk Management
- Security
- Threat Detection
- Vulnerability Management
website: https://cloud.google.com/security-command-center
---
