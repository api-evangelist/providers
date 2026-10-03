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
- description: API documentation is provided at https://docs.bloomboard.com but no machine‑readable contract was found.
  name: BloomBoard API
  slug: bloomboard-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomboard/refs/heads/main/well-known/bloomboard-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bloomboard-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomboard/refs/heads/main/well-known/bloomboard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bloomboard-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomboard/refs/heads/main/hosts/bloomboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloomboard-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomboard/refs/heads/main/vendors/bloomboard-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloomboard-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bloomboard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomboard.com/terms/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bloomboard.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://my.bloomboard.com/public/static/PrivacyPolicy.html
- group: company
  title: ''
  type: Newsroom
  url: https://bloomboard.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomboard/refs/heads/main/security/bloomboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloomboard.com
- group: docs
  title: ''
  type: Documentation
  url: https://bloomboard.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://bloomboard.com/why-bloomboard
- group: operate
  title: ''
  type: Support
  url: https://support.bloomboard.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://bloomboard.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://bloomboard.com/contact-us
coverage:
  checked: '2026-09-29'
  detail: Documentation at https://docs.bloomboard.com is a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.bloomboard.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: BloomBoard is a talent development provider for K‑12 school districts and higher‑education institutions. It offers turnkey programs that help educators advance through apprenticeship, certification, and degree pathways, addressing educator pipeline, advancement, and retention challenges. The platform connects districts with partner institutions to deliver on‑the‑job learning and professional growth solutions.
layout: provider
modified: '2026-09-29'
name: Bloomboard
nav: Providers
network: true
overview: 'Bloomboard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Talent Development, K-12, Higher Education, and Workforce.


  Bloomboard''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
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
  name: Bloomboard Domain Security
  slug: bloomboard-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bloomboard
tags:
- Education
- Talent Development
- K-12
- Higher Education
- Workforce
website: https://bloomboard.com
---
