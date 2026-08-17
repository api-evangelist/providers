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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-17'
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
overview: 'Microsoft Forms publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Forms, Microsoft, Microsoft 365, Quizzes, and Surveys.


  Microsoft Forms'' developer surface includes developer portal, authentication, support, and 6 more developer resources.'
plans:
- name: Microsoft Forms Plans Pricing
  plan_count: 3
  slug: microsoft-forms-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Microsoft Forms Rate Limits
  slug: microsoft-forms-rate-limits
score:
  band: emerging
  composite: 22.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 22.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
- Microsoft 365
- Quizzes
- Surveys
website: https://www.microsoft.com/en-us/microsoft-365/online-surveys-polls-quizzes
---
