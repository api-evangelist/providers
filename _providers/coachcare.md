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
- description: Coachcare provides remote care management services.
  name: Coachcare API
  slug: coachcare-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coachcare/refs/heads/main/vendors/coachcare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coachcare-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coachcare/refs/heads/main/hosts/coachcare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coachcare-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coachcare.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.coachcare.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coachcare.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.coachcare.com/category/news/
- group: company
  title: ''
  type: Blog
  url: https://www.coachcare.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coachcare
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coachcare/refs/heads/main/security/coachcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coachcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coachcare.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://dashboard.coachcare.com/mcp
  - status: 401
    url: https://support.coachcare.com/mcp
  - status: 200
    url: https://www.coachcare.com
  - status: 403
    url: https://equityzen.com/company/coachcare
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Coachcare provides a comprehensive remote care management platform that connects patients, clinicians, and care teams through integrated digital tools. Their services include chronic care management, remote patient monitoring, diabetes management, and other Medicare‑covered programs, enabling scalable, high‑touch care delivery across large health systems. The platform offers APIs for data exchange, EHR integration, and device connectivity, supporting clinicians with alerts, task management, and analytics to improve outcomes and operational efficiency.
image: https://www.coachcare.com/wp-content/uploads/2024/08/Radically-simplifying-remote-care-management-programs.png
layout: provider
modified: '2026-10-09'
name: Coachcare
nav: Providers
network: true
overview: 'Coachcare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Remote Care Management, EHR Integration, Clinical Services, Chronic Care Management, and Remote Patient Monitoring.


  Coachcare''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.0
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
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coachcare Domain Security
  slug: coachcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coachcare
tags:
- Remote Care Management
- EHR Integration
- Clinical Services
- Chronic Care Management
- Remote Patient Monitoring
- Value-Based Care
website: https://www.coachcare.com
---
