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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ballerina Agentic Access
  operation_count: 6
  slug: ballerina-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.central.ballerina.io
  baseurl_source: declared
  description: Public read API for the Ballerina Central package registry — list or search packages by keyword and organization, run a full-text search with suggestions and field highlighting, and list the published
  name: Ballerina Packages API
  slug: ballerina-packages-api
- baseURL: https://api.central.ballerina.io
  baseurl_source: declared
  description: Search the connector clients declared inside packages published to Ballerina Central — the outbound integration half of the registry, covering the 727 WSO2-maintained ballerinax connector packages. Ea
  name: Ballerina Connectors API
  slug: ballerina-connectors-api
- baseURL: https://api.central.ballerina.io
  baseurl_source: declared
  description: Search the event triggers and listeners declared inside packages published to Ballerina Central — the inbound, event-driven half of the registry, paired with the connector index. Each hit embeds the f
  name: Ballerina Triggers API
  slug: ballerina-triggers-api
- baseURL: https://api.central.ballerina.io
  baseurl_source: declared
  description: Retrieve the complete generated API documentation model for one published package version — every module, client, function, record, type, constant, error, listener, annotation and enum, in both a nest
  name: Ballerina Docs API
  slug: ballerina-docs-api
artifact_total: 86
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ballerina Connectors API
  slug: open-ballerina-connectors-api
- collection_type: open
  name: Ballerina Docs API
  slug: open-ballerina-docs-api
- collection_type: open
  name: Ballerina Packages API
  slug: open-ballerina-packages-api
- collection_type: open
  name: Ballerina Triggers API
  slug: open-ballerina-triggers-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/agentic-access/ballerina-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ballerina-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/security/ballerina-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ballerina-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ballerina-platform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ballerinalang
- group: company
  title: ''
  type: Website
  url: https://ballerina.io/
- group: other
  title: ''
  type: CaseStudies
  url: https://ballerina.io/case-studies/
- group: learn
  title: ''
  type: Learning
  url: https://ballerina.io/learn/
- group: other
  title: ''
  type: Events
  url: https://ballerina.io/community/events/
- group: company
  title: ''
  type: Newsletter
  url: https://ballerina.io/community/#subscribe-to-our-newsletter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ballerina.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ballerina.io/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://ballerina.io/security-policy/
- group: other
  title: ''
  type: Trademark
  url: https://ballerina.io/trademark-usage-policy/
- group: company
  title: ''
  type: Blog
  url: https://blog.ballerina.io/
- group: build
  title: ''
  type: Libraries
  url: https://central.ballerina.io/ballerina-library
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/rules/ballerina-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/ballerina-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/vocabulary/ballerina-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/ballerina-vocabulary.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://ballerina.io/learn/
- group: start
  title: ''
  type: GettingStarted
  url: https://ballerina.io/learn/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://lib.ballerina.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://central.ballerina.io/
- group: start
  title: ''
  type: SignUp
  url: https://central.ballerina.io/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ballerinalang
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/packages/ballerina-packages.yml
  title: ''
  type: Packages
  url: packages/ballerina-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/cli/ballerina-cli.yml
  title: ''
  type: CLI
  url: cli/ballerina-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/mcp/ballerina-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ballerina-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/mcp/ballerina-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ballerina-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/llms/ballerina-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ballerina-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/authentication/ballerina-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ballerina-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/conventions/ballerina-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ballerina-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/errors/ballerina-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ballerina-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/lifecycle/ballerina-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ballerina-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/changelog/ballerina-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ballerina-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/conformance/ballerina-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ballerina-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/data-model/ballerina-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ballerina-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/security/ballerina-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ballerina-vulnerability-disclosure.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/plans/ballerina-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ballerina-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/rate-limits/ballerina-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ballerina-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/json-schema/central-api-package-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/central-api-package-schema.json
created: '2025-06-05'
description: 'Ballerina is an open-source programming language for the cloud, created and maintained by WSO2, whose type system, syntax and tooling are built around network interaction: services, clients, data transformation and integration are language constructs rather than framework add-ons. It ships first-party generators for OpenAPI, AsyncAPI, GraphQL, gRPC, WSDL, EDI and FHIR, a package registry called Ballerina Central with a public read API, and a first-party MCP server and Agent Skills for coding agents.'
examples:
- key_count: 8
  name: Central Api Connector Example
  slug: central-api-connector-example
- key_count: 4
  name: Central Api Connector Search Response Example
  slug: central-api-connector-search-response-example
- key_count: 5
  name: Central Api Module Example
  slug: central-api-module-example
- key_count: 3
  name: Central Api Package Docs Example
  slug: central-api-package-docs-example
- key_count: 28
  name: Central Api Package Example
  slug: central-api-package-example
- key_count: 6
  name: Central Api Package Fulltext Search Response Example
  slug: central-api-package-fulltext-search-response-example
- key_count: 4
  name: Central Api Package Search Response Example
  slug: central-api-package-search-response-example
- key_count: 8
  name: Central Api Trigger Example
  slug: central-api-trigger-example
- key_count: 4
  name: Central Api Trigger Search Response Example
  slug: central-api-trigger-search-response-example
features:
- name: Web Services
- name: Working With Data
- name: Restful API
- name: gRPC API
- name: GraphQL API
- name: Kafka Consumer
- name: Kafka Producer
- name: Databases
- name: LLMS
- name: WSDL
- name: Sequence Diagrams
- name: Flowcharts
- name: GraphQL CLI
- name: Git-based workflow
- name: VS Code Integration
- name: Diagramming
- name: Declarative data processing
- name: Model optionality
- name: Model choices as discriminate unions
- name: Model data as data
- name: Pattern matching
- name: Data validation at the boundary
- name: Data immutability
- name: XML support
- name: JSON support
- name: Model data streams
- name: Model tabular data
finops:
- name: Ballerina Finops
  service_category: API
  slug: ballerina-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ballerina.png
json_schemas:
- name: ApiDocs
  property_count: 3
  slug: central-api-api-docs
- name: BadRequestError
  property_count: 0
  slug: central-api-bad-request-error
- name: Connector
  property_count: 8
  slug: central-api-connector
- name: ConnectorSearchResponse
  property_count: 4
  slug: central-api-connector-search-response
- name: Module
  property_count: 5
  slug: central-api-module
- name: NotFoundMessage
  property_count: 1
  slug: central-api-not-found-message
- name: PackageFullTextSearchResponse
  property_count: 0
  slug: central-api-package-full-text-search-response
- name: Package
  property_count: 28
  slug: central-api-package
- name: PackageSearchResponse
  property_count: 4
  slug: central-api-package-search-response
- name: Trigger
  property_count: 8
  slug: central-api-trigger
- name: TriggerSearchResponse
  property_count: 4
  slug: central-api-trigger-search-response
json_structures:
- name: Central Api Api Docs Structure
  property_count: 3
  slug: central-api-api-docs-structure
- name: Central Api Bad Request Error Structure
  property_count: 0
  slug: central-api-bad-request-error-structure
- name: Central Api Connector Search Response Structure
  property_count: 4
  slug: central-api-connector-search-response-structure
- name: Central Api Connector Structure
  property_count: 8
  slug: central-api-connector-structure
- name: Central Api Module Structure
  property_count: 5
  slug: central-api-module-structure
- name: Central Api Not Found Message Structure
  property_count: 1
  slug: central-api-not-found-message-structure
- name: Central Api Package Full Text Search Response Structure
  property_count: 0
  slug: central-api-package-full-text-search-response-structure
- name: Central Api Package Search Response Structure
  property_count: 4
  slug: central-api-package-search-response-structure
- name: Central Api Package Structure
  property_count: 28
  slug: central-api-package-structure
- name: Central Api Trigger Search Response Structure
  property_count: 4
  slug: central-api-trigger-search-response-structure
- name: Central Api Trigger Structure
  property_count: 8
  slug: central-api-trigger-structure
jsonld:
- class_count: 11
  name: Ballerina Context
  property_count: 47
  slug: ballerina-context
layout: provider
mcp_servers:
- description: WSO2 ships a first-party MCP server for Ballerina called `ballerina-library`. It runs over stdio as part of the `ballerina` Claude Code plugin (registered from the ballerina-skills marketplace) and ex
  name: Ballerina MCP Server
  slug: ballerina-mcp-server
modified: '2026-09-04'
name: Ballerina
nav: Providers
network: true
overview: 'Ballerina publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Packages API, Connectors API, Triggers API, and 1 more. Tagged areas include Integration, Orchestration, Open Source, Programming Language, and Package Registry.


  The Ballerina catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ballerina''s developer surface includes engineering blog, documentation, getting-started guide, API reference, signup flow, support, CLI, and 34 more developer resources.'
plans:
- name: Ballerina Plans Pricing
  plan_count: 0
  slug: ballerina-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Ballerina Rate Limits
  slug: ballerina-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ballerina API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ballerina-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Ballerina API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 9
  slug: ballerina-spectral-rules
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 59.5
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 28.9
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/screenshots/ballerina-2026-06-20T172929.png
security:
- kind: authentication
  name: Ballerina Authentication
  slug: ballerina-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ballerina Domain Security
  slug: ballerina-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ballerina Vulnerability Disclosure
  slug: ballerina-vulnerability-disclosure
  summary_line: Hackerone
slug: ballerina
tags:
- Integration
- Orchestration
- Open Source
- Programming Language
- Package Registry
- Developer Tools
- Code Generation
- Agent Skills
use_cases:
- name: Integration
- name: Healthcare
- name: Data-oriented programming
- name: Event-Driven Architecture (EDA)
- name: B2B integrations
- name: ETL
- name: Microservices
- name: Backends for Frontends
website: https://ballerina.io/
---
