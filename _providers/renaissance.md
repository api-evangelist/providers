---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.proxile.renaissance.com
  baseurl_source: declared
  description: Lexile measure lookup by ISBN-13, returning the stored Lexile book record. OpenAPI 3.0.1 published at the API host root; the API gateway validates a JWT issued by Renaissance auth (client credentials)
  name: Lexile API
  slug: lexile-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Classes API from Renaissance — 1 operation(s) for classes.
  name: Renaissance Classes API
  slug: renaissance-classes-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Events API from Renaissance — 1 operation(s) for events.
  name: Renaissance Events API
  slug: renaissance-events-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Health API from Renaissance — 1 operation(s) for health.
  name: Renaissance Health API
  slug: renaissance-health-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Pathway API from Renaissance — 1 operation(s) for pathway.
  name: Renaissance Pathway API
  slug: renaissance-pathway-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Predictions API from Renaissance — 3 operation(s) for predictions.
  name: Renaissance Predictions API
  slug: renaissance-predictions-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Reading Level API from Renaissance — 1 operation(s) for reading level.
  name: Renaissance Reading Level API
  slug: renaissance-reading-level-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Skills API from Renaissance — 1 operation(s) for skills.
  name: Renaissance Skills API
  slug: renaissance-skills-api
- baseURL: https://proficiency.renaissance.com
  baseurl_source: declared
  description: The Utility API from Renaissance — 2 operation(s) for utility.
  name: Renaissance Utility API
  slug: renaissance-utility-api
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/renaissance/overlays/renaissance-student-proficiency-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/renaissance-student-proficiency-service-overlay.yaml
- group: other
  href: https://artifacts.apis.io/renaissance/overlays/renaissance-student-pathway-event-proxy-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/renaissance-student-pathway-event-proxy-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/renaissance/security/renaissance-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/renaissance-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.renaissance.com/
- group: operate
  title: ''
  type: Support
  url: https://support.renaissance.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.renaissance.com/resources/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.renaissance.com/resources/blog/feed/
- group: start
  title: ''
  type: Login
  url: https://login.renaissance.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.renaissance.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.renaissance.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RenaissancePlace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.renaissance.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.renaissance.com/
- group: auth
  href: https://artifacts.apis.io/renaissance/conformance/renaissance-conformance.yml
  title: ''
  type: Compliance
  url: conformance/renaissance-conformance.yml
- group: design
  href: https://artifacts.apis.io/renaissance/conformance/renaissance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/renaissance-conformance.yml
- group: agent
  href: https://artifacts.apis.io/renaissance/llms/renaissance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/renaissance-llms.txt
- group: agent
  href: https://artifacts.apis.io/renaissance/well-known/renaissance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/renaissance-well-known.yml
- group: auth
  href: https://artifacts.apis.io/renaissance/authentication/renaissance-authentication.yml
  title: ''
  type: Authentication
  url: authentication/renaissance-authentication.yml
- group: auth
  href: https://artifacts.apis.io/renaissance/scopes/renaissance-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/renaissance-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.renaissance.com/.well-known/openid-configuration
- group: design
  href: https://artifacts.apis.io/renaissance/conventions/renaissance-conventions.yml
  title: ''
  type: Conventions
  url: conventions/renaissance-conventions.yml
- group: design
  href: https://artifacts.apis.io/renaissance/lifecycle/renaissance-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/renaissance-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/renaissance/errors/renaissance-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/renaissance-problem-types.yml
- group: design
  href: https://artifacts.apis.io/renaissance/data-model/renaissance-data-model.yml
  title: ''
  type: DataModel
  url: data-model/renaissance-data-model.yml
- group: auth
  href: https://artifacts.apis.io/renaissance/security/renaissance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/renaissance-domain-security.yml
- group: build
  href: https://artifacts.apis.io/renaissance/packages/renaissance-packages.yml
  title: ''
  type: Packages
  url: packages/renaissance-packages.yml
- group: agent
  href: https://artifacts.apis.io/renaissance/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/renaissance/changelog/renaissance-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/renaissance-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.renaissance.com/product-updates/
- group: commercial
  href: https://artifacts.apis.io/renaissance/plans/renaissance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/renaissance-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/renaissance/rate-limits/renaissance-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/renaissance-rate-limits.yml
created: '2026-09-13'
description: 'Renaissance Learning, Inc. is a pre-K–12 education technology company whose assessment, practice and analytics products — Star Assessments, Accelerated Reader, Freckle, myON, Lalilo, Flocabulary, Nearpod, FastBridge, DnA, eduCLIMBER, eSchoolData, SchoolCity and the Renaissance Growth Platform — are used by schools in more than 100 countries. Its machine-readable surface is not a published developer program: district integration is delivered through 1EdTech OneRoster 1.1 rostering (certified across twelve products), LTI 1.3 / LTI Advantage launches (Nearpod, SchoolCity), an Ed-Fi Assessment Outcomes API certification for DnA, and a Renaissance-operated OAuth 2.0 / OpenID Connect authorization server at auth.renaissance.com. Three first-party OpenAPI contracts are served publicly but token-gated on Renaissance-controlled hosts: the Student Proficiency Service, the Student Pathway Event Proxy and the Lexile API.'
finops:
- has_sources: true
  method: derived
  name: Renaissance Finops
  primary_unit: ''
  service_category: ''
  slug: renaissance-finops
  template: true
image: https://www.renaissance.com/wp-content/uploads/2023/04/renaissance-logo-facebook.png
layout: provider
modified: '2026-09-13'
name: Renaissance
nav: Providers
network: true
overview: 'Renaissance publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Lexile API, Classes API, Events API, and 6 more. Tagged areas include Education, EdTech, K-12, Assessment, and Learning Analytics.


  The Renaissance catalog on APIs.io includes 1 Spectral governance ruleset.


  Renaissance''s developer surface includes support, engineering blog, authentication, changelog, and 27 more developer resources.'
plans:
- name: Renaissance Plans Pricing
  plan_count: 0
  slug: renaissance-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Renaissance Rate Limits
  slug: renaissance-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Renaissance API Rules
  rule_count: 49
  severity_counts:
    error: 40
    hint: 0
    info: 6
    warn: 3
  slug: renaissance-rules
scopes:
- name: Renaissance Scopes
  scope_count: 4
  slug: renaissance-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 49.7
    developer_ergonomics: 28.0
    discoverability: 78.6
    operational_transparency: 44.7
  previous_composite: 44.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/renaissance/renaissance-2026-10-11T125131.png
security:
- kind: authentication
  name: Renaissance Authentication
  slug: renaissance-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Renaissance Domain Security
  slug: renaissance-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Renaissance Trust Center
  slug: renaissance-trust-center
  summary_line: SOC 2
skill_count: 2
skills:
- name: renaissance-freckle-event-ingest
  slug: renaissance-freckle-event-ingest
- name: renaissance-student-proficiency-lookup
  slug: renaissance-student-proficiency-lookup
slug: renaissance
tags:
- Education
- EdTech
- K-12
- Assessment
- Learning Analytics
- Student Data
- OneRoster
- LTI
- Ed-Fi
- Rostering
- Interoperability
- Machine Learning
website: https://www.renaissance.com/
---
