---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nuget Agentic Access
  operation_count: 16
  slug: nuget-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 7
apis:
- description: 'The NuGet Catalog API is an append-only resource that records the full history of all package events on nuget.org, including packages being added, modified, listed, unlisted, and deleted. It provides '
  name: NuGet Catalog API
  slug: nuget-catalog-api
- description: The NuGet Search API allows clients to query for packages available on a NuGet package source using the SearchQueryService resource found in the service index. It supports filtering by keyword, target
  name: NuGet Search API
  slug: nuget-search-api
- description: 'The NuGet Package Content API, accessed through the PackageBaseAddress resource, allows clients to download package content files (.nupkg) and package manifests (.nuspec) from a NuGet feed. It uses a '
  name: NuGet Package Content API
  slug: nuget-package-content-api
- description: Autocomplete package IDs and enumerate package versions for typeahead and discovery features.
  name: NuGet Autocomplete API
  slug: nuget-autocomplete-api
- description: Endpoints for pushing new packages, deleting or unlisting packages, and relisting previously unlisted packages on a NuGet feed.
  name: NuGet Package Publish API
  slug: nuget-package-publish-api
- description: Package registration endpoints for fetching metadata about packages, organized into an index, pages, and leaves hierarchy.
  name: NuGet Registration API
  slug: nuget-registration-api
- description: The service index is the entry point for the NuGet V3 API. It is a JSON document that lists all available resources and their capabilities.
  name: NuGet Service Index API
  slug: nuget-service-index-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  url: https://github.com/NuGet/NuGetGallery/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuget-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuget-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuget-domain-security.yml
- group: auth
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
- name: Nuget Finops
  service_category: Developer Tools / Package Registry
  slug: nuget-finops
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
overview: 'NuGet publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Search API, Package Content API, and 4 more. Tagged areas include Package Management, .NET, Packages, Dependencies, and Software Distribution.


  The NuGet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NuGet''s developer surface includes authentication, developer portal, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Nuget Plans Pricing
  plan_count: 1
  slug: nuget-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Nuget Rate Limits
  slug: nuget-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: NuGet API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: nuget-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.6
  delta: 0.7
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 9.8
    contract_quality: 55.1
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuget/refs/heads/main/screenshots/nuget-2026-06-20T190513.png
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
slug: nuget
tags:
- Package Management
- .NET
- Packages
- Dependencies
- Software Distribution
- Registry
website: https://www.nuget.org/
---
