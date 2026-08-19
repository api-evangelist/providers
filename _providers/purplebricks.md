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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 76
  human_in_the_loop: 2
  name: Purplebricks Agentic Access
  operation_count: 205
  slug: purplebricks-agentic-access
  summary_line: 205 operations · 76 acting · 2 human-in-the-loop
api_count: 13
apis:
- description: 'The largest of the publicly-reachable Purplebricks microservice APIs (86 v1 paths plus an 11-path v2), covering the property record end to end: active, preactive, inactive and withdrawn properties, pr'
  name: Purplebricks Property API
  slug: purplebricks-property-api
- description: 'Identity and account service for Purplebricks customers: authentication, user records, email confirmation, phone verification, marketing preferences and the expert-created account path. Bearer-token p'
  name: Purplebricks Account API
  slug: purplebricks-account-api
- description: 'Free-valuation funnel service: valuation intent capture, lead capture, postcode resolution, valuation reports, follow-up scheduling and a Salesforce diary pilot, plus a v2 valuation surface. This is t'
  name: Purplebricks Valuations API
  slug: purplebricks-valuations-api
- description: 'Viewing and appointment service: appointments, open days, property access details, per-property and per-user viewing surfaces, and a Bland voice-agent integration surface. Documents 409 conflict and 4'
  name: Purplebricks Viewings API
  slug: purplebricks-viewings-api
- description: 'Threaded messaging between customers, sellers and local property experts: message threads, individual messages, read state, system messages and cursor-paginated thread listings, with a v2 thread surfa'
  name: Purplebricks Messaging API
  slug: purplebricks-messaging-api
- description: Lettings integration service run by the Team Integrations squad. Creates valuation, viewing and offer enquiries in street.co.uk, handles inbound street.co.uk listing webhooks, exposes the pre-instruct
  name: Purplebricks Lettings API
  slug: purplebricks-lettings-api
- description: 'Portal syndication service exposing Rightmove, Zoopla and OnTheMarket branch records alongside property operations. This is the machine-readable trace of the UK no-MLS seam: an agency pushing branch a'
  name: Purplebricks Branch API
  slug: purplebricks-branch-api
- description: Outbound and inbound communication service covering the contact-us surface, customer emails and TPS (Telephone Preference Service) screening — the UK direct-marketing suppression check that any regula
  name: Purplebricks Communications API
  slug: purplebricks-communications-api
- description: Conveyancing quote service run by PB Digital, generating and retrieving conveyancing quotes for the legal leg of a Purplebricks sale.
  name: Purplebricks Conveyancing API
  slug: purplebricks-conveyancing-api
- description: Small agent-experience service exposing team lookups for the local property experts who staff the Purplebricks model in place of high-street branches.
  name: Purplebricks Agent API
  slug: purplebricks-agent-api
- description: Single-surface feedback management service used to manage viewing and vendor feedback across the platform.
  name: Purplebricks Feedback API
  slug: purplebricks-feedback-api
- description: Platform workflow service exposing workflow steps and an instruct-availability check that gates whether a seller can be instructed at a given point in the journey.
  name: Purplebricks Workflow API
  slug: purplebricks-workflow-api
- description: Agent-facing microservice that reads and toggles Outlook calendar synchronisation for a local property expert. The only Purplebricks API path disclosed in robots.txt, and the thread that led to the re
  name: Purplebricks Outlook Sync API
  slug: purplebricks-outlook-sync-api
artifact_total: 33
asyncapis:
- description: ''
  name: Purplebricks Webhooks
  slug: purplebricks-webhooks
collections:
- collection_type: open
  name: Purplebricks Account API 1 - Platform
  slug: open-purplebricks-account-v1
- collection_type: open
  name: Purplebricks.Agent.Api 1.0 - Squad Agents Experience
  slug: open-purplebricks-agent-v1
- collection_type: open
  name: Purplebricks.Branch.Api 1.0 - Squad Agents Experience
  slug: open-purplebricks-branch-v1
- collection_type: open
  name: Purplebricks.Communications.Api 1.0 - Core Team
  slug: open-purplebricks-communications-v1
- collection_type: open
  name: PB Conveyancing Api 1.0 - PB Digital
  slug: open-purplebricks-conveyancing-v1
- collection_type: open
  name: Purplebricks Feedback API 1 - Core Squad
  slug: open-purplebricks-feedback-v1
- collection_type: open
  name: Purplebricks.Lettings.Api 1 - Team Integrations
  slug: open-purplebricks-lettings-v1
- collection_type: open
  name: Purplebricks.Messaging.Api 1.0 - Backend
  slug: open-purplebricks-messaging-v1
- collection_type: open
  name: Purplebricks.Messaging.Api 2.0 - Backend
  slug: open-purplebricks-messaging-v2
- collection_type: open
  name: Purplebricks.Microservice.Outlook.Api 1.0 - Squad Agents and Intel
  slug: open-purplebricks-outlook-v1
- collection_type: open
  name: Purplebricks Property API 1.0 - Platform
  slug: open-purplebricks-property-v1
- collection_type: open
  name: Purplebricks Property API 2.0 - Platform
  slug: open-purplebricks-property-v2
- collection_type: open
  name: Purplebricks.Valuations.Api 1.0 - Core
  slug: open-purplebricks-valuations-v1
- collection_type: open
  name: Purplebricks.Valuations.Api 2 - Core
  slug: open-purplebricks-valuations-v2
- collection_type: open
  name: Purplebricks.Viewings.Api 1.0 - Customer Experience
  slug: open-purplebricks-viewings-v1
- collection_type: open
  name: Purplebricks Workflow API 1.0 - Platform
  slug: open-purplebricks-workflow-v1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/purplebricks-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/purplebricks-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.purplebricks.co.uk/
- group: other
  title: ''
  type: PropertySearch
  url: https://www.purplebricks.co.uk/search/property-for-sale
- group: other
  title: ''
  type: PropertySearch
  url: https://www.purplebricks.co.uk/search/property-to-rent
- group: commercial
  title: ''
  type: HousePrices
  url: https://www.purplebricks.co.uk/house-prices
- group: other
  title: ''
  type: Agents
  url: https://www.purplebricks.co.uk/estate-agents
- group: other
  title: ''
  type: Landlords
  url: https://www.purplebricks.co.uk/landlords
- group: start
  title: ''
  type: PortalDistribution
  url: https://www.purplebricks.co.uk/where-we-advertise
- group: commercial
  title: ''
  type: Pricing
  url: https://www.purplebricks.co.uk/services/our-packages
- group: other
  title: ''
  type: Mortgages
  url: https://www.purplebricksmortgages.co.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purplebricks.co.uk/terms
- group: company
  title: ''
  type: Blog
  url: https://www.purplebricks.co.uk/blog
- group: company
  title: ''
  type: TechBlog
  url: https://purplebricks.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/purplebricks
- group: company
  title: ''
  type: Careers
  url: https://purplebricks.bamboohr.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/purplebricks-uk/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/purplebricksuk
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/purplebricksUK
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/purplebricksuk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCXD3FPBFjPuMA4pCs-_KBJA
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@purplebricksuk
- group: auth
  title: ''
  type: Authentication
  url: authentication/purplebricks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/purplebricks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/purplebricks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/purplebricks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/purplebricks-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/purplebricks-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/purplebricks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/purplebricks-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://api.purplebricks.co.uk/property-api/swagger/index.html
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-book-a-valuation.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-go-to-market-listing.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-book-a-viewing.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-messaging-thread.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-conveyancing-quote.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/purplebricks-portal-branch-lookup.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.purplebricks.co.uk/terms/privacy-policy
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.purplebricks.co.uk/terms/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://www.purplebricks.co.uk/register
- group: start
  title: ''
  type: Login
  url: https://www.purplebricks.co.uk/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.purplebricks.co.uk/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.purplebricks.co.uk/faqs
- group: other
  title: ''
  type: Robots
  url: https://www.purplebricks.co.uk/robots.txt
- group: other
  title: ''
  type: Sitemap
  url: https://www.purplebricks.co.uk/sitemap.xml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/purplebricks-well-known.yml
- group: design
  title: ''
  type: Webhooks-Inbound
  url: asyncapi/purplebricks-webhooks.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/purplebricks-mcp.yml
created: '2026-07-26'
description: 'Purplebricks is the United Kingdom''s largest online (hybrid) estate agency, founded in 2014 by Michael and Kenny Bruce and David Shepherd, selling and letting residential property across England, Wales and Scotland through a fixed-fee, remote model staffed by local property experts rather than a high-street branch network. After a 2023 sale to rival online agent Strike for a nominal one pound the combined business was rebranded back under the Purplebricks name, and in 2026 the founding Bruce brothers returned alongside Sir Charles Dunstone''s Freston Ventures. It sits on the brokerage rung of the value chain, originating the seller relationship and the listing and then distributing that stock to Rightmove, Zoopla, OnTheMarket and PrimeLocation through the UK''s portal feed arrangements, because the UK has no MLS and therefore no shared cooperative data exchange. Its API posture is best described as published-but-undeclared: there is no developer portal, no partner programme,
  no signup and no documentation site, yet the estate serves sixteen real OpenAPI 3.0.1 documents and thirteen live public Swagger UIs across api.purplebricks.co.uk and www.purplebricks.co.uk, covering property, account, valuations, viewings, messaging, lettings, branch/portal syndication, communications, conveyancing, agent, feedback, workflow and Outlook calendar sync. Every operation is Bearer-token protected with no public key issuance, errors are ASP.NET ProblemDetails (RFC 7807), and the branch service exposes the Rightmove, Zoopla and OnTheMarket syndication seam directly. RESO is absent, as expected outside North America, and the genuinely open UK property data layer it consumes for its sold-prices tool belongs to government (HM Land Registry), not to Purplebricks.'
image: https://images.ctfassets.net/xhygqgfuea6b/3iPW7f24NM6u7Klc7YopsZ/43f36d4f236766caaa30f29fc85cafa1/purplebricks-logo.png
layout: provider
modified: '2026-07-26'
name: Purplebricks
nav: Providers
network: true
overview: 'Purplebricks publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Property API, Account API, Valuations API, and 10 more. Tagged areas include Real Estate, United Kingdom, Property Listings, Online Estate Agency, and Rentals.


  The Purplebricks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Purplebricks'' developer surface includes pricing, engineering blog, YouTube channel, authentication, API reference, signup flow, support, and 42 more developer resources.'
random_paper: 110
score:
  band: thin
  composite: 38.0
  delta: 0.3
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 52.0
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 81.3
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Purplebricks Authentication
  slug: purplebricks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Purplebricks Domain Security
  slug: purplebricks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purplebricks
tags:
- Real Estate
- United Kingdom
- Property Listings
- Online Estate Agency
- Rentals
- Lettings
- PropTech
- Mortgage
- Conveyancing
- Land Registry
- OpenAPI
- Microservices
- Swagger
- Azure
website: https://www.purplebricks.co.uk/
---
