---
access_model:
  confidence: high
  label: Paid membership or per-document purchase · Registry API requires accredited certificate
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.naesb.org/ESPI_Standards.asp
  - https://www.naesb.org//misc/naesb_matl_order_espi_standards.pdf
  - https://www.naesb.org//misc/NAESB_Nonmember_Evaluation.pdf
  - https://www.naesb.org/pdf4/eir_webregistry_technical_guide_v6.1_1018.pdf
  trial: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The NAESB REQ.21 ESPI Model Business Practices define the data exchange protocol for transferring retail energy usage information from a utility (Data Custodian) to a Third Party with the Retail Custo
  name: NAESB REQ.21 Energy Services Provider Interface (ESPI)
  slug: naesb-espi-green-button
- description: 'The NAESB Electric Industry Registry is the central repository of registry information used by the North American wholesale electric industry for electronic tagging; it replaced the NERC TSIN in 2012 '
  name: NAESB Electric Industry Registry (EIR) webRegistry Web Services
  slug: naesb-eir-webregistry
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/naesb-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naesb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.naesb.org/
- group: company
  title: ''
  type: About
  url: https://www.naesb.org/aboutus.asp
- group: operate
  title: ''
  type: ContactUs
  url: https://www.naesb.org/contactus.asp
- group: docs
  title: ''
  type: Documentation
  url: https://www.naesb.org/ESPI_Standards.asp
- group: build
  title: ''
  type: Tools
  url: https://www.naesb.org/naesb_tools.asp
- group: auth
  title: ''
  type: Certification
  url: https://www.naesb.org/materials/certification.asp
- group: other
  title: ''
  type: CertifiedProducts
  url: https://www.naesb.org/pdf2/cert_products.pdf
- group: auth
  title: ''
  type: CertificationAuthorities
  url: https://www.naesb.org/pdf4/ac_authorities_2023.pdf
- group: commercial
  title: ''
  type: Pricing
  url: https://www.naesb.org/pdf/ordrform.pdf
- group: other
  title: ''
  type: Licensing
  url: https://www.naesb.org/copyright.asp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.naesb.org/pdf4/terms&conditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.naesb.org/privacy.asp
- group: other
  title: ''
  type: Membership
  url: https://www.naesb.org/membership.asp
- group: company
  title: ''
  type: Newsletter
  url: https://www.naesb.org/bulletin_newsletter.asp
- group: operate
  title: ''
  type: PressReleases
  url: https://www.naesb.org/news.asp
- group: other
  title: ''
  type: WhitePapers
  url: https://www.naesb.org/white_papers.asp
- group: operate
  title: ''
  type: Support
  url: https://www.naesb.org/contactus.asp
- group: auth
  title: ''
  type: Compliance
  url: https://www.naesb.org/materials/certification.asp
- group: auth
  title: ''
  type: Authentication
  url: authentication/naesb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/naesb-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/naesb-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/naesb-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/naesb-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/naesb-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/naesb-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/naesb-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: 'The North American Energy Standards Board (NAESB) is the non-profit, industry-consensus standards development organization formed in 1994 that writes the business practice standards for the North American wholesale and retail natural gas and electricity markets, organized into four quadrants — Wholesale Electric (WEQ), Retail Electric (REQ), Wholesale Gas (WGQ) and Retail Gas (RGQ). Headquartered in Houston, Texas, its home market is the United States (with Canadian and Mexican participation). NAESB sits upstream of every utility, ISO/RTO and energy-data platform in the value chain: it authors REQ.21 Energy Services Provider Interface (ESPI), the standard that is the basis of every Green Button implementation in North America, and it operates the NAESB Electric Industry Registry (EIR) that underpins electronic tagging across the wholesale electric market. Its API posture is deliberately split and must not be overstated. NAESB is not a data holder and no consumer-data mandate
  applies to it; the Green Button standard it publishes is adopted by US utilities purely voluntarily, with no federal obligation behind it. The specifications themselves are copyright-protected and paywalled — $8,000/year membership, $2,000 per quadrant version, or $250 per individual standard — with only a free, view-only, three-business-day evaluation waiver for non-members. The single genuinely open artifact is the set of ESPI XML schemas, released under Apache 2.0 as a documented one-time exception to the NAESB Copyright Policy and downloadable anonymously after a one-click terms-of-use acknowledgement. The one real API NAESB operates, the EIR webRegistry SOAP service administered by OATI, is closed: it requires a paid registry subscription and a digitally signed X.509 certificate issued by an NAESB-Authorized Certification Authority, and its endpoint could not even complete a TLS handshake anonymously. Open standard schemas, closed standards text, closed registry API, no consumer data
  and no open market data of its own.'
image: https://www.naesb.org/images/naesb-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: NAESB MCP Server
  slug: naesb-mcp-server
modified: '2026-07-27'
name: NAESB
nav: Providers
network: true
overview: 'NAESB publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Standards, Utilities, and Electricity.


  NAESB''s developer surface includes documentation, tooling, pricing, support, authentication, changelog, and 23 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 47.0
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 37.1
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naesb/refs/heads/main/screenshots/naesb-2026-08-07T184604.png
security:
- kind: authentication
  name: Naesb Authentication
  slug: naesb-authentication
  summary_line: mutualTLS/oauth2 · 2 schemes
- kind: domain-security
  name: Naesb Domain Security
  slug: naesb-domain-security
  summary_line: TLSv1.2 · DMARC
slug: naesb
tags:
- Energy
- United States
- Standards
- Utilities
- Electricity
- Gas
- Green Button
- Smart Metering
- Energy Markets
- Grid
website: https://www.naesb.org/
---
