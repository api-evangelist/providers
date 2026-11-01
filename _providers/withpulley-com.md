---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/withpulley-com/vendors/withpulley-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/withpulley-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/withpulley-com/llms/withpulley-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/withpulley-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/withpulley-com/well-known/withpulley-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/withpulley-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/withpulley-com/hosts/withpulley-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/withpulley-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.withpulley.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://build.withpulley.com/get-started
- group: auth
  href: https://artifacts.apis.io/withpulley-com/security/withpulley-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/withpulley-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withpulley.com/
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found on the provider's website.
  evidence:
  - status: 200
    url: https://www.withpulley.com/openapi.json
  - status: 404
    url: https://www.withpulley.com/api/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: 'Pulley is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by crv) and added to the network as a stub for full-pipeline profiling.'
image: https://www.withpulley.com/opengraph.jpg
layout: provider
modified: '2026-10-22'
name: Pulley
nav: Providers
network: true
overview: 'Pulley is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Pulley''s developer surface includes support, getting-started guide, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 30.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Withpulley Com Domain Security
  slug: withpulley-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withpulley-com
tags:
- Company
website: https://www.withpulley.com/
---
