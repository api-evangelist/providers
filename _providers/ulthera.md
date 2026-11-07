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
  href: https://artifacts.apis.io/ulthera/hosts/ulthera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ulthera-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ulthera/security/ulthera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ulthera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ultherapy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ultherapy.com/
- group: operate
  title: ''
  type: Support
  url: https://ultherapy.com/find-a-provider/
created: '2026-10-22'
description: Ulthera is a medical aesthetics company that offers non‑invasive skin lifting treatments using ultrasound technology. Their flagship product, Ultherapy, delivers natural‑looking lifts by stimulating collagen production without surgery. The company provides patient resources, physician information, and a global network of certified providers. Ultherapy’s technology is FDA‑cleared and used worldwide for facial rejuvenation and skin tightening.
image: https://ultherapy.com/app/uploads/2020/02/ULT_MetadataCard_0.0_Homepage.png
layout: provider
modified: '2026-10-22'
name: Ulthera
nav: Providers
network: true
overview: 'Ulthera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Aesthetics, Skin, and Ultrasound.


  Ulthera''s developer surface includes documentation, support, and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ulthera/ulthera-2026-11-03T145359.png
security:
- kind: domain-security
  name: Ulthera Domain Security
  slug: ulthera-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ulthera
tags:
- Company
- Medical
- Aesthetics
- Skin
- Ultrasound
website: https://ultherapy.com/
---
