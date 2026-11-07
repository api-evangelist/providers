---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI 智能对话 platform providing conversational agents and tools.
  name: Mycel AI
  slug: mycel-ai
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/pianam-cn/llms/pianam-cn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pianam-cn-llms.txt
- group: other
  href: https://artifacts.apis.io/pianam-cn/a2a/pianam-cn-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/pianam-cn-a2a.yml
- group: other
  href: https://artifacts.apis.io/pianam-cn/hosts/pianam-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pianam-cn-hosts.yml
- group: build
  href: https://artifacts.apis.io/pianam-cn/packages/pianam-cn-packages.yml
  title: ''
  type: SDKs
  url: packages/pianam-cn-packages.yml
- group: build
  href: https://artifacts.apis.io/pianam-cn/packages/pianam-cn-packages.yml
  title: ''
  type: Packages
  url: packages/pianam-cn-packages.yml
- group: auth
  href: https://artifacts.apis.io/pianam-cn/security/pianam-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pianam-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pianam.cn/
created: '2026-10-29'
description: Pianam.cn provides Mycel, an AI-powered conversational platform offering chat, image generation, code execution, and skill-based AI services. The site hosts a web interface for AI assistants, a developer portal, and links to trade.pianam.cn for API key management. It targets Chinese users with a range of AI tools and integrates with GitHub projects.
layout: provider
modified: '2026-10-29'
name: pianam-cn
nav: Providers
network: true
overview: 'pianam-cn publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Chatbots, Conversations, and Chinese.


  The pianam-cn catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Pianam Cn Plans Pricing
  plan_count: 1
  slug: pianam-cn-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: pianam-cn API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: pianam-cn-rules
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 42.5
    catalog_earned_first_party: 8.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 60.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.8
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pianam-cn/pianam-cn-2026-11-03T141202.png
security:
- kind: authentication
  name: Pianam Cn Authentication
  slug: pianam-cn-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pianam Cn Domain Security
  slug: pianam-cn-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-users
  slug: pianam-cn-list-users
slug: pianam-cn
tags:
- Company
- Artificial Intelligence
- Chatbots
- Conversations
- Chinese
website: https://pianam.cn/
---
