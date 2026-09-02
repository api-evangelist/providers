---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Sonde Platform Service API lets partners run Sonde Vocal Biomarker Health Checks from their own mobile, web and embedded applications. Services cover user registration (UserService), signed-URL au
  name: Sonde Platform Service API
  slug: sonde-platform-service-api
- description: 'The Sonde Screening API (Sonde Product Partner API) exposes partner screening-session outcomes: an OAuth 2.0 client-credentials token endpoint and a paged, filterable screening-results report listing '
  name: Sonde Screening API
  slug: sonde-screening-api
artifact_total: 7
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
  title: ''
  type: OpenAPI
  url: openapi/sonde-health-screening-api-openapi.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sonde-health-screening-api-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonde-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sonde-health-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sonde-health-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sonde-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sonde-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sonde-health-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sonde-health-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sonde-health-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sonde-health-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sonde-health-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sonde-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sonde-health-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sonde-health-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonde-health-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonde-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/sonde-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sonde-health-rate-limits.yml
created: '2026-08-28'
description: 'Sonde Health is a Boston-based digital health company that turns short voice samples into vocal biomarkers — objective, AI-derived measures of respiratory, mental and cognitive fitness. Founded out of PureTech Health, Sonde has banked over 1,000,000 voice samples from more than 80,000 subjects to train its Health Check models. Partners integrate through the Sonde Platform Service API (a HIPAA-aligned REST API on api.sondeservices.com secured with OAuth 2.0 client-credentials and fine-grained sonde-platform/* scopes), through on-device Passive, Cued and Edge SDKs for Android and iOS, and through OEM integrations such as Qualcomm''s Snapdragon Sound platform. The cloud flow is upload-and-score: register a subject, request a signed storage URL, upload a WAV sample, then create an inference job and poll for Respiratory Symptoms Risk, Mental Fitness voice-feature scores, M3/PHQ-2 questionnaire scores, or an English transcription.'
image: http://static1.squarespace.com/static/5daafd349a9f9f7b4aa8680f/t/5df3f83d91da223324d2f090/1587518087705/Sonde_Logo+horizontal+PMS3025.png?format=1500w
layout: provider
modified: '2026-08-28'
name: Sonde Health
nav: Providers
network: true
overview: 'Sonde Health publishes 1 API on the [APIs.io](https://apis.io/) network: Sonde Screening API. Tagged areas include Company, Health, Healthcare, Digital Health, and Vocal Biomarkers.


  Sonde Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, developer portal, authentication, and 25 more developer resources.'
plans:
- name: Sonde Health Plans Pricing
  plan_count: 0
  slug: sonde-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Sonde Health Rate Limits
  slug: sonde-health-rate-limits
scopes:
- name: Sonde Health Scopes
  scope_count: 0
  slug: sonde-health-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 38.8
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 51.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Sonde Health Authentication
  slug: sonde-health-authentication
  summary_line: oauth2/apiKey · 1 scheme
- kind: domain-security
  name: Sonde Health Domain Security
  slug: sonde-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonde-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Vocal Biomarkers
- Voice
- Audio
- Machine-Learning
- Artificial Intelligence
- Mental Health
- Respiratory
- Remote Patient Monitoring
- Wellness
- HIPAA
website: https://www.sondehealth.com/
---
