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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for the MakeLeaps cloud invoicing platform. Authenticated with OAuth 2.0 client-credentials against api.makeleaps.com, it exposes partner-scoped resources for clients, documents (invoices, qu
  name: MakeLeaps API
  slug: makeleaps-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.makeleaps.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.makeleaps.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.makeleaps.com/en/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.makeleaps.com/en/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.makeleaps.com/en/api/tutorial/sending-your-first-document-with-makeleaps/
- group: operate
  title: ''
  type: Support
  url: https://help.makeleaps.jp/ja/
- group: company
  title: ''
  type: Blog
  url: https://www.makeleaps.com/updates/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MakeLeaps
- group: commercial
  title: ''
  type: Pricing
  url: https://www.makeleaps.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.makeleaps.com/home/profile/create/
- group: start
  title: ''
  type: Login
  url: https://app.makeleaps.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.makeleaps.com/%E5%88%A9%E7%94%A8%E8%A6%8F%E7%B4%84/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.makeleaps.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.makeleaps.com/
- group: build
  title: ''
  type: SDKs
  url: packages/makeleaps-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makeleaps-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/makeleaps-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makeleaps-llms.txt
created: '2026-07-17'
description: MakeLeaps is a cloud invoicing, quoting, and payment-management SaaS operated by Meikuriipusu K.K., a Ricoh Group company headquartered in Meguro-ku, Tokyo. The platform lets businesses create ten document types (quotes, invoices, purchase orders, receipts and more), send them electronically or by post in one click, track payments with automated bank reconciliation, and stay compliant with Japan's qualified-invoice law and electronic-bookkeeping regulations. MakeLeaps exposes a REST API at api.makeleaps.com secured with OAuth 2.0 client-credentials, letting partners create clients and documents and drive the sending workflow programmatically, plus a Salesforce (Apex) managed-package SDK and published tutorials for building your own MCP server over your invoice data.
image: https://www.makeleaps.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: MakeLeaps
nav: Providers
network: true
overview: 'MakeLeaps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Invoicing, Billing, Accounting, and Finance.


  MakeLeaps'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 33.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/makeleaps/refs/heads/main/screenshots/makeleaps-2026-07-25T225937.png
security:
- kind: authentication
  name: Makeleaps Authentication
  slug: makeleaps-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Makeleaps Domain Security
  slug: makeleaps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makeleaps
tags:
- Company
- Invoicing
- Billing
- Accounting
- Finance
- Payments
- Document-Management
- E-Invoicing
- Software-as-a-Service
- Japan
- Ricoh
website: https://www.makeleaps.com/en/
---
