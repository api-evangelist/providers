---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Orkes Agentic Access
  operation_count: 35
  slug: orkes-agentic-access
  summary_line: 35 operations · 22 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Authentication API from Orkes — 1 operation(s) for authentication.
  name: Orkes Authentication API
  slug: orkes-authentication-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Human Tasks API from Orkes — 5 operation(s) for human tasks.
  name: Orkes Human Tasks API
  slug: orkes-human-tasks-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Schedules API from Orkes — 4 operation(s) for schedules.
  name: Orkes Schedules API
  slug: orkes-schedules-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Secrets API from Orkes — 2 operation(s) for secrets.
  name: Orkes Secrets API
  slug: orkes-secrets-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Task Metadata API from Orkes — 2 operation(s) for task metadata.
  name: Orkes Task Metadata API
  slug: orkes-task-metadata-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Tasks API from Orkes — 2 operation(s) for tasks.
  name: Orkes Tasks API
  slug: orkes-tasks-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Workflow Execution API from Orkes — 7 operation(s) for workflow execution.
  name: Orkes Workflow Execution API
  slug: orkes-workflow-execution-api
- baseURL_template: '{baseUrl}/api'
  baseurl_source: spec_template
  description: The Workflow Metadata API from Orkes — 2 operation(s) for workflow metadata.
  name: Orkes Workflow Metadata API
  slug: orkes-workflow-metadata-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orkes Conductor REST Authentication API
  slug: open-orkes-authentication-api
- collection_type: open
  name: Orkes Conductor REST API
  slug: open-orkes-conductor-api
- collection_type: open
  name: Orkes Conductor REST Authentication Human Tasks API
  slug: open-orkes-human-tasks-api
- collection_type: open
  name: Orkes Conductor REST Authentication Schedules API
  slug: open-orkes-schedules-api
- collection_type: open
  name: Orkes Conductor REST Authentication Secrets API
  slug: open-orkes-secrets-api
- collection_type: open
  name: Orkes Conductor REST Authentication Task Metadata API
  slug: open-orkes-task-metadata-api
- collection_type: open
  name: Orkes Conductor REST Authentication Tasks API
  slug: open-orkes-tasks-api
- collection_type: open
  name: Orkes Conductor REST Authentication Workflow Execution API
  slug: open-orkes-workflow-execution-api
- collection_type: open
  name: Orkes Conductor REST Authentication Workflow Metadata API
  slug: open-orkes-workflow-metadata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orkes-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orkes-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orkes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orkes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orkes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orkes-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orkes-inc
- group: company
  title: ''
  type: Website
  url: https://orkes.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://orkes.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://orkes.io/blog
created: '2026-03-26'
description: Orkes is a modern workflow orchestration platform built on Netflix Conductor for orchestrating microservices, AI agents, and durable workflows.
finops:
- name: Orkes Finops
  service_category: API
  slug: orkes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orkes.png
layout: provider
modified: '2026-05-19'
name: Orkes
nav: Providers
network: true
overview: 'Orkes publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Human Tasks API, Schedules API, and 5 more. Tagged areas include Microservices.


  Orkes'' developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Orkes Plans Pricing
  plan_count: 3
  slug: orkes-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Orkes Rate Limits
  slug: orkes-rate-limits
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.7
    developer_ergonomics: 14.3
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orkes/refs/heads/main/screenshots/orkes-2026-06-20T191209.png
security:
- kind: authentication
  name: Orkes Authentication
  slug: orkes-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orkes Domain Security
  slug: orkes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orkes Vulnerability Disclosure
  slug: orkes-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Orkes Trust Center
  slug: orkes-trust-center
  summary_line: SOC 2
slug: orkes
tags:
- Microservices
website: https://orkes.io/
---
