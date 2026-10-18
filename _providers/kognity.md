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
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kognity/refs/heads/main/conformance/kognity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kognity-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kognity/refs/heads/main/llms/kognity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kognity-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kognity/refs/heads/main/hosts/kognity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kognity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kognity/refs/heads/main/vendors/kognity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kognity-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kognity.com/privacy-and-security/
- group: commercial
  title: ''
  type: Pricing
  url: https://kognity.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://kognity.com/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://kognity.com/resources/content-type/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kognity
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kognity/refs/heads/main/security/kognity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kognity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kognity.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://go.kognity.com/api/mcp
  - status: 200
    url: https://kognity.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Kognity provides a digital curriculum and online learning platform for schools, offering interactive textbooks, built‑in assessments, and analytics. Trusted by over 2,000 schools worldwide, it supports IB, IGCSE, NGSS and other curricula, helping educators deliver engaging, standards‑aligned content and track student progress.
layout: provider
modified: '2026-10-15'
name: Kognity
nav: Providers
network: true
overview: 'Kognity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, EdTech, Curriculum, Learning Platform, and Software-as-a-Service.


  Kognity''s developer surface includes pricing, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kognity Domain Security
  slug: kognity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kognity
tags:
- Education
- EdTech
- Curriculum
- Learning Platform
- Software-as-a-Service
- Company
website: https://kognity.com/
---
