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
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://sublime-systems.com
- group: company
  title: ''
  type: Blog
  url: https://sublime-systems.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://sublime-systems.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sublime-systems.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://sublime-systems.com/build/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sublime-cement/
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/SublimeSystems
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/sublime-systems-stock
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sublime-systems/refs/heads/main/security/sublime-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sublime-systems-domain-security.yml
coverage:
  checked: '2026-09-18'
  detail: Sublime Systems manufactures low-carbon cement sold through general-contractor distribution partners; sublime-systems.com is a WordPress marketing site with no developer section, and every OpenAPI, GraphQL, llms.txt, agent-card and /.well-known/ path probed on it returned 404.
  evidence:
  - status: 200
    url: https://sublime-systems.com/
  - status: 404
    url: https://sublime-systems.com/developers
  - status: 404
    url: https://sublime-systems.com/openapi.json
  - status: 404
    url: https://sublime-systems.com/.well-known/agent-card.json
  - status: 404
    url: https://sublime-systems.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-09-18'
description: Sublime Systems is a Somerville, Massachusetts cement manufacturer spun out of MIT that makes Sublime Cement, a low-carbon replacement for ordinary portland cement. Its ambient-temperature electrochemical "refinery for rocks" process extracts reactive calcium and silicates from low-value rocks and industrial byproducts and blends them into an ASTM-compliant cement that drops into existing concrete mix designs and equipment. The company sells through general-contractor distribution partners and publishes no developer program, API, SDK or machine-readable contract of any kind.
image: https://sublime-systems.com/wp-content/uploads/2025/05/image-3.jpg
layout: provider
modified: '2026-09-18'
name: Sublime Systems
nav: Providers
network: true
overview: 'Sublime Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cement, Construction Materials, Climate Tech, and Decarbonization.


  Sublime Systems'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sublime Systems Domain Security
  slug: sublime-systems-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sublime-systems
tags:
- Company
- Cement
- Construction Materials
- Climate Tech
- Decarbonization
- Manufacturing
- Electrochemistry
website: https://sublime-systems.com
---
