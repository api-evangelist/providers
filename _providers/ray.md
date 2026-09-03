---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Ray Agentic Access
  operation_count: 6
  slug: ray-agentic-access
  summary_line: 6 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API on the Ray head node for submitting, listing, inspecting, and stopping Ray jobs, plus streaming logs. Default base URL is http://<head-node>:8265/api/jobs/. Open-source clusters are typically
  name: Ray Jobs REST API
  slug: jobs-api
- description: Internal REST API powering the Ray Dashboard, exposing endpoints for nodes, actors, tasks, placement groups, runtime environments, and cluster events. Same base URL as the Jobs API (http://<head>:8265
  name: Ray Dashboard API
  slug: dashboard-api
- description: HTTP interface for invoking models and applications deployed via Ray Serve. Each deployed application is exposed as an HTTP endpoint on the Serve HTTP proxy (default port 8000); authentication and rou
  name: Ray Serve HTTP API
  slug: serve-api
- baseURL: http://127.0.0.1:8265/api
  baseurl_source: declared
  description: The Jobs API from Ray — 4 operation(s) for jobs.
  name: Ray Jobs API
  slug: ray-jobs-api
- baseURL: http://127.0.0.1:8265/api
  baseurl_source: declared
  description: The Version API from Ray — 1 operation(s) for version.
  name: Ray Version API
  slug: ray-version-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ray REST Jobs API
  slug: open-ray-jobs-api
- collection_type: open
  name: Ray REST Jobs Version API
  slug: open-ray-version-api
- collection_type: open
  name: Ray Jobs REST API
  slug: open-ray
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ray-project/ray/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ray-project/ray/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ray-project/ray/blob/master/CONTRIBUTING.rst
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ray-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ray-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ray.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ray.io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ray-project/ray
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ray-project
- group: other
  title: ''
  type: Anyscale
  url: https://www.anyscale.com
- group: operate
  title: ''
  type: Slack
  url: https://www.ray.io/community
- group: operate
  title: ''
  type: Forums
  url: https://discuss.ray.io
- group: company
  title: ''
  type: Blog
  url: https://www.anyscale.com/blog
- group: operate
  title: ''
  type: Issues
  url: https://github.com/ray-project/ray/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/ray-project/ray/blob/master/LICENSE
created: '2026-05-11'
description: Ray is an open-source unified compute framework, stewarded by Anyscale, that scales Python and AI workloads from a laptop to a cluster. It consists of Ray Core (a distributed runtime) and a set of AI libraries (Ray Train, Ray Data, Ray Tune, Ray Serve, RLlib) for training, batch inference, hyperparameter search, and model serving. Ray clusters expose a Dashboard and Jobs REST API on the head node (default port 8265) for submitting jobs, inspecting actors and tasks, and serving deployed applications via Ray Serve HTTP endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ray.png
layout: provider
modified: '2026-05-11'
name: Ray
nav: Providers
network: true
overview: 'Ray publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and Version API. Tagged areas include Distributed Computing, Machine-Learning, AI Infrastructure, Python, and Model Serving.


  Ray''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -5.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 42.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ray/refs/heads/main/screenshots/ray-2026-06-20T192611.png
security:
- kind: domain-security
  name: Ray Domain Security
  slug: ray-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ray
tags:
- Distributed Computing
- Machine-Learning
- AI Infrastructure
- Python
- Model Serving
- Open-Source
- Compute
website: https://www.ray.io
---
