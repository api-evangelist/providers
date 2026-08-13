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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
api_count: 12
apis:
- description: The Pinwheel Deposit Switch API automates moving a customer's direct deposit allocations from one financial institution to another by connecting directly to 17,000+ payroll providers. The product comb
  name: Pinwheel Deposit Switch API
  slug: pinwheel-deposit-switch-api
- description: 'Pinwheel Verify is a payroll-connected income and employment verification API that returns identity, employment status and dates, current and historical paystubs, shifts (for hourly workers), and tax '
  name: Pinwheel Verify API
  slug: pinwheel-verify-api
- description: The Pinwheel Taxes API retrieves W-2, 1099-K, 1099-MISC, and 1099-NEC documents directly from a worker's payroll provider, returning them as both PDF and structured JSON. Tax-prep software, gig platfo
  name: Pinwheel Taxes API
  slug: pinwheel-taxes-api
- description: The Pinwheel Bill Switch API updates a user's stored payment method across merchant and biller accounts (streaming, telecom, utilities, insurance, subscriptions) so that a financial institution can mo
  name: Pinwheel Bill Switch API
  slug: pinwheel-bill-switch-api
- description: Pinwheel Bill Manager detects, organizes, and acts on a customer's recurring bills and subscriptions. It auto-identifies recurring charges with 80% greater accuracy than category-based detection, surf
  name: Pinwheel Bill Manager API
  slug: pinwheel-bill-manager-api
- description: Switch Kit bundles Pinwheel's Deposit Switch and Bill Switch products into a single onboarding experience banks and fintechs can drop into account-opening and reactivation flows. It is the productized
  name: Pinwheel Switch Kit API
  slug: pinwheel-switch-kit-api
- description: The Pinwheel Connected Accounts API gives applications ongoing, consented access to a user's payroll and external-account data after the initial link. Builders use it to keep employment, income, and a
  name: Pinwheel Connected Accounts API
  slug: pinwheel-connected-accounts-api
- description: The Pinwheel Link Token API mints short-lived link_tokens that initialize the Pinwheel Link drop-in UI (Web, iOS, Android, React Native, Flutter, Capacitor). The token scopes the session to a specific
  name: Pinwheel Link Token API
  slug: pinwheel-link-token-api
- description: The Pinwheel Accounts API exposes the linked payroll accounts a user has connected through Pinwheel Link, surfacing account-level metadata such as platform, status, employment relationship, and suppor
  name: Pinwheel Accounts API
  slug: pinwheel-accounts-api
- description: The Pinwheel Jobs API is the asynchronous execution surface for every Pinwheel job — direct_deposit_switch, direct_deposit_allocations, paystubs, employment, identity, income, shifts, tax_forms, bill_
  name: Pinwheel Jobs API
  slug: pinwheel-jobs-api
- description: 'The Pinwheel Platforms API exposes the catalog of supported payroll providers and employer-side platforms (ADP, Workday, Paychex, Paycom, Gusto, Rippling, plus 1,600+ others). Clients use it to check '
  name: Pinwheel Platforms API
  slug: pinwheel-platforms-api
- description: 'The Pinwheel Webhooks API is how the platform delivers asynchronous events — job completions, link events, account status changes, deposit switch outcomes, tax-form availability, and banking events — '
  name: Pinwheel Webhooks API
  slug: pinwheel-webhooks-api
artifact_total: 47
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/pinwheel-api-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinwheel-api-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://pinwheelapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pinwheelapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pinwheelapi.com/public/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pinwheelapi.com/public/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pinwheelapi.com/public/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://www.pinwheelapistatus.com/
- group: start
  title: ''
  type: Signup
  url: https://app.getpinwheel.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.getpinwheel.com/login
- group: start
  title: ''
  type: Sandbox
  url: https://docs.pinwheelapi.com/public/docs/sandbox
- group: auth
  title: ''
  type: Authentication
  url: https://docs.pinwheelapi.com/public/docs/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.pinwheelapi.com/public/docs/webhooks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/underdog-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinwheel-api/
- group: company
  title: ''
  type: Blog
  url: https://pinwheelapi.com/blog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/underdog-tech/pinwheel-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/underdog-tech/pinwheel-android-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/underdog-tech/react-native-pinwheel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/underdog-tech/pinwheel-flutter-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/underdog-tech/pinwheel-capacitor-sdk
created: '2026-05-25'
description: Pinwheel is an employment and income data platform that connects banks, fintechs, and lenders directly to payroll systems. The API covers direct deposit switching (PreMatch, NativeLink), income and employment verification, paystub and shift data, tax form retrieval (W-2, 1099), bill switch, and bill manager. Pinwheel maintains direct integrations with 1,600+ payroll platforms covering an estimated 80% of U.S. workers and is the first Consumer Reporting Agency (CRA) in the payroll-connectivity space.
features:
- description: Move a customer's direct deposit allocations to a new institution via PreMatch (credential-less I-9 match), NativeLink (device-saved credentials), or Forms; routed by the Prime algorithm for highest conversion.
  name: Direct Deposit Switch
- description: Real-time payroll-connected verification returning identity, employment status, paystubs, shifts, and tax forms from the source payroll system.
  name: Income & Employment Verification (Verify)
- description: Pull W-2, 1099-K, 1099-MISC, and 1099-NEC documents directly from payroll providers as PDF and structured JSON.
  name: Tax Form Retrieval
- description: Update stored payment methods across merchant and biller accounts so issuers can capture recurring card-on-file spend.
  name: Bill Switch
- description: Auto-detect, organize, and act on recurring bills and subscriptions with 80% greater accuracy than category-based detection.
  name: Bill Manager
- description: Bundled Deposit Switch + Bill Switch onboarding flow productized for primary-banking activation.
  name: Switch Kit
- description: Ongoing consented access to payroll and external account data for re-underwriting, servicing, and credential refresh.
  name: Connected Accounts
- description: Drop-in UI for Web, iOS, Android, React Native, Flutter, and Capacitor that handles consent, MFA, and credential capture across 1,600+ payroll platforms.
  name: Pinwheel Link
- description: First payroll-connectivity provider designated as a CRA, allowing Verify outputs to be used directly in FCRA-governed credit decisions.
  name: Consumer Reporting Agency (CRA) Status
- description: 1,600+ supported payroll platforms reaching an estimated 80% of U.S. workers.
  name: Coverage
- description: Asynchronous event delivery for job completions, link events, account status changes, and banking events with HMAC signatures and optional encryption.
  name: Webhooks with Signing & Optional Payload Encryption
- description: Full-feature sandbox with synthetic users, employers, jobs, and webhook event simulation.
  name: Sandbox Environment
- description: Dated API versions selectable via header (v2022-03-02 through v2025-07-08+).
  name: Versioned API
graphqls:
- description: This directory contains a conceptual GraphQL schema for the [Pinwheel](https://pinwheelapi.com/) payroll connectivity and income verification platform. Pinwheel provides direct integrations with 1,600
  name: Pinwheel API - GraphQL Schema
  slug: pinwheel-api-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinwheel-api.png
integrations:
- description: Direct payroll-provider integration for verification, paystubs, and deposit allocation.
  name: ADP
- description: Direct payroll-provider integration covering enterprise employers.
  name: Workday
- description: SMB-focused payroll integration.
  name: Paychex
- description: Mid-market payroll integration.
  name: Paycom
- description: SMB cloud payroll integration covering startups and small employers.
  name: Gusto
- description: HRIS + payroll integration.
  name: Rippling
- description: Long-tail coverage including local processors, government payroll, and industry-specific systems.
  name: 1,600+ Additional Payroll Platforms
layout: provider
modified: '2026-05-25'
name: Pinwheel
nav: Providers
network: true
overview: 'Pinwheel publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Employment, Income, Payroll, Direct Deposit, and Identity.


  Pinwheel''s developer surface includes developer portal, documentation, API reference, getting-started guide, changelog, signup flow, sandbox, and 14 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 48.1
    developer_ergonomics: 69.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 43.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinwheel-api/refs/heads/main/screenshots/pinwheel-api-2026-06-20T191724.png
security:
- kind: domain-security
  name: Pinwheel Api Domain Security
  slug: pinwheel-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pinwheel Api Trust Center
  slug: pinwheel-api-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: pinwheel-api
solutions:
- description: Primary banking activation via Switch Kit; deposit and recurring-payment capture to drive balance, engagement, and lifetime value.
  name: For Banks & Credit Unions
- description: FCRA-grade payroll-connected income, employment, and tax-form verification for mortgage, auto, personal loan, and BNPL underwriting.
  name: For Lenders
- description: Drop-in Pinwheel Link plus Connected Accounts to power onboarding, direct deposit capture, and ongoing data refresh.
  name: For Fintechs & Challenger Banks
- description: Direct W-2/1099 retrieval and tax-platform webhooks for tax-prep flows and gig-worker tax tools.
  name: For Tax & Payroll Software
- description: Real-time employment and income verification at application time, plus shift data for hourly workers.
  name: For Property Managers & Gig Platforms
tags:
- Employment
- Income
- Payroll
- Direct Deposit
- Identity
- Verification
- Financial
- Tax
- Bill Pay
use_cases:
- description: National banks, credit unions, and challenger banks use Deposit Switch + Bill Switch to make a newly-opened account the customer's primary financial relationship.
  name: Banking Primacy
- description: Lenders use Verify as a real-time alternative to Work Number for payroll-direct income and employment verification.
  name: Mortgage & Auto Lending
- description: Consumer lenders use Verify and Connected Accounts to refresh income at underwriting and during re-pricing windows.
  name: Personal Loan / BNPL Underwriting
- description: Tax-prep software uses the Taxes API to skip manual W-2 / 1099 uploads and pull forms directly from payroll.
  name: Tax Preparation
- description: Gig platforms use prior-year 1099 retrieval to power quarterly self-employment tax estimates for their workers.
  name: Gig Worker Quarterly Tax Estimation
- description: Property managers use Verify to confirm tenant employment and income at application time.
  name: Property Management & Rental Screening
- description: Personal finance apps and challenger banks use Bill Manager to give users a single view of recurring obligations with one-click switch and cancel.
  name: Subscription & Recurring Bill Management
website: https://pinwheelapi.com/
---
