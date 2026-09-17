---
access_model:
  confidence: medium
  label: Publicly callable with no credential and no signup; commercial terms are set by a EULA rather than by a published plan.
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://fac-api.magvar.com/swagger-ui.html
  - https://www.magvar.com/EULA_SurveyValidationAPI.html
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Helmerich And Payne Agentic Access
  operation_count: 1
  slug: helmerich-and-payne-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- baseURL: https://fac-api.magvar.com
  baseurl_source: declared
  description: Survey Validation and QC
  name: Helmerich And Payne Survey Validation Controller API
  slug: helmerich-and-payne-survey-validation-controller-api
artifact_total: 6
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/overlays/helmerich-and-payne-magvar-survey-validation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/helmerich-and-payne-magvar-survey-validation-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/security/helmerich-and-payne-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/helmerich-and-payne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hpinc.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helmerich-&-payne/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/helmerichpayne
- group: docs
  title: ''
  type: Documentation
  url: https://www.hpinc.com/resources/customer-tools
- group: docs
  title: ''
  type: APIReference
  url: https://fac-api.magvar.com/swagger-ui.html
- group: operate
  title: ''
  type: Support
  url: https://www.magvar.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.hpinc.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hpinc.com/privacy-notices-settings-and-policies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.magvar.com/EULA_SurveyValidationAPI.html
- group: start
  title: ''
  type: Login
  url: https://www.hpinc.com/customer-login
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/llms/helmerich-and-payne-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/helmerich-and-payne-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/authentication/helmerich-and-payne-authentication.yml
  title: ''
  type: Authentication
  url: authentication/helmerich-and-payne-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/conventions/helmerich-and-payne-conventions.yml
  title: ''
  type: Conventions
  url: conventions/helmerich-and-payne-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/conformance/helmerich-and-payne-conformance.yml
  title: ''
  type: Conformance
  url: conformance/helmerich-and-payne-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/lifecycle/helmerich-and-payne-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/helmerich-and-payne-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/sandbox/helmerich-and-payne-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/helmerich-and-payne-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/rate-limits/helmerich-and-payne-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/helmerich-and-payne-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/plans/helmerich-and-payne-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/helmerich-and-payne-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/data-model/helmerich-and-payne-data-model.yml
  title: ''
  type: DataModel
  url: data-model/helmerich-and-payne-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/errors/helmerich-and-payne-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/helmerich-and-payne-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/helmerich-and-payne/refs/heads/main/agentic-access/helmerich-and-payne-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/helmerich-and-payne-agentic-access.yml
created: '2026-04-28'
description: 'Helmerich & Payne, Inc. (H&P, NYSE: HP) is a Tulsa-based drilling solutions company that operates one of the largest land rig fleets in the United States alongside international and offshore operations, and sells rig automation and wellbore-placement technology under the H&P Technologies banner — FlexRig, AutoSlide, StallAssist, FlexB2D and Autodriller Pro. Its public API surface is narrow but real: through Magnetic Variation Services LLC (MagVAR), the directional-drilling survey-correction company H&P acquired in 2018, it publishes the MagVAR Survey Validation API, an anonymous, read-only HTTPS endpoint that runs ISCWSA OWSG Rev-2 dynamic quality control on MWD survey stations and returns per-field Green/Orange/Red verdicts with inclination and azimuth uncertainty. H&P links the API from its own customer-tools page and documents it with a Swagger 2.0 contract served at the API host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helmerich-and-payne.png
layout: provider
modified: '2026-09-13'
name: Helmerich And Payne
nav: Providers
network: true
overview: 'Helmerich And Payne publishes 1 API on the [APIs.io](https://apis.io/) network: Survey Validation Controller API. Tagged areas include Oil and Gas, Drilling, Energy, Wellbore Placement, and Directional Drilling.


  Helmerich And Payne''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Helmerich And Payne Plans Pricing
  plan_count: 0
  slug: helmerich-and-payne-plans-pricing
press:
- date: '2026-05-25'
  title: tm261920-1_nonfiling - none - 21.9154899s
  url: https://www.sec.gov/Archives/edgar/data/46765/000110465926005786/tm261920-1_def14a.htm
- date: '2026-05-25'
  title: Helmerich & Payne, Inc. (HP) Q2 2026 Earnings Call ...
  url: https://seekingalpha.com/article/4901915-helmerich-and-payne-inc-hp-q2-2026-earnings-call-transcript
- date: '2026-05-25'
  title: Helmerich & Payne Inc. (HP) reports earnings - Quartz
  url: https://qz.com/helmerich-payne-inc-hp-reports-earnings-1851756433
- date: '2026-05-25'
  title: Helmerich & Payne Announces Executive Leadership Update
  url: https://norfolkdailynews.com/online_features/press_releases/helmerich-payne-announces-executive-leadership-update/article_820453cc-7ea9-5707-b906-6f9c6f04d5c5.html
- date: '2026-05-25'
  title: Very proud to share this story from our customer Helmerich ...
  url: https://www.linkedin.com/posts/botanosman_very-proud-to-share-this-story-from-our-customer-activity-7391856907306803200-2Kzu
random_paper: 13
rate_limits:
- limit_count: 0
  name: Helmerich And Payne Rate Limits
  slug: helmerich-and-payne-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 44.2
    developer_ergonomics: 44.6
    discoverability: 75.9
    operational_transparency: 2.6
  previous_composite: 35.3
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Helmerich And Payne Authentication
  slug: helmerich-and-payne-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Helmerich And Payne Domain Security
  slug: helmerich-and-payne-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helmerich-and-payne
tags:
- Oil and Gas
- Drilling
- Energy
- Wellbore Placement
- Directional Drilling
- Survey Management
- Geomagnetics
- Rig Automation
- Industrial
website: https://www.hpinc.com
---
