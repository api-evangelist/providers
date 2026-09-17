---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 189
  human_in_the_loop: 20
  name: Dynamic Labs Agentic Access
  operation_count: 294
  slug: dynamic-labs-agentic-access
  summary_line: 294 operations · 189 acting · 20 human-in-the-loop
api_count: 31
apis:
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Retrieve aggregate environment analytics.
  name: Dynamic Analytics API
  slug: dynamic-labs-analytics-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Create and revoke environment-scoped API tokens.
  name: Dynamic API Tokens API
  slug: dynamic-labs-api-tokens-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Provision MPC-TSS embedded wallets for users.
  name: Dynamic Embedded Wallets API
  slug: dynamic-labs-embedded-wallets-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Retrieve and update environment (project) configuration.
  name: Dynamic Environments API
  slug: dynamic-labs-environments-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Download data exports.
  name: Dynamic Exports API
  slug: dynamic-labs-exports-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Fetch the JSON Web Key Set used to verify Dynamic JWTs.
  name: Dynamic JWKS API
  slug: dynamic-labs-jwks-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: List and manage end users authenticated into an environment.
  name: Dynamic Users API
  slug: dynamic-labs-users-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: View and manage wallets linked to users.
  name: Dynamic Wallets API
  slug: dynamic-labs-wallets-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Manage webhook endpoints for event notifications.
  name: Dynamic Webhooks API
  slug: dynamic-labs-webhooks-api
- description: 'REST API for backend integrations: list users and wallets, manage policies, validate JWTs, fetch auth events, manage environments.'
  name: Dynamic Backend API
  slug: backend-api
- description: Webhook delivery of auth, user, wallet, and session events. Subscriptions managed through dashboard and Backend API.
  name: Dynamic Webhooks
  slug: webhooks
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Chainalysis API from Dynamic — 3 operation(s) for chainalysis.
  name: Dynamic Chainalysis API
  slug: dynamic-labs-chainalysis-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Chains API from Dynamic — 1 operation(s) for chains.
  name: Dynamic Chains API
  slug: dynamic-labs-chains-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Custom Fields API from Dynamic — 2 operation(s) for custom fields.
  name: Dynamic Custom Fields API
  slug: dynamic-labs-custom-fields-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Custom Networks API from Dynamic — 2 operation(s) for custom networks.
  name: Dynamic Custom Networks API
  slug: dynamic-labs-custom-networks-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The DeeplinkUrls API from Dynamic — 2 operation(s) for deeplinkurls.
  name: Dynamic Deeplink URLS API
  slug: dynamic-labs-deeplinkurls-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Events API from Dynamic — 3 operation(s) for events.
  name: Dynamic Events API
  slug: dynamic-labs-events-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The ExternalJwt API from Dynamic — 1 operation(s) for externaljwt.
  name: Dynamic External JWT API
  slug: dynamic-labs-externaljwt-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Gates API from Dynamic — 4 operation(s) for gates.
  name: Dynamic Gates API
  slug: dynamic-labs-gates-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The GlobalWalletAccessControl API from Dynamic — 5 operation(s) for globalwalletaccesscontrol.
  name: Dynamic Global Wallet Access Control API
  slug: dynamic-labs-globalwalletaccesscontrol-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The GlobalWalletConnections API from Dynamic — 1 operation(s) for globalwalletconnections.
  name: Dynamic Global Wallet Connections API
  slug: dynamic-labs-globalwalletconnections-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The GlobalWallets API from Dynamic — 3 operation(s) for globalwallets.
  name: Dynamic Global Wallets API
  slug: dynamic-labs-globalwallets-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Invites API from Dynamic — 3 operation(s) for invites.
  name: Dynamic Invites API
  slug: dynamic-labs-invites-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Members API from Dynamic — 4 operation(s) for members.
  name: Dynamic Members API
  slug: dynamic-labs-members-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Mfa API from Dynamic — 2 operation(s) for mfa.
  name: Dynamic Mfa API
  slug: dynamic-labs-mfa-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The NameServices API from Dynamic — 4 operation(s) for nameservices.
  name: Dynamic Name Services API
  slug: dynamic-labs-nameservices-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Organizations API from Dynamic — 8 operation(s) for organizations.
  name: Dynamic Organizations API
  slug: dynamic-labs-organizations-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Origins API from Dynamic — 2 operation(s) for origins.
  name: Dynamic Origins API
  slug: dynamic-labs-origins-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Projects API from Dynamic — 2 operation(s) for projects.
  name: Dynamic Projects API
  slug: dynamic-labs-projects-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The SDK API from Dynamic — 124 operation(s) for sdk.
  name: Dynamic SDK API
  slug: dynamic-labs-sdk-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The SDK Views API from Dynamic — 2 operation(s) for sdk views.
  name: Dynamic SDK Views API
  slug: dynamic-labs-sdk-views-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Sessions API from Dynamic — 3 operation(s) for sessions.
  name: Dynamic Sessions API
  slug: dynamic-labs-sessions-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Settings API from Dynamic — 9 operation(s) for settings.
  name: Dynamic Settings API
  slug: dynamic-labs-settings-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The TestAccount API from Dynamic — 1 operation(s) for testaccount.
  name: Dynamic Test Account API
  slug: dynamic-labs-testaccount-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Visits API from Dynamic — 1 operation(s) for visits.
  name: Dynamic Visits API
  slug: dynamic-labs-visits-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Waas API from Dynamic — 14 operation(s) for waas.
  name: Dynamic Waas API
  slug: dynamic-labs-waas-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The WalletConnect API from Dynamic — 1 operation(s) for walletconnect.
  name: Dynamic Wallet Connect API
  slug: dynamic-labs-walletconnect-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: Gate authentication with allowlists.
  name: Dynamic Allow Lists API
  slug: dynamic-labs-allow-lists-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The Custom Hostnames API from Dynamic — 2 operation(s) for custom hostnames.
  name: Dynamic Custom Hostnames API
  slug: dynamic-labs-custom-hostnames-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The MFA Settings API from Dynamic — 3 operation(s) for mfa settings.
  name: Dynamic MFA Settings API
  slug: dynamic-labs-mfa-settings-api
- baseURL: https://app.dynamicauth.com/api/v0
  baseurl_source: declared
  description: The User API Tokens API from Dynamic — 2 operation(s) for user api tokens.
  name: Dynamic User API Tokens API
  slug: dynamic-labs-user-api-tokens-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dynamic Allowlists API
  slug: open-dynamic-labs-allowlists-api
- collection_type: open
  name: Dynamic Allowlists Analytics API
  slug: open-dynamic-labs-analytics-api
- collection_type: open
  name: Dynamic Allowlists API Tokens API
  slug: open-dynamic-labs-api-tokens-api
- collection_type: open
  name: Dynamic Allowlists Embedded Wallets API
  slug: open-dynamic-labs-embedded-wallets-api
- collection_type: open
  name: Dynamic Allowlists Environments API
  slug: open-dynamic-labs-environments-api
- collection_type: open
  name: Dynamic Allowlists Exports API
  slug: open-dynamic-labs-exports-api
- collection_type: open
  name: Dynamic Allowlists JWKS API
  slug: open-dynamic-labs-jwks-api
- collection_type: open
  name: Dynamic Allowlists Users API
  slug: open-dynamic-labs-users-api
- collection_type: open
  name: Dynamic Allowlists Wallets API
  slug: open-dynamic-labs-wallets-api
- collection_type: open
  name: Dynamic Allowlists Webhooks API
  slug: open-dynamic-labs-webhooks-api
- collection_type: open
  name: Dynamic API
  slug: open-dynamic-labs
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/agentic-access/dynamic-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dynamic-labs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/security/dynamic-labs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dynamic-labs-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/security/dynamic-labs-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamic-labs-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/security/dynamic-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamic-labs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/authentication/dynamic-labs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamic-labs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dynamic-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dynamic-labs-financial
- group: company
  title: ''
  type: Website
  url: https://www.dynamic.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dynamic.xyz
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/plans/dynamic-labs-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamic-labs-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/rate-limits/dynamic-labs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dynamic-labs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/finops/dynamic-labs-finops.yml
  title: ''
  type: FinOps
  url: finops/dynamic-labs-finops.yml
created: '2026-07-01'
description: Dynamic is a web3 authentication and embedded wallet platform. It provides multi-chain login, embedded and smart wallets secured with MPC-TSS, onramps, and end-to-end user management through a developer dashboard, client SDKs, and an environment-scoped REST API for programmatically managing users, wallets, projects, webhooks, and token verification.
finops:
- name: Dynamic Labs Finops
  service_category: Identity and Access Management
  slug: dynamic-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dynamic-labs.png
layout: provider
modified: '2026-07-01'
name: Dynamic
nav: Providers
network: true
overview: 'Dynamic publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Tokens API, Embedded Wallets API, and 36 more. Tagged areas include Web3, Authentication, Embedded Wallets, Wallets, and MPC.


  Dynamic''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Dynamic Labs Plans Pricing
  plan_count: 3
  slug: dynamic-labs-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Dynamic Labs Rate Limits
  slug: dynamic-labs-rate-limits
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 29.8
    discoverability: 68.5
    operational_transparency: 34.2
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamic-labs/refs/heads/main/screenshots/dynamic-labs-2026-07-25T212555.png
security:
- kind: authentication
  name: Dynamic Labs Authentication
  slug: dynamic-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dynamic Labs Domain Security
  slug: dynamic-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dynamic Labs Vulnerability Disclosure
  slug: dynamic-labs-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Dynamic Labs Trust Center
  slug: dynamic-labs-trust-center
  summary_line: SOC 2
slug: dynamic-labs
tags:
- Web3
- Authentication
- Embedded Wallets
- Wallets
- MPC
- Onboarding
- Crypto
website: https://www.dynamic.xyz
---
