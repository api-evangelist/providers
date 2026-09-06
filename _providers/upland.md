---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://api.prod.upland.me/developers-api
  baseurl_source: declared
  description: REST API for approved Upland third-party applications. Maps application users to Upland user IDs through a connection-code flow, exposes read-only player data (profile, balances, properties, NFTs, tra
  name: Upland Developers API
  slug: upland-developers-api
- baseURL: https://chain-history.upland.me
  baseurl_source: declared
  description: Public, unauthenticated Antelope (Leap 5.0.3) node and Hyperion 3.3.10 full-history API for Upland's own appchain, which replaced Upland's EOS deployment on 2025-04-26. Exposes the standard Antelope /
  name: Upland Appchain History & Chain API
  slug: upland-appchain-history-chain-api
artifact_total: 7
asyncapis:
- description: ''
  name: Upland Webhooks
  slug: upland-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://upland.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.upland.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.upland.me/upland-developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.prod.upland.me/developers-api/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.upland.me/upland-developers/playing-the-sandbox/get-started
- group: start
  title: ''
  type: SignUp
  url: https://developers.upland.me
- group: operate
  title: ''
  type: Support
  url: https://support.upland.me/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/upland
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upland.me/documents/Upland_Terms_of_Service_June_8_2026.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upland.me/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upland-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/upland-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upland-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upland-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upland-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upland-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upland-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upland-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upland-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/upland-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upland-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/upland-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/upland-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upland-rate-limits.yml
created: '2026-09-02'
description: 'Upland (Uplandme, Inc.) is a San Francisco-based Web3 metaverse company that maps virtual property onto real-world addresses, letting players buy, sell, trade and build on tokenized parcels of real cities using its in-world currency UPX and the SPARKLET token. Upland runs a public third-party Developer Program: the Upland Developers API is a documented REST contract (OpenAPI 3.0, 46 operations across Authentication, Upland User, Escrow Containers, Tournaments, Dev Shops, Application Usage and generic read-only endpoints) that lets an approved application map its own users to Upland user IDs, read a player''s profile, balances, properties and NFTs, place player assets into an application-scoped escrow container, run Rumble tournaments with UPX entry fees and prize distribution, and receive eighteen documented webhook notifications. A parallel sandbox environment mirrors production. Upland also operates its own Antelope (Leap 5.0.3) appchain, whose chain RPC and Hyperion full-history
  API are publicly callable and documented.'
image: https://www.upland.me/images/seo/graph.png?v=3
layout: provider
modified: '2026-09-02'
name: Upland
nav: Providers
network: true
overview: 'Upland publishes 2 APIs on the [APIs.io](https://apis.io/) network: Developers API and Appchain History & Chain API. Tagged areas include Metaverse, Web3, Gaming, Blockchain, and NFT.


  The Upland catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upland''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 18 more developer resources.'
plans:
- name: Upland Plans Pricing
  plan_count: 0
  slug: upland-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Upland Rate Limits
  slug: upland-rate-limits
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Upland Authentication
  slug: upland-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Upland Domain Security
  slug: upland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upland
tags:
- Metaverse
- Web3
- Gaming
- Blockchain
- NFT
- Virtual Real Estate
- Digital Assets
- Escrow
- Tournaments
- Antelope
- Webhooks
- Developer Platform
website: https://upland.me/
---
