---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: REST API for advertisers and agencies to manage campaigns, teasers, targeting, conversion tracking, and access detailed statistics and reporting for native advertising campaigns.
  name: MGID Advertiser API
  slug: mgid-advertiser-api
- description: REST API for publishers to retrieve widget and website performance metrics including impressions, clicks, revenue, CPM, eCPM, visibility rates, and traffic analytics broken down by date, device, count
  name: MGID Publisher API
  slug: mgid-publisher-api
- description: REST API for advertising agencies to manage client accounts, retrieve financial statistics, view expense reports by service type, and transfer funds between agency and client accounts.
  name: MGID Agency API
  slug: mgid-agency-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mgid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mgid.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.mgid.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mgid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mgid-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.mgid.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://help.mgid.com/mgids-pricing-and-billing-model
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mgid.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/MGID
- group: commercial
  title: ''
  type: Plans
  url: plans/mgid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mgid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mgid-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://help.mgid.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mgid.com/advertisers/get-started-with-mgid-ads
- group: operate
  title: ''
  type: Support
  url: https://www.mgid.com/contacts
- group: operate
  title: ''
  type: FAQ
  url: https://help.mgid.com/advertisers/faq
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mgid.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.mgid.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mgid.com/services/advertisers-tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mgid.com/services/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/mgid-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mgid-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mgid-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mgid-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/mgid-packages.yml
- group: design
  title: ''
  type: Components
  url: components/mgid-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mgid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mgid-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mgid-llms.txt
created: '2026-06-13'
description: MGID is a native advertising platform providing a REST API for managing publishers, advertisers, and agencies. The API enables management of campaigns, ad teasers, widgets, conversion tracking, geo and device targeting, and access to detailed traffic and revenue analytics for content monetization across native, display, and video ad formats.
finops:
- name: Mgid Finops
  service_category: ''
  slug: mgid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mgid.png
jsonld:
- class_count: 23
  name: Mgid Context
  property_count: 0
  slug: mgid-context
layout: provider
modified: '2026-08-12'
name: MGID
nav: Providers
network: true
overview: 'MGID publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Native Advertising, Ad Tech, Publishers, Advertisers, and Campaigns.


  The MGID catalog on APIs.io includes 1 JSON-LD context.


  MGID''s developer surface includes documentation, engineering blog, pricing, API reference, getting-started guide, support, FAQ, and 22 more developer resources.'
plans:
- name: Mgid Plans Pricing
  plan_count: 3
  slug: mgid-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Mgid Rate Limits
  slug: mgid-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 40.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 38.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mgid/refs/heads/main/screenshots/mgid-2026-06-20T185319.png
security:
- kind: authentication
  name: Mgid Authentication
  slug: mgid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mgid Domain Security
  slug: mgid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mgid
tags:
- Native Advertising
- Ad Tech
- Publishers
- Advertisers
- Campaigns
- Content Monetization
- Programmatic
website: https://www.mgid.com
---
