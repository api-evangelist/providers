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
api_count: 1
apis:
- description: API for Blue Earth Diagnostics services (no contract found)
  name: Blue Earth Diagnostics API
  slug: blue-earth-diagnostics-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-earth-diagnostics/refs/heads/main/hosts/blue-earth-diagnostics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-earth-diagnostics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-earth-diagnostics/refs/heads/main/vendors/blue-earth-diagnostics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blue-earth-diagnostics-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blueearthdiagnostics.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.blueearthdiagnostics.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.blueearthdiagnostics.com/management
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-earth-diagnostics/refs/heads/main/security/blue-earth-diagnostics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-earth-diagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blueearthdiagnostics.com/
created: '2026-09-29'
description: Blue Earth Diagnostics is a Bracco-owned company providing advanced nuclear medicine diagnostics and imaging services. It offers a range of PET, SPECT, and therapeutic radiopharmaceuticals, supporting clinical trials and research partnerships. The company focuses on innovative diagnostic solutions and collaborates with healthcare professionals worldwide.
layout: provider
modified: '2026-09-29'
name: Blue Earth Diagnostics
nav: Providers
network: true
overview: Blue Earth Diagnostics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagnostics, Nuclear Medicine, Healthcare, and Imaging.
random_paper: 0
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blue Earth Diagnostics Domain Security
  slug: blue-earth-diagnostics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: blue-earth-diagnostics
tags:
- Company
- Diagnostics
- Nuclear Medicine
- Healthcare
- Imaging
website: https://www.blueearthdiagnostics.com/
---
