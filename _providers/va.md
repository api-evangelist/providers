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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Va Agentic Access
  operation_count: 114
  slug: va-agentic-access
  summary_line: 114 operations · 39 acting
api_count: 25
apis:
- description: Allows Veterans and authorized third parties to access patient health data using the HL7 FHIR R4 standard, including records, medications, conditions, immunizations, and appointments from VA facilitie
  name: Patient Health API (FHIR)
  slug: patient-health-api-fhir
- description: Provides access to health care expense data for VA patients including medical charges, services received, and payments for health-related expenses using the FHIR standard.
  name: Health Care Costs and Coverage API (FHIR)
  slug: health-care-costs-and-coverage-api-fhir
- description: Enables authorized parties to request the status of a Veteran's benefits claim appeal, including the current step in the process, estimated decision dates, and hearing information.
  name: Appeals Status API
  slug: appeals-status-api
- description: Allows accredited representatives and Veterans to interact with VA decision reviews (benefit appeals), including submitting Supplemental Claims, Higher-Level Reviews, and Board Appeals.
  name: Decision Reviews API
  slug: decision-reviews-api
- description: Provides location information and services data for VA facilities including VA Medical Centers, community-based outpatient clinics, Vet Centers, and benefits offices across the United States.
  name: VA Facilities API
  slug: va-facilities-api
- description: Provides information about VA forms including metadata, current versions, and downloadable URLs for official VA forms used in benefits and healthcare applications.
  name: VA Forms API
  slug: va-forms-api
- description: Allows authorized third parties to verify a Veteran's service history, Veteran status, discharge information, and disability rating using OAuth 2.0 authorization from the Veteran.
  name: Veteran Verification API
  slug: veteran-verification-api
- description: Enables accredited VSO representatives to view and update direct deposit information for Veterans receiving VA disability compensation and pension payments.
  name: Direct Deposit Management API
  slug: direct-deposit-management-api
- description: Allows Veterans and authorized third parties to generate official VA letters confirming veteran status, service history, benefit summary, and other information required for housing, employment, and be
  name: VA Letter Generator API
  slug: va-letter-generator-api
- description: Provides reference data used for VA benefits forms and applications, including lists of service branches, discharge types, disabilities, countries, and other standardized VA data sets.
  name: Benefits Reference Data API
  slug: benefits-reference-data-api
- description: The Appealable Issues API from Veterans Affairs — 1 operation(s) for appealable issues.
  name: Veterans Affairs Appealable Issues API
  slug: va-appealable-issues-api
- description: The Appeals Status API from Veterans Affairs — 1 operation(s) for appeals status.
  name: Veterans Affairs Appeals Status API
  slug: va-appeals-status-api
- description: The Contestable Issues API from Veterans Affairs — 1 operation(s) for contestable issues.
  name: Veterans Affairs Contestable Issues API
  slug: va-contestable-issues-api
- description: The Higher-Level Reviews API from Veterans Affairs — 10 operation(s) for higher-level reviews.
  name: Veterans Affairs Higher-Level Reviews API
  slug: va-higher-level-reviews-api
- description: The Labs And Tests API from Veterans Affairs — 1 operation(s) for labs and tests.
  name: Veterans Affairs Labs And Tests API
  slug: va-labs-and-tests-api
- description: The Legacy Appeals API from Veterans Affairs — 2 operation(s) for legacy appeals.
  name: Veterans Affairs Legacy Appeals API
  slug: va-legacy-appeals-api
- description: The Medical Records API from Veterans Affairs — 30 operation(s) for medical records.
  name: Veterans Affairs Medical Records API
  slug: va-medical-records-api
- description: The Messaging API from Veterans Affairs — 20 operation(s) for messaging.
  name: Veterans Affairs Messaging API
  slug: va-messaging-api
- description: The Notice of Disagreements API from Veterans Affairs — 15 operation(s) for notice of disagreements.
  name: Veterans Affairs Notice of Disagreements API
  slug: va-notice-of-disagreements-api
- description: The Other Accredited Representatives API from Veterans Affairs — 1 operation(s) for other accredited representatives.
  name: Veterans Affairs Other Accredited Representatives API
  slug: va-other-accredited-representatives-api
- description: The Prescriptions API from Veterans Affairs — 8 operation(s) for prescriptions.
  name: Veterans Affairs Prescriptions API
  slug: va-prescriptions-api
- description: The Supplemental Claims API from Veterans Affairs — 15 operation(s) for supplemental claims.
  name: Veterans Affairs Supplemental Claims API
  slug: va-supplemental-claims-api
- description: The Tooltips API from Veterans Affairs — 2 operation(s) for tooltips.
  name: Veterans Affairs Tooltips API
  slug: va-tooltips-api
- description: The Unique User Metrics API from Veterans Affairs — 1 operation(s) for unique user metrics.
  name: Veterans Affairs Unique User Metrics API
  slug: va-unique-user-metrics-api
- description: The VSO Accredited Representatives API from Veterans Affairs — 1 operation(s) for vso accredited representatives.
  name: Veterans Affairs VSO Accredited Representatives API
  slug: va-vso-accredited-representatives-api
artifact_total: 39
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/va-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/va-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/va-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/va-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/va-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.va.gov
- group: docs
  title: ''
  type: Documentation
  url: https://developer.va.gov
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/department-of-veterans-affairs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/department-of-veterans-affairs
- group: company
  title: ''
  type: Blog
  url: https://news.va.gov
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.va.gov/onboarding/working-with-lighthouse-apis
- group: operate
  title: ''
  type: StatusPage
  url: https://valighthouse.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/deptvetaffairs
- group: commercial
  title: ''
  type: Plans
  url: plans/va-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/va-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/va-finops.yml
created: '2026-06-13'
description: The US Department of Veterans Affairs (VA) Lighthouse API platform provides a portfolio of public-facing REST APIs enabling third-party developers and partners to access veteran benefits data, health records (FHIR), appeals and decision review status, facilities information, forms, and service history verification. APIs support OAuth 2.0 with OpenID Connect and API key authentication and are available with sandbox and production environments.
examples:
- key_count: 1
  name: Va Appealable Issues Response Example
  slug: va-appealable-issues-response-example
- key_count: 1
  name: Va Appeals Status Response Example
  slug: va-appeals-status-response-example
- key_count: 2
  name: Va Higher Level Review Request Example
  slug: va-higher-level-review-request-example
- key_count: 2
  name: Va Notice Of Disagreement Request Example
  slug: va-notice-of-disagreement-request-example
- key_count: 2
  name: Va Supplemental Claim Request Example
  slug: va-supplemental-claim-request-example
finops:
- name: Va Finops
  service_category: ''
  slug: va-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/va.png
jsonld:
- class_count: 0
  name: Va Context
  property_count: 0
  slug: va-context
layout: provider
modified: '2026-06-13'
name: Veterans Affairs
nav: Providers
network: true
overview: 'Veterans Affairs publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Appealable Issues API, Appeals Status API, Contestable Issues API, and 12 more. Tagged areas include Veterans, Government, Health, Benefits, and FHIR.


  The Veterans Affairs catalog on APIs.io includes 1 JSON-LD context.


  Veterans Affairs'' developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Va Plans Pricing
  plan_count: 2
  slug: va-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Va Rate Limits
  slug: va-rate-limits
scopes:
- name: Va Scopes
  scope_count: 35
  slug: va-scopes
  summary_line: 35 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.0
  delta: -5.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/va/refs/heads/main/screenshots/va-2026-06-20T200739.png
security:
- kind: authentication
  name: Va Authentication
  slug: va-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Va Domain Security
  slug: va-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Va Vulnerability Disclosure
  slug: va-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: va
tags:
- Veterans
- Government
- Health
- Benefits
- FHIR
- Appeals
- Federal
website: https://www.va.gov
---
