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
  href: https://artifacts.apis.io/disc-medicine/hosts/disc-medicine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disc-medicine-hosts.yml
- group: other
  href: https://artifacts.apis.io/disc-medicine/vendors/disc-medicine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disc-medicine-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.discmedicine.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discmedicine.com/privacy-notice
- group: other
  title: ''
  type: Leadership
  url: https://www.discmedicine.com/team
- group: auth
  href: https://artifacts.apis.io/disc-medicine/security/disc-medicine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disc-medicine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.discmedicine.com
coverage:
  checked: '2026-10-23'
  detail: The main site redirects via JavaScript to a landing page, providing no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://disc-medicine.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Disc Medicine is a biotechnology company focused on developing novel therapies for hematologic diseases. It advances drug candidates such as Bitopertin and DISC-0974 through clinical trials, offering detailed pipeline information, patient resources, and investor relations via its corporate website.
image: https://www.discmedicine.com/images/common/og-img.png
layout: provider
modified: '2026-10-23'
name: Disc Medicine
nav: Providers
network: true
overview: Disc Medicine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Hematology, Clinical Trials, Investor Relations, and Healthcare.
random_paper: 22
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 7
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
  previous_composite: 9.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/disc-medicine/disc-medicine-2026-11-03T130752.png
security:
- kind: domain-security
  name: Disc Medicine Domain Security
  slug: disc-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: disc-medicine
tags:
- Biotechnology
- Hematology
- Clinical Trials
- Investor Relations
- Healthcare
website: https://www.discmedicine.com
---
