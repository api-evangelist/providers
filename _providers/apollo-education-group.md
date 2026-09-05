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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The University of Phoenix identity provider, running ForgeRock Access Management in the /alpha realm. The OpenID Connect discovery document is served anonymously (HTTP 200, 2026-09-04) at https://logi
  name: University of Phoenix Single Sign-On (OpenID Connect / OAuth 2.0)
  slug: phoenix-sso-openid-connect
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apollo-education-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.phoenix.edu/
- group: company
  title: ''
  type: Blog
  url: https://www.phoenix.edu/blog.html
- group: operate
  title: ''
  type: Support
  url: https://www.phoenix.edu/about/contact-us.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.phoenix.edu/student-resources/faq.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.phoenix.edu/tuition-financial-aid.html
- group: start
  title: ''
  type: SignUp
  url: https://www.phoenix.edu/application/quick-app/personal-info
- group: start
  title: ''
  type: Login
  url: https://my.phoenix.edu/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phoenix.edu/copyright-legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phoenix.edu/copyright-legal/privacy-policy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apollo-education-group-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apollo-education-group-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apollo-education-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apollo-education-group-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apollo-education-group-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apollo-education-group-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apollo-education-group-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/apollo-education-group-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apollo-education-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apollo-education-group-rate-limits.yml
created: '2026-03-23'
description: 'Apollo Education Group is a private education provider that operates the University of Phoenix and other institutions offering associate''s, bachelor''s, master''s, and doctoral degree programs. The organization focuses on providing accessible higher education to working adult learners through online and in-person formats. Taken private in 2017, the group has since been renamed Phoenix Education Partners; the former apolloeducationgroup.com domain no longer serves and the live surface is the operating institution''s site at phoenix.edu. There is no public developer program: the only machine-readable contracts the group publishes are the identity documents behind its student single sign-on.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apollo-education-group.png
layout: provider
modified: '2026-09-04'
name: Apollo Education Group
nav: Providers
network: true
overview: 'Apollo Education Group publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, Online Education, Private Education, and University.


  Apollo Education Group''s developer surface includes engineering blog, support, pricing, signup flow, authentication, and 15 more developer resources.'
plans:
- name: Apollo Education Group Plans Pricing
  plan_count: 0
  slug: apollo-education-group-plans-pricing
press:
- date: '2026-05-25'
  title: Apollo-backed Phoenix Education Partners files for US IPO
  url: https://www.reuters.com/business/apollo-backed-phoenix-education-partners-files-us-ipo-2025-08-29/
- date: '2026-05-25'
  title: University of Phoenix Owner, Apollo Education Group, Will ...
  url: https://www.nytimes.com/2016/02/09/business/dealbook/apollo-education-group-university-of-phoenix-owner-to-be-taken-private.html
- date: '2026-05-25'
  title: University of Phoenix Operator Apollo Education Group to Be ...
  url: https://www.edsurge.com/news/2016-02-08-university-of-phoenix-operator-apollo-education-group-to-be-acquired-for-1-1b
- date: '2026-05-25'
  title: Peter Fitch - Apollo Education Group
  url: https://www.linkedin.com/in/peter-fitch-57a861a2
- date: '2026-05-25'
  title: Higher Education Policy News
  url: https://www.highereddive.com/topic/policy/?page=94
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apollo Education Group Rate Limits
  slug: apollo-education-group-rate-limits
scopes:
- name: Apollo Education Group Scopes
  scope_count: 7
  slug: apollo-education-group-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 2.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/apollo-education-group/refs/heads/main/screenshots/apollo-education-group-2026-06-20T172307.png
security:
- kind: authentication
  name: Apollo Education Group Authentication
  slug: apollo-education-group-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Apollo Education Group Domain Security
  slug: apollo-education-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apollo-education-group
tags:
- Education
- Higher Education
- Online Education
- Private Education
- University
website: https://www.phoenix.edu/
---
