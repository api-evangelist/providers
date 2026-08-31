---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: Domain Group Agentic Access
  operation_count: 221
  slug: domain-group-agentic-access
  summary_line: 221 operations · 76 acting
api_count: 3
apis:
- description: The AddressLocators API from Domain Group — 1 operation(s) for addresslocators.
  name: Domain Group Address Locators API
  slug: domain-group-addresslocators-api
- description: The Agencies API from Domain Group — 5 operation(s) for agencies.
  name: Domain Group Agencies API
  slug: domain-group-agencies-api
- description: The Agents API from Domain Group — 4 operation(s) for agents.
  name: Domain Group Agents API
  slug: domain-group-agents-api
- description: The Authorities API from Domain Group — 6 operation(s) for authorities.
  name: Domain Group Authorities API
  slug: domain-group-authorities-api
- description: The CampaignReporting API from Domain Group — 2 operation(s) for campaignreporting.
  name: Domain Group Campaign Reporting API
  slug: domain-group-campaignreporting-api
- description: The Dataset API from Domain Group — 1 operation(s) for dataset.
  name: Domain Group Dataset API
  slug: domain-group-dataset-api
- description: The Demographics API from Domain Group — 1 operation(s) for demographics.
  name: Domain Group Demographics API
  slug: domain-group-demographics-api
- description: The Disclaimers API from Domain Group — 2 operation(s) for disclaimers.
  name: Domain Group Disclaimers API
  slug: domain-group-disclaimers-api
- description: The Enquiries API from Domain Group — 2 operation(s) for enquiries.
  name: Domain Group Enquiries API
  slug: domain-group-enquiries-api
- description: The Leadscope API from Domain Group — 2 operation(s) for leadscope.
  name: Domain Group Leadscope API
  slug: domain-group-leadscope-api
- description: The Listings API from Domain Group — 18 operation(s) for listings.
  name: Domain Group Listings API
  slug: domain-group-listings-api
- description: The ListingSearch API from Domain Group — 2 operation(s) for listingsearch.
  name: Domain Group Listing Search API
  slug: domain-group-listingsearch-api
- description: The Locations API from Domain Group — 1 operation(s) for locations.
  name: Domain Group Locations API
  slug: domain-group-locations-api
- description: The Me API from Domain Group — 3 operation(s) for me.
  name: Domain Group Me API
  slug: domain-group-me-api
- description: The PreMarket API from Domain Group — 2 operation(s) for premarket.
  name: Domain Group Pre Market API
  slug: domain-group-premarket-api
- description: The Products API from Domain Group — 8 operation(s) for products.
  name: Domain Group Products API
  slug: domain-group-products-api
- description: The Projects API from Domain Group — 6 operation(s) for projects.
  name: Domain Group Projects API
  slug: domain-group-projects-api
- description: The Properties API from Domain Group — 10 operation(s) for properties.
  name: Domain Group Properties API
  slug: domain-group-properties-api
- description: The PropertyAvm API from Domain Group — 2 operation(s) for propertyavm.
  name: Domain Group Property Avm API
  slug: domain-group-propertyavm-api
- description: The PropertyFeatures API from Domain Group — 1 operation(s) for propertyfeatures.
  name: Domain Group Property Features API
  slug: domain-group-propertyfeatures-api
- description: The PropertyLike API from Domain Group — 1 operation(s) for propertylike.
  name: Domain Group Property Like API
  slug: domain-group-propertylike-api
- description: The PropertyRadar API from Domain Group — 7 operation(s) for propertyradar.
  name: Domain Group Property Radar API
  slug: domain-group-propertyradar-api
- description: The PropertySearch API from Domain Group — 1 operation(s) for propertysearch.
  name: Domain Group Property Search API
  slug: domain-group-propertysearch-api
- description: The PropertyZoningPerils API from Domain Group — 1 operation(s) for propertyzoningperils.
  name: Domain Group Property Zoning Perils API
  slug: domain-group-propertyzoningperils-api
- description: The SalesResults API from Domain Group — 5 operation(s) for salesresults.
  name: Domain Group Sales Results API
  slug: domain-group-salesresults-api
- description: The Schools API from Domain Group — 2 operation(s) for schools.
  name: Domain Group Schools API
  slug: domain-group-schools-api
- description: The Statistics API from Domain Group — 6 operation(s) for statistics.
  name: Domain Group Statistics API
  slug: domain-group-statistics-api
- description: The Webhooks API from Domain Group — 2 operation(s) for webhooks.
  name: Domain Group Webhooks API
  slug: domain-group-webhooks-api
artifact_total: 38
asyncapis:
- description: Event surface for the Domain Public API. Domain does not publish an AsyncAPI document; this one is generated by API Evangelist strictly from Domain's published webhook documentation at https://develop
  name: Domain Group Webhooks
  slug: domain-group-webhooks-asyncapi
- description: ''
  name: Domain Group Webhooks
  slug: domain-group-webhooks
collections:
- collection_type: open
  name: Domain Public API
  slug: open-domain-group-openapi-latest
- collection_type: open
  name: Domain Public API
  slug: open-domain-group-openapi-v1
- collection_type: open
  name: Domain Public API
  slug: open-domain-group-openapi-v2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/domain-group-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/domain-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domain-group-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/domain-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/domain-group-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.domain.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.domain.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.domain.com.au/docs/latest
- group: docs
  title: ''
  type: APIReference
  url: https://developer.domain.com.au/docs/latest/apis
- group: start
  title: ''
  type: SignUp
  url: https://developer.domain.com.au/docs/latest/getting-started/creating-first-project
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.domain.com.au/docs/latest/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.domain.com.au/docs/latest/authentication
- group: docs
  title: ''
  type: OpenAPI
  url: https://developer.domain.com.au/static/latest/media/latest/openapi.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/domain-group-openid-configuration.json
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.domain.com.au/v1/.well-known/openid-configuration
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.domain.com.au/docs/latest/conventions/rate-limiting
- group: start
  title: ''
  type: Sandbox
  url: https://developer.domain.com.au/docs/latest/conventions/sandbox
- group: design
  title: ''
  type: Conventions
  url: https://developer.domain.com.au/docs/latest/conventions
- group: design
  title: ''
  type: Versioning
  url: https://developer.domain.com.au/docs/latest/conventions/versioning
- group: build
  title: ''
  type: Libraries
  url: https://developer.domain.com.au/docs/latest/libraries
- group: operate
  title: ''
  type: Support
  url: https://developer.domain.com.au/docs/latest/support
- group: operate
  title: ''
  type: SLA
  url: https://developer.domain.com.au/docs/latest/support/sla
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domain.com.au/group/api-terms-and-conditions/
- group: other
  title: ''
  type: Policies
  url: https://developer.domain.com.au/docs/latest/support/policies
- group: other
  title: ''
  type: Troubleshooting
  url: https://developer.domain.com.au/docs/latest/troubleshooting
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/domain-group
- group: build
  title: ''
  type: Packages
  url: packages/domain-group-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/domain-group-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/domain-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/domain-group-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/domain-group-latest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/domain-group-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/domain-group-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/domain-group-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/domain-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/domain-group-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.domain.com.au/docs/latest/conventions/versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/domain-group-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/domain-group-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/domain-group-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/domain-group-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/domain-group-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/domain-group-openapi-latest.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/domain-group-openapi-v1.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/domain-group-openapi-v2.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/domain-group-property-valuation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/domain-group-listing-search.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/domain-group-suburb-market-data.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/domain-group-listing-management.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/domain-group-webhook-subscriptions.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/domain-group-jwks.json
created: '2026-07-26'
description: 'Domain Group (Domain Holdings Australia Ltd, trading as domain.com.au) is the second of Australia''s two national residential property portals, alongside REA Group''s realestate.com.au, and since 27 August 2025 has been a wholly owned subsidiary of CoStar Group. Headquartered in Sydney, Domain operates the domain.com.au consumer marketplace plus commercial, agent, and developer-project brands, and sits in the middle of the Australian value chain between selling and leasing agencies on one side and buyers, renters, banks, and PropTech builders on the other. Unlike most of the real estate sector, Domain runs a genuine, self-serve public developer portal at developer.domain.com.au: a developer signs up with GitHub, Google, or email, creates a project, and is immediately granted the "Agents & Listings" and "Properties & Locations" packages, with the remaining eleven packages - Address Suggestions, Campaign reporting, Listings Management, Price Estimation, Property Enrichment, Property
  Package, PropertyRadar, Rental AVM, Schools Data, and Webhooks - added per project and negotiated with an account manager. Domain publishes three machine-readable OpenAPI 3.0.4 documents (latest, v1, v2) directly from its Libraries page, backs them with an OpenID Connect discovery document at auth.domain.com.au, and serves everything from api.domain.com.au behind API-key or OAuth 2.0 (client credentials, authorization code, implicit) credentials. Write access is a different gate entirely: uploading or updating listings requires sandbox sign-off by email to api@domain.com.au and written permission from the principal agent of each agency, making listing management broker-authorised even though the read surface is self-serve. Domain carries no RESO Web API or RESO Data Dictionary certification, exposes no OData $metadata document and no Universal Property Identifier - RESO is a North American NAR-driven standard with no presence in the Australian portal duopoly - and it publishes no open,
  unlicensed dataset; all data is licensed under the Domain Group API Terms and Conditions.'
image: https://s.domainstatic.com.au/domain/144.png
layout: provider
mcp_servers:
- description: ''
  name: Domain Group MCP Server
  slug: domain-group-mcp-server
modified: '2026-07-26'
name: Domain Group
nav: Providers
network: true
overview: 'Domain Group publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Address Locators API, Agencies API, Agents API, and 25 more. Tagged areas include Real-Estate, Australia, Property Listings, Property Data, and Valuation.


  The Domain Group catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Domain Group''s developer surface includes authentication, documentation, API reference, signup flow, getting-started guide, sandbox, support, and 45 more developer resources.'
random_paper: 16
scopes:
- name: Domain Group Scopes
  scope_count: 25
  slug: domain-group-scopes
  summary_line: 25 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 62.6
    developer_ergonomics: 63.7
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domain-group/refs/heads/main/screenshots/domain-group-2026-07-27T125337.png
security:
- kind: authentication
  name: Domain Group Authentication
  slug: domain-group-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Domain Group Domain Security
  slug: domain-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: domain-group
tags:
- Real-Estate
- Australia
- Property Listings
- Property Data
- Valuation
- AVM
- Rentals
- Listing Management
- PropTech
- Portal Marketplace
website: https://www.domain.com.au/
---
