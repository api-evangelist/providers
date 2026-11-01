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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/zenpire-holdings/llms/zenpire-holdings-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zenpire-holdings-llms.txt
- group: agent
  href: https://artifacts.apis.io/zenpire-holdings/well-known/zenpire-holdings-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zenpire-holdings-well-known.yml
- group: other
  href: https://artifacts.apis.io/zenpire-holdings/hosts/zenpire-holdings-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zenpire-holdings-hosts.yml
- group: other
  href: https://artifacts.apis.io/zenpire-holdings/vendors/zenpire-holdings-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zenpire-holdings-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenpire.tech/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://zenpire.tech/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenpire.tech/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://zenpire.tech/blog/
- group: auth
  href: https://artifacts.apis.io/zenpire-holdings/security/zenpire-holdings-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zenpire-holdings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://zenpire.tech/
coverage:
  checked: '2026-10-24'
  detail: The company website provides HTML pages but no discoverable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://zenpire.tech/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: 'Zenpire Holdings is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by bowery-capital) and added to the network as a stub for full-pipeline profiling.'
image: https://zenpire.tech/wp-content/uploads/2026/01/Group-6-2.png
layout: provider
modified: '2026-10-24'
name: Zenpire Holdings
nav: Providers
network: true
overview: 'Zenpire Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shopify Apps, E‑commerce, Dropshipping, Promotions, and Events.


  Zenpire Holdings'' developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zenpire Holdings Domain Security
  slug: zenpire-holdings-domain-security
  summary_line: TLSv1.3
slug: zenpire-holdings
tags:
- Shopify Apps
- E‑commerce
- Dropshipping
- Promotions
- Events
- Sizing
- Product Variants
website: http://zenpire.tech/
---
