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
    auth_clarity: false
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
  score: 3.2
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: JavaScript API for building Word add-ins and interacting with Word document content.
  name: Word JavaScript API
  slug: word-javascript-api
- description: REST API for accessing and manipulating Word documents stored in OneDrive and SharePoint.
  name: Microsoft Graph Word API
  slug: microsoft-graph-word-api
- description: .NET SDK for programmatically creating and manipulating Word documents using Open XML format.
  name: Office Open XML SDK
  slug: office-open-xml-sdk
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ms-word-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ms-word-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/office
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
created: '2024-01-01'
description: APIs for interacting with Microsoft Word documents and functionality.
finops:
- name: Ms Word Finops
  service_category: API
  slug: ms-word-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ms-word.png
layout: provider
modified: '2026-04-28'
name: Microsoft Word API
nav: Providers
network: true
overview: 'Microsoft Word API publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Documents, Office, Productivity, and Word Processing.


  Microsoft Word API''s developer surface includes developer portal, engineering blog, and 4 more developer resources.'
plans:
- name: Ms Word Plans Pricing
  plan_count: 3
  slug: ms-word-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Ms Word Rate Limits
  slug: ms-word-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ms-word/refs/heads/main/screenshots/ms-word-2026-06-20T185847.png
security:
- kind: domain-security
  name: Ms Word Domain Security
  slug: ms-word-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ms Word Vulnerability Disclosure
  slug: ms-word-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ms-word
tags:
- Documents
- Office
- Productivity
- Word Processing
website: https://developer.microsoft.com/office
---
