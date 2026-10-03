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
api_count: 1
apis:
- description: API for BenchPrep platform, described in the Getting Started page.
  name: BenchPrep API
  slug: benchprep-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/plans/benchprep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/benchprep-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/conformance/benchprep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/benchprep-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/well-known/benchprep-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/benchprep-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/well-known/benchprep-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/benchprep-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/hosts/benchprep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benchprep-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/vendors/benchprep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benchprep-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.benchprep.com/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.benchprep.com/
- group: auth
  title: ''
  type: Security
  url: https://www.benchprep.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.benchprep.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://benchprep.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://blog.benchprep.com/getting-started-with-benchpreps-zoom-meetings-integration
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benchprep/refs/heads/main/security/benchprep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benchprep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.benchprep.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.benchprep.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.benchprep.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.benchprep.com/contact-us
- group: operate
  title: ''
  type: Support
  url: https://support.benchprep.com/home/
coverage:
  checked: '2026-09-27'
  detail: Getting Started page renders HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.benchprep.com/get-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: BenchPrep provides a cloud‑based learning management system that helps organizations deliver certification training, exam preparation, and continuing education. Their platform includes AI‑driven learning technology, reporting tools, content management, and integrations, serving enterprises, associations, and educational institutions worldwide.
image: https://cdn.prod.website-files.com/613a53a94111286b54741135/617ae672da9be9e6152bc7f7_opengraph%20image-home2.png
layout: provider
modified: '2026-09-27'
name: BenchPrep
nav: Providers
network: true
overview: 'BenchPrep publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LMS, Education, Training, and Software-as-a-Service.


  BenchPrep''s developer surface includes getting-started guide, engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Benchprep Plans Pricing
  plan_count: 1
  slug: benchprep-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benchprep Domain Security
  slug: benchprep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: benchprep
tags:
- Company
- LMS
- Education
- Training
- Software-as-a-Service
website: https://www.benchprep.com/
---
