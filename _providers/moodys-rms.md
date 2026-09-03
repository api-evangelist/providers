---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 460
  human_in_the_loop: 1
  name: Moodys Rms Agentic Access
  operation_count: 780
  slug: moodys-rms-agentic-access
  summary_line: 780 operations · 460 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: A collection of REST APIs that let Intelligent Risk Platform tenants automate portfolio management, underwriting, and risk-transfer workflows across Risk Modeler, UnderwriteIQ, TreatyIQ, ExposureIQ, a
  name: Moody's RMS Platform APIs
  slug: platform-apis
- description: Physical climate risk data delivered as an API so financial-services organizations can build climate applications on the Intelligent Risk Platform. The public developer page documents four product sur
  name: Moody's RMS Climate On Demand API
  slug: climate-on-demand-api
- description: 'A hosted Model Context Protocol server, irp-integration-mcp, released with Intelligent Risk Platform version 2026.07.c on 2026-06-30. It transforms the Platform API specifications, documentation, and '
  name: Moody's RMS Platform MCP Server
  slug: platform-mcp-server
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The AccountV1 API from Moody's RMS — 21 operation(s) for accountv1.
  name: Moody's RMS Account V1 API
  slug: moodys-rms-accountv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The AccountV2 API from Moody's RMS — 21 operation(s) for accountv2.
  name: Moody's RMS Account V2 API
  slug: moodys-rms-accountv2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Aggregate PortfolioV1 API from Moody's RMS — 12 operation(s) for aggregate portfoliov1.
  name: Moody's RMS Aggregate PortfolioV1 API
  slug: moodys-rms-aggregate-portfoliov1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Aggregate PortfolioV2 API from Moody's RMS — 12 operation(s) for aggregate portfoliov2.
  name: Moody's RMS Aggregate PortfolioV2 API
  slug: moodys-rms-aggregate-portfoliov2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Analysis GroupsV1 API from Moody's RMS — 4 operation(s) for analysis groupsv1.
  name: Moody's RMS Analysis GroupsV1 API
  slug: moodys-rms-analysis-groupsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Analysis GroupsV2 API from Moody's RMS — 4 operation(s) for analysis groupsv2.
  name: Moody's RMS Analysis GroupsV2 API
  slug: moodys-rms-analysis-groupsv2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The BranchV1 API from Moody's RMS — 2 operation(s) for branchv1.
  name: Moody's RMS Branch V1 API
  slug: moodys-rms-branchv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The CedantV1 API from Moody's RMS — 2 operation(s) for cedantv1.
  name: Moody's RMS Cedant V1 API
  slug: moodys-rms-cedantv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Client IP API from Moody's RMS — 1 operation(s) for client ip.
  name: Moody's RMS Client IP API
  slug: moodys-rms-client-ip-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Cluster API from Moody's RMS — 5 operation(s) for cluster.
  name: Moody's RMS Cluster API
  slug: moodys-rms-cluster-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: Returns multiple layers for an address, including chaining the output of one layer into the input for another
  name: Moody's RMS Composite API
  slug: moodys-rms-composite-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Databases API from Moody's RMS — 5 operation(s) for databases.
  name: Moody's RMS Databases API
  slug: moodys-rms-databases-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The DatasourcesV1 API from Moody's RMS — 3 operation(s) for datasourcesv1.
  name: Moody's RMS Datasources V1 API
  slug: moodys-rms-datasourcesv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The DatasourcesV2 API from Moody's RMS — 3 operation(s) for datasourcesv2.
  name: Moody's RMS Datasources V2 API
  slug: moodys-rms-datasourcesv2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The DatastoreV1 API from Moody's RMS — 3 operation(s) for datastorev1.
  name: Moody's RMS Datastore V1 API
  slug: moodys-rms-datastorev1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The DatastoreV2 API from Moody's RMS — 3 operation(s) for datastorev2.
  name: Moody's RMS Datastore V2 API
  slug: moodys-rms-datastorev2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The DomainsV1 API from Moody's RMS — 8 operation(s) for domainsv1.
  name: Moody's RMS Domains V1 API
  slug: moodys-rms-domainsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Earthquake Hazard Lookup API from Moody's RMS — 40 operation(s) for earthquake hazard lookup.
  name: Moody's RMS Earthquake Hazard Lookup API
  slug: moodys-rms-earthquake-hazard-lookup-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The ExportsV1 API from Moody's RMS — 2 operation(s) for exportsv1.
  name: Moody's RMS Exports V1 API
  slug: moodys-rms-exportsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The ExportsV2 API from Moody's RMS — 1 operation(s) for exportsv2.
  name: Moody's RMS Exports V2 API
  slug: moodys-rms-exportsv2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Exposure BatchV3 API from Moody's RMS — 1 operation(s) for exposure batchv3.
  name: Moody's RMS Exposure BatchV3 API
  slug: moodys-rms-exposure-batchv3-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Exposure SetsV1 API from Moody's RMS — 3 operation(s) for exposure setsv1.
  name: Moody's RMS Exposure SetsV1 API
  slug: moodys-rms-exposure-setsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The File StorageV1 API from Moody's RMS — 8 operation(s) for file storagev1.
  name: Moody's RMS File StorageV1 API
  slug: moodys-rms-file-storagev1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: Geocodes an address
  name: Moody's RMS Geocoding API
  slug: moodys-rms-geocoding-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Import Upload API from Moody's RMS — 3 operation(s) for import upload.
  name: Moody's RMS Import Upload API
  slug: moodys-rms-import-upload-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The ImportsV1 API from Moody's RMS — 6 operation(s) for importsv1.
  name: Moody's RMS Imports V1 API
  slug: moodys-rms-importsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Jobs API from Moody's RMS — 2 operation(s) for jobs.
  name: Moody's RMS Jobs API
  slug: moodys-rms-jobs-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Line of BusinessV1 API from Moody's RMS — 2 operation(s) for line of businessv1.
  name: Moody's RMS Line of BusinessV1 API
  slug: moodys-rms-line-of-businessv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The LocationV1 API from Moody's RMS — 30 operation(s) for locationv1.
  name: Moody's RMS Location V1 API
  slug: moodys-rms-locationv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Logins API from Moody's RMS — 2 operation(s) for logins.
  name: Moody's RMS Logins API
  slug: moodys-rms-logins-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The MetricsV1 API from Moody's RMS — 24 operation(s) for metricsv1.
  name: Moody's RMS Metrics V1 API
  slug: moodys-rms-metricsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The MetricsV2 API from Moody's RMS — 27 operation(s) for metricsv2.
  name: Moody's RMS Metrics V2 API
  slug: moodys-rms-metricsv2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The PateV1 API from Moody's RMS — 2 operation(s) for patev1.
  name: Moody's RMS Pate V1 API
  slug: moodys-rms-patev1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Policy ConditionV1 API from Moody's RMS — 1 operation(s) for policy conditionv1.
  name: Moody's RMS Policy ConditionV1 API
  slug: moodys-rms-policy-conditionv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The PolicyV1 API from Moody's RMS — 15 operation(s) for policyv1.
  name: Moody's RMS Policy V1 API
  slug: moodys-rms-policyv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The PortfolioV1 API from Moody's RMS — 16 operation(s) for portfoliov1.
  name: Moody's RMS Portfolio V1 API
  slug: moodys-rms-portfoliov1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The PortfolioV2 API from Moody's RMS — 16 operation(s) for portfoliov2.
  name: Moody's RMS Portfolio V2 API
  slug: moodys-rms-portfoliov2-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The ProducerV1 API from Moody's RMS — 2 operation(s) for producerv1.
  name: Moody's RMS Producer V1 API
  slug: moodys-rms-producerv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The ReportsV1 API from Moody's RMS — 2 operation(s) for reportsv1.
  name: Moody's RMS Reports V1 API
  slug: moodys-rms-reportsv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: Returns one exposure, hazard, risk score, or loss cost layer for an address
  name: Moody's RMS Risk Lookups API
  slug: moodys-rms-risk-lookups-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Server Instances API from Moody's RMS — 3 operation(s) for server instances.
  name: Moody's RMS Server Instances API
  slug: moodys-rms-server-instances-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Step PolicyV1 API from Moody's RMS — 3 operation(s) for step policyv1.
  name: Moody's RMS Step PolicyV1 API
  slug: moodys-rms-step-policyv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The TreatyV1 API from Moody's RMS — 11 operation(s) for treatyv1.
  name: Moody's RMS Treaty V1 API
  slug: moodys-rms-treatyv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The UnderwriterV1 API from Moody's RMS — 2 operation(s) for underwriterv1.
  name: Moody's RMS Underwriter V1 API
  slug: moodys-rms-underwriterv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The UtilityV1 API from Moody's RMS — 6 operation(s) for utilityv1.
  name: Moody's RMS Utility V1 API
  slug: moodys-rms-utilityv1-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The Windstorm Hazard Lookup API from Moody's RMS — 14 operation(s) for windstorm hazard lookup.
  name: Moody's RMS Windstorm Hazard Lookup API
  slug: moodys-rms-windstorm-hazard-lookup-api
- baseURL: https://api-use1.rms.com/platform
  baseurl_source: declared
  description: The WorkflowsV1 API from Moody's RMS — 2 operation(s) for workflowsv1.
  name: Moody's RMS Workflows V1 API
  slug: moodys-rms-workflowsv1-api
artifact_total: 56
collections:
- collection_type: open
  name: Data Bridge
  slug: open-moodys-rms-data-bridge
- collection_type: open
  name: Risk Modeler
  slug: open-moodys-rms-risk-modeler
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/moodys/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/moodys-rms-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moodys-rms-risk-modeler-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moodys-rms-data-bridge-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moodys-rms-location-intelligence-overlay.yaml
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
- description: A service that securely connects a tenant's AI applications with the Intelligent Risk Platform and developer resources. The Platform MCP Server transforms Platform API specifications, documentation, a
  name: Moody's RMS MCP Server
  slug: moodys-rms-mcp-server
modified: '2026-07-25'
name: Moody's RMS
nav: Providers
network: true
overview: 'Moody''s RMS publishes 49 APIs on the [APIs.io](https://apis.io/) network, including Platform APIs, Climate On Demand API, Account V1 API, and 46 more. Tagged areas include Insurance, United States, Property and Casualty, Reinsurance, and Risk Data.


  Moody''s RMS''s developer surface includes changelog, getting-started guide, support, authentication, documentation, API reference, and 26 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 41.1
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 14.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moodys-rms/refs/heads/main/screenshots/moodys-rms-2026-08-07T184230.png
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
