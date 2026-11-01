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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cashmatic/llms/cashmatic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cashmatic-llms.txt
- group: agent
  href: https://artifacts.apis.io/cashmatic/well-known/cashmatic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cashmatic-well-known.yml
- group: other
  href: https://artifacts.apis.io/cashmatic/hosts/cashmatic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashmatic-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cashmatic/security/cashmatic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashmatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashmatic.it/
coverage:
  checked: '2026-10-27'
  detail: The provider website returns HTML without any machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://cashmatic.it/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Cashmatic provides automated cash and card payment solutions for point‑of‑sale businesses. Their platform optimizes cash handling, reduces change‑making errors, and enhances transaction security, helping retailers streamline operations and improve customer experience.
image: https://cashmatic.it/wp-content/uploads/2025/12/logo_cashmatic.svg
layout: provider
modified: '2026-10-27'
name: Cashmatic
nav: Providers
network: true
overview: Cashmatic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Retail, Automation, and POS.
random_paper: 5
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 7
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cashmatic Domain Security
  slug: cashmatic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cashmatic
tags:
- Company
- Payments
- Retail
- Automation
- POS
website: https://cashmatic.it/
---
