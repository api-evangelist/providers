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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/digitalwork/plans/digitalwork-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalwork-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/digitalwork/hosts/digitalwork-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalwork-hosts.yml
- group: auth
  href: https://artifacts.apis.io/digitalwork/security/digitalwork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalwork.com/
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host.
  evidence:
  - status: timeout
    url: https://api.digitalwork.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: DigitalWork is a technology company that provides a platform for managing digital workspaces, enabling teams to collaborate, share files, and automate workflows. The service offers integrations with popular productivity tools, robust API access for developers, and customizable security controls. Founded to streamline remote and hybrid work environments, DigitalWork focuses on scalability, data privacy, and user-friendly interfaces to support enterprises of all sizes.
layout: provider
modified: '2026-10-23'
name: DigitalWork
nav: Providers
network: true
overview: DigitalWork is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Productivity, Cloud, and Enterprise.
plans:
- name: Digitalwork Plans Pricing
  plan_count: 3
  slug: digitalwork-plans-pricing
random_paper: 9
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Digitalwork Domain Security
  slug: digitalwork-domain-security
  summary_line: TLSv1.3
slug: digitalwork
tags:
- Collaboration
- Productivity
- Cloud
- Enterprise
website: https://www.digitalwork.com/
---
