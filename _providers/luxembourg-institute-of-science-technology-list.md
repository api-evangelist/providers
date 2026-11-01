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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/luxembourg-institute-of-science-technology-list/hosts/luxembourg-institute-of-science-technology-list-hosts.yml
  title: ''
  type: Hosts
  url: hosts/luxembourg-institute-of-science-technology-list-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.list.lu/media-events/news
- group: auth
  href: https://artifacts.apis.io/luxembourg-institute-of-science-technology-list/security/luxembourg-institute-of-science-technology-list-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/luxembourg-institute-of-science-technology-list-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.list.lu/
- group: operate
  title: ''
  type: Contact
  url: https://www.list.lu/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.list.lu/privacy-notice
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.list.lu/legal-notice
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.list.lu/vulnerability-and-disclosure
coverage:
  checked: '2026-10-23'
  detail: The Luxembourg Institute of Science & Technology provides research services and does not expose a public API.
  evidence:
  - status: 200
    url: https://www.list.lu/
  reason: not-a-software-company
  state: none
created: '2026-10-23'
description: The Luxembourg Institute of Science & Technology (LIST) is a public research institute based in Luxembourg, focusing on interdisciplinary scientific research and innovation across domains such as digital transformation, health, environment, and advanced manufacturing. LIST collaborates with industry, academia, and governmental bodies to develop cutting‑edge technologies, provide expertise, and foster knowledge transfer, aiming to boost Luxembourg’s competitiveness and sustainable development.
layout: provider
modified: '2026-10-23'
name: Luxembourg Institute of Science & Technology (LIST)
nav: Providers
network: true
overview: Luxembourg Institute of Science & Technology (LIST) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Innovation, Technology, and Luxembourg.
random_paper: 19
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Luxembourg Institute Of Science Technology List Domain Security
  slug: luxembourg-institute-of-science-technology-list-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: luxembourg-institute-of-science-technology-list
tags:
- Company
- Research
- Innovation
- Technology
- Luxembourg
website: https://www.list.lu/
---
