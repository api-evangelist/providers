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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Tasks Agentic Access
  operation_count: 10
  slug: google-cloud-tasks-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Tasks — 5 operation(s) for projects.
  name: Google Cloud Tasks Projects API
  slug: google-cloud-tasks-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud Tasks Projects API
  slug: postman-google-cloud-tasks-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Tasks Projects API
  slug: open-google-cloud-tasks-projects-api
- collection_type: open
  name: Google Cloud Tasks API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-tasks/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-tasks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-tasks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-tasks-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/tasks
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/tasks/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/tasks/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/tasks/pricing
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
  url: https://cloud.google.com/tasks/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.json
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/cloud-tasks-release-notes.xml
created: '2026-03-13'
description: Google Cloud Tasks enables you to manage the execution of large numbers of distributed tasks. Cloud Tasks lets you create and dispatch tasks to worker services running on App Engine or any arbitrary HTTP endpoint, with automatic rate limiting, retry logic, and task deduplication. It provides a fully managed service for asynchronous task execution, allowing you to offload work from your main application and process it reliably in the background.
finops:
- name: Google Cloud Tasks Finops
  service_category: API
  slug: google-cloud-tasks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-tasks.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Tasks
nav: Providers
network: true
overview: 'Google Cloud Tasks publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Asynchronous, Background Jobs, Distributed Systems, Google Cloud, and Queues.


  The Google Cloud Tasks catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Tasks'' developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Tasks Plans Pricing
  plan_count: 3
  slug: google-cloud-tasks-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Google Cloud Tasks Rate Limits
  slug: google-cloud-tasks-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Tasks API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-tasks-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 55.8
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-tasks/refs/heads/main/screenshots/google-cloud-tasks-2026-06-20T182142.png
security:
- kind: domain-security
  name: Google Cloud Tasks Domain Security
  slug: google-cloud-tasks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Tasks Vulnerability Disclosure
  slug: google-cloud-tasks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-tasks
tags:
- Asynchronous
- Background Jobs
- Distributed Systems
- Google Cloud
- Queues
- Task
website: https://cloud.google.com/tasks
---
