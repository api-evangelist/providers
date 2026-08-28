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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Assured Workloads Agentic Access
  operation_count: 6
  slug: google-cloud-assured-workloads-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: Operations for managing compliance violations
  name: Google Cloud Assured Workloads Violations API
  slug: google-cloud-assured-workloads-violations-api
- description: Operations for managing assured workloads
  name: Google Cloud Assured Workloads Workloads API
  slug: google-cloud-assured-workloads-workloads-api
artifact_total: 19
collections:
- collection_type: postman
  name: Google Cloud Assured Workloads Violations API
  slug: postman-google-cloud-assured-workloads-violations-api
- collection_type: postman
  name: Google Cloud Assured Violations Workloads API
  slug: postman-google-cloud-assured-workloads-workloads-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Assured Workloads API
  slug: open-assured-workloads-api
- collection_type: open
  name: Google Cloud Assured Workloads Violations API
  slug: open-google-cloud-assured-workloads-violations-api
- collection_type: open
  name: Google Cloud Assured Violations Workloads API
  slug: open-google-cloud-assured-workloads-workloads-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-assured-workloads/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-assured-workloads-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-assured-workloads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-assured-workloads-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-assured-workloads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-assured-workloads-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/assured-workloads
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/assured-workloads/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/assured-workloads/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/assured-workloads/docs/reference/rest#authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/assured-workloads/pricing
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
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/assured-workloads/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-assured-workloads-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/assuredworkloads-release-notes.xml
created: '2026-03-13'
description: Google Cloud Assured Workloads enables organizations to create and manage compliance-controlled environments on Google Cloud. It provides guardrails for regulatory compliance frameworks such as FedRAMP, HIPAA, CJIS, ITAR, and others by enforcing organizational policies, data residency requirements, and access controls on cloud resources within designated workload environments.
finops:
- name: Google Cloud Assured Workloads Finops
  service_category: API
  slug: google-cloud-assured-workloads-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-assured-workloads.png
json_schemas:
- name: Google Cloud Assured Workloads Workload
  property_count: 9
  slug: google-cloud-assured-workloads-workload
jsonld:
- class_count: 0
  name: Google Cloud Assured Workloads Context
  property_count: 2
  slug: google-cloud-assured-workloads-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Assured Workloads
nav: Providers
network: true
overview: 'Google Cloud Assured Workloads publishes 2 APIs on the [APIs.io](https://apis.io/) network: Violations API and Workloads API. Tagged areas include Compliance, Data Residency, FedRAMP, Governance, and HIPAA.


  The Google Cloud Assured Workloads catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Assured Workloads'' developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Assured Workloads Plans Pricing
  plan_count: 3
  slug: google-cloud-assured-workloads-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Google Cloud Assured Workloads Rate Limits
  slug: google-cloud-assured-workloads-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Assured Workloads API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-assured-workloads-jsonschema-spectral-rules
scopes:
- name: Google Cloud Assured Workloads Scopes
  scope_count: 1
  slug: google-cloud-assured-workloads-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-assured-workloads/refs/heads/main/screenshots/google-cloud-assured-workloads-2026-06-20T182042.png
security:
- kind: authentication
  name: Google Cloud Assured Workloads Authentication
  slug: google-cloud-assured-workloads-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Assured Workloads Domain Security
  slug: google-cloud-assured-workloads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Assured Workloads Vulnerability Disclosure
  slug: google-cloud-assured-workloads-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-assured-workloads
tags:
- Compliance
- Data Residency
- FedRAMP
- Governance
- HIPAA
- Regulatory
website: https://cloud.google.com/assured-workloads
---
