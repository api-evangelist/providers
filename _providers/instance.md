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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Instance Agentic Access
  operation_count: 37
  slug: instance-agentic-access
  summary_line: 37 operations · 15 acting
api_count: 28
apis:
- description: The Archive API from Instance — 1 operation(s) for archive.
  name: Instance Archive API
  slug: instance-archive-api
- description: The Audit API from Instance — 3 operation(s) for audit.
  name: Instance Audit API
  slug: instance-audit-api
- description: The Batch API from Instance — 2 operation(s) for batch.
  name: Instance Batch API
  slug: instance-batch-api
- description: The Captions API from Instance — 1 operation(s) for captions.
  name: Instance Captions API
  slug: instance-captions-api
- description: The Clip API from Instance — 1 operation(s) for clip.
  name: Instance Clip API
  slug: instance-clip-api
- description: The Download API from Instance — 1 operation(s) for download.
  name: Instance Download API
  slug: instance-download-api
- description: The Example API from Instance — 1 operation(s) for example.
  name: Instance Example API
  slug: instance-example-api
- description: The Examples API from Instance — 1 operation(s) for examples.
  name: Instance Examples API
  slug: instance-examples-api
- description: The Fast API from Instance — 1 operation(s) for fast.
  name: Instance Fast API
  slug: instance-fast-api
- description: The Feed API from Instance — 2 operation(s) for feed.
  name: Instance Feed API
  slug: instance-feed-api
- description: The H1 API from Instance — 1 operation(s) for h1.
  name: Instance H1 API
  slug: instance-h1-api
- description: The Health API from Instance — 1 operation(s) for health.
  name: Instance Health API
  slug: instance-health-api
- description: The Ingest API from Instance — 1 operation(s) for ingest.
  name: Instance Ingest API
  slug: instance-ingest-api
- description: The Job API from Instance — 1 operation(s) for job.
  name: Instance Job API
  slug: instance-job-api
- description: The Live Example API from Instance — 1 operation(s) for live example.
  name: Instance Live Example API
  slug: instance-live-example-api
- description: The Live Example Video API from Instance — 1 operation(s) for live example video.
  name: Instance Live Example Video API
  slug: instance-live-example-video-api
- description: The Live State API from Instance — 1 operation(s) for live state.
  name: Instance Live State API
  slug: instance-live-state-api
- description: The Opus API from Instance — 1 operation(s) for opus.
  name: Instance Opus API
  slug: instance-opus-api
- description: The Qr API from Instance — 1 operation(s) for qr.
  name: Instance Qr API
  slug: instance-qr-api
- description: The Record API from Instance — 1 operation(s) for record.
  name: Instance Record API
  slug: instance-record-api
- description: The Robot Rollout Verifier API from Instance — 1 operation(s) for robot rollout verifier.
  name: Instance Robot Rollout Verifier API
  slug: instance-robot-rollout-verifier-api
- description: The Segment API from Instance — 1 operation(s) for segment.
  name: Instance Segment API
  slug: instance-segment-api
- description: The Subtasks API from Instance — 1 operation(s) for subtasks.
  name: Instance Subtasks API
  slug: instance-subtasks-api
- description: The Subtasks Trace API from Instance — 1 operation(s) for subtasks trace.
  name: Instance Subtasks Trace API
  slug: instance-subtasks-trace-api
- description: The Upload API from Instance — 2 operation(s) for upload.
  name: Instance Upload API
  slug: instance-upload-api
- description: The Usage API from Instance — 2 operation(s) for usage.
  name: Instance Usage API
  slug: instance-usage-api
- description: The Verify API from Instance — 3 operation(s) for verify.
  name: Instance Verify API
  slug: instance-verify-api
- description: The Verify Frames API from Instance — 1 operation(s) for verify frames.
  name: Instance Verify Frames API
  slug: instance-verify-frames-api
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instance-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/instance-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.instancelabs.ai/
- group: start
  title: ''
  type: Demo
  url: https://demo.instancelabs.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instancelabs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/tryinstance
- group: operate
  title: ''
  type: Support
  url: mailto:founders@instancelabs.ai
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instance-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instance-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instance-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instance-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/instance-verifier-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instance-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/instance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instance-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/instance-verify-rollout.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/instance-batch-verify.md
created: '2026-07-17'
description: Instance (Instance Labs) is a Y Combinator-backed (Summer 2026) company building a verification layer for robot learning. Their platform ingests raw robot rollouts and episode footage from any robot or camera angle and automatically judges whether a task was completed successfully, returning a verdict with supporting evidence and a detailed subtask breakdown. The company positions itself as the ground-truth / success-detection layer that lets robotics teams trust their training data and train policies faster, and reports its verifier reaching higher accuracy than frontier vision-language models at a fraction of the latency across 10,000+ human-labeled episodes on 7 robot platforms. Founded by MIT computer scientists with backgrounds at SpaceX, AWS, and NASA JPL. Today the product is exposed as a hosted demo (submit videos or capture a live rollout for verification); there is no publicly documented developer API, SDK, or OpenAPI at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instance.png
layout: provider
mcp_servers:
- description: ''
  name: instance-mcp.yml
  slug: instance-mcpyml
modified: '2026-07-19'
name: Instance
nav: Providers
network: true
overview: 'Instance publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Archive API, Audit API, Batch API, and 25 more. Tagged areas include Company, Robotics, Machine Learning, Verification, and Evaluation.


  Instance''s developer surface includes support and 16 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 22.0
  delta: -3.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.3
    developer_ergonomics: 8.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 25.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instance/refs/heads/main/screenshots/instance-2026-07-25T222605.png
security:
- kind: domain-security
  name: Instance Domain Security
  slug: instance-domain-security
  summary_line: TLSv1.3 · HSTS
slug: instance
tags:
- Company
- Robotics
- Machine Learning
- Verification
- Evaluation
- Data Quality
- Artificial Intelligence
- Y Combinator
website: https://www.instancelabs.ai/
---
