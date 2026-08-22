---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uk Caa Agentic Access
  operation_count: 2
  slug: uk-caa-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The Citizen Space (Delib) public consultation API deployed on the CAA's consultations domain. Two documented methods — json_search_results and json_consultation_details — return published CAA consulta
  name: CAA Consultations API
  slug: caa-consultations-api
arazzos:
- description: Search the UK Civil Aviation Authority's published consultation activities, then pull the full detail record for the first match.
  name: Track UK CAA consultations
  slug: uk-caa-track-consultations
artifact_total: 13
collections:
- collection_type: open
  name: CAA Consultations API (Citizen Space 2.4)
  slug: open-uk-caa-consultations-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uk-caa-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uk-caa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uk-caa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uk-caa-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.caa.co.uk/website-policies/vulnerability-disclosure-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uk-caa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/uk-caa-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uk-caa-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uk-caa-atol-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/uk-caa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uk-caa-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uk-caa-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uk-caa-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uk-caa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uk-caa-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uk-caa-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uk-caa-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/uk-caa-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/uk-caa-track-consultations.yml
- group: company
  title: ''
  type: Website
  url: https://www.caa.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.caa.co.uk/data-and-analysis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.caa.co.uk/publications/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.caa.co.uk/aircraft-register/g-info/g-info-forms-and-fees/
- group: company
  title: ''
  type: Blog
  url: https://www.caa.co.uk/newsroom/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civil-aviation-authority
- group: other
  title: ''
  type: X
  url: https://x.com/UK_CAA
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/UKCAA
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/uk.caa
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.caa.co.uk/website-policies/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.caa.co.uk/.well-known/security.txt
- group: start
  title: ''
  type: CustomerPortal
  url: https://portal.caa.co.uk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caa.co.uk/about-us/the-civil-aviation-authority/general-privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.caa.co.uk/about-us/information-requests/contact-us/
- group: other
  title: ''
  type: Accessibility
  url: https://www.caa.co.uk/website-policies/accessibility-statement/
- group: start
  title: ''
  type: Registry
  url: https://www.caa.co.uk/aircraft-register/g-info/search-g-info/
- group: start
  title: ''
  type: Registry
  url: https://www.caa.co.uk/atol-protection/check-an-atol/search-atol-holders/
- group: other
  title: ''
  type: Dataset
  url: https://www.caa.co.uk/data-and-analysis/uk-aviation-market/airports/uk-airport-data/
- group: other
  title: ''
  type: Dataset
  url: https://www.caa.co.uk/data-and-analysis/uk-aviation-market/flight-punctuality/uk-flight-punctuality-statistics/
- group: other
  title: ''
  type: Dataset
  url: https://www.caa.co.uk/atol-protection/check-an-atol/atol-reports/
- group: other
  title: ''
  type: Dataset
  url: https://ckan.publishing.service.gov.uk/api/3/action/organization_show?id=civil-aviation-authority
- group: commercial
  title: ''
  type: Legal
  url: https://www.caa.co.uk/atol-protection/atol-requirements-for-the-travel-industry/do-i-need-an-atol/
- group: commercial
  title: ''
  type: Legal
  url: https://www.caa.co.uk/atol-protection/atol-compliance/requirements-legal-obligations/airline-ticket-agents/
- group: commercial
  title: ''
  type: Legal
  url: https://www.caa.co.uk/about-us/information-requests/accessing-information-held-by-the-caa/
created: '2026-07-28'
description: 'The UK Civil Aviation Authority (CAA) is the United Kingdom''s independent aviation regulator and a public corporation of the Department for Transport. It licenses UK airlines, registers UK civil aircraft on the G-INFO register, regulates airspace and airports, economically regulates Heathrow and Gatwick, enforces UK air passenger rights, and — the part that matters most to travel distribution — runs the Air Travel Organiser''s Licence (ATOL) scheme, which is the statutory gate every business selling flight-inclusive packages to UK consumers must pass through, including sellers established outside the UK. The CAA sits above the distribution chain rather than inside it: it does not distribute inventory, does not operate a GDS or NDC connection, and has no NDC posture of its own. Its API posture is thin and honest to record — there is no developer portal, no OpenAPI, and no published aviation data API. The only documented, self-serve, key-free public API on a CAA domain is the
  Citizen Space (Delib) consultation API at consultations.caa.co.uk/api, a vendor platform API rather than an aviation data API. The aviation surfaces that do exist — the G-INFO aircraft register search and the Check an ATOL search — are undocumented ASP.NET JSON backends whose CORS policy is locked to www.caa.co.uk and which are reCAPTCHA-gated. Bulk aviation data is delivered as CSV, PDF and XLSX files behind opaque GUID download URLs, and the full G-INFO aircraft register is a paid subscription emailed as an MS Excel file licensed for use on a single PC. Home market is the United Kingdom.'
examples:
- key_count: 31
  name: Uk Caa Json Consultation Details All
  slug: uk-caa-json-consultation-details-all
image: https://www.caa.co.uk/apple-touch-icon.png
json_schemas:
- name: Consultation activity
  property_count: 32
  slug: uk-caa-activity
- name: RelatedLink
  property_count: 2
  slug: uk-caa-related-link
- name: SupportingDocument
  property_count: 3
  slug: uk-caa-supporting-document
- name: Term
  property_count: 2
  slug: uk-caa-term
layout: provider
mcp_servers:
- description: ''
  name: uk-caa-mcp.yml
  slug: uk-caa-mcpyml
modified: '2026-07-28'
name: UK Civil Aviation Authority
nav: Providers
network: true
overview: 'UK Civil Aviation Authority publishes 1 API on the [APIs.io](https://apis.io/) network: CAA Consultations API. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Airports.


  UK Civil Aviation Authority''s developer surface includes authentication, changelog, documentation, pricing, engineering blog, YouTube channel, support, and 37 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 44.3
  delta: 2.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 20.5
    contract_quality: 60.8
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 20.5
    operational_transparency: 26.3
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Uk Caa Authentication
  slug: uk-caa-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Uk Caa Domain Security
  slug: uk-caa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uk Caa Vulnerability Disclosure
  slug: uk-caa-vulnerability-disclosure
  summary_line: security.txt
slug: uk-caa
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Airports
- Regulator
- Government
- Distribution
- Consumer Protection
- Open Data
website: https://www.caa.co.uk/
---
