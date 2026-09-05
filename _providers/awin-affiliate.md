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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Awin Affiliate Agentic Access
  operation_count: 12
  slug: awin-affiliate-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.awin.com
  baseurl_source: declared
  description: Accounts the authenticated user can access.
  name: Awin Accounts API
  slug: awin-affiliate-accounts-api
- baseURL: https://api.awin.com
  baseurl_source: declared
  description: Commission groups and rates for a programme.
  name: Awin Commission Groups API
  slug: awin-affiliate-commission-groups-api
- baseURL: https://api.awin.com
  baseurl_source: declared
  description: Advertiser programmes and their details.
  name: Awin Programmes API
  slug: awin-affiliate-programmes-api
- baseURL: https://api.awin.com
  baseurl_source: declared
  description: Aggregated performance reports.
  name: Awin Reports API
  slug: awin-affiliate-reports-api
- baseURL: https://api.awin.com
  baseurl_source: declared
  description: Individual publisher and advertiser transactions.
  name: Awin Transactions API
  slug: awin-affiliate-transactions-api
artifact_total: 21
asyncapis:
- description: ''
  name: Awin Affiliate Webhooks
  slug: awin-affiliate-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Awin Accounts API
  slug: open-awin-affiliate-accounts-api
- collection_type: open
  name: Awin Accounts Commission Groups API
  slug: open-awin-affiliate-commission-groups-api
- collection_type: open
  name: Awin Accounts Programmes API
  slug: open-awin-affiliate-programmes-api
- collection_type: open
  name: Awin Accounts Reports API
  slug: open-awin-affiliate-reports-api
- collection_type: open
  name: Awin Accounts Transactions API
  slug: open-awin-affiliate-transactions-api
- collection_type: open
  name: Awin API
  slug: open-awin-affiliate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/awin-affiliate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/awin-affiliate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/awin-affiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/awin-affiliate-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/awin
- group: company
  title: ''
  type: Website
  url: https://www.awin.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.awin.com/apidocs/introduction-1
- group: auth
  title: ''
  type: Authentication
  url: https://help.awin.com/apidocs/api-authentication
- group: commercial
  title: ''
  type: Plans
  url: plans/awin-affiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/awin-affiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/awin-affiliate-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/awin-affiliate-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/awin-affiliate-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/awin-affiliate-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.awin.com/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/awin-affiliate-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.awin.com/gb/legal/information-security
- group: design
  title: ''
  type: Conformance
  url: conformance/awin-affiliate-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/awin-affiliate-llms.txt
- group: agent
  title: ''
  type: MCP
  url: mcp/awin-affiliate-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/awin-affiliate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/awin-affiliate-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.awin.com
- group: design
  title: ''
  type: Conventions
  url: conventions/awin-affiliate-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/awin-affiliate-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.awin.com/gb/product-releases
- group: design
  title: ''
  type: DataModel
  url: data-model/awin-affiliate-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/awin-affiliate-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Console
  url: https://help.awin.com/apidocs/introduction-1
- group: build
  title: ''
  type: Postman
  url: collections/awin-affiliate.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.awin.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.awin.com/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://help.awin.com/apidocs/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://success.awin.com/s/contactsupport
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.awin.com
- group: company
  title: ''
  type: Blog
  url: https://www.awin.com/gb/market-insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/awin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.awin.com/gb/pricing/advertisers
- group: start
  title: ''
  type: SignUp
  url: https://www.awin.com/gb/getting-started
- group: start
  title: ''
  type: Login
  url: https://ui.awin.com/idp/en/awin/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.awin.com/gb/publisher-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.awin.com/gb/privacy
created: '2026-07-05'
description: Awin is a global affiliate marketing network connecting advertisers (brands) with publishers (content creators, cashback, voucher, and loyalty partners) across thousands of programmes worldwide. Awin exposes a documented public REST API at https://api.awin.com that lets both publishers and advertisers pull data such as individual transactions and aggregated performance reports, inspect commission groups and programme details, list the accounts a user can access, and generate tracking links and offers. All endpoints follow REST principles, return JSON, are served over HTTPS only, and authenticate with an OAuth 2.0 Bearer access token issued at the user level from the Awin UI (the Create Transactions API is the exception and uses an x-api-key). A platform-wide throttle limits requests to 20 API calls per minute per user.
finops:
- name: Awin Affiliate Finops
  service_category: Marketing and Advertising
  slug: awin-affiliate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/awin-affiliate.png
layout: provider
modified: '2026-08-13'
name: Awin
nav: Providers
network: true
overview: 'Awin publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Commission Groups API, Programmes API, and 2 more. Tagged areas include Affiliate Marketing, Advertising, Publishers, Advertisers, and Transaction.


  The Awin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Awin''s developer surface includes authentication, documentation, changelog, developer console, API reference, getting-started guide, support, and 36 more developer resources.'
plans:
- name: Awin Affiliate Plans Pricing
  plan_count: 4
  slug: awin-affiliate-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Awin Affiliate Rate Limits
  slug: awin-affiliate-rate-limits
score:
  band: exemplar
  composite: 68.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 60.4
    developer_ergonomics: 67.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/awin-affiliate/refs/heads/main/screenshots/awin-affiliate-2026-07-25T202025.png
security:
- kind: authentication
  name: Awin Affiliate Authentication
  slug: awin-affiliate-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Awin Affiliate Domain Security
  slug: awin-affiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Awin Affiliate Vulnerability Disclosure
  slug: awin-affiliate-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Awin Affiliate Trust Center
  slug: awin-affiliate-trust-center
  summary_line: ISO 27001, GDPR
slug: awin-affiliate
tags:
- Affiliate Marketing
- Advertising
- Publishers
- Advertisers
- Transaction
- Reporting
- Commissions
- Performance Marketing
website: https://www.awin.com
---
