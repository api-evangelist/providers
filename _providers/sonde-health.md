---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Sonde Platform Service API lets partners run Sonde Vocal Biomarker Health Checks from their own mobile, web and embedded applications. Services cover user registration (UserService), signed-URL au
  name: Sonde Platform Service API
  slug: sonde-platform-service-api
- baseURL: https://api.sondeservices.com
  baseurl_source: declared
  description: The Authentication API from Sonde Health — 1 operation(s) for authentication.
  name: Sonde Health Authentication API
  slug: sonde-health-authentication-api
- baseURL: https://api.sondeservices.com
  baseurl_source: declared
  description: The Platform API from Sonde Health — 1 operation(s) for platform.
  name: Sonde Health Platform API
  slug: sonde-health-platform-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.sondehealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sondehealth.com/dev-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://sondehealth.atlassian.net/wiki/spaces/SA/overview
- group: docs
  title: ''
  type: APIReference
  url: https://sondehealth.atlassian.net/wiki/spaces/SA/pages/2689105939/REST+API+Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://sondehealth.atlassian.net/wiki/spaces/SA/pages/2800156688/Getting+Started%3A+Sonde+Cloud+API
- group: operate
  title: ''
  type: Support
  url: https://www.sondehealth.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.sondehealth.com/news-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sondehealth-samples
- group: start
  title: ''
  type: Login
  url: https://us.sondeservices.com/
- group: start
  title: ''
  type: Portal
  url: https://us.sondeservices.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sondehealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sondehealth.com/privacy
- group: docs
  href: https://artifacts.apis.io/sonde-health/openapi/_original/sonde-health-screening-api-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/sonde-health-screening-api-openapi.yaml
- group: other
  href: https://artifacts.apis.io/sonde-health/overlays/sonde-health-screening-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sonde-health-screening-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/sonde-health/authentication/sonde-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sonde-health-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sonde-health/scopes/sonde-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sonde-health-scopes.yml
- group: design
  href: https://artifacts.apis.io/sonde-health/errors/sonde-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sonde-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sonde-health/conventions/sonde-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sonde-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/sonde-health/lifecycle/sonde-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sonde-health-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sonde-health/lifecycle/sonde-health-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sonde-health-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sonde-health/changelog/sonde-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sonde-health-changelog.yml
- group: build
  href: https://artifacts.apis.io/sonde-health/packages/sonde-health-packages.yml
  title: ''
  type: Packages
  url: packages/sonde-health-packages.yml
- group: build
  href: https://artifacts.apis.io/sonde-health/packages/sonde-health-packages.yml
  title: ''
  type: SDKs
  url: packages/sonde-health-packages.yml
- group: start
  href: https://artifacts.apis.io/sonde-health/sandbox/sonde-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sonde-health-sandbox.yml
- group: design
  href: https://artifacts.apis.io/sonde-health/conformance/sonde-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sonde-health-conformance.yml
- group: auth
  href: https://artifacts.apis.io/sonde-health/conformance/sonde-health-conformance.yml
  title: ''
  type: Compliance
  url: conformance/sonde-health-conformance.yml
- group: design
  href: https://artifacts.apis.io/sonde-health/data-model/sonde-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sonde-health-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sonde-health/security/sonde-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonde-health-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sonde-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sonde-health/llms/sonde-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sonde-health-llms.txt
- group: commercial
  href: https://artifacts.apis.io/sonde-health/plans/sonde-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sonde-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sonde-health/rate-limits/sonde-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sonde-health-rate-limits.yml
created: '2026-08-28'
description: 'Sonde Health is a Boston-based digital health company that turns short voice samples into vocal biomarkers — objective, AI-derived measures of respiratory, mental and cognitive fitness. Founded out of PureTech Health, Sonde has banked over 1,000,000 voice samples from more than 80,000 subjects to train its Health Check models. Partners integrate through the Sonde Platform Service API (a HIPAA-aligned REST API on api.sondeservices.com secured with OAuth 2.0 client-credentials and fine-grained sonde-platform/* scopes), through on-device Passive, Cued and Edge SDKs for Android and iOS, and through OEM integrations such as Qualcomm''s Snapdragon Sound platform. The cloud flow is upload-and-score: register a subject, request a signed storage URL, upload a WAV sample, then create an inference job and poll for Respiratory Symptoms Risk, Mental Fitness voice-feature scores, M3/PHQ-2 questionnaire scores, or an English transcription.'
finops:
- has_sources: true
  method: derived
  name: Sonde Health Finops
  primary_unit: ''
  service_category: ''
  slug: sonde-health-finops
  template: true
image: http://static1.squarespace.com/static/5daafd349a9f9f7b4aa8680f/t/5df3f83d91da223324d2f090/1587518087705/Sonde_Logo+horizontal+PMS3025.png?format=1500w
layout: provider
modified: '2026-09-16'
name: Sonde Health
nav: Providers
network: true
overview: 'Sonde Health publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Platform API, and 1 more. Tagged areas include Company, Health, Healthcare, Digital Health, and Vocal Biomarkers.


  The Sonde Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Sonde Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, developer portal, authentication, and 25 more developer resources.'
plans:
- name: Sonde Health Plans Pricing
  plan_count: 0
  slug: sonde-health-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Sonde Health Rate Limits
  slug: sonde-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Sonde Health API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: sonde-health-rules
scopes:
- name: Sonde Health Scopes
  scope_count: 17
  slug: sonde-health-scopes
  summary_line: 17 scopes · clientCredentials
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 41.6
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 39.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sonde-health/sonde-health-2026-09-02T160216.png
security:
- kind: authentication
  name: Sonde Health Authentication
  slug: sonde-health-authentication
  summary_line: oauth2/apiKey · 1 scheme
- kind: domain-security
  name: Sonde Health Domain Security
  slug: sonde-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: sonde-health-mental-fitness-voice-features
  slug: sonde-health-mental-fitness-voice-features
- name: sonde-health-respiratory-symptoms-risk
  slug: sonde-health-respiratory-symptoms-risk
- name: sonde-health-screening-results-report
  slug: sonde-health-screening-results-report
slug: sonde-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Vocal Biomarkers
- Voice
- Audio
- Machine Learning
- Artificial Intelligence
- Mental Health
- Respiratory
- Remote Patient Monitoring
- Wellness
- HIPAA
website: https://www.sondehealth.com/
---
