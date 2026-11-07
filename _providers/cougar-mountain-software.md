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
  href: https://artifacts.apis.io/cougar-mountain-software/hosts/cougar-mountain-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cougar-mountain-software-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cougarmtn.com/terms-privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.cougarmtn.com/blog/tag/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cougarmtn.com
- group: company
  title: ''
  type: Blog
  url: https://www.cougarmtn.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.cougarmtn.com/
- group: auth
  href: https://artifacts.apis.io/cougar-mountain-software/security/cougar-mountain-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cougar-mountain-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cougarmtn.com/
coverage:
  checked: '2026-10-27'
  detail: Developer portal at https://dev.cougarmtn.com provides marketing pages but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://dev.cougarmtn.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Cougar Mountain Software provides on-premise accounting software solutions tailored for small businesses, nonprofits, and government entities. Their product suite includes Denali Web, Denali Fund, Denali Business, and Denali Payroll, offering comprehensive bookkeeping, fund accounting, payroll processing, and productivity tools. The company emphasizes fraud prevention, compliance, and flexible deployment options, serving a range of industries from nonprofits to township governments.
image: https://www.cougarmtn.com/wp-content/uploads/2026/06/CMS-Image-Migrate-2-01.png
layout: provider
modified: '2026-10-27'
name: Cougar Mountain Software
nav: Providers
network: true
overview: 'Cougar Mountain Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Software, Non-Profit, Small Business, and Government.


  Cougar Mountain Software''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cougar-mountain-software/cougar-mountain-software-2026-11-03T125432.png
security:
- kind: domain-security
  name: Cougar Mountain Software Domain Security
  slug: cougar-mountain-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cougar-mountain-software
tags:
- Accounting
- Software
- Non-Profit
- Small Business
- Government
- On-Premises
website: https://cougarmtn.com/
---
