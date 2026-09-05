---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Semantic Versioning is a versioning scheme using a MAJOR.MINOR.PATCH format where MAJOR increments denote breaking changes, MINOR increments indicate new backward-compatible features, and PATCH increm
  name: Semantic Versioning (SemVer)
  slug: semver
- description: Calendar Versioning (CalVer) uses the release date as the version identifier, typically in YYYY.MM.DD or YYYY-MM-DD format. Used by APIs like Stripe (date-based versions e.g., 2024-06-01) to communica
  name: Calendar Versioning (CalVer)
  slug: calver
- description: URI path versioning embeds the API version in the URL path, typically as the major version number (e.g., /v1/users, /v2/users). The most widely adopted strategy for public REST APIs due to its explici
  name: URI Path Versioning
  slug: uri-path-versioning
- description: 'Header-based versioning passes the API version in a custom HTTP request header (e.g., API-Version: 2026-04-01 or Accept: application/vnd.api.v2+json), keeping URLs clean and enabling more granular ver'
  name: Header-Based Versioning
  slug: header-versioning
- description: OpenAPI handles versioning through the info.version field (using SemVer), the deprecated flag on individual operations, parameters, and schemas, and multiple server entries for different API versions.
  name: OpenAPI Versioning
  slug: openapi-versioning
artifact_total: 39
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/versioning-protocols-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://semver.org/
- group: docs
  title: ''
  type: Documentation
  url: https://semver.org/spec/v2.0.0.html
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/vocabulary/versioning-protocols-vocabulary.yaml
created: '2025'
description: Standards and methodologies for managing changes and updates to APIs, software interfaces, and data formats while maintaining backward compatibility and clear communication of breaking changes. Covers Semantic Versioning (SemVer), Calendar Versioning (CalVer), URI path versioning, header-based versioning, and deprecation management strategies. Used by developers, platform teams, and API governance programs to build maintainable and predictable API lifecycle policies.
examples:
- key_count: 7
  name: Versioning Protocols Calver Example
  slug: versioning-protocols-calver-example
- key_count: 9
  name: Versioning Protocols Semver Example
  slug: versioning-protocols-semver-example
- key_count: 6
  name: Versioning Protocols Uri Path Versioning Example
  slug: versioning-protocols-uri-path-versioning-example
features:
- description: MAJOR.MINOR.PATCH versioning that communicates the impact of changes on API consumers.
  name: Semantic Versioning
- description: Date-based versioning (YYYY.MM.DD) that communicates the freshness of an API release.
  name: Calendar Versioning
- description: Embedding the API major version in the URL path for explicit, cache-friendly versioning.
  name: URI Path Versioning
- description: Passing the API version in HTTP headers for clean URL structures and content negotiation.
  name: Header-Based Versioning
- description: Appending the version to request URLs as a query string parameter (e.g., ?version=2).
  name: Query Parameter Versioning
- description: Structured policies for communicating and retiring old API versions with adequate notice.
  name: Deprecation Management
- description: Tooling and processes to identify breaking changes between API versions using spec diffing.
  name: Breaking Change Detection
- description: Support policy maintaining the current major version plus the two previous versions before retirement.
  name: N-2 Support Policy
finops:
- name: Versioning Protocols Finops
  service_category: API
  slug: versioning-protocols-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/versioning-protocols.png
integrations:
- description: Deploy version routing plugins, deprecation headers, and logging in Kong for API versioning.
  name: Kong API Gateway
- description: Support versioned API proxies and detailed version analytics in Google Apigee.
  name: Apigee
- description: Run different stages for version control and access management in AWS API Gateway.
  name: AWS API Gateway
- description: First-class support for multiple API versions and revisions in Azure APIM.
  name: Azure API Management
- description: Open-source tool for detecting breaking changes between OpenAPI specification versions.
  name: oasdiff
- description: API documentation and governance platform with versioning and deprecation management features.
  name: Redocly
json_schemas:
- name: CalendarVersion
  property_count: 7
  slug: versioning-protocols-calver
- name: SemanticVersion
  property_count: 9
  slug: versioning-protocols-semver
- name: URIPathVersion
  property_count: 6
  slug: versioning-protocols-uri-path-versioning
json_structures:
- name: Versioning Protocols Calver Structure
  property_count: 7
  slug: versioning-protocols-calver-structure
- name: Versioning Protocols Semver Structure
  property_count: 9
  slug: versioning-protocols-semver-structure
- name: Versioning Protocols Uri Path Versioning Structure
  property_count: 6
  slug: versioning-protocols-uri-path-versioning-structure
jsonld:
- class_count: 3
  name: Versioning Protocols Context
  property_count: 22
  slug: versioning-protocols-context
layout: provider
modified: '2026-05-03'
name: Versioning Protocols
nav: Providers
network: true
overview: 'Versioning Protocols publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, Backward Compatibility, Software Development, Version Control, and Semantic Versioning.


  The Versioning Protocols catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Versioning Protocols'' developer surface includes documentation and 3 more developer resources.'
plans:
- name: Versioning Protocols Plans Pricing
  plan_count: 3
  slug: versioning-protocols-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Versioning Protocols Rate Limits
  slug: versioning-protocols-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Versioning Protocols API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: versioning-protocols-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 66.3
    catalog_earned_first_party: 0.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 20.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/versioning-protocols/refs/heads/main/screenshots/versioning-protocols-2026-06-20T200942.png
security:
- kind: domain-security
  name: Versioning Protocols Domain Security
  slug: versioning-protocols-domain-security
  summary_line: TLSv1.3
slug: versioning-protocols
tags:
- API Design
- Backward Compatibility
- Software Development
- Version Control
- Semantic Versioning
- API Lifecycle
- Deprecation
use_cases:
- description: Establish organizational versioning policies that balance innovation with backward compatibility.
  name: API Lifecycle Governance
- description: Communicate breaking changes clearly to API consumers with version bumps and deprecation notices.
  name: Breaking Change Communication
- description: Maintain multiple active API versions simultaneously to support consumers at different adoption stages.
  name: Multi-Version Support
- description: Integrate spec diffing tools into CI/CD pipelines to detect breaking changes before release.
  name: Automated Change Detection
- description: Plan and execute API version deprecations with 12-18 months notice and migration guides.
  name: Deprecation Planning
website: https://semver.org/
---
