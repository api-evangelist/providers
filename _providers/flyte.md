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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Flyte Agentic Access
  operation_count: 45
  slug: flyte-agentic-access
  summary_line: 45 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Signed URL retrieval for execution data inputs and outputs.
  name: Flyte DataProxy API
  slug: flyte-dataproxy-api
- description: Workflow, node, and task execution events.
  name: Flyte Events API
  slug: flyte-events-api
- description: Workflow execution creation, listing, retrieval, and termination.
  name: Flyte Executions API
  slug: flyte-executions-api
- description: Launch plan registration, listing, retrieval, and activation.
  name: Flyte LaunchPlans API
  slug: flyte-launchplans-api
- description: Matchable attribute configuration at project, domain, and workflow levels.
  name: Flyte MatchableAttributes API
  slug: flyte-matchableattributes-api
- description: Named entity metadata for tasks, workflows, and launch plans.
  name: Flyte NamedEntities API
  slug: flyte-namedentities-api
- description: Node execution listing and retrieval.
  name: Flyte NodeExecutions API
  slug: flyte-nodeexecutions-api
- description: Project registration and listing.
  name: Flyte Projects API
  slug: flyte-projects-api
- description: Task execution listing and retrieval.
  name: Flyte TaskExecutions API
  slug: flyte-taskexecutions-api
- description: Task entity registration, listing, and retrieval.
  name: Flyte Tasks API
  slug: flyte-tasks-api
- description: Admin server version information.
  name: Flyte Version API
  slug: flyte-version-api
- description: Workflow entity registration, listing, and retrieval.
  name: Flyte Workflows API
  slug: flyte-workflows-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flyte Admin API
  slug: open-flyte-admin-api
- collection_type: open
  name: Flyte Admin DataProxy API
  slug: open-flyte-dataproxy-api
- collection_type: open
  name: Flyte Admin DataProxy Events API
  slug: open-flyte-events-api
- collection_type: open
  name: Flyte Admin DataProxy Executions API
  slug: open-flyte-executions-api
- collection_type: open
  name: Flyte Admin DataProxy LaunchPlans API
  slug: open-flyte-launchplans-api
- collection_type: open
  name: Flyte Admin DataProxy MatchableAttributes API
  slug: open-flyte-matchableattributes-api
- collection_type: open
  name: Flyte Admin DataProxy NamedEntities API
  slug: open-flyte-namedentities-api
- collection_type: open
  name: Flyte Admin DataProxy NodeExecutions API
  slug: open-flyte-nodeexecutions-api
- collection_type: open
  name: Flyte Admin DataProxy Projects API
  slug: open-flyte-projects-api
- collection_type: open
  name: Flyte Admin DataProxy TaskExecutions API
  slug: open-flyte-taskexecutions-api
- collection_type: open
  name: Flyte Admin DataProxy Tasks API
  slug: open-flyte-tasks-api
- collection_type: open
  name: Flyte Admin DataProxy Version API
  slug: open-flyte-version-api
- collection_type: open
  name: Flyte Admin DataProxy Workflows API
  slug: open-flyte-workflows-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/flyteorg/flyte/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/flyteorg/flyte/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/flyteorg/flyte/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/flyteorg/flyte/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flyte-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flyte-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/flyte-oss
- group: company
  title: ''
  type: Website
  url: https://flyte.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flyte.org
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/flyteorg/flyte
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flyteorg
- group: company
  title: ''
  type: Blog
  url: https://flyte.org/blog
- group: operate
  title: ''
  type: Community
  url: https://flyte.org/community
- group: operate
  title: ''
  type: Slack
  url: https://slack.flyte.org
created: '2026-03-27'
description: Flyte is a Kubernetes-native, open-source workflow orchestration platform for machine learning, data, and analytics pipelines. It provides reproducibility, type safety, strong versioning of tasks and workflows, and a multi-tenant control plane with native first-class scheduling on Kubernetes. Flyte is a Cloud Native Computing Foundation (CNCF) incubating project. Beyond the Python and Go SDKs, Flyte exposes a JSON-over-HTTP REST control-plane API (the Flyte Admin API) generated from the flyteidl protocol buffer definitions via gRPC-Gateway, which is used to register and manage projects, tasks, workflows, and launch plans, to create and inspect executions, to receive lifecycle events, and to read and write matchable attribute overrides.
finops:
- name: Flyte Finops
  service_category: API
  slug: flyte-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flyte.png
layout: provider
modified: '2026-05-19'
name: Flyte
nav: Providers
network: true
overview: 'Flyte publishes 12 APIs on the [APIs.io](https://apis.io/) network, including DataProxy API, Events API, Executions API, and 9 more. Tagged areas include CNCF, Data Orchestration, Kubernetes, Machine-Learning, and Workflow-Automation.


  Flyte''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Flyte Plans Pricing
  plan_count: 3
  slug: flyte-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Flyte Rate Limits
  slug: flyte-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 40.1
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flyte/refs/heads/main/screenshots/flyte-2026-06-20T181349.png
security:
- kind: domain-security
  name: Flyte Domain Security
  slug: flyte-domain-security
  summary_line: TLSv1.3 · HSTS
slug: flyte
tags:
- CNCF
- Data Orchestration
- Kubernetes
- Machine-Learning
- Workflow-Automation
website: https://flyte.org
---
