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
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Microsoft Sway is a presentation and storytelling application that enables creating interactive, web-based content. While Sway has limited direct API access, it integrates with Microsoft 365 for embed
  name: Microsoft Sway API
  slug: sway-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-sway-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://sway.cloud.microsoft/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/sway/flow
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
description: Microsoft Sway is a presentation and storytelling application that enables creating interactive, web-based content. It integrates with Microsoft 365 for sharing and embedding interactive presentations, newsletters, and reports across an organization.
finops:
- name: Microsoft Sway Finops
  service_category: API
  slug: microsoft-sway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-sway.png
layout: provider
modified: '2026-04-28'
name: Microsoft Sway
nav: Providers
network: true
overview: 'Microsoft Sway publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Content Creation, Microsoft, Microsoft-365, Presentations, and Storytelling.


  Microsoft Sway''s developer surface includes developer portal, support, and 5 more developer resources.'
plans:
- name: Microsoft Sway Plans Pricing
  plan_count: 3
  slug: microsoft-sway-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Microsoft Sway Rate Limits
  slug: microsoft-sway-rate-limits
score:
  band: emerging
  composite: 19.4
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
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-sway/refs/heads/main/screenshots/microsoft-sway-2026-06-20T185537.png
security:
- kind: domain-security
  name: Microsoft Sway Domain Security
  slug: microsoft-sway-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: microsoft-sway
tags:
- Content Creation
- Microsoft
- Microsoft-365
- Presentations
- Storytelling
website: https://www.microsoft.com/en-us/microsoft-365/sway/flow
---
