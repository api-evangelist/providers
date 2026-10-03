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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ash-wellness/refs/heads/main/hosts/ash-wellness-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ash-wellness-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ash-wellness/refs/heads/main/vendors/ash-wellness-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ash-wellness-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.poweredbyash.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.poweredbyash.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ashwellness.io/password
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ash-wellness/refs/heads/main/security/ash-wellness-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ash-wellness-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.poweredbyash.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.poweredbyash.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.poweredbyash.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.poweredbyash.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.poweredbyash.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.poweredbyash.com/hc/en-us/requests/new?ticket_form_id=53262861689876
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.poweredbyash.com/about-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Ash Wellness provides at‑home health testing solutions for organizations, enabling health plans and public health entities to close care gaps with convenient, accurate diagnostics. Their platform offers a range of testing kits for infectious disease, cancer screening, chronic conditions, hormonal health, and environmental health, supported by a digital health integration and robust data reporting.
image: https://cdn.prod.website-files.com/679ae4c97905c168c32b0d7d/67c231073af05b85b53a6f79_Ash_og_image.avif
layout: provider
modified: '2026-09-26'
name: Ash Wellness
nav: Providers
network: true
overview: 'Ash Wellness is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health Tech, Diagnostics, At-Home Testing, Healthcare, and B2B.


  Ash Wellness'' developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ash Wellness Domain Security
  slug: ash-wellness-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ash-wellness
tags:
- Health Tech
- Diagnostics
- At-Home Testing
- Healthcare
- B2B
website: https://www.poweredbyash.com/
---
