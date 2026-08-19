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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Amazon Cloud Wan Agentic Access
  operation_count: 4
  slug: amazon-cloud-wan-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- description: API for building and managing global wide area networks, connecting branch offices, data centers, and VPCs with centralized control, monitoring, and network policy automation.
  name: Amazon Cloud WAN API
  slug: amazon-cloud-wan-api
- description: Operations for managing Cloud WAN core networks
  name: Amazon Cloud WAN Core Networks API
  slug: amazon-cloud-wan-core-networks-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Cloud WAN Core Networks API
  slug: open-amazon-cloud-wan-core-networks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-cloud-wan-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-cloud-wan-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-cloud-wan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-cloud-wan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-cloud-wan-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/cloud-wan/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/
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
  url: https://console.aws.amazon.com/networkmanager/
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
  url: https://stackoverflow.com/questions/tagged/aws-cloud-wan
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-cloud-wan-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-cloud-wan-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-cloud-wan-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-cloud-wan-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-cloud-wan-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-cloud-wan-llms.txt
created: '2026-03-16'
description: Amazon Cloud WAN is a managed wide area networking service that simplifies building, managing, and monitoring global WANs by connecting branch offices, data centers, and Amazon VPCs through a central dashboard with network policy automation and unified monitoring.
examples:
- key_count: 6
  name: Cloud Wan Core Network Example
  slug: cloud-wan-core-network-example
- key_count: 3
  name: Cloud Wan Create Core Network Request Example
  slug: cloud-wan-create-core-network-request-example
- key_count: 1
  name: Cloud Wan Create Core Network Response Example
  slug: cloud-wan-create-core-network-response-example
- key_count: 1
  name: Cloud Wan Delete Core Network Response Example
  slug: cloud-wan-delete-core-network-response-example
- key_count: 1
  name: Cloud Wan Get Core Network Response Example
  slug: cloud-wan-get-core-network-response-example
- key_count: 2
  name: Cloud Wan List Core Networks Response Example
  slug: cloud-wan-list-core-networks-response-example
features:
- description: Build and manage global wide area networks through a single centralized dashboard.
  name: Centralized WAN Management
- description: Automate management and security tasks across your entire WAN infrastructure.
  name: Network Policy Automation
- description: Monitor on-premises and AWS network health and performance from one view.
  name: Unified Monitoring
- description: Isolate sensitive traffic from standard data flows with segmentation policies.
  name: Network Segmentation
- description: Connect branch offices, data centers, and VPCs with minimal configuration globally.
  name: Global Connectivity
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-cloud-wan.png
integrations:
- description: Connect VPCs and on-premises networks through Transit Gateway attachments.
  name: AWS Transit Gateway
- description: Dedicated network connections from on-premises to AWS.
  name: AWS Direct Connect
- description: Connect VPCs across regions into the global WAN.
  name: Amazon VPC
- description: Control access to Cloud WAN resources with IAM policies.
  name: AWS IAM
json_schemas:
- name: CoreNetwork
  property_count: 6
  slug: cloud-wan-core-network
- name: CreateCoreNetworkRequest
  property_count: 3
  slug: cloud-wan-create-core-network-request
- name: CreateCoreNetworkResponse
  property_count: 1
  slug: cloud-wan-create-core-network-response
- name: DeleteCoreNetworkResponse
  property_count: 1
  slug: cloud-wan-delete-core-network-response
- name: GetCoreNetworkResponse
  property_count: 1
  slug: cloud-wan-get-core-network-response
- name: ListCoreNetworksResponse
  property_count: 2
  slug: cloud-wan-list-core-networks-response
json_structures:
- name: Cloud Wan Core Network Structure
  property_count: 6
  slug: cloud-wan-core-network-structure
- name: Cloud Wan Create Core Network Request Structure
  property_count: 3
  slug: cloud-wan-create-core-network-request-structure
- name: Cloud Wan Create Core Network Response Structure
  property_count: 1
  slug: cloud-wan-create-core-network-response-structure
- name: Cloud Wan Delete Core Network Response Structure
  property_count: 1
  slug: cloud-wan-delete-core-network-response-structure
- name: Cloud Wan Get Core Network Response Structure
  property_count: 1
  slug: cloud-wan-get-core-network-response-structure
- name: Cloud Wan List Core Networks Response Structure
  property_count: 2
  slug: cloud-wan-list-core-networks-response-structure
jsonld:
- class_count: 7
  name: Amazon Cloud Wan Context
  property_count: 9
  slug: amazon-cloud-wan-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-cloud-wan-mcp.yml
  slug: amazon-cloud-wan-mcpyml
modified: '2026-06-20'
name: Amazon Cloud WAN
nav: Providers
network: true
overview: 'Amazon Cloud WAN publishes 1 API on the [APIs.io](https://apis.io/) network: Core Networks API. Tagged areas include Cloud WAN, Networking, Wide Area Network, and SD-WAN.


  The Amazon Cloud WAN catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Cloud WAN''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 19 more developer resources.'
random_paper: 107
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Cloud WAN API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-cloud-wan-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Cloud WAN API Rules
  rule_count: 23
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 10
  slug: amazon-cloud-wan-spectral-rules
score:
  band: developing
  composite: 39.6
  delta: -4.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 41.7
    contract_quality: 21.5
    developer_ergonomics: 45.2
    discoverability: 77.8
    governance: 41.7
    operational_transparency: 18.4
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-cloud-wan/refs/heads/main/screenshots/amazon-cloud-wan-2026-07-25T195941.png
security:
- kind: authentication
  name: Amazon Cloud Wan Authentication
  slug: amazon-cloud-wan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Cloud Wan Domain Security
  slug: amazon-cloud-wan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Cloud Wan Vulnerability Disclosure
  slug: amazon-cloud-wan-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Cloud Wan Trust Center
  slug: amazon-cloud-wan-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-cloud-wan
tags:
- Cloud WAN
- Networking
- Wide Area Network
- SD-WAN
use_cases:
- description: Build globally distributed corporate WANs using AWS infrastructure.
  name: Global Enterprise WAN
- description: Extend on-premises corporate WANs into AWS cloud environments seamlessly.
  name: Hybrid Network Extension
- description: Centralize network configuration, monitoring, and automation across all locations.
  name: Network Centralization
website: https://aws.amazon.com/cloud-wan/
---
