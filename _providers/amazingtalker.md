---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://en.amazingtalker.com
  baseurl_source: spec
  description: The Pages API from AmazingTalker — 1 operation(s) for pages.
  name: AmazingTalker Pages API
  slug: amazingtalker-pages-api
artifact_total: 5
collections:
- collection_type: open
  name: Find tutors plugin Pages API
  slug: open-amazingtalker-pages-api
common:
- group: other
  href: https://artifacts.apis.io/amazingtalker/overlays/amazingtalker-find-tutors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amazingtalker-find-tutors-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/amazingtalker/well-known/amazingtalker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazingtalker-well-known.yml
- group: agent
  href: https://artifacts.apis.io/amazingtalker/mcp/amazingtalker-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/amazingtalker-mcp.yml
- group: agent
  href: https://artifacts.apis.io/amazingtalker/llms/amazingtalker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazingtalker-llms.txt
- group: auth
  href: https://artifacts.apis.io/amazingtalker/authentication/amazingtalker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazingtalker-authentication.yml
- group: design
  href: https://artifacts.apis.io/amazingtalker/conformance/amazingtalker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazingtalker-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amazingtalker/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/amazingtalker/security/amazingtalker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazingtalker-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazingTalker
- group: company
  title: ''
  type: Blog
  url: https://en.amazingtalker.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.amazingtalker.com/privacy-and-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.amazingtalker.com/privacy-and-terms
- group: company
  title: ''
  type: Website
  url: https://en.amazingtalker.com
created: '2026-07-17'
description: AmazingTalker is an online tutoring marketplace, founded in 2016 and headquartered in Taipei, that connects students with vetted professional tutors for personalized 1-on-1 lessons in more than 60 languages plus academic, music, and lifestyle subjects. Learners browse tutor profiles, compare pricing and ratings, book trial and formal lessons on a flexible pay-as-you-go basis, and meet over Zoom. AmazingTalker publicly exposes a ChatGPT-plugin OpenAPI (findTeachers) that returns bookable tutors for a subject with price, learning-need, auxiliary-language, and location filters.
image: https://en.amazingtalker.com/.well-known/logo.png
layout: provider
modified: '2026-07-17'
name: AmazingTalker
nav: Providers
network: true
overview: 'AmazingTalker publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Pages API. Tagged areas include Company, Education, Tutoring, Language Learning, and Marketplace.


  AmazingTalker''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 37.3
    developer_ergonomics: 16.1
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazingtalker/amazingtalker-2026-07-25T195910.png
security:
- kind: authentication
  name: Amazingtalker Authentication
  slug: amazingtalker-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Amazingtalker Domain Security
  slug: amazingtalker-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: Find AmazingTalker tutors
  slug: amazingtalker-find-tutors
slug: amazingtalker
tags:
- Company
- Education
- Tutoring
- Language Learning
- Marketplace
- EdTech
- Chat Gpt Plugin
website: https://en.amazingtalker.com
---
