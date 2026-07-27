---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Perchwell Agentic Access
  operation_count: 18
  slug: perchwell-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 8
apis:
- description: Legacy RETS 1.7 server (DMQL2 query language) providing backward compatibility for RETS clients, exposing Listing, Agent, Brokerage, Office, and OpenHouse resources via the Search and GetMetadata tran
  name: Perchwell RETS API
  slug: perchwell-rets-api
- description: Real estate sale and rental listing feed.
  name: Perchwell Listings API
  slug: perchwell-listings-api
- description: RESO Media resource (nested within Property).
  name: Perchwell Media API
  slug: perchwell-media-api
- description: RESO Member resource (agents).
  name: Perchwell Member API
  slug: perchwell-member-api
- description: OData service metadata.
  name: Perchwell Metadata API
  slug: perchwell-metadata-api
- description: RESO Office resource.
  name: Perchwell Office API
  slug: perchwell-office-api
- description: RESO OpenHouse resource.
  name: Perchwell OpenHouse API
  slug: perchwell-openhouse-api
- description: RESO Property resource (listings; Media is nested).
  name: Perchwell Property API
  slug: perchwell-property-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perchwell-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://perchwell.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.perchwell.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.perchwell.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.perchwell.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.perchwell.com/#/json_api_getting_started
- group: company
  title: ''
  type: Blog
  url: https://www.perchwell.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@perchwell.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perchwell
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perchwell.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perchwell.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.perchwell.com/accounts/sign_in
- group: operate
  title: ''
  type: HelpCenter
  url: http://support.perchwell.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perchwell-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/perchwell-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perchwell-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/perchwell-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/perchwell-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/perchwell-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perchwell-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/perchwell-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/perchwell-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/perchwell-json-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/perchwell-reso-web-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perchwell-domain-security.yml
created: '2026-07-17'
description: 'Perchwell is a modern, unified MLS (Multiple Listing Service) technology platform used by MLS organizations, brokerages, and real estate agents across the United States. Founded in 2015 and headquartered in New York City, Perchwell provides search, client collaboration, listing add/edit, branded reports, and market analytics on a cloud-native, RESO-certified foundation. For developers and data partners, Perchwell operates three real estate data APIs: a simple token-authenticated JSON API for listing feeds, a RESO Data Dictionary certified RESO Web API (OData 4.01) exposing the standard Property, Member, Office, OpenHouse, and Media resources with full read/write support, and a legacy RETS 1.7 server for backward compatibility. Customers include CRMLS, Baldwin REALTORS, Engel & Volkers, and Keller Williams. Perchwell is SOC 2 compliant and backed by Lux Capital, Founders Fund, and Starwood Capital.'
image: https://perchwell.com/_media/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: perchwell-mcp.yml
  slug: perchwell-mcpyml
modified: '2026-07-20'
name: Perchwell
nav: Providers
network: true
overview: 'Perchwell publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Listings API, Media API, Member API, and 4 more. Tagged areas include Company, Real Estate, MLS, Listings, and Property Data.


  Perchwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 52.1
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 45.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Perchwell Authentication
  slug: perchwell-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Perchwell Domain Security
  slug: perchwell-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: perchwell
tags:
- Company
- Real Estate
- MLS
- Listings
- Property Data
- RESO
- RETS
- OData
- Real Estate Data
website: https://perchwell.com
---
