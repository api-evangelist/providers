---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Azure Private Link Agentic Access
  operation_count: 29
  slug: microsoft-azure-private-link-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-private-link Operations API
  slug: microsoft-azure-private-link-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Private Endpoints operations
  name: microsoft-azure-private-link Private Endpoints API
  slug: microsoft-azure-private-link-private-endpoints-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The PrivateDnsZoneGroups API from Microsoft Azure Private Link — 2 operation(s) for privatednszonegroups.
  name: Microsoft Azure Private Link Private Dns Zone Groups API
  slug: microsoft-azure-private-link-privatednszonegroups-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The PrivateLinkService API from Microsoft Azure Private Link — 1 operation(s) for privatelinkservice.
  name: Microsoft Azure Private Link Private Link Service API
  slug: microsoft-azure-private-link-privatelinkservice-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The PrivateLinkServices API from Microsoft Azure Private Link — 9 operation(s) for privatelinkservices.
  name: Microsoft Azure Private Link Private Link Services API
  slug: microsoft-azure-private-link-privatelinkservices-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Private Link — 2 operation(s) for subscriptions.
  name: Microsoft Azure Private Link Subscriptions API
  slug: microsoft-azure-private-link-subscriptions-api
artifact_total: 35
collections:
- collection_type: open
  name: Azure Private Link REST Operations API
  slug: open-microsoft-azure-private-link-operations-api
- collection_type: open
  name: Azure Private Link REST Operations Private Endpoints API
  slug: open-microsoft-azure-private-link-private-endpoints-api
- collection_type: open
  name: Azure Private Link REST API
  slug: open-microsoft-azure-private-link
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/rules/microsoft-azure-private-link-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-private-link-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/json-ld/microsoft-azure-private-link-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-private-link-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/vocabulary/microsoft-azure-private-link-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-private-link-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-private-link/hosts/microsoft-azure-private-link-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-private-link-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-private-link/vendors/microsoft-azure-private-link-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-private-link-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-private-link/finops/microsoft-azure-private-link-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-private-link-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-private-link/capabilities/microsoft-azure-private-link-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-private-link-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/private-link/private-link-overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/private-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal
- group: start
  title: ''
  type: Quickstart
  url: https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/azurenetworkingblog
- group: operate
  title: ''
  type: Roadmap
  url: https://azure.microsoft.com/en-us/updates/?category=networking
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/private-link/
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-private-link/plans/microsoft-azure-private-link-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-private-link-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-private-link/agentic-access/microsoft-azure-private-link-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-private-link-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/authentication/microsoft-azure-private-link-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-private-link-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/scopes/microsoft-azure-private-link-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-private-link-scopes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/conventions/microsoft-azure-private-link-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-private-link-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/conventions/microsoft-azure-private-link-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-private-link-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/errors/microsoft-azure-private-link-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-private-link-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-private-link/rate-limits/microsoft-azure-private-link-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-private-link-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/data-model/microsoft-azure-private-link-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-private-link-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/lifecycle/microsoft-azure-private-link-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-private-link-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  title: ''
  type: Deprecation
  url: https://azure.microsoft.com/en-us/updates/?updateType=retirements
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-private-link/changelog/microsoft-azure-private-link-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-private-link-changelog.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-private-link/packages/microsoft-azure-private-link-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-private-link-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-private-link/packages/microsoft-azure-private-link-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-private-link-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-private-link/cli/microsoft-azure-private-link-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-private-link-cli.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-private-link/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-private-link/llms/microsoft-azure-private-link-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-private-link-llms.txt
- group: design
  href: https://artifacts.apis.io/microsoft-azure-private-link/conformance/microsoft-azure-private-link-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-private-link-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/compliance/
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/security/microsoft-azure-private-link-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-private-link-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/cvd
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/security/microsoft-azure-private-link-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-private-link-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/well-known/microsoft-azure-private-link-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-private-link-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-private-link/well-known/microsoft-azure-private-link-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-private-link-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-private-link/security/microsoft-azure-private-link-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-private-link-domain-security.yml
created: '2026-05-04'
description: 'Microsoft Azure Private Link gives a virtual network a private IP address onto an Azure PaaS service, a partner service, or a service the customer publishes themselves, so traffic reaches it across the Microsoft backbone and never traverses the public internet. It has two sides. A consumer creates a private endpoint pointing at a target resource id and attaches a private DNS zone group so the service''s own hostname resolves to that private address. A producer publishes a private link service in front of a Standard Load Balancer, hands out an opaque alias, and approves or rejects the connections that arrive — including connections from other tenants. Both sides are managed through the Azure Resource Manager REST API at management.azure.com, which Microsoft publishes as Swagger 2.0 in its azure-rest-api-specs repository: 24 operations at api-version 2025-03-01, OAuth2 bearer only, with no API key and no anonymous surface.'
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Private Link Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-private-link-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-private-link.png
json_schemas:
- name: AutoApprovedPrivateLinkServicesResult
  property_count: 2
  slug: microsoft-azure-private-link-auto-approved-private-link-services-result
- name: AvailablePrivateEndpointTypesResult
  property_count: 2
  slug: microsoft-azure-private-link-available-private-endpoint-types-result
- name: CheckPrivateLinkServiceVisibilityRequest
  property_count: 1
  slug: microsoft-azure-private-link-check-private-link-service-visibility-request
- name: OperationList
  property_count: 2
  slug: microsoft-azure-private-link-operation-list
- name: PrivateDnsZoneGroupListResult
  property_count: 2
  slug: microsoft-azure-private-link-private-dns-zone-group-list-result
- name: PrivateDnsZoneGroup
  property_count: 3
  slug: microsoft-azure-private-link-private-dns-zone-group
- name: PrivateEndpointConnectionListResult
  property_count: 2
  slug: microsoft-azure-private-link-private-endpoint-connection-list-result
- name: PrivateEndpointConnection
  property_count: 4
  slug: microsoft-azure-private-link-private-endpoint-connection
- name: PrivateEndpoint
  property_count: 3
  slug: microsoft-azure-private-link-private-endpoint
- name: PrivateLinkServiceListResult
  property_count: 2
  slug: microsoft-azure-private-link-private-link-service-list-result
- name: PrivateLinkService
  property_count: 3
  slug: microsoft-azure-private-link-private-link-service
- name: ResourceList
  property_count: 2
  slug: microsoft-azure-private-link-resource-list
- name: Resource
  property_count: 6
  slug: microsoft-azure-private-link-resource
jsonld:
- class_count: 35
  name: Microsoft Azure Private Link Context
  property_count: 62
  slug: microsoft-azure-private-link-context
layout: provider
modified: '2026-11-05'
name: Microsoft Azure Private Link
nav: Providers
network: true
overview: 'Microsoft Azure Private Link publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including microsoft-azure-private-link Operations API, microsoft-azure-private-link Private Endpoints API, Private Dns Zone Groups API, and 3 more. Tagged areas include Networking, Private Connectivity, Cloud Infrastructure, Virtual Networks, and DNS.


  The Microsoft Azure Private Link catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Private Link''s developer surface includes developer portal, documentation, API reference, getting-started guide, quickstart, engineering blog, pricing, and 42 more developer resources.'
plans:
- name: Microsoft Azure Private Link Plans Pricing
  plan_count: 0
  slug: microsoft-azure-private-link-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Microsoft Azure Private Link Rate Limits
  slug: microsoft-azure-private-link-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Microsoft Azure Private Link API Rules
  rule_count: 52
  severity_counts:
    error: 44
    hint: 0
    info: 5
    warn: 3
  slug: microsoft-azure-private-link-rules
scopes:
- name: Microsoft Azure Private Link Scopes
  scope_count: 1
  slug: microsoft-azure-private-link-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 35
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 57.2
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 89.5
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 28.6
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-private-link/microsoft-azure-private-link-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Private Link Authentication
  slug: microsoft-azure-private-link-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Private Link Domain Security
  slug: microsoft-azure-private-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Private Link Vulnerability Disclosure
  slug: microsoft-azure-private-link-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Private Link Trust Center
  slug: microsoft-azure-private-link-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: approve-endpoint-connections
  slug: microsoft-azure-private-link-approve-endpoint-connections
- name: connect-to-paas-service
  slug: microsoft-azure-private-link-connect-to-paas-service
slug: microsoft-azure-private-link
tags:
- Networking
- Private Connectivity
- Cloud Infrastructure
- Virtual Networks
- DNS
- Security
- Azure Resource Manager
- Infrastructure-as-a-Service
website: https://www.microsoft.com/
---
