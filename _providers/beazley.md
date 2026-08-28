---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Beazley Agentic Access
  operation_count: 75
  slug: beazley-agentic-access
  summary_line: 75 operations · 26 acting
api_count: 9
apis:
- description: The current published version of Beazley's risk data capture API. Provides a channel for partner systems to feed quote and risk data directly into Beazley's core Record of Risk systems, with create, r
  name: 'Beazley Data Capture: Quote and Risk Data v2'
  slug: beazley-data-capture-quote-and-risk-data-v2
- description: The original version of Beazley's risk data capture API, feeding quote and risk data from partner systems into Beazley's core Record of Risk systems. Superseded by v2 but still published in the develo
  name: 'Beazley Data Capture: Quote and Risk Data v1'
  slug: beazley-data-capture-quote-and-risk-data-v1
- description: A pre-release version of the Data Capture API published under Beazley's Prerelease APIM product, exposing a single create-risk operation. Backed by an Azure Logic App rather than the core Record of Ri
  name: 'Beazley Data Capture: Quote and Risk Data v3 (pre-release)'
  slug: beazley-data-capture-quote-and-risk-data-v3
- description: Compliance validation and search for Beazley's underwriting systems. Runs rule-driven compliance checks determined by system and action parameters, searches broker agencies, broker contacts and produc
  name: Beazley Compliance Web API
  slug: beazley-compliance-web-api
- description: Marketing details for Beazley's partner organisations — broker and insured organisations, contacts and microsites — with read and write operations over contacts and organisations plus microsite-scoped
  name: Beazley Broker and Insured Marketing Data v2
  slug: beazley-broker-and-insured-marketing-data-v2
- description: A standard set of foreign exchange rates for Beazley systems, exposing rates, rate providers and supported currencies. Reference data supporting multi-currency specialty insurance placement, published
  name: Beazley Currency Exchange
  slug: beazley-currency-exchange
- description: 'Public-facing reference data on Beazley''s people and divisions, with person lookup by record id, profile images, profile image by email, and a deleted people feed for downstream synchronisation. Sold '
  name: About Beazley
  slug: beazley-about-beazley
- description: Insurance glossary and knowledge API providing definitions of insurance terms, frequently asked questions by intent name, and Beazley product lookup by term. Published sandbox-only and backed by an Az
  name: Beazley Fast Reader
  slug: beazley-fast-reader
- description: A set of simple rating endpoints published for testing, exposing a single cyber rating operation. The only rating surface in Beazley's public catalog, and explicitly described as being for testing rat
  name: Beazley Simple Raters
  slug: beazley-simple-raters
artifact_total: 30
collections:
- collection_type: open
  name: About Beazley (Sandbox)
  slug: open-beazley-about-beazley-sandbox
- collection_type: open
  name: About Beazley
  slug: open-beazley-about-beazley
- collection_type: open
  name: Broker and Insured Marketing Data v2 (Sandbox)
  slug: open-beazley-broker-and-insured-marketing-data-v2-sandbox
- collection_type: open
  name: Broker and Insured Marketing Data v2
  slug: open-beazley-broker-and-insured-marketing-data-v2
- collection_type: open
  name: Compliance Web API
  slug: open-beazley-compliance-web-api
- collection_type: open
  name: Currency Exchange (Sandbox)
  slug: open-beazley-currency-exchange-sandbox
- collection_type: open
  name: Currency Exchange
  slug: open-beazley-currency-exchange
- collection_type: open
  name: 'Data Capture: Quote and Risk Data (Sandbox)'
  slug: open-beazley-data-capture-quote-and-risk-data-sandbox
- collection_type: open
  name: 'Data Capture: Quote and Risk Data v2 (Sandbox)'
  slug: open-beazley-data-capture-quote-and-risk-data-v2-sandbox
- collection_type: open
  name: 'Data Capture: Quote and Risk Data v2'
  slug: open-beazley-data-capture-quote-and-risk-data-v2
- collection_type: open
  name: 'Data Capture: Quote and Risk Data v3 (pre-release)'
  slug: open-beazley-data-capture-quote-and-risk-data-v3-pre-release
- collection_type: open
  name: 'Data Capture: Quote and Risk Data'
  slug: open-beazley-data-capture-quote-and-risk-data
- collection_type: open
  name: Fast Reader
  slug: open-beazley-fast-reader
- collection_type: open
  name: Simple Raters
  slug: open-beazley-simple-raters
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beazley-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beazley-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beazley-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.beazley.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.beazley.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.beazley.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.beazley.com/apis
- group: start
  title: ''
  type: SignUp
  url: https://developer.beazley.com/signup
- group: other
  title: ''
  type: SignIn
  url: https://developer.beazley.com/signin
- group: commercial
  title: ''
  type: Plans
  url: https://developer.beazley.com/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.beazley.com/products
- group: start
  title: ''
  type: BrokerPortal
  url: https://www.beazley.com/en-us/broker-centre
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beazley
- group: other
  title: ''
  type: Email
  url: mailto:ITArchitecture@Beazley.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beazley-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/beazley-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beazley-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beazley-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beazley-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beazley-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beazley-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beazley-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/beazley-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beazley-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/beazley-plans.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/beazley-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.beazley.security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beazley
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beazley.com/en-us/privacy-and-cookies-statements/
- group: commercial
  title: ''
  type: LegalInformation
  url: https://www.beazley.com/en-us/legal-information-en/
- group: operate
  title: ''
  type: Support
  url: mailto:ITArchitecture@Beazley.com
- group: operate
  title: ''
  type: Contact
  url: https://www.beazley.com/en-us/contact-us/
- group: company
  title: ''
  type: News
  url: https://www.beazley.com/en-us/news-and-events/
created: '2026-07-25'
description: Beazley plc is a London-headquartered specialty insurer and one of the largest managing agents at Lloyd's of London, underwriting through Lloyd's syndicates alongside US admitted and surplus lines carriers and a European company platform. Its book is specialty property and casualty — cyber and technology risks (where it is a global market leader), professional indemnity, management liability and directors and officers, marine, political risk, contingency, environmental, healthcare and property. Its home market is the United Kingdom, where there is no open-insurance mandate; the only market-wide data and API modernization effort is the Lloyd's Blueprint Two programme, and Beazley sat on the closed beta group that tested Lloyd's ACORD-based Core Data Record. Unusually for a carrier, Beazley operates a real first-party developer portal at developer.beazley.com — an Azure API Management portal with self-serve account signup, a publicly browsable catalog of 14 published APIs across
  nine families, sandbox environments, and machine-readable OpenAPI 3.0.1 for every one of them. The APIs are partner-and-broker oriented rather than consumer facing — risk and quote data capture into Beazley's core Record of Risk systems, broker and insured marketing data, compliance validation, currency exchange, a cyber rater, and insurance-terms reference data. Every API is behind an Azure APIM subscription key and every product carries approvalRequired, so browsing and spec download are open but actually calling the gateway requires Beazley to approve the subscription. There is no ACORD, AL3 or IVANS reference anywhere in the portal or the specs, no webhook or event catalog, no GraphQL, and no bind, issue or FNOL endpoint — bind is done by brokers through the gated myBeazley quote-and-bind portal, not through the public API surface. Beazley is subject to a recommended all-cash offer from Zurich Insurance Group announced 2 March 2026.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Derived candidate tool set — Beazley publishes no MCP server.
  name: Beazley candidate MCP tool manifest
  slug: beazley-candidate-mcp-tool-manifest
modified: '2026-07-25'
name: Beazley
nav: Providers
network: true
overview: 'Beazley publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Data Capture: Quote and Risk Data v2, Data Capture: Quote and Risk Data v1, Data Capture: Quote and Risk Data v3 (pre-release), and 6 more. Tagged areas include Insurance, United Kingdom, Property and Casualty, Cyber Insurance, and Specialty Insurance.


  Beazley''s developer surface includes authentication, documentation, API reference, signup flow, sandbox, support, product news, and 27 more developer resources.'
plans:
- name: Beazley Plans
  plan_count: 9
  slug: beazley-plans
random_paper: 13
rate_limits:
- limit_count: 8
  name: Beazley Rate Limits
  slug: beazley-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 16.7
    contract_quality: 44.1
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 39.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beazley/refs/heads/main/screenshots/beazley-2026-07-25T202607.png
security:
- kind: authentication
  name: Beazley Authentication
  slug: beazley-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Beazley Domain Security
  slug: beazley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Beazley Trust Center
  slug: beazley-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, SOC 2 Type 2
slug: beazley
tags:
- Insurance
- United Kingdom
- Property and Casualty
- Cyber Insurance
- Specialty Insurance
- Lloyd's of London
- Underwriting
- Risk Data
- Brokers
- Carrier
website: https://www.beazley.com/
---
