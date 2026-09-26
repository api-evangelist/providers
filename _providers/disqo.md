---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-09-25'
api_count: 4
apis:
- baseURL: https://projects-api.audience.disqo.com
  baseurl_source: declared
  description: Create, list, retrieve, update and delete survey Projects and their Quotas against the DISQO panel, and manage the included-users, excluded-users and excluded-projects lists that drive recontact and w
  name: DISQO Audience Projects API
  slug: disqo-audience-projects-api
- description: Estimate the number of panelists — feasible completes — available for a given set of qualifications, country, device mix, length of interview and incidence rate before a project is created and fielded
  name: DISQO Audience Feasibility API
  slug: disqo-audience-feasibility-api
- description: List, retrieve and create client-specific custom screening questions that can be attached to a project as pre-screening qualifications beyond the standard DISQO panelist attribute library.
  name: DISQO Audience Custom Questions API
  slug: disqo-audience-custom-questions-api
- description: 'Validate an email address for co-registration flows — checks address format, whether the address already exists in the DISQO system, and optionally runs an Email Oversight verification. Authenticated '
  name: DISQO CoReg API
  slug: disqo-coreg-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.disqo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.disqo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.disqo.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.disqo.com/docs/audience-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.disqo.com/docs/audience-api/
- group: company
  title: ''
  type: Blog
  url: https://developer.disqo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.disqo.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.disqo.com/legal/api-managed-services-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.disqo.com/privacy-policy/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/postman/disqo-audience-api-postman.json
  title: ''
  type: Postman
  url: postman/disqo-audience-api-postman.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/llms/disqo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/disqo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/authentication/disqo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/disqo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/conventions/disqo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/disqo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/errors/disqo-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/disqo-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/lifecycle/disqo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/disqo-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/changelog/disqo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/disqo-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/sandbox/disqo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/disqo-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/data-model/disqo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/disqo-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/conformance/disqo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/disqo-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/packages/disqo-packages.yml
  title: ''
  type: Packages
  url: packages/disqo-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/security/disqo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disqo-domain-security.yml
created: '2026-08-04'
description: DISQO is a Glendale, California consumer-insights and advertising-measurement company that operates a first-party, fully opted-in consumer panel and sells programmatic access to it. Its public API surface is the DISQO Audience API — a RESTful, HTTP Basic authenticated set of services for checking sample feasibility, creating and managing survey projects and quotas, attaching custom screening questions, and managing included/excluded panelist and project lists — plus a redirect/callback tracking contract that returns panelists to DISQO with an HMAC-SHA256 signed status. A separate CoReg API validates email addresses for co-registration flows. DISQO also sells Brand Lift, Outcomes Lift, Research Management and cross-platform ad measurement products on top of the same panel.
image: https://www.disqo.com/wp-content/uploads/2025/11/HomePage_Header.png
layout: provider
modified: '2026-08-04'
name: DISQO
nav: Providers
network: true
overview: 'DISQO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audience Projects API, and 3 more. Tagged areas include Company, Audiences, Market Research, Surveys, and Consumer Insights.


  DISQO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 14 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 68.6
    discoverability: 80.0
    operational_transparency: 15.8
  previous_composite: 28.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/disqo/refs/heads/main/screenshots/disqo-2026-08-07T164402.png
security:
- kind: authentication
  name: Disqo Authentication
  slug: disqo-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Disqo Domain Security
  slug: disqo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: disqo
tags:
- Company
- Audiences
- Market Research
- Surveys
- Consumer Insights
- Advertising Measurement
- Panel
- Brand Lift
- Data
- Analytics
website: https://www.disqo.com/
---
