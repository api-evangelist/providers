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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bhubai/refs/heads/main/llms/bhubai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bhubai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bhubai/refs/heads/main/hosts/bhubai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bhubai-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bhubai/refs/heads/main/security/bhubai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bhubai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bhubai.com
coverage:
  checked: '2026-09-28'
  detail: bhubai.com returns a JavaScript shell with no machine-readable API documentation.
  evidence:
  - status: 200
    url: https://bhubai.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bhubai is a company listed in the API Evangelist harvest backlog, identified from secondary-market sources. At this time, public information about its products, services, or API offerings is limited. The entry serves as a placeholder for future enrichment as more data becomes available.
layout: provider
modified: '2026-09-28'
name: Bhubai
nav: Providers
network: true
overview: Bhubai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Platform, and Services.
random_paper: 3
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 6
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
    discoverability: 42.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bhubai Domain Security
  slug: bhubai-domain-security
  summary_line: TLSv1.3
slug: bhubai
tags:
- Company
- Technology
- Platform
- Services
website: https://bhubai.com
---
