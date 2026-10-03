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
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/well-known/apus-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apus-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/well-known/apus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apus-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://www.amu.apus.edu/help/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/plans/apus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apus-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/conformance/apus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apus-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/llms/apus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apus-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/hosts/apus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apus-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/vendors/apus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apus-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.apus.edu/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.apus.edu/about/leadership/board-of-trustees/ms-paula-singer/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.apus.edu/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.apu.apus.edu/transfer-credit/getting-started/transfer-credit-evaluations/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/security/apus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apus-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apus/refs/heads/main/security/apus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apusapps.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apus.edu/aboutus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apus.edu/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apus.edu/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.apus.edu/news-center/
coverage:
  checked: 2026-09-25
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://dev.apus.edu/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Apus, operating as the American Public University System, is a U.S.-based higher education institution offering online degree programs through its colleges including American Public University and American Military University. The system provides accredited undergraduate and graduate programs, serves military and civilian students, and is a subsidiary of American Public Education, Inc. It emphasizes flexible learning, veteran benefits, and a mission to deliver accessible education worldwide.
image: https://www.apus.edu/images/shared/og/system-default-og.png
layout: provider
modified: '2026-09-25'
name: Apus
nav: Providers
network: true
overview: 'Apus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Online Learning, HigherEd, Veterans, and Accreditation.


  Apus'' developer surface includes support, getting-started guide, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Apus Plans Pricing
  plan_count: 7
  slug: apus-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apus Domain Security
  slug: apus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apus Vulnerability Disclosure
  slug: apus-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apus
tags:
- Education
- Online Learning
- HigherEd
- Veterans
- Accreditation
website: https://www.apusapps.com/en/
---
