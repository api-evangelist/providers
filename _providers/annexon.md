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
  href: https://artifacts.apis.io/annexon/hosts/annexon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/annexon-hosts.yml
- group: other
  href: https://artifacts.apis.io/annexon/vendors/annexon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/annexon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://annexonbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://annexonbio.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/annexon/security/annexon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/annexon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://annexonbio.com
coverage:
  checked: '2026-10-22'
  detail: No public developer documentation or API specifications were found on the company's website.
  evidence:
  - status: 404
    url: https://www.annexon.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Annexon Biosciences develops therapies that target the classical complement pathway by inhibiting C1q. The company focuses on treating autoimmune, neurodegenerative, and ophthalmic diseases, and has advanced a first‑in‑class C1q‑blocking antibody, ANX005, into a pivotal Phase 3 trial for Guillain‑Barré syndrome. Its pipeline includes early complement inhibitors for conditions of the body, brain, and eye.
image: https://annexonbio.com/wp-content/uploads/2025/05/Annexon.webp
layout: provider
modified: '2026-10-22'
name: Annexon
nav: Providers
network: true
overview: Annexon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Autoimmune Diseases, Neurodegenerative Diseases, and Ophthalmic diseases.
random_paper: 15
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.9
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
screenshot: https://apis.io/screenshots/annexon/annexon-2026-11-03T120844.png
security:
- kind: domain-security
  name: Annexon Domain Security
  slug: annexon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: annexon
tags:
- Autoimmune Diseases
- Neurodegenerative Diseases
- Ophthalmic diseases
website: https://annexonbio.com
---
