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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Nomad Agentic Access
  operation_count: 79
  slug: nomad-agentic-access
  summary_line: 79 operations · 33 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The HashiCorp Nomad Go SDK is the official Go client library for interacting with the Nomad HTTP API. It provides a high-level, idiomatic Go interface for managing jobs, allocations, nodes, deployment
  name: HashiCorp Nomad Go SDK
  slug: go-sdk
- description: The python-nomad library is a Python client for the HashiCorp Nomad HTTP API. It provides Pythonic access to Nomad resources including jobs, nodes, allocations, deployments, evaluations, namespaces, a
  name: HashiCorp Nomad Python SDK
  slug: python-sdk
- description: The Nomad Java SDK is an official Java client library for the HashiCorp Nomad HTTP API. It enables Java and JVM-based applications to interact with Nomad clusters for submitting jobs, querying allocat
  name: HashiCorp Nomad Java SDK
  slug: java-sdk
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for managing Access Control List policies, tokens, and authentication methods.
  name: HashiCorp Nomad ACL API
  slug: nomad-acl-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for interacting with the local Nomad agent, including health checks, member listing, and server management.
  name: HashiCorp Nomad Agent API
  slug: nomad-agent-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying allocations. An allocation declares that a set of tasks in a job should be run on a particular node.
  name: HashiCorp Nomad Allocations API
  slug: nomad-allocations-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying and managing deployments. Deployments track the rolling update of allocations between two versions of a job.
  name: HashiCorp Nomad Deployments API
  slug: nomad-deployments-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying evaluations. Evaluations are the mechanism by which Nomad makes scheduling decisions.
  name: HashiCorp Nomad Evaluations API
  slug: nomad-evaluations-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for listing, creating, reading, updating, and deleting jobs. Jobs are the primary unit of work in Nomad.
  name: HashiCorp Nomad Jobs API
  slug: nomad-jobs-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for managing namespaces, which segment jobs and their associated objects.
  name: HashiCorp Nomad Namespaces API
  slug: nomad-namespaces-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for managing node pools, which group nodes for scheduling constraints.
  name: HashiCorp Nomad Node Pools API
  slug: nomad-node-pools-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying and managing client nodes registered with the Nomad cluster.
  name: HashiCorp Nomad Nodes API
  slug: nomad-nodes-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for cluster-level operations such as Raft peer management and autopilot configuration.
  name: HashiCorp Nomad Operator API
  slug: nomad-operator-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for listing known regions in the Nomad cluster.
  name: HashiCorp Nomad Regions API
  slug: nomad-regions-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying scaling policies and their status.
  name: HashiCorp Nomad Scaling API
  slug: nomad-scaling-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for searching across Nomad objects by prefix or fuzzy match.
  name: HashiCorp Nomad Search API
  slug: nomad-search-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: The Service API from HashiCorp Nomad — 1 operation(s) for service.
  name: HashiCorp Nomad Service API
  slug: nomad-service-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: The Services API from HashiCorp Nomad — 1 operation(s) for services.
  name: HashiCorp Nomad Services API
  slug: nomad-services-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for querying the status of the Nomad cluster including leader and peer information.
  name: HashiCorp Nomad Status API
  slug: nomad-status-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for system maintenance operations such as garbage collection and reconciliation.
  name: HashiCorp Nomad System API
  slug: nomad-system-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for managing Nomad variables, which store encrypted key-value data.
  name: HashiCorp Nomad Variables API
  slug: nomad-variables-api
- baseURL: http://localhost:4646
  baseurl_source: declared
  description: Endpoints for managing CSI and host volumes attached to Nomad allocations.
  name: HashiCorp Nomad Volumes API
  slug: nomad-volumes-api
artifact_total: 73
asyncapis:
- description: The Nomad Event Stream provides a way to subscribe to Job, Allocation, Evaluation, Deployment, Node, Node Pool, and Service changes in near real time. The /v1/event/stream endpoint streams events as n
  name: HashiCorp Nomad Event Stream
  slug: nomad-event-stream-asyncapi
collections:
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL API
  slug: postman-nomad-acl-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Agent API
  slug: postman-nomad-agent-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Allocations API
  slug: postman-nomad-allocations-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Deployments API
  slug: postman-nomad-deployments-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Evaluations API
  slug: postman-nomad-evaluations-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Jobs API
  slug: postman-nomad-jobs-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Namespaces API
  slug: postman-nomad-namespaces-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Node Pools API
  slug: postman-nomad-node-pools-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Nodes API
  slug: postman-nomad-nodes-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Operator API
  slug: postman-nomad-operator-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Regions API
  slug: postman-nomad-regions-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Scaling API
  slug: postman-nomad-scaling-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Search API
  slug: postman-nomad-search-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Service API
  slug: postman-nomad-service-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Services API
  slug: postman-nomad-services-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Status API
  slug: postman-nomad-status-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL System API
  slug: postman-nomad-system-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Variables API
  slug: postman-nomad-variables-api
- collection_type: postman
  name: HashiCorp Nomad HTTP ACL Volumes API
  slug: postman-nomad-volumes-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Nomad HTTP ACL API
  slug: open-nomad-acl-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Agent API
  slug: open-nomad-agent-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Allocations API
  slug: open-nomad-allocations-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Deployments API
  slug: open-nomad-deployments-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Evaluations API
  slug: open-nomad-evaluations-api
- collection_type: open
  name: HashiCorp Nomad HTTP API
  slug: open-nomad-http-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Jobs API
  slug: open-nomad-jobs-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Namespaces API
  slug: open-nomad-namespaces-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Node Pools API
  slug: open-nomad-node-pools-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Nodes API
  slug: open-nomad-nodes-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Operator API
  slug: open-nomad-operator-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Regions API
  slug: open-nomad-regions-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Scaling API
  slug: open-nomad-scaling-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Search API
  slug: open-nomad-search-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Service API
  slug: open-nomad-service-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Services API
  slug: open-nomad-services-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Status API
  slug: open-nomad-status-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL System API
  slug: open-nomad-system-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Variables API
  slug: open-nomad-variables-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Volumes API
  slug: open-nomad-volumes-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hashicorp-nomad/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nomad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nomad-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashicorp
- group: start
  title: ''
  type: Portal
  url: https://developer.hashicorp.com/nomad
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/nomad/docs
- group: company
  title: ''
  type: Website
  url: https://www.nomadproject.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hashicorp.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hashicorp.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.hashicorp.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog
- group: start
  title: ''
  type: Login
  url: https://portal.cloud.hashicorp.com/sign-in
- group: design
  title: ''
  type: JSONLD
  url: json-ld/nomad-context.jsonld
created: '2026-03-20'
description: HashiCorp Nomad is a flexible workload orchestrator that enables organizations to deploy and manage containers, legacy applications, and batch jobs across any infrastructure. The Nomad developer platform provides a comprehensive HTTP API, official SDKs, and tooling for automating job scheduling, cluster management, and service orchestration at scale.
finops:
- name: Nomad Finops
  service_category: Workload Orchestration
  slug: nomad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nomad.png
json_schemas:
- name: HashiCorp Nomad Job
  property_count: 20
  slug: nomad-job
jsonld:
- class_count: 0
  name: Nomad Context
  property_count: 13
  slug: nomad-context
layout: provider
modified: '2026-05-19'
name: HashiCorp Nomad
nav: Providers
network: true
overview: 'HashiCorp Nomad publishes 19 APIs on the [APIs.io](https://apis.io/) network, including ACL API, Agent API, Allocations API, and 16 more. Tagged areas include Workload Orchestration, Container Orchestration, Scheduling, Infrastructure, and DevOps.


  The HashiCorp Nomad catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  HashiCorp Nomad''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Nomad Plans Pricing
  plan_count: 3
  slug: nomad-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Nomad Rate Limits
  slug: nomad-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: HashiCorp Nomad API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: nomad-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: HashiCorp Nomad API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: nomad-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 68.4
    developer_ergonomics: 41.7
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomad/refs/heads/main/screenshots/nomad-2026-06-20T190354.png
security:
- kind: authentication
  name: Nomad Authentication
  slug: nomad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Nomad Domain Security
  slug: nomad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nomad
tags:
- Workload Orchestration
- Container Orchestration
- Scheduling
- Infrastructure
- DevOps
website: https://www.nomadproject.io/
---
