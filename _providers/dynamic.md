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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Dynamic's REST API for wallet infrastructure — admin and environment management endpoints plus SDK-facing endpoints for auth, passkeys, embedded wallets, MPC/WaaS, users, sessions, MFA, gates, and web
  name: Dynamic REST API
  slug: dynamic-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Dynamic Webhooks
  slug: dynamic-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dynamic.xyz/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.dynamic.xyz/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.dynamic.xyz/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dynamic.xyz/docs/overview/introduction/welcome
- group: company
  title: ''
  type: Blog
  url: https://www.dynamic.xyz/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.dynamic.xyz/
- group: start
  title: ''
  type: Login
  url: https://app.dynamic.xyz/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dynamic.xyz/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynamic.xyz/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamic.xyz/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynamic-labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dynamic.xyz/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dynamic-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dynamic-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/dynamic-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/dynamic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dynamic-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dynamic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dynamic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dynamic-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dynamic-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dynamic-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/dynamic-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dynamic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dynamic.xyz/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/dynamic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dynamic.xyz/submit-bug-bounty-report
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dynamic-domain-security.yml
created: '2026-07-17'
description: Dynamic is a wallet infrastructure platform for fintech, crypto, and stablecoin applications, letting companies embed non-custodial wallets, connect 800+ external wallets, run distributed (TSS-MPC) key management, and build onchain products such as crypto payments, trading, yield, and global money movement without in-house crypto expertise. Developers integrate through a full stack that ranges from low-level REST APIs to prebuilt UI SDKs for React, JavaScript, React Native, Flutter, Swift, Kotlin, Unity, and server-side Node, Python, Rust, and Java, plus a `dyn` CLI, an official documentation MCP server, and webhooks for environment events. The REST API is organized into admin and SDK endpoints for environments, users, wallets, sessions, MFA, gates, and Wallet-as-a-Service (WaaS). Dynamic was backed by a16z and was acquired by Fireblocks in October 2025.
image: https://cdn.prod.website-files.com/626692727bba3f384e008e8a/67efcc8f11a9608cf3084bc3_328d77e78384deddd386bc6036ac7cc3_shared-img-home.jpg
layout: provider
mcp_servers:
- description: ''
  name: dynamic-mcp.yml
  slug: dynamic-mcpyml
modified: '2026-07-18'
name: Dynamic
nav: Providers
network: true
overview: 'Dynamic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wallet Infrastructure, Web3, Crypto, and Authentication.


  The Dynamic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dynamic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, changelog, and 22 more developer resources.'
random_paper: 21
score:
  band: strong
  composite: 56.3
  delta: 8.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 69.6
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 48.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamic/refs/heads/main/screenshots/dynamic-2026-07-25T212559.png
security:
- kind: authentication
  name: Dynamic Authentication
  slug: dynamic-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dynamic Domain Security
  slug: dynamic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dynamic Vulnerability Disclosure
  slug: dynamic-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Dynamic Trust Center
  slug: dynamic-trust-center
  summary_line: SOC 2
slug: dynamic
tags:
- Company
- Wallet Infrastructure
- Web3
- Crypto
- Authentication
- Embedded Wallets
- Stablecoins
- Key Management
- MPC
- Developer Tools
- Fintech
- Blockchain
website: https://www.dynamic.xyz/docs
---
