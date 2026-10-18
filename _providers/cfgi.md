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
  href: https://raw.githubusercontent.com/api-evangelist/cfgi/refs/heads/main/hosts/cfgi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfgi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cfgi/refs/heads/main/vendors/cfgi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfgi-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cfgi.com/privacy-statement/
- group: other
  title: ''
  type: Leadership
  url: https://www.cfgi.com/about-us/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cfgi/refs/heads/main/security/cfgi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfgi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cfgi.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.cfgi.com/api
- group: operate
  title: ''
  type: Support
  url: https://www.cfgi.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.cfgi.com/blog
coverage:
  checked: '2026-10-08'
  detail: No API documentation or contract was found on api.cfgi.com, and the website provides no developer portal.
  evidence:
  - status: 0
    url: https://api.cfgi.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: CFGI (Corporate Finance Group International) is a global advisory firm providing finance, accounting, tax, risk, and technology services to corporations, private equity firms, and investors. With over 25 years of experience, CFGI offers private capital solutions, technical accounting, cybersecurity, ESG advisory, and strategic transaction support across multiple industries worldwide.
image: https://www.cfgi.com/wp-content/uploads/2024/01/Header-img-2-1.png
layout: provider
modified: '2026-10-07'
name: Cfgi
nav: Providers
network: true
overview: 'Cfgi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Advisory, Consulting, ESG, and Technology.


  Cfgi''s developer surface includes API reference, support, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cfgi Domain Security
  slug: cfgi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cfgi
tags:
- Finance
- Advisory
- Consulting
- ESG
- Technology
- Company
website: https://www.cfgi.com
---
