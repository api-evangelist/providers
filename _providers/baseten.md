---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Baseten Agentic Access
  operation_count: 2
  slug: baseten-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: Deployment management, async/queued inference, chain calls (multi-model workflows), training, dedicated-deployment lifecycle, async result polling, and webhook delivery.
  name: Baseten Management & Async API
  slug: management
- description: The Chat Completions API from Baseten — 1 operation(s) for chat completions.
  name: Baseten Chat Completions API
  slug: baseten-chat-completions-api
- description: The Messages API from Baseten — 1 operation(s) for messages.
  name: Baseten Messages API
  slug: baseten-messages-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Baseten LLM Inference Chat Completions API
  slug: open-baseten-chat-completions-api
- collection_type: open
  name: Baseten LLM Inference API
  slug: open-baseten-llm
- collection_type: open
  name: Baseten LLM Inference Chat Completions Messages API
  slug: open-baseten-messages-api
- collection_type: open
  name: Baseten Anthropic-Compatible Inference API
  slug: open-baseten-messages
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/baseten-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/baseten-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baseten-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/baseten-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/basetenlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/baseten
- group: company
  title: ''
  type: Website
  url: https://www.baseten.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.baseten.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.baseten.co/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/baseten-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/baseten-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/baseten-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.baseten.co/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.baseten.co/blog/
created: '2026-05-08'
description: Baseten is a production inference platform for deploying and serving custom and pre-trained ML models. Offers a Model APIs catalog with OpenAI-compatible endpoints (DeepSeek, Qwen, GLM, Nemotron), dedicated deployments via Truss, autoscaling GPU compute, async/queue inference, training, chains (multi-model workflows), and management APIs.
finops:
- name: Baseten Finops
  service_category: AI
  slug: baseten-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/baseten.png
json_schemas:
- name: ChatCompletionContentPartImageParam
  property_count: 2
  slug: baseten-chatcompletioncontentpartimageparam
- name: ChatCompletionContentPartInputAudioParam
  property_count: 2
  slug: baseten-chatcompletioncontentpartinputaudioparam
- name: ChatCompletionContentPartTextParam
  property_count: 2
  slug: baseten-chatcompletioncontentparttextparam
- name: ChatCompletionLogProb
  property_count: 3
  slug: baseten-chatcompletionlogprob
- name: ChatCompletionLogProbs
  property_count: 1
  slug: baseten-chatcompletionlogprobs
- name: ChatCompletionLogProbsContent
  property_count: 4
  slug: baseten-chatcompletionlogprobscontent
- name: ChatCompletionMessage
  property_count: 5
  slug: baseten-chatcompletionmessage
- name: ChatCompletionMessageToolCallParam
  property_count: 4
  slug: baseten-chatcompletionmessagetoolcallparam
- name: ChatCompletionNamedFunction
  property_count: 1
  slug: baseten-chatcompletionnamedfunction
- name: ChatCompletionNamedToolChoiceParam
  property_count: 2
  slug: baseten-chatcompletionnamedtoolchoiceparam
- name: ChatCompletionRequest
  property_count: 43
  slug: baseten-chatcompletionrequest
- name: ChatCompletionStreamResponse
  property_count: 6
  slug: baseten-chatcompletionresponse
- name: ChatCompletionResponseStreamChoice
  property_count: 5
  slug: baseten-chatcompletionresponsestreamchoice
- name: ChatCompletionToolsParam
  property_count: 2
  slug: baseten-chatcompletiontoolsparam
- name: CompletionTokensDetails
  property_count: 4
  slug: baseten-completiontokensdetails
- name: DeltaMessage
  property_count: 3
  slug: baseten-deltamessage
- name: DisaggregatedParams
  property_count: 7
  slug: baseten-disaggregatedparams
- name: File
  property_count: 2
  slug: baseten-file
- name: FileFile
  property_count: 3
  slug: baseten-filefile
- name: Function
  property_count: 2
  slug: baseten-function
- name: FunctionCall
  property_count: 2
  slug: baseten-functioncall
- name: FunctionDefinition
  property_count: 4
  slug: baseten-functiondefinition
- name: ImageURL
  property_count: 2
  slug: baseten-imageurl
- name: InputAudio
  property_count: 2
  slug: baseten-inputaudio
- name: InputMessage
  property_count: 2
  slug: baseten-inputmessage
- name: JsonSchema
  property_count: 4
  slug: baseten-jsonschema
- name: MessagesRequest
  property_count: 12
  slug: baseten-messagesrequest
- name: MessagesResponse
  property_count: 8
  slug: baseten-messagesresponse
- name: PromptTokensDetails
  property_count: 2
  slug: baseten-prompttokensdetails
- name: ResponseFormatGrammar
  property_count: 2
  slug: baseten-responseformatgrammar
- name: ResponseFormatJson
  property_count: 2
  slug: baseten-responseformatjson
- name: ResponseFormatJsonObject
  property_count: 1
  slug: baseten-responseformatjsonobject
- name: ResponseFormatStructuralTag
  property_count: 2
  slug: baseten-responseformatstructuraltag
- name: ResponseFormatText
  property_count: 1
  slug: baseten-responseformattext
- name: StreamOptions
  property_count: 2
  slug: baseten-streamoptions
- name: TextBlock
  property_count: 2
  slug: baseten-textblock
- name: ToolCall
  property_count: 4
  slug: baseten-toolcall
- name: ToolChoice
  property_count: 0
  slug: baseten-toolchoice
- name: ToolDefinition
  property_count: 3
  slug: baseten-tooldefinition
- name: ToolResultBlock
  property_count: 4
  slug: baseten-toolresultblock
- name: ToolUseBlock
  property_count: 4
  slug: baseten-tooluseblock
- name: Usage
  property_count: 2
  slug: baseten-usage
- name: UsageInfo
  property_count: 5
  slug: baseten-usageinfo
json_structures:
- name: Baseten Structure
  property_count: 0
  slug: baseten-structure
layout: provider
modified: '2026-05-19'
name: Baseten
nav: Providers
network: true
overview: 'Baseten publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat Completions API and Messages API. Tagged areas include AI, ML, Inference, Deployment, and MLOps.


  The Baseten catalog on APIs.io includes 1 Spectral governance ruleset.


  Baseten''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Baseten Plans Pricing
  plan_count: 1
  slug: baseten-plans-pricing
random_paper: 142
rate_limits:
- limit_count: 1
  name: Baseten Rate Limits
  slug: baseten-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Baseten API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: baseten-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.9
  delta: -6.2
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 9.8
    contract_quality: 58.0
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/baseten/refs/heads/main/screenshots/baseten-2026-06-20T173126.png
security:
- kind: authentication
  name: Baseten Authentication
  slug: baseten-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Baseten Domain Security
  slug: baseten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Baseten Trust Center
  slug: baseten-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR, CSA STAR
slug: baseten
tags:
- AI
- ML
- Inference
- Deployment
- MLOps
- OpenAI Compatible
- Anthropic Compatible
- Truss
website: https://www.baseten.co/
---
