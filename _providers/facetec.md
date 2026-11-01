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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: FaceTec provides 3D facial biometric technology via APIs for liveness detection, face matching, OCR, NFC and UR codes.
  name: FaceTec API
  slug: facetec-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/facetec/hosts/facetec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/facetec-hosts.yml
- group: other
  href: https://artifacts.apis.io/facetec/vendors/facetec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/facetec-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.facetec.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.facetec.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.facetec.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.facetec.com/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.facetec.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/facetec
- group: auth
  href: https://artifacts.apis.io/facetec/security/facetec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/facetec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://facetec.com/
coverage:
  checked: '2026-10-28'
  detail: Developer portal at https://dev.facetec.com returns HTML but no machine‑readable spec.
  evidence:
  - status: 200
    url: https://dev.facetec.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: FaceTec provides 3D facial biometric technology for liveness detection, face matching, and identity verification. Their platform enables secure onboarding, fraud prevention, and user authentication across devices using video‑selfie capture, OCR, NFC and UR codes. Trusted by enterprises for billions of checks annually, FaceTec offers SDKs and APIs for developers to integrate biometric security into web, mobile and embedded applications.
layout: provider
modified: '2026-10-28'
name: FaceTec
nav: Providers
network: true
overview: 'FaceTec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biometric, IdentityVerification, Security, SDK, and API.


  FaceTec''s developer surface includes pricing, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.1
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
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Facetec Domain Security
  slug: facetec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: facetec
tags:
- Biometric
- IdentityVerification
- Security
- SDK
- API
website: https://facetec.com/
---
