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
    agent_card: false
    agent_skills: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hyperbolic Ai Agentic Access
  operation_count: 5
  slug: hyperbolic-ai-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 5
apis:
- description: Decentralized on-demand GPU compute marketplace renting idle H100, H200, A100, and RTX 4090 capacity from third-party suppliers. Pricing starts at $0.50/GPU/hr (RTX 4090), $1.39-$1.49/hr (H100), up to
  name: Hyperbolic GPU Marketplace API
  slug: hyperbolic-marketplace-api
- description: Text-to-speech audio endpoint
  name: Hyperbolic Audio Generation API
  slug: hyperbolic-ai-audio-generation-api
- description: Generate chat-style completions from open-source LLMs
  name: Hyperbolic Chat Completions API
  slug: hyperbolic-ai-chat-completions-api
- description: Legacy base-model text completion endpoint
  name: Hyperbolic Completions API
  slug: hyperbolic-ai-completions-api
- description: Text-to-image diffusion endpoint
  name: Hyperbolic Image Generation API
  slug: hyperbolic-ai-image-generation-api
- description: List available inference models
  name: Hyperbolic Models API
  slug: hyperbolic-ai-models-api
arazzos:
- description: Use an LLM to craft a vivid image prompt, then render it with a diffusion model.
  name: Hyperbolic Chat To Image
  slug: hyperbolic-ai-chat-to-image-workflow
- description: Generate an assistant reply with an LLM, then narrate it with text-to-speech.
  name: Hyperbolic Chat To Speech
  slug: hyperbolic-ai-chat-to-speech-workflow
- description: List the live model catalog, pick a chat model, and run a chat completion against it.
  name: Hyperbolic Discover Model And Chat
  slug: hyperbolic-ai-discover-model-and-chat-workflow
- description: List the catalog and run a base-model text completion against a non-instruct model.
  name: Hyperbolic Discover Model And Complete
  slug: hyperbolic-ai-discover-model-and-complete-workflow
- description: Render an image with diffusion, then describe it with a vision LLM and narrate the caption.
  name: Hyperbolic Generate And Describe Image
  slug: hyperbolic-ai-generate-and-describe-image-workflow
- description: Render an image, judge it with a vision model, and re-render once if it fails QA.
  name: Hyperbolic Image Prompt QA Loop
  slug: hyperbolic-ai-image-prompt-qa-workflow
- description: List models, write a short story, illustrate it, and narrate it across four endpoints.
  name: Hyperbolic Multimodal Story
  slug: hyperbolic-ai-multimodal-story-workflow
- description: Confirm a reasoning model, summarize a topic with it, and narrate the summary.
  name: Hyperbolic Research Summarize And Narrate
  slug: hyperbolic-ai-research-summarize-narrate-workflow
- description: Run an OpenAI-compatible tool call and feed the tool result back for a final answer.
  name: Hyperbolic Tool Calling Roundtrip
  slug: hyperbolic-ai-tool-calling-roundtrip-workflow
artifact_total: 66
collections:
- collection_type: postman
  name: Hyperbolic Audio Generation API
  slug: postman-hyperbolic-audio-generation-api
- collection_type: postman
  name: Hyperbolic Chat Completions API
  slug: postman-hyperbolic-chat-completions-api
- collection_type: postman
  name: Hyperbolic Completions API
  slug: postman-hyperbolic-completions-api
- collection_type: postman
  name: Hyperbolic Image Generation API
  slug: postman-hyperbolic-image-generation-api
- collection_type: postman
  name: Hyperbolic Models API
  slug: postman-hyperbolic-models-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperbolic Audio Generation API
  slug: open-hyperbolic-ai-audio-generation-api
- collection_type: open
  name: Hyperbolic Audio Generation Chat Completions API
  slug: open-hyperbolic-ai-chat-completions-api
- collection_type: open
  name: Hyperbolic Audio Generation Completions API
  slug: open-hyperbolic-ai-completions-api
- collection_type: open
  name: Hyperbolic Audio Generation Image Generation API
  slug: open-hyperbolic-ai-image-generation-api
- collection_type: open
  name: Hyperbolic Audio Generation Models API
  slug: open-hyperbolic-ai-models-api
- collection_type: open
  name: Hyperbolic Audio Generation API
  slug: open-hyperbolic-audio-generation-api
- collection_type: open
  name: Hyperbolic Chat Completions API
  slug: open-hyperbolic-chat-completions-api
- collection_type: open
  name: Hyperbolic Completions API
  slug: open-hyperbolic-completions-api
- collection_type: open
  name: Hyperbolic Image Generation API
  slug: open-hyperbolic-image-generation-api
- collection_type: open
  name: Hyperbolic Models API
  slug: open-hyperbolic-models-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HyperbolicLabs/hyperbolic-cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/HyperbolicLabs/hyperbolic-cli/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/HyperbolicLabs/hyperbolic-cli/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperbolic-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperbolic-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperbolic-ai-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hyperbolic/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-chat-to-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-chat-to-speech-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-discover-model-and-chat-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-discover-model-and-complete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-generate-and-describe-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-image-prompt-qa-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-multimodal-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-research-summarize-narrate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hyperbolic-ai-tool-calling-roundtrip-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.hyperbolic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/overview/platform-comparison
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/inference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperbolic.ai/inference/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/on-demand/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hyperbolic.ai/on-demand/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hyperbolic.ai/reserved/overview
- group: start
  title: ''
  type: Signup
  url: https://app.hyperbolic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.hyperbolic.ai/settings/api-keys
- group: start
  title: ''
  type: Sandbox
  url: https://app.hyperbolic.ai/models
- group: company
  title: ''
  type: Blog
  url: https://www.hyperbolic.ai/blog
- group: company
  title: ''
  type: AboutUs
  url: https://www.hyperbolic.ai/about
- group: company
  title: ''
  type: Careers
  url: https://www.hyperbolic.ai/careers
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/hyperbolic
- group: company
  title: ''
  type: PressKit
  url: https://www.hyperbolic.ai/media-kit
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperbolic.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperbolic.ai/terms-of-use
- group: operate
  title: ''
  type: ContactForm
  url: mailto:contact@hyperbolic.ai
- group: operate
  title: ''
  type: ContactForm
  url: mailto:sales@hyperbolic.ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@hyperbolic.ai
- group: operate
  title: ''
  type: ContactForm
  url: https://calendly.com/d/cq79-jyv-jg4/hyperbolic-sales-demo
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hyperbolic_labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperbolic-labs/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@hyperboliclabs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HyperbolicLabs
- group: other
  title: ''
  type: OpenSourceProject
  url: https://github.com/HyperbolicLabs/Hyper-dOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/HyperbolicLabs/Hyperbolic-AgentKit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/HyperbolicLabs/hyperbolic-ts
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/hyperbolic-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/hyperbolic-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/homebrew-hyperbolic
- group: build
  title: ''
  type: SDKs
  url: https://github.com/HyperbolicLabs/hyperbolic-gradio
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/hyperbolic-x402
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/skypilot
- group: build
  title: ''
  type: Tools
  url: https://github.com/HyperbolicLabs/skypilot-catalog
- group: other
  title: ''
  type: OpenSourceProject
  url: https://github.com/HyperbolicLabs/jungle.proto
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/HyperbolicLabs/inference-benchmarks
- group: operate
  title: ''
  type: Forums
  url: https://github.com/HyperbolicLabs/feature-requests
- group: docs
  title: ''
  type: Documentation
  url: https://huggingface.co/docs/inference-providers/en/providers/hyperbolic
- group: other
  title: ''
  type: ApiBaseURL
  url: https://api.hyperbolic.xyz/v1
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperbolic-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperbolic-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperbolic-ai-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hyperbolic-ai-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/hyperbolic-ai-rules.yml
created: '2026-05-25'
description: Hyperbolic is an open-access AI cloud and decentralized GPU marketplace serving 200,000+ builders with affordable inference and bare-metal compute. The platform combines a serverless OpenAI-compatible inference API spanning 25+ open-source LLMs (including the only public Llama-3.1-405B-Base in BF16), image and audio models, with an on-demand GPU rental marketplace aggregating idle H100 / H200 / A100 / RTX 4090 capacity from third-party suppliers at 3-10x lower cost than hyperscalers. Reserved clusters, dedicated endpoints, an OpenAI-drop-in Python and TypeScript SDK, a Go CLI, an MCP server, the Hyperbolic AgentKit, the open-source Hyper-dOS distributed operating system, and Coinbase x402 crypto payments round out the stack.
examples:
- key_count: 2
  name: Hyperbolic Audio Generation Example
  slug: hyperbolic-audio-generation-example
- key_count: 2
  name: Hyperbolic Chat Completion Example
  slug: hyperbolic-chat-completion-example
- key_count: 2
  name: Hyperbolic Image Generation Example
  slug: hyperbolic-image-generation-example
- key_count: 2
  name: Hyperbolic Models List Example
  slug: hyperbolic-models-list-example
features:
- OpenAI-compatible REST API at https://api.hyperbolic.xyz/v1 — drop-in replacement requiring only api_key and base_url changes
- 25+ open-source inference models — Llama 3.1 8B/70B/405B, Qwen 2.5, DeepSeek V3, DeepSeek R1, Hermes 3, Mistral, Llama 3.2 Vision, Qwen2-VL
- Only public provider serving Llama-3.1-405B-Base in BF16 (high-throughput precision) and FP8 (low-latency)
- Image generation with Stable Diffusion XL, SD 3.5, FLUX.1 (sunset), ControlNet, custom LoRAs from $0.0025/image
- Audio generation (Melo TTS sunset, Whisper coming soon) from $0.001 per 1000 characters
- Decentralized GPU marketplace renting H100, H200, A100, RTX 4090 from third-party suppliers
- On-demand instances deploy in under 1 minute — up to 75% cheaper than AWS / Azure / GCP
- Reserved clusters with volume discounts up to 40% on 3-12 month commitments
- Dedicated single-tenant endpoints for high-throughput inference workloads
- Streaming, tool/function calling, structured JSON output, vision input on supported models
- Python SDK and TypeScript SDK fully OpenAI-compatible
- Hyperbolic CLI (Go) distributed via Homebrew tap
- Model Context Protocol (MCP) server for Claude integration
- Hyperbolic AgentKit — Python agent framework
- Hyper-dOS — open-source Distributed Operating System for GPU orchestration
- Coinbase x402 payment integration for crypto-native chat completions
- Crypto payment support (USDC, USDT, DAI) alongside credit cards
- Hugging Face Inference Providers integration
- Three usage tiers — Basic (60 RPM, free), Pro (600 RPM, $5+ deposit), Enterprise (unlimited, sales)
- 200,000+ builder community
- Marketplace platform fee of 10% on GPU rental income
finops:
- name: Hyperbolic Ai Finops
  service_category: AI and Machine Learning
  slug: hyperbolic-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperbolic-ai.png
json_schemas:
- name: Hyperbolic Chat Completion
  property_count: 0
  slug: hyperbolic-chat-completion
jsonld:
- class_count: 0
  name: Hyperbolic Ai Context
  property_count: 8
  slug: hyperbolic-ai-context
layout: provider
modified: '2026-05-25'
name: Hyperbolic
nav: Providers
network: true
overview: 'Hyperbolic publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audio Generation API, Chat Completions API, Completions API, and 2 more. Tagged areas include Artificial Intelligence, Compute, Decentralized, DePIN, and GPU.


  The Hyperbolic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Hyperbolic''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, sandbox, engineering blog, and 56 more developer resources.'
plans:
- name: Hyperbolic Ai Plans Pricing
  plan_count: 16
  slug: hyperbolic-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Hyperbolic Ai Rate Limits
  slug: hyperbolic-ai-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Hyperbolic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: hyperbolic-ai-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Hyperbolic API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 7
  slug: hyperbolic-ai-rules
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 69.9
    developer_ergonomics: 78.6
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 25.0
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperbolic-ai/refs/heads/main/screenshots/hyperbolic-ai-2026-06-20T183118.png
security:
- kind: authentication
  name: Hyperbolic Ai Authentication
  slug: hyperbolic-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hyperbolic Ai Domain Security
  slug: hyperbolic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperbolic-ai
tags:
- Artificial Intelligence
- Compute
- Decentralized
- DePIN
- GPU
- Image-Generation
- Inference
- LLM
- Marketplace
- Open-Source
website: https://www.hyperbolic.ai/
---
