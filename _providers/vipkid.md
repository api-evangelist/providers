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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vipkid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vipkid.com/
- group: company
  title: ''
  type: About
  url: https://www.vipkid.com/mkt/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.vipkid.com/mkt/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.vipkid.com/mkt/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.vipkid.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vipkid.com/landing/teach-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vipkid.com/landing/teach-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VIPKID-OpenSource
- group: build
  title: ''
  type: Packages
  url: packages/vipkid-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vipkid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vipkid-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vipkid-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/vipkid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vipkid-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: VIPKid ships only consumer apps and a teacher portal — there is no developer subdomain at all (developer/docs/developers/openapi .vipkid.com and .vipkid.com.cn all fail to resolve), /openapi.json and /swagger.json return 404 or 502 on all nine VIPKid and VIPTeacher hosts, and every /.well-known/* request on the main domains is 302'd to Akamai's domain-control-validation host rather than answered with a document.
  evidence:
  - status: 404
    url: https://api.vipkid.com/openapi.json
  - status: 502
    url: https://www.vipkid.com/openapi.json
  - status: 302
    url: https://www.vipkid.com/.well-known/security.txt
  - status: 404
    url: https://www.vipteacher.com/.well-known/agent-card.json
  - status: 404
    url: https://open.vipkid.com.cn/swagger.json
  - status: 500
    url: https://blog.vipkid.com/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: VIPKid (Beijing Dami Technology Co., Ltd. / 北京大米科技有限公司) is an online language-education company founded in 2013 that connects children with English teachers over one-to-one live video lessons, and runs a global teacher-marketplace side (VIPTeacher) alongside consumer learning brands including Lingo Bus, VIPKID AI 双师智学, VIPKID 国际教育 and the Dino parent-child reading rooms. The product is delivered entirely as consumer web and mobile apps and a teacher portal; VIPKid publishes no public developer program, API reference, or machine-readable contract of any kind.
image: https://img.vipkidstatic.com/teacher/FBShare_Image_1200x630.png
layout: provider
modified: '2026-09-04'
name: VIPKid
nav: Providers
network: true
overview: 'VIPKid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Language Learning.


  VIPKid''s developer surface includes support, signup flow, and 13 more developer resources.'
plans:
- name: Vipkid Plans Pricing
  plan_count: 0
  slug: vipkid-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Vipkid Rate Limits
  slug: vipkid-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 17.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 44.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Vipkid Domain Security
  slug: vipkid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vipkid
tags:
- Company
- Education
- EdTech
- Online Learning
- Language Learning
- English Language Teaching
- Tutoring
- K-12
- Consumer
- China
website: https://www.vipkid.com/
---
