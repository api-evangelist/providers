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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.3
  scored_at: '2026-09-12'
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
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.apple.com/
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
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apple-safari-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/apple-safari-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/apple-safari-security.txt
- group: auth
  title: ''
  type: Security
  url: security/apple-safari-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apple-safari-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/apple-safari-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apple-safari-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/apple-safari-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apple-safari-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/apple-safari-cli.yml
- group: design
  title: ''
  type: Components
  url: components/apple-safari-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apple-safari-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apple-safari-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apple-safari-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apple-safari-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.apple.com/system-status/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apple-safari-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apple-safari-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apple-safari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apple-safari-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apple-safari-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apple.com/documentation/safariservices
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WebKit
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.apple.com/programs/
- group: start
  title: ''
  type: SignUp
  url: https://developer.apple.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.apple.com/support/terms/apple-developer-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/legal/privacy/
created: '2024'
description: Apple's web browser available across macOS, iOS, and iPadOS, providing a fast, efficient, and private browsing experience with features like Intelligent Tracking Prevention, iCloud syncing, and web standards support.
finops:
- name: Apple Safari Finops
  service_category: API
  slug: apple-safari-finops
image: https://www.apple.com/v/safari/q/images/meta/safari__bo5fx1ipmoqq_og.png
layout: provider
mcp_servers:
- description: Apple's first-party Model Context Protocol server for web developers, introduced by WebKit in Safari 27 beta and Safari Technology Preview 247. It connects an MCP-compatible agent to a live Safari bro
  name: Safari MCP server
  slug: safari-mcp-server
modified: '2026-09-07'
name: Apple Safari
nav: Providers
network: true
overview: 'Apple Safari publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apple, Browser, Privacy, Web Browser, and Webkit.


  Apple Safari''s developer surface includes release notes, engineering blog, documentation, YouTube channel, support, CLI, authentication, and 31 more developer resources.'
plans:
- name: Apple Safari Plans Pricing
  plan_count: 3
  slug: apple-safari-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Apple Safari Rate Limits
  slug: apple-safari-rate-limits
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 88.9
    operational_transparency: 76.3
  previous_composite: 57.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/apple-safari/refs/heads/main/screenshots/apple-safari-2026-06-20T172321.png
security:
- kind: authentication
  name: Apple Safari Authentication
  slug: apple-safari-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Apple Safari Domain Security
  slug: apple-safari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Safari Vulnerability Disclosure
  slug: apple-safari-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Apple Safari Trust Center
  slug: apple-safari-trust-center
  summary_line: Common Criteria (CC), Cryptographic module validation (CMVP / FIPS), SOC 3
slug: apple-safari
tags:
- Apple
- Browser
- Privacy
- Web Browser
- Webkit
website: https://www.apple.com/
---
