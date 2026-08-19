---
access_model:
  confidence: high
  label: Paid · Zoopla membership required · credentials issued by Member Services
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  - terms-of-use
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Zoopla Agentic Access
  operation_count: 9
  slug: zoopla-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 3
apis:
- description: Poll-based REST API used by Zoopla member agents to retrieve consumer leads generated on the portal. Applicant leads (buyers and renters enquiring on a property) and appraisal leads (owners asking for
  name: Zoopla Leads API
  slug: zoopla-leads-api
- description: REST API that lets a member agent's CRM activate the Premium Listing product against a Zoopla listing, read the activation history for an account or a single listing_id, check whether a listing is pre
  name: Zoopla Premium Listing Activations API
  slug: zoopla-premium-listing-activations-api
- description: REST API for activating the Weekly Featured Property product on a Zoopla listing from an agency CRM, reading activation history across an account or for a single listingId, and checking whether a list
  name: Zoopla Weekly Featured Property (WFP) Activations API
  slug: zoopla-weekly-featured-property-activations-api
artifact_total: 32
asyncapis:
- description: API Evangelist derivation of Zoopla's Lead Push Service. Zoopla publishes no AsyncAPI document; this document is derived from the published push-service documentation at https://developers.zoopla.co.u
  name: Zoopla Lead Push Service
  slug: zoopla-leads-push-asyncapi
- description: ''
  name: Zoopla Leads Webhooks
  slug: zoopla-leads-webhooks
collections:
- collection_type: postman
  name: 01. Products API
  slug: postman-zoopla-products-api
- collection_type: open
  name: Leads API
  slug: open-zoopla-leads-api
- collection_type: open
  name: Premium Listing activations
  slug: open-zoopla-premium-listing-activations
- collection_type: open
  name: Weekly Featured Property (WFP) Activations
  slug: open-zoopla-weekly-featured-property-activations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoopla-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoopla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoopla-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoopla-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoopla-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoopla.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zoopla.co.uk/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zoopla.co.uk/pages/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.zoopla.co.uk/pages/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://business.zoopla.co.uk/contact-us
- group: operate
  title: ''
  type: Support
  url: https://support.zoopla.co.uk/hc/en-gb
- group: other
  title: ''
  type: Business
  url: https://business.zoopla.co.uk/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.houseful.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoopla-eng
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zoopla
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zoopla.co.uk/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zoopla.co.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zoopla.co.uk/pages/zoopla-apis
- group: auth
  title: ''
  type: Security
  url: https://www.zoopla.co.uk/vulnerability-disclosure/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zoopla-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zoopla-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/zoopla-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://support.zoopla.co.uk/hc/en-gb/article_attachments/360016811117/Products-API.json
- group: build
  title: ''
  type: Postman
  url: postman/zoopla-products-api.postman_collection.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zoopla-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zoopla-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoopla-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/zoopla-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoopla-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoopla-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zoopla-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zoopla-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zoopla-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/zoopla-leads-push-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zoopla-leads-webhooks.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zoopla-poll-leads.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zoopla-receive-lead-push.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zoopla-activate-premium-listing.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zoopla-activate-weekly-featured-property.md
created: '2026-07-26'
description: 'Zoopla Limited is one of the two dominant residential property portals in the United Kingdom, operating zoopla.co.uk alongside PrimeLocation under the Houseful group (formerly ZPG), which also owns the Alto/Jupix estate-agency CRM software and the Hometrack valuation and mortgage-risk business. In a market with no MLS and no cooperative listing standard, Zoopla sits at the demand end of the value chain — consumers search on the portal, and listings reach it from agency CRM systems rather than from a shared data pool. Its API posture reflects that position honestly: the old public Zoopla listings API on the Mashery-hosted developer.zoopla.co.uk portal has been retired and the site no longer serves a valid certificate, and the current developer documentation at developers.zoopla.co.uk states plainly that "the Zoopla listings API is no longer publicly available." What remains public is a small, real, machine-readable surface aimed at member estate agents and their CRM vendors
  — a Leads API for polling applicant and appraisal enquiries, a real-time lead Push service, and two product-activation APIs for Premium Listings and Weekly Featured Properties. The documentation and three Swagger/OpenAPI contracts are openly readable with no login, but credentials are not self-serve: you must already be a Zoopla member on a listings package, and client_id/client_secret are issued by Member Services after you send them a GPG public key. There is no RESO Web API or Data Dictionary certification, no OData $metadata document, and no Universal Property Identifier anywhere in Zoopla''s stack — RESO is a North American construct and the UK has not adopted it. Zoopla publishes no open data; the open property layer in the UK belongs to the public sector (HM Land Registry Price Paid and Ordnance Survey), not to the portals.'
examples:
- key_count: 6
  name: Zoopla Premium Listing Accepted 202
  slug: zoopla-premium-listing-accepted-202
- key_count: 6
  name: Zoopla Premium Listing Activated
  slug: zoopla-premium-listing-activated
- key_count: 1
  name: Zoopla Premium Listing Create Request
  slug: zoopla-premium-listing-create-request
- key_count: 2
  name: Zoopla Premium Listing Create With Highlights Request
  slug: zoopla-premium-listing-create-with-highlights-request
- key_count: 1
  name: Zoopla Premium Listing Duplicate Pending Error
  slug: zoopla-premium-listing-duplicate-pending-error
- key_count: 5
  name: Zoopla Premium Listing Error
  slug: zoopla-premium-listing-error
- key_count: 1
  name: Zoopla Premium Listing Highlights Patch Request
  slug: zoopla-premium-listing-highlights-patch-request
- key_count: 5
  name: Zoopla Premium Listing Pending
  slug: zoopla-premium-listing-pending
- key_count: 1
  name: Zoopla Push Applicant Lead
  slug: zoopla-push-applicant-lead
- key_count: 1
  name: Zoopla Push Appraisal Lead
  slug: zoopla-push-appraisal-lead
- key_count: 8
  name: Zoopla Wfp Accepted 202
  slug: zoopla-wfp-accepted-202
- key_count: 7
  name: Zoopla Wfp Activated
  slug: zoopla-wfp-activated
- key_count: 1
  name: Zoopla Wfp Create Request
  slug: zoopla-wfp-create-request
- key_count: 2
  name: Zoopla Wfp Create With Custom Details Request
  slug: zoopla-wfp-create-with-custom-details-request
- key_count: 1
  name: Zoopla Wfp Duplicate Pending Error
  slug: zoopla-wfp-duplicate-pending-error
- key_count: 6
  name: Zoopla Wfp Error
  slug: zoopla-wfp-error
- key_count: 6
  name: Zoopla Wfp Pending
  slug: zoopla-wfp-pending
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface (no hosted server published)
  slug: candidate-mcp-tool-surface-no-hosted-server-published
modified: '2026-07-26'
name: Zoopla
nav: Providers
network: true
overview: 'Zoopla publishes 3 APIs on the [APIs.io](https://apis.io/) network: Leads API, Premium Listing Activations API, and Weekly Featured Property (WFP) Activations API. Tagged areas include Real Estate, United Kingdom, Property Listings, Property Portal, and PropTech.


  The Zoopla catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Zoopla''s developer surface includes authentication, documentation, signup flow, support, getting-started guide, API reference, code examples, and 34 more developer resources.'
random_paper: 65
scopes:
- name: Zoopla Scopes
  scope_count: 3
  slug: zoopla-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 38.4
  delta: -6.4
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 42.3
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 13.2
  previous_composite: 44.8
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zoopla/refs/heads/main/screenshots/zoopla-2026-08-17T083116.png
security:
- kind: authentication
  name: Zoopla Authentication
  slug: zoopla-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoopla Domain Security
  slug: zoopla-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zoopla Vulnerability Disclosure
  slug: zoopla-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: zoopla
tags:
- Real Estate
- United Kingdom
- Property Listings
- Property Portal
- PropTech
- Rentals
- Estate Agents
- Leads
- CRM Integration
website: https://www.zoopla.co.uk/
---
