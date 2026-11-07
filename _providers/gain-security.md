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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/gain-security/well-known/gain-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gain-security-well-known.yml
- group: other
  href: https://artifacts.apis.io/gain-security/hosts/gain-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gain-security-hosts.yml
- group: other
  href: https://artifacts.apis.io/gain-security/vendors/gain-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gain-security-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gain.security/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gain.security/privacy
- group: auth
  href: https://artifacts.apis.io/gain-security/security/gain-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gain-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gain.security
coverage:
  checked: '2026-10-24'
  detail: Gain Security website provides no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://gain.security
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Gain Security provides a comprehensive security platform that helps organizations protect their digital assets, detect threats, and respond to incidents in real time. Backed by Boldstart Ventures, the company offers solutions including vulnerability management, threat intelligence, and automated response workflows, enabling enterprises to strengthen their security posture and reduce risk across cloud, on‑premise, and hybrid environments.
image: https://gain.security/og.png
layout: provider
modified: '2026-10-24'
name: Gain Security
nav: Providers
network: true
overview: Gain Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Platform, Threat Detection, and Vulnerability Management.
random_paper: 4
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
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
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gain-security/gain-security-2026-11-03T132450.png
security:
- kind: domain-security
  name: Gain Security Domain Security
  slug: gain-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gain-security
tags:
- Company
- Security
- Platform
- Threat Detection
- Vulnerability Management
website: https://gain.security
---
