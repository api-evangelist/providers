---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: 'The first-party gRPC/ProtoBuf interface Picarro publishes for external access to Picarro SAM (semiconductor airborne molecular contamination) systems. The `picarro-edge` server exposes three services '
  name: Picarro Edge — SAM FOUP gRPC API
  slug: picarro-edge-sam-foup-grpc-api
- description: The gRPC interface to the host computer underneath a Picarro SAM deployment. `platformserver` exposes NetConfig for network connectivity and Wi-Fi management, SysConfig for product/version information
  name: Picarro Platform Server API
  slug: picarro-platform-server-api
- description: The Keycloak-backed identity service that fronts the Picarro P-Cubed cloud platform. It publishes an anonymous OpenID Connect discovery document for the `picarro` realm, advertising the authorization,
  name: Picarro Identity (P-Cubed SSO)
  slug: picarro-identity-p-cubed-sso
- description: P-Cubed is Picarro's cloud data processing and storage platform. Picarro analyzers stream or batch data to it, customers interact with the results in a graphics-rich web environment, and — per Picarro
  name: Picarro P-Cubed Platform
  slug: picarro-p-cubed-platform
artifact_total: 9
asyncapis:
- description: 'Picarro Edge implements a publish/subscribe surface on top of gRPC server streaming: every service exposes a `watch(picarro.signal.Filter)` method that returns a stream of `Signal` messages, where the'
  name: Picarro Edge — SAM FOUP Signal Streams
  slug: picarro-sam-foup-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picarro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.picarro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/picarro/sam-foup-public/blob/master/README.md
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/picarro/sam-foup-public/tree/master/proto
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/picarro/sam-foup-public/blob/master/README.md#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/picarro
- group: operate
  title: ''
  type: Support
  url: https://www.picarro.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.picarro.com/support/caseform
- group: operate
  title: ''
  type: Community
  url: https://www.picarro.com/support/community
- group: company
  title: ''
  type: Blog
  url: https://www.picarro.com/company/press_releases
- group: start
  title: ''
  type: SignUp
  url: https://www.picarro.com/user/register
- group: start
  title: ''
  type: Login
  url: https://www.picarro.com/user/login
- group: commercial
  title: ''
  type: Pricing
  url: https://store.picarro.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.picarro.com/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.picarro.com/privacy_policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.picarro.com/ensuring_data_security_and_compliance
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.picarro.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.picarro.com/status/gas
- group: operate
  title: ''
  type: Contact
  url: https://www.picarro.com/company/contact_us
- group: other
  title: ''
  type: Resources
  url: https://www.picarro.com/resources/library
- group: other
  title: ''
  type: SoftwareDownloads
  url: https://www.picarro.com/software_downloads
- group: company
  title: ''
  type: Careers
  url: https://www.picarro.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.picarro.com/partners
- group: build
  title: ''
  type: Packages
  url: packages/picarro-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/picarro-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/picarro-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/picarro-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/picarro-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/picarro-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/picarro-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/picarro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/picarro-problem-types.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/picarro-sam-foup-asyncapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/picarro-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/picarro-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/picarro-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/picarro-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/picarro-tool-crosswalk.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/picarro-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/picarro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/picarro-run-foup-measurement.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/picarro-manage-measurement-sets.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/picarro-monitor-analyzer-health.md
created: '2026-08-02'
description: Picarro, Inc. is a Santa Clara, California company that builds high-precision gas concentration and stable-isotope analyzers based on Cavity Ring-Down Spectroscopy (CRDS), together with the cloud software and mobile platforms that turn those measurements into operational decisions. Its instruments measure more than 700 compounds — methane, ethane, CO2, N2O, ammonia, ethylene oxide, hydrogen peroxide, water isotopes and cleanroom-level airborne molecular contamination — at parts-per- billion and parts-per-trillion sensitivity. Picarro serves natural gas utilities (mobile methane leak detection and the Picarro Surveyor programme), sterilization and EtO facilities, refinery and chemical-plant fenceline monitoring, semiconductor cleanrooms and FOUP contamination control, pharmaceutical manufacturing, and atmospheric and earth-science research. The company reports 25+ years of operation, 5,000+ instruments installed in about 100 countries, and 77 patents. Its software side is P-Cubed,
  a cloud data-processing and storage platform with a customer-facing API for custom data transformation routines, a companion mobile app for field leak investigations, and — for semiconductor deployments — a publicly published gRPC/ProtoBuf interface (picarro/sam-foup-public) for external control and monitoring of Picarro Edge systems.
image: https://www.picarro.com/sites/default/files/picarro_logo.png
layout: provider
modified: '2026-08-02'
name: Picarro
nav: Providers
network: true
overview: 'Picarro publishes 1 API on the [APIs.io](https://apis.io/) network: Edge — SAM FOUP gRPC API. Tagged areas include Company, Gas Detection, Environmental Monitoring, Emissions, and Methane.


  The Picarro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Picarro''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 37 more developer resources.'
random_paper: 87
scopes:
- name: Picarro Scopes
  scope_count: 9
  slug: picarro-scopes
  summary_line: 9 scopes · authorizationCode/implicit/password/clientCredentials
score:
  band: developing
  composite: 50.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.4
    developer_ergonomics: 64.7
    discoverability: 83.3
    governance: 3.1
    operational_transparency: 36.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Picarro Authentication
  slug: picarro-authentication
  summary_line: openIdConnect/oauth2/saml2/none · 3 schemes
- kind: domain-security
  name: Picarro Domain Security
  slug: picarro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Picarro Trust Center
  slug: picarro-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017, ISO/IEC 27018, SOC 2 Type 2, ISO 9001:2015
slug: picarro
tags:
- Company
- Gas Detection
- Environmental Monitoring
- Emissions
- Methane
- Greenhouse Gas
- Scientific Instruments
- Semiconductor
- Industrial IoT
- Sensors
- Analytics
- gRPC
website: https://www.picarro.com/
---
