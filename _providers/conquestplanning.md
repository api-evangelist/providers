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
- description: API access for Conquestplanning platform (developer portal)
  name: Conquestplanning API
  slug: conquestplanning-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conquestplanning/refs/heads/main/hosts/conquestplanning-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conquestplanning-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/conquestplanning/refs/heads/main/vendors/conquestplanning-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conquestplanning-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://conquestplanning.com/media
- group: other
  title: ''
  type: Leadership
  url: https://conquestplanning.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.conquestplanning.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conquestplanning/refs/heads/main/security/conquestplanning-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conquestplanning-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conquestplanning.com
- group: docs
  title: ''
  type: Documentation
  url: https://conquestplanning.com/platform
- group: commercial
  title: ''
  type: Pricing
  url: https://conquestplanning.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://conquestplanning.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conquestplanning.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://conquestplanning.com/get-started
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://conquestplanning.com
  - status: 403
    url: https://equityzen.com/company/conquestplanning
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Conquestplanning provides AI‑driven financial planning software for wealth firms, advisors, and institutions. Their Strategic Advice Manager (SAM) engine delivers verifiable, personalized advice at scale, integrating behavioral finance agents and compliance tools. The platform supports multi‑language locales, offers a pricing page, resources, and a developer portal for API access, aiming to modernize financial planning with transparent, auditable recommendations.
image: https://cdn.prod.website-files.com/62aa2492f1114e6a77f39a86/6aa15c4a645aa3b4fa71e92c_og-general-cq.png
layout: provider
modified: '2026-10-10'
name: Conquestplanning
nav: Providers
network: true
overview: 'Conquestplanning is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Planning, Artificial Intelligence, Wealth Management, and Software-as-a-Service.


  Conquestplanning''s developer surface includes documentation, pricing, support, getting-started guide, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 16.5
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
    developer_ergonomics: 35.7
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conquestplanning Domain Security
  slug: conquestplanning-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: conquestplanning
tags:
- Company
- Financial-Planning
- Artificial Intelligence
- Wealth Management
- Software-as-a-Service
website: https://conquestplanning.com
---
