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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuemath-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuemath.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cuemath.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.cuemath.com/signup/
- group: start
  title: ''
  type: Login
  url: https://leap.cuemath.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.cuemath.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.cuemath.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cuemath.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cuemath.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuemath
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuemath-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cuemath-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cuemath-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cuemath-rate-limits.yml
coverage:
  checked: '2026-08-11'
  detail: 'Cuemath ships only a consumer tutoring product: api.cuemath.com returns 404, no developer or docs subdomain resolves at all, and the single HTTP API found on its infrastructure — app.cuemath.com/api — is a session-cookie application backend that Cuemath''s own llms.txt explicitly lists under "API endpoints not meant for public access".'
  evidence:
  - status: 404
    url: https://api.cuemath.com/
  - status: 404
    url: https://www.cuemath.com/openapi.json
  - status: 401
    url: https://app.cuemath.com/api
  - status: 200
    url: https://www.cuemath.com/llms.txt
  - status: 200
    url: https://api.github.com/orgs/cuemath
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: Cuemath is an India-headquartered education technology company founded in 2013 by Manan Khurma that delivers live, one-to-one online math tutoring to students in grades K through 12 across more than 80 countries. Its MathFit framework and LEAP learning platform pair certified tutors with an interactive, gamified curriculum aligned to US Common Core standards, spanning arithmetic, algebra, geometry, pre-calculus, AP calculus and standardized test preparation. Cuemath sells directly to families as a subscription tutoring product; it operates a consumer web and mobile application rather than a developer platform, and publishes no public API, SDK or developer portal.
image: https://d138zd1ktt9iqe.cloudfront.net/static/website-v3/math-fit-teaser-16-9.webp
layout: provider
modified: '2026-08-11'
name: Cuemath
nav: Providers
network: true
overview: 'Cuemath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  Cuemath''s developer surface includes pricing, signup flow, engineering blog, support, and 10 more developer resources.'
plans:
- name: Cuemath Plans Pricing
  plan_count: 0
  slug: cuemath-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Cuemath Rate Limits
  slug: cuemath-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Cuemath Domain Security
  slug: cuemath-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cuemath
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Mathematics
- K-12
- Consumer Application
website: https://www.cuemath.com/
---
