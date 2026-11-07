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
- group: agent
  href: https://artifacts.apis.io/golden-state-medical-supply/llms/golden-state-medical-supply-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/golden-state-medical-supply-llms.txt
- group: other
  href: https://artifacts.apis.io/golden-state-medical-supply/hosts/golden-state-medical-supply-hosts.yml
  title: ''
  type: Hosts
  url: hosts/golden-state-medical-supply-hosts.yml
- group: other
  href: https://artifacts.apis.io/golden-state-medical-supply/vendors/golden-state-medical-supply-vendors.yml
  title: ''
  type: Vendors
  url: vendors/golden-state-medical-supply-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gsms.us/privacy-policy-2/
- group: auth
  href: https://artifacts.apis.io/golden-state-medical-supply/security/golden-state-medical-supply-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/golden-state-medical-supply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gsms.us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://gsms.us
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Golden State Medical Supply (GSMS) is a pharmaceutical distributor and packaging solutions provider based in the United States. Founded by veteran entrepreneurs, GSMS focuses on delivering high‑quality generic medicines, custom labeling, and flexible package sizes to meet diverse customer needs. The company emphasizes regulatory compliance, reliable supply chains, and responsive customer service, positioning itself as a trusted partner for pharmacies, hospitals, and healthcare providers across the nation.
image: https://gsms.us/wp-content/uploads/2025/12/GSMS_2023_TM_Final_2C_Logo-Medium-1.png
layout: provider
modified: '2026-10-22'
name: Golden State Medical Supply
nav: Providers
network: true
overview: Golden State Medical Supply is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Distribution, Packaging, and Healthcare.
random_paper: 5
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.0
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/golden-state-medical-supply/golden-state-medical-supply-2026-11-03T132916.png
security:
- kind: domain-security
  name: Golden State Medical Supply Domain Security
  slug: golden-state-medical-supply-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: golden-state-medical-supply
tags:
- Company
- Pharmaceuticals
- Distribution
- Packaging
- Healthcare
website: https://gsms.us
---
