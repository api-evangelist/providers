---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://radware.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.radware.com/products/alteon/
- group: docs
  title: ''
  type: Documentation
  url: https://support.radware.com/app/answers/answer_view/a_id/16280/~/alteon-rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://portals.radware.com/ProductDocumentation/
- group: operate
  title: ''
  type: Support
  url: https://support.radware.com/
- group: company
  title: ''
  type: Blog
  url: https://www.radware.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Radware
- group: auth
  title: ''
  type: Authentication
  url: authentication/alteon-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/alteon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alteon-packages.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.radware.com/newsroom/certifications/
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/radware
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alteon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alteon-domain-security.yml
created: '2026-07-17'
description: Alteon is Radware's application delivery controller (ADC) and advanced load balancer product line, providing Layer 4-7 load balancing, SSL/TLS offloading, application acceleration, global server load balancing, and integrated application security across on-premises, virtual, and public-cloud environments. Originally Alteon WebSystems (a Matrix Partners-backed company that IPO'd in 1999 and was later acquired by Nortel), the Alteon product line is now developed and supported by Radware. Alteon exposes a device-embedded REST API (accessed at https://<device>/restdoc/, HTTP Basic auth, available from Alteon 34.0.4 / 33.5.8 / 33.0.12 and above) plus first-party automation clients including a Python SDK, a certified Terraform provider, and Ansible modules.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alteon.png
layout: provider
modified: '2026-07-17'
name: Alteon
nav: Providers
network: true
overview: 'Alteon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Application Delivery, Load Balancing, and Application Delivery Controller.


  Alteon''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 18.2
  delta: -1.7
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alteon/refs/heads/main/screenshots/alteon-2026-07-25T195817.png
security:
- kind: authentication
  name: Alteon Authentication
  slug: alteon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alteon Domain Security
  slug: alteon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Alteon Vulnerability Disclosure
  slug: alteon-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: alteon
tags:
- Company
- Infrastructure
- Application Delivery
- Load Balancing
- Application Delivery Controller
- Application Security
- Networking
- Radware
website: https://radware.com
---
