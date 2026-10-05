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
api_count: 1
apis:
- description: API for Botamedi services
  name: Botamedi API
  slug: botamedi-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botamedi/refs/heads/main/hosts/botamedi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botamedi-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botamedi/refs/heads/main/security/botamedi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botamedi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thebotamedi.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thebotamedi.com/privacypolicy.html
- group: operate
  title: ''
  type: Support
  url: https://thebotamedi.com/contacts.html
coverage:
  checked: '2026-10-03'
  detail: The provider's website returns HTTP 406 for common OpenAPI URLs, and no documentation host is identified.
  evidence:
  - status: 406
    url: https://thebotamedi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Botamedi Inc. develops marine phytochemical‑based therapeutics aimed at improving human and animal health. Established in 2001, the company leverages its proprietary SEANOL® technology to create safe, effective treatments derived from marine algae, targeting chronic degenerative diseases and promoting cellular health through natural compounds.
layout: provider
modified: '2026-10-03'
name: Botamedi
nav: Providers
network: true
overview: 'Botamedi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Pharmaceuticals, Marine, Therapeutics, and SEANOL.


  Botamedi''s developer surface includes support and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botamedi Domain Security
  slug: botamedi-domain-security
  summary_line: TLSv1.3
slug: botamedi
tags:
- Biotechnology
- Pharmaceuticals
- Marine
- Therapeutics
- SEANOL
website: https://thebotamedi.com
---
