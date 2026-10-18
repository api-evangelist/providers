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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/concentricinc/refs/heads/main/hosts/concentricinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/concentricinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/concentricinc/refs/heads/main/vendors/concentricinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/concentricinc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concentricusa.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.concentricusa.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concentricusa.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.concentricusa.com/news
- group: company
  title: ''
  type: Blog
  url: https://blog.concentricusa.com/engineering-uptime
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/concentricinc/refs/heads/main/security/concentricinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concentricinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.concentricusa.com
coverage:
  checked: '2026-10-10'
  detail: The public website provides only HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.concentricusa.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Concentric Inc provides critical infrastructure power and cooling solutions for data centers, industrial facilities, and commercial enterprises. With over 25 years of experience, they deliver power systems, forklift power, environmental safety products, and maintenance services across the United States, supporting mission‑critical operations and sustainability initiatives.
image: https://www.concentricusa.com/hubfs/Homepage%20extension%20team%20green.png
layout: provider
modified: '2026-10-10'
name: Concentricinc
nav: Providers
network: true
overview: 'Concentricinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Power, Infrastructure, DataCenter, Industrial, and Sustainability.


  Concentricinc''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.4
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Concentricinc Domain Security
  slug: concentricinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concentricinc
tags:
- Power
- Infrastructure
- DataCenter
- Industrial
- Sustainability
website: https://www.concentricusa.com
---
