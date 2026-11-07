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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/medzero/well-known/medzero-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/medzero-well-known.yml
- group: other
  href: https://artifacts.apis.io/medzero/hosts/medzero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/medzero-hosts.yml
- group: other
  href: https://artifacts.apis.io/medzero/vendors/medzero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/medzero-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medzero.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medzero.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://medzero.com/category/news/
- group: auth
  href: https://artifacts.apis.io/medzero/security/medzero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medzero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medzero.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://medzero.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: medZERO provides a spending account that gives employees on‑demand, zero‑interest, zero‑fee financing to pay out‑of‑pocket healthcare expenses. The service works with any benefit plan, provider, or HSA and requires no credit check, allowing employees to repay over time while employers enhance their benefits offerings. It is positioned for employers, benefits professionals, and employees seeking a smarter way to manage healthcare costs.
image: https://medzero.com/wp-content/uploads/family-enjoying-springtime-outdoors-with-kids.jpg_s1024x1024wisk20cN-kg5LPWykurTIoVDaWUIbahnc6d0tDbc15XnxBkBVU.jpg
layout: provider
modified: '2026-10-24'
name: MedZero
nav: Providers
network: true
overview: MedZero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include healthcare-financing, Employee Benefits, Financial Wellness, Spending Account, and Employer Benefits.
random_paper: 14
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/medzero/medzero-2026-11-03T135429.png
security:
- kind: domain-security
  name: Medzero Domain Security
  slug: medzero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medzero
tags:
- healthcare-financing
- Employee Benefits
- Financial Wellness
- Spending Account
- Employer Benefits
website: https://medzero.com
---
