---
access_model:
  confidence: high
  label: Enterprise · Approval required (portal signup, then Anywhere approval for sandbox and again for production)
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://developers.anywhere.re/docs/how-it-works
  - https://developers.anywhere.re/terms-use-api-license-agreement
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 23
apis:
- description: Endpoints for MLS listings data assembled by Anywhere's MLS Data Platform (MDP), which downloads, processes and enriches listings from multiple MLS sources. Returns listings in canonical RESO format e
  name: Anywhere MLS Data Service API
  slug: mls-data-service
- description: A bundle of APIs representing clean, curated master data for Agent, Office, Company, Staff and Listings entities, plus shared address and property services. Data is normalized from Anywhere and non-An
  name: Anywhere Master Data (MDM) API
  slug: master-data-services
- description: Synchronize marketing data for all Anywhere franchise brands and the brokerage group to an external system. Marketing data includes Company, Office, Agent, Team, Listings and New Development informati
  name: Anywhere Listing Syndication API
  slug: listing-syndication
- description: Real-time search over Anywhere listing details for applications that do not maintain a local data store. Documented as short-response-time and typically used for mobile applications.
  name: Anywhere Dynamic Search API
  slug: dynamic-search
- description: A bundle of APIs for listings submitted through external and internal products, enhancing property listings with SMS Property ID, RealVitalize ID and Dash attribute management.
  name: Anywhere Listing Extensions API
  slug: listingextensions
- description: Synchronize promotion data from Anywhere, covering channels, publication lists in each channel, nominated listings and listings flagged in each publication list. Used to create and update channels and
  name: Anywhere Listings Promotions API
  slug: property-promotions
- description: Listing management metric information for Anywhere franchise brands, including video views, virtual tour views and listing views, available as soon as data is received from Anywhere source systems.
  name: Anywhere Listing Metric API
  slug: realogy-listings-metrics
- description: Synchronize marketing data for all Anywhere franchise brands and brokerages, including Corporate Staff, Company, Office, Agent, Team, Listings and New Developments information.
  name: Anywhere Marketing - Franchise API
  slug: broker-agent-tools
- description: Synchronize Anywhere marketing data together with franchise brokerage production (transaction) details. Marketing detail includes Corporate Staff, Company, Office, Agent, Team, Listings and New Develo
  name: Anywhere Marketing and Transactions API
  slug: broker-agent-tools-plus
- description: Synchronize brokerage production (transaction) data from Anywhere, including Sale and Other Income transactions and the associated buyer and seller information.
  name: Anywhere Transactions - Franchise API
  slug: realogy-broker-production
- description: Write and update data into Anywhere systems, covering Listing, Transaction, Agent, Team, Office and Company data across all Anywhere franchise brands. Backed by the Anywhere Dash back-office platform.
  name: Anywhere Back Office Management API
  slug: backoffice
- description: Read-only access to Anywhere back-office data from the Dash platform, including listing, transaction, agent, team, office and company data.
  name: Anywhere BackOffice Read-only API
  slug: realogyentitiesro
- description: Powers third-party CRM applications to sync lead data with Anywhere source systems so agents can manage leads and contacts in one place. Third-party CRMs can receive, submit and update leads, and quer
  name: Anywhere Leads Management API
  slug: agentcrmintegration
- description: 'Submit a new lead to Anywhere''s referral platform for a specific real estate referral program and share status updates across the customer''s home buying or selling journey, including agent placement, '
  name: Anywhere Referral Leads API
  slug: referralplatformv2
- description: Submit a new lead to Anywhere's referral platform for a specific real estate referral program, creating a connected experience between the client, Anywhere and the agent, with status updates throughou
  name: Anywhere Referral Partner Integration API
  slug: referral-partner-integration
- description: 'An endpoint for third-party CRM integration partners to deliver recruiting activities into Anywhere''s iProspect application, validated against current iProspect business rules to prevent invalid data '
  name: Anywhere Agent Recruiting API
  slug: iprospect
- description: 'Track a consumer''s real estate transaction end to end, giving buyers visibility into the closing process with clear milestones, action items and status updates. Backed by Anywhere Integrated Services '
  name: Anywhere Consumer Journey API
  slug: c2shinningc
- description: 'Manage and access earnest money data for brokered trades: payee search, buyer and seller retrieval for a deal, creation of disbursement records, and retrieval and update of bank and transaction detail'
  name: Anywhere Earnest Money API
  slug: earnestmoney
- description: Exposes Anywhere Integrated Services settlement companies and their details, letting a consuming application retrieve settlement companies by filter criteria with results sorted by proximity.
  name: Anywhere Settlement Company API
  slug: settlement-company-capability
- description: 'Lets corporate clients trigger new relocation initiations or authorizations into Cartus. Authorizations are processed, a new customer file is created in the Cartus case management system, and the new '
  name: Anywhere Relocation Authorization API
  slug: relocationauthorization
- description: Allows HomeAdvisor to integrate its backend services with the RealVitalize backend — accessing enrollment information and adding or updating enrollment-related jobs, invoices and project status.
  name: Anywhere RealVitalize API
  slug: realvitalize-vendor-services
- description: Build and manage user access to Anywhere brand extranet applications and build user access reports. Exposes a user's profile plus the list of applications, brands, companies, master franchises and off
  name: Anywhere User Access Management API
  slug: realogy-user-access
- description: Handles ingestion, routing and assignment of leads for Anywhere brands. Listed on the developer portal home page as a Partner-visibility product; its product page returns HTTP 403 to anonymous visitor
  name: Anywhere Leads Engine API
  slug: anywhere-leads-engine
artifact_total: 27
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/anywhere-real-estate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anywhere-real-estate-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anywhere-real-estate-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anywhere-real-estate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anywhere-real-estate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anywhere-real-estate-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anywhere-real-estate-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anywhere-real-estate-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.anywhere.re/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/anywhere-real-estate-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/anywhere-real-estate-packages.yml
- group: design
  title: ''
  type: Components
  url: components/anywhere-real-estate-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anywhere-real-estate-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/anywhere-real-estate-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anywhere-real-estate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anywhere.re/
- group: start
  title: ''
  type: Portal
  url: https://developers.anywhere.re/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.anywhere.re/api-products
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.anywhere.re/docs/how-it-works
- group: auth
  title: ''
  type: Authentication
  url: https://developers.anywhere.re/docs/realogy-oauth
- group: auth
  title: ''
  type: Authentication
  url: authentication/anywhere-real-estate-okta-prod-authorization-server.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/anywhere-real-estate-okta-prod-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/anywhere-real-estate-okta-nonprod-authorization-server.json
- group: start
  title: ''
  type: SignUp
  url: https://developers.anywhere.re/user/register
- group: start
  title: ''
  type: Login
  url: https://developers.anywhere.re/Login
- group: operate
  title: ''
  type: Support
  url: https://developers.anywhere.re/support
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.anywhere.re/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.anywhere.re/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.anywhere.re/terms-use-api-license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.anywhere.re/en/global-privacy-notice
- group: company
  title: ''
  type: Blog
  url: https://developers.anywhere.re/get-inspired?type=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Anywhererealestate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anywhere-real-estate-inc/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/anywhere_re
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@anywhererealestateinc
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.anywhere.re/
created: '2026-07-26'
description: 'Anywhere Real Estate Inc. (formerly Realogy Holdings Corp., NYSE: HOUS) is one of the largest residential real estate services companies in the United States, headquartered at 175 Park Avenue, Madison, New Jersey. It franchises and operates Better Homes and Gardens Real Estate, CENTURY 21, Coldwell Banker, Coldwell Banker Commercial, Corcoran, ERA and Sotheby''s International Realty; runs the Anywhere Advisors brokerage, the Anywhere Integrated Services title and settlement business, the Anywhere Leads referral network and Cartus relocation. Its own home page states that as of January 9, 2026 Anywhere Real Estate and Compass came together as Compass International Holdings. Unusually for a brokerage, Anywhere operates a genuine Apigee-backed developer portal at developers.anywhere.re that publicly lists 23 documented API products spanning MLS and listing data, marketing syndication, transactions, back office, leads, agent recruiting, earnest money, title settlement, relocation
  and user access. Anywhere is a RESO consumer rather than a RESO certificant: its MLS Data Service returns listings in "canonical RESO format" and its Master Data product uses RESO name space convention, but Anywhere appears nowhere in the RESO Certification Status directory. Access is licensed, not open — every specification, Postman collection and SDK page redirects anonymous visitors to login, and both sandbox and production access require an Anywhere review of up to two business days under a binding API Terms of Use and License Agreement.'
image: https://developers.anywhere.re/sites/default/files/anywhere_favicon.png
layout: provider
modified: '2026-07-26'
name: Anywhere Real Estate
nav: Providers
network: true
overview: 'Anywhere Real Estate publishes 23 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, Property Listings, MLS, and RESO.


  Anywhere Real Estate''s developer surface includes authentication, changelog, sandbox, developer portal, documentation, getting-started guide, signup flow, and 29 more developer resources.'
random_paper: 86
scopes:
- name: Anywhere Real Estate Scopes
  scope_count: 0
  slug: anywhere-real-estate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.0
  delta: 1.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 38.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 66.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anywhere-real-estate/refs/heads/main/screenshots/anywhere-real-estate-2026-08-07T161434.png
security:
- kind: authentication
  name: Anywhere Real Estate Authentication
  slug: anywhere-real-estate-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Anywhere Real Estate Domain Security
  slug: anywhere-real-estate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Anywhere Real Estate Trust Center
  slug: anywhere-real-estate-trust-center
  summary_line: SOC 1, SOC 2 Type 2, ISO/IEC 27001:2022, SOX, GDPR, EU-US Data Privacy Framework, Cyber Essentials
slug: anywhere-real-estate
tags:
- Real Estate
- United States
- Property Listings
- MLS
- RESO
- Brokerage
- Franchising
- PropTech
- Title
- Escrow
- Relocation
- Leads
- Transactions
website: https://anywhere.re/
---
