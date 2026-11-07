---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Sambanova Systems Agentic Access
  operation_count: 21
  slug: sambanova-systems-agentic-access
  summary_line: 21 operations · 18 acting
api_count: 2
apis:
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Audio API from SambaNova Systems — 2 operation(s) for audio.
  name: SambaNova Systems Audio API
  slug: sambanova-systems-audio-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Chat completions API from SambaNova Systems — 1 operation(s) for chat completions.
  name: SambaNova Systems Chat completions API
  slug: sambanova-systems-chat-completions-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Completions API from SambaNova Systems — 1 operation(s) for completions.
  name: SambaNova Systems Completions API
  slug: sambanova-systems-completions-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Embeddings API from SambaNova Systems — 1 operation(s) for embeddings.
  name: SambaNova Systems Embeddings API
  slug: sambanova-systems-embeddings-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The File Management API from SambaNova Systems — 1 operation(s) for file management.
  name: SambaNova Systems File Management API
  slug: sambanova-systems-file-management-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Main Agent API from SambaNova Systems — 1 operation(s) for main agent.
  name: SambaNova Systems Main Agent API
  slug: sambanova-systems-main-agent-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Main Agent Interactive API from SambaNova Systems — 1 operation(s) for main agent interactive.
  name: SambaNova Systems Main Agent Interactive API
  slug: sambanova-systems-main-agent-interactive-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Messages API from SambaNova Systems — 2 operation(s) for messages.
  name: SambaNova Systems Messages API
  slug: sambanova-systems-messages-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Models API from SambaNova Systems — 2 operation(s) for models.
  name: SambaNova Systems Models API
  slug: sambanova-systems-models-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Responses API from SambaNova Systems — 1 operation(s) for responses.
  name: SambaNova Systems Responses API
  slug: sambanova-systems-responses-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Subagents API from SambaNova Systems — 4 operation(s) for subagents.
  name: SambaNova Systems Subagents API
  slug: sambanova-systems-subagents-api
- baseURL: https://api.sambanova.ai/v1
  baseurl_source: declared
  description: The Subagents Interactive API from SambaNova Systems — 4 operation(s) for subagents interactive.
  name: SambaNova Systems Subagents Interactive API
  slug: sambanova-systems-subagents-interactive-api
artifact_total: 36
collections:
- collection_type: open
  name: Sambanova Agents Service Audio API
  slug: open-sambanova-systems-audio-api
- collection_type: open
  name: Sambanova Agents Service Audio Chat completions API
  slug: open-sambanova-systems-chat-completions-api
- collection_type: open
  name: Sambanova Agents Service Audio Completions API
  slug: open-sambanova-systems-completions-api
- collection_type: open
  name: Sambanova Agents Service Audio Embeddings API
  slug: open-sambanova-systems-embeddings-api
- collection_type: open
  name: Sambanova Agents Service Audio File Management API
  slug: open-sambanova-systems-file-management-api
- collection_type: open
  name: Sambanova Agents Service Audio Main Agent API
  slug: open-sambanova-systems-main-agent-api
- collection_type: open
  name: Sambanova Agents Service Audio Main Agent Interactive API
  slug: open-sambanova-systems-main-agent-interactive-api
- collection_type: open
  name: Sambanova Agents Service Audio Messages API
  slug: open-sambanova-systems-messages-api
- collection_type: open
  name: Sambanova Agents Service Audio Models API
  slug: open-sambanova-systems-models-api
- collection_type: open
  name: Sambanova Agents Service Audio Responses API
  slug: open-sambanova-systems-responses-api
- collection_type: open
  name: Sambanova Agents Service Audio Subagents API
  slug: open-sambanova-systems-subagents-api
- collection_type: open
  name: Sambanova Agents Service Audio Subagents Interactive API
  slug: open-sambanova-systems-subagents-interactive-api
common:
- group: commercial
  href: https://artifacts.apis.io/sambanova-systems/plans/sambanova-systems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sambanova-systems-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://sambanova.ai/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/sambanova-systems/capabilities/sambanova-systems-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sambanova-systems-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/sambanova-systems/security/sambanova-systems-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sambanova-systems-trust-center.yml
- group: operate
  title: ''
  type: Community
  url: https://community.sambanova.ai
- group: other
  title: ''
  type: StarterKits
  url: https://github.com/sambanova/ai-starter-kit
- group: other
  title: ''
  type: Hardware
  url: https://sambanova.ai/products/sn50-rdu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sambanova-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SambaNovaAI
- group: other
  href: https://artifacts.apis.io/sambanova-systems/overlays/sambanova-systems-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sambanova-systems-agents-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sambanova.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.sambanova.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sambanova.ai/cloud
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sambanova.ai/cloud/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sambanova.ai/cloud/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://sambanova.ai/support
- group: company
  title: ''
  type: Blog
  url: https://sambanova.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sambanova
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.sambanova.ai/plans/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.sambanova.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sambanova.ai/legal-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sambanova.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sambanova.ai
- group: operate
  href: https://artifacts.apis.io/sambanova-systems/lifecycle/sambanova-systems-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sambanova-systems-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sambanova-systems/changelog/sambanova-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sambanova-systems-changelog.yml
- group: design
  href: https://artifacts.apis.io/sambanova-systems/lifecycle/sambanova-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sambanova-systems-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/sambanova-systems/authentication/sambanova-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sambanova-systems-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sambanova-systems/security/sambanova-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sambanova-systems-domain-security.yml
- group: build
  href: https://artifacts.apis.io/sambanova-systems/packages/sambanova-systems-packages.yml
  title: ''
  type: Packages
  url: packages/sambanova-systems-packages.yml
- group: build
  href: https://artifacts.apis.io/sambanova-systems/packages/sambanova-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/sambanova-systems-packages.yml
- group: design
  href: https://artifacts.apis.io/sambanova-systems/conventions/sambanova-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sambanova-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/sambanova-systems/errors/sambanova-systems-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/sambanova-systems-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/sambanova-systems/rate-limits/sambanova-systems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sambanova-systems-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sambanova-systems/conformance/sambanova-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sambanova-systems-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sambanova-systems/mcp/sambanova-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sambanova-systems-mcp.yml
- group: design
  href: https://artifacts.apis.io/sambanova-systems/data-model/sambanova-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sambanova-systems-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sambanova-systems/agentic-access/sambanova-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sambanova-systems-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/sambanova-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sambanova-systems/llms/sambanova-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sambanova-systems-llms.txt
- group: agent
  href: https://artifacts.apis.io/sambanova-systems/well-known/sambanova-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sambanova-systems-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sambanova.ai/developer/showcase
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sambanova.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sambanova.ai/docs/en/get-started/overview
created: '2026-07-17'
description: SambaNova Systems is an AI infrastructure company that builds custom Reconfigurable Dataflow Unit (RDU) chips and the SambaCloud, SambaStack, and SambaRack platforms for fast, energy-efficient AI inference. Its developer-facing product, SambaNova Cloud, exposes an OpenAI- and Anthropic-compatible inference API (chat completions, completions, the Responses API, the Messages API, embeddings, and audio transcription/translation) serving open models such as Meta Llama, DeepSeek, MiniMax, gpt-oss, Gemma, and Mistral. A companion Agents Service provides coordinated coding, data-science, deep-research, and financial-analysis agents. Official Python and TypeScript SDKs, tiered rate limits, prompt caching, and dozens of framework integrations round out the platform.
finops:
- has_sources: true
  method: derived
  name: Sambanova Systems Finops
  primary_unit: 1m tokens
  service_category: ''
  slug: sambanova-systems-finops
  template: false
image: https://github.com/sambanova.png
layout: provider
modified: '2026-10-06'
name: SambaNova Systems
nav: Providers
network: true
overview: 'SambaNova Systems publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Chat completions API, Completions API, and 9 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and Inference.


  The SambaNova Systems catalog on APIs.io includes 1 Spectral governance ruleset.


  SambaNova Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Sambanova Systems Plans Pricing
  plan_count: 13
  slug: sambanova-systems-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 11
  name: Sambanova Systems Rate Limits
  slug: sambanova-systems-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: SambaNova Systems API Rules
  rule_count: 68
  severity_counts:
    error: 55
    hint: 0
    info: 7
    warn: 6
  slug: sambanova-systems-rules
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sambanova-systems/sambanova-systems-2026-08-17T081717.png
security:
- kind: authentication
  name: Sambanova Systems Authentication
  slug: sambanova-systems-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sambanova Systems Domain Security
  slug: sambanova-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sambanova Systems Trust Center
  slug: sambanova-systems-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: Generate a chat completion with SambaNova
  slug: sambanova-systems-chat-completion
- name: Run the SambaNova deep research agent
  slug: sambanova-systems-deep-research-agent
- name: Create embeddings with SambaNova
  slug: sambanova-systems-embeddings
- name: Transcribe or translate audio with SambaNova
  slug: sambanova-systems-transcribe-audio
slug: sambanova-systems
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- Inference
- Generative AI
- Agents
- Embeddings
- Platform
- Enterprise
website: https://sambanova.ai
---
