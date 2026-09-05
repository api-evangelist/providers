---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.podiumeducation.com/
- group: company
  title: ''
  type: About
  url: https://www.podiumeducation.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.podiumeducation.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.podiumeducation.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.podiumeducation.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.podiumeducation.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Podium-Education
- group: start
  title: ''
  type: SignUp
  url: https://globalcareeraccelerator.org/app/signup
- group: start
  title: ''
  type: Login
  url: https://globalcareeraccelerator.org/app/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podiumeducation
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/podium-education-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: conformance/podium-education-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/podium-education-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podium-education-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/podium-education-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podium-education-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Podium Education sells a university partnership, not software - The Global Career Accelerator is delivered on a hosted Canvas LMS estate under podedtech.com whose only public doors are the student login at globalcareeraccelerator.org/app/login and an admin sign-in at cms.prod.podedtech.com, and the corporate site has no developer, API or docs section at all.
  evidence:
  - status: 404
    url: https://www.podiumeducation.com/developers
  - status: 404
    url: https://www.podiumeducation.com/openapi.json
  - status: 404
    url: https://globalcareeraccelerator.org/.well-known/agent-card.json
  - status: 302
    url: https://cms.prod.podedtech.com/openapi.json
  - status: 302
    url: https://hq.podedtech.com/
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Podium Education is an Austin, Texas experiential-learning and career platform founded in 2018 that partners with colleges, universities and employers to close the college-to-career gap. Its flagship program, The Global Career Accelerator, is a credit-bearing, financial-aid and Pell-eligible online field experience in which undergraduates work on real brand projects in data analytics, web development, digital marketing and tech operations alongside peers in other countries, earning certificates and minors through their own institution. Podium delivers the program on its own platform stack — a hosted Canvas LMS estate and a student application at globalcareeraccelerator.org — sold to universities as a partnership rather than as software, and it publishes no public developer program, API reference or machine-readable contract.
image: https://cdn.prod.website-files.com/628e8d0a56d5555b8d2ca0b3/6298fbe54a0af2001fad3612_podium-thumb.png
layout: provider
modified: '2026-08-26'
name: Podium Education
nav: Providers
network: true
overview: 'Podium Education is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, EdTech, and Online Learning.


  Podium Education''s developer surface includes engineering blog, support, signup flow, and 13 more developer resources.'
plans:
- name: Podium Education Plans Pricing
  plan_count: 0
  slug: podium-education-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Podium Education Rate Limits
  slug: podium-education-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 17.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podium-education/refs/heads/main/screenshots/podium-education-2026-09-02T151612.png
security:
- kind: domain-security
  name: Podium Education Domain Security
  slug: podium-education-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: podium-education
tags:
- Company
- Education
- Higher Education
- EdTech
- Online Learning
- Workforce Development
- Career Services
- Learning Management
website: https://www.podiumeducation.com/
---
