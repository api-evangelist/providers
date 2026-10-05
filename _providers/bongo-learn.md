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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bongo-learn/refs/heads/main/conformance/bongo-learn-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bongo-learn-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bongo-learn/refs/heads/main/hosts/bongo-learn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bongo-learn-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bongo-learn/refs/heads/main/vendors/bongo-learn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bongo-learn-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bongolearn.com/terms/
- group: auth
  title: ''
  type: Security
  url: https://bongolearn.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bongolearn.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://bongolearn.com/tag/news/
- group: other
  title: ''
  type: Leadership
  url: https://bongolearn.com/team/
- group: start
  title: ''
  type: GettingStarted
  url: https://bongolearn.com/channel-sales-onboarding/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bongo-learn/refs/heads/main/security/bongo-learn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bongo-learn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bongolearn.com
- group: docs
  title: ''
  type: Documentation
  url: https://bongolearn.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://bongolearn.com/blog/
- group: company
  title: ''
  type: About
  url: https://bongolearn.com/about/
- group: company
  title: ''
  type: Careers
  url: https://bongolearn.com/careers-at-bongo/
- group: operate
  title: ''
  type: Contact
  url: https://bongolearn.com/contact
coverage:
  checked: '2026-10-02'
  detail: The documentation pages return JavaScript challenges preventing automated reading.
  evidence:
  - status: 429
    url: https://bongolearn.com/resources/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bongo Learn provides an assessment and skills development platform for partners and higher education, offering AI role‑play, video assessments, scoring, and coaching tools to certify and measure partner enablement and student learning outcomes.
image: https://bongolearn.com/wp-content/uploads/2026/03/partner-background.png
layout: provider
modified: '2026-10-02'
name: Bongo Learn
nav: Providers
network: true
overview: 'Bongo Learn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Artificial Intelligence, Assessment, PartnerEnablement, and Skills Development.


  Bongo Learn''s developer surface includes getting-started guide, documentation, engineering blog, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 17.5
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
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bongo Learn Domain Security
  slug: bongo-learn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bongo-learn
tags:
- Education
- Artificial Intelligence
- Assessment
- PartnerEnablement
- Skills Development
- Platform
website: https://bongolearn.com
---
