---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Realtor Ca Agentic Access
  operation_count: 34
  slug: realtor-ca-agentic-access
  summary_line: 34 operations · 2 acting
api_count: 4
apis:
- description: The REALTOR.ca Data Distribution Facility (DDF®) Web API is CREA's national listing distribution surface, exposed as OData v4-style read endpoints over Property, Member, Office, OpenHouse and Destinat
  name: REALTOR.ca DDF Web API
  slug: realtor-ca-ddf-web-api
- description: The DDF® Lead API accepts an email lead for a REALTOR® from a downstream site. Because member email addresses are deliberately excluded from the DDF® Web API payloads, real estate advertising websites
  name: REALTOR.ca DDF Lead API
  slug: realtor-ca-ddf-lead-api
- description: A fire-and-forget listing-event logging service documented inside the DDF® Web API documentation. Sites and applications displaying DDF® listings call it to record View, Click and email_realtor events
  name: CREA Analytics Web Service
  slug: crea-analytics-web-service
- description: CREA's OAuth 2.0 / OpenID Connect authorization server at identity.crea.ca, which issues the access tokens every DDF® Web API call requires. Its discovery document is served anonymously and advertises
  name: CREA Identity Server
  slug: crea-identity-server
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/realtor-ca-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtor-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.realtor.ca/
- group: company
  title: ''
  type: Website
  url: https://www.crea.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://ddfapi-docs.realtor.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://www.crea.ca/ddf/
- group: docs
  title: ''
  type: APIReference
  url: https://ddfapi-docs.realtor.ca/
- group: start
  title: ''
  type: GettingStarted
  url: https://ddfapi-docs.realtor.ca/#section/Quickstart-Overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.crea.ca/ddf/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crea.ca/ddf/member-policy-and-rules/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crea.ca/privacy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.crea.ca/legal/
- group: operate
  title: ''
  type: Support
  url: https://support.crea.ca/
- group: operate
  title: ''
  type: Forum
  url: https://crea.vanillacommunity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.crea.ca/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.crea.ca/feed/
- group: operate
  title: ''
  type: ChangeLog
  url: https://ddfapi-docs.realtor.ca/releasenotes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/realtor-ca-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtor-ca-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtor-ca-crea-identity-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtor-ca-auth0-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/realtor-ca-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/realtor-ca-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/realtor-ca-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/realtor-ca-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/realtor-ca-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/realtor-ca-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/realtor-ca-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/realtor-ca-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/realtor-ca-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.crea.ca/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/realtor-ca-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/realtor-ca-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/realtor-ca-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realtor-ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canadian-real-estate-association/
created: '2026-07-26'
description: 'REALTOR.ca is the national residential property listing portal of the Canadian Real Estate Association (CREA), the cooperative trade association representing roughly 160,000 REALTORS® across some 60 member boards and associations in Canada. Unlike the United States, where roughly 500 independent MLSs each run their own data pipe, Canadian listing distribution is consolidated through CREA''s REALTOR.ca Data Distribution Facility (DDF®), a single national syndication service that normalizes MLS® System data from member boards and republishes it to member websites, franchisor sites, real estate advertising websites and technology providers. CREA sits squarely in the middle of the Canadian value chain — it owns the consumer portal, the national listing pool, and the syndication rails that every downstream site depends on. Its API posture is real but closed: the DDF® Web API is a genuine OData surface at https://ddfapi.realtor.ca/odata/v1 with public, browsable documentation and
  a downloadable OpenAPI 3.0.4 description, yet every endpoint (including the OData $metadata document) returns 401 without a Bearer token, and tokens are only issued via client_credentials against identity.crea.ca using data-feed credentials that a REALTOR® or broker owner must first create and link in the member portal. CREA is a RESO member and states its data is normalized to the RESO Data Dictionary, but no CREA entry could be confirmed in the RESO certification directory, so this profile records the DDF® Web API as RESO-aligned rather than RESO-certified. There is no self-serve developer signup, no sandbox, no open data product, and no public consumer search API for realtor.ca itself.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realtor-ca.png
layout: provider
mcp_servers:
- description: ''
  name: realtor-ca-mcp.yml
  slug: realtor-ca-mcpyml
modified: '2026-07-26'
name: REALTOR.ca
nav: Providers
network: true
overview: 'REALTOR.ca publishes 2 APIs on the [APIs.io](https://apis.io/) network: DDF Web API and DDF Lead API. Tagged areas include Real Estate, Canada, Property Listings, MLS, and RESO.


  REALTOR.ca''s developer surface includes documentation, API reference, getting-started guide, legal docs, support, engineering blog, changelog, and 30 more developer resources.'
random_paper: 18
scopes:
- name: Realtor Ca Scopes
  scope_count: 5
  slug: realtor-ca-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: thin
  composite: 35.8
  delta: -3.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Realtor Ca Authentication
  slug: realtor-ca-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Realtor Ca Domain Security
  slug: realtor-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Realtor Ca Vulnerability Disclosure
  slug: realtor-ca-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: realtor-ca
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- RESO
- IDX
- Listing Syndication
- PropTech
- OData
- Rentals
website: https://www.realtor.ca/
---
