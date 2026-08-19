---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: Threshold-key Auth Network nodes that issue and recover key shares anchored to OAuth/social/passkey identity providers. Accessed primarily through the Web3Auth client SDK rather than as a developer-fa
  name: Web3Auth Auth Network
  slug: auth-network
- description: Backend REST endpoints used by the Web3Auth dashboard to manage projects, verifiers, custom auth, and analytics. Available to project administrators.
  name: Web3Auth Dashboard / Verifier API
  slug: dashboard-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/web3auth-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/web3auth-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/web3auth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/web3auth
- group: company
  title: ''
  type: Website
  url: https://web3auth.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/web3auth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/web3auth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/web3auth-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://web3auth.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.web3auth.io/rss/
created: '2026-05-08'
description: Web3Auth (now MetaMask Embedded Wallets) is a non-custodial threshold-key wallet and authentication platform. It provides client SDKs (Web, React, Vue, iOS, Android, Flutter, React Native, Unity, Unreal, Node.js) and a backend Auth Network for OAuth-anchored MPC key shares. Public HTTP surface is limited and SDK-first.
finops:
- name: Web3Auth Finops
  service_category: Web3
  slug: web3auth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/web3auth.png
layout: provider
modified: '2026-05-08'
name: Web3Auth
nav: Providers
network: true
overview: 'Web3Auth publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, Wallets, Authentication, MPC, and Embedded Wallets.


  Web3Auth''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Web3Auth Plans Pricing
  plan_count: 4
  slug: web3auth-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Web3Auth Rate Limits
  slug: web3auth-rate-limits
score:
  band: minimal
  composite: 10.8
  delta: -3.8
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/web3auth/refs/heads/main/screenshots/web3auth-2026-06-20T201326.png
security:
- kind: domain-security
  name: Web3Auth Domain Security
  slug: web3auth-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Web3Auth Trust Center
  slug: web3auth-trust-center
  summary_line: SOC 2, GDPR
slug: web3auth
tags:
- Web3
- Wallets
- Authentication
- MPC
- Embedded Wallets
website: https://web3auth.io/
---
