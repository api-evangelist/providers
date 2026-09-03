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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Microsoft Graph Loop API enables developers to interact with Microsoft Loop workspaces and components. Loop components are portable, collaborative content blocks that sync across Microsoft 365 app
  name: Microsoft Graph Loop API
  slug: graph-loop-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-loop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-loop-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs
- group: start
  title: ''
  type: Portal
  url: https://loop.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-loop
- group: docs
  title: ''
  type: Documentation
  url: https://support.microsoft.com/en-us/topic/get-started-with-microsoft-loop-9f4d8d4f-dfc6-4518-9ef6-069408c21f0c
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
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
description: Microsoft Loop is a collaborative productivity app that brings together teams, content, and tasks across Microsoft 365 tools. It provides API access through Microsoft Graph for managing Loop workspaces and components.
finops:
- name: Microsoft Loop Finops
  service_category: API
  slug: microsoft-loop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-loop.png
layout: provider
modified: '2026-04-28'
name: Microsoft Loop
nav: Providers
network: true
overview: 'Microsoft Loop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Collaboration, Microsoft, Microsoft-365, and Productivity.


  Microsoft Loop''s developer surface includes developer portal, documentation, authentication, support, and 6 more developer resources.'
plans:
- name: Microsoft Loop Plans Pricing
  plan_count: 3
  slug: microsoft-loop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Microsoft Loop Rate Limits
  slug: microsoft-loop-rate-limits
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-loop/refs/heads/main/screenshots/microsoft-loop-2026-06-20T185507.png
security:
- kind: domain-security
  name: Microsoft Loop Domain Security
  slug: microsoft-loop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Loop Vulnerability Disclosure
  slug: microsoft-loop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-loop
tags:
- Collaboration
- Microsoft
- Microsoft-365
- Productivity
website: https://www.microsoft.com/en-us/microsoft-loop
---
