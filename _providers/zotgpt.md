---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 29.7
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: OpenAI-compatible chat completions.
  name: ZotGPT (UC Irvine) Chat API
  slug: zotgpt-chat-api
- description: Vector embeddings across the campus model catalog.
  name: ZotGPT (UC Irvine) Embeddings API
  slug: zotgpt-embeddings-api
artifact_total: 9
collections:
- collection_type: open
  name: ZotGPT API (Deprecated)
  slug: open-zotgpt-api
- collection_type: open
  name: ZotGPT Gateway
  slug: open-zotgpt-gateway
common:
- group: company
  title: ''
  type: Website
  url: https://zotgpt.uci.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.azureapi.zotgpt.uci.edu
- group: docs
  title: ''
  type: Documentation
  url: https://zotgpt.uci.edu/services/
- group: docs
  title: ''
  type: APIReference
  url: https://zotgpt.uci.edu/services/gateway/
- group: start
  title: ''
  type: GettingStarted
  url: https://zotgpt.uci.edu/services/gateway/clients/
- group: operate
  title: ''
  type: Support
  url: https://zotgpt.uci.edu/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zotgpt.uci.edu/privacy/
- group: other
  title: ''
  type: Organization
  url: https://oit.uci.edu
- group: other
  title: ''
  type: Team
  url: https://zotgpt.uci.edu/team/
- group: company
  title: ''
  type: Partners
  url: https://zotgpt.uci.edu/partners/
- group: other
  title: ''
  type: Sustainability
  url: https://zotgpt.uci.edu/sustainability/
- group: learn
  title: ''
  type: Training
  url: https://zotgpt.uci.edu/services/academy/
- group: other
  title: ''
  type: Prompts
  url: https://zotgpt.uci.edu/prompts/
- group: other
  title: ''
  type: Marketplace
  url: https://zotgpt.uci.edu/services/marketplace/
- group: company
  title: ''
  type: Blog
  url: https://www.oit.uci.edu/services/ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zotgpt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zotgpt-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zotgpt-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://zotgpt.uci.edu/services/gateway/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zotgpt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zotgpt-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zotgpt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zotgpt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zotgpt-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/zotgpt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zotgpt-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/zotgpt-gateway-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zotgpt-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zotgpt-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zotgpt-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zotgpt-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zotgpt-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: 'ZotGPT is the University of California, Irvine''s institutionally-operated generative AI platform, built and run in-house by the UCI Office of Information Technology AI Team rather than purchased as a vendor seat. Launched to faculty and staff in early 2024 and to students in April 2024, it now spans four end-user products (Chat, ClassChat, Creator, Prompt Library), a training arm (Academy), and two generations of developer API. The platform is deliberately multi-cloud and multi-model: the interactive applications run on UC Irvine''s own AWS accounts in us-west-2 behind Shibboleth SSO, the first-generation developer API was fronted by Azure API Management, and models are sourced across OpenAI, Anthropic (via AWS Bedrock), Google, Azure, and open-source options such as Mistral and DeepSeek. The deprecated Azure-managed API at api.zotgpt.uci.edu is being retired in favor of the ZotGPT Gateway, a Portkey-specification unified AI gateway that gives the campus one endpoint, virtual
  API keys, per-key spend limits, and provider-agnostic model routing. Data is held under UC Irvine''s P3 protection standard, retained 12 months, and contractually excluded from vendor model training.'
finops:
- name: Zotgpt Finops
  service_category: ''
  slug: zotgpt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zotgpt.png
layout: provider
modified: '2026-07-28'
name: ZotGPT (UC Irvine)
nav: Providers
network: true
overview: 'ZotGPT (UC Irvine) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Embeddings API. Tagged areas include Artificial Intelligence, Generative AI, LLM, AI Gateway, and Higher Education.


  ZotGPT (UC Irvine)''s developer surface includes documentation, API reference, getting-started guide, support, training material, engineering blog, authentication, and 27 more developer resources.'
plans:
- name: Zotgpt Plans Pricing
  plan_count: 5
  slug: zotgpt-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Zotgpt Rate Limits
  slug: zotgpt-rate-limits
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 17.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 49.1
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 48.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zotgpt/refs/heads/main/screenshots/zotgpt-2026-08-17T083120.png
security:
- kind: authentication
  name: Zotgpt Authentication
  slug: zotgpt-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Zotgpt Domain Security
  slug: zotgpt-domain-security
  summary_line: no transport/DNS hardening detected
slug: zotgpt
tags:
- Artificial Intelligence
- Generative AI
- LLM
- AI Gateway
- Higher Education
- University
- Education
- Multi-Cloud
- Multi-Model
- Chat Completions
- Embeddings
- Model Routing
- Retrieval Augmented Generation
- Identity
- United States
- California
website: https://zotgpt.uci.edu/
---
