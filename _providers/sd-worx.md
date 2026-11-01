---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.sdworx.com/en-en/about-sd-worx/trust-centre
- group: agent
  href: https://artifacts.apis.io/sd-worx/llms/sd-worx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sd-worx-llms.txt
- group: auth
  href: https://artifacts.apis.io/sd-worx/well-known/sd-worx-read-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sd-worx-read-security.txt
- group: agent
  href: https://artifacts.apis.io/sd-worx/well-known/sd-worx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sd-worx-well-known.yml
- group: other
  href: https://artifacts.apis.io/sd-worx/hosts/sd-worx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sd-worx-hosts.yml
- group: other
  href: https://artifacts.apis.io/sd-worx/vendors/sd-worx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sd-worx-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sdworx.com/en-en/about-sd-worx/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sdworx.com/en-en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.sdworx.com/en-en/about-sd-worx/press
- group: start
  title: ''
  type: Login
  url: https://www.sdworx.com/en-en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SDWorx
- group: auth
  href: https://artifacts.apis.io/sd-worx/security/sd-worx-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sd-worx-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sd-worx/security/sd-worx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sd-worx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sdworx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sdworx.com/en-en/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.sdworx.com/en-en/contact-us
coverage:
  checked: '2026-10-27'
  detail: The developer documentation is a JavaScript‑rendered site with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.sdworx.com/en-en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: SD Worx is a leading European provider of HR, payroll and workforce management solutions. They help organisations across Europe streamline HR processes, payroll, time‑and‑attendance, and employee engagement, enabling businesses to focus on growth. Their cloud‑based platform combines compliance expertise with modern technology to support companies of all sizes.
layout: provider
modified: '2026-10-27'
name: SD Worx
nav: Providers
network: true
overview: 'SD Worx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include HR, Payroll, Workforce-Management, Europe, and Cloud.


  SD Worx''s developer surface includes documentation and 15 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sd Worx Domain Security
  slug: sd-worx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sd Worx Trust Center
  slug: sd-worx-trust-center
  summary_line: ISO 27001, GDPR
slug: sd-worx
tags:
- HR
- Payroll
- Workforce-Management
- Europe
- Cloud
website: https://www.sdworx.com/
---
