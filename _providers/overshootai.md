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
- group: company
  title: ''
  type: Website
  url: https://www.overshoot.ai/
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


  overshoot.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 10 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 2
  name: Overshootai Rate Limits
  slug: overshootai-rate-limits
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
website: https://www.overshoot.ai/
---
