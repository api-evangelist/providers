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
- description: API for Applied Medical resources (no public spec discovered)
  name: Applied Medical API
  slug: applied-medical-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/applied-medical-resources/refs/heads/main/hosts/applied-medical-resources-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applied-medical-resources-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appliedmedical.com/Legal/TermsOfSale
- group: operate
  title: ''
  type: Support
  url: https://support.appliedmedical.com/sp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appliedmedical.com/Legal/PrivacyPolicy
- group: company
  title: ''
  type: Newsroom
  url: https://appliedmedical.com/WhoWeAre/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/applied-medical-resources/refs/heads/main/security/applied-medical-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applied-medical-resources-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appliedmedical.com/
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.appliedmedical.com or related hosts.
  evidence:
  - status: 404
    url: https://api.appliedmedical.com/openapi.json
  - status: 404
    url: https://api.appliedmedical.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Applied Medical Resources, a division of the global Applied Medical group, designs and manufactures innovative medical devices for minimally invasive surgery across a range of specialties. The privately‑held company focuses on improving patient outcomes through advanced technology, education, and support for healthcare professionals. With a worldwide presence, it serves hospitals and clinics, offering products that enhance surgical precision, reduce recovery times, and lower overall healthcare costs while maintaining high standards of safety and efficacy.
image: https://appliedmedicalus-cdn-prd.azureedge.net/IMG/Applied-Medical-Preview-Default.png
layout: provider
modified: '2026-09-25'
name: Applied Medical Resources
nav: Providers
network: true
overview: 'Applied Medical Resources publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Devices, Healthcare, and Surgery.


  Applied Medical Resources'' developer surface includes support and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 67.9
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
  name: Applied Medical Resources Domain Security
  slug: applied-medical-resources-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applied-medical-resources
tags:
- Company
- Medical
- Devices
- Healthcare
- Surgery
website: https://appliedmedical.com/
---
