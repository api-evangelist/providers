---
aid: versioning-protocols
name: Versioning Protocols
description: Standards and methodologies for managing changes and updates to APIs, software interfaces, and data formats while maintaining backward compatibility and clear communication of breaking changes. Covers Semantic Versioning (SemVer), Calendar Versioning (CalVer), URI path versioning, header-based versioning, and deprecation management strategies. Used by developers, platform teams, and API governance programs to build maintainable and predictable API lifecycle policies.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/apis.yml
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
tags:
  - API Design
  - Backward Compatibility
  - Software Development
  - Version Control
  - Semantic Versioning
  - API Lifecycle
  - Deprecation
apis:
  - aid: versioning-protocols:semver
    name: Semantic Versioning (SemVer)
    description: Semantic Versioning is a versioning scheme using a MAJOR.MINOR.PATCH format where MAJOR increments denote breaking changes, MINOR increments indicate new backward-compatible features, and PATCH increments represent backward-compatible bug fixes. SemVer 2.0.0 is the canonical specification maintained at semver.org.
    humanURL: https://semver.org/
    tags:
      - Semantic Versioning
      - SemVer
      - Breaking Changes
      - API Versioning
    properties:
      - type: Documentation
        url: https://semver.org/
      - type: Specification
        url: https://semver.org/spec/v2.0.0.html
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/json-schema/versioning-protocols-semver-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/json-structure/versioning-protocols-semver-structure.json
  - aid: versioning-protocols:calver
    name: Calendar Versioning (CalVer)
    description: Calendar Versioning (CalVer) uses the release date as the version identifier, typically in YYYY.MM.DD or YYYY-MM-DD format. Used by APIs like Stripe (date-based versions e.g., 2024-06-01) to communicate when an API version was released rather than the impact of changes.
    humanURL: https://calver.org/
    tags:
      - Calendar Versioning
      - CalVer
      - Date-Based Versioning
      - API Versioning
    properties:
      - type: Documentation
        url: https://calver.org/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/json-schema/versioning-protocols-calver-schema.json
  - aid: versioning-protocols:uri-path-versioning
    name: URI Path Versioning
    description: URI path versioning embeds the API version in the URL path, typically as the major version number (e.g., /v1/users, /v2/users). The most widely adopted strategy for public REST APIs due to its explicitness, cache-friendliness, and ease of documentation. Minor and patch changes are deployed in place under the same major version path.
    humanURL: https://www.askantech.com/api-versioning-strategies-rest-header-url-deprecation-guide/
    tags:
      - URI Versioning
      - Path Versioning
      - REST
      - API Design
    properties:
      - type: Documentation
        url: https://www.askantech.com/api-versioning-strategies-rest-header-url-deprecation-guide/
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/json-schema/versioning-protocols-uri-path-versioning-schema.json
  - aid: versioning-protocols:header-versioning
    name: Header-Based Versioning
    description: 'Header-based versioning passes the API version in a custom HTTP request header (e.g., API-Version: 2026-04-01 or Accept: application/vnd.api.v2+json), keeping URLs clean and enabling more granular version control. Aligns well with full SemVer strings and content negotiation patterns.'
    humanURL: https://redocly.com/blog/api-versioning-best-practices
    tags:
      - Header Versioning
      - Content Negotiation
      - REST
      - API Design
    properties:
      - type: Documentation
        url: https://redocly.com/blog/api-versioning-best-practices
  - aid: versioning-protocols:openapi-versioning
    name: OpenAPI Versioning
    description: OpenAPI handles versioning through the info.version field (using SemVer), the deprecated flag on individual operations, parameters, and schemas, and multiple server entries for different API versions. Tools like oasdiff enable automated breaking change detection between OpenAPI spec versions.
    humanURL: https://openapispec.com/docs/how/how-does-openapi-handle-api-versioning/
    tags:
      - OpenAPI
      - API Specification
      - Breaking Changes
      - Deprecation
    properties:
      - type: Documentation
        url: https://openapispec.com/docs/how/how-does-openapi-handle-api-versioning/
common:
  - type: Website
    url: https://semver.org/
  - type: Documentation
    url: https://semver.org/spec/v2.0.0.html
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/vocabulary/versioning-protocols-vocabulary.yaml
  - type: Features
    data:
      - name: Semantic Versioning
        description: MAJOR.MINOR.PATCH versioning that communicates the impact of changes on API consumers.
      - name: Calendar Versioning
        description: Date-based versioning (YYYY.MM.DD) that communicates the freshness of an API release.
      - name: URI Path Versioning
        description: Embedding the API major version in the URL path for explicit, cache-friendly versioning.
      - name: Header-Based Versioning
        description: Passing the API version in HTTP headers for clean URL structures and content negotiation.
      - name: Query Parameter Versioning
        description: Appending the version to request URLs as a query string parameter (e.g., ?version=2).
      - name: Deprecation Management
        description: Structured policies for communicating and retiring old API versions with adequate notice.
      - name: Breaking Change Detection
        description: Tooling and processes to identify breaking changes between API versions using spec diffing.
      - name: N-2 Support Policy
        description: Support policy maintaining the current major version plus the two previous versions before retirement.
  - type: UseCases
    data:
      - name: API Lifecycle Governance
        description: Establish organizational versioning policies that balance innovation with backward compatibility.
      - name: Breaking Change Communication
        description: Communicate breaking changes clearly to API consumers with version bumps and deprecation notices.
      - name: Multi-Version Support
        description: Maintain multiple active API versions simultaneously to support consumers at different adoption stages.
      - name: Automated Change Detection
        description: Integrate spec diffing tools into CI/CD pipelines to detect breaking changes before release.
      - name: Deprecation Planning
        description: Plan and execute API version deprecations with 12-18 months notice and migration guides.
  - type: Integrations
    data:
      - name: Kong API Gateway
        description: Deploy version routing plugins, deprecation headers, and logging in Kong for API versioning.
      - name: Apigee
        description: Support versioned API proxies and detailed version analytics in Google Apigee.
      - name: AWS API Gateway
        description: Run different stages for version control and access management in AWS API Gateway.
      - name: Azure API Management
        description: First-class support for multiple API versions and revisions in Azure APIM.
      - name: oasdiff
        description: Open-source tool for detecting breaking changes between OpenAPI specification versions.
      - name: Redocly
        description: API documentation and governance platform with versioning and deprecation management features.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
