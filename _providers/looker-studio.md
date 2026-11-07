---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Looker Studio Agentic Access
  operation_count: 18
  slug: looker-studio-agentic-access
  summary_line: 18 operations · 6 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for searching and managing Looker Studio assets (reports and data sources).
  name: Looker Studio Assets API
  slug: looker-studio-assets-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for managing third-party authentication including OAuth2, API keys, and username/password credentials.
  name: Looker Studio Authentication API
  slug: looker-studio-authentication-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations related to connector configuration, including user-configurable options and authentication setup.
  name: Looker Studio Configuration API
  slug: looker-studio-configuration-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for fetching data from the external source and returning it to Looker Studio.
  name: Looker Studio Data API
  slug: looker-studio-data-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for embedding Looker Studio reports in external applications and websites.
  name: Looker Studio Embed API
  slug: looker-studio-embed-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations related to the visualization manifest configuration that defines how a visualization is discovered and loaded.
  name: Looker Studio Manifest API
  slug: looker-studio-manifest-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for managing asset permissions including getting, updating, adding, and revoking member access.
  name: Looker Studio Permissions API
  slug: looker-studio-permissions-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for creating and configuring linked Looker Studio reports.
  name: Looker Studio Reports API
  slug: looker-studio-reports-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for defining the data structure and field definitions returned by the connector.
  name: Looker Studio Schema API
  slug: looker-studio-schema-api
- baseURL: https://datastudio.googleapis.com/v1
  baseurl_source: declared
  description: Operations for loading and rendering community visualizations in Looker Studio reports.
  name: Looker Studio Visualization API
  slug: looker-studio-visualization-api
- baseURL: https://lookerstudio.google.com
  baseurl_source: declared
  description: oEmbed-compatible endpoint for platforms that support the oEmbed standard.
  name: Looker Studio o Embed API
  slug: looker-studio-o-embed-api
artifact_total: 85
collections:
- collection_type: postman
  name: Looker Studio Assets API
  slug: postman-looker-studio-assets-api
- collection_type: postman
  name: Looker Studio Assets Authentication API
  slug: postman-looker-studio-authentication-api
- collection_type: postman
  name: Looker Studio Assets Configuration API
  slug: postman-looker-studio-configuration-api
- collection_type: postman
  name: Looker Studio Assets Data API
  slug: postman-looker-studio-data-api
- collection_type: postman
  name: Looker Studio Assets Embed API
  slug: postman-looker-studio-embed-api
- collection_type: postman
  name: Looker Studio Assets Manifest API
  slug: postman-looker-studio-manifest-api
- collection_type: postman
  name: Looker Studio Assets oEmbed API
  slug: postman-looker-studio-oembed-api
- collection_type: postman
  name: Looker Studio Assets Permissions API
  slug: postman-looker-studio-permissions-api
- collection_type: postman
  name: Looker Studio Assets Reports API
  slug: postman-looker-studio-reports-api
- collection_type: postman
  name: Looker Studio Assets Schema API
  slug: postman-looker-studio-schema-api
- collection_type: postman
  name: Looker Studio Assets Visualization API
  slug: postman-looker-studio-visualization-api
- collection_type: open
  name: Looker Studio API
  slug: open-looker-studio-api
- collection_type: open
  name: Looker Studio Assets API
  slug: open-looker-studio-assets-api
- collection_type: open
  name: Looker Studio Assets Authentication API
  slug: open-looker-studio-authentication-api
- collection_type: open
  name: Looker Studio Community Connector API
  slug: open-looker-studio-community-connector-api
- collection_type: open
  name: Looker Studio Community Visualization API
  slug: open-looker-studio-community-visualization-api
- collection_type: open
  name: Looker Studio Assets Configuration API
  slug: open-looker-studio-configuration-api
- collection_type: open
  name: Looker Studio Assets Data API
  slug: open-looker-studio-data-api
- collection_type: open
  name: Looker Studio Assets Embed API
  slug: open-looker-studio-embed-api
- collection_type: open
  name: Looker Studio Embedding API
  slug: open-looker-studio-embedding-api
- collection_type: open
  name: Looker Studio Linking API
  slug: open-looker-studio-linking-api
- collection_type: open
  name: Looker Studio Assets Manifest API
  slug: open-looker-studio-manifest-api
- collection_type: open
  name: Looker Studio Assets oEmbed API
  slug: open-looker-studio-oembed-api
- collection_type: open
  name: Looker Studio Assets Permissions API
  slug: open-looker-studio-permissions-api
- collection_type: open
  name: Looker Studio Assets Reports API
  slug: open-looker-studio-reports-api
- collection_type: open
  name: Looker Studio Assets Schema API
  slug: open-looker-studio-schema-api
- collection_type: open
  name: Looker Studio Assets Visualization API
  slug: open-looker-studio-visualization-api
common:
- group: design
  href: https://artifacts.apis.io/looker-studio/rules/looker-studio-rules.yml
  title: ''
  type: Spectral
  url: rules/looker-studio-rules.yml
- group: design
  href: https://artifacts.apis.io/looker-studio/rules/looker-studio-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/looker-studio-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/looker-studio/json-ld/looker-studio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/looker-studio-context.jsonld
- group: design
  href: https://artifacts.apis.io/looker-studio/vocabulary/looker-studio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/looker-studio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/looker-studio/data-model/looker-studio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/looker-studio-data-model.yml
- group: design
  href: https://artifacts.apis.io/looker-studio/errors/looker-studio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/looker-studio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/looker-studio/conformance/looker-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/looker-studio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/looker-studio/llms/looker-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/looker-studio-llms.txt
- group: agent
  href: https://artifacts.apis.io/looker-studio/well-known/looker-studio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/looker-studio-well-known.yml
- group: other
  href: https://artifacts.apis.io/looker-studio/hosts/looker-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/looker-studio-hosts.yml
- group: build
  href: https://artifacts.apis.io/looker-studio/packages/looker-studio-packages.yml
  title: ''
  type: Packages
  url: packages/looker-studio-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: commercial
  href: https://artifacts.apis.io/looker-studio/plans/looker-studio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/looker-studio-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/looker-studio/rate-limits/looker-studio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/looker-studio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/looker-studio/finops/looker-studio-finops.yml
  title: ''
  type: FinOps
  url: finops/looker-studio-finops.yml
- group: other
  href: https://artifacts.apis.io/looker-studio/capabilities/looker-studio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/looker-studio-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/looker-studio/overview
- group: agent
  href: https://artifacts.apis.io/looker-studio/agentic-access/looker-studio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/looker-studio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/looker-studio/security/looker-studio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/looker-studio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/looker-studio/security/looker-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/looker-studio-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/looker-studio/authentication/looker-studio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/looker-studio-authentication.yml
- group: auth
  href: https://artifacts.apis.io/looker-studio/scopes/looker-studio-scopes.yml
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
- has_sources: true
  method: generated
  name: Looker Studio Finops
  primary_unit: ''
  service_category: Business Intelligence
  slug: looker-studio-finops
  template: false
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
overview: 'Looker Studio publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Configuration API, and 8 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Visualization, and Google.


  The Looker Studio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Looker Studio''s developer surface includes sandbox, authentication, developer portal, documentation, getting-started guide, engineering blog, support, and 35 more developer resources.'
plans:
- name: Looker Studio Plans Pricing
  plan_count: 2
  slug: looker-studio-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Looker Studio Rate Limits
  slug: looker-studio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Looker Studio — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: looker-studio-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 119
  extends:
  - spectral:oas
  name: Looker Studio API Rules
  rule_count: 78
  severity_counts:
    error: 70
    hint: 0
    info: 2
    warn: 6
  slug: looker-studio-rules
scopes:
- name: Looker Studio Scopes
  scope_count: 3
  slug: looker-studio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.0
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 58.6
    developer_ergonomics: 72.6
    discoverability: 78.6
    operational_transparency: 52.6
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/looker-studio/looker-studio-2026-08-17T082124.png
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
