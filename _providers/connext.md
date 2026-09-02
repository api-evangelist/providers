---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Batched Intents API from Everclear — 2 operation(s) for batched intents.
  name: Everclear Batched Intents API
  slug: connext-batched-intents-api
- description: The Configs API from Everclear — 1 operation(s) for configs.
  name: Everclear Configs API
  slug: connext-configs-api
- description: The History API from Everclear — 1 operation(s) for history.
  name: Everclear History API
  slug: connext-history-api
- description: The Intents API from Everclear — 4 operation(s) for intents.
  name: Everclear Intents API
  slug: connext-intents-api
- description: The Invoices API from Everclear — 3 operation(s) for invoices.
  name: Everclear Invoices API
  slug: connext-invoices-api
- description: The Routes API from Everclear — 2 operation(s) for routes.
  name: Everclear Routes API
  slug: connext-routes-api
- description: The Solana API from Everclear — 2 operation(s) for solana.
  name: Everclear Solana API
  slug: connext-solana-api
- description: The Tron API from Everclear — 1 operation(s) for tron.
  name: Everclear Tron API
  slug: connext-tron-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chimera Batched Intents API
  slug: open-connext-batched-intents-api
- collection_type: open
  name: Chimera Configs API
  slug: open-connext-configs-api
- collection_type: open
  name: Chimera History API
  slug: open-connext-history-api
- collection_type: open
  name: Chimera Intents API
  slug: open-connext-intents-api
- collection_type: open
  name: Chimera Invoices API
  slug: open-connext-invoices-api
- collection_type: open
  name: Chimera Routes API
  slug: open-connext-routes-api
- collection_type: open
  name: Chimera Solana API
  slug: open-connext-solana-api
- collection_type: open
  name: Chimera Tron API
  slug: open-connext-tron-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.connext.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.everclear.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.everclear.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.everclear.org/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.everclear.org/developers/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.connext.network/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everclearorg
- group: company
  title: ''
  type: Blog
  url: https://blog.connext.network/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/connext-everclear-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/connext-everclear-overlay.yaml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/connext-everclear-subgraph.graphql
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connext-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/connext-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/connext-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/connext-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connext-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/connext-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/connext-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/connext-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connext-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connext-conformance.yml
created: '2026-08-09'
description: Everclear (previously Connext) was a crosschain clearing layer for the intent economy. It netted bidirectional rebalancing flows between solvers, fillers and bridges across chains so that liquidity moved once instead of many times, cutting rebalancing cost by up to 10x. Rebalancers deposited into a Spoke contract on any supported chain and named the destination chains they wanted funds on; a Hub contract on the Everclear clearing chain netted those intents against opposing flow, and any intent that could not be netted became a discounted invoice that arbitrageurs could purchase — a dutch-auction style mechanism that kept the system solvent without a central operator. Everclear shipped a public, unauthenticated REST API ("Chimera API") that read indexed intents, invoices, supported assets, route quotes and settlement history, and that built unsigned EVM, Solana and Tron transactions for callers to sign with their own wallet. On 2026-05-21 the team announced the protocol, the
  Everclear Foundation and the labs unit had all been wound down; the protocol is sunset, the API host no longer answers, and this profile is an archival record of the developer surface Everclear published.
image: https://raw.githubusercontent.com/everclearorg/brand/main/Everclear-Logo-Black.png
layout: provider
modified: '2026-08-09'
name: Everclear
nav: Providers
network: true
overview: 'Everclear publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Batched Intents API, Configs API, History API, and 5 more. Tagged areas include Company, Blockchain, Cryptocurrency, Web3, and Interoperability.


  Everclear''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 46.5
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 33.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Connext Authentication
  slug: connext-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Connext Domain Security
  slug: connext-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connext
tags:
- Company
- Blockchain
- Cryptocurrency
- Web3
- Interoperability
- Cross-Chain
- Bridging
- Settlement
- Liquidity
- Intents
- DeFi
- Chain Abstraction
- Defunct
website: https://www.connext.network/
---
