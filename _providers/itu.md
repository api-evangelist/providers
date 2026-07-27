---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Itu Agentic Access
  operation_count: 20
  slug: itu-agentic-access
  summary_line: 20 operations · 2 acting
api_count: 2
apis:
- description: The undocumented JSON API that serves the ITU DataHub (datahub.itu.int), ITU's official ICT statistics portal and the successor to ICT Eye. Confirmed anonymously callable on 2026-07-25 with no key, he
  name: ITU DataHub API
  slug: itu-datahub-api
- description: An ITU-D Technology and Network Development API that scores a batch of coordinates against the ITU Interactive Transmission Map (Broadband Maps) fibre network data. Two routes are published on the ITU
  name: ITU Proximity to Fibre Node API
  slug: itu-proximity-to-fibre-node-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/itu-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itu-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itu-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/itu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/itu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/itu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/itu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/itu-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/itu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/itu-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/itu-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://bbmaps.itu.int/llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.itu.int/
- group: docs
  title: ''
  type: Documentation
  url: https://www.itu.int/en/ITU-T/publications/Pages/recs.aspx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ITUINT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itu
- group: company
  title: ''
  type: Blog
  url: https://www.itu.int/hub/
- group: operate
  title: ''
  type: Support
  url: https://www.itu.int/home/contact/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itu.int/en/about/Pages/terms-of-use.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itu.int/en/about/Pages/privacy-notice.aspx
created: '2026-07-25'
description: 'The International Telecommunication Union (ITU) is the United Nations specialized agency for information and communication technologies, headquartered in Geneva and made up of 194 Member States plus roughly 1,000 sector members. It sits at the top of the global telecom value chain rather than inside it: ITU-R allocates the global radio spectrum and manages the master international frequency register and satellite filings, ITU-T publishes the Recommendations that define interoperable telecom networks, and ITU-D collects and publishes the world''s reference ICT statistics. Its market is Global by treaty. Its API posture is genuinely open but entirely undeclared: ITU operates real, anonymously callable HTTP APIs behind the DataHub statistics portal and behind an ITU-D "Proximity to Fibre Node" demonstration built on the ITU Broadband Maps, and neither requires a key, a login, or a partner agreement — but there is no developer portal, no api.itu.int, no published OpenAPI, no SDK,
  no terms of programmatic use, and the official ITU GitHub organization has zero public repositories. ITU is not a CAMARA participant and not a GSMA Open Gateway operator; network APIs are being standardised outside the UN system, and ITU''s role in that layer is limited to the IMT requirements framework rather than any callable interface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: itu-mcp.yml
  slug: itu-mcpyml
modified: '2026-07-26'
name: ITU
nav: Providers
network: true
overview: 'ITU publishes 2 APIs on the [APIs.io](https://apis.io/) network: DataHub API and Proximity to Fibre Node API. Tagged areas include Telecommunications, Global, Regulator, Standards, and Spectrum.


  ITU''s developer surface includes authentication, code examples, documentation, engineering blog, support, and 17 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.8
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.7
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Itu Authentication
  slug: itu-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Itu Domain Security
  slug: itu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: itu
tags:
- Telecommunications
- Global
- Regulator
- Standards
- Spectrum
- Satellite
- Broadband
- ICT Statistics
- Open Data
- United Nations
website: https://www.itu.int/
---
