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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'REST API for tax compliance and information reporting: account owners, accounts, transactions, inventory, realized gains, tax documentation (W-8/W-9), filers, form items, disposition methods, transfer'
  name: TaxBit API
  slug: taxbit-api
artifact_total: 6
asyncapis:
- description: ''
  name: Taxbit Webhooks
  slug: taxbit-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://taxbit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.taxbit.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.taxbit.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.taxbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.taxbit.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://taxbitsupport.zendesk.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.taxbit.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.taxbit.com/blogs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taxbit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.taxbit.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.taxbit.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/taxbit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taxbit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taxbit-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taxbit-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taxbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taxbit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/taxbit-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taxbit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/taxbit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taxbit-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/taxbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/taxbit-packages.yml
- group: design
  title: ''
  type: Components
  url: components/taxbit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taxbit-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taxbit-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TaxBit is an end-to-end tax compliance and information-reporting platform for the digital economy, serving enterprises and governments across 70+ jurisdictions and 140+ countries. Its API turns transaction data into accurate cost basis, realized gains (IRS Form 8949 / 1099-B), and regulatory filings, and handles tax-documentation collection (W-9, W-8BEN, W-8BEN-E, self-certification), US TIN validation, DAC7 digital-platform-seller reporting, and CARF/DAC8 crypto-asset reporting. The REST API (documented at apidocs.taxbit.com) authenticates with tenant-scoped and account-owner-scoped bearer tokens, and TaxBit ships embeddable React/browser SDKs for collecting tax documentation directly inside customer apps.
image: https://files.readme.io/e2c1133-small-taxbit-dark.png
layout: provider
mcp_servers:
- description: ''
  name: taxbit-mcp.yml
  slug: taxbit-mcpyml
modified: '2026-07-21'
name: TaxBit
nav: Providers
network: true
overview: 'TaxBit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Tax Compliance, Information Reporting, and Digital Assets.


  The TaxBit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TaxBit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 40.9
  delta: -5.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 46.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/taxbit/refs/heads/main/screenshots/taxbit-2026-08-17T082251.png
security:
- kind: authentication
  name: Taxbit Authentication
  slug: taxbit-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Taxbit Domain Security
  slug: taxbit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Taxbit Trust Center
  slug: taxbit-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: taxbit
tags:
- Company
- Tax
- Tax Compliance
- Information Reporting
- Digital Assets
- Cryptocurrency
- Accounting
- Regtech
website: https://taxbit.com/
---
