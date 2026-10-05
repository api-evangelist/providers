---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blazebioscience/refs/heads/main/hosts/blazebioscience-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blazebioscience-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blazebioscience/refs/heads/main/vendors/blazebioscience-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blazebioscience-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.blazebioscience.com/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blazebioscience/refs/heads/main/security/blazebioscience-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blazebioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blazebioscience.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blazebioscience.com/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/blazebioscience
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Blaze Bioscience develops imaging agents and imaging systems for precision tumor imaging, enabling surgeons to visualize cancer tissue intraoperatively. The company focuses on fluorescence-guided surgery, offering tumor paint technology and clinical programs across multiple cancer types, with FDA Fast Track designation for tozuleristide.
layout: provider
modified: '2026-09-29'
name: Blazebioscience
nav: Providers
network: true
overview: Blazebioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Imaging, Fluorescence, and Tumor-Paint.
random_paper: 8
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blazebioscience Domain Security
  slug: blazebioscience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blazebioscience
tags:
- Company
- Biotechnology
- Imaging
- Fluorescence
- Tumor-Paint
website: https://www.blazebioscience.com
---
