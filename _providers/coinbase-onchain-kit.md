---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: Core @coinbase/onchainkit npm package providing React components and TypeScript utilities for onchain apps. Includes Wallet, Identity, Transaction, Swap, Checkout, Fund, NFT, Token, and Earn component
  name: OnchainKit React SDK
  slug: onchainkit-sdk
- description: Bootstrap CLI (`npm create onchain`) that scaffolds a new OnchainKit application pre-wired with Wagmi, Viem, TailwindCSS, and Base. Generates starter projects for web apps and Mini Apps.
  name: create-onchain CLI
  slug: create-onchain-cli
- description: Utility that generates the Mini App manifest required to publish a Frames-based Mini App to Farcaster and other Mini App hosts. Validates manifest fields and handles signing.
  name: OnchainKit MiniApp Manifest Generator
  slug: miniapp-manifest
- description: OnchainKit components and connectors that expose Coinbase Smart Wallet — an ERC-4337 smart contract wallet — for sign-in, paymaster-sponsored transactions, passkeys, and session keys.
  name: Coinbase Smart Wallet Integration
  slug: smart-wallet
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinbase-onchain-kit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.base.org/builders/onchainkit
- group: docs
  title: ''
  type: Documentation
  url: https://docs.base.org/onchainkit
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coinbase/onchainkit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinbase
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@coinbase/onchainkit
- group: company
  title: ''
  type: Twitter
  url: https://x.com/OnchainKit
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/buildonbase
- group: commercial
  title: ''
  type: License
  url: https://github.com/coinbase/onchainkit/blob/main/LICENSE.md
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.base.org/llms.txt
created: '2026-05-23'
description: Coinbase OnchainKit is a TypeScript React framework from Coinbase for building onchain applications on Base and other EVM networks. It bundles ready-made React components (wallets, identity, transactions, swap, checkout, fund, NFT), TypeScript utilities, and integrations with Smart Wallet, Base Account, Frames, and Mini Apps. OnchainKit is distributed as the @coinbase/onchainkit npm package along with companion CLIs (create-onchain) and a MiniApp manifest generator. It is built on top of Wagmi, Viem, and TailwindCSS and is the recommended client SDK for the Base ecosystem.
finops:
- name: Coinbase Onchain Kit Finops
  service_category: API
  slug: coinbase-onchain-kit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinbase-onchain-kit.png
layout: provider
modified: '2026-05-23'
name: Coinbase OnchainKit
nav: Providers
network: true
overview: 'Coinbase OnchainKit publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Onchain, Web3, React, SDK, and Base.


  Coinbase OnchainKit''s developer surface includes documentation, GitHub presence, and 8 more developer resources.'
plans:
- name: Coinbase Onchain Kit Plans Pricing
  plan_count: 1
  slug: coinbase-onchain-kit-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 2
  name: Coinbase Onchain Kit Rate Limits
  slug: coinbase-onchain-kit-rate-limits
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinbase-onchain-kit/refs/heads/main/screenshots/coinbase-onchain-kit-2026-06-20T174729.png
security:
- kind: domain-security
  name: Coinbase Onchain Kit Domain Security
  slug: coinbase-onchain-kit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coinbase-onchain-kit
tags:
- Onchain
- Web3
- React
- SDK
- Base
- Smart Wallet
- Frames
- Mini Apps
website: https://www.base.org/builders/onchainkit
---
