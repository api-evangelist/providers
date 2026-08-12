---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Kuaishou Open Platform (快手开放平台) exposes a JSON HTTP API for third-party applications, mini programs and merchant tools built on Kuaishou. Access is granted through a standard OAuth 2.0 authorizati
  name: Kuaishou Open Platform API
  slug: open-platform
- description: Kwai for Business is Kuaishou's international advertising and marketing platform for the Kwai app. Its developer portal at developers.kwai.com documents a marketing API served from the /rest/n/mapi pa
  name: Kwai for Business Marketing API
  slug: kwai-for-business
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kuaishou-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuaishou.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.kuaishou.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kwai
- group: operate
  title: ''
  type: Support
  url: https://www.kuaishou.com/about/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.kuaishou.com/help/feedback
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kuaishou.com/about/policy?tab=protocol
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kuaishou.com/about/policy?tab=privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/kuaishou-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kuaishou-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kuaishou-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kuaishou-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kuaishou-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kuaishou-llms.txt
created: '2026-07-17'
description: 'Kuaishou Technology (快手) is a Beijing-based short-video and live-streaming platform operating Kuaishou in mainland China and Kwai internationally, spanning short video, live commerce, local services and online marketing. Its developer surface is split across two public properties: the Kuaishou Open Platform (open.kuaishou.com), which exposes an OAuth 2.0 authorization-code flow and a JSON Open API for third-party apps, mini programs and merchant integrations; and Kwai for Business (developers.kwai.com), the international marketing/advertising API used by advertisers and measurement partners. Kuaishou also publishes open source under the Kwai GitHub organization. Documentation on both portals is delivered as a JavaScript single-page application and is largely Chinese-language and gated behind developer registration, so this profile records only endpoints and pages verified by live HTTP probe.'
image: https://s2-11031.kwimgs.com/kos/nlav11031/assets/favicon.ico
layout: provider
modified: '2026-07-19'
name: Kuaishou
nav: Providers
network: true
overview: 'Kuaishou publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Social, Video, and Short Video.


  Kuaishou''s developer surface includes support, authentication, and 12 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 18.8
  provenance:
    conformance: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kuaishou/refs/heads/main/screenshots/kuaishou-2026-07-25T224317.png
security:
- kind: authentication
  name: Kuaishou Authentication
  slug: kuaishou-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kuaishou Domain Security
  slug: kuaishou-domain-security
  summary_line: TLSv1.2 · DMARC
slug: kuaishou
tags:
- Company
- Consumer
- Social
- Video
- Short Video
- Live Streaming
- Advertising
- Marketing
- Social Media
- Content
- China
website: https://www.kuaishou.com/
---
