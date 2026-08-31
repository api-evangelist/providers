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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Freertos Agentic Access
  operation_count: 11
  slug: amazon-freertos-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: Over-the-air firmware update management
  name: Amazon FreeRTOS OTA Updates API
  slug: amazon-freertos-ota-updates-api
- description: FreeRTOS software configuration management
  name: Amazon FreeRTOS Software Configurations API
  slug: amazon-freertos-software-configurations-api
- description: Resource metadata labels
  name: Amazon FreeRTOS Tags API
  slug: amazon-freertos-tags-api
arazzos:
- description: Confirm an OTA update exists, delete it with its stream and job, and verify removal.
  name: Amazon FreeRTOS Decommission OTA Update
  slug: amazon-freertos-decommission-ota-update-workflow
- description: Confirm a FreeRTOS software configuration exists, delete it, and verify removal.
  name: Amazon FreeRTOS Decommission Software Configuration
  slug: amazon-freertos-decommission-software-configuration-workflow
- description: Survey existing hardware platforms, create a new FreeRTOS software configuration, and confirm it.
  name: Amazon FreeRTOS Provision Software Configuration
  slug: amazon-freertos-provision-software-configuration-workflow
- description: Create an OTA firmware update, read it back, and branch on its creation status.
  name: Amazon FreeRTOS Roll Out OTA Update
  slug: amazon-freertos-rollout-ota-update-workflow
- description: Resolve a software configuration ARN, apply resource tags, and read them back.
  name: Amazon FreeRTOS Tag Software Configuration
  slug: amazon-freertos-tag-software-configuration-workflow
- description: Read a FreeRTOS software configuration, update its metadata, and confirm the change.
  name: Amazon FreeRTOS Update Software Configuration
  slug: amazon-freertos-update-software-configuration-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: Amazon FreeRTOS Management API
  slug: postman-amazon-freertos
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon FreeRTOS Management OTA Updates API
  slug: open-amazon-freertos-ota-updates-api
- collection_type: open
  name: Amazon FreeRTOS Management OTA Updates Software Configurations API
  slug: open-amazon-freertos-software-configurations-api
- collection_type: open
  name: Amazon FreeRTOS Management OTA Updates Tags API
  slug: open-amazon-freertos-tags-api
- collection_type: open
  name: Amazon FreeRTOS Management API
  slug: open-amazon-freertos
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aws/amazon-freertos/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aws/amazon-freertos/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/aws/amazon-freertos/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aws/amazon-freertos/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aws/amazon-freertos/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/aws/amazon-freertos/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-freertos-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-freertos-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-freertos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-freertos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-freertos-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-freertos/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-decommission-ota-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-decommission-software-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-provision-software-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-rollout-ota-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-tag-software-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-freertos-update-software-configuration-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/freertos/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/freertos/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/freertos/
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
  url: https://aws.amazon.com/blogs/iot/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/aws/amazon-freertos
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/iot/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
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
  url: https://stackoverflow.com/questions/tagged/amazon-freertos
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-freertos-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-freertos-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-freertos-context.jsonld
created: '2026-03-16'
description: Amazon FreeRTOS is an open source, real-time operating system for microcontrollers that makes it easy to program, deploy, secure, connect, and manage small, low-power edge devices. It extends the FreeRTOS kernel with libraries for secure connectivity, over-the-air updates, and more.
examples:
- key_count: 5
  name: Amazon Freertos Device Example
  slug: amazon-freertos-device-example
- key_count: 5
  name: Amazon Freertos Ota File Example
  slug: amazon-freertos-ota-file-example
- key_count: 10
  name: Amazon Freertos Ota Update Example
  slug: amazon-freertos-ota-update-example
- key_count: 9
  name: Amazon Freertos Software Configuration Example
  slug: amazon-freertos-software-configuration-example
- key_count: 2
  name: Amazon Freertos Tag Example
  slug: amazon-freertos-tag-example
features:
- description: Open-source real-time operating system kernel with preemptive multitasking for microcontrollers.
  name: FreeRTOS Kernel
- description: Over-the-air firmware update delivery with code signing verification and rollback support.
  name: OTA Update Management
- description: TLS 1.2/1.3 encrypted MQTT and HTTP connectivity using AWS IoT Core.
  name: Secure Connectivity
- description: Zero-touch device provisioning using AWS IoT Fleet Provisioning and Just-In-Time Registration.
  name: Device Provisioning
- description: Cryptographic library for secure key storage and operations on embedded devices.
  name: corePKCS11
- description: IPv4/IPv6 TCP/IP networking stack optimized for embedded systems.
  name: FreeRTOS+TCP
- description: Over 100 partner-qualified hardware platforms from major MCU vendors including Espressif, ST, NXP, Renesas.
  name: Qualified Hardware
finops:
- name: Amazon Freertos Finops
  service_category: API
  slug: amazon-freertos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-freertos.png
json_schemas:
- name: Device
  property_count: 5
  slug: amazon-freertos-device
- name: OtaFile
  property_count: 5
  slug: amazon-freertos-ota-file
- name: OtaUpdate
  property_count: 10
  slug: amazon-freertos-ota-update
- name: SoftwareConfiguration
  property_count: 9
  slug: amazon-freertos-software-configuration
- name: Tag
  property_count: 2
  slug: amazon-freertos-tag
json_structures:
- name: Amazon Freertos Device Structure
  property_count: 0
  slug: amazon-freertos-device-structure
- name: Amazon Freertos Ota File Structure
  property_count: 0
  slug: amazon-freertos-ota-file-structure
- name: Amazon Freertos Ota Update Structure
  property_count: 0
  slug: amazon-freertos-ota-update-structure
- name: Amazon Freertos Software Configuration Structure
  property_count: 0
  slug: amazon-freertos-software-configuration-structure
- name: Amazon Freertos Tag Structure
  property_count: 0
  slug: amazon-freertos-tag-structure
jsonld:
- class_count: 5
  name: Amazon Freertos Context
  property_count: 11
  slug: amazon-freertos-context
layout: provider
modified: '2026-05-19'
name: Amazon FreeRTOS
nav: Providers
network: true
overview: 'Amazon FreeRTOS publishes 3 APIs on the [APIs.io](https://apis.io/) network: OTA Updates API, Software Configurations API, and Tags API. Tagged areas include Embedded Systems, IoT, Microcontrollers, and RTOS.


  The Amazon FreeRTOS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon FreeRTOS''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 28 more developer resources.'
plans:
- name: Amazon Freertos Plans Pricing
  plan_count: 3
  slug: amazon-freertos-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Amazon Freertos Rate Limits
  slug: amazon-freertos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon FreeRTOS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-freertos-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: Amazon FreeRTOS API Rules
  rule_count: 35
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 25
  slug: amazon-freertos-spectral-rules
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 80.8
    developer_ergonomics: 69.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 100.0
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/screenshots/amazon-freertos-2026-06-20T171652.png
security:
- kind: authentication
  name: Amazon Freertos Authentication
  slug: amazon-freertos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Freertos Domain Security
  slug: amazon-freertos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Freertos Vulnerability Disclosure
  slug: amazon-freertos-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Freertos Trust Center
  slug: amazon-freertos-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-freertos
tags:
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
use_cases:
- description: Deploy FreeRTOS on industrial sensors for secure cloud connectivity and remote firmware updates.
  name: Industrial IoT Sensors
- description: Build connected home devices with low-power FreeRTOS firmware and AWS IoT integration.
  name: Smart Home Devices
- description: Develop GPS and location tracking devices with FreeRTOS for fleet and supply chain monitoring.
  name: Asset Tracking
- description: Collect vibration, temperature, and current data from FreeRTOS devices for ML-based maintenance prediction.
  name: Predictive Maintenance
- description: Build FDA-validated medical devices with FreeRTOS for remote patient monitoring and diagnostics.
  name: Medical IoT
- description: Deploy smart meters and grid sensors running FreeRTOS for utility data collection and OTA updates.
  name: Energy Management
website: https://aws.amazon.com/freertos/
---
