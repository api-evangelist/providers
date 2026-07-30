---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 460
  human_in_the_loop: 1
  name: Moodys Rms Agentic Access
  operation_count: 780
  slug: moodys-rms-agentic-access
  summary_line: 780 operations · 460 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: A collection of REST APIs that let Intelligent Risk Platform tenants automate portfolio management, underwriting, and risk-transfer workflows across Risk Modeler, UnderwriteIQ, TreatyIQ, ExposureIQ, a
  name: Moody's RMS Platform APIs
  slug: platform-apis
- description: The Risk Modeler 2.0 public API — the legacy catastrophe-modeling and underwriting surface of the Intelligent Risk Platform, superseded by the Platform APIs but still documented and specified. The har
  name: Moody's RMS Risk Modeler API
  slug: risk-modeler-api
- description: Administers database connections and moves exposure and results data into and out of the Intelligent Risk Platform. The harvested OpenAPI 3.0.1 definition carries 21 paths covering database and server
  name: Moody's RMS Data Bridge API
  slug: data-bridge-api
- description: Address geocoding and per-location peril and hazard risk lookups used to enrich exposure before modeling. The harvested OpenAPI 3.0.1 definition carries 366 paths under three declared tags — Geocoding
  name: Moody's RMS Location Intelligence API
  slug: location-intelligence-api
- description: Physical climate risk data delivered as an API so financial-services organizations can build climate applications on the Intelligent Risk Platform. The public developer page documents four product sur
  name: Moody's RMS Climate On Demand API
  slug: climate-on-demand-api
- description: 'A hosted Model Context Protocol server, irp-integration-mcp, released with Intelligent Risk Platform version 2026.07.c on 2026-06-30. It transforms the Platform API specifications, documentation, and '
  name: Moody's RMS Platform MCP Server
  slug: platform-mcp-server
artifact_total: 10
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moodys-rms-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/moodys-rms-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/moodys-rms-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moodys-rms-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moodys-rms-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moodys-rms-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rms.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.rms.com/platform/docs/policies
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moodys-rms-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moodys-rms-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moodys-rms-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moodys-rms-llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rms.com/platform/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://support.rms.com/o/html-doc/OLH_Content/SCGuide_Help_Center/Content/SCGuide/Welcome.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moodys.com/web/en/us/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moodys.com/web/en/us/legal/privacy-policy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/rms-developers/rms-developers/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moodys-rms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moodys-rms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moodys-rms-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.moodys.com/web/en/us/who-we-serve/insurance.html
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rms.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rms.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RMS
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/rms-developers/rms-developers/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rms.com/platform/reference
created: '2026-07-25'
description: 'Moody''s RMS is the catastrophe risk modeling and risk-data business of Moody''s Corporation, headquartered in Newark, California in its home market of the United States and serving property and casualty insurers, reinsurers, brokers, and capital-market participants worldwide. Founded at Stanford in 1988 as Risk Management Solutions and acquired by Moody''s in 2021, the company sells peril models (hurricane, earthquake, flood, wildfire, severe convective storm, terror, cyber, pandemic) and the exposure data infrastructure that carriers use to price, accumulate, and transfer catastrophe risk. Its products run on the cloud-native Intelligent Risk Platform, which fronts Risk Modeler, ExposureIQ, UnderwriteIQ, TreatyIQ, and Risk Data Exchange. Unlike most of the US insurance sector, Moody''s RMS is genuinely API-forward: it operates a public, self-serve ReadMe developer portal at developer.rms.com covering Platform APIs, Risk Modeler, Data Bridge, Location Intelligence, and Climate
  On Demand, publishes downloadable OpenAPI 3.0 definitions and public Postman collections from its own rms-developers GitHub repository, and exposes live REST hosts at api-use1.rms.com and api-euw1.rms.com. Reference documentation is readable without a login, but the APIs themselves are tenant-scoped: keys are issued only to licensed Intelligent Risk Platform tenants, so there is no self-serve signup and no sandbox. Its data-standards posture is cat-risk rather than ACORD — the exchange formats are the RMS EDM/RDM databases, the Risk Data Open Standard (RDOS), and interoperability with CEDE and OED; ACORD appears only as a geocoding-resolution code mapping inside the Location Intelligence API. These are risk-data and analytics APIs, not policy APIs: no quote, bind, issue, or FNOL surface is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: moodys-rms-mcp.yml
  slug: moodys-rms-mcpyml
modified: '2026-07-25'
name: Moody's RMS
nav: Providers
network: true
overview: 'Moody''s RMS publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Platform APIs, Risk Modeler API, Data Bridge API, and 2 more. Tagged areas include Insurance, United States, Property and Casualty, Reinsurance, and Risk Data.


  Moody''s RMS''s developer surface includes changelog, getting-started guide, support, authentication, documentation, API reference, and 21 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 41.6
  delta: -2.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 38.5
    developer_ergonomics: 64.7
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moodys Rms Authentication
  slug: moodys-rms-authentication
  summary_line: apiKey/accessToken · 1 scheme
- kind: domain-security
  name: Moodys Rms Domain Security
  slug: moodys-rms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moodys-rms
tags:
- Insurance
- United States
- Property and Casualty
- Reinsurance
- Risk Data
- Catastrophe Modeling
- Underwriting
- Climate Risk
- Geocoding
- Analytics
website: https://www.moodys.com/web/en/us/who-we-serve/insurance.html
---
