---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 21
apis:
- description: 'tekton.dev/v1 kind=Task — defines a series of steps that launch specific build or delivery tools, ingest specific inputs (params, workspaces, resources), and produce specific outputs (results). Tasks '
  name: Tekton Task CRD
  slug: tekton-task-crd
- description: tekton.dev/v1 kind=TaskRun — instantiates a Task with specific inputs, workspace bindings, and execution parameters. The TaskRun controller runs the steps as Kubernetes pods and surfaces status, logs,
  name: Tekton TaskRun CRD
  slug: tekton-taskrun-crd
- description: tekton.dev/v1 kind=Pipeline — defines an ordered/parallelized series of Tasks that accomplish a specific build or delivery goal. Pipelines compose Tasks via params, workspaces, results, and finally ta
  name: Tekton Pipeline CRD
  slug: tekton-pipeline-crd
- description: tekton.dev/v1 kind=PipelineRun — instantiates a Pipeline with specific param values, workspace bindings, service accounts, and timeouts. The PipelineRun controller orchestrates the underlying TaskRuns
  name: Tekton PipelineRun CRD
  slug: tekton-pipelinerun-crd
- description: tekton.dev/v1beta1 kind=ClusterTask — cluster-scoped variant of Task, allowing a single definition to be referenced from any namespace. Marked deprecated in favor of remote resolution but still widely
  name: Tekton ClusterTask CRD
  slug: tekton-clustertask-crd
- description: tekton.dev/v1beta1 kind=StepAction — reusable, parameterizable step definition that can be referenced from multiple Tasks, enabling tighter sharing than copy-pasting step blocks.
  name: Tekton StepAction CRD
  slug: tekton-stepaction-crd
- description: tekton.dev/v1beta1 kind=CustomRun — generic execution resource that custom controllers reconcile, enabling third-party orchestrators to extend Tekton with non-Pod-based execution semantics.
  name: Tekton CustomRun CRD
  slug: tekton-customrun-crd
- description: The Tekton Resolution API (tekton.dev/v1alpha1 kind=ResolutionRequest) and built-in resolvers (Git, Hub, Bundles, Cluster, HTTP) fetch Tasks and Pipelines from remote sources at run time, so PipelineR
  name: Tekton Resolver Framework
  slug: tekton-resolver-api
- description: triggers.tekton.dev/v1beta1 kind=EventListener — runs an HTTP server (Sink) that receives webhooks (e.g., GitHub push events), applies interceptors, and creates Pipeline/TaskRun objects via TriggerTem
  name: Tekton EventListener CRD
  slug: tekton-eventlistener-crd
- description: triggers.tekton.dev/v1beta1 kind=Trigger — combines TriggerBindings (extracting fields from incoming events) and a TriggerTemplate (instantiating PipelineRuns/TaskRuns) used by EventListeners.
  name: Tekton Trigger CRD
  slug: tekton-trigger-crd
- description: triggers.tekton.dev/v1beta1 kind=TriggerBinding (and ClusterTriggerBinding) — extracts fields from event payloads and binds them to params used by TriggerTemplates.
  name: Tekton TriggerBinding CRD
  slug: tekton-triggerbinding-crd
- description: triggers.tekton.dev/v1beta1 kind=TriggerTemplate — declares the PipelineRun/TaskRun resources that should be instantiated when a matching event is received, parameterized by TriggerBindings.
  name: Tekton TriggerTemplate CRD
  slug: tekton-triggertemplate-crd
- description: triggers.tekton.dev/v1alpha1 kind=ClusterInterceptor (and namespace-scoped Interceptor) — pluggable webhook handler that filters, validates, and mutates incoming events before they reach a TriggerTemp
  name: Tekton ClusterInterceptor CRD
  slug: tekton-clusterinterceptor-crd
- description: Tekton Results provides a long-term store and a gRPC + REST API for completed PipelineRun/TaskRun records and their logs, freeing the Kubernetes etcd from acting as a CI history database.
  name: Tekton Results API
  slug: tekton-results-api
- description: Tekton Chains observes completed TaskRuns/PipelineRuns and emits signed in-toto/SLSA provenance attestations to OCI registries, transparency logs (Rekor), or storage backends — supplying the supply-ch
  name: Tekton Chains
  slug: tekton-chains-api
- description: Pipelines as Code lets you store Tekton Pipeline definitions inside the same Git repository as your application code (.tekton/) and runs them on PR/push events from GitHub/GitLab/Bitbucket/Gitea, prov
  name: Tekton Pipelines as Code
  slug: tekton-pipelines-as-code
- description: The Tekton Dashboard exposes a web UI and a thin proxy/HTTP API over the Tekton CRDs and Tekton Results, providing browsing, log streaming, and run management capabilities.
  name: Tekton Dashboard API
  slug: tekton-dashboard-api
- description: tkn is the official Tekton command-line tool wrapping the Kubernetes API for Tekton resources — start runs, stream logs, list/describe Tasks and Pipelines, manage triggers, and bootstrap projects.
  name: Tekton CLI (tkn)
  slug: tekton-cli-tkn
- description: operator.tekton.dev kinds (TektonConfig, TektonPipeline, TektonTrigger, TektonChain, TektonHub, TektonAddon, TektonDashboard, TektonResult) — the Tekton Operator installs and lifecycle-manages all Tek
  name: Tekton Operator CRDs
  slug: tekton-operator-crd
- description: Tekton Hub is a public catalog of reusable Tasks and Pipelines exposed via REST API — search, fetch, and resolve community-published resources for use via the Hub resolver.
  name: Tekton Hub API
  slug: tekton-hub-api
- description: The Tekton Catalog hosts community-curated, versioned Task and Pipeline definitions consumed via the Hub or directly by the Git resolver.
  name: Tekton Catalog
  slug: tekton-catalog-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tekton
  slug: open-tekton-pipeline
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tekton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tekton.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://tekton.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tekton.dev/docs/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tektoncd
- group: other
  title: ''
  type: Source
  url: https://github.com/tektoncd/pipeline
- group: other
  title: ''
  type: Triggers
  url: https://github.com/tektoncd/triggers
- group: other
  title: ''
  type: Chains
  url: https://github.com/tektoncd/chains
- group: other
  title: ''
  type: Results
  url: https://github.com/tektoncd/results
- group: other
  title: ''
  type: Operator
  url: https://github.com/tektoncd/operator
- group: build
  title: ''
  type: CLI
  url: https://github.com/tektoncd/cli
- group: other
  title: ''
  type: Dashboard
  url: https://github.com/tektoncd/dashboard
- group: other
  title: ''
  type: Catalog
  url: https://github.com/tektoncd/catalog
- group: other
  title: ''
  type: Hub
  url: https://hub.tekton.dev/
- group: commercial
  title: ''
  type: License
  url: https://github.com/tektoncd/pipeline/blob/main/LICENSE
- group: other
  title: ''
  type: CNCF Project
  url: https://www.cncf.io/projects/tekton/
- group: operate
  title: ''
  type: Slack Community
  url: https://tektoncd.slack.com/
- group: company
  title: ''
  type: Blog
  url: https://tekton.dev/blog/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/tektoncd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/TektonCD
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/tektoncd/pipeline/releases
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/tektoncd/pipeline/blob/main/roadmap.md
- group: commercial
  title: ''
  type: Plans
  url: plans/tekton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tekton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tekton-finops.yml
created: '2026-05-08'
description: Tekton is a cloud-native CI/CD framework implemented as a set of Kubernetes Custom Resource Definitions and controllers under the tekton.dev API group. Tekton is a CNCF Incubating project. Its primary API surface is Kubernetes-native — Tasks, Pipelines, PipelineRuns, TaskRuns, EventListeners, Triggers, etc. — accessed through the Kubernetes API server (kubectl, client-go, the tkn CLI, and the Tekton Dashboard). Tekton itself is open-source under Apache 2.0; commercial offerings layered on Tekton (Red Hat OpenShift Pipelines, Jenkins X, Google Cloud Build private preview integrations, IBM Cloud Continuous Delivery, Pipelines-as-Code on GitOps platforms) are out of scope of the upstream project.
finops:
- name: Tekton Finops
  service_category: DevOps / CI/CD
  slug: tekton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tekton.png
layout: provider
modified: '2026-05-08'
name: Tekton
nav: Providers
network: true
overview: 'Tekton publishes 1 API on the [APIs.io](https://apis.io/) network: Task CRD. Tagged areas include DevOps, CI/CD, Kubernetes, CNCF, and Pipelines.


  Tekton''s developer surface includes documentation, getting-started guide, CLI, engineering blog, YouTube channel, release notes, and 19 more developer resources.'
plans:
- name: Tekton Plans Pricing
  plan_count: 2
  slug: tekton-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Tekton Rate Limits
  slug: tekton-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 32.3
    developer_ergonomics: 28.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 26.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tekton/refs/heads/main/screenshots/tekton-2026-06-20T195017.png
security:
- kind: domain-security
  name: Tekton Domain Security
  slug: tekton-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tekton
tags:
- DevOps
- CI/CD
- Kubernetes
- CNCF
- Pipelines
- Open Source
- CRD
- Operator
website: https://tekton.dev/
---
