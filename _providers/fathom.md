---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 11
  human_in_the_loop: 0
  name: Fathom Agentic Access
  operation_count: 20
  slug: fathom-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 5
apis:
- description: Account information
  name: Fathom Analytics Account API
  slug: fathom-account-api
- description: Event management per site
  name: Fathom Analytics Events API
  slug: fathom-events-api
- description: Milestone management per site
  name: Fathom Analytics Milestones API
  slug: fathom-milestones-api
- description: Aggregation reports and current visitor counts
  name: Fathom Analytics Reports API
  slug: fathom-reports-api
- description: Site management
  name: Fathom Analytics Sites API
  slug: fathom-sites-api
artifact_total: 28
collections:
- collection_type: postman
  name: Fathom Analytics REST Account API
  slug: postman-fathom-account-api
- collection_type: postman
  name: Fathom Analytics REST Account Events API
  slug: postman-fathom-events-api
- collection_type: postman
  name: Fathom Analytics REST Account Milestones API
  slug: postman-fathom-milestones-api
- collection_type: postman
  name: Fathom Analytics REST Account Reports API
  slug: postman-fathom-reports-api
- collection_type: postman
  name: Fathom Analytics REST Account Sites API
  slug: postman-fathom-sites-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fathom-analytics/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fathom-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fathom-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fathom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fathom-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://usefathom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://usefathom.com/docs
- group: docs
  title: ''
  type: APIDocumentation
  url: https://usefathom.com/api
- group: company
  title: ''
  type: Blog
  url: https://usefathom.com/blog
- group: company
  title: ''
  type: BlogFeed
  url: https://usefathom.com/blog/feed.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://usefathom.com/changelog
- group: operate
  title: ''
  type: ChangelogFeed
  url: https://usefathom.com/changelog/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://usefathom.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usefathom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usefathom
- group: other
  title: ''
  type: X
  url: https://twitter.com/usefathom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fathom-analytics
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/plans/fathom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/rate-limits/fathom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/finops/fathom-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/vocabulary/fathom-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/json-ld/fathom-context.jsonld
- group: company
  title: ''
  type: BlogFeedJSON
  url: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/blogs/blogs.json
created: '2026-06-12'
description: Fathom Analytics is a privacy-first website analytics platform that provides GDPR-compliant, cookie-free analytics as an alternative to Google Analytics. The platform serves thousands of companies, including Fortune 100 enterprises and government agencies, offering simple and accurate traffic metrics without tracking personally identifiable information. Fathom exposes a REST API with base URL https://api.usefathom.com/v1, enabling developers to manage sites, events, and milestones, generate aggregated custom reports, and retrieve real-time visitor counts. Authentication is via Bearer token API keys, which are generated in the account settings area and support configurable permissions scoped to admin, all sites, or individual sites.
examples:
- key_count: 4
  name: Fathom Get Account Example
  slug: fathom-get-account-example
- key_count: 1
  name: Fathom Get Aggregations Example
  slug: fathom-get-aggregations-example
- key_count: 3
  name: Fathom Get Current Visitors Example
  slug: fathom-get-current-visitors-example
- key_count: 5
  name: Fathom Get Site Example
  slug: fathom-get-site-example
- key_count: 3
  name: Fathom List Sites Example
  slug: fathom-list-sites-example
finops:
- name: Fathom Finops
  service_category: ''
  slug: fathom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fathom.png
json_schemas:
- name: Fathom Account
  property_count: 4
  slug: fathom-account
- name: Fathom Event
  property_count: 5
  slug: fathom-event
- name: Fathom Milestone
  property_count: 6
  slug: fathom-milestone
- name: Fathom Site
  property_count: 5
  slug: fathom-site
jsonld:
- class_count: 6
  name: Fathom Context
  property_count: 24
  slug: fathom-context
layout: provider
modified: '2026-06-12'
name: Fathom Analytics
nav: Providers
network: true
overview: 'Fathom Analytics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Events API, Milestones API, and 2 more. Tagged areas include Analytics, Privacy, GDPR, Website Analytics, and Cookieless.


  The Fathom Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fathom Analytics'' developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 18 more developer resources.'
plans:
- name: Fathom Plans Pricing
  plan_count: 5
  slug: fathom-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Fathom Rate Limits
  slug: fathom-rate-limits
rules:
- name: Fathom Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fathom-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.0
  delta: -4.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 69.5
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 64.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fathom/refs/heads/main/screenshots/fathom-2026-06-20T181055.png
security:
- kind: authentication
  name: Fathom Authentication
  slug: fathom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fathom Domain Security
  slug: fathom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fathom Trust Center
  slug: fathom-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: fathom
tags:
- Analytics
- Privacy
- GDPR
- Website Analytics
- Cookieless
- Page Views
- Events
- Reporting
website: https://usefathom.com/
---
