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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation for Care Medical services as listed on the website.
  name: Care Medical Services API
  slug: care-medical-services-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caremedical3e74/refs/heads/main/hosts/caremedical3e74-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caremedical3e74-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caremedical3e74/refs/heads/main/vendors/caremedical3e74-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caremedical3e74-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caremedical3e74/refs/heads/main/security/caremedical3e74-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caremedical3e74-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caremedga.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caremedga.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caremedga.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://caremedga.com/services
- group: operate
  title: ''
  type: Contact
  url: https://caremedga.com/contact
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discovered on the API host.
  evidence:
  - status: 0
    url: https://api.caremedga.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Caremedical3e74 is a local home medical equipment provider operating in Georgia, USA. It offers a range of medical supplies and equipment for home use, including respiratory devices, mobility aids, and daily living accessories. The company emphasizes compassionate, responsive service and community involvement, partnering with customers and referral sources to ensure high-quality care. Its website provides detailed service listings, contact information for multiple locations, and policies such as terms of use and privacy.
layout: provider
modified: '2026-10-07'
name: Caremedical3e74
nav: Providers
network: true
overview: 'Caremedical3e74 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Equipment, Home Care, and Georgia.


  Caremedical3e74''s developer surface includes documentation and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caremedical3E74 Domain Security
  slug: caremedical3e74-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caremedical3e74
tags:
- Company
- Medical
- Equipment
- Home Care
- Georgia
website: https://caremedga.com
---
