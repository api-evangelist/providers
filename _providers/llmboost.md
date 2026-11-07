---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: LLMboost provides a monitoring API for brand visibility in AI recommendation engines.
  name: LLMboost API
  slug: llmboost-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/llmboost/plans/llmboost-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/llmboost-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/llmboost/hosts/llmboost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmboost-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmboost/vendors/llmboost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmboost-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llmboost.ai/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llmboost.ai/en/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://llmboost.ai/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://llmboost.ai/en/press
- group: start
  title: ''
  type: Login
  url: https://llmboost.ai/en/login
- group: auth
  href: https://artifacts.apis.io/llmboost/security/llmboost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmboost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmboost.ai/
coverage:
  checked: '2026-10-18'
  detail: Pricing page returns HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://llmboost.ai/en/pricing
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: LLMboost helps brands ensure they are visible when AI-driven recommendation engines like ChatGPT, Claude, and Perplexity suggest products. By optimizing for AI discovery alongside traditional SEO, LLMboost provides tools and insights to boost brand presence in the emerging AI recommendation landscape, turning AI traffic into measurable growth opportunities for businesses.
image: https://llmboost.ai/dist/icons/open-graph-r1.png
layout: provider
modified: '2026-10-18'
name: LLMboost
nav: Providers
network: true
overview: 'LLMboost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Brand Intelligence, AI Visibility, Citation Monitoring, Competitor Tracking, and Technical Health.


  LLMboost''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Llmboost Plans Pricing
  plan_count: 6
  slug: llmboost-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Llmboost Domain Security
  slug: llmboost-domain-security
  summary_line: TLSv1.3
slug: llmboost
tags:
- Brand Intelligence
- AI Visibility
- Citation Monitoring
- Competitor Tracking
- Technical Health
website: https://llmboost.ai/
---
