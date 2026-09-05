---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pendo Agentic Access
  operation_count: 13
  slug: pendo-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- description: The Pendo Engage API provides programmatic access to product analytics data and in-app guide management — visitors, accounts, features, pages, guides, reports, metadata, and aggregations. Used to push
  name: Pendo Engage API
  slug: engage-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Accounts API from Pendo — 1 operation(s) for accounts.
  name: Pendo Accounts API
  slug: pendo-accounts-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Features API from Pendo — 2 operation(s) for features.
  name: Pendo Features API
  slug: pendo-features-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Guides API from Pendo — 2 operation(s) for guides.
  name: Pendo Guides API
  slug: pendo-guides-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Metadata API from Pendo — 2 operation(s) for metadata.
  name: Pendo Metadata API
  slug: pendo-metadata-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Pages API from Pendo — 2 operation(s) for pages.
  name: Pendo Pages API
  slug: pendo-pages-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Reports API from Pendo — 3 operation(s) for reports.
  name: Pendo Reports API
  slug: pendo-reports-api
- baseURL: https://app.pendo.io/api/v1
  baseurl_source: declared
  description: The Visitors API from Pendo — 1 operation(s) for visitors.
  name: Pendo Visitors API
  slug: pendo-visitors-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pendo Engage Accounts API
  slug: open-pendo-accounts-api
- collection_type: open
  name: Pendo Engage Accounts Features API
  slug: open-pendo-features-api
- collection_type: open
  name: Pendo Engage Accounts Guides API
  slug: open-pendo-guides-api
- collection_type: open
  name: Pendo Engage Accounts Metadata API
  slug: open-pendo-metadata-api
- collection_type: open
  name: Pendo Engage Accounts Pages API
  slug: open-pendo-pages-api
- collection_type: open
  name: Pendo Engage Accounts Reports API
  slug: open-pendo-reports-api
- collection_type: open
  name: Pendo Engage Accounts Visitors API
  slug: open-pendo-visitors-api
- collection_type: open
  name: Pendo Engage API
  slug: open-pendo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pendo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pendo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pendo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pendo-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pendo-io
- group: company
  title: ''
  type: Website
  url: https://www.pendo.io/
- group: other
  title: ''
  type: Developers
  url: https://www.pendo.io/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://engageapi.pendo.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/pendo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pendo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pendo-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://app.pendo.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.pendo.io/blog/
created: '2026-05-08'
description: Pendo is a product analytics, in-app guidance, and feedback platform. Captures product usage, surfaces NPS, and delivers in-app messages, walkthroughs, and resource centers.
finops:
- name: Pendo Finops
  service_category: Product
  slug: pendo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pendo.png
layout: provider
modified: '2026-05-08'
name: Pendo
nav: Providers
network: true
overview: 'Pendo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Features API, Guides API, and 4 more. Tagged areas include Product, Analytics, In-App Guidance, Customer Success, and NPS.


  Pendo''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Pendo Plans Pricing
  plan_count: 1
  slug: pendo-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Pendo Rate Limits
  slug: pendo-rate-limits
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 17.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pendo/refs/heads/main/screenshots/pendo-2026-06-20T191536.png
security:
- kind: authentication
  name: Pendo Authentication
  slug: pendo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pendo Domain Security
  slug: pendo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pendo Trust Center
  slug: pendo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: pendo
tags:
- Product
- Analytics
- In-App Guidance
- Customer Success
- NPS
website: https://www.pendo.io/
---
