---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betterdoctor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/betterdoctor
- group: company
  title: ''
  type: Website
  url: https://betterdoctor.com
created: '2026-07-17'
description: BetterDoctor Inc. was a San Francisco health-technology company (founded 2012) that built a provider data verification and directory-accuracy platform, helping health plans keep their provider directories current while letting clinicians attest to and manage their own practice information. Its original public API surfaced physician, practice-location, specialty, and insurance-plan data for building healthcare provider-directory applications. Backed by 500 Global and Uncork Capital, BetterDoctor was acquired by Quest Analytics, where the product continues as a provider-attestation and network-adequacy service used by 700,000+ healthcare professionals across 360,000+ locations. The standalone developer API has since been retired; betterdoctor.com now redirects to Quest Analytics.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betterdoctor.png
layout: provider
modified: '2026-07-18'
name: BetterDoctor
nav: Providers
network: true
overview: BetterDoctor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Provider Directory, Health Plans, and Doctors.
random_paper: 16
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betterdoctor/refs/heads/main/screenshots/betterdoctor-2026-07-25T202808.png
security:
- kind: domain-security
  name: Betterdoctor Domain Security
  slug: betterdoctor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: betterdoctor
tags:
- Company
- Healthcare
- Provider Directory
- Health Plans
- Doctors
- Data Verification
- Network Adequacy
website: https://betterdoctor.com
---
