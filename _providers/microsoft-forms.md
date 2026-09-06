---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Microsoft Graph Forms API provides programmatic access to Microsoft Forms for creating and managing forms, surveys, and quizzes. Developers can retrieve form definitions, access response data, and
  name: Microsoft Graph Forms API
  slug: graph-forms-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-forms-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs
- group: start
  title: ''
  type: Portal
  url: https://forms.office.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/online-surveys-polls-quizzes
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: Microsoft Forms is a web-based application for creating surveys, quizzes, and polls. It provides API access through Microsoft Graph for managing forms, retrieving responses, and integrating form functionality into custom applications.
finops:
- name: Microsoft Forms Finops
  service_category: API
  slug: microsoft-forms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-forms.png
layout: provider
modified: '2026-04-28'
name: Microsoft Forms
nav: Providers
network: true
overview: 'Microsoft Forms publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forms, Microsoft, Microsoft-365, Quizzes, and Surveys.


  Microsoft Forms'' developer surface includes developer portal, authentication, support, and 6 more developer resources.'
plans:
- name: Microsoft Forms Plans Pricing
  plan_count: 3
  slug: microsoft-forms-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Forms Rate Limits
  slug: microsoft-forms-rate-limits
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-forms/refs/heads/main/screenshots/microsoft-forms-2026-06-20T185503.png
security:
- kind: domain-security
  name: Microsoft Forms Domain Security
  slug: microsoft-forms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: microsoft-forms
tags:
- Forms
- Microsoft
- Microsoft-365
- Quizzes
- Surveys
website: https://www.microsoft.com/en-us/microsoft-365/online-surveys-polls-quizzes
---
