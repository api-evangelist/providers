---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://granulate.io/'', ''status'': 301, ''note'': ''declared website redirects to https://www.intel.com/content/www/us/en/homepage.html — a different registrable domain (granulate.io -> intel.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/intel/gprofiler/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/intel/gprofiler/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/intel/gprofiler/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/intel/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/intel/gprofiler/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/intel/gprofiler/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/granulate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://granulate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/intel/gprofiler#readme
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/intel/gprofiler
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intel
- group: build
  title: ''
  type: Packages
  url: packages/granulate-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/granulate-cli.yml
created: '2026-07-17'
description: Granulate is a real-time continuous optimization company acquired by Intel in 2022 and now offered as Intel Tiber App-Level Optimization. Its platform autonomously tunes OS-level and runtime behavior (scheduling, memory, networking) for compute, Kubernetes, and big-data workloads to cut CPU cost and latency without code changes. Granulate also maintains gProfiler, an open-source, low-overhead, system-wide continuous profiler that combines multiple sampling profilers (perf, py-spy, async-profiler, rbspy, PHP/.NET/Node.js) into a single flamegraph and optionally uploads results to the Granulate Performance Studio. gProfiler ships as an Apache-2.0 agent (github.com/intel/gprofiler), a self-hosted backend/UI (github.com/intel/gprofiler-performance-studio), a Docker image, and cloud-marketplace images. The former granulate.io developer surface now redirects to intel.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/granulate.png
layout: provider
modified: '2026-07-19'
name: Granulate
nav: Providers
network: true
overview: 'Granulate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Performance, Continuous Profiling, and Observability.


  Granulate''s developer surface includes documentation, CLI, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 20.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/granulate/refs/heads/main/screenshots/granulate-2026-07-25T220247.png
security:
- kind: domain-security
  name: Granulate Domain Security
  slug: granulate-domain-security
  summary_line: TLSv1.3
slug: granulate
tags:
- Company
- DevOps
- Performance
- Continuous Profiling
- Observability
- Optimization
- Kubernetes
- Intel
website: https://granulate.io/
---
