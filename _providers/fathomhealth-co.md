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
- group: design
  href: https://artifacts.apis.io/fathomhealth-co/conformance/fathomhealth-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fathomhealth-co-conformance.yml
- group: other
  href: https://artifacts.apis.io/fathomhealth-co/hosts/fathomhealth-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fathomhealth-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/fathomhealth-co/vendors/fathomhealth-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fathomhealth-co-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://fathomhealth.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fathomhealth.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://fathomhealth.com/team
- group: auth
  href: https://artifacts.apis.io/fathomhealth-co/security/fathomhealth-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fathomhealth-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fathomhealth.com
- group: company
  title: ''
  type: Blog
  url: https://fathomhealth.com/insights
coverage:
  checked: '2026-10-22'
  detail: The provider's website is a JavaScript‑rendered single‑page app with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://fathomhealth.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Fathom provides AI-powered medical coding automation, enabling healthcare providers to code millions of charts per day with high accuracy and reduced cost. Their platform uses advanced natural language processing to extract billing information from clinical documentation, streamlining revenue cycle management and improving operational efficiency for hospitals and clinics.
layout: provider
modified: '2026-10-22'
name: Fathom
nav: Providers
network: true
overview: 'Fathom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Medical Coding, and Automation.


  Fathom''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 45.5
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fathomhealth-co/fathomhealth-co-2026-11-03T131907.png
security:
- kind: domain-security
  name: Fathomhealth Co Domain Security
  slug: fathomhealth-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fathomhealth-co
tags:
- Company
- Healthcare
- Artificial Intelligence
- Medical Coding
- Automation
website: https://fathomhealth.com
---
