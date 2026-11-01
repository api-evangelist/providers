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
  href: https://artifacts.apis.io/curai-com/hosts/curai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/curai-com/vendors/curai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curaihealth.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://curaihealth.com/support
- group: auth
  href: https://artifacts.apis.io/curai-com/security/curai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://curaihealth.com/
coverage:
  checked: '2026-10-22'
  detail: No public developer portal or API documentation was found on curaihealth.com or its subdomains.
  evidence:
  - status: 200
    url: https://developer.curaihealth.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Curai Health provides affordable, technology‑enabled primary care that connects patients with doctors through a digital platform. The service offers virtual visits, personalized care plans, and a subscription model that aims to reduce the cost of routine healthcare. Founded with backing from Khosla Ventures, Curai leverages AI to triage and streamline patient interactions, delivering care from home while maintaining a focus on quality and accessibility.
layout: provider
modified: '2026-10-22'
name: Curai
nav: Providers
network: true
overview: 'Curai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telemedicine, AI, and PrimaryCare.


  Curai''s developer surface includes support and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.8
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
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Curai Com Domain Security
  slug: curai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curai-com
tags:
- Company
- Healthcare
- Telemedicine
- AI
- PrimaryCare
website: https://curaihealth.com/
---
