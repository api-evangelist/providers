---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Dun And Bradstreet Agentic Access
  operation_count: 14
  slug: dun-and-bradstreet-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 15
apis:
- description: The Identity Resolution surface of D&B Direct+ matches an input business record — name, address, phone, email, registration number — to a single authoritative D-U-N-S Number. The API returns ranked ca
  name: D&B Direct+ Identity Resolution API
  slug: direct-plus-identity-resolution
- description: The Search surface of D&B Direct+ lets applications find businesses, principals, and related entities using flexible criteria such as company name, address, registration number, beneficial owner, or c
  name: D&B Direct+ Search API
  slug: direct-plus-search
- description: The Enrich surface returns standardized "data blocks" for a given D-U-N-S Number. Blocks group attributes by domain — Company Information, Principals & Contacts, Hierarchy & Connections, Financial Str
  name: D&B Direct+ Enrich (Data Blocks) API
  slug: direct-plus-enrich
- description: 'Multi-Process combines Identity Resolution and Enrich into a single request: the caller submits a candidate input record plus a set of desired data blocks, D&B resolves the input to a D-U-N-S Number a'
  name: D&B Direct+ Multi-Process API
  slug: direct-plus-multi-process
- description: The Data File (Batch) surface lets customers submit large input files and receive matched, enriched output files asynchronously. The workflow is upload → process → poll status → download — suitable fo
  name: D&B Direct+ Data File (Batch) API
  slug: direct-plus-data-file
- description: The Monitoring surface lets customers register a portfolio of D-U-N-S Numbers and subscribe to change events. When D&B detects an update to a monitored attribute — address, ownership, financials, risk
  name: D&B Direct+ Monitoring API
  slug: direct-plus-monitoring
- description: 'The Research surface lets customers retrieve historical responses Direct+ has previously returned, supporting audit, dispute, and reconciliation use cases where the application needs to see the exact '
  name: D&B Direct+ Research API
  slug: direct-plus-research
- description: OAuth 2.0 token issuance for Direct+.
  name: Dun & Bradstreet Authentication API
  slug: dun-and-bradstreet-authentication-api
- description: Asynchronous batch file submission, status, and download.
  name: Dun & Bradstreet Data File API
  slug: dun-and-bradstreet-data-file-api
- description: Retrieve Data Blocks for a known D-U-N-S Number.
  name: Dun & Bradstreet Enrich API
  slug: dun-and-bradstreet-enrich-api
- description: Match an input record to a D-U-N-S Number.
  name: Dun & Bradstreet Identity Resolution API
  slug: dun-and-bradstreet-identity-resolution-api
- description: Subscribe to and consume change notifications on a portfolio.
  name: Dun & Bradstreet Monitoring API
  slug: dun-and-bradstreet-monitoring-api
- description: Combined match plus enrich in a single call.
  name: Dun & Bradstreet Multi-Process API
  slug: dun-and-bradstreet-multi-process-api
- description: Retrieve historical responses for audit and reconciliation.
  name: Dun & Bradstreet Research API
  slug: dun-and-bradstreet-research-api
- description: Find companies, principals, and related entities.
  name: Dun & Bradstreet Search API
  slug: dun-and-bradstreet-search-api
arazzos:
- description: Obtain a Direct+ token, resolve a candidate record to a D-U-N-S Number, and pull its company information block.
  name: D&B Authenticate And Match Company
  slug: dun-and-bradstreet-authenticate-and-match-company-workflow
- description: Submit a batch input file, poll until processing completes, then download the matched and enriched results.
  name: D&B Batch Match And Enrich File
  slug: dun-and-bradstreet-batch-match-enrich-file-workflow
- description: Resolve a candidate to a D-U-N-S Number and branch to enrichment only when an acceptable match is found.
  name: D&B Cleanse Match And Enrich
  slug: dun-and-bradstreet-cleanse-match-and-enrich-workflow
- description: Find a principal or contact, then enrich the organization they are associated with.
  name: D&B Contact Search And Enrich
  slug: dun-and-bradstreet-contact-search-and-enrich-workflow
- description: Browse companies by free-form criteria, then enrich the first candidate's Data Blocks.
  name: D&B Criteria Search And Get Company
  slug: dun-and-bradstreet-criteria-search-and-get-company-workflow
- description: Match a candidate, remove its D-U-N-S Number from a monitoring registration, and confirm remaining notifications.
  name: D&B Manage Portfolio Membership
  slug: dun-and-bradstreet-manage-portfolio-membership-workflow
- description: Resolve a candidate to a D-U-N-S Number, then retrieve a historical Direct+ response for audit and reconciliation.
  name: D&B Match And Audit History
  slug: dun-and-bradstreet-match-and-audit-history-workflow
- description: Resolve a candidate to a D-U-N-S Number, create a monitoring registration, and add the D-U-N-S Number to its portfolio.
  name: D&B Match And Monitor Company
  slug: dun-and-bradstreet-match-and-monitor-company-workflow
- description: Obtain a token, then resolve and enrich a candidate record in a single multiProcess call.
  name: D&B Match Plus Enrich
  slug: dun-and-bradstreet-match-plus-enrich-workflow
- description: Create a monitoring registration, enroll a portfolio of D-U-N-S Numbers, and pull pending change notifications.
  name: D&B Register And Pull Notifications
  slug: dun-and-bradstreet-register-and-pull-notifications-workflow
artifact_total: 80
collections:
- collection_type: postman
  name: D&B Direct+ API
  slug: postman-dnb-direct-plus-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dun-and-bradstreet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dun-and-bradstreet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dun-and-bradstreet-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dun-bradstreet/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-authenticate-and-match-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-batch-match-enrich-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-cleanse-match-and-enrich-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-contact-search-and-enrich-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-criteria-search-and-get-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-manage-portfolio-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-match-and-audit-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-match-and-monitor-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-match-plus-enrich-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dun-and-bradstreet-register-and-pull-notifications-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.dnb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://directplus.documentation.dnb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://directplus.documentation.dnb.com/
- group: docs
  title: ''
  type: APIReference
  url: https://directplus.documentation.dnb.com/html/pages/APIList.html
- group: start
  title: ''
  type: GettingStarted
  url: https://directplus.documentation.dnb.com/html/pages/UsingAPIs.html
- group: auth
  title: ''
  type: Authentication
  url: https://directplus.documentation.dnb.com/html/guides/Authentication.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://directplus.documentation.dnb.com/html/resources/ChangeHistory.html
- group: start
  title: ''
  type: Signup
  url: https://directplus.documentation.dnb.com/registration/register
- group: start
  title: ''
  type: Login
  url: https://directplus.documentation.dnb.com/home
- group: operate
  title: ''
  type: Support
  url: https://service.dnb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dnb.com/utility-pages/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dnb.com/utility-pages/privacy-policy.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.dnb.com/utility-pages/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dun-&-bradstreet
- group: other
  title: ''
  type: X
  url: https://twitter.com/DunBradstreet
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/DunandBradstreet
- group: company
  title: ''
  type: Blog
  url: https://www.dnb.com/perspectives.html
- group: commercial
  title: ''
  type: Pricing
  url: plans/dun-and-bradstreet-plans-pricing.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dun-and-bradstreet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dun-and-bradstreet-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/dnb-direct-plus-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dun-and-bradstreet-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dun-and-bradstreet-context.jsonld
- group: commercial
  title: ''
  type: FinOps
  url: finops/dun-and-bradstreet-finops.yml
created: '2026-05-23'
description: Dun & Bradstreet is a leading global provider of business decisioning data and analytics, anchored by the D-U-N-S Number — a unique nine-digit identifier assigned to more than 500 million businesses worldwide. Founded in 1841 as The Mercantile Agency in New York City and now headquartered in Jacksonville, Florida, D&B operates the D&B Data Cloud, a master commercial database used by enterprises and governments for credit, risk, supply, master data, sales, marketing, compliance, and third-party due diligence. Its primary developer surface is D&B Direct+, a RESTful API platform that lets customers match, enrich, monitor, and stream company data programmatically using OAuth 2.0 access tokens. D&B was taken private by Clearlake Capital in August 2025 for approximately $7.7 billion (including debt).
examples:
- key_count: 2
  name: Dnb Direct Plus Add Duns To Registration Example
  slug: dnb-direct-plus-add-duns-to-registration-example
- key_count: 2
  name: Dnb Direct Plus Cleanse Match Example
  slug: dnb-direct-plus-cleanse-match-example
- key_count: 2
  name: Dnb Direct Plus Create Monitoring Registration Example
  slug: dnb-direct-plus-create-monitoring-registration-example
- key_count: 2
  name: Dnb Direct Plus Download Batch File Results Example
  slug: dnb-direct-plus-download-batch-file-results-example
- key_count: 2
  name: Dnb Direct Plus Generate Access Token Example
  slug: dnb-direct-plus-generate-access-token-example
- key_count: 2
  name: Dnb Direct Plus Get Audit Record Example
  slug: dnb-direct-plus-get-audit-record-example
- key_count: 2
  name: Dnb Direct Plus Get Batch File Status Example
  slug: dnb-direct-plus-get-batch-file-status-example
- key_count: 2
  name: Dnb Direct Plus Get Data Blocks By Duns Example
  slug: dnb-direct-plus-get-data-blocks-by-duns-example
- key_count: 2
  name: Dnb Direct Plus Multi Process Match And Enrich Example
  slug: dnb-direct-plus-multi-process-match-and-enrich-example
- key_count: 2
  name: Dnb Direct Plus Pull Monitoring Notifications Example
  slug: dnb-direct-plus-pull-monitoring-notifications-example
- key_count: 2
  name: Dnb Direct Plus Remove Duns From Registration Example
  slug: dnb-direct-plus-remove-duns-from-registration-example
- key_count: 2
  name: Dnb Direct Plus Search Companies By Criteria Example
  slug: dnb-direct-plus-search-companies-by-criteria-example
- key_count: 2
  name: Dnb Direct Plus Search Contacts Example
  slug: dnb-direct-plus-search-contacts-example
- key_count: 2
  name: Dnb Direct Plus Submit Batch File Example
  slug: dnb-direct-plus-submit-batch-file-example
features:
- description: Every business in the D&B Data Cloud carries a unique nine-digit D-U-N-S Number that acts as a persistent, globally recognized enterprise identifier.
  name: D-U-N-S Number Identity
- description: More than 500 million company records spanning legal entities, branches, subsidiaries, contacts, and beneficial owners across virtually every country.
  name: Data Cloud Coverage
- description: Versioned, domain-grouped attribute bundles (Company, Financials, Hierarchy, Risk, Compliance, ESG, Beneficial Ownership) that callers opt into per request.
  name: Data Blocks
- description: Multi-Process combines Identity Resolution and Enrich, eliminating a round-trip for onboarding and CRM-augment workflows.
  name: Match + Enrich in One Call
- description: Direct+ offers REST synchronous calls, Data File asynchronous batch processing, and Monitoring change-notification streams over the same data substrate.
  name: Synchronous + Batch + Streaming
- description: Corporate hierarchies — parent, headquarters, ultimate domestic parent, ultimate global parent, branches — are exposed as first-class relationships rather than denormalized fields.
  name: Hierarchy and Linkage
- description: Enrich includes UBO, sanctions, watchlist, and PEP screening data to support KYB, AML, and third-party risk management programs.
  name: Beneficial Ownership and Compliance
- description: Authentication is standard OAuth 2.0 client-credentials grant; bearer tokens are scoped per Direct+ subscription.
  name: OAuth 2.0 Client Credentials
finops:
- name: Dun And Bradstreet Finops
  service_category: ''
  slug: dun-and-bradstreet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dun-and-bradstreet.png
integrations:
- description: D&B Hoovers and D&B Direct+ data flow into Salesforce CRM via D&B's managed packages and AppExchange listings.
  name: Salesforce
- description: Direct+ enrichment plugs into Dynamics 365 Sales and Customer Insights to augment accounts and contacts.
  name: Microsoft Dynamics 365
- description: D&B's master-data integrations enrich SAP S/4HANA and SAP Ariba supplier records with D-U-N-S Numbers and Data Blocks.
  name: SAP
- description: Direct+ data feeds Oracle ERP, EPM, and Procurement Cloud master data pipelines.
  name: Oracle
- description: D&B publishes data products on the Snowflake Marketplace so customers can query Data Cloud attributes directly in their warehouse.
  name: Snowflake Marketplace
- description: D&B firmographics enrich Adobe Real-Time CDP profiles for B2B personalization.
  name: Adobe Real-Time CDP
- description: Connectors push D&B Hoovers / Direct+ company data into HubSpot CRM properties.
  name: HubSpot
json_schemas:
- name: DnB Direct+ Match Candidate
  property_count: 3
  slug: dnb-direct-plus-match-candidate
- name: DnB Direct+ Monitoring Notification
  property_count: 6
  slug: dnb-direct-plus-monitoring-notification
- name: DnB Direct+ Organization
  property_count: 13
  slug: dnb-direct-plus-organization
json_structures:
- name: Dnb Direct Plus Organization Structure
  property_count: 0
  slug: dnb-direct-plus-organization-structure
jsonld:
- class_count: 1
  name: Dun And Bradstreet Context
  property_count: 23
  slug: dun-and-bradstreet-context
layout: provider
modified: '2026-05-23'
name: Dun & Bradstreet
nav: Providers
network: true
overview: 'Dun & Bradstreet publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Data File API, Enrich API, and 5 more. Tagged areas include Business Data, Company Data, D-U-N-S Number, Credit, and Risk.


  The Dun & Bradstreet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dun & Bradstreet''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, signup flow, support, and 31 more developer resources.'
plans:
- name: Dun And Bradstreet Plans Pricing
  plan_count: 2
  slug: dun-and-bradstreet-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Dun And Bradstreet Rate Limits
  slug: dun-and-bradstreet-rate-limits
rules:
- name: Dun & Bradstreet API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: dnb-direct-plus-rules
- name: Dun & Bradstreet API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dun-and-bradstreet-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.8
  delta: -3.4
  facets:
    commercial_clarity: 81.6
    contract_quality: 75.0
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 37.5
    operational_transparency: 15.8
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dun-and-bradstreet/refs/heads/main/screenshots/dun-and-bradstreet-2026-06-20T180319.png
security:
- kind: authentication
  name: Dun And Bradstreet Authentication
  slug: dun-and-bradstreet-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dun And Bradstreet Domain Security
  slug: dun-and-bradstreet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dun-and-bradstreet
solutions:
- description: Credit risk, accounts-receivable, trade payment, and collections solutions powered by Direct+ financial and risk blocks.
  name: Finance & Credit
- description: D&B Hoovers, Audience Targeting, and Connect for Salesforce build on Direct+ firmographics and contacts.
  name: Sales & Marketing
- description: D&B Risk Analytics, Beneficial Ownership, and Compliance Center combine enrichment and monitoring for vendor risk programs.
  name: Third-Party Risk & Compliance
- description: D&B Optimizer and master-data services use Direct+ to clean, deduplicate, and continuously synchronize enterprise customer and supplier records.
  name: Master Data
- description: Supplier intelligence, ESG, diversity, and supply-chain risk analytics combine Direct+ data blocks with D&B portfolio monitoring.
  name: Supply
tags:
- Business Data
- Company Data
- D-U-N-S Number
- Credit
- Risk
- Master Data
- Data Enrichment
- Identity Resolution
- Compliance
- Supply Chain
- Sales Intelligence
- Monitoring
use_cases:
- description: Resolve a prospective customer's name and address to a D-U-N-S Number, then enrich with financial, ownership, and compliance data before extending credit or signing a contract.
  name: Customer Onboarding (KYB)
- description: Use Multi-Process and Monitoring to keep an internal supplier master synchronized with D&B's authoritative company records, automatically flagging mergers, dissolutions, address changes, and ownership shifts.
  name: Supplier Master Data Management
- description: Combine Enrich blocks for compliance, beneficial ownership, ESG, and financial stress to score third parties continuously against a policy.
  name: Third-Party Risk Management
- description: Retrieve PAYDEX scores, financial-strength indicators, and trade payment history to automate credit limit decisions in lending and B2B trade.
  name: Credit Decisioning
- description: Search and Enrich power lead scoring, total-addressable-market modeling, and account-based marketing by attaching firmographic data to CRM records.
  name: Sales and Marketing Intelligence
- description: Use compliance and beneficial-ownership blocks to satisfy AML, KYB, and sanctions-screening obligations.
  name: Compliance and Sanctions Screening
- description: The D-U-N-S Number remains widely used as a registration identifier for procurement, grants, and supplier qualification programs.
  name: Government and Grants Eligibility
website: https://www.dnb.com/
---
