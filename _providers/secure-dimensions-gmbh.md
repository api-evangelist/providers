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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/secure-dimensions-gmbh/hosts/secure-dimensions-gmbh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secure-dimensions-gmbh-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.secure-dimensions.de/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.secure-dimensions.de/privacy
- group: auth
  href: https://artifacts.apis.io/secure-dimensions-gmbh/security/secure-dimensions-gmbh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secure-dimensions-gmbh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.secure-dimensions.de
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.secure-dimensions.de
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Secure Dimensions GmbH provides holistic geosecurity solutions, offering services such as risk assessment, monitoring, and incident response for critical infrastructure. The company focuses on integrating physical and cyber security measures to protect assets against natural and man‑made threats. Founded in 2009, it serves clients across Europe and globally, emphasizing innovative technology and expert consultancy.
layout: provider
modified: '2026-10-23'
name: Secure Dimensions GmbH
nav: Providers
network: true
overview: Secure Dimensions GmbH is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 0
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.6
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
screenshot: https://apis.io/screenshots/secure-dimensions-gmbh/secure-dimensions-gmbh-2026-11-03T142933.png
security:
- kind: domain-security
  name: Secure Dimensions Gmbh Domain Security
  slug: secure-dimensions-gmbh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: secure-dimensions-gmbh
tags:
- Company
website: http://www.secure-dimensions.de
---
