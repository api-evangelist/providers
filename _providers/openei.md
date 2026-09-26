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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: http://www.energy.gov/vulnerability-disclosure-policy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openei/refs/heads/main/hosts/openei-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openei-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://auth.openei.org/register?redir=https://openei.org/wiki/Main+Page
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openei/refs/heads/main/security/openei-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/openei-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openei/refs/heads/main/security/openei-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openei-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openei.org/
coverage:
  checked: 2026-09-23
  detail: OpenAPI spec request at https://api.openei.org/openapi.json returned 403, indicating access is gated behind authentication.
  evidence:
  - status: 403
    url: https://api.openei.org/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-23'
description: OpenEI (Open Energy Information) is a collaborative platform that provides free, open access to energy data, models, and analysis tools. It aims to accelerate the transition to sustainable energy by sharing information, fostering community contributions, and supporting research and policy development. The site hosts a wiki, datasets, and APIs for developers to retrieve energy-related information.
layout: provider
modified: '2026-09-23'
name: OpenEI
nav: Providers
network: true
overview: 'OpenEI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Data, Open Source, Community, and Research.


  OpenEI''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  previous_composite: 8.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openei Domain Security
  slug: openei-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openei Vulnerability Disclosure
  slug: openei-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: openei
tags:
- Energy
- Data
- Open Source
- Community
- Research
website: https://openei.org/
---
