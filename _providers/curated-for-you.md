---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Companies API from Curated for You — 1 operation(s) for companies.
  name: Curated for You Companies API
  slug: curated-for-you-companies-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Curations API from Curated for You — 1 operation(s) for curations.
  name: Curated for You Curations API
  slug: curated-for-you-curations-api
- baseURL: https://api.curatedforyou.io
  baseurl_source: declared
  description: The Users API from Curated for You — 1 operation(s) for users.
  name: Curated for You Users API
  slug: curated-for-you-users-api
artifact_total: 14
collections:
- collection_type: open
  name: Curated for You Chronicle API
  slug: open-curated-for-you-chronicle-api
- collection_type: open
  name: Curated for You Chronicle Companies API
  slug: open-curated-for-you-companies-api
- collection_type: open
  name: Curated for You Chronicle Curations API
  slug: open-curated-for-you-curations-api
- collection_type: open
  name: Curated for You Chronicle Feedback API
  slug: open-curated-for-you-feedback-api
- collection_type: open
  name: Curated for You Chronicle shopify API
  slug: open-curated-for-you-shopify-api
- collection_type: open
  name: Curated for You Chronicle Users API
  slug: open-curated-for-you-users-api
common:
- group: other
  href: https://artifacts.apis.io/curated-for-you/overlays/curated-for-you-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/curated-for-you-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://curatedforyou.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.curatedforyou.io/redoc
- group: company
  title: ''
  type: Blog
  url: https://www.curatedforyou.io/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.curatedforyou.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curatedforyou.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curatedforyou.io/privacy-policy-1
- group: auth
  href: https://artifacts.apis.io/curated-for-you/authentication/curated-for-you-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curated-for-you-authentication.yml
- group: design
  href: https://artifacts.apis.io/curated-for-you/conventions/curated-for-you-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curated-for-you-conventions.yml
- group: design
  href: https://artifacts.apis.io/curated-for-you/errors/curated-for-you-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/curated-for-you-problem-types.yml
- group: design
  href: https://artifacts.apis.io/curated-for-you/conformance/curated-for-you-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curated-for-you-conformance.yml
- group: design
  href: https://artifacts.apis.io/curated-for-you/data-model/curated-for-you-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curated-for-you-data-model.yml
- group: design
  href: https://artifacts.apis.io/curated-for-you/lifecycle/curated-for-you-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/curated-for-you-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/curated-for-you/mcp/curated-for-you-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/curated-for-you-mcp.yml
- group: agent
  href: https://artifacts.apis.io/curated-for-you/llms/curated-for-you-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/curated-for-you-llms.txt
- group: agent
  href: https://artifacts.apis.io/curated-for-you/well-known/curated-for-you-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curated-for-you-well-known.yml
- group: auth
  href: https://artifacts.apis.io/curated-for-you/security/curated-for-you-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curated-for-you-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/curated-for-you/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Curated for You is an Austin, Texas lifestyle-commerce platform (Techstars-backed) that matches retail products to shoppers' lifestyles — places, affinities, and trends — using a taxonomy of 1,000+ lifestyle concepts and AI to power product discovery across storefronts, Shopify, web, social, email, and organic search. The company works with retailers such as REVOLVE, Steve Madden, and Saks Off 5th, and has partnered with Microsoft to bring AI-powered curations into Copilot. The Curated for You API (v2, OpenAPI 3.1) lets integrators authenticate, discover the companies they can access, retrieve curations and exported curation snapshots, submit product feedback, and manage Shopify store installs, collections, and analysis/resync jobs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curated-for-you.png
layout: provider
modified: '2026-07-18'
name: Curated for You
nav: Providers
network: true
overview: 'Curated for You publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Companies API, Curations API, and Users API. Tagged areas include Company, E-Commerce, Retail, Product Discovery, and Personalization.


  The Curated for You catalog on APIs.io includes 1 Spectral governance ruleset.


  Curated for You''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Curated for You API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: curated-for-you-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 42.8
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 33.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 30.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/curated-for-you/curated-for-you-2026-07-25T210930.png
security:
- kind: authentication
  name: Curated For You Authentication
  slug: curated-for-you-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Curated For You Domain Security
  slug: curated-for-you-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Retrieve a company's curations
  slug: curated-for-you-retrieve-curations
- name: Sync and analyze a Shopify store's collections
  slug: curated-for-you-shopify-sync
slug: curated-for-you
tags:
- Company
- E-Commerce
- Retail
- Product Discovery
- Personalization
- Artificial Intelligence
- Curation
- Shopify
- Lifestyle Commerce
website: https://curatedforyou.io/
---
