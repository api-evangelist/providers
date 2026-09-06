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
api_count: 1
apis:
- description: 'The private Django REST API that backs the AAK Tele-Science platform. The application frontend at aakscience.com preconnects to django.aakscience.com, and the company runs a drf-yasg (Swagger) schema '
  name: AAK Tele-Science API
  slug: aak-tele-science-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aaktelescienceinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aakscience.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AAK-Tele-Science
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aak-telesciences
- group: commercial
  title: ''
  type: Pricing
  url: https://aakscience.com/subscriptions
- group: start
  title: ''
  type: SignUp
  url: https://aakscience.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://aakscience.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aakscience.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aakscience.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://aakscience.com/contact
- group: company
  title: ''
  type: Blog
  url: https://aakscience.com/newBlogs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aaktelescienceinc-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aaktelescienceinc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aaktelescienceinc-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: AAK Tele-Science runs a real Django REST API behind django.aakscience.com, but its drf-yasg schema endpoints answer "Swagger authentication required" and the production API host returns HTTP 401 with a zero-length body on every path — including a control path that does not exist — so the contract is readable only by an authenticated subscriber, and no public developer portal or reference exists to fall back to.
  evidence:
  - status: 401
    url: https://django-dev.aakscience.com/.json
  - status: 401
    url: https://django.aakscience.com/api/
  - status: 401
    url: https://django.aakscience.com/zzz-nonexistent-path-9f8a7b/
  - status: 200
    url: https://aakscience.com/sitemap.xml
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: AAK Tele-Science, Inc. (aakscience.com) is a Davis, California software company founded in 2020 that operates a cloud-based collaborative platform for the global scientific research community. The AAK platform connects researchers, institutions, service providers, venture capitalists and investors around shared research projects, layering machine-learning-assisted discovery, predictive analytics and a data-fragmentation privacy protocol over a subscription SaaS product. The platform is delivered as a React single-page application backed by a Django REST API at django.aakscience.com; that API is real but is not publicly documented — its drf-yasg schema endpoints require HTTP authentication and the production API host answers 401 to every path, so no machine-readable contract is reachable without credentials.
image: https://aakscience.com/aak.webp
layout: provider
modified: '2026-09-05'
name: AAK Tele-Science, Inc.
nav: Providers
network: true
overview: 'AAK Tele-Science, Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Science, Collaboration, and Analytics.


  AAK Tele-Science, Inc.''s developer surface includes pricing, signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Aaktelescienceinc Plans Pricing
  plan_count: 0
  slug: aaktelescienceinc-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aaktelescienceinc Rate Limits
  slug: aaktelescienceinc-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Aaktelescienceinc Domain Security
  slug: aaktelescienceinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aaktelescienceinc
tags:
- Company
- Research
- Science
- Collaboration
- Analytics
- Machine Learning
- SaaS
- Data
website: https://aakscience.com
---
