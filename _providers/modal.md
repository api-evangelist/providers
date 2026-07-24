---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 28
  human_in_the_loop: 3
  name: Modal Com Agentic Access
  operation_count: 56
  slug: modal-com-agentic-access
  summary_line: 56 operations · 28 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: Modal App lifecycle.
  name: Modal Apps API
  slug: modal-com-apps-api
- description: Distributed key-value stores.
  name: Modal Dicts API
  slug: modal-com-dicts-api
- description: Modal workspace environments.
  name: Modal Environments API
  slug: modal-com-environments-api
- description: Process execution inside sandboxes.
  name: Modal Execution API
  slug: modal-com-execution-api
- description: Volume file operations.
  name: Modal Files API
  slug: modal-com-files-api
- description: Sandbox filesystem operations.
  name: Modal Filesystem API
  slug: modal-com-filesystem-api
- description: Modal Function definitions, invocations, and scaling.
  name: Modal Functions API
  slug: modal-com-functions-api
- description: Container image specifications and builds.
  name: Modal Images API
  slug: modal-com-images-api
- description: Asynchronous function invocations and result retrieval.
  name: Modal Invocations API
  slug: modal-com-invocations-api
- description: Distributed FIFO queues.
  name: Modal Queues API
  slug: modal-com-queues-api
- description: Sandbox lifecycle and management.
  name: Modal Sandboxes API
  slug: modal-com-sandboxes-api
- description: Scheduled function executions.
  name: Modal Schedules API
  slug: modal-com-schedules-api
- description: Encrypted environment-variable secrets.
  name: Modal Secrets API
  slug: modal-com-secrets-api
- description: Modal API tokens.
  name: Modal Tokens API
  slug: modal-com-tokens-api
- description: Volume lifecycle.
  name: Modal Volumes API
  slug: modal-com-volumes-api
- description: HTTP/ASGI/WSGI web endpoints backed by Modal Functions.
  name: Modal WebEndpoints API
  slug: modal-com-webendpoints-api
- description: Modal workspaces.
  name: Modal Workspaces API
  slug: modal-com-workspaces-api
artifact_total: 61
collections:
- collection_type: open
  name: Modal Dicts and Queues API
  slug: open-modal-dicts-queues
- collection_type: open
  name: Modal Functions API
  slug: open-modal-functions
- collection_type: open
  name: Modal Images API
  slug: open-modal-images
- collection_type: open
  name: Modal Sandboxes API
  slug: open-modal-sandboxes
- collection_type: open
  name: Modal Schedules API
  slug: open-modal-schedules
- collection_type: open
  name: Modal Secrets API
  slug: open-modal-secrets
- collection_type: open
  name: Modal Tokens and Workspace API
  slug: open-modal-tokens
- collection_type: open
  name: Modal Volumes API
  slug: open-modal-volumes
- collection_type: open
  name: Modal Web Endpoints API
  slug: open-modal-web-endpoints
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modal-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modal-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modal-com-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://modal.com
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://modal.com/docs/guide
- group: build
  title: ''
  type: CodeExamples
  url: https://modal.com/docs/examples
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/reference
- group: company
  title: ''
  type: Blog
  url: https://modal.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://modal.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modal.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modal.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modal.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.modal.com
- group: start
  title: ''
  type: Signup
  url: https://modal.com/signup
- group: start
  title: ''
  type: Signup
  url: https://modal.com/login
- group: operate
  title: ''
  type: Support
  url: https://modal.com/support
- group: operate
  title: ''
  type: Forums
  url: https://modal.com/slack
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/modal_labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modal-labs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modal-labs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/modal-labs/modal-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/modal-labs/libmodal
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/modal-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/multinode-training-guide
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/modal-labs/awesome-modal
- group: build
  title: ''
  type: Tools
  url: https://github.com/modal-labs/synchronicity
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/quillman
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/turbo-art
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/ci-on-modal
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/modal-labs/credential-injection
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/modal-labs/gpu-glossary
- group: build
  title: ''
  type: Tools
  url: https://github.com/modal-labs/stopwatch
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/modal/
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/modal
- group: build
  title: ''
  type: Tools
  url: https://modal.com/docs/reference/cli/run
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/gpu
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/scale
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/cold-start
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/memory-snapshots
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/retries
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/timeouts
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/preemption
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/tunnels
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/cloud-bucket-mounts
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/notebooks
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/private-vpc
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/region-selection
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/managing-deployments
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/observability
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs/guide/security
- group: commercial
  title: ''
  type: Plans
  url: https://modal.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://modal.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/modal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/modal-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/modal-com-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/modal-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Modal is a serverless cloud platform for AI and data workloads. Modal lets developers write ordinary Python and run it on remote GPUs and CPUs with sub-second cold starts, instant autoscaling, and declarative container images. The platform's primitives — Functions, Sandboxes, Volumes, Images, Secrets, Dicts, Queues, Schedules, and Web Endpoints — cover inference, fine-tuning, multi-node training, batch processing, agent code execution, and HTTP/web APIs. Modal sells per-second metered compute across the full NVIDIA GPU lineup (T4 → B200) under Starter, Team, and Enterprise plans. Modal Labs raised a $355M Series C in 2026 and is used in production by Decagon, Runway, Physical Intelligence, Suno, Chai Discovery, Lovable, Quora, Reducto, and many others.
examples:
- key_count: 2
  name: Modal Create Sandbox Example
  slug: modal-create-sandbox-example
- key_count: 2
  name: Modal Invoke Function Example
  slug: modal-invoke-function-example
features:
- Serverless Python functions with sub-second cold starts and autoscaling container pools
- GPU compute across T4, L4, A10, L40S, A100 40/80GB, RTX PRO 6000, H100, H200, and B200
- Modal Sandboxes for executing untrusted user/agent code with full container isolation
- Declarative Image builder with layered caching (pip_install, apt_install, run_commands, from_registry, from_dockerfile)
- Modal Volumes — distributed file system with commit/reload semantics; v2 supports many concurrent writers
- Cloud bucket mounts for S3, GCS, R2, and Azure
- Dicts and Queues for cross-container shared state and coordination
- Modal Secrets for encrypted environment-variable injection
- Modal Cron and Period schedules with timezone support
- Web Endpoints via FastAPI, ASGI, WSGI, and custom web servers — streaming and WebSockets
- Proxy-auth tokens, custom URL labels, and live development with `modal serve`
- '`modal run`, `modal deploy`, `modal serve`, `modal shell`, `modal container exec` CLI workflows'
- Python SDK (`modal`) plus JavaScript/TypeScript and Go SDKs via `libmodal`
- Modal Notebooks for interactive development with GPU attachment
- Multi-node distributed training with gang scheduling
- Memory snapshots and warm pools for sub-second cold starts on large models
- Per-second metered billing for CPU, memory, and GPU with tag-based chargeback
- Plan-based concurrency quotas (containers, GPUs, cron jobs, web endpoints)
- Token id/secret authentication scoped to workspace and environment
- Static outbound IP via `modal.Proxy` for IP-allowlisted integrations
- Tunnels and port forwarding for sandbox networking
- SOC 2 Type II certified
finops:
- name: Modal Finops
  service_category: Compute
  slug: modal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modal-com.png
json_schemas:
- name: Modal Function
  property_count: 16
  slug: modal-function
- name: Modal Sandbox
  property_count: 14
  slug: modal-sandbox
jsonld:
- class_count: 25
  name: Modal Com Context
  property_count: 4
  slug: modal-com-context
layout: provider
modified: '2026-05-25'
name: Modal
nav: Providers
network: true
overview: 'Modal publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Dicts API, Environments API, and 14 more. Tagged areas include Serverless, GPU, Cloud Compute, AI Infrastructure, and Sandboxes.


  The Modal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Modal''s developer surface includes authentication, developer portal, documentation, getting-started guide, code examples, engineering blog, changelog, and 51 more developer resources.'
plans:
- name: Modal Plans Pricing
  plan_count: 3
  slug: modal-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Modal Rate Limits
  slug: modal-rate-limits
rules:
- name: Modal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: modal-com-jsonschema-spectral-rules
- name: Modal API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: modal-rules
score:
  band: strong
  composite: 67.5
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 60.9
    developer_ergonomics: 52.2
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 68.4
  previous_composite: 67.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modal/refs/heads/main/screenshots/modal-com-2026-06-20T185747.png
security:
- kind: authentication
  name: Modal Com Authentication
  slug: modal-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Modal Com Domain Security
  slug: modal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modal
tags:
- Serverless
- GPU
- Cloud Compute
- AI Infrastructure
- Sandboxes
- Inference
- Training
- Batch Processing
- Python
- TypeScript
- Go
website: https://modal.com
---
