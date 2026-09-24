---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'The OpenDBM REST API is a self-hosted FastAPI service published inside AiCure''s open-source OpenDBM repository (rest_api/). It exposes the OpenDBM digital-biomarker pipeline over HTTP: an OAuth2 passw'
  name: OpenDBM REST API
  slug: aicure-opendbm-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://aicure.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aicure.github.io/open_dbm/
- group: docs
  title: ''
  type: Documentation
  url: https://aicure.github.io/open_dbm/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://aicure.github.io/open_dbm/api/api-doc
- group: start
  title: ''
  type: GettingStarted
  url: https://aicure.github.io/open_dbm/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://aicure.github.io/open_dbm/extras/issue-reporting
- group: operate
  title: ''
  type: HelpCenter
  url: https://aicure.com/contact
- group: company
  title: ''
  type: Blog
  url: https://aicure.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AiCure
- group: start
  title: ''
  type: Login
  url: https://login.aicure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicure.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicure.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://aicure.com/company/data-privacy-security
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/packages/aicure-packages.yml
  title: ''
  type: Packages
  url: packages/aicure-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/packages/aicure-packages.yml
  title: ''
  type: SDKs
  url: packages/aicure-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/conformance/aicure-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicure-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/lifecycle/aicure-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aicure-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/changelog/aicure-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aicure-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/authentication/aicure-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicure-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/conventions/aicure-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aicure-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/errors/aicure-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicure-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/data-model/aicure-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicure-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/sandbox/aicure-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aicure-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/llms/aicure-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicure-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/plans/aicure-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicure-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/rate-limits/aicure-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aicure-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/security/aicure-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aicure-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aicure/refs/heads/main/security/aicure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicure-domain-security.yml
created: '2026-09-14'
description: 'AiCure (AICure Corporation, New York) builds AI-driven patient engagement and medication-adherence software for clinical trials. Its H.Code platform uses smartphone computer vision to confirm dosing, captures audio and video for digital phenotyping, and feeds predictive analytics, ePRO and site dashboards for sponsors, CROs and investigative sites. The commercial platform is sold to sponsors and CROs and has no public self-serve developer program: the production host api.aicure.com is an AWS API Gateway that answers every anonymous path with 403 Missing Authentication Token, and login.aicure.com is a customer sign-in SPA. AiCure''s one public, machine-readable API surface is OpenDBM, the AGPL-3.0 open-source digital-behavioral-measurement toolkit it publishes at github.com/AiCure/open_dbm, which ships a self-hosted FastAPI REST service (POST /odbm/v1/*) with OAuth2 password-grant JWT auth alongside a Python library on PyPI.'
image: https://aicure.com/img/favicon/apple-touch-icon.png
layout: provider
modified: '2026-09-14'
name: AiCure
nav: Providers
network: true
overview: 'AiCure publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Clinical Trials, Medication Adherence, and Digital Biomarkers.


  AiCure''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 21 more developer resources.'
plans:
- name: Aicure Plans Pricing
  plan_count: 0
  slug: aicure-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aicure Rate Limits
  slug: aicure-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 68.5
    operational_transparency: 18.4
  previous_composite: 37.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicure Authentication
  slug: aicure-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aicure Domain Security
  slug: aicure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aicure Trust Center
  slug: aicure-trust-center
  summary_line: ISO/IEC 27001, SOC 2
slug: aicure
tags:
- Company
- Healthcare
- Clinical Trials
- Medication Adherence
- Digital Biomarkers
- Digital Health
- Artificial Intelligence
- Computer Vision
- Patient Engagement
- Life Sciences
- Open Source
website: https://aicure.com/
---
