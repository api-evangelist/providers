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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Clarity Agentic Access
  operation_count: 1
  slug: microsoft-clarity-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Microsoft Clarity provides heatmaps, session recordings, and behavioral analytics with API access for custom integrations.
  name: Microsoft Clarity API
  slug: api
- description: Project live insights data export
  name: Microsoft Clarity DataExport API
  slug: microsoft-clarity-dataexport-api
artifact_total: 10
collections:
- collection_type: open
  name: Microsoft Clarity Data Export API
  slug: open-microsoft-clarity
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-clarity-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-clarity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-clarity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-clarity-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-clarity
- group: start
  title: ''
  type: Portal
  url: https://clarity.microsoft.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup
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
- group: company
  title: ''
  type: Blog
  url: https://clarity.microsoft.com/blog/feed
created: '2026-03-13'
description: Microsoft Clarity is a free web analytics tool providing heatmaps, session recordings, and behavioral insights through an API for custom integrations.
finops:
- name: Microsoft Clarity Finops
  service_category: API
  slug: microsoft-clarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-clarity.png
layout: provider
modified: '2026-04-28'
name: Microsoft Clarity
nav: Providers
network: true
overview: 'Microsoft Clarity publishes 1 API on the [APIs.io](https://apis.io/) network: DataExport API. Tagged areas include Analytics, Heatmaps, Session Recording, and Web Analytics.


  Microsoft Clarity''s developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Clarity Plans Pricing
  plan_count: 3
  slug: microsoft-clarity-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Microsoft Clarity Rate Limits
  slug: microsoft-clarity-rate-limits
score:
  band: developing
  composite: 44.8
  delta: -2.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 37.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-clarity/refs/heads/main/screenshots/microsoft-clarity-2026-06-20T185449.png
security:
- kind: authentication
  name: Microsoft Clarity Authentication
  slug: microsoft-clarity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Microsoft Clarity Domain Security
  slug: microsoft-clarity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Clarity Vulnerability Disclosure
  slug: microsoft-clarity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-clarity
tags:
- Analytics
- Heatmaps
- Session Recording
- Web Analytics
website: https://clarity.microsoft.com/
---
