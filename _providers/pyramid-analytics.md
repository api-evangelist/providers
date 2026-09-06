---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Pyramid's main programmatic surface. All calls are HTTP POST against /API3/<section>/<method> on the customer's own Pyramid server, carrying a JSON body and a "paToken" security token in the HTTP head
  name: Pyramid REST API 3.0
  slug: pyramid-analytics-rest-api-3
- description: A client-side JavaScript API (PyramidEmbedClient) for embedding Pyramid content — hubs, discoveries, presentations, publications and the search bar — into third-party web applications, with its own em
  name: Pyramid Embed API
  slug: pyramid-analytics-embed-api
artifact_total: 7
asyncapis:
- description: ''
  name: Pyramid Analytics Webhooks
  slug: pyramid-analytics-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pyramid-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pyramidanalytics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/API%20Overview.htm
- group: docs
  title: ''
  type: Documentation
  url: https://help.pyramidanalytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/APIs%20and%20SDKs.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://help.pyramidanalytics.com/Content/Root/developer/reference/APIs/REST%20API/Using%20REST.htm
- group: operate
  title: ''
  type: Support
  url: https://www.pyramidanalytics.com/company/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.pyramidanalytics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pyramidanalytics.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pyramid-Analytics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pyramidanalytics.com/decision-intelligence-platform/get-pricing/
- group: start
  title: ''
  type: Login
  url: https://customers.pyramidanalytics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pyramidanalytics.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pyramidanalytics.com/privacy-policy/
- group: operate
  title: ''
  type: Roadmap
  url: https://help.pyramidanalytics.com/Content/Root/Guides/general/Release%20Framework.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pyramid-analytics-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pyramid-analytics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/pyramid-analytics-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/pyramid-analytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pyramid-analytics-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pyramid-analytics-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pyramid-analytics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pyramid-analytics-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pyramid-analytics-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/pyramid-analytics-components.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/pyramid-analytics-stock
created: '2026-08-26'
description: Pyramid Analytics is a decision intelligence software company whose platform unifies data preparation, business analytics and AI-assisted insight generation in a single environment, deployed either onto the customer's own infrastructure ("Pyramid Deployed") or hosted by Pyramid ("Pyramid Managed"). Its programmable surface is a POST-only REST API — API 3.0, documented as 234 methods across authentication, access, content, analytics, dataSources, tasks, notification and themes — together with a JavaScript Embed API for hosting Pyramid content inside third-party applications, Custom Visual and Workflow APIs, an OData feed that turns any Pyramid query into a consumable data source, and Swagger-generated client SDKs for Java, C#, JavaScript/TypeScript, Python and PHP. Because Pyramid runs inside each customer's own tenancy, the API base URL is the customer's own Pyramid server rather than a vendor-hosted host, and the SDK packages are distributed through the customer portal rather
  than public package registries.
image: https://www.pyramidanalytics.com/wp-content/uploads/2022/02/pyramid-analytics.jpg
layout: provider
modified: '2026-08-26'
name: Pyramid Analytics
nav: Providers
network: true
overview: 'Pyramid Analytics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Business Intelligence, Decision Intelligence, Embedded Analytics, and Data Visualization.


  The Pyramid Analytics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pyramid Analytics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 19 more developer resources.'
plans:
- name: Pyramid Analytics Plans Pricing
  plan_count: 0
  slug: pyramid-analytics-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Pyramid Analytics Rate Limits
  slug: pyramid-analytics-rate-limits
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 46.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pyramid-analytics/refs/heads/main/screenshots/pyramid-analytics-2026-09-02T152358.png
security:
- kind: authentication
  name: Pyramid Analytics Authentication
  slug: pyramid-analytics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pyramid Analytics Domain Security
  slug: pyramid-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pyramid-analytics
tags:
- Analytics
- Business Intelligence
- Decision Intelligence
- Embedded Analytics
- Data Visualization
- Data Preparation
- Enterprise Software
- Reporting
website: https://www.pyramidanalytics.com/
---
