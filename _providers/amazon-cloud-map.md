---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amazon Cloud Map Agentic Access
  operation_count: 6
  slug: amazon-cloud-map-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- description: Operations for registering and discovering service instances
  name: Amazon Cloud Map Instances API
  slug: amazon-cloud-map-instances-api
- description: Operations for managing service discovery namespaces
  name: Amazon Cloud Map Namespaces API
  slug: amazon-cloud-map-namespaces-api
- description: Operations for managing services within namespaces
  name: Amazon Cloud Map Services API
  slug: amazon-cloud-map-services-api
artifact_total: 64
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloud-map-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloud-map-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloud-map-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloud-map-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-cloud-map-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloud-map/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloud-map/
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
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/compute/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudmap/
- group: start
  title: ''
  type: SignUp
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-cloud-map
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloud-map-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloud-map-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloud-map-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloud-map-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloud-map-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloud-map-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-cloud-map-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-cloud-map-lifecycle.yml
created: '2026-03-16'
description: Amazon Cloud Map is a cloud resource discovery service that maintains an updated registry of application resources and their locations. Define custom names for application resources and use Cloud Map to dynamically discover service dependencies with integrated health checking and automatic updates.
examples:
- key_count: 5
  name: Cloud Map Create Service Request Example
  slug: cloud-map-create-service-request-example
- key_count: 1
  name: Cloud Map Create Service Response Example
  slug: cloud-map-create-service-response-example
- key_count: 4
  name: Cloud Map Discover Instances Request Example
  slug: cloud-map-discover-instances-request-example
- key_count: 1
  name: Cloud Map Discover Instances Response Example
  slug: cloud-map-discover-instances-response-example
- key_count: 5
  name: Cloud Map Http Instance Summary Example
  slug: cloud-map-http-instance-summary-example
- key_count: 2
  name: Cloud Map Instance Example
  slug: cloud-map-instance-example
- key_count: 2
  name: Cloud Map List Instances Response Example
  slug: cloud-map-list-instances-response-example
- key_count: 2
  name: Cloud Map List Namespaces Response Example
  slug: cloud-map-list-namespaces-response-example
- key_count: 2
  name: Cloud Map List Services Response Example
  slug: cloud-map-list-services-response-example
- key_count: 6
  name: Cloud Map Namespace Example
  slug: cloud-map-namespace-example
- key_count: 3
  name: Cloud Map Register Instance Request Example
  slug: cloud-map-register-instance-request-example
- key_count: 1
  name: Cloud Map Register Instance Response Example
  slug: cloud-map-register-instance-response-example
- key_count: 6
  name: Cloud Map Service Example
  slug: cloud-map-service-example
features:
- description: Maintain an up-to-date registry of application resources with custom naming.
  name: Service Registry
- description: Continuously monitor health of every IP-based component and route only to healthy endpoints.
  name: Health Monitoring
- description: Automatically update service registries as services scale up or down.
  name: Dynamic Discovery
- description: Define custom names for application resources rather than hardcoding IP addresses.
  name: Custom Names
- description: Maintain service registries across different deployment environments, regions, and application versions.
  name: Multi-Environment Support
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloud-map.png
integrations:
- description: Automatically register ECS task IPs in Cloud Map as containers launch.
  name: Amazon ECS
- description: Integrate Kubernetes service discovery with Cloud Map for hybrid environments.
  name: Amazon EKS
- description: DNS-based service discovery backed by Route 53 private hosted zones.
  name: Amazon Route 53
- description: Use Cloud Map as the service registry for App Mesh virtual services.
  name: AWS App Mesh
- description: Control access to Cloud Map namespaces with IAM policies.
  name: AWS IAM
json_schemas:
- name: CreateServiceRequest
  property_count: 5
  slug: cloud-map-create-service-request
- name: CreateServiceResponse
  property_count: 1
  slug: cloud-map-create-service-response
- name: DiscoverInstancesRequest
  property_count: 4
  slug: cloud-map-discover-instances-request
- name: DiscoverInstancesResponse
  property_count: 1
  slug: cloud-map-discover-instances-response
- name: HttpInstanceSummary
  property_count: 5
  slug: cloud-map-http-instance-summary
- name: Instance
  property_count: 2
  slug: cloud-map-instance
- name: ListInstancesResponse
  property_count: 2
  slug: cloud-map-list-instances-response
- name: ListNamespacesResponse
  property_count: 2
  slug: cloud-map-list-namespaces-response
- name: ListServicesResponse
  property_count: 2
  slug: cloud-map-list-services-response
- name: Namespace
  property_count: 6
  slug: cloud-map-namespace
- name: RegisterInstanceRequest
  property_count: 3
  slug: cloud-map-register-instance-request
- name: RegisterInstanceResponse
  property_count: 1
  slug: cloud-map-register-instance-response
- name: Service
  property_count: 6
  slug: cloud-map-service
json_structures:
- name: Cloud Map Create Service Request Structure
  property_count: 5
  slug: cloud-map-create-service-request-structure
- name: Cloud Map Create Service Response Structure
  property_count: 1
  slug: cloud-map-create-service-response-structure
- name: Cloud Map Discover Instances Request Structure
  property_count: 4
  slug: cloud-map-discover-instances-request-structure
- name: Cloud Map Discover Instances Response Structure
  property_count: 1
  slug: cloud-map-discover-instances-response-structure
- name: Cloud Map Http Instance Summary Structure
  property_count: 5
  slug: cloud-map-http-instance-summary-structure
- name: Cloud Map Instance Structure
  property_count: 2
  slug: cloud-map-instance-structure
- name: Cloud Map List Instances Response Structure
  property_count: 2
  slug: cloud-map-list-instances-response-structure
- name: Cloud Map List Namespaces Response Structure
  property_count: 2
  slug: cloud-map-list-namespaces-response-structure
- name: Cloud Map List Services Response Structure
  property_count: 2
  slug: cloud-map-list-services-response-structure
- name: Cloud Map Namespace Structure
  property_count: 6
  slug: cloud-map-namespace-structure
- name: Cloud Map Register Instance Request Structure
  property_count: 3
  slug: cloud-map-register-instance-request-structure
- name: Cloud Map Register Instance Response Structure
  property_count: 1
  slug: cloud-map-register-instance-response-structure
- name: Cloud Map Service Structure
  property_count: 6
  slug: cloud-map-service-structure
jsonld:
- class_count: 15
  name: Amazon Cloud Map Context
  property_count: 20
  slug: amazon-cloud-map-context
layout: provider
modified: '2026-06-20'
name: Amazon Cloud Map
nav: Providers
network: true
overview: 'Amazon Cloud Map publishes 3 APIs on the [APIs.io](https://apis.io/) network: Instances API, Namespaces API, and Services API. Tagged areas include Cloud Map, Service Discovery, Microservices, and DNS.


  The Amazon Cloud Map catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Cloud Map''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 20 more developer resources.'
random_paper: 9
rules:
- name: Amazon Cloud Map API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-cloud-map-jsonschema-spectral-rules
- name: Amazon Cloud Map API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 12
  slug: amazon-cloud-map-spectral-rules
score:
  band: developing
  composite: 55.0
  delta: -4.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 70.3
    developer_ergonomics: 41.3
    discoverability: 83.3
    governance: 80.2
    operational_transparency: 21.1
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-map/refs/heads/main/screenshots/amazon-cloud-map-2026-07-25T195942.png
security:
- kind: authentication
  name: Amazon Cloud Map Authentication
  slug: amazon-cloud-map-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Cloud Map Domain Security
  slug: amazon-cloud-map-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloud Map Vulnerability Disclosure
  slug: amazon-cloud-map-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloud Map Trust Center
  slug: amazon-cloud-map-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloud-map
tags:
- Cloud Map
- Service Discovery
- Microservices
- DNS
use_cases:
- description: Enable services to locate dependencies in dynamic container environments with ECS and EKS.
  name: Microservice Discovery
- description: Ensure traffic routes only to verified healthy service endpoints.
  name: Health-Based Routing
- description: Automatically register and deregister services during CI/CD pipeline deployments.
  name: CI/CD Integration
- description: Discover services across multiple AWS regions with a unified namespace.
  name: Multi-Region Service Mesh
website: https://aws.amazon.com/cloud-map/
---
