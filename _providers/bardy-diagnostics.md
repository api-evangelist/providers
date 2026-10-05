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
  href: https://raw.githubusercontent.com/api-evangelist/bardy-diagnostics/refs/heads/main/hosts/bardy-diagnostics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bardy-diagnostics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bardy-diagnostics/refs/heads/main/vendors/bardy-diagnostics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bardy-diagnostics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bardy-diagnostics/refs/heads/main/security/bardy-diagnostics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bardy-diagnostics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bardydx.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bardydx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bardydx.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.bardydx.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.bardydx.com/contact/
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at common API endpoints.
  evidence:
  - status: dns_error
    url: https://api.bardydx.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bardy Diagnostics provides ambulatory ECG monitoring solutions, including the CAM Patch and BDxCONNECT platforms, enabling continuous cardiac rhythm tracking for patients and clinicians. The company focuses on remote cardiac diagnostics, offering detailed reports, arrhythmia detection, and integration with healthcare professional workflows. As part of Baxter’s portfolio, Bardy Diagnostics delivers innovative, FDA‑cleared technologies for real‑time cardiac monitoring and data analytics.
image: https://www.bardydx.com/wp-content/uploads/2024/12/BDx-Remote-Monitoring.png
layout: provider
modified: '2026-09-27'
name: Bardy Diagnostics
nav: Providers
network: true
overview: 'Bardy Diagnostics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Cardiology, Diagnostics, and Remote Monitoring.


  Bardy Diagnostics'' developer surface includes support and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bardy Diagnostics Domain Security
  slug: bardy-diagnostics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bardy-diagnostics
tags:
- Company
- Healthcare
- Cardiology
- Diagnostics
- Remote Monitoring
website: https://www.bardydx.com
---
