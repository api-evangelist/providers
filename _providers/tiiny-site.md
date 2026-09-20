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
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://tiiny.site/
coverage:
  checked: '2026-09-19'
  detail: Double Helix Construction sells a PDF prompt playbook through Gumroad from a one-page Tiiny Host landing site; its only machine surface is a five-field agent-card stub on an unregistered resolved.sh placeholder subdomain that fails AgentCard shape (no skills, capabilities, protocolVersion or endpoint; the registry's message/send test returns 403), and tiiny.site - the domain this stub was created under - is Tiiny Host's platform domain, which 301s to tiiny.host and is not this company's site.
  evidence:
  - status: 200
    url: https://realestate-ai-os.resolved.sh/.well-known/agent-card.json
  - status: 200
    url: https://realestate-ai-os.resolved.sh/
  - status: 200
    url: https://realestate-ai-os.tiiny.site/
  - status: 404
    url: https://realestate-ai-os.tiiny.site/openapi.json
  - status: 404
    url: https://realestate-ai-os.tiiny.site/.well-known/agent-card.json
  - status: 200
    url: https://helixbuilder.gumroad.com/l/hvtgin
  - status: 301
    url: https://tiiny.site/
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: 'Double Helix Construction is a company surfaced via the API Evangelist harvest backlog (source: a2a-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-19'
name: Double Helix Construction
nav: Providers
network: true
overview: Double Helix Construction is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 5
score:
  band: minimal
  composite: 2.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 27.8
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: tiiny-site
tags:
- Company
website: https://tiiny.site/
---
