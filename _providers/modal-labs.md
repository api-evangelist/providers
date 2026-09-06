---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Modal Labs Agentic Access
  operation_count: 3
  slug: modal-labs-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Decorate Python functions with @app.function to run them remotely on Modal's cloud. Invoke deployed functions synchronously (.remote), asynchronously (.spawn), in parallel (.map), or look them up from
  name: Modal Functions and Remote Invocation
  slug: modal-labs-functions-api
- description: Distributed, high-performance file system volumes for sharing state across functions and containers, managed via modal.Volume in the SDK and the `modal volume` CLI. Read/write, commit, and reload oper
  name: Modal Volumes
  slug: modal-labs-volumes-api
- description: Distributed key-value store (modal.Dict) and distributed queue (modal.Queue) for passing state and messages between functions and containers. Accessed exclusively through the SDK; no public REST inter
  name: Modal Dicts and Queues
  slug: modal-labs-dicts-queues-api
- description: 'Securely inject environment variables and credentials into functions and sandboxes via modal.Secret, managed in the dashboard, CLI, or SDK (Secret.from_name / from_dict). SDK/CLI-only; no public REST '
  name: Modal Secrets
  slug: modal-labs-secrets-api
- description: Run functions on a recurring schedule using modal.Period or modal.Cron passed to @app.function(schedule=...). Schedules are declared in code and managed through deployment; there is no REST scheduling
  name: Modal Cron and Scheduled Functions
  slug: modal-labs-scheduled-api
- description: Define container images programmatically with modal.Image (from_registry, debian_slim, pip_install, run_commands) and attach GPUs by passing gpu= (T4, L4, A10, L40S, A100, H100, H200, B200) to a funct
  name: Modal Images and GPU
  slug: modal-labs-images-gpu-api
- description: 'The `modal` command-line interface for deploying apps, running functions, tailing logs, managing volumes/secrets/dicts, and launching shells. Wraps the same gRPC control plane the SDK uses; it is the '
  name: Modal CLI
  slug: modal-labs-cli
- baseURL: https://<workspace>--<app>-<function>.modal.run
  baseurl_source: declared
  description: The Modal Web Endpoints (Representative) API from Modal — 2 operation(s) for modal web endpoints (representative).
  name: Modal Modal Web Endpoints (Representative) API
  slug: modal-labs-modal-web-endpoints-representative-api
- description: Defines, deploys, and invokes serverless Python Functions on Modal with per-function GPU/CPU/memory configuration, autoscaling, and sub-second cold starts.
  name: Modal Functions API
  slug: modal-functions-api
- description: Logical grouping of functions, classes, and resources deployed and versioned together as an App.
  name: Modal Apps API
  slug: modal-apps-api
- description: Spins up isolated, GPU-capable sandbox containers for running untrusted code (LLM agents, tool use, code-interpreter workflows) with file-system and network controls.
  name: Modal Sandboxes API
  slug: modal-sandboxes-api
- description: Builds, caches, and rehydrates container images with pip / conda / apt / uv layers and supports custom Dockerfiles for function and sandbox runtimes.
  name: Modal Images API
  slug: modal-images-api
- description: Distributed read/write Volumes for persistent storage of model weights, datasets, and caches across function invocations.
  name: Modal Volumes API
  slug: modal-volumes-api
- description: Network File Systems for shared, mountable file storage across multiple functions and sandboxes.
  name: Modal Network File Systems API
  slug: modal-network-file-systems-api
- description: Stores environment-variable secrets and API keys, mountable into functions and sandboxes at runtime.
  name: Modal Secrets API
  slug: modal-secrets-api
- description: Publishes HTTP, WebSocket, and ASGI/WSGI web endpoints (FastAPI, Flask, Streamlit) backed by serverless Modal containers with custom domains and TLS.
  name: Modal Web Endpoints API
  slug: modal-web-endpoints-api
- description: Schedules functions to run on cron expressions with retries, time-zone awareness, and job history.
  name: Modal Cron API
  slug: modal-cron-api
- description: Distributed FIFO queues for asynchronous workloads, work-stealing, and producer/consumer patterns across functions.
  name: Modal Queues API
  slug: modal-queues-api
- description: Distributed dictionaries (key-value stores) for sharing state between functions and across container restarts.
  name: Modal Dicts API
  slug: modal-dicts-api
- description: Forwards local ports into Modal containers (and vice versa) for development, debugging, and hybrid networking.
  name: Modal Tunnels API
  slug: modal-tunnels-api
- description: Multi-environment isolation (dev / staging / prod) within a workspace, each with its own apps, secrets, and quotas.
  name: Modal Environments API
  slug: modal-environments-api
- description: Manages workspaces, tokens, members, and authentication for the Modal control plane.
  name: Modal Token / Workspace API
  slug: modal-token-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Modal Web Endpoints (Representative) Modal Web Endpoints (Representative) Modal Web Endpoints (Representative) Modal Web Endpoints (Representative) API
  slug: open-modal-labs-modal-web-endpoints-representative-api
- collection_type: open
  name: Modal Web Endpoints (Representative)
  slug: open-modal-labs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modal-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modal-labs-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modal-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modal-labs
- group: company
  title: ''
  type: Website
  url: https://modal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://modal.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/modal-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modal-labs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/modal-labs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://modal.com/blog/atom.xml
created: '2026-07-01'
description: Modal is a serverless cloud for AI, data, and general compute. Developers define infrastructure as code in Python (with JavaScript and Go SDKs) and run functions, GPUs, sandboxes, web endpoints, cron jobs, and volumes on demand. The primary developer interface is the Modal SDK and CLI communicating with a gRPC backend, not a conventional first-party REST API. User-deployed Modal Functions can be exposed as HTTPS web endpoints (@modal.fastapi_endpoint / asgi_app / wsgi_app / web_server) on *.modal.run, and Sandboxes can expose ports via network tunnels.
finops:
- name: Modal Labs Finops
  service_category: Compute
  slug: modal-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modal-labs.png
layout: provider
modified: '2026-07-01'
name: Modal
nav: Providers
network: true
overview: 'Modal publishes 1 API on the [APIs.io](https://apis.io/) network: Modal Web Endpoints (Representative) API. Tagged areas include Serverless, Compute, GPU, AI Infrastructure, and Sandboxes.


  Modal''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Modal Labs Plans Pricing
  plan_count: 4
  slug: modal-labs-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Modal Labs Rate Limits
  slug: modal-labs-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 20.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Modal Labs Domain Security
  slug: modal-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: modal-labs
tags:
- Serverless
- Compute
- GPU
- AI Infrastructure
- Sandboxes
- Infrastructure as Code
website: https://modal.com/
---
