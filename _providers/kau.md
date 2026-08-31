---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: King Abdulaziz University operates an institutional single sign-on portal (sso.kau.edu.sa) and an Oracle Access Manager federation login endpoint (iam.kau.edu.sa/oamsso-bin/login-fed.pl). These provid
  name: KAU Single Sign-On / Identity Federation
  slug: identity-sso
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kau-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kau.edu.sa/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kau.edu.sa/page/open-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/king-abdulaziz-university
- group: company
  title: ''
  type: Twitter
  url: https://x.com/kauedu_sa
- group: auth
  title: ''
  type: Authentication
  url: https://sso.kau.edu.sa/
- group: commercial
  title: ''
  type: Plans
  url: plans/kau-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kau-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kau-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'King Abdulaziz University (KAU) is a large public research university in Jeddah, Saudi Arabia, ranked #149 in the QS World University Rankings 2025, serving over 100,000 students across 33+ faculties and institutes. Its public web presence runs on the official kau.edu.sa (.gov.sa) domain and includes a beta "Open Data" page, a library/Deanship of Library Affairs portal, and a King Abdulaziz Scientific Platform. KAU operates gated identity infrastructure (an SSO portal at sso.kau.edu.sa and an Oracle Access Manager federation endpoint at iam.kau.edu.sa) but, as of this review, publishes no openly documented, self-service developer API, API reference, or developer portal. There is no official KAU GitHub organization; only a student-run Google Developer Student Club and individual academic projects are present on GitHub.'
finops:
- name: Kau Finops
  service_category: Education
  slug: kau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kau.png
jsonld:
- class_count: 6
  name: Kau Context
  property_count: 2
  slug: kau-context
layout: provider
modified: '2026-06-03'
name: King Abdulaziz University
nav: Providers
network: true
overview: 'King Abdulaziz University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Saudi Arabia.


  The King Abdulaziz University catalog on APIs.io includes 1 JSON-LD context.


  King Abdulaziz University''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Kau Plans Pricing
  plan_count: 2
  slug: kau-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Kau Rate Limits
  slug: kau-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 15.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kau/refs/heads/main/screenshots/kau-2026-06-20T183925.png
security:
- kind: domain-security
  name: Kau Domain Security
  slug: kau-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: kau
tags:
- Education
- Higher Education
- University
- Research
- Saudi Arabia
- Middle East
website: https://www.kau.edu.sa/en
---
