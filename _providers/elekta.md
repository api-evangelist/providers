---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.elekta.com/company/digital-product-security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/security/elekta-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/elekta-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/well-known/elekta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elekta-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/hosts/elekta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elekta-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/vendors/elekta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elekta-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elekta.com/legal-notices/
- group: operate
  title: ''
  type: Support
  url: https://www.elekta.com/tags/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Elekta
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/security/elekta-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elekta-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/security/elekta-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elekta-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elekta/refs/heads/main/security/elekta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elekta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elekta.com/
coverage:
  checked: '2026-10-12'
  detail: Elekta's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.elekta.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Elekta provides radiation oncology and cancer care solutions, offering advanced radiotherapy equipment, software, and services. The company focuses on innovative treatments such as MR-Linac, adaptive radiotherapy, and oncology informatics, serving healthcare providers worldwide.
image: https://www.elekta.com/og-default-1200-630_hu_a405b2b0c8001544.jpg
layout: provider
modified: '2026-10-12'
name: Elekta
nav: Providers
network: true
overview: 'Elekta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Medical Devices, and Radiotherapy.


  Elekta''s developer surface includes support and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Elekta Domain Security
  slug: elekta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Elekta Vulnerability Disclosure
  slug: elekta-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Elekta Trust Center
  slug: elekta-trust-center
  summary_line: HIPAA, GDPR
slug: elekta
tags:
- Company
- Healthcare
- Oncology
- Medical Devices
- Radiotherapy
website: https://www.elekta.com/
---
