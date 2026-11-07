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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/r92m-com/hosts/r92m-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/r92m-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/r92m-com/vendors/r92m-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/r92m-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.route92medical.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.route92medical.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.route92medical.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.route92medical.com/about-us/leadership/
- group: auth
  href: https://artifacts.apis.io/r92m-com/security/r92m-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/r92m-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://r92m.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://r92m.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Route 92 Medical (R92m) is a healthcare technology company focused on providing innovative medical solutions and services. The company operates a platform that connects patients, providers, and payers to streamline medical logistics, improve care coordination, and enhance patient outcomes. Founded with backing from Norwest Venture Partners, Route 92 Medical leverages modern technology to address challenges in the medical industry.
layout: provider
modified: '2026-10-26'
name: R92m
nav: Providers
network: true
overview: R92m is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Technology, Platform, and Medical.
random_paper: 22
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/r92m-com/r92m-com-2026-11-03T141854.png
security:
- kind: domain-security
  name: R92M Com Domain Security
  slug: r92m-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: r92m-com
tags:
- Company
- Healthcare
- Technology
- Platform
- Medical
website: https://r92m.com
---
