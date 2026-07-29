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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Elastic Load Balancing Agentic Access
  operation_count: 13
  slug: amazon-elastic-load-balancing-agentic-access
  summary_line: 13 operations
api_count: 5
apis:
- description: Operations for creating and managing listeners
  name: Amazon Elastic Load Balancing Listeners API
  slug: amazon-elastic-load-balancing-listeners-api
- description: Operations for creating and managing load balancers
  name: Amazon Elastic Load Balancing Load Balancers API
  slug: amazon-elastic-load-balancing-load-balancers-api
- description: Operations for creating and managing listener rules
  name: Amazon Elastic Load Balancing Rules API
  slug: amazon-elastic-load-balancing-rules-api
- description: Operations for creating and managing target groups
  name: Amazon Elastic Load Balancing Target Groups API
  slug: amazon-elastic-load-balancing-target-groups-api
- description: Operations for registering and deregistering targets
  name: Amazon Elastic Load Balancing Targets API
  slug: amazon-elastic-load-balancing-targets-api
arazzos:
- description: Create a target group and attach a host-header rule to an existing listener.
  name: Amazon Elastic Load Balancing Add a Host-Based Routing Rule
  slug: amazon-elastic-load-balancing-add-host-based-routing-rule-workflow
- description: Look up a load balancer by name and attach a new forwarding listener.
  name: Amazon Elastic Load Balancing Add a Listener to an Existing Load Balancer
  slug: amazon-elastic-load-balancing-add-listener-to-existing-load-balancer-workflow
- description: Attach a path-pattern fixed-response rule to a listener and confirm it.
  name: Amazon Elastic Load Balancing Add a Path-Based Maintenance Rule
  slug: amazon-elastic-load-balancing-add-path-maintenance-rule-workflow
- description: Walk a load balancer's listeners and target groups to inventory its routing.
  name: Amazon Elastic Load Balancing Audit Load Balancer Configuration
  slug: amazon-elastic-load-balancing-audit-load-balancer-configuration-workflow
- description: Resolve a load balancer by name, inventory its listeners, then delete it.
  name: Amazon Elastic Load Balancing Decommission a Load Balancer
  slug: amazon-elastic-load-balancing-decommission-load-balancer-workflow
- description: Confirm a target exists, deregister it, then poll until it has drained.
  name: Amazon Elastic Load Balancing Drain and Deregister a Target
  slug: amazon-elastic-load-balancing-drain-and-deregister-target-workflow
- description: Register a target then poll its health until it reaches the healthy state.
  name: Amazon Elastic Load Balancing Poll Target Health Until Healthy
  slug: amazon-elastic-load-balancing-poll-target-health-until-healthy-workflow
- description: Stand up an Application Load Balancer with a target group, listener, and registered targets.
  name: Amazon Elastic Load Balancing Provision an Application Load Balancer
  slug: amazon-elastic-load-balancing-provision-application-load-balancer-workflow
- description: Stand up a TCP Network Load Balancer with a target group, listener, and registered targets.
  name: Amazon Elastic Load Balancing Provision a Network Load Balancer
  slug: amazon-elastic-load-balancing-provision-network-load-balancer-workflow
- description: Create a target group, register a target, then read back its health state.
  name: Amazon Elastic Load Balancing Register Targets and Check Health
  slug: amazon-elastic-load-balancing-register-targets-and-check-health-workflow
- description: Resolve a load balancer by name and apply an attribute change.
  name: Amazon Elastic Load Balancing Tune Load Balancer Attributes
  slug: amazon-elastic-load-balancing-tune-load-balancer-attributes-workflow
artifact_total: 86
collections:
- collection_type: postman
  name: Amazon Elastic Load Balancing v2 API
  slug: postman-amazon-elastic-load-balancing
- collection_type: open
  name: Amazon Elastic Load Balancing v2 API
  slug: open-amazon-elastic-load-balancing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-elastic-load-balancing-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-elastic-load-balancing-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-elastic-load-balancing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-elastic-load-balancing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-elastic-load-balancing-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-elastic-load-balancing/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-add-host-based-routing-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-add-listener-to-existing-load-balancer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-add-path-maintenance-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-audit-load-balancer-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-decommission-load-balancer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-drain-and-deregister-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-poll-target-health-until-healthy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-provision-application-load-balancer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-provision-network-load-balancer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-register-targets-and-check-health-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-elastic-load-balancing-tune-load-balancer-attributes-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/elasticloadbalancing/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/elasticloadbalancing/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/ec2/home#LoadBalancers/
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
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/elasticloadbalancing/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/elasticloadbalancing
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-elastic-load-balancing-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-elastic-load-balancing-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions, ensuring high availability and fault tolerance for your applications.
examples:
- key_count: 5
  name: Amazon Elastic Load Balancing Action Example
  slug: amazon-elastic-load-balancing-action-example
- key_count: 1
  name: Amazon Elastic Load Balancing Create Listener Response Example
  slug: amazon-elastic-load-balancing-create-listener-response-example
- key_count: 1
  name: Amazon Elastic Load Balancing Create Load Balancer Response Example
  slug: amazon-elastic-load-balancing-create-load-balancer-response-example
- key_count: 1
  name: Amazon Elastic Load Balancing Create Rule Response Example
  slug: amazon-elastic-load-balancing-create-rule-response-example
- key_count: 1
  name: Amazon Elastic Load Balancing Create Target Group Response Example
  slug: amazon-elastic-load-balancing-create-target-group-response-example
- key_count: 2
  name: Amazon Elastic Load Balancing Describe Listeners Response Example
  slug: amazon-elastic-load-balancing-describe-listeners-response-example
- key_count: 2
  name: Amazon Elastic Load Balancing Describe Load Balancers Response Example
  slug: amazon-elastic-load-balancing-describe-load-balancers-response-example
- key_count: 2
  name: Amazon Elastic Load Balancing Describe Rules Response Example
  slug: amazon-elastic-load-balancing-describe-rules-response-example
- key_count: 2
  name: Amazon Elastic Load Balancing Describe Target Groups Response Example
  slug: amazon-elastic-load-balancing-describe-target-groups-response-example
- key_count: 1
  name: Amazon Elastic Load Balancing Describe Target Health Response Example
  slug: amazon-elastic-load-balancing-describe-target-health-response-example
- key_count: 10
  name: Amazon Elastic Load Balancing Example
  slug: amazon-elastic-load-balancing-example
- key_count: 7
  name: Amazon Elastic Load Balancing Listener Example
  slug: amazon-elastic-load-balancing-listener-example
- key_count: 10
  name: Amazon Elastic Load Balancing Load Balancer Example
  slug: amazon-elastic-load-balancing-load-balancer-example
- key_count: 5
  name: Amazon Elastic Load Balancing Rule Example
  slug: amazon-elastic-load-balancing-rule-example
- key_count: 2
  name: Amazon Elastic Load Balancing Tag Example
  slug: amazon-elastic-load-balancing-tag-example
- key_count: 10
  name: Amazon Elastic Load Balancing Target Group Example
  slug: amazon-elastic-load-balancing-target-group-example
features:
- description: HTTP/HTTPS load balancing with advanced request routing based on content
  name: Application Load Balancer
- description: Ultra-high performance TCP/UDP load balancing at OSI layer 4
  name: Network Load Balancer
- description: Distribute traffic to third-party virtual appliances for inspection
  name: Gateway Load Balancer
- description: Automatically route traffic away from unhealthy targets
  name: Health Checks
- description: Offload SSL/TLS decryption from application servers
  name: SSL/TLS Termination
finops:
- name: Amazon Elastic Load Balancing Finops
  service_category: API
  slug: amazon-elastic-load-balancing-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Action
  property_count: 5
  slug: amazon-elastic-load-balancing-action
- name: CreateListenerResponse
  property_count: 1
  slug: amazon-elastic-load-balancing-create-listener-response
- name: CreateLoadBalancerResponse
  property_count: 1
  slug: amazon-elastic-load-balancing-create-load-balancer-response
- name: CreateRuleResponse
  property_count: 1
  slug: amazon-elastic-load-balancing-create-rule-response
- name: CreateTargetGroupResponse
  property_count: 1
  slug: amazon-elastic-load-balancing-create-target-group-response
- name: DescribeListenersResponse
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-listeners-response
- name: DescribeLoadBalancersResponse
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-load-balancers-response
- name: DescribeRulesResponse
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-rules-response
- name: DescribeTargetGroupsResponse
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-target-groups-response
- name: DescribeTargetHealthResponse
  property_count: 1
  slug: amazon-elastic-load-balancing-describe-target-health-response
- name: Listener
  property_count: 7
  slug: amazon-elastic-load-balancing-listener
- name: LoadBalancer
  property_count: 12
  slug: amazon-elastic-load-balancing-load-balancer
- name: Rule
  property_count: 5
  slug: amazon-elastic-load-balancing-rule
- name: Amazon Elastic Load Balancer
  property_count: 16
  slug: amazon-elastic-load-balancing
- name: Tag
  property_count: 2
  slug: amazon-elastic-load-balancing-tag
- name: TargetGroup
  property_count: 15
  slug: amazon-elastic-load-balancing-target-group
json_structures:
- name: Amazon Elastic Load Balancing Action Structure
  property_count: 5
  slug: amazon-elastic-load-balancing-action-structure
- name: Amazon Elastic Load Balancing Create Listener Response Structure
  property_count: 1
  slug: amazon-elastic-load-balancing-create-listener-response-structure
- name: Amazon Elastic Load Balancing Create Load Balancer Response Structure
  property_count: 1
  slug: amazon-elastic-load-balancing-create-load-balancer-response-structure
- name: Amazon Elastic Load Balancing Create Rule Response Structure
  property_count: 1
  slug: amazon-elastic-load-balancing-create-rule-response-structure
- name: Amazon Elastic Load Balancing Create Target Group Response Structure
  property_count: 1
  slug: amazon-elastic-load-balancing-create-target-group-response-structure
- name: Amazon Elastic Load Balancing Describe Listeners Response Structure
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-listeners-response-structure
- name: Amazon Elastic Load Balancing Describe Load Balancers Response Structure
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-load-balancers-response-structure
- name: Amazon Elastic Load Balancing Describe Rules Response Structure
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-rules-response-structure
- name: Amazon Elastic Load Balancing Describe Target Groups Response Structure
  property_count: 2
  slug: amazon-elastic-load-balancing-describe-target-groups-response-structure
- name: Amazon Elastic Load Balancing Describe Target Health Response Structure
  property_count: 1
  slug: amazon-elastic-load-balancing-describe-target-health-response-structure
- name: Amazon Elastic Load Balancing Listener Structure
  property_count: 7
  slug: amazon-elastic-load-balancing-listener-structure
- name: Amazon Elastic Load Balancing Load Balancer Structure
  property_count: 12
  slug: amazon-elastic-load-balancing-load-balancer-structure
- name: Amazon Elastic Load Balancing Rule Structure
  property_count: 5
  slug: amazon-elastic-load-balancing-rule-structure
- name: Amazon Elastic Load Balancing Structure
  property_count: 16
  slug: amazon-elastic-load-balancing-structure
- name: Amazon Elastic Load Balancing Tag Structure
  property_count: 2
  slug: amazon-elastic-load-balancing-tag-structure
- name: Amazon Elastic Load Balancing Target Group Structure
  property_count: 15
  slug: amazon-elastic-load-balancing-target-group-structure
jsonld:
- class_count: 0
  name: Amazon Elastic Load Balancing Context
  property_count: 6
  slug: amazon-elastic-load-balancing-context
layout: provider
modified: '2026-05-19'
name: Amazon Elastic Load Balancing
nav: Providers
network: true
overview: 'Amazon Elastic Load Balancing publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Listeners API, Load Balancers API, Rules API, and 2 more. Tagged areas include Amazon Web Services, High Availability, Load Balancing, Networking, and Scalability.


  The Amazon Elastic Load Balancing catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Elastic Load Balancing''s developer surface includes authentication, developer portal, documentation, engineering blog, developer console, signup flow, support, and 31 more developer resources.'
plans:
- name: Amazon Elastic Load Balancing Plans Pricing
  plan_count: 3
  slug: amazon-elastic-load-balancing-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Amazon Elastic Load Balancing Rate Limits
  slug: amazon-elastic-load-balancing-rate-limits
rules:
- name: Amazon Elastic Load Balancing API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-elastic-load-balancing-jsonschema-spectral-rules
- name: Amazon Elastic Load Balancing API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 14
  slug: amazon-elastic-load-balancing-spectral-rules
score:
  band: exemplar
  composite: 71.0
  delta: -3.9
  facets:
    commercial_clarity: 89.5
    contract_quality: 77.2
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 74.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-load-balancing/refs/heads/main/screenshots/amazon-elastic-load-balancing-2026-06-20T171649.png
security:
- kind: authentication
  name: Amazon Elastic Load Balancing Authentication
  slug: amazon-elastic-load-balancing-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Elastic Load Balancing Domain Security
  slug: amazon-elastic-load-balancing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Elastic Load Balancing Vulnerability Disclosure
  slug: amazon-elastic-load-balancing-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Elastic Load Balancing Trust Center
  slug: amazon-elastic-load-balancing-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-elastic-load-balancing
tags:
- Amazon Web Services
- High Availability
- Load Balancing
- Networking
- Scalability
use_cases:
- description: Distribute HTTP/HTTPS traffic across multiple web servers
  name: Web Application Load Balancing
- description: Route requests to different microservices based on URL paths or headers
  name: Microservices Routing
- description: Load balance traffic to ECS containers and Kubernetes pods
  name: Container Load Balancing
- description: Distribute global traffic across multiple AWS regions
  name: Multi-Region Traffic Management
website: https://aws.amazon.com/elasticloadbalancing/
---
