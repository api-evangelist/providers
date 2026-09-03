---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
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
  title: ''
  type: Postman
  url: postman/disqo-audience-api-postman.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/disqo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/disqo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/disqo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/disqo-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/disqo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/disqo-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/disqo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/disqo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/disqo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/disqo-packages.yml
- group: auth
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
overview: 'DISQO publishes 1 API on the [APIs.io](https://apis.io/) network: Audience Projects API. Tagged areas include Company, Audience, Market Research, Surveys, and Consumer Insights.


  DISQO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 14 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 28.8
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Audience
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
