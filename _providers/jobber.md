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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Jobber Agentic Access
  operation_count: 1
  slug: jobber-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Jobber — 1 operation(s) for graphql.
  name: Jobber GraphQL API
  slug: jobber-graphql-api
artifact_total: 53
collections:
- collection_type: open
  name: Jobber Developer API
  slug: open-jobber-developer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jobber-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jobber-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jobber-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jobber-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://getjobber.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.getjobber.com
- group: start
  title: ''
  type: Signup
  url: https://developer.getjobber.com/signup/
- group: start
  title: ''
  type: Console
  url: https://secure.getjobber.com/login
- group: start
  title: ''
  type: Signup
  url: https://getjobber.com/sign-up/
- group: commercial
  title: ''
  type: Pricing
  url: https://getjobber.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://getjobber.com/about/
- group: learn
  title: ''
  type: Academy
  url: https://getjobber.com/academy/
- group: docs
  title: ''
  type: Documentation
  url: https://getjobber.com/podcast/
- group: build
  title: ''
  type: Tools
  url: https://getjobber.com/free-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://getjobber.com/grants/
- group: docs
  title: ''
  type: Documentation
  url: https://getjobber.com/summit/
- group: other
  title: ''
  type: Marketplace
  url: https://secure.getjobber.com/app_marketplace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetJobber
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GetJobber/Jobber-AppTemplate-React
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/GetJobber/Jobber-AppTemplate-RailsAPI
- group: other
  title: ''
  type: Application
  url: https://apps.apple.com/app/jobber-on-the-go/id577517234
- group: other
  title: ''
  type: Application
  url: https://play.google.com/store/apps/details?id=com.getjobber.jobber
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@getjobber.com
- group: commercial
  title: ''
  type: Plans
  url: plans/jobber-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jobber-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jobber-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/jobber-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/jobber-vocabulary.yml
created: '2026-05-25T00:00:00.000Z'
description: Jobber is field service management software for home and commercial service businesses, serving 100,000+ businesses across more than 50 trade verticals (cleaning, HVAC, plumbing, electrical, landscaping, roofing, painting, handyman, and more). The platform covers the full service-delivery lifecycle — requests, assessments, quotes, scheduling, visits, time tracking, expenses, invoicing, payments, and reporting — with first-party iOS and Android apps for technicians. The Jobber Developer API is a single GraphQL endpoint at https://api.getjobber.com/api/graphql secured by OAuth 2.0, versioned by date via the X-JOBBER-GRAPHQL-VERSION header, and throttled by a leaky-bucket query-cost budget on top of a 2,500-requests / 5-minute DDoS guard. Third-party apps are published in the Jobber App Marketplace.
examples:
- key_count: 2
  name: Jobber Create Invoice Example
  slug: jobber-create-invoice-example
- key_count: 2
  name: Jobber List Jobs Example
  slug: jobber-list-jobs-example
features:
- description: Single endpoint at https://api.getjobber.com/api/graphql exposing every core Jobber resource for read and write.
  name: GraphQL Developer API
- description: App-based OAuth 2.0 with scoped access tokens managed via the Jobber Developer Center.
  name: OAuth 2.0 Authorization
- description: Requests pinned to a specific schema date via the X-JOBBER-GRAPHQL-VERSION header; breaking changes are published in the changelog.
  name: Date-based API Versioning
- description: Per-app/account point budget (default 10,000) restored at 500 points/sec; cost telemetry returned in extensions.cost.
  name: Leaky-Bucket Query Cost Throttling
- description: 2,500 requests per 5 minutes per app/account combination, separate from the cost budget.
  name: DDoS Request Guard
- description: Public catalog at apps.getjobber.com where third-party apps are published and installed by Jobber accounts.
  name: App Marketplace
- description: 90-day developer testing signup with special accounts for app development and validation.
  name: Developer Testing Accounts
- description: The Developer Center's Test in GraphiQL feature automates OAuth and issues 60-minute access tokens for ad-hoc queries.
  name: GraphiQL In Console
- description: Complete service-delivery lifecycle from request through invoicing modeled in the API.
  name: Quotes, Jobs, Visits, Invoices and Payments
- description: Account-level custom fields can be defined and attached to clients, properties, jobs, quotes, and invoices.
  name: Custom Field Configurations
- description: All Jobber GraphQL nodes use opaque Encoded IDs (EncodedId type) — required for cross-account safety.
  name: Encoded Global IDs
- description: First-party iOS (4.8 on the App Store) and Android (4.5 on Google Play) apps for technicians in the field.
  name: Mobile Apps (iOS / Android)
finops:
- name: Jobber Finops
  service_category: Business Application Software
  slug: jobber-finops
graphqls:
- description: Jobber's Developer API is a GraphQL API for accessing and modifying data on Jobber accounts.
  name: Jobber GraphQL API
  slug: jobber-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jobber.png
integrations:
- description: Native two-way sync of clients, invoices, and payments (Connect plan and up).
  name: QuickBooks Online
- description: First-party card and ACH processing for invoices and deposits.
  name: Stripe / Jobber Payments
- description: Sync clients into Mailchimp audiences for marketing campaigns.
  name: Mailchimp
- description: No-code integration with 5,000+ apps via Zapier triggers and actions.
  name: Zapier
- description: Two-way sync of Jobber jobs and visits with Google Calendar.
  name: Google Calendar
- description: Automated review collection from completed jobs.
  name: NiceJob
- description: Working-capital financing surfaced through the Jobber dashboard.
  name: Fundbox / Jobber Capital
json_schemas:
- name: Jobber Client
  property_count: 15
  slug: jobber-client
- name: Jobber Invoice
  property_count: 12
  slug: jobber-invoice
- name: Jobber Job
  property_count: 17
  slug: jobber-job
jsonld:
- class_count: 0
  name: Jobber Context
  property_count: 7
  slug: jobber-context
layout: provider
modified: '2026-05-25'
name: Jobber
nav: Providers
network: true
overview: 'Jobber publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Field Service Management, Home Service, Scheduling, Quoting, and Invoicing.


  The Jobber catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Jobber''s developer surface includes authentication, developer portal, documentation, signup flow, developer console, pricing, academy / training, and 21 more developer resources.'
plans:
- name: Jobber Plans Pricing
  plan_count: 4
  slug: jobber-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Jobber Rate Limits
  slug: jobber-rate-limits
rules:
- name: Jobber API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jobber-jsonschema-spectral-rules
- name: Jobber API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: jobber-rules
score:
  band: developing
  composite: 55.4
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 76.3
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jobber/refs/heads/main/screenshots/jobber-2026-06-20T183746.png
security:
- kind: authentication
  name: Jobber Authentication
  slug: jobber-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jobber Domain Security
  slug: jobber-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jobber Vulnerability Disclosure
  slug: jobber-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jobber
solutions:
- description: Residential and commercial cleaning operations.
  name: Cleaning
- description: Heating, ventilation, and air conditioning service.
  name: HVAC
- description: Residential and light-commercial plumbing.
  name: Plumbing
- description: Licensed electrical contractors.
  name: Electrical
- description: Recurring lawn maintenance, landscaping installs, and tree care.
  name: Landscaping and Lawn Care
- description: Interior and exterior residential painting.
  name: Painting
- description: Residential roofing and gutter service.
  name: Roofing
- description: General contractors, remodelers, and handyman businesses.
  name: Construction and Handyman
- description: Recurring chemical-treatment service businesses.
  name: Pest Control and Pool Care
tags:
- Field Service Management
- Home Service
- Scheduling
- Quoting
- Invoicing
- Dispatching
- Mobile Workforce
- CRM
- SaaS
- GraphQL
use_cases:
- description: Mirror Jobber clients into a marketing or CRM platform and push outreach events back into Jobber as Requests or Notes.
  name: CRM and Client Communications Sync
- description: Auto-create Jobs from accepted Quotes, schedule Visits, and post completion events to other systems.
  name: Quote and Job Workflow Automation
- description: Replicate Invoices, Payments, and Expenses into accounting (QuickBooks, Xero) or BI warehouses.
  name: Accounting and FinOps Integration
- description: Aggregate Visits, TimeSheetEntries, and Users to compute utilization, productivity, and route efficiency.
  name: Field Workforce Analytics
- description: Tie Requests and Leads back to ad and SEO sources to measure customer acquisition cost.
  name: Marketing Attribution
- description: Use Visit and User data to dispatch external crews from a third-party workforce management platform.
  name: Subcontractor and Crew Dispatching
- description: Wire inbound voice / chat AI assistants directly into Jobber Requests and scheduling mutations.
  name: AI Receptionist and Voice Booking
website: https://getjobber.com
---
