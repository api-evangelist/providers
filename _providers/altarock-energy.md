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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/altarock-energy/refs/heads/main/hosts/altarock-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altarock-energy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altarockenergy.com/terms-conditions-2
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altarockenergy.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://altarockenergy.com/2010/09/comparing-and-contrasting-egs-with-other-forms-of-renewable-energy/price-range/
- group: company
  title: ''
  type: Newsroom
  url: https://altarockenergy.com/newsroom/
- group: operate
  title: ''
  type: ChangeLog
  url: https://altarockenergy.com/newsroom/releases/
- group: company
  title: ''
  type: Blog
  url: https://altarockenergy.com/newsroom/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/altarock-energy/refs/heads/main/security/altarock-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altarock-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altarockenergy.com
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's API host or website.
  evidence:
  - status: 0
    url: https://api.altarockenergy.com/openapi.json
  - status: 404
    url: https://altarockenergy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: AltaRock Energy is a technology leader in Enhanced Geothermal Systems (EGS) development, raising EGS to massive scale. It provides clean, affordable, renewable geothermal energy worldwide, advancing innovative drilling, reservoir engineering, and power generation to make geothermal power available anywhere and everywhere.
image: http://altarockenergy.com/wp-content/uploads/2021/03/Petty-Susan.jpg
layout: provider
modified: '2026-09-24'
name: Altarock Energy
nav: Providers
network: true
overview: 'Altarock Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Geothermal, Cleantech, RenewableEnergy, and Technology.


  Altarock Energy''s developer surface includes pricing, changelog, engineering blog, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.1
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 21.1
  previous_composite: 1.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altarock Energy Domain Security
  slug: altarock-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: altarock-energy
tags:
- Energy
- Geothermal
- Cleantech
- RenewableEnergy
- Technology
- Company
website: https://altarockenergy.com
---
