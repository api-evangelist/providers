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
  href: https://artifacts.apis.io/sorriso-pharmaceuticals/hosts/sorriso-pharmaceuticals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sorriso-pharmaceuticals-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sorrisopharma.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://sorrisopharma.com/news/
- group: auth
  href: https://artifacts.apis.io/sorriso-pharmaceuticals/security/sorriso-pharmaceuticals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sorriso-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sorrisopharma.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.sorrisopharma.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Sorriso Pharmaceuticals is a biopharmaceutical company focused on developing innovative therapies for rare diseases and unmet medical needs. The company operates a modern website (sorrisopharma.com) that provides corporate information, product pipelines, research initiatives, and investor relations. While detailed API specifications are not publicly listed, the organization maintains a professional online presence reflecting its commitment to scientific advancement and patient care.
layout: provider
modified: '2026-10-22'
name: Sorriso Pharmaceuticals
nav: Providers
network: true
overview: Sorriso Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Healthcare, Pharmaceuticals, and Research.
random_paper: 20
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.1
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
screenshot: https://apis.io/screenshots/sorriso-pharmaceuticals/sorriso-pharmaceuticals-2026-11-03T143545.png
security:
- kind: domain-security
  name: Sorriso Pharmaceuticals Domain Security
  slug: sorriso-pharmaceuticals-domain-security
  summary_line: DMARC
slug: sorriso-pharmaceuticals
tags:
- Company
- Biopharma
- Healthcare
- Pharmaceuticals
- Research
website: https://www.sorrisopharma.com/
---
