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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Indexing Agentic Access
  operation_count: 2
  slug: google-indexing-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- baseURL: https://indexing.googleapis.com/v3
  baseurl_source: declared
  description: The urlNotifications API from Google Indexing — 1 operation(s) for urlnotifications.
  name: Google Indexing URL Notifications API
  slug: google-indexing-urlnotifications-api
- baseURL: https://indexing.googleapis.com/v3
  baseurl_source: declared
  description: The urlNotifications:publish API from Google Indexing — 1 operation(s) for urlnotifications:publish.
  name: Google Indexing urlNotifications:publish API
  slug: google-indexing-urlnotifications-publish-api
artifact_total: 21
collections:
- collection_type: postman
  name: Google Indexing urlNotifications API
  slug: postman-google-indexing-urlnotifications-api
- collection_type: postman
  name: Google Indexing urlNotifications urlNotifications:publish API
  slug: postman-google-indexing-urlnotifications-publish-api
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
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-indexing/overview
- group: agent
  href: https://artifacts.apis.io/google-indexing/agentic-access/google-indexing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-indexing-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-indexing/security/google-indexing-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-indexing-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-indexing/security/google-indexing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-indexing-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-indexing/authentication/google-indexing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-indexing-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-indexing/scopes/google-indexing-scopes.yml
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
  href: https://artifacts.apis.io/google-indexing/json-ld/context.jsonld
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
  href: https://artifacts.apis.io/google-indexing/sandbox/google-indexing-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-indexing-sandbox.yml
- group: build
  href: https://artifacts.apis.io/google-indexing/packages/google-indexing-packages.yml
  title: ''
  type: Packages
  url: packages/google-indexing-packages.yml
- group: build
  href: https://artifacts.apis.io/google-indexing/packages/google-indexing-packages.yml
  title: ''
  type: SDKs
  url: packages/google-indexing-packages.yml
- group: agent
  href: https://artifacts.apis.io/google-indexing/well-known/google-indexing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-indexing-well-known.yml
- group: auth
  href: https://artifacts.apis.io/google-indexing/well-known/google-indexing-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-indexing-security.txt
- group: auth
  href: https://artifacts.apis.io/google-indexing/security/google-indexing-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-indexing-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/google-indexing/llms/google-indexing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-indexing-llms.txt
- group: design
  href: https://artifacts.apis.io/google-indexing/conformance/google-indexing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-indexing-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-indexing/errors/google-indexing-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-indexing-error-codes.yml
- group: design
  href: https://artifacts.apis.io/google-indexing/lifecycle/google-indexing-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-indexing-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/google-indexing/conventions/google-indexing-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-indexing-conventions.yml
- group: operate
  href: https://artifacts.apis.io/google-indexing/changelog/google-indexing-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-indexing-changelog.yml
- group: design
  href: https://artifacts.apis.io/google-indexing/data-model/google-indexing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-indexing-data-model.yml
- group: agent
  href: https://artifacts.apis.io/google-indexing/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/google-indexing/plans/google-indexing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-indexing-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-indexing/rate-limits/google-indexing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-indexing-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-indexing/finops/google-indexing-finops.yml
  title: ''
  type: FinOps
  url: finops/google-indexing-finops.yml
- group: design
  href: https://artifacts.apis.io/google-indexing/rules/google-indexing-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/google-indexing-spectral-rules.yml
created: '2026-03-13'
description: The Google Indexing API lets a site owner tell Google directly when a page has been added, updated, or removed, instead of waiting for a crawl. It is a two-operation API — publish a URL notification, and read back the latest notification metadata for a URL. Google restricts its use to pages carrying JobPosting structured data, or BroadcastEvent embedded in a VideoObject. It is free of charge, capped by default at 200 publish requests per day per Google Cloud project, and gated on Search Console ownership verification rather than on price.
finops:
- has_sources: true
  method: derived
  name: Google Indexing Finops
  primary_unit: ''
  service_category: ''
  slug: google-indexing-finops
  template: true
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
overview: 'Google Indexing publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: URL Notifications API and urlNotifications:publish API. Tagged areas include Crawling, Google, Indexing, Search, and SEO.


  The Google Indexing catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Indexing''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, API reference, pricing, and 32 more developer resources.'
plans:
- name: Google Indexing Plans Pricing
  plan_count: 1
  slug: google-indexing-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Google Indexing Rate Limits
  slug: google-indexing-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Google Indexing — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-indexing-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
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
  composite: 66.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.9
    catalog_earned_first_party: 20.0
    catalog_gap: 40.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 74.4
    discoverability: 66.1
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 66.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/google-indexing/google-indexing-2026-06-20T182255.png
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
skill_count: 2
skills:
- name: Tell Google a page has been removed
  slug: google-indexing-remove-url-from-index
- name: Submit a URL to Google for crawling
  slug: google-indexing-submit-url-for-crawling
slug: google-indexing
tags:
- Crawling
- Google
- Indexing
- Search
- SEO
- URLs
website: https://www.google.com/
---
