---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Multi-agent orchestration system that routes tasks across frontier foundation models (OpenAI, Anthropic, Google). OpenAI-compatible API surface. Two variants - Fugu Mini (low-latency) and Fugu Ultra (
  name: Sakana Fugu API (Beta)
  slug: fugu
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sakana-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sakana-ai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sakana-ai
- group: company
  title: ''
  type: Website
  url: https://sakana.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SakanaAI
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/SakanaAI
- group: commercial
  title: ''
  type: Plans
  url: plans/sakana-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sakana-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sakana-ai-finops.yml
created: '2026-05-08'
description: Sakana AI is a Tokyo-based AI R&D company founded by ex-Google researchers focused on collective intelligence, evolutionary optimization, and nature-inspired AI methods. The company's first commercial product is Sakana Fugu - a multi-agent orchestration system with an OpenAI-compatible API (currently in beta). Sakana also publishes Sakana Chat (consumer) and Sakana Marlin (beta).
finops:
- name: Sakana Ai Finops
  service_category: AI and Machine Learning
  slug: sakana-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sakana-ai.png
layout: provider
modified: '2026-05-08'
name: Sakana AI
nav: Providers
network: true
overview: 'Sakana AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Research, Foundation Models, and Multi-Agent.


  Sakana AI''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Sakana Ai Plans Pricing
  plan_count: 2
  slug: sakana-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Sakana Ai Rate Limits
  slug: sakana-ai-rate-limits
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 11.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sakana-ai/refs/heads/main/screenshots/sakana-ai-2026-06-20T193337.png
security:
- kind: domain-security
  name: Sakana Ai Domain Security
  slug: sakana-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sakana Ai Vulnerability Disclosure
  slug: sakana-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sakana-ai
tags:
- Artificial Intelligence
- LLM
- Research
- Foundation Models
- Multi-Agent
- Orchestration
website: https://sakana.ai/
---
