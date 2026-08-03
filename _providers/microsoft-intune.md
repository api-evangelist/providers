---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Microsoft Intune Agentic Access
  operation_count: 22
  slug: microsoft-intune-agentic-access
  summary_line: 22 operations · 16 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: The Microsoft Graph API for Intune enables programmatic access to Intune information and actions for your tenant. The API performs the same Intune operations as those available through the Azure Porta
  name: Microsoft Intune API
  slug: microsoft-intune-api
- description: The Intune Data Warehouse API provides access to your Intune data in a machine-readable format for use in your favorite analytics tool. You can use the API to generate reports that provide insight int
  name: Intune Data Warehouse API
  slug: intune-data-warehouse-api
- description: The Microsoft Graph Device Management API enables programmatic management of devices enrolled in Intune, including listing managed devices, performing remote actions such as wipe and retire, and retri
  name: Intune Device Management API
  slug: intune-device-management-api
- description: The Microsoft Graph Device Configuration API allows you to define and deploy device configuration policies across enrolled devices, including operating system platform and versioning, domain membershi
  name: Intune Device Configuration API
  slug: intune-device-configuration-api
- description: The Microsoft Graph Device Compliance API enables you to define and enforce device compliance policies, such as password complexity, encryption, and threat protection levels, and retrieve compliance s
  name: Intune Device Compliance API
  slug: intune-device-compliance-api
- description: The Microsoft Graph Device Enrollment API enables you to enroll organization-owned or corporate-owned devices for management with Intune, supporting various enrollment methods depending on device type
  name: Intune Device Enrollment API
  slug: intune-device-enrollment-api
- description: The Microsoft Graph Mobile App Management (MAM) API enables you to manage app protection policies, deploy apps to devices, configure app settings, and manage app usage policies to protect organization
  name: Intune Mobile App Management API
  slug: intune-mobile-app-management-api
- description: The Intune Reports Export API enables you to export Intune reporting data using Microsoft Graph API export jobs. You can create export jobs to generate reports that provide insight into device complia
  name: Intune Reports Export API
  slug: intune-reports-export-api
- description: Operations for managing device compliance policies. Compliance policies define rules and settings that a device must comply with to be considered compliant.
  name: Microsoft Intune Device Compliance Policies API
  slug: microsoft-intune-device-compliance-policies-api
- description: Operations for managing device configuration profiles. Configuration profiles define settings that are applied to enrolled devices.
  name: Microsoft Intune Device Configurations API
  slug: microsoft-intune-device-configurations-api
- description: Operations for managing devices enrolled in Intune. Includes listing, retrieving, creating, updating, and deleting managed device records.
  name: Microsoft Intune Managed Devices API
  slug: microsoft-intune-managed-devices-api
- description: Remote actions that can be performed on managed devices, including retire, wipe, sync, remote lock, reset passcode, and reboot.
  name: Microsoft Intune Remote Actions API
  slug: microsoft-intune-remote-actions-api
artifact_total: 37
collections:
- collection_type: open
  name: Microsoft Intune Graph API
  slug: open-microsoft-intune
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-intune-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-intune-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-intune-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-intune-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-intune-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/microsoft-intune-product
- group: start
  title: ''
  type: X-portal
  url: https://endpoint.microsoft.com/
- group: company
  title: ''
  type: X-blog
  url: https://techcommunity.microsoft.com/t5/microsoft-intune-blog/bg-p/MicrosoftEndpointManagerBlog
- group: learn
  title: ''
  type: X-learning
  url: https://docs.microsoft.com/en-us/learn/browse/?products=m365%2Cmem
- group: commercial
  title: ''
  type: X-privacy
  url: https://privacy.microsoft.com/
- group: commercial
  title: ''
  type: X-terms-of-service
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: operate
  title: ''
  type: X-status
  url: https://status.azure.com/
- group: build
  title: ''
  type: X-github
  url: https://github.com/microsoftgraph
- group: build
  title: ''
  type: X-github-samples
  url: https://github.com/microsoft/mggraph-intune-samples
- group: build
  title: ''
  type: X-powershell-samples
  url: https://github.com/microsoftgraph/powershell-intune-samples
- group: docs
  title: ''
  type: X-developer-documentation
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/intune-graph-apis
- group: build
  title: ''
  type: X-sdk
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk
- group: start
  title: ''
  type: X-sdk-getting-started
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/app-sdk-get-started
- group: build
  title: ''
  type: X-app-wrapping-tool
  url: https://learn.microsoft.com/en-us/intune/intune-service/developer/apps-prepare-mobile-application-management
- group: operate
  title: ''
  type: X-community
  url: https://techcommunity.microsoft.com/t5/microsoft-intune/ct-p/MicrosoftIntune
- group: operate
  title: ''
  type: X-support
  url: https://learn.microsoft.com/en-us/mem/get-support
- group: company
  title: ''
  type: X-twitter
  url: https://twitter.com/MSIntune
- group: other
  title: ''
  type: X-whatsnew
  url: https://learn.microsoft.com/en-us/intune/intune-service/fundamentals/in-development
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/security/blog/product/microsoft-intune/feed/
created: '2024'
description: Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM). It helps organizations control how their devices are used, including mobile phones, tablets, and laptops, and enables management of apps on those devices.
finops:
- name: Microsoft Intune Finops
  service_category: Endpoint Management
  slug: microsoft-intune-finops
image: https://docs.microsoft.com/en-us/mem/intune/fundamentals/media/what-is-intune/intune-logo.png
json_schemas:
- name: configurationManagerClientEnabledFeatures
  property_count: 7
  slug: microsoft-intune-configurationmanagerclientenabledfeatures
- name: deviceActionResult
  property_count: 5
  slug: microsoft-intune-deviceactionresult
- name: deviceAndAppManagementAssignmentTarget
  property_count: 1
  slug: microsoft-intune-deviceandappmanagementassignmenttarget
- name: deviceComplianceActionItem
  property_count: 6
  slug: microsoft-intune-devicecomplianceactionitem
- name: deviceCompliancePolicy
  property_count: 7
  slug: microsoft-intune-devicecompliancepolicy
- name: deviceCompliancePolicyAssignment
  property_count: 3
  slug: microsoft-intune-devicecompliancepolicyassignment
- name: deviceComplianceScheduledActionForRule
  property_count: 4
  slug: microsoft-intune-devicecompliancescheduledactionforrule
- name: deviceConfiguration
  property_count: 7
  slug: microsoft-intune-deviceconfiguration
- name: deviceConfigurationAssignment
  property_count: 3
  slug: microsoft-intune-deviceconfigurationassignment
- name: deviceHealthAttestationState
  property_count: 18
  slug: microsoft-intune-devicehealthattestationstate
- name: Microsoft Intune Managed Device
  property_count: 56
  slug: microsoft-intune-managed-device
- name: managedDevice
  property_count: 55
  slug: microsoft-intune-manageddevice
- name: odataError
  property_count: 1
  slug: microsoft-intune-odataerror
json_structures:
- name: Microsoft Intune Structure
  property_count: 0
  slug: microsoft-intune-structure
jsonld:
- class_count: 0
  name: Microsoft Intune Context
  property_count: 5
  slug: microsoft-intune-context
layout: provider
modified: '2026-05-19'
name: Microsoft Intune
nav: Providers
network: true
overview: 'Microsoft Intune publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Device Compliance Policies API, Device Configurations API, Managed Devices API, and 1 more. Tagged areas include App Protection, Azure, Compliance, Device Configuration, and Endpoint Management.


  The Microsoft Intune catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Intune''s developer surface includes authentication, engineering blog, and 22 more developer resources.'
plans:
- name: Microsoft Intune Plans Pricing
  plan_count: 9
  slug: microsoft-intune-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Microsoft Intune Rate Limits
  slug: microsoft-intune-rate-limits
rules:
- name: Microsoft Intune API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-intune-jsonschema-spectral-rules
scopes:
- name: Microsoft Intune Scopes
  scope_count: 4
  slug: microsoft-intune-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.0
    developer_ergonomics: 13.0
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-intune/refs/heads/main/screenshots/microsoft-intune-2026-06-20T185505.png
security:
- kind: authentication
  name: Microsoft Intune Authentication
  slug: microsoft-intune-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Intune Domain Security
  slug: microsoft-intune-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Intune Vulnerability Disclosure
  slug: microsoft-intune-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-intune
tags:
- App Protection
- Azure
- Compliance
- Device Configuration
- Endpoint Management
- Enrollment
- MAM
- MDM
- Microsoft Graph
- Mobile Application Management
- Mobile Device Management
- Security
website: https://www.microsoft.com/en-us/security/business/microsoft-intune
---
