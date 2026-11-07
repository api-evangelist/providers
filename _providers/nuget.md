---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nuget Agentic Access
  operation_count: 16
  slug: nuget-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 2
apis:
- baseURL: https://api.nuget.org/v3
  baseurl_source: spec
  description: Endpoints for pushing new packages, deleting or unlisting packages, and relisting previously unlisted packages on a NuGet feed.
  name: NuGet Package Publish API
  slug: nuget-package-publish-api
- baseURL: https://api.nuget.org/v3/registration5-gz-semver2
  baseurl_source: spec
  description: Package registration endpoints for fetching metadata about packages, organized into an index, pages, and leaves hierarchy.
  name: NuGet Registration API
  slug: nuget-registration-api
- baseURL: https://api.nuget.org/v3
  baseurl_source: spec
  description: The service index is the entry point for the NuGet V3 API. It is a JSON document that lists all available resources and their capabilities.
  name: NuGet Service Index API
  slug: nuget-service-index-api
- baseURL: https://api.nuget.org/v3/
  baseurl_source: declared
  description: The Autocomplete API from Microsoft NuGet — 1 operation(s) for autocomplete.
  name: Microsoft NuGet Autocomplete API
  slug: microsoft-nuget-autocomplete-api
- baseURL: https://api.nuget.org/v3/
  baseurl_source: declared
  description: The Flatcontainer API from Microsoft NuGet — 3 operation(s) for flatcontainer.
  name: Microsoft NuGet Flatcontainer API
  slug: microsoft-nuget-flatcontainer-api
- baseURL: https://api.nuget.org/v3/
  baseurl_source: declared
  description: The Query API from Microsoft NuGet — 1 operation(s) for query.
  name: Microsoft NuGet Query API
  slug: microsoft-nuget-query-api
- baseURL: https://api.nuget.org/v3/
  baseurl_source: declared
  description: The Registration5 Gz Semver2 API from Microsoft NuGet — 2 operation(s) for registration5 gz semver2.
  name: Microsoft NuGet Registration5 Gz Semver2 API
  slug: microsoft-nuget-registration5-gz-semver2-api
artifact_total: 64
collections:
- collection_type: open
  name: NuGet Catalog Autocomplete API
  slug: open-nuget-autocomplete-api
- collection_type: open
  name: NuGet Autocomplete Catalog API
  slug: open-nuget-catalog-api
- collection_type: open
  name: NuGet Catalog Autocomplete Package Content API
  slug: open-nuget-package-content-api
- collection_type: open
  name: NuGet Package Metadata API
  slug: open-nuget-package-metadata-api
- collection_type: open
  name: NuGet Catalog Autocomplete Package Publish API
  slug: open-nuget-package-publish-api
- collection_type: open
  name: NuGet Catalog Autocomplete Registration API
  slug: open-nuget-registration-api
- collection_type: open
  name: NuGet Catalog Autocomplete Search API
  slug: open-nuget-search-api
- collection_type: open
  name: NuGet Server API
  slug: open-nuget-server-api
- collection_type: open
  name: NuGet Catalog Autocomplete Service Index API
  slug: open-nuget-service-index-api
common:
- group: auth
  href: https://artifacts.apis.io/nuget/well-known/nuget-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuget-www-security.txt
- group: agent
  href: https://artifacts.apis.io/nuget/well-known/nuget-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nuget-well-known.yml
- group: design
  href: https://artifacts.apis.io/nuget/rules/nuget-rules.yml
  title: ''
  type: Spectral
  url: rules/nuget-rules.yml
- group: design
  href: https://artifacts.apis.io/nuget/rules/nuget-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/nuget-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/nuget/json-ld/nuget-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nuget-context.jsonld
- group: design
  href: https://artifacts.apis.io/nuget/vocabulary/nuget-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nuget-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/nuget/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nuget/data-model/nuget-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nuget-data-model.yml
- group: build
  href: https://artifacts.apis.io/nuget/cli/nuget-cli.yml
  title: ''
  type: CLI
  url: cli/nuget-cli.yml
- group: design
  href: https://artifacts.apis.io/nuget/conventions/nuget-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nuget-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/bounty-safe-harbor
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/nuget/api/overview
- group: design
  href: https://artifacts.apis.io/nuget/lifecycle/nuget-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nuget-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nuget/errors/nuget-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nuget-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nuget/conformance/nuget-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuget-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nuget/llms/nuget-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nuget-llms.txt
- group: other
  href: https://artifacts.apis.io/nuget/hosts/nuget-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuget-hosts.yml
- group: build
  href: https://artifacts.apis.io/nuget/integrations/nuget-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/nuget-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/nuget/vendors/nuget-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuget-vendors.yml
- group: build
  href: https://artifacts.apis.io/nuget/packages/nuget-packages.yml
  title: ''
  type: SDKs
  url: packages/nuget-packages.yml
- group: build
  href: https://artifacts.apis.io/nuget/packages/nuget-packages.yml
  title: ''
  type: Packages
  url: packages/nuget-packages.yml
- group: commercial
  href: https://artifacts.apis.io/nuget/plans/nuget-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nuget-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nuget/rate-limits/nuget-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nuget-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nuget/finops/nuget-finops.yml
  title: ''
  type: FinOps
  url: finops/nuget-finops.yml
- group: other
  href: https://artifacts.apis.io/nuget/capabilities/nuget-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nuget-capability-edges.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NuGet
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuget.org/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/NuGet/NuGetGallery/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/NuGet/NuGetGallery/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/NuGet/NuGetGallery/blob/main/LICENSE.txt
- group: agent
  href: https://artifacts.apis.io/nuget/agentic-access/nuget-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nuget-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nuget/security/nuget-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuget-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nuget/security/nuget-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuget-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nuget/authentication/nuget-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nuget-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://learn.microsoft.com/en-us/nuget/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/nuget/api/overview
- group: company
  title: ''
  type: Website
  url: https://www.nuget.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuget.org/policies/Terms
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/nuget/
- group: start
  title: ''
  type: Login
  url: https://www.nuget.org/users/account/LogOn
- group: agent
  title: ''
  type: MCPServer
  url: https://devblogs.microsoft.com/dotnet/nuget-mcp-server-preview/
created: '2025-03-05'
description: NuGet is the package manager for .NET, providing a centralized repository for developers to discover, share, and consume reusable code libraries. The NuGet developer platform exposes a set of HTTP APIs that enable programmatic access to package search, metadata retrieval, content download, catalog browsing, and package publishing against the nuget.org feed.
finops:
- has_sources: true
  method: generated
  name: Nuget Finops
  primary_unit: request
  service_category: Developer Tools / Package Registry
  slug: nuget-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuget.png
json_schemas:
- name: AlternatePackage
  property_count: 2
  slug: nuget-alternatepackage
- name: AutocompleteResponse
  property_count: 2
  slug: nuget-autocompleteresponse
- name: NuGet Catalog Event
  property_count: 16
  slug: nuget-catalog-event
- name: CatalogEntry
  property_count: 22
  slug: nuget-catalogentry
- name: CatalogIndex
  property_count: 4
  slug: nuget-catalogindex
- name: CatalogItemReference
  property_count: 6
  slug: nuget-catalogitemreference
- name: CatalogPackageType
  property_count: 2
  slug: nuget-catalogpackagetype
- name: CatalogPage
  property_count: 5
  slug: nuget-catalogpage
- name: CatalogPageReference
  property_count: 4
  slug: nuget-catalogpagereference
- name: Dependency
  property_count: 2
  slug: nuget-dependency
- name: DependencyGroup
  property_count: 2
  slug: nuget-dependencygroup
- name: Deprecation
  property_count: 3
  slug: nuget-deprecation
- name: GenericObject
  property_count: 0
  slug: nuget-generic-object
- name: NuGet Package
  property_count: 32
  slug: nuget-package
- name: PackageDeleteLeaf
  property_count: 7
  slug: nuget-packagedeleteleaf
- name: PackageDetailsLeaf
  property_count: 30
  slug: nuget-packagedetailsleaf
- name: PackageType
  property_count: 1
  slug: nuget-packagetype
- name: RegistrationIndex
  property_count: 2
  slug: nuget-registration-index
- name: RegistrationLeafDocument
  property_count: 6
  slug: nuget-registration-leaf-document
- name: RegistrationPage
  property_count: 6
  slug: nuget-registration-page
- name: RegistrationIndex
  property_count: 2
  slug: nuget-registrationindex
- name: RegistrationLeaf
  property_count: 3
  slug: nuget-registrationleaf
- name: RegistrationLeafDocument
  property_count: 6
  slug: nuget-registrationleafdocument
- name: RegistrationPage
  property_count: 6
  slug: nuget-registrationpage
- name: RegistrationPageEntry
  property_count: 6
  slug: nuget-registrationpageentry
- name: SearchResponse
  property_count: 2
  slug: nuget-searchresponse
- name: SearchResult
  property_count: 16
  slug: nuget-searchresult
- name: SearchResultVersion
  property_count: 3
  slug: nuget-searchresultversion
- name: ServiceIndex
  property_count: 2
  slug: nuget-service-index
- name: ServiceIndex
  property_count: 2
  slug: nuget-serviceindex
- name: ServiceIndexResource
  property_count: 3
  slug: nuget-serviceindexresource
- name: VersionEnumerationResponse
  property_count: 1
  slug: nuget-versionenumerationresponse
- name: VersionIndex
  property_count: 1
  slug: nuget-versionindex
- name: Vulnerability
  property_count: 2
  slug: nuget-vulnerability
json_structures:
- name: Nuget Structure
  property_count: 0
  slug: nuget-structure
jsonld:
- class_count: 0
  name: Nuget Context
  property_count: 8
  slug: nuget-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: NuGet
nav: Providers
network: true
overview: 'NuGet publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Package Publish API, Registration API, Service Index API, and 4 more. Tagged areas include Package Management, .NET, Packages, Dependencies, and Software Distribution.


  The NuGet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  NuGet''s developer surface includes CLI, getting-started guide, support, authentication, developer portal, documentation, engineering blog, and 37 more developer resources.'
plans:
- name: Nuget Plans Pricing
  plan_count: 1
  slug: nuget-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 7
  name: Nuget Rate Limits
  slug: nuget-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: NuGet — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: nuget-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: NuGet API Rules
  rule_count: 53
  severity_counts:
    error: 50
    hint: 0
    info: 2
    warn: 1
  slug: nuget-rules
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 54.0
    developer_ergonomics: 73.2
    discoverability: 63.3
    operational_transparency: 68.4
  open_source:
    applies: true
    score: 100.0
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nuget/nuget-2026-06-20T190513.png
security:
- kind: authentication
  name: Nuget Authentication
  slug: nuget-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nuget Domain Security
  slug: nuget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nuget Vulnerability Disclosure
  slug: nuget-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: nuget-find-package
  slug: nuget-find-package
- name: nuget-publish-package
  slug: nuget-publish-package
slug: nuget
tags:
- Package Management
- .NET
- Packages
- Dependencies
- Software Distribution
- Registry
- Developer Tools
website: https://www.nuget.org/
---
