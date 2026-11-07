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
  href: https://artifacts.apis.io/mei-pharma/vendors/mei-pharma-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mei-pharma-vendors.yml
- group: other
  href: https://artifacts.apis.io/mei-pharma/hosts/mei-pharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mei-pharma-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://litestrategy.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://support.meipharma.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://litestrategy.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://litestrategy.com/media/
- group: company
  title: ''
  type: Website
  url: https://www.meipharma.com
- group: auth
  href: https://artifacts.apis.io/mei-pharma/security/mei-pharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mei-pharma-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.meipharma.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: MEI Pharma is a biotech investment firm focused on developing and commercializing innovative pharmaceutical solutions. The company originated as a venture-backed portfolio entity and has transitioned through a rebranding phase, aligning its strategic vision with emerging market opportunities in therapeutic development and digital health integration. While its prior web presence redirected to unrelated entities, MEI Pharma maintains a corporate identity distinct from Lite Strategy, emphasizing its commitment to advancing medical research and fostering partnerships across the healthcare ecosystem.
image: https://litestrategy.com/wp-content/uploads/2025/09/LITS-Metadata-02.jpg
layout: provider
modified: '2026-10-26'
name: MEI Pharma
nav: Providers
network: true
overview: 'MEI Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharma, Investment, Therapeutics, and Digital Health.


  MEI Pharma''s developer surface includes support and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.0
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
screenshot: https://apis.io/screenshots/mei-pharma/mei-pharma-2026-11-03T135440.png
security:
- kind: domain-security
  name: Mei Pharma Domain Security
  slug: mei-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mei-pharma
tags:
- Biotechnology
- Pharma
- Investment
- Therapeutics
- Digital Health
website: https://www.meipharma.com
---
