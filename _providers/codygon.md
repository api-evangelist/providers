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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Codygon provides AI analytics and data quality platform APIs as described on their documentation site.
  name: Codygon API
  slug: codygon-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/codygon/hosts/codygon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codygon-hosts.yml
- group: other
  href: https://artifacts.apis.io/codygon/vendors/codygon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codygon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codygon.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.codygon.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codygon.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/codygon/security/codygon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codygon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codygon.com/
- group: company
  title: ''
  type: Blog
  url: https://codygon.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://codygon.com/resources
- group: operate
  title: ''
  type: PressReleases
  url: https://codygon.com/press-releases
coverage:
  checked: '2026-10-20'
  detail: Documentation site renders via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://codygon.com/resources
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Codygon provides an AI analytics and data quality platform for enterprises, offering the Tower dashboard creation tool and the Anode data governance solution. Founded in 2020 in India, it serves customers such as Pfizer, Merck, and Aramco, delivering predictive, prescriptive, and descriptive analytics without requiring SQL or BI teams.
image: https://codygon.com/favicon.svg
layout: provider
modified: '2026-10-19'
name: Codygon
nav: Providers
network: true
overview: 'Codygon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Data Quality, and Enterprise.


  Codygon''s developer surface includes support, engineering blog, documentation, and 7 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Codygon Domain Security
  slug: codygon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codygon
tags:
- Company
- Artificial Intelligence
- Analytics
- Data Quality
- Enterprise
website: https://codygon.com/
---
