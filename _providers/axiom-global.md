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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-global/refs/heads/main/hosts/axiom-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiom-global-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-global/refs/heads/main/vendors/axiom-global-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiom-global-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://axiomglobal.com/media/
- group: start
  title: ''
  type: Login
  url: https://app.axiomglobal.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-global/refs/heads/main/security/axiom-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiom-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiomglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://axiomglobal.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiomglobal.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://axiomglobal.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://axiomglobal.com/careers/
coverage:
  checked: '2026-09-27'
  detail: Axiom Global provides staffing and talent solutions but offers no public developer program or API.
  evidence:
  - status: 200
    url: https://axiomglobal.com/about/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Axiom Global Technologies provides consulting, talent acquisition, cost containment, and electronic document management solutions. Their services include IT consulting, diversity hiring programs, bill review for cost savings, and EDM solutions for document scanning and secure hosting. Based in Walnut Creek, CA, they serve enterprises seeking expertise, integrity, and results across human capital and operational efficiency.
image: https://axiomglobal.com/wp-content/uploads/2020/09/the-office-staff-is-working-in-the-office-42HFM8A.jpg
layout: provider
modified: '2026-09-27'
name: Axiom Global
nav: Providers
network: true
overview: 'Axiom Global is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Talent Acquisition, Cost Containment, and Document Management.


  Axiom Global''s developer surface includes documentation and 9 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiom Global Domain Security
  slug: axiom-global-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axiom-global
tags:
- Company
- Consulting
- Talent Acquisition
- Cost Containment
- Document Management
- IT Services
website: https://axiomglobal.com/
---
