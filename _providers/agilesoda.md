---
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-14'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agilesoda/refs/heads/main/security/agilesoda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agilesoda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agilesoda.ai/
- group: docs
  title: ''
  type: Documentation
  url: http://docs.agilesoda.ai/agiledocs_ko
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgileSoda
- group: operate
  title: ''
  type: Support
  url: https://agilesoda.ai/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agilesoda
- group: company
  title: ''
  type: Careers
  url: https://agilesoda.ai/company?tab=careers
- group: company
  title: ''
  type: News
  url: https://agilesoda.ai/resources?tab=news
- group: company
  title: ''
  type: InvestorRelations
  url: https://agilesoda.ai/ir
- group: commercial
  title: ''
  type: LegalNotice
  url: https://agilesoda.ai/ethics
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agilesoda/refs/heads/main/llms/agilesoda-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agilesoda-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agilesoda/refs/heads/main/packages/agilesoda-packages.yml
  title: ''
  type: Packages
  url: packages/agilesoda-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agilesoda/refs/heads/main/plans/agilesoda-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agilesoda-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agilesoda/refs/heads/main/rate-limits/agilesoda-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agilesoda-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: AgileSoDA's documentation portal at docs.agilesoda.ai publicly lists a ModelServant "API Guide" and a Developer's Guide for each of its five documented products, but every one of those pages returns the portal's username/password sign-on form instead of content, so the only API contract the company publishes is readable only by existing customers.
  evidence:
  - status: 200
    url: http://docs.agilesoda.ai/agiledocs_ko
  - status: 200
    url: http://docs.agilesoda.ai/msvt_api_v100
  - status: 200
    url: http://docs.agilesoda.ai/twreader_develop_v220
  - status: 404
    url: https://agilesoda.ai/openapi.json
  - status: 404
    url: https://agilesoda.ai/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-09-12'
description: 'AgileSoDA (애자일소다) is a Seoul-based enterprise AI software company founded in April 2015, whose name combines "Agility" with "Software Defined AI". It builds agentic AI systems that automate and optimize complex business decisions for Korean enterprises across insurance, banking, manufacturing and the public sector. Its current line is organized around the JT (Just Type) platform — JT Foundry for deploying and operating agents, JT Solution, Agentic OCR (ETL with VLM), Agentic RAG, Agentic Ops, the insurance-document extractor InsuDoc, Ground Forge for automated data annotation and a vibe-coding UI Package — alongside earlier products SparklingSoDA, BakingSoDA (reinforcement-learning decision agents), TwinDoc, TwinReader OCR and ModelServant. The company was named a Gartner Cool Vendor in 2024. Software is delivered as licensed, customer-deployed enterprise systems rather than a public cloud API: AgileSoDA publishes a product documentation portal at docs.agilesoda.ai that includes
  a ModelServant API Guide and per-product Developer''s Guides, but every guide sits behind a login, and no public OpenAPI, SDK, package or self-service developer program was found.'
image: https://agilesoda.ai/images/logo/logo_OG.png
layout: provider
modified: '2026-09-12'
name: AgileSoDA
nav: Providers
network: true
overview: 'AgileSoDA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Machine-Learning, and Enterprise Software.


  AgileSoDA''s developer surface includes documentation, support, product news, and 11 more developer resources.'
plans:
- name: Agilesoda Plans Pricing
  plan_count: 0
  slug: agilesoda-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Agilesoda Rate Limits
  slug: agilesoda-rate-limits
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agilesoda Domain Security
  slug: agilesoda-domain-security
  summary_line: TLSv1.3
slug: agilesoda
tags:
- Company
- Artificial Intelligence
- AI Agents
- Machine-Learning
- Enterprise Software
- Document Processing
- Optical Character Recognition
- Retrieval Augmented Generation
- Reinforcement Learning
- Insurance
- South Korea
website: https://agilesoda.ai/
---
