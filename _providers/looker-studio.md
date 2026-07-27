---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Looker Studio Agentic Access
  operation_count: 18
  slug: looker-studio-agentic-access
  summary_line: 18 operations · 10 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Operations for searching and managing Looker Studio assets (reports and data sources).
  name: Looker Studio Assets API
  slug: looker-studio-assets-api
- description: Operations for managing third-party authentication including OAuth2, API keys, and username/password credentials.
  name: Looker Studio Authentication API
  slug: looker-studio-authentication-api
- description: Operations related to connector configuration, including user-configurable options and authentication setup.
  name: Looker Studio Configuration API
  slug: looker-studio-configuration-api
- description: Operations for fetching data from the external source and returning it to Looker Studio.
  name: Looker Studio Data API
  slug: looker-studio-data-api
- description: Operations for embedding Looker Studio reports in external applications and websites.
  name: Looker Studio Embed API
  slug: looker-studio-embed-api
- description: Operations related to the visualization manifest configuration that defines how a visualization is discovered and loaded.
  name: Looker Studio Manifest API
  slug: looker-studio-manifest-api
- description: oEmbed-compatible endpoint for platforms that support the oEmbed standard.
  name: Looker Studio oEmbed API
  slug: looker-studio-oembed-api
- description: Operations for managing asset permissions including getting, updating, adding, and revoking member access.
  name: Looker Studio Permissions API
  slug: looker-studio-permissions-api
- description: Operations for creating and configuring linked Looker Studio reports.
  name: Looker Studio Reports API
  slug: looker-studio-reports-api
- description: Operations for defining the data structure and field definitions returned by the connector.
  name: Looker Studio Schema API
  slug: looker-studio-schema-api
- description: Operations for loading and rendering community visualizations in Looker Studio reports.
  name: Looker Studio Visualization API
  slug: looker-studio-visualization-api
artifact_total: 62
collections:
- collection_type: open
  name: Looker Studio API
  slug: open-looker-studio-api
- collection_type: open
  name: Looker Studio Community Connector API
  slug: open-looker-studio-community-connector-api
- collection_type: open
  name: Looker Studio Community Visualization API
  slug: open-looker-studio-community-visualization-api
- collection_type: open
  name: Looker Studio Embedding API
  slug: open-looker-studio-embedding-api
- collection_type: open
  name: Looker Studio Linking API
  slug: open-looker-studio-linking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/looker-studio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/looker-studio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/looker-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/looker-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/looker-studio-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.google.com/looker/docs/studio
- group: start
  title: ''
  type: GettingStarted
  url: https://support.google.com/looker-studio/answer/6283323
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/data-analytics
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/looker/docs/studio/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/looker-open-source
- group: operate
  title: ''
  type: Community
  url: https://www.googlecloudcommunity.com/gc/Looker-Looker-Studio/ct-p/looker
- group: company
  title: ''
  type: Website
  url: https://lookerstudio.google.com
- group: start
  title: ''
  type: Login
  url: https://lookerstudio.google.com/?requirelogin=1
- group: start
  title: ''
  type: Signup
  url: https://lookerstudio.google.com
- group: commercial
  title: ''
  type: Pricing
  url: https://support.google.com/looker-studio/answer/9171315
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.cloud.google.com/looker-studio/docs/release-notes
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.google.com/looker-studio/api/errors
- group: operate
  title: ''
  type: Developer Forum
  url: https://discuss.google.dev/c/looker/looker-q-a/looker-studio/214
- group: other
  title: ''
  type: Developers
  url: https://developers.google.com/looker-studio
- group: other
  title: ''
  type: Publishing
  url: https://developers.google.com/looker-studio/integrate
created: '2024-01-15'
description: Looker Studio (formerly Google Data Studio) is a free tool that turns your data into informative, easy to read, easy to share, and fully customizable dashboards and reports. The API allows developers to programmatically manage assets, build custom connectors and visualizations, embed reports, and automate workflows.
finops:
- name: Looker Studio Finops
  service_category: Business Intelligence
  slug: looker-studio-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg
json_schemas:
- name: AddMembersRequest
  property_count: 2
  slug: looker-studio-addmembersrequest
- name: Looker Studio Asset
  property_count: 11
  slug: looker-studio-asset
- name: AssetType
  property_count: 0
  slug: looker-studio-assettype
- name: AuthType
  property_count: 0
  slug: looker-studio-authtype
- name: AuthTypeResponse
  property_count: 2
  slug: looker-studio-authtyperesponse
- name: ConfigParam
  property_count: 7
  slug: looker-studio-configparam
- name: Looker Studio Community Connector
  property_count: 13
  slug: looker-studio-connector
- name: Looker Studio Data Source
  property_count: 9
  slug: looker-studio-data-source
- name: DataConfig
  property_count: 3
  slug: looker-studio-dataconfig
- name: DimensionFilter
  property_count: 4
  slug: looker-studio-dimensionfilter
- name: Error
  property_count: 1
  slug: looker-studio-error
- name: Field
  property_count: 10
  slug: looker-studio-field
- name: FieldSemantics
  property_count: 4
  slug: looker-studio-fieldsemantics
- name: GetConfigRequest
  property_count: 2
  slug: looker-studio-getconfigrequest
- name: GetConfigResponse
  property_count: 3
  slug: looker-studio-getconfigresponse
- name: GetDataRequest
  property_count: 4
  slug: looker-studio-getdatarequest
- name: GetDataResponse
  property_count: 3
  slug: looker-studio-getdataresponse
- name: GetSchemaRequest
  property_count: 1
  slug: looker-studio-getschemarequest
- name: GetSchemaResponse
  property_count: 1
  slug: looker-studio-getschemaresponse
- name: InteractionConfig
  property_count: 2
  slug: looker-studio-interactionconfig
- name: LoadVisualizationRequest
  property_count: 2
  slug: looker-studio-loadvisualizationrequest
- name: LoadVisualizationResponse
  property_count: 3
  slug: looker-studio-loadvisualizationresponse
- name: Looker Studio Permissions
  property_count: 2
  slug: looker-studio-permissions
- name: Looker Studio Report
  property_count: 10
  slug: looker-studio-report
- name: RevokePermissionsRequest
  property_count: 1
  slug: looker-studio-revokepermissionsrequest
- name: Role
  property_count: 0
  slug: looker-studio-role
- name: SearchAssetsResponse
  property_count: 2
  slug: looker-studio-searchassetsresponse
- name: SetCredentialsRequest
  property_count: 5
  slug: looker-studio-setcredentialsrequest
- name: SetCredentialsResponse
  property_count: 1
  slug: looker-studio-setcredentialsresponse
- name: StyleConfig
  property_count: 3
  slug: looker-studio-styleconfig
- name: Looker Studio Community Visualization
  property_count: 6
  slug: looker-studio-visualization
- name: VisualizationComponent
  property_count: 6
  slug: looker-studio-visualizationcomponent
- name: VisualizationConfig
  property_count: 3
  slug: looker-studio-visualizationconfig
- name: VisualizationManifest
  property_count: 6
  slug: looker-studio-visualizationmanifest
- name: VisualizationResource
  property_count: 2
  slug: looker-studio-visualizationresource
json_structures:
- name: Looker Studio Structure
  property_count: 0
  slug: looker-studio-structure
jsonld:
- class_count: 0
  name: Looker Studio Context
  property_count: 40
  slug: looker-studio-context
layout: provider
modified: '2026-05-19'
name: Looker Studio
nav: Providers
network: true
overview: 'Looker Studio publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Configuration API, and 8 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Visualization, and Google.


  The Looker Studio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Looker Studio''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 18 more developer resources.'
plans:
- name: Looker Studio Plans Pricing
  plan_count: 2
  slug: looker-studio-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Looker Studio Rate Limits
  slug: looker-studio-rate-limits
rules:
- name: Looker Studio API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: looker-studio-jsonschema-spectral-rules
scopes:
- name: Looker Studio Scopes
  scope_count: 3
  slug: looker-studio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 69.4
  delta: 4.7
  facets:
    commercial_clarity: 73.7
    contract_quality: 74.1
    developer_ergonomics: 45.7
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 64.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/looker-studio/refs/heads/main/screenshots/looker-studio-2026-06-20T184714.png
security:
- kind: authentication
  name: Looker Studio Authentication
  slug: looker-studio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Looker Studio Domain Security
  slug: looker-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Looker Studio Vulnerability Disclosure
  slug: looker-studio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: looker-studio
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
- Google
- Reports
website: https://lookerstudio.google.com
---
