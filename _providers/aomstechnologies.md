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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.amstechnologies.com/Information/Terms-and-Conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://amstechnologies.com/news/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aomstechnologies/refs/heads/main/hosts/aomstechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aomstechnologies-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aomstechnologies/refs/heads/main/security/aomstechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aomstechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amstechnologies.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amstechnologies.com/cookie-policy-eu/
- group: operate
  title: ''
  type: Support
  url: https://amstechnologies.com/contact-us/
coverage:
  checked: 2026-09-25
  detail: No OpenAPI or other machine-readable contract found at api.amstechnologies.com and no documentation host provides specs.
  evidence:
  - status: 0
    url: https://api.amstechnologies.com/openapi.json
  - status: 0
    url: https://api.amstechnologies.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aomstechnologies, operating as AMS Technologies, provides optical, thermal management, and electronics solutions for high-mix low-volume markets. They offer custom engineering, production services, and a range of technology products aimed at European industry resilience and innovation.
layout: provider
modified: '2026-09-25'
name: Aomstechnologies
nav: Providers
network: true
overview: 'Aomstechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Optical, Thermal Management, Electronics, and Engineering.


  Aomstechnologies'' developer surface includes support and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aomstechnologies Domain Security
  slug: aomstechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aomstechnologies
tags:
- Company
- Optical
- Thermal Management
- Electronics
- Engineering
- Custom Solutions
website: https://amstechnologies.com
---
