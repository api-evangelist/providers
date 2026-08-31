---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.6
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Open, unauthenticated bulk data files covering every current Australian Airworthiness Directive (AD). combinedadweb.json lists all current ADs with aircraft and equipment references; adweb.csv lists a
  name: CASA Airworthiness Directives Data Files
  slug: casa-airworthiness-directives-data
- description: The complete Australian Civil Aircraft Register published as a daily comma-delimited data file (acrftreg.csv, approximately 7.6MB) and a zip compressed equivalent (acrftreg.zip, approximately 1MB). CA
  name: Australian Civil Aircraft Register Data Files
  slug: casa-aircraft-register-data
- description: A partner-only API that supplies CASA advisories, notifications and geospatial map data to drone safety applications, and processes Automated Airspace Authorisations for Sydney Harbour (R405A/B) and t
  name: CASA RPAS Digital Platform API
  slug: casa-rpas-digital-platform
artifact_total: 12
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/casa-aviation-mcp.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/casa-aviation-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/casa-aviation-aircraft-register-examples.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.casa.gov.au/aircraft/aircraft-registration/data-files-registered-aircraft/downloading-and-using-our-data-files
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casa-aviation-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/casa-aviation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.casa.gov.au/about-us/reporting-and-accountability/external-security-vulnerability-disclosure-program
- group: auth
  title: ''
  type: Authentication
  url: authentication/casa-aviation-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/casa-aviation-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/casa-aviation-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://my.casa.gov.au/outage/
- group: design
  title: ''
  type: Conformance
  url: conformance/casa-aviation-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/casa-aviation-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/casa-aviation-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/casa-aviation-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casa-aviation-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.casa.gov.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.casa.gov.au/aircraft/aircraft-registration/data-files-registered-aircraft
- group: start
  title: ''
  type: Portal
  url: https://my.casa.gov.au/
- group: operate
  title: ''
  type: Support
  url: https://www.casa.gov.au/about-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casa.gov.au/sites/default/files/2021-09/rpas-platform-terms-conditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casa.gov.au/about-us/about-website/privacy-statement
- group: company
  title: ''
  type: Blog
  url: https://www.casa.gov.au/about-us/news-media-releases-and-speeches
- group: company
  title: ''
  type: BlogRSS
  url: https://www.casa.gov.au/rss.xml
- group: operate
  title: ''
  type: Contact
  url: https://www.casa.gov.au/about-us/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civil-aviation-safety-authority-casa-/
- group: learn
  title: ''
  type: YouTube
  url: http://www.youtube.com/user/casabriefing
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CivilAviationSafetyAuthority
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/casabriefing
created: '2026-07-28'
description: 'The Civil Aviation Safety Authority (CASA) is Australia''s independent statutory aviation safety regulator, established under the Civil Aviation Act 1988. It maintains the Australian Civil Aircraft Register (VH- marks), issues Airworthiness Directives, licenses flight crew and maintenance organisations, certifies air operators, and regulates drone and RPAS operations. CASA sits entirely OUTSIDE the travel distribution chain — it is a safety regulator, not a distributor, so it has no GDS, NDC, channel-manager or OTA position, and airline fare distribution, full-content agreements and consumer disclosure are not CASA functions. Its API posture is split and honest: two genuinely open, no-key, documented bulk data products (the full Airworthiness Directives listing as JSON/CSV and the complete civil aircraft register as a daily CSV, both served from services.casa.gov.au), and one approval-gated partner API — the CASA RPAS Digital Platform at data.casa.rpasplatform.net — whose endpoints
  are named in public PDFs but require a service account, a signed four-year agreement, a CASA onboarding check-out and a paid Airservices Australia airspace data licence. There is no self-serve developer portal, no OpenAPI, and new RPAS Platform onboarding is currently paused pending Airservices'' Flight Information Management System.'
examples:
- key_count: 3
  name: Casa Aviation Aircraft Register Examples
  slug: casa-aviation-aircraft-register-examples
- key_count: 3
  name: Casa Aviation Airworthiness Directives Examples
  slug: casa-aviation-airworthiness-directives-examples
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: CASA Airworthiness Directive listing row (adweb.csv) and series row (folder.csv)
  property_count: 0
  slug: casa-aviation-ad-listing-row.schema
- name: Australian Civil Aircraft Register row (acrftreg.csv)
  property_count: 44
  slug: casa-aviation-aircraft-register-row.schema
- name: CASA Airworthiness Directive record (combinedadweb.json)
  property_count: 1
  slug: casa-aviation-airworthiness-directive.schema
layout: provider
mcp_servers:
- description: ''
  name: Civil Aviation Safety Authority (CASA) MCP Server
  slug: civil-aviation-safety-authority-casa-mcp-server
modified: '2026-07-28'
name: Civil Aviation Safety Authority (CASA)
nav: Providers
network: true
overview: 'Civil Aviation Safety Authority (CASA) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Aviation, Airports, and Government.


  Civil Aviation Safety Authority (CASA)''s developer surface includes code examples, getting-started guide, authentication, documentation, developer portal, support, engineering blog, and 23 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 20.0
    developer_ergonomics: 37.5
    discoverability: 74.1
    governance: 8.3
    operational_transparency: 21.1
  previous_composite: 30.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/casa-aviation/refs/heads/main/screenshots/casa-aviation-2026-08-07T163248.png
security:
- kind: authentication
  name: Casa Aviation Authentication
  slug: casa-aviation-authentication
  summary_line: none/service-account · 2 schemes
- kind: domain-security
  name: Casa Aviation Domain Security
  slug: casa-aviation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Casa Aviation Vulnerability Disclosure
  slug: casa-aviation-vulnerability-disclosure
  summary_line: disclosure policy published
slug: casa-aviation
tags:
- Travel
- Australia
- Aviation
- Airports
- Government
- Regulator
- Aviation Safety
- Open Data
- Drones
website: https://www.casa.gov.au/
---
