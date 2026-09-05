---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    dynamic_client_registration: true
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
  score: 34.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://app.genialis.com
  baseurl_source: declared
  description: The about API from Genialis — 3 operation(s) for about.
  name: Genialis About API
  slug: genialis-about-api
- baseURL: https://app.genialis.com
  baseurl_source: declared
  description: The api API from Genialis — 156 operation(s) for api.
  name: Genialis API
  slug: genialis-api-api
- baseURL: https://app.genialis.com
  baseurl_source: declared
  description: The health_check API from Genialis — 1 operation(s) for health_check.
  name: Genialis Health Check API
  slug: genialis-health-check-api
- baseURL: https://app.genialis.com
  baseurl_source: declared
  description: The rest-auth API from Genialis — 6 operation(s) for rest-auth.
  name: Genialis Rest Auth API
  slug: genialis-rest-auth-api
- baseURL: https://app.genialis.com
  baseurl_source: declared
  description: The saml-auth API from Genialis — 3 operation(s) for saml-auth.
  name: Genialis Saml Auth API
  slug: genialis-saml-auth-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/genialis-base-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.genialis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.genialis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genialis.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.genialis.com/resdk/start.html
- group: docs
  title: ''
  type: APIReference
  url: https://app.genialis.com/api/schema
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genialis
- group: start
  title: ''
  type: SignUp
  url: https://app.genialis.com/
- group: operate
  title: ''
  type: Support
  url: https://genialis.atlassian.net/servicedesk/customer/portal/3
- group: company
  title: ''
  type: Blog
  url: https://www.genialis.com/category/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genialis.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genialis.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.genialis.com/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/genialis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genialis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genialis-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/genialis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/genialis-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/genialis-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/genialis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/genialis-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genialis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/genialis-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/genialis-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/genialis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/genialis-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genialis-llms.txt
created: '2026-08-21'
description: Genialis is a precision oncology company that builds AI models of cancer biology to find and validate biomarkers for drug developers. Its commercial platform, Genialis Expressions, is a multiomics and clinical data infrastructure for RNA-seq and related assays, and its Genialis Supermodel is a foundation model of cancer biology used for response prediction (krasID, adcID, DDR). The Expressions platform exposes a public Django REST Framework API at app.genialis.com covering data objects, samples, collections, processes, annotations, predictions and variants, published as a live OpenAPI 3.0.3 document, and is consumed programmatically through the open-source ReSDK Python client. Genialis also maintains the open-source Resolwe dataflow engine and Resolwe Bioinformatics pipelines that the platform is built on. Founded in Slovenia with offices in Boston, Houston and Ljubljana.
image: https://www.genialis.com/wp-content/uploads/2023/12/Genialis-large-logo.png
layout: provider
modified: '2026-08-21'
name: Genialis
nav: Providers
network: true
overview: 'Genialis publishes 5 APIs on the [APIs.io](https://apis.io/) network, including About API, Health Check API, and 3 more. Tagged areas include Company, Bioinformatics, Precision Medicine, Genomics, and Life Sciences.


  Genialis'' developer surface includes documentation, getting-started guide, API reference, signup flow, support, engineering blog, authentication, and 21 more developer resources.'
plans:
- name: Genialis Plans Pricing
  plan_count: 0
  slug: genialis-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Genialis Rate Limits
  slug: genialis-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 49.5
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 46.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genialis/refs/heads/main/screenshots/genialis-2026-09-02T145552.png
security:
- kind: authentication
  name: Genialis Authentication
  slug: genialis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Genialis Domain Security
  slug: genialis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Genialis Trust Center
  slug: genialis-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: genialis
tags:
- Company
- Bioinformatics
- Precision Medicine
- Genomics
- Life Sciences
- Healthcare
- Machine-Learning
- Artificial Intelligence
- Multiomics
- Oncology
- Data Platform
- Open-Source
website: https://www.genialis.com/
---
