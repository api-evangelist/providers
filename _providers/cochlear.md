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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cochlear/refs/heads/main/llms/cochlear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cochlear-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cochlear/refs/heads/main/hosts/cochlear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cochlear-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cochlear/refs/heads/main/vendors/cochlear-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cochlear-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cochlear.com/us/en/corporate/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://www.cochlear.com/at/de/corporate/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cochlear/refs/heads/main/security/cochlear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cochlear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cochlear.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cochlear.com/us/en/about-us
- group: operate
  title: ''
  type: Support
  url: https://support.cochlear.com/us/en/support/home
- group: company
  title: ''
  type: Careers
  url: https://www.cochlear.com/us/en/corporate/careers
- group: company
  title: ''
  type: Investors
  url: https://www.cochlear.com/us/en/corporate/investors
coverage:
  checked: '2026-10-13'
  detail: API endpoints return 403 Forbidden, no OpenAPI or other machine-readable contract discovered.
  evidence:
  - status: 403
    url: https://api.cochlear.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Cochlear is a global leader in implantable hearing solutions, helping over 700,000 people hear through advanced cochlear implant technology. The company focuses on patient-centered innovation, offering a range of devices, accessories, and support services to improve quality of life for individuals with hearing loss.
layout: provider
modified: '2026-10-13'
name: Cochlear
nav: Providers
network: true
overview: 'Cochlear is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hearing, Medical Devices, Healthcare, and Implantable Technology.


  Cochlear''s developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cochlear Domain Security
  slug: cochlear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cochlear
tags:
- Company
- Hearing
- Medical Devices
- Healthcare
- Implantable Technology
website: https://www.cochlear.com
---
