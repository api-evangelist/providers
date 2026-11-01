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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/incentiv/conformance/incentiv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/incentiv-conformance.yml
- group: agent
  href: https://artifacts.apis.io/incentiv/well-known/incentiv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/incentiv-well-known.yml
- group: other
  href: https://artifacts.apis.io/incentiv/hosts/incentiv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/incentiv-hosts.yml
- group: other
  href: https://artifacts.apis.io/incentiv/vendors/incentiv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/incentiv-vendors.yml
- group: auth
  href: https://artifacts.apis.io/incentiv/security/incentiv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/incentiv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.incentiv.co/
- group: company
  title: ''
  type: Blog
  url: https://www.incentiv.co/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incentiv.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incentiv.co/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.incentiv.co/support
- group: operate
  title: ''
  type: Contact
  url: https://www.incentiv.co/contact-us
coverage:
  checked: '2026-10-24'
  detail: The Incentiv website provides only static HTML without any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.incentiv.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Incentiv provides compensation management software tailored for private equity firms and their portfolio companies. The platform streamlines executive compensation, bonus pools, equity incentive plans, and succession planning, leveraging data from over 500 portfolio companies to deliver trusted benchmarks. It aims to replace manual spreadsheets with a unified talent management solution that supports short‑term and long‑term incentive planning, diversity measurement, and talent development, helping private equity talent leaders make data‑driven decisions.
image: https://cdn.prod.website-files.com/64948c228c600f03e2d7e084/67f4e8a3c86614bd67a72ec2_Incentiv.png
layout: provider
modified: '2026-10-24'
name: Incentiv
nav: Providers
network: true
overview: 'Incentiv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compensation, Private-Equity, Talent-Management, and Software.


  Incentiv''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Incentiv Domain Security
  slug: incentiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: incentiv
tags:
- Company
- Compensation
- Private-Equity
- Talent-Management
- Software
website: https://www.incentiv.co/
---
