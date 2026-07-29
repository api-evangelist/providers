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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Shield Agentic Access
  operation_count: 7
  slug: amazon-shield-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 7
apis:
- description: The Amazon Shield REST API API from Amazon Shield — 1 operation(s) for amazon shield rest api.
  name: Amazon Shield Amazon Shield REST API API
  slug: amazon-shield-amazon-shield-rest-api-api
- description: 'The #CreateProtectionGroup API from Amazon Shield — 1 operation(s) for #createprotectiongroup.'
  name: 'Amazon Shield #CreateProtectionGroup API'
  slug: amazon-shield-createprotectiongroup-api
- description: 'The #CreateSubscription API from Amazon Shield — 1 operation(s) for #createsubscription.'
  name: 'Amazon Shield #CreateSubscription API'
  slug: amazon-shield-createsubscription-api
- description: 'The #DescribeAttack API from Amazon Shield — 1 operation(s) for #describeattack.'
  name: 'Amazon Shield #DescribeAttack API'
  slug: amazon-shield-describeattack-api
- description: 'The #DescribeProtection API from Amazon Shield — 1 operation(s) for #describeprotection.'
  name: 'Amazon Shield #DescribeProtection API'
  slug: amazon-shield-describeprotection-api
- description: 'The #DescribeSubscription API from Amazon Shield — 1 operation(s) for #describesubscription.'
  name: 'Amazon Shield #DescribeSubscription API'
  slug: amazon-shield-describesubscription-api
- description: 'The #ListProtections API from Amazon Shield — 1 operation(s) for #listprotections.'
  name: 'Amazon Shield #ListProtections API'
  slug: amazon-shield-listprotections-api
artifact_total: 72
collections:
- collection_type: postman
  name: Amazon Shield REST Amazon Shield REST API API
  slug: postman-amazon-shield-amazon-shield-rest-api-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #CreateProtectionGroup API'
  slug: postman-amazon-shield-createprotectiongroup-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #CreateSubscription API'
  slug: postman-amazon-shield-createsubscription-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #DescribeAttack API'
  slug: postman-amazon-shield-describeattack-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #DescribeProtection API'
  slug: postman-amazon-shield-describeprotection-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #DescribeSubscription API'
  slug: postman-amazon-shield-describesubscription-api
- collection_type: postman
  name: 'Amazon Shield REST Amazon Shield REST API #ListProtections API'
  slug: postman-amazon-shield-listprotections-api
- collection_type: open
  name: Amazon Shield REST API
  slug: open-amazon-shield-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-shield/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-shield-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-shield-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-shield-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-shield-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-shield-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/shield/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html
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
  url: https://aws.amazon.com/premiumsupport/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/wafv2/shieldv2
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-shield-context-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-shield-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-attack-detail-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-create-protection-group-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-create-protection-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-create-protection-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-describe-attack-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-describe-attack-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-describe-protection-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-describe-protection-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-list-protections-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-list-protections-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-mitigation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-protection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-summarized-counter-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-api-tag-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-shield-protection-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-attack-detail-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-create-protection-group-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-create-protection-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-create-protection-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-describe-attack-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-describe-attack-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-describe-protection-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-describe-protection-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-list-protections-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-list-protections-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-mitigation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-protection-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-summarized-counter-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-api-tag-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-shield-protection-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-attack-detail-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-create-protection-group-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-create-protection-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-create-protection-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-describe-attack-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-describe-attack-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-describe-protection-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-describe-protection-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-list-protections-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-list-protections-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-mitigation-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-protection-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-summarized-counter-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-api-tag-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-shield-protection-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-shield-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-shield-vocabulary.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amazon-shield-api-openapi.yml
created: '2024-01-15'
description: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. It provides always-on detection and automatic inline mitigations that minimize application downtime and latency, with two tiers of protection - Shield Standard for automatic defense against common attacks and Shield Advanced for enhanced detection and 24/7 access to the DDoS Response Team.
examples:
- key_count: 6
  name: Amazon Shield Api Attack Detail Example
  slug: amazon-shield-api-attack-detail-example
- key_count: 5
  name: Amazon Shield Api Create Protection Group Request Example
  slug: amazon-shield-api-create-protection-group-request-example
- key_count: 3
  name: Amazon Shield Api Create Protection Request Example
  slug: amazon-shield-api-create-protection-request-example
- key_count: 1
  name: Amazon Shield Api Create Protection Response Example
  slug: amazon-shield-api-create-protection-response-example
- key_count: 1
  name: Amazon Shield Api Describe Attack Request Example
  slug: amazon-shield-api-describe-attack-request-example
- key_count: 1
  name: Amazon Shield Api Describe Attack Response Example
  slug: amazon-shield-api-describe-attack-response-example
- key_count: 2
  name: Amazon Shield Api Describe Protection Request Example
  slug: amazon-shield-api-describe-protection-request-example
- key_count: 1
  name: Amazon Shield Api Describe Protection Response Example
  slug: amazon-shield-api-describe-protection-response-example
- key_count: 2
  name: Amazon Shield Api List Protections Request Example
  slug: amazon-shield-api-list-protections-request-example
- key_count: 2
  name: Amazon Shield Api List Protections Response Example
  slug: amazon-shield-api-list-protections-response-example
- key_count: 1
  name: Amazon Shield Api Mitigation Example
  slug: amazon-shield-api-mitigation-example
- key_count: 5
  name: Amazon Shield Api Protection Example
  slug: amazon-shield-api-protection-example
- key_count: 6
  name: Amazon Shield Api Summarized Counter Example
  slug: amazon-shield-api-summarized-counter-example
- key_count: 2
  name: Amazon Shield Api Tag Example
  slug: amazon-shield-api-tag-example
- key_count: 7
  name: Amazon Shield Protection Example
  slug: amazon-shield-protection-example
finops:
- name: Amazon Shield Finops
  service_category: API
  slug: amazon-shield-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AttackDetail
  property_count: 6
  slug: amazon-shield-api-attack-detail
- name: CreateProtectionGroupRequest
  property_count: 5
  slug: amazon-shield-api-create-protection-group-request
- name: CreateProtectionRequest
  property_count: 3
  slug: amazon-shield-api-create-protection-request
- name: CreateProtectionResponse
  property_count: 1
  slug: amazon-shield-api-create-protection-response
- name: DescribeAttackRequest
  property_count: 1
  slug: amazon-shield-api-describe-attack-request
- name: DescribeAttackResponse
  property_count: 1
  slug: amazon-shield-api-describe-attack-response
- name: DescribeProtectionRequest
  property_count: 2
  slug: amazon-shield-api-describe-protection-request
- name: DescribeProtectionResponse
  property_count: 1
  slug: amazon-shield-api-describe-protection-response
- name: ListProtectionsRequest
  property_count: 2
  slug: amazon-shield-api-list-protections-request
- name: ListProtectionsResponse
  property_count: 2
  slug: amazon-shield-api-list-protections-response
- name: Mitigation
  property_count: 1
  slug: amazon-shield-api-mitigation
- name: Protection
  property_count: 5
  slug: amazon-shield-api-protection
- name: SummarizedCounter
  property_count: 6
  slug: amazon-shield-api-summarized-counter
- name: Tag
  property_count: 2
  slug: amazon-shield-api-tag
- name: Amazon Shield Protection
  property_count: 7
  slug: amazon-shield-protection
json_structures:
- name: Amazon Shield Api Attack Detail Structure
  property_count: 6
  slug: amazon-shield-api-attack-detail-structure
- name: Amazon Shield Api Create Protection Group Request Structure
  property_count: 5
  slug: amazon-shield-api-create-protection-group-request-structure
- name: Amazon Shield Api Create Protection Request Structure
  property_count: 3
  slug: amazon-shield-api-create-protection-request-structure
- name: Amazon Shield Api Create Protection Response Structure
  property_count: 1
  slug: amazon-shield-api-create-protection-response-structure
- name: Amazon Shield Api Describe Attack Request Structure
  property_count: 1
  slug: amazon-shield-api-describe-attack-request-structure
- name: Amazon Shield Api Describe Attack Response Structure
  property_count: 1
  slug: amazon-shield-api-describe-attack-response-structure
- name: Amazon Shield Api Describe Protection Request Structure
  property_count: 2
  slug: amazon-shield-api-describe-protection-request-structure
- name: Amazon Shield Api Describe Protection Response Structure
  property_count: 1
  slug: amazon-shield-api-describe-protection-response-structure
- name: Amazon Shield Api List Protections Request Structure
  property_count: 2
  slug: amazon-shield-api-list-protections-request-structure
- name: Amazon Shield Api List Protections Response Structure
  property_count: 2
  slug: amazon-shield-api-list-protections-response-structure
- name: Amazon Shield Api Mitigation Structure
  property_count: 1
  slug: amazon-shield-api-mitigation-structure
- name: Amazon Shield Api Protection Structure
  property_count: 5
  slug: amazon-shield-api-protection-structure
- name: Amazon Shield Api Summarized Counter Structure
  property_count: 6
  slug: amazon-shield-api-summarized-counter-structure
- name: Amazon Shield Api Tag Structure
  property_count: 2
  slug: amazon-shield-api-tag-structure
- name: Amazon Shield Protection Structure
  property_count: 7
  slug: amazon-shield-protection-structure
jsonld:
- class_count: 14
  name: Amazon Shield Context
  property_count: 31
  slug: amazon-shield-context-context
- class_count: 0
  name: Amazon Shield Context
  property_count: 3
  slug: amazon-shield-context
layout: provider
modified: '2026-05-19'
name: Amazon Shield
nav: Providers
network: true
overview: 'Amazon Shield publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Amazon Shield REST API API, #CreateProtectionGroup API, #CreateSubscription API, and 4 more. Tagged areas include DDoS Protection, Networking, and Security.


  The Amazon Shield catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Shield''s developer surface includes authentication, developer portal, documentation, support, signup flow, code examples, and 62 more developer resources.'
plans:
- name: Amazon Shield Plans Pricing
  plan_count: 3
  slug: amazon-shield-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Amazon Shield Rate Limits
  slug: amazon-shield-rate-limits
rules:
- name: Amazon Shield API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-shield-jsonschema-spectral-rules
- name: Amazon Shield API Rules
  rule_count: 24
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 15
  slug: amazon-shield-spectral-rules
score:
  band: strong
  composite: 62.2
  delta: -3.2
  facets:
    commercial_clarity: 81.6
    contract_quality: 67.8
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-shield/refs/heads/main/screenshots/amazon-shield-2026-06-20T171822.png
security:
- kind: authentication
  name: Amazon Shield Authentication
  slug: amazon-shield-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Shield Domain Security
  slug: amazon-shield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Shield Vulnerability Disclosure
  slug: amazon-shield-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Shield Trust Center
  slug: amazon-shield-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-shield
tags:
- DDoS Protection
- Networking
- Security
website: https://aws.amazon.com/
---
