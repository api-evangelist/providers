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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ballerina Agentic Access
  operation_count: 9
  slug: ballerina-agentic-access
  summary_line: 9 operations
api_count: 3
apis:
- description: The Connectors API from Ballerina — 2 operation(s) for connectors.
  name: Ballerina Connectors API
  slug: ballerina-connectors-api
- description: The Organizations API from Ballerina — 2 operation(s) for organizations.
  name: Ballerina Organizations API
  slug: ballerina-organizations-api
- description: The Packages API from Ballerina — 5 operation(s) for packages.
  name: Ballerina Packages API
  slug: ballerina-packages-api
artifact_total: 82
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ballerina Central API
  slug: open-ballerina-central-api
- collection_type: open
  name: Ballerina Central Connectors API
  slug: open-ballerina-connectors-api
- collection_type: open
  name: Ballerina Central Connectors Organizations API
  slug: open-ballerina-organizations-api
- collection_type: open
  name: Ballerina Central Connectors Packages API
  slug: open-ballerina-packages-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ballerina-agentic-access.yml
- group: auth
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
- group: learn
  title: ''
  type: Learning
  url: https://ballerina.io/learn/
- group: learn
  title: ''
  type: Learning
  url: https://ballerina.io/learn/
- group: build
  title: ''
  type: Packages
  url: https://central.ballerina.io/
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
  title: ''
  type: SpectralRules
  url: rules/ballerina-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ballerina-vocabulary.yaml
created: '2025-06-05'
description: Integration problems have been solved by restricted drag-and-drop tools/DSLs or generic programming languages that dont understand the unique challenges of integrations.
examples:
- key_count: 7
  name: Central Api Connector Example
  slug: central-api-connector-example
- key_count: 4
  name: Central Api Connector Search Response Example
  slug: central-api-connector-search-response-example
- key_count: 6
  name: Central Api Connector Summary Example
  slug: central-api-connector-summary-example
- key_count: 5
  name: Central Api Module Example
  slug: central-api-module-example
- key_count: 4
  name: Central Api Organization Example
  slug: central-api-organization-example
- key_count: 1
  name: Central Api Package Docs Example
  slug: central-api-package-docs-example
- key_count: 13
  name: Central Api Package Example
  slug: central-api-package-example
- key_count: 4
  name: Central Api Package Search Response Example
  slug: central-api-package-search-response-example
- key_count: 11
  name: Central Api Package Summary Example
  slug: central-api-package-summary-example
- key_count: 9
  name: Central Api Package Version Example
  slug: central-api-package-version-example
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
graphqls:
- description: ''
  name: Ballerina GraphQL API
  slug: ballerina-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ballerina.png
json_schemas:
- name: Connector
  property_count: 7
  slug: central-api-connector
- name: ConnectorSearchResponse
  property_count: 4
  slug: central-api-connector-search-response
- name: ConnectorSummary
  property_count: 6
  slug: central-api-connector-summary
- name: Module
  property_count: 5
  slug: central-api-module
- name: Organization
  property_count: 4
  slug: central-api-organization
- name: PackageDocs
  property_count: 1
  slug: central-api-package-docs
- name: Package
  property_count: 13
  slug: central-api-package
- name: PackageSearchResponse
  property_count: 4
  slug: central-api-package-search-response
- name: PackageSummary
  property_count: 11
  slug: central-api-package-summary
- name: PackageVersion
  property_count: 9
  slug: central-api-package-version
json_structures:
- name: Central Api Connector Search Response Structure
  property_count: 4
  slug: central-api-connector-search-response-structure
- name: Central Api Connector Structure
  property_count: 7
  slug: central-api-connector-structure
- name: Central Api Connector Summary Structure
  property_count: 6
  slug: central-api-connector-summary-structure
- name: Central Api Module Structure
  property_count: 5
  slug: central-api-module-structure
- name: Central Api Organization Structure
  property_count: 4
  slug: central-api-organization-structure
- name: Central Api Package Docs Structure
  property_count: 1
  slug: central-api-package-docs-structure
- name: Central Api Package Search Response Structure
  property_count: 4
  slug: central-api-package-search-response-structure
- name: Central Api Package Structure
  property_count: 13
  slug: central-api-package-structure
- name: Central Api Package Summary Structure
  property_count: 11
  slug: central-api-package-summary-structure
- name: Central Api Package Version Structure
  property_count: 9
  slug: central-api-package-version-structure
jsonld:
- class_count: 10
  name: Ballerina Context
  property_count: 27
  slug: ballerina-context
layout: provider
modified: '2026-04-21'
name: Ballerina
nav: Providers
network: true
overview: 'Ballerina publishes 3 APIs on the [APIs.io](https://apis.io/) network: Connectors API, Organizations API, and Packages API. Tagged areas include Integrations, Orchestrations, Open Source, and Programming Language.


  The Ballerina catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ballerina''s developer surface includes engineering blog and 19 more developer resources.'
plans:
- name: Ballerina Plans Pricing
  plan_count: 3
  slug: ballerina-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Ballerina Rate Limits
  slug: ballerina-rate-limits
rules:
- name: Ballerina API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ballerina-jsonschema-spectral-rules
- name: Ballerina API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 9
  slug: ballerina-spectral-rules
score:
  band: thin
  composite: 40.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 65.7
    developer_ergonomics: 2.2
    discoverability: 46.3
    governance: 68.8
    operational_transparency: 23.7
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ballerina/refs/heads/main/screenshots/ballerina-2026-06-20T172929.png
security:
- kind: domain-security
  name: Ballerina Domain Security
  slug: ballerina-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ballerina
tags:
- Integrations
- Orchestrations
- Open Source
- Programming Language
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
