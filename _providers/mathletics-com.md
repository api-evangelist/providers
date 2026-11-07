---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/mathletics-com/vendors/mathletics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mathletics-com-vendors.yml
- group: other
  href: https://artifacts.apis.io/mathletics-com/hosts/mathletics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mathletics-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.mathletics.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://mathletics.com/blog
- group: auth
  href: https://artifacts.apis.io/mathletics-com/security/mathletics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mathletics-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mathletics.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://knowledgebase.mathletics.com/mcp
  - status: 200
    url: http://mathletics.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: 3P Learning Pty, operating under the brand Mathletics, provides an online mathematics learning platform for students worldwide. Founded in 2005, the company offers curriculum‑aligned games, assessments and teacher tools to support classroom and home learning, serving millions of users across schools and families.
image: https://www.mathletics.com/uk/wp-content/uploads/sites/1/mathletics-logo@1x.svg
layout: provider
modified: '2026-10-22'
name: 3P Learning Pty
nav: Providers
network: true
overview: '3P Learning Pty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Math, E-Learning, K-12, and Software-as-a-Service.


  3P Learning Pty''s developer surface includes support, engineering blog, and 4 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mathletics-com/mathletics-com-2026-11-03T135353.png
security:
- kind: domain-security
  name: Mathletics Com Domain Security
  slug: mathletics-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mathletics-com
tags:
- Education
- Math
- E-Learning
- K-12
- Software-as-a-Service
website: https://www.mathletics.com/
---
