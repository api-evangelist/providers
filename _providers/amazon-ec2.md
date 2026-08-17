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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amazon Ec2 Agentic Access
  operation_count: 26
  slug: amazon-ec2-agentic-access
  summary_line: 26 operations
api_count: 8
apis:
- description: Operations for creating and managing Amazon Machine Images
  name: Amazon EC2 AMIs API
  slug: amazon-ec2-amis-api
- description: Operations for allocating and managing static IP addresses
  name: Amazon EC2 Elastic IPs API
  slug: amazon-ec2-elastic-ips-api
- description: Operations for launching, managing, and terminating EC2 instances
  name: Amazon EC2 Instances API
  slug: amazon-ec2-instances-api
- description: Operations for managing SSH key pairs used for instance access
  name: Amazon EC2 Key Pairs API
  slug: amazon-ec2-key-pairs-api
- description: Operations for managing reusable instance launch configurations
  name: Amazon EC2 Launch Templates API
  slug: amazon-ec2-launch-templates-api
- description: Operations for describing AWS regions and availability zones
  name: Amazon EC2 Regions API
  slug: amazon-ec2-regions-api
- description: Operations for managing security group rules and firewall settings
  name: Amazon EC2 Security Groups API
  slug: amazon-ec2-security-groups-api
- description: Operations for requesting and managing Spot Instances
  name: Amazon EC2 Spot Instances API
  slug: amazon-ec2-spot-instances-api
arazzos:
- description: Allocate a VPC Elastic IP, confirm the instance is running, then associate the address.
  name: Amazon EC2 Allocate and Associate Elastic IP
  slug: amazon-ec2-allocate-and-associate-eip-workflow
- description: Describe a security group, then describe instances filtered by that group.
  name: Amazon EC2 Audit Security Group Usage
  slug: amazon-ec2-audit-security-group-usage-workflow
- description: Launch an instance, poll until running, allocate an Elastic IP, then associate it.
  name: Amazon EC2 Bind Elastic IP to a New Instance
  slug: amazon-ec2-bind-eip-to-new-instance-workflow
- description: Create an AMI from a source instance, confirm it, then launch a clone from that AMI.
  name: Amazon EC2 Clone an Instance via Image
  slug: amazon-ec2-clone-instance-via-image-workflow
- description: Terminate an instance, wait until terminated, then delete its security group.
  name: Amazon EC2 Deprovision a Secured Instance
  slug: amazon-ec2-deprovision-secured-instance-workflow
- description: Confirm an AMI exists, deregister it, then verify it is gone.
  name: Amazon EC2 Deregister an AMI After Confirmation
  slug: amazon-ec2-deregister-image-and-cleanup-workflow
- description: Look up a security group by name and add a scoped inbound rule to it.
  name: Amazon EC2 Harden an Existing Security Group
  slug: amazon-ec2-harden-existing-security-group-workflow
- description: Launch an instance, then poll DescribeInstances until it reaches the running state.
  name: Amazon EC2 Launch and Await Running
  slug: amazon-ec2-launch-and-await-running-workflow
- description: Create a security group, open SSH ingress, create a key pair, and launch an instance.
  name: Amazon EC2 Launch a Secured Instance
  slug: amazon-ec2-launch-secured-instance-workflow
- description: Describe instances, page through with NextToken, then image the first instance found.
  name: Amazon EC2 Inventory Instances Then Image First
  slug: amazon-ec2-paginate-instances-then-tag-image-workflow
- description: Describe regions and availability zones, then launch an instance in a chosen zone.
  name: Amazon EC2 Place an Instance in an Availability Zone
  slug: amazon-ec2-place-instance-in-zone-workflow
- description: Create a key pair, confirm it via describe, then launch an instance using it.
  name: Amazon EC2 Prepare Key and Launch
  slug: amazon-ec2-prepare-key-and-launch-workflow
- description: Create a launch template, confirm it, then launch an instance referencing the template parameters.
  name: Amazon EC2 Create a Launch Template and Boot From It
  slug: amazon-ec2-rebuild-image-from-launch-template-workflow
- description: Terminate an instance, wait until terminated, then release its Elastic IP.
  name: Amazon EC2 Release Elastic IP on Terminate
  slug: amazon-ec2-release-eip-on-terminate-workflow
- description: Request Spot Instances, then poll the Spot request until it is fulfilled.
  name: Amazon EC2 Request Spot Instances and Track
  slug: amazon-ec2-request-spot-and-track-workflow
- description: Reboot an instance and poll its status until checks report passed.
  name: Amazon EC2 Restart and Verify Instance
  slug: amazon-ec2-restart-and-verify-instance-workflow
- description: Verify a key pair exists, create its replacement, then delete the old key pair.
  name: Amazon EC2 Rotate Key Pair
  slug: amazon-ec2-rotate-key-pair-workflow
- description: Stop an instance, wait until stopped, then create an AMI from it.
  name: Amazon EC2 Stop and Create Image
  slug: amazon-ec2-stop-and-create-image-workflow
- description: Stop an instance, wait until stopped, then start it again and confirm running.
  name: Amazon EC2 Stop and Start Instance Cycle
  slug: amazon-ec2-stop-start-instance-cycle-workflow
artifact_total: 80
collections:
- collection_type: postman
  name: Amazon EC2 API
  slug: postman-amazon-ec2
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EC2 AMIs API
  slug: open-amazon-ec2-amis-api
- collection_type: open
  name: Amazon EC2 AMIs Elastic IPs API
  slug: open-amazon-ec2-elastic-ips-api
- collection_type: open
  name: Amazon EC2 AMIs Instances API
  slug: open-amazon-ec2-instances-api
- collection_type: open
  name: Amazon EC2 AMIs Key Pairs API
  slug: open-amazon-ec2-key-pairs-api
- collection_type: open
  name: Amazon EC2 AMIs Launch Templates API
  slug: open-amazon-ec2-launch-templates-api
- collection_type: open
  name: Amazon EC2 AMIs Regions API
  slug: open-amazon-ec2-regions-api
- collection_type: open
  name: Amazon EC2 AMIs Security Groups API
  slug: open-amazon-ec2-security-groups-api
- collection_type: open
  name: Amazon EC2 AMIs Spot Instances API
  slug: open-amazon-ec2-spot-instances-api
- collection_type: open
  name: Amazon EC2 API
  slug: open-amazon-ec2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ec2-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-ec2-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ec2-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-ec2-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-ec2-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-ec2/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-allocate-and-associate-eip-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-audit-security-group-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-bind-eip-to-new-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-clone-instance-via-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-deprovision-secured-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-deregister-image-and-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-harden-existing-security-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-launch-and-await-running-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-launch-secured-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-paginate-instances-then-tag-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-place-instance-in-zone-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-prepare-key-and-launch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-rebuild-image-from-launch-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-release-eip-on-terminate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-request-spot-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-restart-and-verify-instance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-rotate-key-pair-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-stop-and-create-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-ec2-stop-start-instance-cycle-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/ec2/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ec2/
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
  url: https://console.aws.amazon.com/ec2/
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
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-ec2
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-ec2-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ec2-vocabulary.yaml
created: '2024-01-15'
description: Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud, allowing you to launch virtual server instances, manage networking, and configure storage with complete control over your computing resources.
examples:
- key_count: 4
  name: Amazon Ec2 Instance Example
  slug: amazon-ec2-instance-example
- key_count: 1
  name: Ec2 Openapi Create Image Response Example
  slug: ec2-openapi-create-image-response-example
- key_count: 2
  name: Ec2 Openapi Describe Instances Response Example
  slug: ec2-openapi-describe-instances-response-example
- key_count: 3
  name: Ec2 Openapi Instance Example
  slug: ec2-openapi-instance-example
- key_count: 3
  name: Ec2 Openapi Run Instances Response Example
  slug: ec2-openapi-run-instances-response-example
- key_count: 2
  name: Ec2 Openapi Tag Example
  slug: ec2-openapi-tag-example
features:
- description: Over 750 instance types optimized for compute, memory, storage, GPU, and inferencing workloads.
  name: Diverse Instance Types
- description: Pre-configured OS images for Windows, Linux, and macOS with custom and marketplace options.
  name: Amazon Machine Images
- description: Static IPv4 addresses that can be quickly remapped to different instances for fault tolerance.
  name: Elastic IPs
- description: Virtual firewalls to control inbound and outbound traffic to EC2 instances.
  name: Security Groups
- description: Access spare EC2 capacity at up to 90% discount over On-Demand prices for flexible workloads.
  name: Spot Instances
- description: Control instance placement for low-latency cluster networking or high-availability distribution.
  name: Placement Groups
- description: Version-controlled configurations for launching EC2 instances with consistent settings.
  name: Launch Templates
- description: Next-generation virtualization infrastructure delivering near bare-metal performance and security.
  name: Nitro System
finops:
- name: Amazon Ec2 Finops
  service_category: API
  slug: amazon-ec2-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon EC2 Instance
  property_count: 21
  slug: amazon-ec2-instance
- name: CreateImageResponse
  property_count: 1
  slug: ec2-openapi-create-image-response
- name: DescribeInstancesResponse
  property_count: 2
  slug: ec2-openapi-describe-instances-response
- name: Instance
  property_count: 16
  slug: ec2-openapi-instance
- name: RunInstancesResponse
  property_count: 3
  slug: ec2-openapi-run-instances-response
- name: Tag
  property_count: 2
  slug: ec2-openapi-tag
json_structures:
- name: Amazon Ec2 Instance Structure
  property_count: 21
  slug: amazon-ec2-instance-structure
- name: Ec2 Openapi Create Image Response Structure
  property_count: 1
  slug: ec2-openapi-create-image-response-structure
- name: Ec2 Openapi Describe Instances Response Structure
  property_count: 2
  slug: ec2-openapi-describe-instances-response-structure
- name: Ec2 Openapi Instance Structure
  property_count: 16
  slug: ec2-openapi-instance-structure
- name: Ec2 Openapi Run Instances Response Structure
  property_count: 3
  slug: ec2-openapi-run-instances-response-structure
- name: Ec2 Openapi Tag Structure
  property_count: 2
  slug: ec2-openapi-tag-structure
jsonld:
- class_count: 6
  name: Amazon Ec2 Context
  property_count: 35
  slug: amazon-ec2-context
layout: provider
modified: '2026-05-19'
name: Amazon EC2
nav: Providers
network: true
overview: 'Amazon EC2 publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AMIs API, Elastic IPs API, Instances API, and 5 more. Tagged areas include Cloud Computing, Compute, IaaS, Infrastructure, and Virtual Machines.


  The Amazon EC2 catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon EC2''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 38 more developer resources.'
plans:
- name: Amazon Ec2 Plans Pricing
  plan_count: 3
  slug: amazon-ec2-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Amazon Ec2 Rate Limits
  slug: amazon-ec2-rate-limits
rules:
- name: Amazon EC2 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-ec2-jsonschema-spectral-rules
- name: Amazon EC2 API Rules
  rule_count: 34
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 18
  slug: amazon-ec2-spectral-rules
score:
  band: strong
  composite: 63.4
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 78.4
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 63.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ec2/refs/heads/main/screenshots/amazon-ec2-2026-06-20T171637.png
security:
- kind: authentication
  name: Amazon Ec2 Authentication
  slug: amazon-ec2-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Ec2 Domain Security
  slug: amazon-ec2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ec2 Vulnerability Disclosure
  slug: amazon-ec2-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Ec2 Trust Center
  slug: amazon-ec2-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-ec2
tags:
- Cloud Computing
- Compute
- IaaS
- Infrastructure
- Virtual Machines
use_cases:
- description: Deploy scalable web applications and APIs with full control over the compute environment.
  name: Web Application Hosting
- description: GPU-accelerated instances for deep learning model training and inference workloads.
  name: Machine Learning Training
- description: Cluster networking instances for computational fluid dynamics, genomics, and financial modeling.
  name: High-Performance Computing
- description: Certified instances for SAP HANA, SAP S/4HANA, and other enterprise database applications.
  name: SAP and Enterprise Workloads
- description: Flexible on-demand compute for CI/CD pipelines, dev environments, and test automation.
  name: Development and Testing
website: https://aws.amazon.com/ec2/
---
