---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Route 53 Agentic Access
  operation_count: 9
  slug: amazon-route-53-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: Operations for managing health checks.
  name: Amazon Route 53 Health Checks API
  slug: amazon-route-53-health-checks-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: Operations for managing DNS hosted zones.
  name: Amazon Route 53 Hosted Zones API
  slug: amazon-route-53-hosted-zones-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: Operations for managing DNS resource record sets.
  name: Amazon Route 53 Resource Record Sets API
  slug: amazon-route-53-resource-record-sets-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Cidrcollection API from Amazon Route 53 — 3 operation(s) for route 53 cidrcollection.
  name: Amazon Route 53 Route 53 Cidrcollection API
  slug: amazon-route-53-cidrcollection-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Delegationset API from Amazon Route 53 — 2 operation(s) for route 53 delegationset.
  name: Amazon Route 53 Route 53 Delegationset API
  slug: amazon-route-53-delegationset-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Operations API from Amazon Route 53 — 30 operation(s) for route 53 operations.
  name: Amazon Route 53 Route 53 Operations API
  slug: amazon-route-53-operations-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Queryloggingconfig API from Amazon Route 53 — 2 operation(s) for route 53 queryloggingconfig.
  name: Amazon Route 53 Route 53 Queryloggingconfig API
  slug: amazon-route-53-queryloggingconfig-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Tags API from Amazon Route 53 — 2 operation(s) for route 53 tags.
  name: Amazon Route 53 Route 53 Tags API
  slug: amazon-route-53-tags-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Trafficpolicy API from Amazon Route 53 — 3 operation(s) for route 53 trafficpolicy.
  name: Amazon Route 53 Route 53 Trafficpolicy API
  slug: amazon-route-53-trafficpolicy-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Trafficpolicyinstance API from Amazon Route 53 — 2 operation(s) for route 53 trafficpolicyinstance.
  name: Amazon Route 53 Route 53 Trafficpolicyinstance API
  slug: amazon-route-53-trafficpolicyinstance-api
- baseURL_template: https://route53.{region}.amazonaws.com
  baseurl_source: spec_template
  description: The Route 53 Trafficpolicyinstances API from Amazon Route 53 — 3 operation(s) for route 53 trafficpolicyinstances.
  name: Amazon Route 53 Route 53 Trafficpolicyinstances API
  slug: amazon-route-53-trafficpolicyinstances-api
artifact_total: 85
collections:
- collection_type: postman
  name: Amazon Route 53 Health Checks API
  slug: postman-amazon-route-53-health-checks-api
- collection_type: postman
  name: Amazon Route 53 Health Checks Hosted Zones API
  slug: postman-amazon-route-53-hosted-zones-api
- collection_type: postman
  name: Amazon Route 53 Health Checks Resource Record Sets API
  slug: postman-amazon-route-53-resource-record-sets-api
- collection_type: open
  name: Amazon Route 53 Health Checks API
  slug: open-amazon-route-53-health-checks-api
- collection_type: open
  name: Amazon Route 53 Health Checks Hosted Zones API
  slug: open-amazon-route-53-hosted-zones-api
- collection_type: open
  name: Amazon Route 53 Health Checks Resource Record Sets API
  slug: open-amazon-route-53-resource-record-sets-api
- collection_type: open
  name: Amazon Route 53 API
  slug: open-amazon-route-53
common:
- group: other
  href: https://artifacts.apis.io/amazon-route-53/capabilities/amazon-route-53-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-route-53-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-route-53/plans/amazon-route-53-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-route-53-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-route-53/rate-limits/amazon-route-53-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-route-53-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-route-53/finops/amazon-route-53-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-route-53-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-route-53/overview
- group: agent
  href: https://artifacts.apis.io/amazon-route-53/agentic-access/amazon-route-53-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-route-53-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-route-53/security/amazon-route-53-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-route-53-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-route-53/security/amazon-route-53-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-route-53-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-route-53/security/amazon-route-53-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-route-53-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-route-53/authentication/amazon-route-53-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-route-53-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/route53/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/aws
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/route53/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-route53
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-ld/amazon-route-53-context-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-route-53-context-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-ld/amazon-route-53-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-route-53-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-hosted-zone-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-hosted-zone-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-change-info-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-change-info-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-change-resource-record-sets-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-change-resource-record-sets-request-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-change-resource-record-sets-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-change-resource-record-sets-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-create-health-check-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-create-health-check-request-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-create-health-check-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-create-health-check-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-create-hosted-zone-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-create-hosted-zone-request-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-create-hosted-zone-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-create-hosted-zone-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-delegation-set-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-delegation-set-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-delete-hosted-zone-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-delete-hosted-zone-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-get-health-check-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-get-health-check-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-get-hosted-zone-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-get-hosted-zone-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-health-check-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-health-check-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-hosted-zone-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-hosted-zone-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-list-health-checks-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-list-health-checks-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-list-hosted-zones-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-list-hosted-zones-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-list-resource-record-sets-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-list-resource-record-sets-response-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/json-schema/amazon-route-53-openapi-resource-record-set-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-route-53-openapi-resource-record-set-schema.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-hosted-zone-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-hosted-zone-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-change-info-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-change-info-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-change-resource-record-sets-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-change-resource-record-sets-request-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-change-resource-record-sets-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-change-resource-record-sets-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-create-health-check-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-create-health-check-request-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-create-health-check-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-create-health-check-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-create-hosted-zone-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-create-hosted-zone-request-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-create-hosted-zone-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-create-hosted-zone-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-delegation-set-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-delegation-set-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-delete-hosted-zone-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-delete-hosted-zone-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-get-health-check-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-get-health-check-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-get-hosted-zone-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-get-hosted-zone-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-health-check-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-health-check-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-hosted-zone-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-hosted-zone-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-list-health-checks-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-list-health-checks-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-list-hosted-zones-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-list-hosted-zones-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-list-resource-record-sets-response-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-list-resource-record-sets-response-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/json-structure/amazon-route-53-openapi-resource-record-set-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-route-53-openapi-resource-record-set-structure.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-hosted-zone-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-hosted-zone-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-change-info-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-change-info-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-change-resource-record-sets-request-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-change-resource-record-sets-request-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-change-resource-record-sets-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-change-resource-record-sets-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-create-health-check-request-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-create-health-check-request-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-create-health-check-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-create-health-check-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-create-hosted-zone-request-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-create-hosted-zone-request-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-create-hosted-zone-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-create-hosted-zone-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-delegation-set-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-delegation-set-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-delete-hosted-zone-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-delete-hosted-zone-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-get-health-check-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-get-health-check-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-get-hosted-zone-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-get-hosted-zone-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-health-check-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-health-check-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-hosted-zone-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-hosted-zone-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-list-health-checks-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-list-health-checks-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-list-hosted-zones-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-list-hosted-zones-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-list-resource-record-sets-response-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-list-resource-record-sets-response-example.json
- group: build
  href: https://artifacts.apis.io/amazon-route-53/examples/amazon-route-53-openapi-resource-record-set-example.json
  title: ''
  type: Examples
  url: examples/amazon-route-53-openapi-resource-record-set-example.json
- group: design
  href: https://artifacts.apis.io/amazon-route-53/rules/amazon-route-53-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-route-53-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-route-53/vocabulary/amazon-route-53-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-route-53-vocabulary.yaml
- group: docs
  href: https://artifacts.apis.io/amazon-route-53/openapi/_original/amazon-route-53-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-route-53-openapi.yml
description: Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service that provides DNS routing, domain name registration, and health checking capabilities. Route 53 connects user requests to internet applications running on AWS or on-premises infrastructure, and can be used to route traffic based on latency, geolocation, geoproximity, and weighted round-robin policies.
examples:
- key_count: 8
  name: Amazon Route 53 Hosted Zone Example
  slug: amazon-route-53-hosted-zone-example
- key_count: 4
  name: Amazon Route 53 Openapi Change Info Example
  slug: amazon-route-53-openapi-change-info-example
- key_count: 1
  name: Amazon Route 53 Openapi Change Resource Record Sets Request Example
  slug: amazon-route-53-openapi-change-resource-record-sets-request-example
- key_count: 1
  name: Amazon Route 53 Openapi Change Resource Record Sets Response Example
  slug: amazon-route-53-openapi-change-resource-record-sets-response-example
- key_count: 2
  name: Amazon Route 53 Openapi Create Health Check Request Example
  slug: amazon-route-53-openapi-create-health-check-request-example
- key_count: 1
  name: Amazon Route 53 Openapi Create Health Check Response Example
  slug: amazon-route-53-openapi-create-health-check-response-example
- key_count: 5
  name: Amazon Route 53 Openapi Create Hosted Zone Request Example
  slug: amazon-route-53-openapi-create-hosted-zone-request-example
- key_count: 3
  name: Amazon Route 53 Openapi Create Hosted Zone Response Example
  slug: amazon-route-53-openapi-create-hosted-zone-response-example
- key_count: 3
  name: Amazon Route 53 Openapi Delegation Set Example
  slug: amazon-route-53-openapi-delegation-set-example
- key_count: 1
  name: Amazon Route 53 Openapi Delete Hosted Zone Response Example
  slug: amazon-route-53-openapi-delete-hosted-zone-response-example
- key_count: 1
  name: Amazon Route 53 Openapi Get Health Check Response Example
  slug: amazon-route-53-openapi-get-health-check-response-example
- key_count: 2
  name: Amazon Route 53 Openapi Get Hosted Zone Response Example
  slug: amazon-route-53-openapi-get-hosted-zone-response-example
- key_count: 5
  name: Amazon Route 53 Openapi Health Check Example
  slug: amazon-route-53-openapi-health-check-example
- key_count: 6
  name: Amazon Route 53 Openapi Hosted Zone Example
  slug: amazon-route-53-openapi-hosted-zone-example
- key_count: 5
  name: Amazon Route 53 Openapi List Health Checks Response Example
  slug: amazon-route-53-openapi-list-health-checks-response-example
- key_count: 5
  name: Amazon Route 53 Openapi List Hosted Zones Response Example
  slug: amazon-route-53-openapi-list-hosted-zones-response-example
- key_count: 6
  name: Amazon Route 53 Openapi List Resource Record Sets Response Example
  slug: amazon-route-53-openapi-list-resource-record-sets-response-example
- key_count: 10
  name: Amazon Route 53 Openapi Resource Record Set Example
  slug: amazon-route-53-openapi-resource-record-set-example
finops:
- has_sources: true
  method: derived
  name: Amazon Route 53 Finops
  primary_unit: million queries
  service_category: ''
  slug: amazon-route-53-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-route-53.png
json_schemas:
- name: Amazon Route 53 Hosted Zone
  property_count: 8
  slug: amazon-route-53-hosted-zone
- name: ChangeInfo
  property_count: 4
  slug: amazon-route-53-openapi-change-info
- name: ChangeResourceRecordSetsRequest
  property_count: 1
  slug: amazon-route-53-openapi-change-resource-record-sets-request
- name: ChangeResourceRecordSetsResponse
  property_count: 1
  slug: amazon-route-53-openapi-change-resource-record-sets-response
- name: CreateHealthCheckRequest
  property_count: 2
  slug: amazon-route-53-openapi-create-health-check-request
- name: CreateHealthCheckResponse
  property_count: 1
  slug: amazon-route-53-openapi-create-health-check-response
- name: CreateHostedZoneRequest
  property_count: 5
  slug: amazon-route-53-openapi-create-hosted-zone-request
- name: CreateHostedZoneResponse
  property_count: 3
  slug: amazon-route-53-openapi-create-hosted-zone-response
- name: DelegationSet
  property_count: 3
  slug: amazon-route-53-openapi-delegation-set
- name: DeleteHostedZoneResponse
  property_count: 1
  slug: amazon-route-53-openapi-delete-hosted-zone-response
- name: GetHealthCheckResponse
  property_count: 1
  slug: amazon-route-53-openapi-get-health-check-response
- name: GetHostedZoneResponse
  property_count: 2
  slug: amazon-route-53-openapi-get-hosted-zone-response
- name: HealthCheck
  property_count: 5
  slug: amazon-route-53-openapi-health-check
- name: HostedZone
  property_count: 6
  slug: amazon-route-53-openapi-hosted-zone
- name: ListHealthChecksResponse
  property_count: 5
  slug: amazon-route-53-openapi-list-health-checks-response
- name: ListHostedZonesResponse
  property_count: 5
  slug: amazon-route-53-openapi-list-hosted-zones-response
- name: ListResourceRecordSetsResponse
  property_count: 6
  slug: amazon-route-53-openapi-list-resource-record-sets-response
- name: ResourceRecordSet
  property_count: 10
  slug: amazon-route-53-openapi-resource-record-set
json_structures:
- name: Amazon Route 53 Hosted Zone Structure
  property_count: 8
  slug: amazon-route-53-hosted-zone-structure
- name: Amazon Route 53 Openapi Change Info Structure
  property_count: 4
  slug: amazon-route-53-openapi-change-info-structure
- name: Amazon Route 53 Openapi Change Resource Record Sets Request Structure
  property_count: 1
  slug: amazon-route-53-openapi-change-resource-record-sets-request-structure
- name: Amazon Route 53 Openapi Change Resource Record Sets Response Structure
  property_count: 1
  slug: amazon-route-53-openapi-change-resource-record-sets-response-structure
- name: Amazon Route 53 Openapi Create Health Check Request Structure
  property_count: 2
  slug: amazon-route-53-openapi-create-health-check-request-structure
- name: Amazon Route 53 Openapi Create Health Check Response Structure
  property_count: 1
  slug: amazon-route-53-openapi-create-health-check-response-structure
- name: Amazon Route 53 Openapi Create Hosted Zone Request Structure
  property_count: 5
  slug: amazon-route-53-openapi-create-hosted-zone-request-structure
- name: Amazon Route 53 Openapi Create Hosted Zone Response Structure
  property_count: 3
  slug: amazon-route-53-openapi-create-hosted-zone-response-structure
- name: Amazon Route 53 Openapi Delegation Set Structure
  property_count: 3
  slug: amazon-route-53-openapi-delegation-set-structure
- name: Amazon Route 53 Openapi Delete Hosted Zone Response Structure
  property_count: 1
  slug: amazon-route-53-openapi-delete-hosted-zone-response-structure
- name: Amazon Route 53 Openapi Get Health Check Response Structure
  property_count: 1
  slug: amazon-route-53-openapi-get-health-check-response-structure
- name: Amazon Route 53 Openapi Get Hosted Zone Response Structure
  property_count: 2
  slug: amazon-route-53-openapi-get-hosted-zone-response-structure
- name: Amazon Route 53 Openapi Health Check Structure
  property_count: 5
  slug: amazon-route-53-openapi-health-check-structure
- name: Amazon Route 53 Openapi Hosted Zone Structure
  property_count: 6
  slug: amazon-route-53-openapi-hosted-zone-structure
- name: Amazon Route 53 Openapi List Health Checks Response Structure
  property_count: 5
  slug: amazon-route-53-openapi-list-health-checks-response-structure
- name: Amazon Route 53 Openapi List Hosted Zones Response Structure
  property_count: 5
  slug: amazon-route-53-openapi-list-hosted-zones-response-structure
- name: Amazon Route 53 Openapi List Resource Record Sets Response Structure
  property_count: 6
  slug: amazon-route-53-openapi-list-resource-record-sets-response-structure
- name: Amazon Route 53 Openapi Resource Record Set Structure
  property_count: 10
  slug: amazon-route-53-openapi-resource-record-set-structure
jsonld:
- class_count: 14
  name: Amazon Route 53 Context
  property_count: 55
  slug: amazon-route-53-context-context
- class_count: 0
  name: Amazon Route 53 Context
  property_count: 4
  slug: amazon-route-53-context
layout: provider
modified: '2026-05-19'
name: Amazon Route 53
nav: Providers
network: true
overview: 'Amazon Route 53 publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health Checks API, Hosted Zones API, Resource Record Sets API, and 8 more. Tagged areas include Amazon Web Services, DNS, Domain Registration, Health Checks, and Routing.


  The Amazon Route 53 catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Route 53''s developer surface includes authentication, developer portal, documentation, support, engineering blog, GitHub presence, signup flow, and 80 more developer resources.'
plans:
- name: Amazon Route 53 Plans Pricing
  plan_count: 22
  slug: amazon-route-53-plans-pricing
- name: Amazon Route 53 Price Estimates
  plan_count: 0
  slug: amazon-route-53-price-estimates
random_paper: 7
rate_limits:
- limit_count: 2
  name: Amazon Route 53 Rate Limits
  slug: amazon-route-53-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon Route 53 — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-route-53-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: Amazon Route 53 API Rules
  rule_count: 26
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 17
  slug: amazon-route-53-spectral-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 12.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 82.9
    contract_governance: 27.3
    contract_quality: 73.5
    developer_ergonomics: 39.3
    discoverability: 42.9
    operational_transparency: 36.8
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-route-53/amazon-route-53-2026-06-20T171815.png
security:
- kind: authentication
  name: Amazon Route 53 Authentication
  slug: amazon-route-53-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Route 53 Domain Security
  slug: amazon-route-53-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Route 53 Vulnerability Disclosure
  slug: amazon-route-53-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Route 53 Trust Center
  slug: amazon-route-53-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-route-53
tags:
- Amazon Web Services
- DNS
- Domain Registration
- Health Checks
- Routing
website: https://aws.amazon.com/
---
