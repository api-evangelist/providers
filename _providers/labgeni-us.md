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
api_count: 1
apis:
- description: API documentation is hosted on the LabGenius website but no machine‑readable OpenAPI/GraphQL spec was found.
  name: LabGenius API
  slug: labgenius-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/labgeni-us/llms/labgeni-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/labgeni-us-llms.txt
- group: other
  href: https://artifacts.apis.io/labgeni-us/hosts/labgeni-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/labgeni-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/labgeni-us/vendors/labgeni-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/labgeni-us-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://labgeniustx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://labgeniustx.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://labgeniustx.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://labgeniustx.com/team
- group: auth
  href: https://artifacts.apis.io/labgeni-us/security/labgeni-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/labgeni-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://labgeni.us
created: '2026-10-26'
description: LabGenius Therapeutics is pioneering a closed-loop platform that combines AI, robotic automation, and synthetic biology to accelerate the discovery of next-generation therapeutic antibodies for solid tumours, aiming to transform antibody discovery for cancer treatment and other diseases.
image: https://labgeniustx.com/wp-content/uploads/2025/01/labgenius-homepage-sharing.jpeg
layout: provider
modified: '2026-10-26'
name: LabGenius
nav: Providers
network: true
overview: LabGenius is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, AI, AntibodyDiscovery, and Therapeutics.
random_paper: 15
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Labgeni Us Domain Security
  slug: labgeni-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: labgeni-us
tags:
- Company
- Biotechnology
- AI
- AntibodyDiscovery
- Therapeutics
- MachineLearning
website: https://labgeni.us
---
