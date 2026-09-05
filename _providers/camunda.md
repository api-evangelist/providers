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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Camunda Agentic Access
  operation_count: 23
  slug: camunda-agentic-access
  summary_line: 23 operations · 19 acting
api_count: 1
apis:
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Cluster API from Camunda — 1 operation(s) for cluster.
  name: Camunda Cluster API
  slug: camunda-cluster-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Decisions API from Camunda — 2 operation(s) for decisions.
  name: Camunda Decisions API
  slug: camunda-decisions-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Deployments API from Camunda — 2 operation(s) for deployments.
  name: Camunda Deployments API
  slug: camunda-deployments-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Incidents API from Camunda — 2 operation(s) for incidents.
  name: Camunda Incidents API
  slug: camunda-incidents-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Jobs API from Camunda — 4 operation(s) for jobs.
  name: Camunda Jobs API
  slug: camunda-jobs-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Messages API from Camunda — 1 operation(s) for messages.
  name: Camunda Messages API
  slug: camunda-messages-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Process Definitions API from Camunda — 3 operation(s) for process definitions.
  name: Camunda Process Definitions API
  slug: camunda-process-definitions-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Process Instances API from Camunda — 3 operation(s) for process instances.
  name: Camunda Process Instances API
  slug: camunda-process-instances-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The Signals API from Camunda — 1 operation(s) for signals.
  name: Camunda Signals API
  slug: camunda-signals-api
- baseURL_template: '{baseUrl}/v2'
  baseurl_source: spec_template
  description: The User Tasks API from Camunda — 3 operation(s) for user tasks.
  name: Camunda User Tasks API
  slug: camunda-user-tasks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Camunda 8 REST API
  slug: open-camunda-8-api
- collection_type: open
  name: Camunda 8 REST Cluster API
  slug: open-camunda-cluster-api
- collection_type: open
  name: Camunda 8 REST Cluster Decisions API
  slug: open-camunda-decisions-api
- collection_type: open
  name: Camunda 8 REST Cluster Deployments API
  slug: open-camunda-deployments-api
- collection_type: open
  name: Camunda 8 REST Cluster Incidents API
  slug: open-camunda-incidents-api
- collection_type: open
  name: Camunda 8 REST Cluster Jobs API
  slug: open-camunda-jobs-api
- collection_type: open
  name: Camunda 8 REST Cluster Messages API
  slug: open-camunda-messages-api
- collection_type: open
  name: Camunda 8 REST Cluster Process Definitions API
  slug: open-camunda-process-definitions-api
- collection_type: open
  name: Camunda 8 REST Cluster Process Instances API
  slug: open-camunda-process-instances-api
- collection_type: open
  name: Camunda 8 REST Cluster Signals API
  slug: open-camunda-signals-api
- collection_type: open
  name: Camunda 8 REST Cluster User Tasks API
  slug: open-camunda-user-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camunda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/camunda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/camunda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camunda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camunda-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camunda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/camunda
- group: company
  title: ''
  type: Website
  url: https://camunda.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.camunda.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.camunda.io/docs/apis-tools/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.camunda.io/docs/guides/
- group: company
  title: ''
  type: Blog
  url: https://camunda.com/blog/
- group: operate
  title: ''
  type: Community
  url: https://forum.camunda.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://camunda.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://camunda.com/legal/terms/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.camunda.io/llms.txt
created: '2026-03-16'
description: Camunda is a process orchestration platform that enables organizations to design, automate, and improve business processes using BPMN (Business Process Model and Notation). Camunda provides a complete solution for workflow automation, decision automation, and process monitoring.
finops:
- name: Camunda Finops
  service_category: API
  slug: camunda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camunda.png
layout: provider
modified: '2026-05-19'
name: Camunda
nav: Providers
network: true
overview: 'Camunda publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Decisions API, Deployments API, and 7 more. Tagged areas include BPMN, Business Process Management, Process Automation, and Workflows.


  Camunda''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Camunda Plans Pricing
  plan_count: 3
  slug: camunda-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Camunda Rate Limits
  slug: camunda-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 47.6
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camunda/refs/heads/main/screenshots/camunda-2026-06-20T173920.png
security:
- kind: authentication
  name: Camunda Authentication
  slug: camunda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Camunda Domain Security
  slug: camunda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Camunda Vulnerability Disclosure
  slug: camunda-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Camunda Trust Center
  slug: camunda-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: camunda
tags:
- BPMN
- Business Process Management
- Process Automation
- Workflows
website: https://camunda.com/
---
