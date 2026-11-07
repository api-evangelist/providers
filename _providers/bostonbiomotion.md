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
  href: https://artifacts.apis.io/bostonbiomotion/well-known/bostonbiomotion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bostonbiomotion-well-known.yml
- group: other
  href: https://artifacts.apis.io/bostonbiomotion/hosts/bostonbiomotion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bostonbiomotion-hosts.yml
- group: other
  href: https://artifacts.apis.io/bostonbiomotion/vendors/bostonbiomotion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bostonbiomotion-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://proteusmotion.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://proteusmotion.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/proteusmotion
- group: auth
  href: https://artifacts.apis.io/bostonbiomotion/security/bostonbiomotion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bostonbiomotion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proteusmotion.com
coverage:
  checked: '2026-10-03'
  detail: All attempted OpenAPI spec URLs on the API host returned 404, and no documentation host was identified.
  evidence:
  - status: 404
    url: https://api.proteusmotion.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Bostonbiomotion, now operating under the brand Proteus, provides advanced biomechanical measurement solutions for strength and power assessment. Their platform combines hardware sensors with cloud analytics to deliver real‑time performance insights for athletes, clinicians, and fitness facilities. The company focuses on sports performance, physical therapy, and training environments, offering products that capture motion data and translate it into actionable metrics for improving training outcomes.
image: https://proteusmotion.com/wp-content/uploads/2022/09/Moving-Proteus_wScreen-1024x576.webp
layout: provider
modified: '2026-10-03'
name: Bostonbiomotion
nav: Providers
network: true
overview: 'Bostonbiomotion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Bostonbiomotion''s developer surface includes support and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 2.6
  previous_composite: 7.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bostonbiomotion/bostonbiomotion-2026-11-03T122325.png
security:
- kind: domain-security
  name: Bostonbiomotion Domain Security
  slug: bostonbiomotion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bostonbiomotion
tags:
- Company
website: https://proteusmotion.com
---
