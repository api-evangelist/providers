---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Pagespeed Agentic Access
  operation_count: 1
  slug: google-pagespeed-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- baseURL: https://www.googleapis.com/pagespeedonline/v5
  baseurl_source: declared
  description: Page performance analysis
  name: Google PageSpeed Analysis API
  slug: google-pagespeed-analysis-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google PageSpeed PageSpeed Insights Analysis API
  slug: postman-google-pagespeed-analysis-api
- collection_type: open
  name: Google PageSpeed PageSpeed Insights Analysis API
  slug: open-google-pagespeed-analysis-api
- collection_type: open
  name: Google PageSpeed PageSpeed Insights API
  slug: open-pagespeed-insights
common:
- group: commercial
  href: https://artifacts.apis.io/google-pagespeed/finops/google-pagespeed-finops.yml
  title: ''
  type: FinOps
  url: finops/google-pagespeed-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-pagespeed/overview
- group: agent
  href: https://artifacts.apis.io/google-pagespeed/agentic-access/google-pagespeed-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-pagespeed-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-pagespeed/security/google-pagespeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-pagespeed-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-pagespeed/authentication/google-pagespeed-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-pagespeed-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pagespeed
- group: start
  title: ''
  type: Portal
  url: https://pagespeed.web.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/speed/docs/insights/v5/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/speed/docs/insights
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/speed/docs/insights/v5/get-started#APIKey
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
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/webmasters
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apis/library/pagespeedonline.googleapis.com
- group: design
  href: https://artifacts.apis.io/google-pagespeed/json-ld/google-pagespeed-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-pagespeed-context.jsonld
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/speed/docs/insights/v5/reference
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/apis/credentials
- group: build
  href: https://artifacts.apis.io/google-pagespeed/packages/google-pagespeed-packages.yml
  title: ''
  type: Packages
  url: packages/google-pagespeed-packages.yml
- group: build
  href: https://artifacts.apis.io/google-pagespeed/packages/google-pagespeed-packages.yml
  title: ''
  type: SDKs
  url: packages/google-pagespeed-packages.yml
- group: auth
  href: https://artifacts.apis.io/google-pagespeed/well-known/google-pagespeed-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-pagespeed-security.txt
- group: auth
  href: https://artifacts.apis.io/google-pagespeed/security/google-pagespeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pagespeed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: agent
  href: https://artifacts.apis.io/google-pagespeed/llms/google-pagespeed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-pagespeed-llms.txt
- group: design
  href: https://artifacts.apis.io/google-pagespeed/conformance/google-pagespeed-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-pagespeed-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-pagespeed/errors/google-pagespeed-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-pagespeed-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-pagespeed/lifecycle/google-pagespeed-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-pagespeed-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/speed/docs/insights/release_notes
- group: operate
  href: https://artifacts.apis.io/google-pagespeed/changelog/google-pagespeed-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-pagespeed-changelog.yml
- group: auth
  href: https://artifacts.apis.io/google-pagespeed/scopes/google-pagespeed-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-pagespeed-scopes.yml
- group: start
  href: https://artifacts.apis.io/google-pagespeed/sandbox/google-pagespeed-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-pagespeed-sandbox.yml
- group: design
  href: https://artifacts.apis.io/google-pagespeed/conventions/google-pagespeed-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-pagespeed-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-pagespeed/data-model/google-pagespeed-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-pagespeed-data-model.yml
- group: agent
  href: https://artifacts.apis.io/google-pagespeed/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/google-pagespeed/plans/google-pagespeed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-pagespeed-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-pagespeed/rate-limits/google-pagespeed-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-pagespeed-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/google-pagespeed/rules/google-pagespeed-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/google-pagespeed-jsonschema-spectral-rules.yml
- group: build
  href: https://artifacts.apis.io/google-pagespeed/postman/google-pagespeed-analysis-api.postman_collection.json
  title: ''
  type: PostmanCollection
  url: postman/google-pagespeed-analysis-api.postman_collection.json
created: '2026-03-13'
description: Google PageSpeed Insights provides APIs for analyzing the performance of web pages on both mobile and desktop devices, returning performance scores, Core Web Vitals metrics, and actionable optimization recommendations powered by Lighthouse.
finops:
- has_sources: true
  method: derived
  name: Google Pagespeed Finops
  primary_unit: ''
  service_category: ''
  slug: google-pagespeed-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-pagespeed.png
json_schemas:
- name: PageSpeed Insights Result
  property_count: 5
  slug: google-pagespeed-result
jsonld:
- class_count: 0
  name: Google Pagespeed Context
  property_count: 3
  slug: google-pagespeed-context
layout: provider
modified: '2026-08-13'
name: Google PageSpeed
nav: Providers
network: true
overview: 'Google PageSpeed publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Analysis API. Tagged areas include Core Web Vitals, Google, Lighthouse, Page Speed, and SEO.


  The Google PageSpeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google PageSpeed''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, developer console, API reference, and 32 more developer resources.'
plans:
- name: Google Pagespeed Plans Pricing
  plan_count: 0
  slug: google-pagespeed-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Google Pagespeed Rate Limits
  slug: google-pagespeed-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google PageSpeed — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-pagespeed-jsonschema-spectral-rules
scopes:
- name: Google Pagespeed Scopes
  scope_count: 1
  slug: google-pagespeed-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 50.7
    catalog_earned_first_party: 0.0
    catalog_gap: 64.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 14.4
    contract_quality: 58.5
    developer_ergonomics: 72.0
    discoverability: 66.1
    operational_transparency: 55.3
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
screenshot: https://apis.io/screenshots/google-pagespeed/google-pagespeed-2026-06-20T182219.png
security:
- kind: authentication
  name: Google Pagespeed Authentication
  slug: google-pagespeed-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Pagespeed Domain Security
  slug: google-pagespeed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Google Pagespeed Vulnerability Disclosure
  slug: google-pagespeed-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: Audit a page with PageSpeed Insights
  slug: google-pagespeed-audit-page-performance
- name: Track Core Web Vitals across a set of pages
  slug: google-pagespeed-track-core-web-vitals
slug: google-pagespeed
tags:
- Core Web Vitals
- Google
- Lighthouse
- Page Speed
- SEO
- Web Performance
website: https://www.google.com/
---
