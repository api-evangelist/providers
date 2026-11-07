---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
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
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AdCreator AI provides advertising creative generation via its Shopify app.
  name: AdCreator AI API
  slug: adcreator-ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/adcreator-ai-com/plans/adcreator-ai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adcreator-ai-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adcreator-ai-com/llms/adcreator-ai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adcreator-ai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/adcreator-ai-com/a2a/adcreator-ai-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adcreator-ai-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/adcreator-ai-com/hosts/adcreator-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adcreator-ai-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adcreator-ai.com/legal/terms
- group: start
  title: ''
  type: SignUp
  url: https://adcreator-ai.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adcreator-ai.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://adcreator-ai.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://adcreator-ai.com/blog
- group: auth
  href: https://artifacts.apis.io/adcreator-ai-com/security/adcreator-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adcreator-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adcreator-ai.com/
coverage:
  checked: '2026-10-31'
  detail: Pricing page provides API info but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://adcreator-ai.com/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdCreator AI is a Shopify app that uses artificial intelligence to generate advertising creatives for Facebook, Instagram, TikTok, and Google from product photos in about 60 seconds. It offers a free tier, a trial, and paid plans with multiple ad variants, and includes a tariff calculator for import duties. The platform also provides real‑time rate alerts via email, Slack, or webhook, and features tools like headline generation, ad rewriting, and brand voice assistance.
image: https://adcreator-ai.com/public/og-image.png
layout: provider
modified: '2026-10-31'
name: AdCreator AI
nav: Providers
network: true
overview: 'AdCreator AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Artificial Intelligence, Shopify, Marketing, and E-Commerce.


  AdCreator AI''s developer surface includes signup flow, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Adcreator Ai Com Plans Pricing
  plan_count: 4
  slug: adcreator-ai-com-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adcreator Ai Com Domain Security
  slug: adcreator-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: adcreator-ai-com
tags:
- Advertising
- Artificial Intelligence
- Shopify
- Marketing
- E-Commerce
- Company
website: https://adcreator-ai.com/
---
