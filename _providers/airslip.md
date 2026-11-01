---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/airslip/llms/airslip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airslip-llms.txt
- group: other
  href: https://artifacts.apis.io/airslip/hosts/airslip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airslip-hosts.yml
- group: auth
  href: https://artifacts.apis.io/airslip/security/airslip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airslip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airslip.com/
coverage:
  checked: '2026-10-19'
  detail: The Airslip site returns a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: 200
    url: https://airslip.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Airslip provides a platform that enables users to seamlessly integrate and manage digital receipts, warranties, and product information across multiple retailers. The service aggregates purchase data, offers personalized product insights, and facilitates easy access to documentation and support for consumer goods. By leveraging APIs, developers can embed receipt capture, warranty verification, and product lifecycle management into their applications, enhancing user experience and post-purchase engagement. Airslip aims to simplify the post-purchase journey for both consumers and businesses, fostering transparency and convenience in product ownership.
layout: provider
modified: '2026-10-19'
name: Airslip
nav: Providers
network: true
overview: Airslip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Receipts, Warranty, and Consumer.
random_paper: 12
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Airslip Domain Security
  slug: airslip-domain-security
  summary_line: TLSv1.3
slug: airslip
tags:
- Company
- Receipts
- Warranty
- Consumer
website: https://airslip.com/
---
