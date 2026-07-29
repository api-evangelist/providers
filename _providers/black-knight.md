---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: MSP (Mortgage Servicing Platform) was Black Knight's flagship product — the mainframe-rooted system of record that services the majority of US first-mortgage loans. MSP DX (Direct Exchange) is the RES
  name: MSP DX (Direct Exchange) APIs
  slug: msp-dx
- description: Borrower-facing servicing capabilities including the Promise To Pay API, which enables clients to document borrower payment promises along with reason codes, supporting collection workflows. Originall
  name: Servicing Digital / Promise To Pay APIs
  slug: servicing-digital
- description: LoanSphere was Black Knight's umbrella brand for default management (foreclosure, bankruptcy, loss-mitigation case management), document services (eClosing, eVault, eRecording via Simplifile/DocVerify
  name: LoanSphere Default, Document & Decisioning Suite
  slug: loansphere
- description: Empower was Black Knight's mid-to-enterprise loan origination system. After the ICE acquisition, Empower coexists with ICE's larger Encompass LOS (from the 2020 Ellie Mae acquisition). Empower API acc
  name: Empower LOS APIs
  slug: empower-los
- description: Although Encompass came to ICE via the 2020 Ellie Mae acquisition (not Black Knight), it is now the canonical LOS API surface under ICE Mortgage Technology and effectively supersedes the Empower publi
  name: Encompass Developer Connect (sibling product under ICE)
  slug: encompass-developer-connect
- description: Optimal Blue's Product & Pricing Engine (PPE) generates eligible products and pricing for any user in any format and automates loan creation, locking, post-lock management, and secondary / lock-desk w
  name: Optimal Blue Product & Pricing APIs (divested to Constellation)
  slug: optimal-blue-ppe
- description: Workflow and data APIs for the Resitrader loan-trading application — execute trades, manage data modules, centralize trading operations. Now operated by Optimal Blue under Constellation Software owner
  name: Optimal Blue Loan Trading APIs (Resitrader)
  slug: optimal-blue-trading
- description: Data tools including 16 Mortgage Market Rate Indices, integrable into dashboards. Successor to Black Knight's Originations Market Monitor and Mortgage Monitor data products at the API level.
  name: Optimal Blue Business Intelligence APIs
  slug: optimal-blue-business-intelligence
- description: Loansifter is the turnkey PPE for mortgage brokers — generate and display eligible products and pricing across borrower scenarios. Originally a Black Knight (via Optimal Blue) product, now under Const
  name: Optimal Blue Broker Pricing APIs (Loansifter)
  slug: optimal-blue-broker-pricing
artifact_total: 43
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-knight-domain-security.yml
- group: company
  title: Successor site (blackknightinc.com redirects here)
  type: Website
  url: https://mortgagetech.ice.com
- group: company
  title: 302-redirects to mortgagetech.ice.com
  type: LegacyWebsite
  url: https://www.blackknightinc.com
- group: other
  title: Intercontinental Exchange (NYSE ICE) — acquired Sept 2023
  type: ParentCompany
  url: https://www.ice.com
- group: start
  title: ICE Developer Portal (Mortgage Servicing, Fixed Income & Data Services)
  type: DeveloperPortal
  url: https://developer.ice.com
- group: start
  title: ICE Mortgage Technology Developer Portal (Encompass Developer Connect)
  type: DeveloperPortal
  url: https://developer.icemortgagetechnology.com
- group: start
  title: Optimal Blue Digital Marketplace (now Constellation Software)
  type: DeveloperPortal
  url: https://digitalmarketplace.optimalblue.com
- group: build
  title: 6 public sample repos (exp19-exp21 series, api-best-practices)
  type: GitHubOrganization
  url: https://github.com/ICEMortgageTechnology
- group: build
  title: 0 public repos (pre-rebrand placeholder)
  type: LegacyGitHubOrganization
  url: https://github.com/elliemae
- group: other
  title: ICE completed acquisition of Black Knight Sept 2023 (~$11.7B; Optimal Blue divested to Constellation Software)
  type: Acquisition
  url: https://www.ice.com
- group: design
  title: ''
  type: SpectralRules
  url: rules/black-knight-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/black-knight-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/black-knight-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/black-knight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/black-knight-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/black-knight-finops.yml
created: '2026-05-23'
description: 'Black Knight, Inc. was a Jacksonville-based mortgage technology and data provider whose core franchises were MSP (the dominant US loan-servicing platform), LoanSphere (default, document, and decisioning suites), Empower LOS (mid-market loan origination), and the Optimal Blue secondary marketing / product-and-pricing engine. Intercontinental Exchange (NYSE: ICE) acquired Black Knight in September 2023 for approximately $11.7B (down from the originally-announced $13.1B in May 2022) after divesting Optimal Blue to Constellation Software''s Perseus Operating Group as a condition of FTC clearance. Black Knight''s product lines now sit inside ICE Mortgage Technology alongside Encompass (the ex-Ellie Mae LOS). The blackknightinc.com domain redirects to mortgagetech.ice.com, and developer surfaces have migrated to developer.ice.com (MSP DX APIs, Servicing Vault, Loss Mitigation, Payoffs, Promise To Pay) and developer.icemortgagetechnology.com (Encompass Developer Connect). Optimal
  Blue''s APIs are now hosted at digitalmarketplace.optimalblue.com under independent Constellation Software ownership. This profile documents the API surfaces as they existed under Black Knight and tracks the post-acquisition fate of each product line.'
examples:
- key_count: 15
  name: Msp Loan Example
  slug: msp-loan-example
- key_count: 12
  name: Msp Payment Example
  slug: msp-payment-example
- key_count: 12
  name: Optimal Blue Lock Example
  slug: optimal-blue-lock-example
- key_count: 10
  name: Optimal Blue Pricing Example
  slug: optimal-blue-pricing-example
- key_count: 10
  name: Servicing Promise To Pay Example
  slug: servicing-promise-to-pay-example
features:
- description: Mainframe-rooted system of record that historically serviced the majority of US first mortgages; the largest single concentration in mortgage tech.
  name: MSP Loan Servicing of Record
- description: Modern REST surface over MSP covering loan boarding, escrow, payments, payoffs, default management, loss mitigation, investor reporting, stop-advance, and ownership transfer.
  name: MSP DX REST APIs
- description: Foreclosure, bankruptcy, and loss-mitigation case management; document services (eClosing, eVault, eRecording); decisioning analytics.
  name: LoanSphere Default Suite
- description: Mid-to-enterprise loan origination system with partner-gated integration; now coexists with Encompass under ICE.
  name: Empower LOS
- description: Industry-dominant product-and-pricing engine for rate locks and secondary marketing; divested to Constellation Software in 2023.
  name: Optimal Blue PPE
- description: Whole-loan trading platform; part of Optimal Blue, now Constellation.
  name: Resitrader Loan Trading
- description: Optimal Blue Business Intelligence APIs publish 16 mortgage rate indices derived from real-time PPE flow.
  name: 16 Mortgage Market Rate Indices
finops:
- name: Black Knight Finops
  service_category: ''
  slug: black-knight-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/black-knight.png
integrations:
- description: Sibling product under ICE; primary LOS integration target going forward.
  name: Encompass (Ellie Mae) LOS
- description: Cross-sell into ICE's broader data/markets platform.
  name: ICE Fixed Income & Data Services
- description: Optimal Blue Integration Studio ships done-for-you Salesforce connectors.
  name: Salesforce
json_schemas:
- name: MSP Escrow Item
  property_count: 7
  slug: msp-escrow
- name: MSP Loan
  property_count: 15
  slug: msp-loan
- name: MSP Payment
  property_count: 12
  slug: msp-payment
- name: Optimal Blue Rate Lock
  property_count: 12
  slug: optimal-blue-lock
- name: Optimal Blue Pricing Search Result
  property_count: 10
  slug: optimal-blue-pricing
- name: Promise To Pay
  property_count: 10
  slug: servicing-promise-to-pay
json_structures:
- name: Msp Loan Structure
  property_count: 0
  slug: msp-loan-structure
jsonld:
- class_count: 24
  name: Black Knight Context
  property_count: 10
  slug: black-knight-context
layout: provider
modified: '2026-07-25'
name: Black Knight (Acquired by ICE — Now ICE Mortgage Technology)
nav: Providers
network: true
overview: 'Black Knight (Acquired by ICE — Now ICE Mortgage Technology) publishes 1 API on the [APIs.io](https://apis.io/) network: Encompass Developer Connect (sibling product under ICE). Tagged areas include Mortgage Technology, Loan Servicing, Loan Origination, Secondary Marketing, and Default Management.


  The Black Knight (Acquired by ICE — Now ICE Mortgage Technology) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Black Knight Plans Pricing
  plan_count: 4
  slug: black-knight-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 0
  name: Black Knight Rate Limits
  slug: black-knight-rate-limits
rules:
- name: Black Knight (Acquired by ICE — Now ICE Mortgage Technology) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: black-knight-jsonschema-spectral-rules
- name: Black Knight (Acquired by ICE — Now ICE Mortgage Technology) API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: black-knight-rules
score:
  band: thin
  composite: 33.0
  delta: -5.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 33.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 38.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/black-knight/refs/heads/main/screenshots/black-knight-2026-06-20T173333.png
security:
- kind: domain-security
  name: Black Knight Domain Security
  slug: black-knight-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: black-knight
tags:
- Mortgage Technology
- Loan Servicing
- Loan Origination
- Secondary Marketing
- Default Management
- Investor Reporting
- Product Pricing Engine
- Real Estate Data
- FinTech
- Acquired Company
- ICE Mortgage Technology
use_cases:
- description: Servicers report loan-level activity to GSE and private investors via MSP DX investor-reporting APIs.
  name: Investor Loan Reporting
- description: Default servicers automate foreclosure, bankruptcy, and loss-mitigation case management via Loss Mitigation and Collections APIs.
  name: Default Workflow Automation
- description: Originators lock rates and price loans through Optimal Blue PPE APIs.
  name: Secondary Marketing Rate Lock
- description: Aggregators trade whole loans through Resitrader APIs.
  name: Whole Loan Trading
- description: Servicers document borrower payment commitments through the Promise To Pay API for collection workflows.
  name: Borrower Promise To Pay
website: https://mortgagetech.ice.com
---
