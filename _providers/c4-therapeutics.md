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
api_count: 1
apis:
- description: API information for C4 Therapeutics is documented on their "Our Science" page.
  name: C4 Therapeutics API
  slug: c4-therapeutics-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/c4-therapeutics/hosts/c4-therapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/c4-therapeutics-hosts.yml
- group: other
  href: https://artifacts.apis.io/c4-therapeutics/vendors/c4-therapeutics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/c4-therapeutics-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://c4therapeutics.com/terms-of-use-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://c4therapeutics.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/c4-therapeutics/security/c4-therapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/c4-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://c4therapeutics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://c4therapeutics.com/our-science/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.c4therapeutics.com/
- group: operate
  title: ''
  type: PressReleases
  url: https://ir.c4therapeutics.com/press-releases
- group: company
  title: ''
  type: Blog
  url: https://c4therapeutics.com/life-at-c4t/
coverage:
  checked: '2026-10-06'
  detail: The provider's documentation is HTML only with no machine‑readable OpenAPI, GraphQL or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://c4therapeutics.com/our-science/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: C4 Therapeutics is a biopharmaceutical company focused on developing novel targeted protein degradation therapies for cancer. The company leverages its proprietary TORPEDO® platform to discover and advance degraders such as CFT8919 and Cemsidomide, aiming to address unmet medical needs. It provides information for patients, healthcare providers, investors, and partners through its corporate website and investor relations portal.
layout: provider
modified: '2026-10-06'
name: C4 Therapeutics
nav: Providers
network: true
overview: 'C4 Therapeutics is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Cancer, Targeted Protein Degradation, and TORPEDO Platform.


  C4 Therapeutics'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 54.5
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/c4-therapeutics/c4-therapeutics-2026-11-03T122915.png
security:
- kind: domain-security
  name: C4 Therapeutics Domain Security
  slug: c4-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: c4-therapeutics
tags:
- Company
- Biopharma
- Cancer
- Targeted Protein Degradation
- TORPEDO Platform
website: https://c4therapeutics.com/
---
