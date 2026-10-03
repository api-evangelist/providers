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
  href: https://raw.githubusercontent.com/api-evangelist/astonsci/refs/heads/main/hosts/astonsci-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astonsci-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astonsci/refs/heads/main/security/astonsci-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astonsci-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://astonsci.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/astonsci
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Aston Sci. is a clinical-stage biopharmaceutical company focused on developing innovative medicines to meet unmet medical needs. The company presents its pipeline, science focus areas, and corporate information through its website.
image: http://astonsci.com/common/imgs/open-graph.png
layout: provider
modified: '2026-09-26'
name: Astonsci
nav: Providers
network: true
overview: Astonsci is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biopharma, Clinical Stage, Innovation, Medicine, and South Korea.
random_paper: 10
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
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
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Astonsci Domain Security
  slug: astonsci-domain-security
  summary_line: no transport/DNS hardening detected
slug: astonsci
tags:
- Biopharma
- Clinical Stage
- Innovation
- Medicine
- South Korea
website: http://astonsci.com
---
