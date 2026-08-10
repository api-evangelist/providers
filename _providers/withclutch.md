---
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Clutch delivers daily origination datasets to credit union customers over either SFTP or a File Transfer API. The public knowledge base documents the datasets (lending, account opening, funding, NACHA
  name: Clutch Data Exports File Transfer API
  slug: clutch-data-exports-file-transfer-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://withclutch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.withclutch.com/support/solutions
- group: operate
  title: ''
  type: Support
  url: https://support.withclutch.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://withclutch.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withclutch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withclutch.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withclutch.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://withclutch.com/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withclutch.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.withclutch.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withclutch/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/withclutch_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/withclutch-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/withclutch-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/withclutch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/withclutch-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/withclutch-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/withclutch-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/withclutch-data-exports.yml
coverage:
  checked: '2026-08-05'
  detail: Clutch's public knowledge base documents a File Transfer API and publishes full field dictionaries for its five daily data exports, but the File Transfer API reference article itself 302s to the Freshdesk customer login (error=login_required), so no base URL, authentication scheme, endpoint list or machine-readable spec is publicly readable.
  evidence:
  - status: 302
    url: https://support.withclutch.com/support/solutions/articles/153000248800
  - status: 200
    url: https://support.withclutch.com/support/solutions/articles/153000254486-data-exports-api-vs-sftp-delivery
  - status: 404
    url: https://api.clutch.partners/openapi.json
  - status: 404
    url: https://withclutch.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Clutch (withclutch.com) is a US fintech that builds digital origination and lending automation software exclusively for credit unions. The platform spans consumer loan origination, deposit and business account opening, an omnichannel banker workstation (Fulfillment), an automated decisioning engine (Fastlane), targeted remarketing, data insights, and AI assistants — HAL for lending and Emma for collections — packaged as the Clutch Lending Automation System (LAS). Clutch integrates with credit union cores, loan origination systems such as MeridianLink Consumer LOS (LoansPQ), digital banking platforms and decisioning vendors, and reports powering origination for roughly 150 credit unions including six of the ten largest in the United States. Its customer-facing data surface is a File Transfer API and SFTP delivery for daily CSV exports covering lending, account opening, funding, NACHA and HAL conversation datasets; the API reference itself sits behind the customer support login.
image: https://withclutch.com/wp-content/uploads/2025/07/Clutch.svg
json_schemas:
- name: Clutch Account Opening Data Export record
  property_count: 64
  slug: withclutch-account-opening
- name: Clutch Funding Data Export record
  property_count: 12
  slug: withclutch-funding
- name: Clutch HAL Data Export record
  property_count: 10
  slug: withclutch-hal
- name: Clutch Lending Data Export record
  property_count: 59
  slug: withclutch-lending
- name: Clutch NACHA Data Export record
  property_count: 24
  slug: withclutch-nacha
layout: provider
modified: '2026-08-05'
name: Clutch
nav: Providers
network: true
overview: 'Clutch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Credit Unions, Lending, Loan Origination, and Account Opening.


  Clutch''s developer surface includes documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 28.0
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 9.7
    developer_ergonomics: 15.2
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 28.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Withclutch Domain Security
  slug: withclutch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Withclutch Vulnerability Disclosure
  slug: withclutch-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Withclutch Trust Center
  slug: withclutch-trust-center
  summary_line: SOC 2 Type 2
slug: withclutch
tags:
- Company
- Credit Unions
- Lending
- Loan Origination
- Account Opening
- Financial Services
- Fintech
- Banking
- Data Exports
website: https://withclutch.com/
---
