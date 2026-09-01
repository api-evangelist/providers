---
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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Open Kraken is the integration layer of the Kraken utility operating system. Kraken publicly describes it as "APIs, events and MCP" for building apps and experiences against data and capabilities insi
  name: Open Kraken APIs and Events
  slug: open-kraken-apis-and-events
- description: An AI access layer that Kraken announced as an expansion of Open Kraken, built using the Model Context Protocol and described as MCP gateways that let a utility's own AI agents orchestrate approved ac
  name: Open Kraken AI Access Layer (MCP)
  slug: open-kraken-ai-access-layer-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kraken-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kraken-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kraken-technologies-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/kraken-technologies-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/kraken-technologies-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kraken-technologies-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kraken-technologies-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kraken-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kraken.tech/legal/trust-center
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kraken-technologies-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kraken-technologies-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kraken.tech/vulnerability-disclosure-process
- group: company
  title: ''
  type: Website
  url: https://www.kraken.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kraken.tech/
- group: other
  title: ''
  type: DesignSystem
  url: https://tako.kraken.tech/
- group: build
  title: ''
  type: SDK
  url: https://github.com/kraken-tech/kraken-apps-examples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kraken-tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octoenergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/krakentech/
- group: company
  title: ''
  type: Blog
  url: https://www.kraken.tech/insights
- group: operate
  title: ''
  type: PressReleases
  url: https://www.kraken.tech/press-releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.kraken.tech/product-updates
- group: company
  title: ''
  type: Partners
  url: https://www.kraken.tech/marketplace
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.kraken.tech/bpo-partner-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.kraken.tech/vulnerability-disclosure-process
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kraken-technologies-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.kraken.tech/legal/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/kraken-technologies-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://support.kraken.tech/
- group: commercial
  title: ''
  type: Legal
  url: https://www.kraken.tech/legal
- group: other
  title: ''
  type: Subprocessors
  url: https://www.kraken.tech/legal/subprocessors
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.kraken.tech/legal/dpa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kraken.tech/legal/marketplace-access-and-use-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kraken.tech/legal/privacy-notice
created: '2026-07-27'
description: 'Kraken Technologies is the United Kingdom energy technology company behind Kraken, the licensed cloud operating system for utilities. Founded in 2016 inside Octopus Energy and spun out as an independent business, Kraken says it supports more than 90 million customer accounts for licensees including E.ON Next, EDF, Origin, Tokyo Gas, National Grid, Good Energy, Plenitude, Energy Queensland, Essential Energy, Portsmouth Water and TalkTalk across electricity, gas, water and broadband. It sits one layer behind the utility rather than in front of the consumer: it does not hold a supply licence, does not settle in the wholesale market and does not publish grid or market data, so the retailers and networks it powers carry the regulatory obligations, not Kraken. Its API posture matches that position and is honestly closed. The Open Kraken programme publicly advertises APIs, events, embedded apps, Flow automation and an MCP-based AI access layer, but every reference surface is gated:
  docs.kraken.tech forces SSO login on every path, no base URL or endpoint is published anywhere, the Tako design-system package requires a private npm token issued by email, and the Marketplace runs under signed access-and-use terms. There is no self-serve developer signup, no consumer data-portability API of its own, and no open market data.'
image: https://www.kraken.tech/favicon-96x96.png
layout: provider
mcp_servers:
- description: ''
  name: Kraken Technologies MCP Server
  slug: kraken-technologies-mcp-server
modified: '2026-07-27'
name: Kraken Technologies
nav: Providers
network: true
overview: 'Kraken Technologies publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  Kraken Technologies'' developer surface includes authentication, changelog, documentation, SDKs, engineering blog, support, legal docs, and 27 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 29.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 48.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kraken-technologies/refs/heads/main/screenshots/kraken-technologies-2026-08-07T171335.png
security:
- kind: authentication
  name: Kraken Technologies Authentication
  slug: kraken-technologies-authentication
  summary_line: jwt-bearer/saml/sso · 3 schemes
- kind: domain-security
  name: Kraken Technologies Domain Security
  slug: kraken-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kraken Technologies Vulnerability Disclosure
  slug: kraken-technologies-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kraken Technologies Trust Center
  slug: kraken-technologies-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 1 Type 2, SOC 2 Type 2
slug: kraken-technologies
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Demand Response
- DER
- Billing
- Energy Platform
website: https://www.kraken.tech/
---
