---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/clawshow-ai/plans/clawshow-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clawshow-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/clawshow-ai/llms/clawshow-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawshow-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/clawshow-ai/hosts/clawshow-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawshow-ai-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FutuShow
- group: auth
  href: https://artifacts.apis.io/clawshow-ai/security/clawshow-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawshow-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawshow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://clawshow.ai/en
- group: commercial
  title: ''
  type: Pricing
  url: https://clawshow.ai/en#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawshow.ai/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawshow.ai/confidentialite
- group: start
  title: ''
  type: SignUp
  url: https://esign.clawshow.ai/signup?lang=fr
coverage:
  checked: '2026-11-04'
  detail: Provider's website serves HTML SPA pages and PDF guides but no OpenAPI/AsyncAPI/GraphQL spec was found at standard locations.
  evidence:
  - status: 200
    url: https://clawshow.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ClawShow provides advanced electronic signature solutions (AES, eIDAS art. 26) tailored for schools, training institutions, and SMEs. Their platform enables creation and management of school contracts, training agreements, quotes, and client contracts, hosted in France with unlimited users per enterprise plan. The service emphasizes compliance, security, and ease of use for French private schools and professional services.
image: https://clawshow.ai/android-chrome-512x512.png
layout: provider
modified: '2026-11-03'
name: ClawShow
nav: Providers
network: true
overview: 'ClawShow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Signature, Education, Software-as-a-Service, France, and Compliance.


  ClawShow''s developer surface includes documentation, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Clawshow Ai Plans Pricing
  plan_count: 1
  slug: clawshow-ai-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawshow Ai Domain Security
  slug: clawshow-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clawshow-ai
tags:
- E-Signature
- Education
- Software-as-a-Service
- France
- Compliance
website: https://clawshow.ai/
---
