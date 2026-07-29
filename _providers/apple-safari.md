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
api_count: 9
apis:
- description: API for building Safari Web Extensions that extend and customize the browsing experience.
  name: Safari Extensions API
  slug: safari-extensions-api
- description: API for creating app extensions that add features and functionality to Safari on macOS.
  name: Safari App Extensions API
  slug: safari-app-extensions-api
- description: WebKit APIs for interacting with web content, including JavaScript evaluation and DOM manipulation.
  name: Safari Web Content API
  slug: safari-web-content-api
- description: iOS and macOS API for integrating Safari functionality into apps, including Safari View Controller.
  name: Safari Services API
  slug: safari-services-api
- description: API for sending push notifications to users through Safari on macOS, iOS, and iPadOS using the Push API, Notifications API, and Service Workers.
  name: Safari Web Push API
  slug: safari-web-push-api
- description: API for creating content blockers and declarative content blocking rules in Safari web extensions to filter and block web content.
  name: Safari Content Blocking API
  slug: safari-content-blocking-api
- description: APIs and tools for inspecting, debugging, and optimizing web content in Safari, including Web Inspector and the ability to add custom web development tools.
  name: Safari Developer Tools API
  slug: safari-developer-tools-api
- description: API for authenticating users through web services in Safari using ASWebAuthenticationSession, supporting OAuth, passkeys, and WebAuthn standards.
  name: Safari Authentication Services API
  slug: safari-authentication-services-api
- description: JavaScript APIs for implementing Apple Pay payments in Safari, supporting both the Apple Pay JS API and the Payment Request API.
  name: Apple Pay on the Web API
  slug: apple-pay-on-the-web-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apple-safari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apple-safari-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apple.com/safari/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.apple.com/documentation/safari-release-notes
- group: other
  title: ''
  type: Resources
  url: https://developer.apple.com/safari/resources/
- group: company
  title: ''
  type: Blog
  url: https://webkit.org/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webkit.org/
- group: learn
  title: ''
  type: YouTube
  url: https://developer.apple.com/videos/safari-web/
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/forums/
created: '2024'
description: Apple's web browser available across macOS, iOS, and iPadOS, providing a fast, efficient, and private browsing experience with features like Intelligent Tracking Prevention, iCloud syncing, and web standards support.
finops:
- name: Apple Safari Finops
  service_category: API
  slug: apple-safari-finops
image: https://www.apple.com/v/safari/q/images/meta/safari__bo5fx1ipmoqq_og.png
layout: provider
modified: '2026-04-19'
name: Apple Safari
nav: Providers
network: true
overview: 'Apple Safari publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apple, Browser, Privacy, Web Browser, and Webkit.


  Apple Safari''s developer surface includes release notes, engineering blog, documentation, YouTube channel, support, and 4 more developer resources.'
plans:
- name: Apple Safari Plans Pricing
  plan_count: 3
  slug: apple-safari-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Apple Safari Rate Limits
  slug: apple-safari-rate-limits
score:
  band: emerging
  composite: 27.0
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 28.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apple-safari/refs/heads/main/screenshots/apple-safari-2026-06-20T172321.png
security:
- kind: domain-security
  name: Apple Safari Domain Security
  slug: apple-safari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Safari Vulnerability Disclosure
  slug: apple-safari-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apple-safari
tags:
- Apple
- Browser
- Privacy
- Web Browser
- Webkit
website: https://developer.apple.com/safari/
---
