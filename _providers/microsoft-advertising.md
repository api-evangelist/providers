---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: The Microsoft Advertising Campaign Management API enables programmatic management of advertising campaigns, ad groups, ads, keywords, and targeting. Developers can create and modify campaign structure
  name: Microsoft Advertising Campaign Management API
  slug: campaign-management-api
- description: The Microsoft Advertising Reporting API provides access to performance reports for campaigns, ad groups, ads, and keywords. Developers can request reports on impressions, clicks, conversions, spend, a
  name: Microsoft Advertising Reporting API
  slug: reporting-api
- description: The Microsoft Advertising Bulk API enables efficient management of large-scale advertising campaigns through batch upload and download operations. It supports CSV-based bulk operations for creating, u
  name: Microsoft Advertising Bulk API
  slug: bulk-api
- description: Keyword ideas, bid and budget opportunities, and traffic estimates for Microsoft Advertising campaigns via the AdInsightService SOAP endpoint.
  name: Microsoft Advertising Ad Insight API
  slug: ad-insight-api
- description: Manage Microsoft Advertising customers, accounts, users and agency links via the CustomerManagementService SOAP endpoint.
  name: Microsoft Advertising Customer Management API
  slug: customer-management-api
- description: Retrieve invoices, account balances and insertion orders via the CustomerBillingService SOAP endpoint.
  name: Microsoft Advertising Customer Billing API
  slug: customer-billing-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/microsoft-advertising/changelog/microsoft-advertising-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-advertising-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-advertising/conventions/microsoft-advertising-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-advertising-conventions.yml
- group: start
  href: https://artifacts.apis.io/microsoft-advertising/sandbox/microsoft-advertising-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-advertising-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/authentication/microsoft-advertising-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-advertising-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/scopes/microsoft-advertising-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-advertising-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/advertising/guides/release-notes#breaking-changes
- group: design
  href: https://artifacts.apis.io/microsoft-advertising/lifecycle/microsoft-advertising-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-advertising-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-advertising/errors/microsoft-advertising-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-advertising-error-codes.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-advertising/llms/microsoft-advertising-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-advertising-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/well-known/microsoft-advertising-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-advertising-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-advertising/well-known/microsoft-advertising-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-advertising-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-advertising/hosts/microsoft-advertising-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-advertising-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-advertising/integrations/microsoft-advertising-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-advertising-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-advertising/vendors/microsoft-advertising-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-advertising-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-advertising/packages/microsoft-advertising-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-advertising-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/security/microsoft-advertising-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-advertising-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-advertising/plans/microsoft-advertising-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-advertising-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-advertising/rate-limits/microsoft-advertising-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-advertising-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-advertising/finops/microsoft-advertising-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-advertising-finops.yml
- group: company
  title: ''
  type: Website
  url: https://about.ads.microsoft.com/en-us
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/security/microsoft-advertising-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-advertising-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-advertising/security/microsoft-advertising-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-advertising-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-advertising
- group: start
  title: ''
  type: Portal
  url: https://ads.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/advertising/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/advertising/guides/client-libraries
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/advertising/guides/authentication-oauth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://about.ads.microsoft.com/en-us/blog/rss
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/advertising/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/advertising/guides/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/advertising/guides/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BingAds
created: '2024-01-15'
description: Microsoft Advertising provides APIs for managing ad campaigns, reporting on performance, and bulk operations across the Microsoft Advertising network including Bing, MSN, and partner sites. The platform offers programmatic access to campaign management, reporting, and bulk operations services for advertisers and developers.
finops:
- has_sources: false
  method: generated
  name: Microsoft Advertising Finops
  primary_unit: request
  service_category: API
  slug: microsoft-advertising-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-advertising.png
layout: provider
modified: '2026-11-04'
name: Microsoft Advertising
nav: Providers
network: true
overview: 'Microsoft Advertising is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Analytics, Bing Ads, Bulk Operations, and Campaigns.


  Microsoft Advertising''s developer surface includes changelog, sandbox, authentication, developer portal, support, engineering blog, documentation, and 31 more developer resources.'
plans:
- name: Microsoft Advertising Plans Pricing
  plan_count: 3
  slug: microsoft-advertising-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Advertising Rate Limits
  slug: microsoft-advertising-rate-limits
scopes:
- name: Microsoft Advertising Scopes
  scope_count: 2
  slug: microsoft-advertising-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.5
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 80.4
    operational_transparency: 68.4
  previous_composite: 27.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microsoft-advertising/microsoft-advertising-2026-06-20T185348.png
security:
- kind: authentication
  name: Microsoft Advertising Authentication
  slug: microsoft-advertising-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Microsoft Advertising Domain Security
  slug: microsoft-advertising-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Advertising Vulnerability Disclosure
  slug: microsoft-advertising-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Advertising Trust Center
  slug: microsoft-advertising-trust-center
  summary_line: GDPR
slug: microsoft-advertising
tags:
- Advertising
- Analytics
- Bing Ads
- Bulk Operations
- Campaigns
- Microsoft
- Reporting
- SOAP
- Search Advertising
website: https://about.ads.microsoft.com/en-us
---
