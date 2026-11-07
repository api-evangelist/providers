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
  href: https://artifacts.apis.io/added-health/hosts/added-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/added-health-hosts.yml
- group: auth
  href: https://artifacts.apis.io/added-health/security/added-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/added-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.addedhealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addedhealth.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://addedhealth.com/cookie-policy
- group: docs
  title: ''
  type: Documentation
  url: https://addedhealth.com/
coverage:
  checked: '2026-10-29'
  detail: Added Health does not provide a developer program or public API documentation.
  evidence:
  - status: 200
    url: https://www.addedhealth.com/
  - status: 0
    url: https://api.addedhealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Added Health provides private, proactive primary care services in London and Oxford, offering relationship‑based, technology‑backed clinics that focus on whole‑person health. The company emphasizes a human‑first approach, continuous learning, and personalized care without commissions or kickbacks. Their model integrates narrative intelligence to capture patient stories, aiming to improve diagnosis accuracy and deliver precise, preventive healthcare.
image: https://framerusercontent.com/assets/kaSnVdBWjJGEFhYZULpkIKefrgA.png
layout: provider
modified: '2026-10-29'
name: Added Health
nav: Providers
network: true
overview: 'Added Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, ProactiveHealth, and London.


  Added Health''s developer surface includes documentation and 5 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/added-health/added-health-2026-11-03T120243.png
security:
- kind: domain-security
  name: Added Health Domain Security
  slug: added-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: added-health
tags:
- Company
- Healthcare
- Primary Care
- ProactiveHealth
- London
- Oxford
website: https://www.addedhealth.com/
---
