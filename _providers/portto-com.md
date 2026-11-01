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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Blocto provides SDKs and wallet services for developers to integrate blockchain functionality.
  name: Blocto API
  slug: blocto-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/portto-com/well-known/portto-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portto-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/portto-com/hosts/portto-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portto-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/portto-com/vendors/portto-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portto-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.portto.com/hc/en-us
- group: auth
  href: https://artifacts.apis.io/portto-com/security/portto-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portto-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portto.com
coverage:
  checked: '2026-10-25'
  detail: Documentation is served as markdown via a GitBook site requiring query parameters for content, with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.blocto.app/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Blocto is a blockchain wallet and developer platform that enables users to manage digital assets across multiple blockchains and interact with decentralized applications (dApps) through a unified interface. Founded in 2020, Blocto provides SDKs, APIs, and tools for developers to integrate wallet functionality, token management, and transaction signing into their applications, supporting chains such as Solana, Ethereum, Polygon, and more. The platform emphasizes a seamless user experience, cross-chain compatibility, and security features for both consumers and enterprises.
image: https://ik.imagekit.io/judimpo/join-game-judimpo.png?updatedAt=1775356285813
layout: provider
modified: '2026-10-25'
name: Blocto
nav: Providers
network: true
overview: 'Blocto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Wallet, DeveloperPlatform, and Crypto.


  Blocto''s developer surface includes support and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Portto Com Domain Security
  slug: portto-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portto-com
tags:
- Company
- Blockchain
- Wallet
- DeveloperPlatform
- Crypto
- dApp
website: https://portto.com
---
