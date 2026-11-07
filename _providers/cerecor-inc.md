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
  href: https://artifacts.apis.io/cerecor-inc/hosts/cerecor-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cerecor-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/cerecor-inc/vendors/cerecor-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cerecor-inc-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avalotx.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/cerecor-inc/security/cerecor-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cerecor-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avalotx.com
coverage:
  checked: '2026-10-26'
  detail: The website provides only WordPress JSON endpoints and no OpenAPI, GraphQL, or other machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.avalotx.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Cerecor Inc., now operating as Avalo Therapeutics, is a clinical-stage biotechnology company focused on developing novel IL-1β pathway inhibitors for immune-mediated inflammatory diseases. The company advances candidates such as abdakibart (AVTX-009) for hidradenitis suppurativa and AVTX-010, a long‑acting anti‑IL‑β monoclonal antibody, aiming to address unmet medical needs through innovative therapeutics.
image: https://www.avalotx.com/wp-content/uploads/2025/07/hero2.webp
layout: provider
modified: '2026-10-26'
name: Cerecor Inc.
nav: Providers
network: true
overview: Cerecor Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, IL-1β, and Clinical Stage.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
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
screenshot: https://apis.io/screenshots/cerecor-inc/cerecor-inc-2026-11-03T123714.png
security:
- kind: domain-security
  name: Cerecor Inc Domain Security
  slug: cerecor-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cerecor-inc
tags:
- Company
- Biotechnology
- Therapeutics
- IL-1β
- Clinical Stage
website: https://www.avalotx.com
---
