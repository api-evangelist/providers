---
access_model:
  confidence: high
  label: Self-serve signup from $30/month; enterprise plans quoted by sales
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - authentication
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.7
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: REST API for brands/advertisers to manage programs, partner recruitment and contracts, product catalogs, conversions and action reconciliation, promo codes, deals, reporting and payouts across affilia
  name: impact.com Brand API
  slug: impactcom-brand-api
- description: REST API for media partners/publishers to access programs and contracts, ads and tracking links, product catalogs and stores, promo codes and promotions, actions and commissions, invoices, tax documen
  name: impact.com Partner API
  slug: impactcom-partner-api
- description: REST API for agencies managing multiple client brand accounts — advertiser roster, company information, compliance content submission and results, consolidated reporting, and job management. Current v
  name: impact.com Agency API
  slug: impactcom-agency-api
- description: REST and GraphQL APIs for Advocate customer-referral programs — participants and accounts, referral codes and share links, referrals, rewards and reward balances, data exports and webhook subscription
  name: impact.com Advocate API
  slug: impactcom-advocate-api
artifact_total: 79
asyncapis:
- description: ''
  name: Impact Radius Advocate Webhooks
  slug: impact-radius-advocate-webhooks
collections:
- collection_type: open
  name: Agency API — Advertisers
  slug: open-impact-radius-agency-advertisers-v3
- collection_type: open
  name: Agency API — Company Information
  slug: open-impact-radius-agency-companyinformation-v3
- collection_type: open
  name: Agency API — Compliance Content
  slug: open-impact-radius-agency-compliance-v3
- collection_type: open
  name: Agency API — Jobs Management
  slug: open-impact-radius-agency-jobs-v3
- collection_type: open
  name: Agency API — Reports
  slug: open-impact-radius-agency-reports-v3
- collection_type: open
  name: Brand API - Account Information
  slug: open-impact-radius-brand-account-v14
- collection_type: open
  name: Brand API - Action Inquiries
  slug: open-impact-radius-brand-actioninquiries-v14
- collection_type: open
  name: Brand API - Actions
  slug: open-impact-radius-brand-actions-v14
- collection_type: open
  name: Brand API - Ads
  slug: open-impact-radius-brand-ads-v14
- collection_type: open
  name: impact.com REST API - Account
  slug: open-impact-radius-brand-advocate-account-v13
- collection_type: open
  name: impact.com API - Export
  slug: open-impact-radius-brand-advocate-export-v13
- collection_type: open
  name: SaaSquatch by impact.com API - Referral
  slug: open-impact-radius-brand-advocate-referral-v13
- collection_type: open
  name: impact.com API - Referral Code
  slug: open-impact-radius-brand-advocate-referralcode-v13
- collection_type: open
  name: impact.com API - Reward
  slug: open-impact-radius-brand-advocate-reward-v13
- collection_type: open
  name: impact.com API - Reward Balance
  slug: open-impact-radius-brand-advocate-rewardbalance-v13
- collection_type: open
  name: impact.com API - Share Links
  slug: open-impact-radius-brand-advocate-sharelinks-v13
- collection_type: open
  name: impact.com API - User
  slug: open-impact-radius-brand-advocate-user-v13
- collection_type: open
  name: impact.com API - Webhook
  slug: open-impact-radius-brand-advocate-webhook-v13
- collection_type: open
  name: Brand API - Call Data
  slug: open-impact-radius-brand-calldata-v14
- collection_type: open
  name: Brand API - Product Catalogs
  slug: open-impact-radius-brand-catalogs-v14
- collection_type: open
  name: Brand API - Clicks
  slug: open-impact-radius-brand-clicks-v14
- collection_type: open
  name: Brand API - Contacts
  slug: open-impact-radius-brand-contacts-v14
- collection_type: open
  name: Brand API - Contracts
  slug: open-impact-radius-brand-contracts-v14
- collection_type: open
  name: Brand API - Conversions
  slug: open-impact-radius-brand-conversions-v14
- collection_type: open
  name: Brand API - Deals
  slug: open-impact-radius-brand-deals-v14
- collection_type: open
  name: Brand API - Deferred Deep Linking
  slug: open-impact-radius-brand-deferreddeeplink-v14
- collection_type: open
  name: Brand API - Exception Lists
  slug: open-impact-radius-brand-exceptionlists-v14
- collection_type: open
  name: Brand API - Partner Invoices
  slug: open-impact-radius-brand-invoices-v14
- collection_type: open
  name: Brand API - Jobs
  slug: open-impact-radius-brand-jobs-v14
- collection_type: open
  name: Brand API - Notes
  slug: open-impact-radius-brand-notes-v14
- collection_type: open
  name: Brand API - Page Load
  slug: open-impact-radius-brand-pageload-v14
- collection_type: open
  name: Brand API - Partner Groups
  slug: open-impact-radius-brand-partnergroups-v14
- collection_type: open
  name: Brand API - Partners
  slug: open-impact-radius-brand-partners-v14
- collection_type: open
  name: Brand API - Phone Numbers
  slug: open-impact-radius-brand-phonenumbers-v14
- collection_type: open
  name: Brand API - Programs
  slug: open-impact-radius-brand-programs-v14
- collection_type: open
  name: Brand API - Promo Code Exception Lists
  slug: open-impact-radius-brand-promocodeexceptionlists-v14
- collection_type: open
  name: Brand API - Promo Codes
  slug: open-impact-radius-brand-promocodes-v14
- collection_type: open
  name: Brand API - Reports & Exports
  slug: open-impact-radius-brand-reports-v14
- collection_type: open
  name: Brand API - Routing Rules
  slug: open-impact-radius-brand-routingrules-v14
- collection_type: open
  name: Brand API - Submissions
  slug: open-impact-radius-brand-submissions-v14
- collection_type: open
  name: Brand API - Tasks
  slug: open-impact-radius-brand-tasks-v14
- collection_type: open
  name: Brand API - Tracking Links
  slug: open-impact-radius-brand-trackinglinks-v14
- collection_type: open
  name: Brand API - Tracking Value Requests
  slug: open-impact-radius-brand-trackingvaluerequests-v14
- collection_type: open
  name: Company Information API
  slug: open-impact-radius-partner-account-v15
- collection_type: open
  name: Action Inquiries API
  slug: open-impact-radius-partner-actioninquiries-v15
- collection_type: open
  name: Impact Publisher Actions API
  slug: open-impact-radius-partner-actions-v15
- collection_type: open
  name: Partner Ads API
  slug: open-impact-radius-partner-ads-v15
- collection_type: open
  name: Partner Programs API
  slug: open-impact-radius-partner-campaigns-v15
- collection_type: open
  name: Partner Catalogs API
  slug: open-impact-radius-partner-catalogs-v15
- collection_type: open
  name: Partner Clicks API
  slug: open-impact-radius-partner-clicks-v15
- collection_type: open
  name: Partner Contracts API
  slug: open-impact-radius-partner-contracts-v15
- collection_type: open
  name: Partner Deals API
  slug: open-impact-radius-partner-deals-v15
- collection_type: open
  name: Partner Event Notifications API
  slug: open-impact-radius-partner-eventnotifications-v15
- collection_type: open
  name: Partner Exception Lists API
  slug: open-impact-radius-partner-exceptionlists-v15
- collection_type: open
  name: Partner Identity Verification API
  slug: open-impact-radius-partner-identityverification-v15
- collection_type: open
  name: Partner Invoices API
  slug: open-impact-radius-partner-invoices-v15
- collection_type: open
  name: Partner Jobs API
  slug: open-impact-radius-partner-jobs-v15
- collection_type: open
  name: Partner Media Properties API
  slug: open-impact-radius-partner-mediaproperties-v15
- collection_type: open
  name: Partner Promo Codes API
  slug: open-impact-radius-partner-promo-codes-v15
- collection_type: open
  name: Partner Promo Code Exception Lists API
  slug: open-impact-radius-partner-promocodeexceptionlists-v15
- collection_type: open
  name: Partner Promotions API
  slug: open-impact-radius-partner-promotions-v15
- collection_type: open
  name: Partner Reports API
  slug: open-impact-radius-partner-reports-v15
- collection_type: open
  name: Partner Stores API
  slug: open-impact-radius-partner-stores-v15
- collection_type: open
  name: Partner Tax Documents API
  slug: open-impact-radius-partner-taxdocument-v15
- collection_type: open
  name: Partner Tracking Links API
  slug: open-impact-radius-partner-trackinglinks-v15
- collection_type: open
  name: Partner Users API
  slug: open-impact-radius-partner-users-v15
- collection_type: open
  name: Partner Withdrawal Settings API
  slug: open-impact-radius-partner-withdrawalsettings-v15
common:
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.impact.com/rest-apis/api-quick-start.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/impact-radius-authentication.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.impact.com/en/support/home
- group: operate
  title: ''
  type: Support
  url: https://help.impact.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://impact.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.impact.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.impact.com/login.user
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impact.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impact.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impact.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impact-radius-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impact-radius-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impact-radius-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/impact-radius-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-radius-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://impact.responsibledisclosure.com/hc/en-us
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impact-radius-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/impact-radius-advocate-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/impact-radius-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impact-radius-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/impact-radius-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impact-radius-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/impact-radius-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impact-radius-conventions.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/impact-radius-advocate-schema.graphql
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/impact-radius-tool-crosswalk.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/impact-radius-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/impact-radius-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/impact-radius-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/impact-radius-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/impact-radius-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/impact-radius-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/impact-radius-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/impact-radius-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/impact-radius-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saasquatch
- group: auth
  title: ''
  type: SecurityAndPrivacy
  url: https://impact.com/security-and-privacy/
created: '2026-07-17'
description: Impact Radius, now operating as impact.com, is a partnership management platform for managing affiliate programs, influencer and creator partnerships, and customer referral (Advocate) initiatives at scale. Brands, agencies, and publishers use it to discover and recruit partners, contract and pay them against business outcomes, track partner-driven traffic and conversions with privacy-first attribution across devices, protect programs from fraud, and optimize performance with predictive analytics. The platform publishes 67 machine-readable OpenAPI 3.1 documents covering 242 operations across Brand (v14), Partner (v15), Agency (v3) and Advocate (v1) REST APIs, an openly introspectable Advocate GraphQL schema, webhooks and event notifications, mobile and browser SDKs, an official hosted MCP server with a published 18-tool catalog and first-party MCP Skills, and llms.txt plus per-page markdown for agent and AI-assisted integration.
image: https://impact.com/wp-content/uploads/2022/04/impact-logo-square.jpg
layout: provider
mcp_servers:
- description: ''
  name: Impact Radius MCP Server
  slug: impact-radius-mcp-server
modified: '2026-08-13'
name: Impact Radius
nav: Providers
network: true
overview: 'Impact Radius publishes 4 APIs on the [APIs.io](https://apis.io/) network, including impact.com Brand API, impact.com Partner API, impact.com Agency API, and 1 more. Tagged areas include Company, Partnership Management, Affiliate Marketing, Influencer Marketing, and Referral Marketing.


  The Impact Radius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Impact Radius'' developer surface includes documentation, getting-started guide, authentication, support, engineering blog, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Impact Radius Plans Pricing
  plan_count: 2
  slug: impact-radius-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Impact Radius Rate Limits
  slug: impact-radius-rate-limits
score:
  band: exemplar
  composite: 68.1
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 16.7
    contract_quality: 66.6
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 92.1
  previous_composite: 68.1
  provenance:
    conformance: derived
    contracts:
      callable: 98.5
      derived: 0
      marker_coverage: 0.0
      total: 67
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impact-radius/refs/heads/main/screenshots/impact-radius-2026-07-25T222140.png
security:
- kind: authentication
  name: Impact Radius Authentication
  slug: impact-radius-authentication
  summary_line: http/apiKey · 6 schemes
- kind: domain-security
  name: Impact Radius Domain Security
  slug: impact-radius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Radius Vulnerability Disclosure
  slug: impact-radius-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Impact Radius Trust Center
  slug: impact-radius-trust-center
  summary_line: SOC 1 Type II, ISO/IEC 27001:2022, PCI-DSS Level 4
slug: impact-radius
tags:
- Company
- Partnership Management
- Affiliate Marketing
- Influencer Marketing
- Referral Marketing
- Attribution
- MarTech
- Advocate
- Creator Economy
- E-Commerce
website: https://impact.com/
---
