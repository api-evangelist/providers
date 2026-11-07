---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/easygroupflights-com/llms/easygroupflights-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easygroupflights-com-llms.txt
- group: other
  href: https://artifacts.apis.io/easygroupflights-com/a2a/easygroupflights-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/easygroupflights-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/easygroupflights-com/well-known/easygroupflights-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easygroupflights-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/easygroupflights-com/hosts/easygroupflights-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easygroupflights-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easygroupflights-com/vendors/easygroupflights-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easygroupflights-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://easygroupflights.com/blog/
- group: auth
  href: https://artifacts.apis.io/easygroupflights-com/security/easygroupflights-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easygroupflights-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easygroupflights.com/
coverage:
  checked: '2026-11-06'
  detail: EasyGroupFlights provides travel booking services but does not publish a developer program or public API documentation.
  evidence:
  - status: 0
    url: https://api.easygroupflights.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-06'
description: EasyGroupFlights is a travel agency specializing in group airfare for schools, sports teams, companies, and tour operators. They are IATA accredited, offering negotiated group fares 20–40% below retail, with 24/7 support and worldwide service.
image: https://easygroupflights.com/og-image.png
layout: provider
modified: '2026-11-06'
name: EasyGroupFlights
nav: Providers
network: true
overview: 'EasyGroupFlights is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, GroupFlights, B2B, Aviation, and Europe.


  EasyGroupFlights'' developer surface includes engineering blog and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easygroupflights Com Domain Security
  slug: easygroupflights-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easygroupflights-com
tags:
- Travel
- GroupFlights
- B2B
- Aviation
- Europe
website: https://easygroupflights.com/
---
