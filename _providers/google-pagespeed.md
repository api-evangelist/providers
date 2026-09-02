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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Pagespeed Agentic Access
  operation_count: 1
  slug: google-pagespeed-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Page performance analysis
  name: Google PageSpeed Analysis API
  slug: google-pagespeed-analysis-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google PageSpeed PageSpeed Insights Analysis API
  slug: postman-google-pagespeed-analysis-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google PageSpeed PageSpeed Insights Analysis API
  slug: open-google-pagespeed-analysis-api
- collection_type: open
  name: Google PageSpeed PageSpeed Insights API
  slug: open-pagespeed-insights
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-pagespeed/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-pagespeed-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-pagespeed-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/google-pagespeed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-pagespeed-packages.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-pagespeed-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-pagespeed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-pagespeed-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/google-pagespeed-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-pagespeed-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-pagespeed-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/speed/docs/insights/release_notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-pagespeed-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-pagespeed-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/google-pagespeed-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-pagespeed-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-pagespeed-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-pagespeed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-pagespeed-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-pagespeed-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: PostmanCollection
  url: postman/google-pagespeed-analysis-api.postman_collection.json
created: '2026-03-13'
description: Google PageSpeed Insights provides APIs for analyzing the performance of web pages on both mobile and desktop devices, returning performance scores, Core Web Vitals metrics, and actionable optimization recommendations powered by Lighthouse.
finops:
- name: Google Pagespeed Finops
  service_category: API
  slug: google-pagespeed-finops
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
overview: 'Google PageSpeed publishes 1 API on the [APIs.io](https://apis.io/) network: Analysis API. Tagged areas include Core Web Vitals, Google, Lighthouse, Page Speed, and SEO.


  The Google PageSpeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google PageSpeed''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, developer console, API reference, and 30 more developer resources.'
plans:
- name: Google Pagespeed Plans Pricing
  plan_count: 0
  slug: google-pagespeed-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Google Pagespeed Rate Limits
  slug: google-pagespeed-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google PageSpeed API Rules
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
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 28
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 14.4
    contract_quality: 64.6
    developer_ergonomics: 67.3
    discoverability: 68.5
    governance: 14.4
    operational_transparency: 52.6
  previous_composite: 50.8
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-pagespeed/refs/heads/main/screenshots/google-pagespeed-2026-06-20T182219.png
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
slug: google-pagespeed
tags:
- Core Web Vitals
- Google
- Lighthouse
- Page Speed
- SEO
- Web Performance
website: https://pagespeed.web.dev/
---
