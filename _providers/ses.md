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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ses/refs/heads/main/hosts/ses-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ses-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ses/refs/heads/main/vendors/ses-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ses-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ses/refs/heads/main/security/ses-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ses-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ses.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ses.com/v2/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ses.com/v2/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.ses.com/v2/cookie-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.ses.com/v2/ses-vulnerability-disclosure-policy
- group: other
  title: ''
  type: VendorInformation
  url: https://www.ses.com/v2/vendor-information
- group: company
  title: ''
  type: AboutUs
  url: https://www.ses.com/v2/company/about-us
created: '2026-09-22'
description: SES (Société Européenne des Satellites) is a leading satellite operator providing global communications services, including broadband internet, broadcast, and secure government connectivity. The company designs, builds, and operates a fleet of geostationary and medium Earth orbit satellites, delivering resilient, high‑throughput connectivity to enterprises, governments, and consumers worldwide. SES focuses on innovative solutions for aviation, maritime, energy, and digital infrastructure, emphasizing sustainability and advanced technology integration across its network.
layout: provider
modified: '2026-09-22'
name: SES
nav: Providers
network: true
overview: SES is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Communications, Aerospace, Enterprise, and Government.
random_paper: 1
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ses Domain Security
  slug: ses-domain-security
  summary_line: DMARC
slug: ses
tags:
- Satellite
- Communications
- Aerospace
- Enterprise
- Government
- Innovation
website: https://www.ses.com/
---
