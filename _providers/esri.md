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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Esri Agentic Access
  operation_count: 6
  slug: esri-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: The Esri ArcGIS Platform API is a set of REST APIs and SDKs from Esri, provider of the ArcGIS GIS suite. It enables developers to integrate Esri's mapping, geocoding, routing, and spatial analysis ser
  name: Esri ArcGIS Platform API
  slug: esri-arcgis-platform-api
- baseURL: https://www.arcgis.com/sharing/rest
  baseurl_source: declared
  description: The Auth API from Esri — 1 operation(s) for auth.
  name: Esri Auth API
  slug: esri-auth-api
- baseURL: https://geocode-api.arcgis.com/arcgis/rest/services
  baseurl_source: declared
  description: The Geocoding API from Esri — 4 operation(s) for geocoding.
  name: Esri Geocoding API
  slug: esri-geocoding-api
- baseURL: https://route-api.arcgis.com/arcgis/rest/services
  baseurl_source: declared
  description: The Routing API from Esri — 1 operation(s) for routing.
  name: Esri Routing API
  slug: esri-routing-api
artifact_total: 20
asyncapis:
- description: ''
  name: Esri Webhooks
  slug: esri-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Esri ArcGIS Location Services Auth API
  slug: open-esri-auth-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Geocoding API
  slug: open-esri-geocoding-api
- collection_type: open
  name: Esri ArcGIS Location Services Auth Routing API
  slug: open-esri-routing-api
- collection_type: open
  name: Esri ArcGIS Location Services API
  slug: open-esri
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/esri-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/esri-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/esri-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/esri-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esri
- group: company
  title: ''
  type: Website
  url: https://www.esri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.arcgis.com/
- group: other
  title: ''
  type: Alias
  url: https://github.com/api-evangelist/esri-arcgis
- group: agent
  title: ''
  type: MCPServer
  url: mcp/esri-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/esri-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/esri-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/esri-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/esri-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/esri-packages.yml
- group: design
  title: ''
  type: Components
  url: components/esri-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/esri-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/esri-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/esri-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.location.arcgis.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://location.arcgis.com/help/release-notes/2026-07/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/esri-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/esri-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.arcgis.com/en/compliance/compliance.htm
- group: auth
  title: ''
  type: TrustCenter
  url: security/esri-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/esri-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.arcgis.com/en/security-concern/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/esri-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/esri-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: WSDL
  url: wsdl/esri-wsdl-index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/esri-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/esri-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/esri-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.arcgis.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.arcgis.com/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.arcgis.com/documentation/mapping-and-location-services/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.esri.com/en-us/products/arcgis-location-platform
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.esri.com/t5/developers/ct-p/developers
- group: company
  title: ''
  type: Blog
  url: https://community.esri.com/t5/developers-blog/bg-p/developers-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Esri
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/esridevs/workspace/esri-arcgis-services
- group: commercial
  title: ''
  type: Pricing
  url: https://location.arcgis.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://location.arcgis.com/sign-up/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.esri.com/en-us/legal/terms/full-master-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esri.com/en-us/privacy/overview
created: '2025-01-14'
description: 'Esri is a global leader in geographic information system (GIS) technology, offering innovative solutions for mapping and spatial analysis. The company provides software, data, and services to help organizations make better decisions based on location intelligence. Esri''s technology is used across a wide range of industries, including government, natural resources, utilities, and public safety. NOTE: This repository is an alias for the canonical Esri ArcGIS profile maintained at api-evangelist/esri-arcgis, which contains the full set of API definitions, OpenAPI artifacts, and developer resources.'
finops:
- name: Esri Finops
  service_category: API
  slug: esri-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/esri.png
layout: provider
mcp_servers:
- description: An Esri-hosted Model Context Protocol server that exposes ArcGIS Location Services — geocoding, routing, elevation, static maps and GeoEnrichment — to MCP-compliant clients and AI agents without calli
  name: MCP for ArcGIS Location Services (beta)
  slug: mcp-for-arcgis-location-services-beta
modified: '2026-09-07'
name: Esri
nav: Providers
network: true
overview: 'Esri publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Geocoding API, and Routing API. Tagged areas include Geographic, Geospatial, GIS, Location, and Mapping.


  The Esri catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Esri''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 38 more developer resources.'
plans:
- name: Esri Plans Pricing
  plan_count: 1
  slug: esri-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Esri Rate Limits
  slug: esri-rate-limits
scopes:
- name: Esri Scopes
  scope_count: 0
  slug: esri-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 34.8
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 53.0
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/esri/refs/heads/main/screenshots/esri-2026-06-20T180822.png
security:
- kind: authentication
  name: Esri Authentication
  slug: esri-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Esri Domain Security
  slug: esri-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Esri Vulnerability Disclosure
  slug: esri-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Esri Trust Center
  slug: esri-trust-center
  summary_line: FedRAMP Moderate, ISO/IEC 27001:2022, SOC 2, GDPR, EU-U.S. Data Privacy Framework, CCPA / CPRA
slug: esri
tags:
- Geographic
- Geospatial
- GIS
- Location
- Mapping
- Maps
- Spatial Analysis
website: https://www.esri.com/
---
