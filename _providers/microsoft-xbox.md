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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Xbox Live Services provides APIs for achievements, leaderboards, multiplayer, matchmaking, social features, presence, and cloud saves. Game developers can integrate Xbox Live features for player ident
  name: Xbox Live Services API
  slug: xbox-live-api
- description: Azure PlayFab provides a complete backend platform for games with APIs for player authentication, data management, economy and commerce, multiplayer servers, analytics, and LiveOps. It supports real-t
  name: Azure PlayFab API
  slug: playfab-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-xbox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-xbox-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/xbox
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/games/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlayFab
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
description: APIs for Xbox gaming platform including Xbox Live Services and Azure PlayFab backend for games.
finops:
- name: Microsoft Xbox Finops
  service_category: API
  slug: microsoft-xbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-xbox.png
layout: provider
modified: '2026-04-28'
name: Microsoft Xbox
nav: Providers
network: true
overview: 'Microsoft Xbox publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Microsoft, PlayFab, Xbox, and Xbox Live.


  Microsoft Xbox''s developer surface includes developer portal, support, and 6 more developer resources.'
plans:
- name: Microsoft Xbox Plans Pricing
  plan_count: 3
  slug: microsoft-xbox-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Microsoft Xbox Rate Limits
  slug: microsoft-xbox-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: -2.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-xbox/refs/heads/main/screenshots/microsoft-xbox-2026-06-20T185546.png
security:
- kind: domain-security
  name: Microsoft Xbox Domain Security
  slug: microsoft-xbox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Xbox Vulnerability Disclosure
  slug: microsoft-xbox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-xbox
tags:
- Gaming
- Microsoft
- PlayFab
- Xbox
- Xbox Live
website: https://developer.microsoft.com/en-us/games/
---
