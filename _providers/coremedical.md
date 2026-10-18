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
- description: CoreMedical Group offers contract, travel, permanent, and interim healthcare staffing solutions as listed on the Services page.
  name: CoreMedical Services
  slug: coremedical-services
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremedical/refs/heads/main/hosts/coremedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coremedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremedical/refs/heads/main/vendors/coremedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coremedical-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coremedicalgroup.com/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.coremedicalgroup.com/blog/interviewing-and-onboarding-for-healthcare-recruiters-at-core-what-to-know
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coremedical/refs/heads/main/security/coremedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coremedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coremedicalgroup.com
- group: company
  title: ''
  type: Blog
  url: https://www.coremedicalgroup.com/our-blogs
- group: docs
  title: ''
  type: Documentation
  url: https://www.coremedicalgroup.com/services
coverage:
  checked: '2026-10-11'
  detail: The Services page provides only HTML documentation with no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://www.coremedicalgroup.com/services
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Coremedical Group provides travel nursing, medical staffing, and healthcare workforce solutions. It connects qualified nurses, therapists, and advanced practice providers with healthcare facilities across the United States, offering contract, permanent, and interim placement services. The company also delivers talent management, HR benefits, and specialized travel resources for healthcare professionals.
layout: provider
modified: '2026-10-10'
name: Coremedical
nav: Providers
network: true
overview: 'Coremedical is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Staffing, Healthcare, TravelNursing, and WorkforceSolutions.


  Coremedical''s developer surface includes getting-started guide, engineering blog, documentation, and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 11.6
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
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coremedical Domain Security
  slug: coremedical-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coremedical
tags:
- Company
- Staffing
- Healthcare
- TravelNursing
- WorkforceSolutions
website: https://www.coremedicalgroup.com
---
