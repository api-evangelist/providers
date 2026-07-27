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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Transit Gateway Agentic Access
  operation_count: 5
  slug: amazon-transit-gateway-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Route Tables API from Amazon Transit Gateway — 1 operation(s) for route tables.
  name: Amazon Transit Gateway Route Tables API
  slug: amazon-transit-gateway-route-tables-api
- description: The Transit Gateways API from Amazon Transit Gateway — 3 operation(s) for transit gateways.
  name: Amazon Transit Gateway Transit Gateways API
  slug: amazon-transit-gateway-transit-gateways-api
- description: The VPC Attachments API from Amazon Transit Gateway — 1 operation(s) for vpc attachments.
  name: Amazon Transit Gateway VPC Attachments API
  slug: amazon-transit-gateway-vpc-attachments-api
artifact_total: 25
collections:
- collection_type: open
  name: Amazon Transit Gateway API
  slug: open-amazon-transit-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-transit-gateway-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-transit-gateway-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-transit-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-transit-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-transit-gateway-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/transit-gateway/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/vpc/latest/tgw/
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
  url: https://aws.amazon.com/blogs/networking-and-content-delivery/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/vpc/
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
  url: https://stackoverflow.com/questions/tagged/aws-transit-gateway
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/rules/amazon-transit-gateway-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/vocabulary/amazon-transit-gateway-vocabulary.yaml
created: '2024-01-15'
description: Amazon Transit Gateway connects VPCs and on-premises networks through a central hub, simplifying network architecture and reducing operational complexity for large-scale cloud deployments.
examples:
- key_count: 2
  name: Amazon Transit Gateway Example
  slug: amazon-transit-gateway-example
features:
- description: Automate operational tasks with Amazon Transit Gateway.
  name: Automation
- description: Programmatic access to Amazon Transit Gateway resources.
  name: API Access
finops:
- name: Amazon Transit Gateway Finops
  service_category: API
  slug: amazon-transit-gateway-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Transit Gateway
  property_count: 8
  slug: amazon-transit-gateway
- name: Tag
  property_count: 2
  slug: amazon-transit-gateway-tag
- name: TransitGateway
  property_count: 6
  slug: amazon-transit-gateway-transit-gateway
json_structures:
- name: Amazon Transit Gateway Structure
  property_count: 0
  slug: amazon-transit-gateway-structure
- name: Amazon Transit Gateway Tag Structure
  property_count: 0
  slug: amazon-transit-gateway-tag-structure
- name: Amazon Transit Gateway Transit Gateway Structure
  property_count: 0
  slug: amazon-transit-gateway-transit-gateway-structure
jsonld:
- class_count: 7
  name: Amazon Transit Gateway Context
  property_count: 5
  slug: amazon-transit-gateway-context
layout: provider
modified: '2026-05-19'
name: Amazon Transit Gateway
nav: Providers
network: true
overview: 'Amazon Transit Gateway publishes 3 APIs on the [APIs.io](https://apis.io/) network: Route Tables API, Transit Gateways API, and VPC Attachments API. Tagged areas include Cloud Networking, Network Hub, Networking, Transit Gateway, and VPC.


  The Amazon Transit Gateway catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Transit Gateway''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 16 more developer resources.'
plans:
- name: Amazon Transit Gateway Plans Pricing
  plan_count: 3
  slug: amazon-transit-gateway-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Amazon Transit Gateway Rate Limits
  slug: amazon-transit-gateway-rate-limits
rules:
- name: Amazon Transit Gateway API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-transit-gateway-jsonschema-spectral-rules
- name: Amazon Transit Gateway API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 10
  slug: amazon-transit-gateway-spectral-rules
score:
  band: strong
  composite: 68.7
  delta: 4.5
  facets:
    commercial_clarity: 81.6
    contract_quality: 72.6
    developer_ergonomics: 41.3
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 64.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-transit-gateway/refs/heads/main/screenshots/amazon-transit-gateway-2026-06-20T171838.png
security:
- kind: authentication
  name: Amazon Transit Gateway Authentication
  slug: amazon-transit-gateway-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Transit Gateway Domain Security
  slug: amazon-transit-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Transit Gateway Vulnerability Disclosure
  slug: amazon-transit-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Transit Gateway Trust Center
  slug: amazon-transit-gateway-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-transit-gateway
tags:
- Cloud Networking
- Network Hub
- Networking
- Transit Gateway
- VPC
use_cases:
- description: Use Amazon Transit Gateway to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/transit-gateway/
---
