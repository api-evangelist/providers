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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The Score Specification (score.yaml) is a declarative, platform-agnostic workload definition format that captures containers, service ports, and resource dependencies in a single file. Reference CLI i
  name: Score Specification
  slug: score-specification
- description: score-compose is the reference Score implementation that translates Score YAML workload specifications into Docker Compose configuration files. It enables local development environments that mirror pr
  name: score-compose
  slug: score-compose
- description: score-k8s is the reference Score implementation that translates Score YAML workload specifications into Kubernetes manifests including Deployments, Services, ConfigMaps, and Secrets. It supports Kuber
  name: score-k8s
  slug: score-k8s
artifact_total: 10
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/score-spec/spec/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/score-spec/spec/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/score-spec/spec/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/score-spec/spec/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/score-spec/spec/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/score-spec/spec/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/score-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://score.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/score-spec
- group: docs
  title: ''
  type: Documentation
  url: https://docs.score.dev/
- group: operate
  title: ''
  type: Slack Channel
  url: https://cloud-native.slack.com/archives/C07DN0D1UCW
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/json-ld/score-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/vocabulary/score-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://score.dev/index.xml
created: '2026-05-02'
description: Score is an open-source, platform-agnostic workload specification developed under the Cloud Native Computing Foundation (CNCF) Sandbox program. It provides a developer-centric YAML specification that enables teams to define application workloads once and deploy them across multiple container platforms including Docker Compose, Kubernetes, and cloud runtimes without environment-specific configuration drift. The score-spec organization provides reference CLI implementations (score-compose and score-k8s) that translate Score YAML into platform-specific manifests, eliminating YAML bloat and reducing cognitive load for platform engineering teams.
examples:
- key_count: 6
  name: Score Basic Workload Example
  slug: score-basic-workload-example
- key_count: 4
  name: Score Compose Output Example
  slug: score-compose-output-example
finops:
- name: Score Finops
  service_category: API
  slug: score-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/score.png
jsonld:
- class_count: 44
  name: Score Context
  property_count: 1
  slug: score-context
layout: provider
modified: '2026-05-02'
name: Score
nav: Providers
network: true
overview: 'Score publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Platform Engineering, Cloud-Native, CNCF, Workload Specification, and Kubernetes.


  The Score catalog on APIs.io includes 1 JSON-LD context.


  Score''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Score Plans Pricing
  plan_count: 3
  slug: score-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Score Rate Limits
  slug: score-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 29.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/score/refs/heads/main/screenshots/score-2026-06-20T193541.png
security:
- kind: domain-security
  name: Score Domain Security
  slug: score-domain-security
  summary_line: TLSv1.3
slug: score
tags:
- Platform Engineering
- Cloud-Native
- CNCF
- Workload Specification
- Kubernetes
- Docker
- Developer Experience
- Open-Source
website: https://score.dev/
---
