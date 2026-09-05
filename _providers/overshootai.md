---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 26.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Overshootai Agentic Access
  operation_count: 17
  slug: overshootai-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 2
apis:
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: Pricing, prepaid balance, and checkout.
  name: overshoot.ai Billing API
  slug: overshootai-billing-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The Chat API from overshoot.ai — 1 operation(s) for chat.
  name: overshoot.ai Chat API
  slug: overshootai-chat-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The Healthz API from overshoot.ai — 1 operation(s) for healthz.
  name: overshoot.ai Healthz API
  slug: overshootai-healthz-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The Metrics API from overshoot.ai — 1 operation(s) for metrics.
  name: overshoot.ai Metrics API
  slug: overshootai-metrics-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The Models API from overshoot.ai — 2 operation(s) for models.
  name: overshoot.ai Models API
  slug: overshootai-models-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The Readyz API from overshoot.ai — 1 operation(s) for readyz.
  name: overshoot.ai Readyz API
  slug: overshootai-readyz-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: Create, inspect, keep alive, and delete live video streams.
  name: overshoot.ai Streams API
  slug: overshootai-streams-api
- baseURL: https://api.overshoot.ai/v1beta
  baseurl_source: declared
  description: The V1beta API from overshoot.ai — 1 operation(s) for v1beta.
  name: overshoot.ai V1beta API
  slug: overshootai-v1beta-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inference Service Billing API
  slug: open-overshootai-billing-api
- collection_type: open
  name: Inference Service Billing Chat API
  slug: open-overshootai-chat-api
- collection_type: open
  name: Inference Service Billing Healthz API
  slug: open-overshootai-healthz-api
- collection_type: open
  name: Inference Service Billing Metrics API
  slug: open-overshootai-metrics-api
- collection_type: open
  name: Inference Service Billing Models API
  slug: open-overshootai-models-api
- collection_type: open
  name: Inference Service Billing Readyz API
  slug: open-overshootai-readyz-api
- collection_type: open
  name: Inference Service Billing Streams API
  slug: open-overshootai-streams-api
- collection_type: open
  name: Inference Service Billing V1beta API
  slug: open-overshootai-v1beta-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/overshootai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/overshootai-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.overshoot.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overshoot.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overshoot.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.overshoot.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://overshoot.ai/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overshoot-ai
- group: start
  title: ''
  type: SignUp
  url: https://platform.overshoot.ai
- group: operate
  title: ''
  type: Support
  url: mailto:founders@overshoot.ai
- group: build
  title: ''
  type: Packages
  url: packages/overshootai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/overshootai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overshootai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overshootai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Overshoot is real-time AI vision infrastructure. It ingests live video streams over WebRTC (LiveKit) and lets developers query those frames with vision-language models through an OpenAI-compatible chat completions API, returning structured results such as bounding boxes, pixel coordinates, OCR text, and JSON in as little as 200ms. The REST API manages the full stream lifecycle (create, keepalive, inspect, delete), lists available VLMs from Overshoot, Anthropic, Google, and OpenAI, and handles prepaid credit billing. Overshoot is a Y Combinator and a16z portfolio company building the vision layer for accessibility, security monitoring, sports analysis, robotics, retail analytics, and structured data extraction from live video.
image: https://overshoot.ai/favicon.ico
layout: provider
modified: '2026-07-20'
name: overshoot.ai
nav: Providers
network: true
overview: 'overshoot.ai publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Chat API, Healthz API, and 5 more. Tagged areas include Company, Artificial Intelligence, Computer-Vision, Video, and Real-Time.


  overshoot.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 9 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 2
  name: Overshootai Rate Limits
  slug: overshootai-rate-limits
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 50.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overshootai/refs/heads/main/screenshots/overshootai-2026-08-07T191137.png
security:
- kind: authentication
  name: Overshootai Authentication
  slug: overshootai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Overshootai Domain Security
  slug: overshootai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overshootai
tags:
- Company
- Artificial Intelligence
- Computer-Vision
- Video
- Real-Time
- Streaming
- Machine-Learning
- Vision Language Models
- Inference
- Developer Tools
website: https://platform.overshoot.ai
---
