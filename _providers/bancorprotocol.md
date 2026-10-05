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
- description: The Bancor Network REST API provides JSON endpoints for token, price, and pool information.
  name: Bancor Network REST API
  slug: bancor-network-rest-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/conventions/bancorprotocol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bancorprotocol-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/llms/bancorprotocol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bancorprotocol-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/well-known/bancorprotocol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bancorprotocol-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/hosts/bancorprotocol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bancorprotocol-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/vendors/bancorprotocol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bancorprotocol-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://support.bancor.network/resources/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bancorprotocol/refs/heads/main/security/bancorprotocol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bancorprotocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bancor.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bancor.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bancor.network/guides/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bancor.network/about-bancor-network/bancor-v3.md
- group: operate
  title: ''
  type: Support
  url: https://support.bancor.network
- group: company
  title: ''
  type: Blog
  url: https://blog.bancor.network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bancorprotocol
coverage:
  checked: '2026-09-27'
  detail: Documentation is available as markdown but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://docs.bancor.network/guides/rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bancorprotocol is a decentralized finance protocol that provides on‑chain liquidity, automated market making, and token conversion across multiple blockchains. Founded in 2017, Bancor enables users to trade assets instantly without order books, offering features like single‑sided liquidity provision, impermanent loss protection, and a suite of tools for developers to integrate on‑chain market infrastructure into their applications.
image: https://framerusercontent.com/assets/Ge6tkw9lQSaRvH2tTNsL5262xQ.png
layout: provider
modified: '2026-09-27'
name: Bancorprotocol
nav: Providers
network: true
overview: 'Bancorprotocol publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decentralized Finance, Liquidity, Automated Market Maker, Blockchain, and Token Conversion.


  Bancorprotocol''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bancorprotocol Domain Security
  slug: bancorprotocol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bancorprotocol
tags:
- Decentralized Finance
- Liquidity
- Automated Market Maker
- Blockchain
- Token Conversion
website: https://bancor.network
---
