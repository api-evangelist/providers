---
access_model:
  confidence: high
  label: Free · Self-serve signup, eligibility-gated
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Indexing Agentic Access
  operation_count: 2
  slug: google-indexing-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The urlNotifications API from Google Indexing — 1 operation(s) for urlnotifications.
  name: Google Indexing urlNotifications API
  slug: google-indexing-urlnotifications-api
- description: The urlNotifications:publish API from Google Indexing — 1 operation(s) for urlnotifications:publish.
  name: Google Indexing urlNotifications:publish API
  slug: google-indexing-urlnotifications-publish-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google Indexing urlNotifications API
  slug: postman-google-indexing-urlnotifications-api
- collection_type: postman
  name: Google Indexing urlNotifications urlNotifications:publish API
  slug: postman-google-indexing-urlnotifications-publish-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Indexing urlNotifications API
  slug: open-google-indexing-urlnotifications-api
- collection_type: open
  name: Google Indexing urlNotifications urlNotifications:publish API
  slug: open-google-indexing-urlnotifications-publish-api
- collection_type: open
  name: Google Indexing API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-indexing/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-indexing-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-indexing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-indexing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-indexing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-indexing-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/search/apis/indexing-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/search/apis/indexing-api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.search.google.com/
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/webmasters/community
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/search/apis/indexing-api/v3/reference/indexing/rest/v3/urlNotifications
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/search/apis/indexing-api/v3/quota-pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/apis/library/indexing.googleapis.com
- group: company
  title: ''
  type: Blog
  url: https://developers.google.com/search/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-indexing-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-indexing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-indexing-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-indexing-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-indexing-security.txt
- group: auth
  title: ''
  type: Security
  url: security/google-indexing-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-indexing-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/google-indexing-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-indexing-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-indexing-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-indexing-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-indexing-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-indexing-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-indexing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-indexing-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-indexing-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-indexing-spectral-rules.yml
created: '2026-03-13'
description: The Google Indexing API lets a site owner tell Google directly when a page has been added, updated, or removed, instead of waiting for a crawl. It is a two-operation API — publish a URL notification, and read back the latest notification metadata for a URL. Google restricts its use to pages carrying JobPosting structured data, or BroadcastEvent embedded in a VideoObject. It is free of charge, capped by default at 200 publish requests per day per Google Cloud project, and gated on Search Console ownership verification rather than on price.
finops:
- name: Google Indexing Finops
  service_category: API
  slug: google-indexing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-indexing.png
json_schemas:
- name: Google Indexing URL Notification
  property_count: 3
  slug: UrlNotification
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-08-13'
name: Google Indexing
nav: Providers
network: true
overview: 'Google Indexing publishes 2 APIs on the [APIs.io](https://apis.io/) network: urlNotifications API and urlNotifications:publish API. Tagged areas include Crawling, Google, Indexing, Search, and SEO.


  The Google Indexing catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Indexing''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, API reference, pricing, and 31 more developer resources.'
plans:
- name: Google Indexing Plans Pricing
  plan_count: 1
  slug: google-indexing-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Google Indexing Rate Limits
  slug: google-indexing-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Google Indexing API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-indexing-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Google Indexing API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: google-indexing-spectral-rules
scopes:
- name: Google Indexing Scopes
  scope_count: 1
  slug: google-indexing-scopes
  summary_line: 1 scope · jwt-bearer/authorizationCode
score:
  band: strong
  composite: 63.7
  coverage:
    artifact_dirs: 28
    catalog_gap: 36.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 66.7
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/screenshots/google-indexing-2026-06-20T182255.png
security:
- kind: authentication
  name: Google Indexing Authentication
  slug: google-indexing-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Indexing Domain Security
  slug: google-indexing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Indexing Vulnerability Disclosure
  slug: google-indexing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-indexing
tags:
- Crawling
- Google
- Indexing
- Search
- SEO
- URLs
website: https://developers.google.com/search/apis/indexing-api
---
