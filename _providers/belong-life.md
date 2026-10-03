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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belong-life/refs/heads/main/hosts/belong-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belong-life-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belong-life/refs/heads/main/vendors/belong-life-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belong-life-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://belong.life/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://belong.life/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://belong.life/press/
- group: company
  title: ''
  type: Blog
  url: https://belong.life/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belong-life/refs/heads/main/security/belong-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belong-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belong.life
coverage:
  checked: '2026-09-27'
  detail: All attempted OpenAPI endpoints returned HTTP 500 and no machine‑readable spec was found.
  evidence:
  - status: 500
    url: https://belong.life/openapi.json
  - status: 500
    url: https://belong.life/openapi.yaml
  - status: 500
    url: https://belong.life/swagger.json
  - status: 500
    url: https://belong.life/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Belong.Life leverages AI and data to enhance patient engagement and healthcare outcomes, offering solutions for clinics, enterprises, pharma, hospitals, payers, and advertisers. Their platform includes AI-driven cancer mentoring, weight management, and health assistants, alongside clinical trial support and research tools, aiming to personalize care and improve decision-making across the health ecosystem.
image: https://belong.life/wp-content/uploads/2021/11/LOGO-icon.png
layout: provider
modified: '2026-09-27'
name: Belong.Life
nav: Providers
network: true
overview: 'Belong.Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Artificial Intelligence, Patient Engagement, Digital Health, and Company.


  Belong.Life''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Belong Life Domain Security
  slug: belong-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: belong-life
tags:
- Health
- Artificial Intelligence
- Patient Engagement
- Digital Health
- Company
website: https://belong.life
---
