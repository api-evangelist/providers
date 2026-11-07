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
  href: https://artifacts.apis.io/skydda/hosts/skydda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skydda-hosts.yml
- group: other
  href: https://artifacts.apis.io/skydda/vendors/skydda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skydda-vendors.yml
- group: auth
  href: https://artifacts.apis.io/skydda/security/skydda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skydda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skydda.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://skydda.ai/platform.html
- group: start
  title: ''
  type: GettingStarted
  url: https://skydda.ai/field-notes.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skydda.ai/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skydda.ai/terms-of-service.html
- group: company
  title: ''
  type: About
  url: https://skydda.ai/company.html
coverage:
  checked: '2026-10-24'
  detail: Platform documentation page is rendered via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://skydda.ai/platform.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Skydda provides an AI‑driven cyber‑defense platform that transforms offensive threat intelligence into actionable defensive actions. By continuously monitoring, exposing, and remediating vulnerabilities, Skydda helps enterprises stay ahead of machine‑speed attacks. The solution integrates with existing security stacks, offering attack path discovery, automated remediation, and continuous learning to improve protection over time. Founded with backing from Crane Venture Partners, Skydda aims to bring wisdom in darkness to modern security operations.
layout: provider
modified: '2026-10-24'
name: Skydda
nav: Providers
network: true
overview: 'Skydda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Artificial Intelligence, Threat Intelligence, and Defense Platform.


  Skydda''s developer surface includes documentation, getting-started guide, and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skydda/skydda-2026-11-03T143316.png
security:
- kind: domain-security
  name: Skydda Domain Security
  slug: skydda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skydda
tags:
- Company
- Cybersecurity
- Artificial Intelligence
- Threat Intelligence
- Defense Platform
website: https://skydda.ai/
---
