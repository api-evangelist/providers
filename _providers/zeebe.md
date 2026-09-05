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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Zeebe Agentic Access
  operation_count: 16
  slug: zeebe-agentic-access
  summary_line: 16 operations · 15 acting
api_count: 1
apis:
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Cluster API from Zeebe — 1 operation(s) for cluster.
  name: Zeebe Cluster API
  slug: zeebe-cluster-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Deployments API from Zeebe — 1 operation(s) for deployments.
  name: Zeebe Deployments API
  slug: zeebe-deployments-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Incidents API from Zeebe — 1 operation(s) for incidents.
  name: Zeebe Incidents API
  slug: zeebe-incidents-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Jobs API from Zeebe — 5 operation(s) for jobs.
  name: Zeebe Jobs API
  slug: zeebe-jobs-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Messages API from Zeebe — 1 operation(s) for messages.
  name: Zeebe Messages API
  slug: zeebe-messages-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Process Instances API from Zeebe — 3 operation(s) for process instances.
  name: Zeebe Process Instances API
  slug: zeebe-process-instances-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Resources API from Zeebe — 1 operation(s) for resources.
  name: Zeebe Resources API
  slug: zeebe-resources-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The Signals API from Zeebe — 1 operation(s) for signals.
  name: Zeebe Signals API
  slug: zeebe-signals-api
- baseURL: https://{region}.zeebe.camunda.io:443/{clusterId}/v2
  baseurl_source: declared
  description: The User Tasks API from Zeebe — 2 operation(s) for user tasks.
  name: Zeebe User Tasks API
  slug: zeebe-user-tasks-api
artifact_total: 66
collections:
- collection_type: postman
  name: Zeebe REST Cluster API
  slug: postman-zeebe-cluster-api
- collection_type: postman
  name: Zeebe REST Cluster Deployments API
  slug: postman-zeebe-deployments-api
- collection_type: postman
  name: Zeebe REST Cluster Incidents API
  slug: postman-zeebe-incidents-api
- collection_type: postman
  name: Zeebe REST Cluster Jobs API
  slug: postman-zeebe-jobs-api
- collection_type: postman
  name: Zeebe REST Cluster Messages API
  slug: postman-zeebe-messages-api
- collection_type: postman
  name: Zeebe REST Cluster Process Instances API
  slug: postman-zeebe-process-instances-api
- collection_type: postman
  name: Zeebe REST Cluster Resources API
  slug: postman-zeebe-resources-api
- collection_type: postman
  name: Zeebe REST Cluster Signals API
  slug: postman-zeebe-signals-api
- collection_type: postman
  name: Zeebe REST Cluster User Tasks API
  slug: postman-zeebe-user-tasks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zeebe REST API
  slug: open-zeebe-api
- collection_type: open
  name: Zeebe REST Cluster API
  slug: open-zeebe-cluster-api
- collection_type: open
  name: Zeebe REST Cluster Deployments API
  slug: open-zeebe-deployments-api
- collection_type: open
  name: Zeebe REST Cluster Incidents API
  slug: open-zeebe-incidents-api
- collection_type: open
  name: Zeebe REST Cluster Jobs API
  slug: open-zeebe-jobs-api
- collection_type: open
  name: Zeebe REST Cluster Messages API
  slug: open-zeebe-messages-api
- collection_type: open
  name: Zeebe REST Cluster Process Instances API
  slug: open-zeebe-process-instances-api
- collection_type: open
  name: Zeebe REST Cluster Resources API
  slug: open-zeebe-resources-api
- collection_type: open
  name: Zeebe REST Cluster Signals API
  slug: open-zeebe-signals-api
- collection_type: open
  name: Zeebe REST Cluster User Tasks API
  slug: open-zeebe-user-tasks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zeebe/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zeebe-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zeebe-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zeebe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeebe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeebe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://camunda.com/platform/zeebe/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.camunda.io/docs/components/zeebe/zeebe-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.camunda.io/docs/apis-tools/zeebe-api-rest/zeebe-api-rest-overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.camunda.io/docs/guides/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/camunda/camunda
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/camunda
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/camunda-community-hub
- group: commercial
  title: ''
  type: Pricing
  url: https://camunda.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://camunda.com/blog/
- group: operate
  title: ''
  type: Issues
  url: https://github.com/camunda/camunda/issues
- group: build
  title: ''
  type: SDKs
  url: https://github.com/camunda/camunda-bpm-spring-boot-starter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/camunda-community-hub/zeebe-client-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/camunda-community-hub/micronaut-zeebe-client
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/camunda/camunda/releases
- group: operate
  title: ''
  type: Forums
  url: https://forum.camunda.io/
created: '2026-03-26'
description: Zeebe is the cloud-native workflow engine that powers Camunda 8, providing scalable, resilient workflow automation and microservices orchestration without relying on a central database, enabling high throughput with horizontal scaling. It implements BPMN 2.0 process execution and provides a REST API for process deployment, instance management, job handling, message correlation, and cluster topology queries.
examples:
- key_count: 2
  name: Zeebe Activatejobs Example
  slug: zeebe-activateJobs-example
- key_count: 6
  name: Zeebe Api Activate Jobs Request Example
  slug: zeebe-api-activate-jobs-request-example
- key_count: 5
  name: Zeebe Api Create Process Instance Request Example
  slug: zeebe-api-create-process-instance-request-example
- key_count: 3
  name: Zeebe Api Deployment Response Example
  slug: zeebe-api-deployment-response-example
- key_count: 13
  name: Zeebe Api Job Example
  slug: zeebe-api-job-example
- key_count: 5
  name: Zeebe Api Process Instance Example
  slug: zeebe-api-process-instance-example
- key_count: 6
  name: Zeebe Api Publish Message Request Example
  slug: zeebe-api-publish-message-request-example
- key_count: 5
  name: Zeebe Api Topology Response Example
  slug: zeebe-api-topology-response-example
- key_count: 2
  name: Zeebe Createprocessinstance Example
  slug: zeebe-createProcessInstance-example
- key_count: 2
  name: Zeebe Deployresources Example
  slug: zeebe-deployResources-example
- key_count: 2
  name: Zeebe Gettopology Example
  slug: zeebe-getTopology-example
- key_count: 2
  name: Zeebe Publishmessage Example
  slug: zeebe-publishMessage-example
finops:
- name: Zeebe Finops
  service_category: API
  slug: zeebe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeebe.png
json_schemas:
- name: ActivateJobsRequest
  property_count: 6
  slug: zeebe-api-activate-jobs-request
- name: CreateProcessInstanceRequest
  property_count: 5
  slug: zeebe-api-create-process-instance-request
- name: DeploymentResponse
  property_count: 3
  slug: zeebe-api-deployment-response
- name: Job
  property_count: 13
  slug: zeebe-api-job
- name: ProcessInstance
  property_count: 5
  slug: zeebe-api-process-instance
- name: PublishMessageRequest
  property_count: 6
  slug: zeebe-api-publish-message-request
- name: TopologyResponse
  property_count: 5
  slug: zeebe-api-topology-response
json_structures:
- name: Zeebe Api Activate Jobs Request Structure
  property_count: 6
  slug: zeebe-api-activate-jobs-request-structure
- name: Zeebe Api Create Process Instance Request Structure
  property_count: 5
  slug: zeebe-api-create-process-instance-request-structure
- name: Zeebe Api Deployment Response Structure
  property_count: 3
  slug: zeebe-api-deployment-response-structure
- name: Zeebe Api Job Structure
  property_count: 13
  slug: zeebe-api-job-structure
- name: Zeebe Api Process Instance Structure
  property_count: 5
  slug: zeebe-api-process-instance-structure
- name: Zeebe Api Publish Message Request Structure
  property_count: 6
  slug: zeebe-api-publish-message-request-structure
- name: Zeebe Api Topology Response Structure
  property_count: 5
  slug: zeebe-api-topology-response-structure
jsonld:
- class_count: 5
  name: Zeebe Api Context
  property_count: 27
  slug: zeebe-api-context
layout: provider
modified: '2026-05-19'
name: Zeebe
nav: Providers
network: true
overview: 'Zeebe publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Cluster API, Deployments API, Incidents API, and 6 more. Tagged areas include BPMN, Camunda, Cloud-Native, Distributed Systems, and Java.


  The Zeebe catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zeebe''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, pricing, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: Zeebe Plans Pricing
  plan_count: 3
  slug: zeebe-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Zeebe Rate Limits
  slug: zeebe-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zeebe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zeebe-jsonschema-spectral-rules
- effective_rule_count: 18
  extends: []
  name: Zeebe API Rules
  rule_count: 18
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 13
  slug: zeebe-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 68.0
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 28.9
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeebe/refs/heads/main/screenshots/zeebe-2026-06-20T201806.png
security:
- kind: authentication
  name: Zeebe Authentication
  slug: zeebe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zeebe Domain Security
  slug: zeebe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zeebe Vulnerability Disclosure
  slug: zeebe-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Zeebe Trust Center
  slug: zeebe-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, GDPR
slug: zeebe
tags:
- BPMN
- Camunda
- Cloud-Native
- Distributed Systems
- Java
- Microservices
- Process Automation
- Workflow Orchestration
website: https://camunda.com/platform/zeebe/
---
