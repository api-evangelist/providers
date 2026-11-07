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
  href: https://artifacts.apis.io/quince-therapeutics/hosts/quince-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quince-therapeutics-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://irulya.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://ir.irulya.com/investors/news/
- group: other
  title: ''
  type: Leadership
  url: https://irulya.com/team/paul-yu/
- group: auth
  href: https://artifacts.apis.io/quince-therapeutics/security/quince-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quince-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://irulya.com/
coverage:
  checked: '2026-10-24'
  detail: The website renders its documentation via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://irulya.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: IRulya Therapeutics Inc., formerly Quince Therapeutics, focuses on developing pulmonary medicines that target disease biology directly in the lungs. Founded to deliver innovative therapies for lung diseases, the company aims to bring novel treatments to patients with unmet needs, leveraging its expertise in drug discovery and development.
image: https://irulya.com/wp-content/uploads/2026/10/IRulya_TM-OG.jpg
layout: provider
modified: '2026-10-23'
name: Quince Therapeutics
nav: Providers
network: true
overview: Quince Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pulmonary Therapeutics, mTOR, and Clinical Trials.
random_paper: 19
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.7
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
screenshot: https://apis.io/screenshots/quince-therapeutics/quince-therapeutics-2026-11-03T141842.png
security:
- kind: domain-security
  name: Quince Therapeutics Domain Security
  slug: quince-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quince-therapeutics
tags:
- Pulmonary Therapeutics
- mTOR
- Clinical Trials
website: https://irulya.com/
---
