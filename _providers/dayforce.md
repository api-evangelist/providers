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
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/security/dayforce-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dayforce-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/llms/dayforce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dayforce-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/well-known/dayforce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dayforce-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/hosts/dayforce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dayforce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/vendors/dayforce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dayforce-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dayforce.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.dayforce.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dayforce.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.dayforce.com/who-we-are/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://www.dayforce.com/blog
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/getting-started
  title: ''
  type: GettingStarted
  url: /getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dayforce.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/security/dayforce-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dayforce-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dayforce/refs/heads/main/security/dayforce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dayforce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dayforce.com
coverage:
  checked: '2026-10-14'
  detail: Developer portal at https://developers.dayforce.com returns HTML with heavy JavaScript and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developers.dayforce.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Dayforce provides a comprehensive, AI‑powered Human Capital Management (HCM) platform that unifies HR, payroll, talent, workforce management, and analytics. The cloud‑based solution helps enterprises automate HR processes, gain real‑time insights, ensure compliance, and improve employee experiences across global workforces.
image: https://www.dayforce.com/getmedia/49e85ed8-2e0e-46ef-92f9-248e2972ccf8/hero-home-1200x627.jpg
layout: provider
modified: '2026-10-13'
name: Dayforce
nav: Providers
network: true
overview: 'Dayforce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HCM, Payroll, Workforce Management, and Talent Management.


  Dayforce''s developer surface includes support, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dayforce Domain Security
  slug: dayforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dayforce Vulnerability Disclosure
  slug: dayforce-vulnerability-disclosure
  summary_line: no policy recorded
slug: dayforce
tags:
- Company
- HCM
- Payroll
- Workforce Management
- Talent Management
- Analytics
website: https://www.dayforce.com
---
