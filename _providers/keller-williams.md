---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Keller Williams Agentic Access
  operation_count: 7
  slug: keller-williams-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: The only Keller Williams API whose specification is published anonymously in the DevHub API catalog. The KW Worldwide Listings service returns Keller Williams Listing Service (KWLS) listings scoped to
  name: KW Worldwide Listings Search API
  slug: keller-williams-worldwide-listings-search-api
- description: Keller Williams uses OpenID Connect on top of OAuth 2.0 to grant a partner application access to an individual KW user's Command data. The authorization server at partners.api.kw.com/idp serves a publ
  name: KW Partner Identity API (OpenID Connect)
  slug: keller-williams-partner-identity-api
- description: 'The partner-facing surface behind the KW Marketplace, where vendors sell products to Keller Williams agents. Keller Williams pushes subscription lifecycle events — subscription creation, subscription '
  name: KW Marketplace Subscription & Metered Billing API
  slug: keller-williams-marketplace-subscription-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Resolve the KW controlled vocabularies, create a KWLS listing, then read it back to confirm it indexed.
  name: Publish a KW Worldwide listing
  slug: keller-williams-publish-listing
artifact_total: 11
asyncapis:
- description: ''
  name: Keller Williams Marketplace Webhooks
  slug: keller-williams-marketplace-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keller-williams-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keller-williams-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keller-williams-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keller-williams-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keller-williams-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keller-williams-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keller-williams-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kw.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.kw.com/base-path-migration-guide
- group: design
  title: ''
  type: Conformance
  url: conformance/keller-williams-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keller-williams-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/keller-williams-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keller-williams-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keller-williams-marketplace-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keller-williams-publish-listing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keller-williams-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.kw.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kw.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kw.com/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kw.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kw.com/docs/listingskww/1/overview
- group: other
  title: ''
  type: APICatalog
  url: https://developer.kw.com/apis
- group: start
  title: ''
  type: SignUp
  url: https://share.hsforms.com/2JQHe7zfKRLSo_cXKjy-5nwbg45/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.kw.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.kw.com/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://developer.kw.com/api-license-agreement
- group: operate
  title: ''
  type: Support
  url: https://developer.kw.com/support
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.kw.com/
- group: company
  title: ''
  type: News
  url: https://kwri.kw.com/
- group: company
  title: ''
  type: Blog
  url: https://outfront.kw.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://outfront.kw.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KWRI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keller-williams-realty
created: '2026-07-26'
description: 'Keller Williams Realty, Inc. (KWRI) is an Austin, Texas headquartered residential real estate franchisor and the largest real estate brokerage franchise in the United States by agent count, operating more than 1,000 market centers worldwide through independently owned and operated offices. In the value chain Keller Williams sits at the brokerage and agent-platform layer, not the data-cooperative layer: it franchises brokerages, and it builds and operates KW Command, a proprietary agent operating system for lead, contact, task, listing, opportunity and marketing management, plus the KW Marketplace where third-party vendors sell integrated products to KW agents. Its API posture is real but partner-gated. Keller Williams runs a genuine Apigee-backed developer portal (DevHub) at developer.kw.com with a live gateway at partners.api.kw.com and a sandbox at sandbox.partners.api.kw.com, an OpenID Connect authorization server whose discovery document is publicly readable, and a published
  API License Agreement. Access is not self-serve: a developer must submit a partnership application through the "Apply to Integrate" form, be approved by KWRI, receive a DevHub account, then sign the KW API License Agreement and Terms of Use before receiving an API key and secret. Only one API — KW Worldwide Listings Search — is visible anonymously in the API catalog; the rest of the catalog (Command MC, Contact and Lead Data, Tasks, Opportunity/Deal/ Transaction Data, User/Organization/Role Information, Marketplace Subscription Management, Internal) is behind a SAML member login. On the sector''s central question, Keller Williams carries no RESO posture at all: it is absent from the RESO certification directory, no RESO Web API, Data Dictionary, OData $metadata or Universal Property Identifier reference appears anywhere in its developer portal or specification, and its own listings spec states in its description that the service "is not a substitution for or tied to any Multiple Listings
  Services database records." This is a brokerage''s own listing and CRM data behind a commercial partner agreement, not licensed MLS data behind a certified standard.'
examples:
- key_count: 6
  name: Keller Williams Listings Search Examples
  slug: keller-williams-listings-search-examples
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-26'
name: Keller Williams
nav: Providers
network: true
overview: 'Keller Williams publishes 1 API on the [APIs.io](https://apis.io/) network: KW Worldwide Listings Search API. Tagged areas include Real Estate, United States, Residential Real Estate, Brokerage, and Franchise.


  The Keller Williams catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Keller Williams'' developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, support, product news, and 27 more developer resources.'
random_paper: 81
scopes:
- name: Keller Williams Scopes
  scope_count: 40
  slug: keller-williams-scopes
  summary_line: 40 scopes · authorizationCode/implicit/clientCredentials/tokenExchange/jwtBearer
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.6
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Keller Williams Authentication
  slug: keller-williams-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Keller Williams Domain Security
  slug: keller-williams-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: keller-williams
tags:
- Real Estate
- United States
- Residential Real Estate
- Brokerage
- Franchise
- Property Listings
- PropTech
- Agent Platform
- CRM
- Partner APIs
- Marketplace
- Austin Texas
website: https://www.kw.com/
---
