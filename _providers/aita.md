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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aita/refs/heads/main/llms/aita-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aita-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aita/refs/heads/main/security/aita-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aita-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aitabio.com/
coverage:
  checked: 2026-09-21
  detail: AiTA provides recruiting services and does not offer a developer program or public API.
  evidence:
  - status: unreachable
    url: https://developer.aita.com
  reason: no-developer-program
  state: none
created: '2026-09-21'
description: AiTA is a recruiting agency focused on artificial intelligence talent, offering AI companies access to a curated network of over 50,000 pre‑vetted engineers and executives. It provides end‑to‑end hiring services, candidate sourcing, and consulting for AI startups and enterprises, emphasizing rapid placement, high acceptance rates, and deep industry expertise across sectors such as healthtech, autonomous vehicles, and enterprise AI.
layout: provider
modified: '2026-09-21'
name: AiTA
nav: Providers
network: true
overview: AiTA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Recruiting, Talent, and Services.
random_paper: 19
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 4.6
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aita Domain Security
  slug: aita-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aita
tags:
- Company
- Artificial Intelligence
- Recruiting
- Talent
- Services
website: https://www.aitabio.com/
---
