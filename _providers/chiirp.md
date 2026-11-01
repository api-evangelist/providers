---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/chiirp/llms/chiirp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chiirp-llms.txt
- group: agent
  href: https://artifacts.apis.io/chiirp/well-known/chiirp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chiirp-well-known.yml
- group: other
  href: https://artifacts.apis.io/chiirp/hosts/chiirp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chiirp-hosts.yml
- group: other
  href: https://artifacts.apis.io/chiirp/vendors/chiirp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chiirp-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chiirp/security/chiirp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chiirp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chiirp.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://chiirp.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: CHIIRP provides an AI‑powered revenue optimization platform for home‑service businesses such as HVAC, plumbing, electrical, garage‑door and roofing companies. Its solution automates lead response, missed‑call recovery, estimate follow‑up and booking through AI voice agents, two‑way SMS, and integrations with ServiceTitan, Housecall Pro, Jobber and more, helping businesses increase conversion and streamline operations.
image: https://chiirp.com/og-image.png
layout: provider
modified: '2026-10-28'
name: CHIIRP
nav: Providers
network: true
overview: CHIIRP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Home Services, Revenue Optimization, and Automation.
random_paper: 15
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chiirp Domain Security
  slug: chiirp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chiirp
tags:
- Company
- AI
- Home Services
- Revenue Optimization
- Automation
website: https://chiirp.com/
---
