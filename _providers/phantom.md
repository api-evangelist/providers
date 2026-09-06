---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: Solana wallet provider injected at window.phantom.solana exposing connect, disconnect, signMessage, signIn (Sign-In With Solana), signTransaction, signAllTransactions, and signAndSendTransaction. Impl
  name: Phantom Solana Provider API
  slug: phantom-solana-provider-api
- description: EIP-1193 compliant Ethereum Provider API injected at window.ethereum and window.phantom.ethereum for Ethereum, Polygon, Base, Monad testnet, and HyperEVM. Supports the full Ethereum RPC surface for co
  name: Phantom EVM Provider API
  slug: phantom-evm-provider-api
- description: Bitcoin provider injected at window.phantom.bitcoin exposing requestAccounts (returning BtcAccount objects with address, publicKey, addressType, and purpose), signMessage, and signPSBT for partially s
  name: Phantom Bitcoin Provider API
  slug: phantom-bitcoin-provider-api
- description: Sui provider exposed via window.phantom for browser and mobile platforms, offering connect, signTransactionBlock, and signMessage methods so Sui dApps can integrate Phantom alongside their existing EV
  name: Phantom Sui Provider API
  slug: phantom-sui-provider-api
- description: Universal Link (https://phantom.app/ul/v1/<method>) and custom protocol (phantom://v1/<method>) deeplinks for iOS and Android lets mobile dApps trigger Phantom for connect, disconnect, signMessage, si
  name: Phantom Deeplinks API
  slug: phantom-deeplinks-api
- description: React SDK (@phantom/react-sdk) for integrating Phantom across Solana and EVM chains with embedded wallet support and OAuth social login (Google, Apple) alongside the browser extension path. Provides h
  name: Phantom React SDK
  slug: phantom-react-sdk
- description: React Native SDK that lets iOS and Android apps embed Phantom wallet functionality, including embedded wallets, social login, and connection to the installed Phantom mobile app via deeplinks. Ships wi
  name: Phantom React Native SDK
  slug: phantom-react-native-sdk
- description: Framework-agnostic Browser SDK for integrating Phantom into vanilla JavaScript or TypeScript web apps. Wraps the injected providers and embedded wallet flows so non-React applications can take advanta
  name: Phantom Browser SDK
  slug: phantom-browser-sdk
- description: Model Context Protocol server (@phantom/mcp-server) that exposes 27 tools to AI agents across wallet operations (connection status, addresses, balances, transfers, transaction sending, message and typ
  name: Phantom MCP Server
  slug: phantom-mcp-server
- description: 'Developer portal for registering apps that integrate Phantom. Provides account creation, app creation with App IDs, domain verification, redirect URL configuration, app metadata editing, and contract '
  name: Phantom Portal
  slug: phantom-portal
artifact_total: 12
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/phantom/phantom-connect-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/phantom/phantom-connect-sdk/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/phantom/phantom-connect-sdk/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phantom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phantom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phantom.com
- group: start
  title: ''
  type: Portal
  url: https://docs.phantom.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://phantom.com/learn/developers
- group: start
  title: ''
  type: Signup
  url: https://phantom.com/download
- group: build
  title: ''
  type: GitHub
  url: https://github.com/phantom
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/phantom/phantom-connect-sdk
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/deep-link-demo-app
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/multi-chain-sandbox
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/sandbox
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/eth_sandbox
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/shortcuts-sandbox
- group: build
  title: ''
  type: Examples
  url: https://github.com/phantom/deep-links-movie-tutorial
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/phantom-wagmi-connector
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/sign-in-with-solana
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/bitcoin-wallet-standard
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/sol-wallet-adapter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/blinks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/phantom-agent-kit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/phantom/phantom-skill-generator
- group: build
  title: ''
  type: Tools
  url: https://github.com/phantom/blocklist
- group: build
  title: ''
  type: Tools
  url: https://github.com/phantom/token-list
- group: build
  title: ''
  type: Tools
  url: https://github.com/phantom/shortcuts
- group: build
  title: ''
  type: Tools
  url: https://github.com/phantom/synpress
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/updates
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.phantom.com/updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phantom.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/user-limits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/best-practices/go-live-checklist
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/developer-powertools/testnet-mode
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/developer-powertools/mobile-web-debugging
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/developer-powertools/domain-and-transaction-warnings
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/developer-powertools/lighthouse
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/developer-powertools/ai-tools
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/resources/cursor-prompts
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/resources/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/resources/logos-and-assets
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phantom.com/resources/faq
- group: company
  title: ''
  type: Blog
  url: https://phantom.com/learn/blog
- group: operate
  title: ''
  type: Support
  url: https://help.phantom.com/hc/en-us
- group: other
  title: ''
  type: Feedback
  url: https://feedback.phantom.com/feature-requests
- group: company
  title: ''
  type: Press
  url: https://phantom.com/press-kit
- group: company
  title: ''
  type: Careers
  url: https://phantom.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phantom.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phantom.com/privacy-policy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://phantom.com/security
- group: company
  title: ''
  type: Twitter
  url: https://x.com/phantom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phantom-app
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@phantom
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/phantom_wallet
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/phantom
created: '2026-05-24'
description: Phantom is a self-custodial multi-chain crypto wallet for Solana, Ethereum, Polygon, Base, Bitcoin, Sui, Monad, and HyperEVM, distributed as a mobile app (iOS/Android) and browser extension with more than 20 million users. For developers, Phantom exposes injected Provider APIs per chain on window.phantom (Solana, EVM, Bitcoin, Sui) following the Wallet Standard and EIP-1193, a Universal Link / phantom:// Deeplinks API for mobile dApp integration with encrypted session handshakes, a multi-platform Connect SDK suite (React, React Native, Browser SDKs) with embedded wallet support and OAuth social login (Google, Apple), and a Phantom MCP Server that exposes 27 tools across wallet operations, swaps, portfolio rebalancing, and Hyperliquid perpetuals for AI agents — each agent receives its own wallet via device-code authentication. Apps register through the Phantom Portal to obtain an App ID, configure redirect URLs, verify domains, and opt into auto-confirm contracts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phantom.png
layout: provider
modified: '2026-05-24'
name: Phantom
nav: Providers
network: true
overview: 'Phantom publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Base, Bitcoin, Blockchain, Crypto, and Cryptocurrency.


  Phantom''s developer surface includes developer portal, documentation, signup flow, GitHub presence, code examples, tooling, changelog, and 49 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  open_source:
    applies: true
    score: 25.0
  previous_composite: 23.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phantom/refs/heads/main/screenshots/phantom-2026-06-20T191634.png
security:
- kind: domain-security
  name: Phantom Domain Security
  slug: phantom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Phantom Vulnerability Disclosure
  slug: phantom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: phantom
tags:
- Base
- Bitcoin
- Blockchain
- Crypto
- Cryptocurrency
- Deep Links
- Embedded Wallet
- Ethereum
- EVM
- Monad
- MCP
- Mobile
- Polygon
- Self-Custody
- Solana
- Sui
- Wallets
- Web3
website: https://phantom.com
---
