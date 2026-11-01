---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/marathon-health-com/hosts/marathon-health-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marathon-health-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/marathon-health-com/vendors/marathon-health-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marathon-health-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.marathon-health.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marathon.health/privacy-policy-center
- group: company
  title: ''
  type: Newsroom
  url: https://marathon.health/resources/news
- group: company
  title: ''
  type: Blog
  url: https://marathon.health/resources/blog
- group: auth
  href: https://artifacts.apis.io/marathon-health-com/security/marathon-health-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marathon-health-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marathon-health.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.marathon-health.com/mcp
  - status: 403
    url: https://trust.marathon-health.com/mcp
  - status: 200
    url: https://www.marathon-health.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Marathon Health provides advanced primary care services for organizations, offering onsite, nearsite, and virtual health centers to lower healthcare costs and improve employee health outcomes. The company focuses on value‑based care, chronic condition management, mental health, and wellness programs for employers across the United States.
image: https://marathon.health/hubfs/Home_Open%20Graph.png
layout: provider
modified: '2026-10-22'
name: Marathon Health
nav: Providers
network: true
overview: 'Marathon Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, PrimaryCare, EmployerBenefits, and ValueBasedCare.


  Marathon Health''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Marathon Health Com Domain Security
  slug: marathon-health-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marathon-health-com
tags:
- Company
- Healthcare
- PrimaryCare
- EmployerBenefits
- ValueBasedCare
website: https://www.marathon-health.com
---
