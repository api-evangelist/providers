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
- group: auth
  href: https://artifacts.apis.io/caregility/well-known/caregility-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/caregility-status-security.txt
- group: agent
  href: https://artifacts.apis.io/caregility/well-known/caregility-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caregility-well-known.yml
- group: other
  href: https://artifacts.apis.io/caregility/hosts/caregility-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caregility-hosts.yml
- group: other
  href: https://artifacts.apis.io/caregility/vendors/caregility-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caregility-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.caregility.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caregility.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://caregility.com/news/
- group: company
  title: ''
  type: Blog
  url: https://caregility.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caregility
- group: auth
  href: https://artifacts.apis.io/caregility/security/caregility-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caregility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caregility.com
coverage:
  checked: '2026-10-07'
  detail: Caregivity website provides only a waitlist and no developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://caregivity.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Caregility provides a connected care platform that enables hospitals and health systems to deliver bedside virtual care, telehealth, and remote patient monitoring. Their solutions integrate with Epic and other EHRs, offering virtual nursing, AI‑enhanced clinical insights, and a suite of smart room devices to improve patient outcomes across inpatient, outpatient, home, and rural settings.
image: https://caregility.com/wp-content/uploads/2026/02/Caregility-Connecting-Care-Everywhere-1024x683.png
layout: provider
modified: '2026-10-07'
name: Caregility
nav: Providers
network: true
overview: 'Caregility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Virtual Care, and Connected Care.


  Caregility''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 21.1
  previous_composite: 11.0
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
security:
- kind: domain-security
  name: Caregility Domain Security
  slug: caregility-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caregility
tags:
- Company
- Healthcare
- Telehealth
- Virtual Care
- Connected Care
website: https://caregility.com
---
