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
api_count: 1
apis:
- description: Developer portal for Celebal Technologies offering AI and data solutions.
  name: Celebal Technologies API
  slug: celebal-technologies-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celebaltechnologies/refs/heads/main/hosts/celebaltechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celebaltechnologies-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celebaltech.com/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://celebaltech.com/services/cloud-infra-and-security/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celebaltech.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.celebaltech.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celebaltechnologies/refs/heads/main/security/celebaltechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celebaltechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celebaltech.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://celebaltech.com
  - status: 403
    url: https://equityzen.com/company/celebaltechnologies
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Celebal Technologies is a premier software services company specializing in Data, AI, Cloud, and IT consulting. It provides enterprise solutions, data engineering, analytics, and AI-driven services to help organizations adopt digital transformation and gain competitive advantage.
image: https://celebaltech.com/logo.png
layout: provider
modified: '2026-10-07'
name: Celebaltechnologies
nav: Providers
network: true
overview: 'Celebaltechnologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Artificial Intelligence, Cloud, and Consulting.


  Celebaltechnologies'' developer surface includes documentation and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celebaltechnologies Domain Security
  slug: celebaltechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celebaltechnologies
tags:
- Company
- Data
- Artificial Intelligence
- Cloud
- Consulting
website: https://celebaltech.com
---
