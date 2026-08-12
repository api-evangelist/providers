---
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
api_count: 1
apis:
- description: 'REST/HTTP API for chat and messaging (User and Admin APIs) with JSON payloads. Production base URL is tenant-specific; a public preprod sandbox is available for testing. Auth via username/password to '
  name: MirrorFly Chat Platform API
  slug: mirrorfly-chat-platform-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirrorfly-messages-api-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mirrorfly.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mirrorfly.com/docs/platformapi/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mirrorfly.com/docs/platformapi/userapis/getstarted/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mirrorfly.com/docs/platformapi/adminapis/get-started/
- group: operate
  title: ''
  type: Support
  url: https://console.mirrorfly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mirrorfly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MirrorFly
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mirrorfly.com/pricing.php
- group: start
  title: ''
  type: SignUp
  url: https://www.mirrorfly.com/contact-sales.php
- group: start
  title: ''
  type: Login
  url: https://console.mirrorfly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mirrorfly.com/terms-and-conditions.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mirrorfly.com/privacy-policy.php
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mirrorfly.com/docs/platformapi/api-changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mirrorfly-messages-api-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mirrorfly-messages-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mirrorfly-messages-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mirrorfly-messages-api-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mirrorfly-messages-api-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mirrorfly-messages-api-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/mirrorfly-messages-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mirrorfly-messages-api-packages.yml
- group: design
  title: ''
  type: Components
  url: components/mirrorfly-messages-api-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mirrorfly-messages-api-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mirrorfly.com/chat-security.php
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirrorfly-messages-api-llms.txt
created: '2026-07-29'
description: 'MirrorFly is a self-hosted CPaaS from CONTUS TECH (Chennai, India) that lets teams embed real-time chat, messaging, HD voice, video calling, live streaming, SIP/VoIP and activity feeds into web and mobile applications, deployed either on MirrorFly''s cloud or entirely on the customer''s own infrastructure. The developer surface has two halves: multi-platform client SDKs and prebuilt UIKits for JavaScript, React, React Native, Angular, Vue, Flutter, Kotlin/Android, Swift/iOS and Objective-C; and a server-side REST Chat Platform API split into User APIs and Admin APIs covering users, contacts, presence, one-to-one and group chat, topics, message history, media, moderation (block/unblock), data migration and data export. Authentication mints a one-hour token from a console-issued username and password. MirrorFly also ships conversational-AI tooling — AI voice agents, chatbots, speech-to-text and an AI contact center — on the same platform.'
image: https://www.mirrorfly.com/assets/images/mirrorFly-logo.jpg
layout: provider
modified: '2026-08-09'
name: MirrorFly Messages API
nav: Providers
network: true
overview: 'MirrorFly Messages API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CPaaS, Communications, Chat / Messaging API, Voice API, and Video API.


  MirrorFly Messages API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Mirrorfly Messages Api Authentication
  slug: mirrorfly-messages-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mirrorfly Messages Api Domain Security
  slug: mirrorfly-messages-api-domain-security
  summary_line: TLSv1.2 · DMARC
slug: mirrorfly-messages-api
tags:
- CPaaS
- Communications
- Chat / Messaging API
- Voice API
- Video API
- SIP/VoIP
- Real-time Communication
- SDK
- Self-hosted / On-premise
- AI Agents / Chatbots
- Contact Center
website: https://www.mirrorfly.com/docs/
---
