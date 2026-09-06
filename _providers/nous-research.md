---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nous Research Agentic Access
  operation_count: 2
  slug: nous-research-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- baseURL: https://inference-api.nousresearch.com/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions.
  name: Nous Research Chat API
  slug: nous-research-chat-api
- baseURL: https://inference-api.nousresearch.com/v1
  baseurl_source: declared
  description: Model discovery and catalog.
  name: Nous Research Models API
  slug: nous-research-models-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nous Research Inference API (Nous Portal) Chat API
  slug: open-nous-research-chat-api
- collection_type: open
  name: Nous Research Inference API (Nous Portal) Chat Models API
  slug: open-nous-research-models-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nous-research-agentic-access.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nous-research-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nous-research-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/nous-research-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nous-research-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nous-research-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nous-research-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nous-research-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nous-research-inference-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nous-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nous-research-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nousresearch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.nousresearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://portal.nousresearch.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://portal.nousresearch.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://portal.nousresearch.com
- group: company
  title: ''
  type: Blog
  url: https://nousresearch.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NousResearch
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/jqVphNsB4H
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/NousResearch
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nousresearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nousresearch/
created: '2026-07-17'
description: Nous Research is an AI research and infrastructure company ("The AI Accelerator Company") known for the open-weight Hermes family of language models (including Hermes 4) and for Nous Portal, an OpenAI-compatible inference API served at inference-api.nousresearch.com. The Portal aggregates Nous's own Hermes models alongside a broad catalog of open and frontier third-party models (OpenRouter- style routing, 280+ models) behind a single chat-completions endpoint. Distinctively, the inference API supports the x402 HTTP payment protocol, returning HTTP 402 with a Solana USDC micropayment envelope so agents can pay per request without a pre-provisioned account. Beyond inference, Nous ships the Hermes Agent framework, Atropos RL environments, and Psyche/DisTrO for distributed model training over the internet. Backed by Paradigm.
image: https://nousresearch.com/wp-content/uploads/2024/03/android-chrome-512x512-1-300x300.png
layout: provider
modified: '2026-07-20'
name: Nous Research
nav: Providers
network: true
overview: 'Nous Research publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Large Language Models, and Inference.


  Nous Research''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, support, and 17 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 13.5
    developer_ergonomics: 33.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nous-research/refs/heads/main/screenshots/nous-research-2026-08-07T185555.png
security:
- kind: authentication
  name: Nous Research Authentication
  slug: nous-research-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nous Research Domain Security
  slug: nous-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nous-research
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Large Language Models
- Inference
- Agents
- Open Weights
- x402
website: https://nousresearch.com
---
