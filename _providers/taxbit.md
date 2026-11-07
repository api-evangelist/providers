---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'REST API for tax compliance and information reporting: account owners, accounts, transactions, inventory, realized gains, tax documentation (W-8/W-9), filers, form items, disposition methods, transfer'
  name: TaxBit API
  slug: taxbit-api
artifact_total: 8
asyncapis:
- description: ''
  name: Taxbit Webhooks
  slug: taxbit-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.taxbit.com/blogs/rss.xml
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
  href: https://artifacts.apis.io/taxbit/security/taxbit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/taxbit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/taxbit/security/taxbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taxbit-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/taxbit/llms/taxbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taxbit-llms.txt
- group: agent
  href: https://artifacts.apis.io/taxbit/mcp/taxbit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/taxbit-mcp.yml
- group: auth
  href: https://artifacts.apis.io/taxbit/authentication/taxbit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/taxbit-authentication.yml
- group: design
  href: https://artifacts.apis.io/taxbit/conventions/taxbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/taxbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/taxbit/conventions/taxbit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/taxbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/taxbit/conformance/taxbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taxbit-conformance.yml
- group: auth
  href: https://artifacts.apis.io/taxbit/conformance/taxbit-conformance.yml
  title: ''
  type: Compliance
  url: conformance/taxbit-conformance.yml
- group: design
  href: https://artifacts.apis.io/taxbit/lifecycle/taxbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taxbit-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/taxbit/packages/taxbit-packages.yml
  title: ''
  type: Packages
  url: packages/taxbit-packages.yml
- group: build
  href: https://artifacts.apis.io/taxbit/packages/taxbit-packages.yml
  title: ''
  type: SDKs
  url: packages/taxbit-packages.yml
- group: design
  href: https://artifacts.apis.io/taxbit/components/taxbit-components.yml
  title: ''
  type: Components
  url: components/taxbit-components.yml
- group: design
  href: https://artifacts.apis.io/taxbit/data-model/taxbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/taxbit-data-model.yml
- group: design
  href: https://artifacts.apis.io/taxbit/asyncapi/taxbit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/taxbit-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/taxbit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TaxBit is an end-to-end tax compliance and information-reporting platform for the digital economy, serving enterprises and governments across 70+ jurisdictions and 140+ countries. Its API turns transaction data into accurate cost basis, realized gains (IRS Form 8949 / 1099-B), and regulatory filings, and handles tax-documentation collection (W-9, W-8BEN, W-8BEN-E, self-certification), US TIN validation, DAC7 digital-platform-seller reporting, and CARF/DAC8 crypto-asset reporting. The REST API (documented at apidocs.taxbit.com) authenticates with tenant-scoped and account-owner-scoped bearer tokens, and TaxBit ships embeddable React/browser SDKs for collecting tax documentation directly inside customer apps.
image: https://files.readme.io/e2c1133-small-taxbit-dark.png
layout: provider
mcp_servers:
- description: Remote MCP server at apidocs.taxbit.com over HTTP.
  name: TaxBit MCP Server
  slug: taxbit-apidocs
modified: '2026-10-06'
name: TaxBit
nav: Providers
network: true
overview: 'TaxBit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, Tax Compliance, Information Reporting, and Digital Assets.


  The TaxBit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TaxBit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 23.7
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/taxbit/taxbit-2026-08-17T082251.png
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
skill_count: 2
skills:
- name: Ingest transactions and report realized gains
  slug: taxbit-ingest-transactions-and-report-gains
- name: Onboard an account owner and collect tax documentation
  slug: taxbit-onboard-and-collect-tax-documentation
slug: taxbit
tags:
- Company
- Tax
- Tax Compliance
- Information Reporting
- Digital Assets
- Cryptocurrency
- Accounting
- RegTech
website: https://taxbit.com/
---
