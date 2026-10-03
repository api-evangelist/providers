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
  href: https://raw.githubusercontent.com/api-evangelist/arkenstone/refs/heads/main/hosts/arkenstone-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arkenstone-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://arkenstonetechnologies.com/news/
- group: company
  title: ''
  type: Blog
  url: https://arkenstonetechnologies.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arkenstone/refs/heads/main/security/arkenstone-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkenstone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arkenstonetechnologies.com/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://arkenstonetechnologies.com/openapi.json
  - status: 0
    url: https://api.arkenstonetechnologies.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Arkenstone Technologies provides strategic consulting and implementation services focused on healthcare innovation, artificial intelligence, robotic process automation, compliance, security, and immersive technologies. Their offerings include healthcare analytics, AI-driven solutions, RPA deployment, and guidance on regulatory compliance, helping organizations navigate digital transformation and market disruptions.
layout: provider
modified: '2026-09-26'
name: Arkenstone
nav: Providers
network: true
overview: 'Arkenstone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, RPA, and Compliance.


  Arkenstone''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arkenstone Domain Security
  slug: arkenstone-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arkenstone
tags:
- Company
- Healthcare
- Artificial Intelligence
- RPA
- Compliance
website: https://arkenstonetechnologies.com/
---
