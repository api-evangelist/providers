---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: true
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Genesco Agentic Access
  operation_count: 0
  slug: genesco-agentic-access
  summary_line: 0 operations
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/security/genesco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genesco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genesco
- group: company
  title: ''
  type: Website
  url: https://www.genesco.com
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/llms/genesco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/genesco-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/agentic-access/genesco-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/genesco-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/agentic-access/genesco-agentic-access.yml
  title: ''
  type: ContentSignal
  url: agentic-access/genesco-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/conformance/genesco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/genesco-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/conventions/genesco-conventions.yml
  title: ''
  type: Conventions
  url: conventions/genesco-conventions.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/plans/genesco-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/genesco-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/genesco/refs/heads/main/rate-limits/genesco-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/genesco-rate-limits.yml
created: '2026-03-24'
description: 'Genesco is a specialty retailer and branded company selling footwear, apparel, and accessories through more than 1,400 retail stores and e-commerce sites under banners including Journeys, Schuh, Johnston & Murphy, and Genesco Brands. Genesco publishes no public API, developer portal, or OpenAPI document — it says so itself in the llms.txt it serves on journeys.com. What it does publish is an agent-access posture: an llms.txt for AI assistants, a Content-Signal AI-usage declaration in robots.txt on Journeys and Johnston & Murphy, a named allow list for AI search and user-requested agents, an llm= referral attribution convention, and server-rendered schema.org ProductGroup JSON-LD on every product page.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genesco.png
layout: provider
modified: '2026-09-12'
name: Genesco
nav: Providers
network: true
overview: Genesco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Footwear, Apparel, E-Commerce, and Agentic Access.
plans:
- name: Genesco Plans Pricing
  plan_count: 0
  slug: genesco-plans-pricing
press:
- date: ''
  title: Genesco Announces Strategic Transformation of Its ...
  url: https://www.businesswire.com/news/home/20260114870793/en/Genesco-Announces-Strategic-Transformation-of-Its-Information-Technology-Operations
- date: ''
  title: Genesco To Acquire Little Burgundy Chain From The Aldo ...
  url: https://www.prnewswire.com/news-releases/genesco-to-acquire-little-burgundy-chain-from-the-aldo-group-300171120.html
- date: ''
  title: THE BUSINESS OF GENESCO Genesco Inc. is a ...
  url: https://www.genesco.com/static-files/0d4e883c-7f40-408e-b163-9b5ac06ce192
- date: ''
  title: Genesco to Overhaul Tech and Accelerate AI-enabled ...
  url: https://www.facebook.com/footwearnews/posts/genesco-to-overhaul-tech-and-accelerate-ai-enabled-innovations-expects-job-cuts/1243652767619925/
- date: ''
  title: THOMSON REUTERS - EDITED TRANSCRIPT - Q4 2019 ...
  url: https://www.genesco.com/static-files/15de29ce-baad-457f-8d34-000574ea17fe
random_paper: 14
rate_limits:
- limit_count: 0
  name: Genesco Rate Limits
  slug: genesco-rate-limits
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 7.9
  provenance:
    agentic_access: first-party
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Genesco Domain Security
  slug: genesco-domain-security
  summary_line: TLSv1.3 · DMARC
slug: genesco
tags:
- Retail
- Footwear
- Apparel
- E-Commerce
- Agentic Access
- Fortune 1000
website: https://www.genesco.com
---
