---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 36
  human_in_the_loop: 2
  name: Hmcts Agentic Access
  operation_count: 78
  slug: hmcts-agentic-access
  summary_line: 78 operations · 36 acting · 2 human-in-the-loop
api_count: 10
apis:
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Administrative operations such as jobs can be run from this set of endpoints.
  name: HM Courts & Tribunals Service Admin API
  slug: hmcts-admin-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: 'Application Codes are reference data, not managed in App Reg. They are required to provide a set repeatable data that can be used by Application List Entries, such as the title, wording or whether an '
  name: HM Courts & Tribunals Service Application Codes API
  slug: hmcts-application-codes-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: An Application List Entry records all details of an individual Application. This will always belong to an Application List.
  name: HM Courts & Tribunals Service Application List Entries API
  slug: hmcts-application-list-entries-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: An Application List Entry Result records the result of an individual Application. Each Application can have multiple child Results and Results cannot exist without a parent Application.
  name: HM Courts & Tribunals Service Application List Entry Results API
  slug: hmcts-application-list-entry-results-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: An Application List records the date, time and location at which one or more Applications is to be considered by a magistrate or delegated authority.
  name: HM Courts & Tribunals Service Application Lists API
  slug: hmcts-application-lists-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Caseworkers API from HM Courts & Tribunals Service — 5 operation(s) for caseworkers.
  name: HM Courts & Tribunals Service Caseworkers API
  slug: hmcts-caseworkers-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Court Locations are reference data, not managed in App Reg. They are a consolidation of both crown and magistrates courts where an application will be heard and resulted.
  name: HM Courts & Tribunals Service Court Locations API
  slug: hmcts-court-locations-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Criminal Justice Areas are reference data, not managed in App Reg. They are officially recognized justice regions and used to classify records by jurisdiction.
  name: HM Courts & Tribunals Service Criminal Justice Areas API
  slug: hmcts-criminal-justice-areas-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Data API from HM Courts & Tribunals Service — 2 operation(s) for data.
  name: HM Courts & Tribunals Service Data API
  slug: hmcts-data-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Display API from HM Courts & Tribunals Service — 4 operation(s) for display.
  name: HM Courts & Tribunals Service Display API
  slug: hmcts-display-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Internal API from HM Courts & Tribunals Service — 1 operation(s) for internal.
  name: HM Courts & Tribunals Service Internal API
  slug: hmcts-internal-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Background job operations for asynchronous tasks (polling status across all job types).
  name: HM Courts & Tribunals Service Jobs API
  slug: hmcts-jobs-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Notification API from HM Courts & Tribunals Service — 1 operation(s) for notification.
  name: HM Courts & Tribunals Service Notification API
  slug: hmcts-notification-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Endpoints to generate and retrieve CSV reports asynchronously.
  name: HM Courts & Tribunals Service Reports API
  slug: hmcts-reports-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Result codes are reference data, not managed in App Reg. They are required to provide a set of ways an Application List Entry can be resulted. e.g. Approved/Denied.
  name: HM Courts & Tribunals Service Result Codes API
  slug: hmcts-result-codes-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The root API from HM Courts & Tribunals Service — 1 operation(s) for root.
  name: HM Courts & Tribunals Service Root API
  slug: hmcts-root-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: Standard Applicants are reference data, not managed in App Reg. Only code, name and usage dates are exposed by reference-data endpoints and exports. Personal and contact details are excluded, includin
  name: HM Courts & Tribunals Service Standard Applicants API
  slug: hmcts-standard-applicants-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The Subscription API from HM Courts & Tribunals Service — 4 operation(s) for subscription.
  name: HM Courts & Tribunals Service Subscription API
  slug: hmcts-subscription-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The validation API from HM Courts & Tribunals Service — 1 operation(s) for validation.
  name: HM Courts & Tribunals Service Validation API
  slug: hmcts-validation-api
- baseURL: https://api-cp-crime-hearing-results-document-subscription.net/{version}
  baseurl_source: declared
  description: The validation-rules API from HM Courts & Tribunals Service — 2 operation(s) for validation-rules.
  name: HM Courts & Tribunals Service Validation Rules API
  slug: hmcts-validation-rules-api
artifact_total: 47
asyncapis:
- description: ''
  name: Hmcts Webhooks
  slug: hmcts-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/agentic-access/hmcts-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hmcts-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/rules/hmcts-rules.yml
  title: ''
  type: Spectral
  url: rules/hmcts-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/rules/hmcts-api-cp-crime-hearing-results-validator-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hmcts-api-cp-crime-hearing-results-validator-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/rules/hmcts-api-cp-crime-hearing-results-document-subscription-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hmcts-api-cp-crime-hearing-results-document-subscription-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/json-ld/hmcts-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hmcts-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/vocabulary/hmcts-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hmcts-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/asyncapi/hmcts-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hmcts-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/data-model/hmcts-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hmcts-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/components/hmcts-components.yml
  title: ''
  type: Components
  url: components/hmcts-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/conventions/hmcts-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hmcts-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gov.uk/help/report-vulnerability
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/lifecycle/hmcts-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hmcts-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/errors/hmcts-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hmcts-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/conformance/hmcts-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hmcts-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/overlays/hmcts-applications-register-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hmcts-applications-register-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/well-known/hmcts-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hmcts-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/well-known/hmcts-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hmcts-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/well-known/hmcts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hmcts-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/hosts/hmcts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hmcts-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/vendors/hmcts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hmcts-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/packages/hmcts-packages.yml
  title: ''
  type: SDKs
  url: packages/hmcts-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/packages/hmcts-packages.yml
  title: ''
  type: Packages
  url: packages/hmcts-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.gov.uk/government/publications/register-a-food-business-privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.gov.uk/government/news/we-need-your-help
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/authentication/hmcts-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hmcts-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/security/hmcts-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hmcts-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/security/hmcts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hmcts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service
- group: docs
  title: ''
  type: Documentation
  url: https://hmcts.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hmcts
- group: company
  title: ''
  type: Blog
  url: https://insidehmcts.blog.gov.uk/
- group: company
  title: ''
  type: About
  url: https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service/about
- group: operate
  title: ''
  type: Support
  url: https://www.gov.uk/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gov.uk/help/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service/about/personal-information-charter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hmctsgovuk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HMCTSgovuk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC5Altka7XMeXog5ZFzBT9dA
- group: other
  title: ''
  type: x-coverage
  url: ''
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/hmcts/api-cp-crime-hearing-results-document-subscription/blob/9f3ab203a23196e728b1e8ae68092245b98ddb7b/.spectral.yml
created: '2026-10-09'
description: HM Courts & Tribunals Service (HMCTS) is the executive agency of the UK Ministry of Justice responsible for administering the criminal, civil and family courts in England and Wales and the reserved unified tribunals across the United Kingdom. Its engineering teams publish open source code on GitHub (github.com/hmcts) and the "HMCTS way" engineering standards at hmcts.github.io, including Spectral API linting rulesets used in its API repositories.
image: https://avatars.githubusercontent.com/u/22817111?v=4
json_schemas:
- name: application-code-get-detail-dto
  property_count: 14
  slug: hmcts-application-code-get-detail-dto
- name: ClientSubscriptionRequest
  property_count: 2
  slug: hmcts-client-subscription-request
- name: ClientSubscription
  property_count: 6
  slug: hmcts-client-subscription
- name: DraftValidationRequest
  property_count: 7
  slug: hmcts-draft-validation-request
- name: DraftValidationResponse
  property_count: 8
  slug: hmcts-draft-validation-response
- name: entry-create-dto
  property_count: 13
  slug: hmcts-entry-create-dto
- name: entry-get-detail-dto_1
  property_count: 15
  slug: hmcts-entry-get-detail-dto-1
- name: entry-get-detail-dto
  property_count: 15
  slug: hmcts-entry-get-detail-dto
- name: entry-update-dto
  property_count: 12
  slug: hmcts-entry-update-dto
- name: EventPayload
  property_count: 7
  slug: hmcts-event-payload
- name: EventTypeResponse
  property_count: 1
  slug: hmcts-event-type-response
- name: HmacCredentials
  property_count: 2
  slug: hmcts-hmac-credentials
- name: job-acknowledgement
  property_count: 8
  slug: hmcts-job-acknowledgement
- name: RotateSecretRequest
  property_count: 1
  slug: hmcts-rotate-secret-request
- name: RuleDetailResponse
  property_count: 6
  slug: hmcts-rule-detail-response
- name: RuleListResponse
  property_count: 3
  slug: hmcts-rule-list-response
- name: UpdateRuleRequest
  property_count: 2
  slug: hmcts-update-rule-request
jsonld:
- class_count: 103
  name: Hmcts Context
  property_count: 226
  slug: hmcts-context
layout: provider
modified: '2026-10-09'
name: HM Courts & Tribunals Service
nav: Providers
network: true
overview: 'HM Courts & Tribunals Service publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Application Codes API, Application List Entries API, and 17 more. Tagged areas include Company, Government, Courts, Justice, and Public Sector.


  The HM Courts & Tribunals Service catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  HM Courts & Tribunals Service''s developer surface includes signup flow, authentication, documentation, engineering blog, support, YouTube channel, and 34 more developer resources.'
plans:
- name: Hmcts Plans Pricing
  plan_count: 0
  slug: hmcts-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Hmcts Rate Limits
  slug: hmcts-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: HM Courts & Tribunals Service — api cp crime hearing results document subscription rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: hmcts-api-cp-crime-hearing-results-document-subscription-spectral-rules
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: HM Courts & Tribunals Service API Rules
  rule_count: 13
  severity_counts:
    error: 5
    hint: 0
    info: 4
    warn: 4
  slug: hmcts-rules
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 71.9
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 30.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/hmcts/refs/heads/main/screenshots/hmcts-2026-10-11T105332.png
security:
- kind: authentication
  name: Hmcts Authentication
  slug: hmcts-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hmcts Domain Security
  slug: hmcts-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Hmcts Vulnerability Disclosure
  slug: hmcts-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hmcts
tags:
- Company
- Government
- Courts
- Justice
- Public Sector
- United Kingdom
website: https://www.gov.uk/government/organisations/hm-courts-and-tribunals-service
---
