---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-09-05'
api_count: 25
apis:
- baseURL: https://www.51offer.com
  baseurl_source: declared
  description: The public JSON API surface of the 51offer official study-abroad site. 51offer serves its own Swagger 1.2 resource listing and 24 resource declarations, unauthenticated, at https://www.51offer.com/api
  name: 51offer Horizon Site API
  slug: 51offer-horizon-site-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/51offer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/51offer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.51offer.com/
- group: company
  title: ''
  type: About
  url: https://www.51offer.com/aboutus/
- group: start
  title: ''
  type: SignUp
  url: https://account.51offer.com/register.html
- group: start
  title: ''
  type: Login
  url: https://account.51offer.com/login.html
- group: operate
  title: ''
  type: Support
  url: https://account.51offer.com/user/feedback.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.51offer.com/aboutus/contract.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.51offer.com/aboutus/protection.html
- group: company
  title: ''
  type: Blog
  url: https://51offer.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/51offer
- group: company
  title: ''
  type: Partners
  url: https://www.51offer.com/aboutus/cooperation.html
- group: build
  title: ''
  type: Packages
  url: packages/51offer-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/51offer-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/51offer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/51offer-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/51offer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/51offer-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/51offer-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/51offer-mcp.yml
created: '2026-09-05'
description: 51offer (Shanghai Huizhi Business Consulting Co., Ltd. / 上海汇紫商务咨询有限公司) is a Shanghai-based one-stop online study-abroad platform for Chinese students applying to universities in the United Kingdom, Australia, the United States, New Zealand, Japan and Singapore. Its consumer surface covers DIY application filing, AI/big-data school and course matching, personal-statement and document services, language training (IELTS/TOEFL), adviser and channel-partner services, a study-abroad mall with online contract signing, payment and refund flows, a GPA calculator and a student content and community section. 51offer publishes no developer program, but its official site www.51offer.com serves a public, unauthenticated Swagger 1.2 API listing at /api-docs ("Horizon Site APIConfig List / 51offer官网所有开放接口清单") describing 24 controllers and several hundred JSON operations, and that listing is the machine-readable contract profiled here.
image: https://static.51offer.com/skin/common/images/favicon.ico
layout: provider
modified: '2026-09-05'
name: 51offer
nav: Providers
network: true
overview: '51offer publishes 1 API on the [APIs.io](https://apis.io/) network: Horizon Site API. Tagged areas include Company, Education, Study Abroad, Higher Education, and University Applications.


  51offer''s developer surface includes authentication, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: 51Offer Plans Pricing
  plan_count: 0
  slug: 51offer-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: 51Offer Rate Limits
  slug: 51offer-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 17.7
    developer_ergonomics: 28.0
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 5.3
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
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 51Offer Authentication
  slug: 51offer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 51Offer Domain Security
  slug: 51offer-domain-security
  summary_line: TLSv1.2
slug: 51offer
tags:
- Company
- Education
- Study Abroad
- Higher Education
- University Applications
- Students
- Language Training
- E-Commerce
- China
- Consulting
website: https://www.51offer.com/
---
