---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://rhizomeai.com/api
  baseurl_source: declared
  description: Search and retrieve regulatory and clinical documents.
  name: Rhizome Ai Documents API
  slug: rhizome-ai-documents-api
artifact_total: 10
collections:
- collection_type: open
  name: Rhizome AI Documents API
  slug: open-rhizome-ai-documents-api
common:
- group: commercial
  href: https://artifacts.apis.io/rhizome-ai/plans/rhizome-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rhizome-ai-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://rhizomeai.com/articles
- group: auth
  href: https://artifacts.apis.io/rhizome-ai/security/rhizome-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rhizome-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/rhizome-ai/well-known/rhizome-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rhizome-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/rhizome-ai/mcp/rhizome-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rhizome-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rhizome-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rhizome-ai/errors/rhizome-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rhizome-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rhizome-ai/conventions/rhizome-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rhizome-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/rhizome-ai/conformance/rhizome-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rhizome-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/rhizome-ai/data-model/rhizome-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rhizome-ai-data-model.yml
- group: other
  href: https://artifacts.apis.io/rhizome-ai/overlays/rhizome-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rhizome-ai-openapi-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/rhizome-ai/openapi/_original/rhizome-ai-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/rhizome-ai-openapi.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rhizomeai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rhizomeai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rhizomeai.com/api-reference/search
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rhizomeai.com/introduction
- group: auth
  href: https://artifacts.apis.io/rhizome-ai/authentication/rhizome-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rhizome-ai-authentication.yml
- group: operate
  href: https://artifacts.apis.io/rhizome-ai/rate-limits/rhizome-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rhizome-ai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/rhizome-ai/llms/rhizome-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rhizome-ai-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:support@rhizomeai.com
- group: commercial
  title: ''
  type: Pricing
  url: https://rhizomeai.com
- group: start
  title: ''
  type: SignUp
  url: https://rhizomeai.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://rhizomeai.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rhizomeai.com/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rhizomeai.com/privacypolicy
- group: company
  title: ''
  type: Website
  url: https://rhizomeai.com
created: '2026-07-17'
description: Rhizome AI is an AI-powered regulatory research platform for pharmaceutical and medical device companies. It lets regulatory affairs teams ask questions and receive cited answers grounded in primary-source documents from health authorities worldwide (FDA, EMA, Health Canada, Swissmedic, MHRA, TGA and others across 10+ agencies), retrieving from up to a thousand documents without hallucinating. Beyond the web application, Rhizome AI publishes an enterprise HTTP API that exposes BM25 keyword search across the regulatory document corpus and full-text, page-by-page document retrieval, authenticated with an x-api-key header. A YC-backed company, Rhizome AI was surfaced as a portfolio-company lead and enriched from its public developer documentation.
finops:
- has_sources: true
  method: derived
  name: Rhizome Ai Finops
  primary_unit: seat
  service_category: ''
  slug: rhizome-ai-finops
  template: false
image: https://rhizomeai.com/favicon.ico
layout: provider
modified: '2026-10-06'
name: Rhizome Ai
nav: Providers
network: true
overview: 'Rhizome Ai publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Documents API. Tagged areas include Company, Regulatory, Pharmaceuticals, Medical Devices, and Life Sciences.


  The Rhizome Ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Rhizome Ai''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, support, pricing, and 19 more developer resources.'
plans:
- name: Rhizome Ai Plans Pricing
  plan_count: 5
  slug: rhizome-ai-plans-pricing
- name: Rhizome Ai Price Estimates
  plan_count: 0
  slug: rhizome-ai-price-estimates
random_paper: 5
rate_limits:
- limit_count: 1
  name: Rhizome Ai Rate Limits
  slug: rhizome-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Rhizome Ai API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: rhizome-ai-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 15.5
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 43.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rhizome-ai/rhizome-ai-2026-08-17T081552.png
security:
- kind: authentication
  name: Rhizome Ai Authentication
  slug: rhizome-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rhizome Ai Domain Security
  slug: rhizome-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Search and retrieve regulatory documents
  slug: rhizome-ai-search-and-retrieve
slug: rhizome-ai
tags:
- Company
- Regulatory
- Pharmaceuticals
- Medical Devices
- Life Sciences
- Document Search
- Artificial Intelligence
- Compliance
website: https://rhizomeai.com
---
