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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/corcentric/refs/heads/main/well-known/corcentric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/corcentric-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corcentric/refs/heads/main/hosts/corcentric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corcentric-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corcentric/refs/heads/main/vendors/corcentric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/corcentric-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corcentric.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.corcentric.com/contact-support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corcentric.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.corcentric.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.corcentric.com/company/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.corcentric.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corcentric/refs/heads/main/security/corcentric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corcentric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corcentric.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.corcentric.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Corcentric provides cloud‑based financial solutions that help organizations reduce fleet costs, accelerate cash flow, and improve overall financial performance. Their offerings include fleet management, financing, and managed accounts receivable services, delivering industry‑leading efficiency and cost savings for B2B enterprises.
image: https://www.corcentric.com/wp-content/uploads/2026/08/corcentric-logo-color-tagline-01.jpg
layout: provider
modified: '2026-10-10'
name: Corcentric
nav: Providers
network: true
overview: 'Corcentric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, B2B, Cloud, Fleet Management, and Receivables.


  Corcentric''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corcentric Domain Security
  slug: corcentric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corcentric
tags:
- Finance
- B2B
- Cloud
- Fleet Management
- Receivables
website: https://www.corcentric.com
---
