---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Dcc Smart Agentic Access
  operation_count: 2
  slug: dcc-smart-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: An open-source HTTP API published by Smart DCC Limited for signing and validating DUIS (DCC User Interface Specification) XML messages. Two operations — POST /sign adds an XML digital signature to a B
  name: DCC Boxed DUIS Signing Tool API
  slug: dcc-boxed-duis-signing-tool-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dcc-smart-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SmartDCCInnovation/dccboxed-signing-tool/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/SmartDCCInnovation/dccboxed-signing-tool/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dcc-smart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dcc-smart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.smartdcc.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.smartdcc.co.uk/about-dcc/
- group: operate
  title: ''
  type: Contact
  url: https://www.smartdcc.co.uk/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.smartdcc.co.uk/news-events/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SmartDCCInnovation
- group: docs
  title: ''
  type: Documentation
  url: https://www.smartdcc.co.uk/document-centre/
- group: start
  title: ''
  type: Onboarding
  url: https://www.smartdcc.co.uk/partner-with-the-dcc/
- group: docs
  title: ''
  type: Specification
  url: https://www.smartdcc.co.uk/media/d5kh4khf/dcc-user-interface-specification-v53-18-mar-2025.pdf
- group: docs
  title: ''
  type: Specification
  url: https://smartenergycodecompany.co.uk/documents/sec-subsidiary-documents/sec-appendix-ad-dcc-user-interface-specification-duis/
- group: docs
  title: ''
  type: Specification
  url: https://smartenergycodecompany.co.uk/documents/sec-subsidiary-documents/sec-appendix-ae-dcc-user-interface-code-of-connection/
- group: docs
  title: ''
  type: Schema
  url: https://www.smartdcc.co.uk/media/6490/duis-xml-schema-v51.docx
- group: other
  title: ''
  type: Dashboard
  url: https://www.smartdcc.co.uk/our-smart-network/network-data-dashboard/
- group: other
  title: ''
  type: Products
  url: https://www.smartdcc.co.uk/our-smart-network/network-products-services/dcc-boxed/
- group: other
  title: ''
  type: Regulation
  url: https://smartenergycodecompany.co.uk/the-smart-energy-code/
- group: build
  title: ''
  type: Packages
  url: packages/dcc-smart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dcc-smart-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dcc-smart-cli.yml
- group: design
  title: ''
  type: Components
  url: components/dcc-smart-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dcc-smart-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dcc-smart-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.smartdcc.co.uk/about-dcc/governance-regulations/governance-reports-policies/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dcc-smart-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.smartdcc.co.uk/our-smart-network/network-data-dashboard/performance/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dcc-smart-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/SmartDCCInnovation/dccboxed-signing-tool/releases
- group: operate
  title: ''
  type: Roadmap
  url: https://www.smartdcc.co.uk/our-smart-network/network-updates/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dcc-smart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.smartdcc.co.uk/media/sn5dn4hr/information-security-policy-3.pdf
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dcc-smart-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dcc-smart-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dcc-smart-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/dcc-smart-dccboxed-keystore-schema.json
- group: operate
  title: ''
  type: Support
  url: https://www.smartdcc.co.uk/contact-us-service-users/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.smartdcc.co.uk/privacy-notice/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smartdcc.co.uk/about-dcc/governance-regulations/charges/
created: '2026-07-27'
description: Smart DCC (the Data Communications Company) is the Ofgem-licensed monopoly that operates Britain's national smart metering communications network, connecting electricity and gas smart meters in homes and businesses to energy suppliers, network operators and other authorised users over a single secure wide-area network. It sits in the middle of the United Kingdom energy value chain as shared infrastructure rather than as a retailer or a data marketplace, and it is regulated through the Smart Meter Communication Licence and governed by the Smart Energy Code. Its API posture reflects that position exactly. Britain mandated the infrastructure, not a consumer data right — there is no UK equivalent of the Australian Consumer Data Right for energy, so Smart DCC operates no consumer data-portability API and publishes no Green Button or Consumer Data Standards surface. The real production interface is the DCC User Interface Specification (DUIS), an XML web service reached over a DCC
  User Gateway Connection, plus the Self-Service Interface; the DUIS specification and its XML schema are published openly as Smart Energy Code subsidiary documents, but the gateway itself is closed to anyone who has not acceded to the Smart Energy Code and passed SMKI and User Entry Process Testing. The only self-serve, machine-readable contract Smart DCC publishes is an OpenAPI for the open-source DCC Boxed DUIS signing and validation tool on GitHub. Network statistics are shown on a public dashboard as a rendered web page with no documented open data API or bulk download, so both the consumer-data and market-data sides are effectively closed while the interface specification itself is open.
image: https://www.smartdcc.co.uk/assets/images/favicon.ico
json_schemas:
- name: Dcc Smart Dccboxed Keystore
  property_count: 0
  slug: dcc-smart-dccboxed-keystore
layout: provider
mcp_servers:
- description: ''
  name: dcc-smart-mcp.yml
  slug: dcc-smart-mcpyml
modified: '2026-07-27'
name: Smart DCC
nav: Providers
network: true
overview: 'Smart DCC publishes 1 API on the [APIs.io](https://apis.io/) network: DCC Boxed DUIS Signing Tool API. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  Smart DCC''s developer surface includes engineering blog, documentation, CLI, sandbox, changelog, support, pricing, and 33 more developer resources.'
random_paper: 82
score:
  band: thin
  composite: 41.0
  delta: -3.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 37.0
    discoverability: 66.7
    governance: 23.4
    operational_transparency: 52.6
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dcc-smart/refs/heads/main/screenshots/dcc-smart-2026-08-07T164213.png
security:
- kind: authentication
  name: Dcc Smart Authentication
  slug: dcc-smart-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dcc Smart Domain Security
  slug: dcc-smart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dcc Smart Vulnerability Disclosure
  slug: dcc-smart-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: dcc-smart
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Grid
- Metering Infrastructure
- Energy Data
website: https://www.smartdcc.co.uk/
---
