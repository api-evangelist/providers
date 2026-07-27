---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 5
  human_in_the_loop: 1
  name: Adt Agentic Access
  operation_count: 18
  slug: adt-agentic-access
  summary_line: 18 operations · 5 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Manage access codes and user permissions
  name: ADT Access Codes API
  slug: adt-access-codes-api
- description: Manage access control panels, credentials, and schedules
  name: ADT Access Control API
  slug: adt-access-control-api
- description: Manage automation rules and smart home scenes
  name: ADT Automation API
  slug: adt-automation-api
- description: Manage sensors, cameras, and smart home devices
  name: ADT Devices API
  slug: adt-devices-api
- description: Retrieve security events and alarm history
  name: ADT Events API
  slug: adt-events-api
- description: Generate security and compliance reports
  name: ADT Reports API
  slug: adt-reports-api
- description: Manage security systems and arming states
  name: ADT Security Systems API
  slug: adt-security-systems-api
- description: Manage business site security systems
  name: ADT Sites API
  slug: adt-sites-api
- description: Manage security system users and permissions
  name: ADT Users API
  slug: adt-users-api
- description: Manage camera recordings and live video
  name: ADT Video API
  slug: adt-video-api
artifact_total: 109
collections:
- collection_type: open
  name: ADT Business API
  slug: open-adt-business-api
- collection_type: open
  name: ADT+ Platform API
  slug: open-adt-platform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adt-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adt
- group: company
  title: ''
  type: Website
  url: https://www.adt.com
- group: start
  title: ''
  type: Portal
  url: https://www.adt.com/smart-home
- group: operate
  title: ''
  type: Support
  url: https://www.adt.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.adt.com/about-adt/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adt.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adt.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.adt.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.adt.com/get-a-quote
created: '2024-01-01'
description: ADT is a provider of monitored security, interactive home and business automation, and related monitoring services for residential and small business customers across the United States and Canada. ADT offers smart home security systems, professional monitoring, video surveillance, access control, and automation integrations with Google Nest, Amazon Alexa, and Z-Wave smart home devices through the ADT+ platform.
examples:
- key_count: 6
  name: Business Api Credential Example
  slug: business-api-credential-example
- key_count: 3
  name: Business Api Credential Input Example
  slug: business-api-credential-input-example
- key_count: 1
  name: Business Api Credential List Example
  slug: business-api-credential-list-example
- key_count: 4
  name: Business Api Event Report Example
  slug: business-api-event-report-example
- key_count: 5
  name: Business Api Site Example
  slug: business-api-site-example
- key_count: 2
  name: Business Api Site List Example
  slug: business-api-site-list-example
- key_count: 4
  name: Business Api User Example
  slug: business-api-user-example
- key_count: 1
  name: Business Api User List Example
  slug: business-api-user-list-example
- key_count: 5
  name: Platform Api Access Code Example
  slug: platform-api-access-code-example
- key_count: 4
  name: Platform Api Access Code Input Example
  slug: platform-api-access-code-input-example
- key_count: 1
  name: Platform Api Access Code List Example
  slug: platform-api-access-code-list-example
- key_count: 2
  name: Platform Api Arm Request Example
  slug: platform-api-arm-request-example
- key_count: 5
  name: Platform Api Automation Example
  slug: platform-api-automation-example
- key_count: 1
  name: Platform Api Automation List Example
  slug: platform-api-automation-list-example
- key_count: 6
  name: Platform Api Device Example
  slug: platform-api-device-example
- key_count: 1
  name: Platform Api Device List Example
  slug: platform-api-device-list-example
- key_count: 1
  name: Platform Api Disarm Request Example
  slug: platform-api-disarm-request-example
- key_count: 6
  name: Platform Api Event Example
  slug: platform-api-event-example
- key_count: 2
  name: Platform Api Event List Example
  slug: platform-api-event-list-example
- key_count: 6
  name: Platform Api System Example
  slug: platform-api-system-example
- key_count: 1
  name: Platform Api System List Example
  slug: platform-api-system-list-example
- key_count: 3
  name: Platform Api System Status Response Example
  slug: platform-api-system-status-response-example
- key_count: 6
  name: Platform Api Video Clip Example
  slug: platform-api-video-clip-example
- key_count: 1
  name: Platform Api Video Clip List Example
  slug: platform-api-video-clip-list-example
features:
- description: 24/7 professional monitoring center that responds to alarms, contacts emergency services, and alerts homeowners.
  name: Professional Security Monitoring
- description: Programmatic control of lights, locks, thermostats, and smart plugs integrated with the ADT+ security platform.
  name: Smart Home Automation
- description: Access and retrieve recorded video clips from indoor, outdoor, and doorbell cameras via API.
  name: Video Surveillance and Clips
- description: Remotely arm and disarm security systems and zones through authenticated API calls.
  name: Remote Arm and Disarm
- description: Real-time status monitoring of door sensors, motion detectors, smoke detectors, and flood sensors.
  name: Sensor and Device Status
- description: Manage smart locks, access codes, and entry permissions for residential and commercial properties.
  name: Access Control Management
- description: Receive real-time webhook notifications for alarm events, zone violations, and system status changes.
  name: Alarm Event Notifications
- description: Manage multiple properties and security systems from a single API integration for commercial customers.
  name: Multi-Site Management
finops:
- name: Adt Finops
  service_category: Security and Monitoring
  slug: adt-finops
image: /assets/icons/adt.png
json_schemas:
- name: CredentialInput
  property_count: 3
  slug: business-api-credential-input
- name: CredentialList
  property_count: 1
  slug: business-api-credential-list
- name: Credential
  property_count: 6
  slug: business-api-credential
- name: EventReport
  property_count: 4
  slug: business-api-event-report
- name: SiteList
  property_count: 2
  slug: business-api-site-list
- name: Site
  property_count: 5
  slug: business-api-site
- name: UserList
  property_count: 1
  slug: business-api-user-list
- name: User
  property_count: 4
  slug: business-api-user
- name: AccessCodeInput
  property_count: 4
  slug: platform-api-access-code-input
- name: AccessCodeList
  property_count: 1
  slug: platform-api-access-code-list
- name: AccessCode
  property_count: 5
  slug: platform-api-access-code
- name: ArmRequest
  property_count: 2
  slug: platform-api-arm-request
- name: AutomationList
  property_count: 1
  slug: platform-api-automation-list
- name: Automation
  property_count: 5
  slug: platform-api-automation
- name: DeviceList
  property_count: 1
  slug: platform-api-device-list
- name: Device
  property_count: 7
  slug: platform-api-device
- name: DisarmRequest
  property_count: 1
  slug: platform-api-disarm-request
- name: EventList
  property_count: 2
  slug: platform-api-event-list
- name: Event
  property_count: 6
  slug: platform-api-event
- name: SystemList
  property_count: 1
  slug: platform-api-system-list
- name: System
  property_count: 6
  slug: platform-api-system
- name: SystemStatusResponse
  property_count: 3
  slug: platform-api-system-status-response
- name: VideoClipList
  property_count: 1
  slug: platform-api-video-clip-list
- name: VideoClip
  property_count: 7
  slug: platform-api-video-clip
json_structures:
- name: Business Api Credential Input Structure
  property_count: 3
  slug: business-api-credential-input-structure
- name: Business Api Credential List Structure
  property_count: 1
  slug: business-api-credential-list-structure
- name: Business Api Credential Structure
  property_count: 6
  slug: business-api-credential-structure
- name: Business Api Event Report Structure
  property_count: 4
  slug: business-api-event-report-structure
- name: Business Api Site List Structure
  property_count: 2
  slug: business-api-site-list-structure
- name: Business Api Site Structure
  property_count: 5
  slug: business-api-site-structure
- name: Business Api User List Structure
  property_count: 1
  slug: business-api-user-list-structure
- name: Business Api User Structure
  property_count: 4
  slug: business-api-user-structure
- name: Platform Api Access Code Input Structure
  property_count: 4
  slug: platform-api-access-code-input-structure
- name: Platform Api Access Code List Structure
  property_count: 1
  slug: platform-api-access-code-list-structure
- name: Platform Api Access Code Structure
  property_count: 5
  slug: platform-api-access-code-structure
- name: Platform Api Arm Request Structure
  property_count: 2
  slug: platform-api-arm-request-structure
- name: Platform Api Automation List Structure
  property_count: 1
  slug: platform-api-automation-list-structure
- name: Platform Api Automation Structure
  property_count: 5
  slug: platform-api-automation-structure
- name: Platform Api Device List Structure
  property_count: 1
  slug: platform-api-device-list-structure
- name: Platform Api Device Structure
  property_count: 7
  slug: platform-api-device-structure
- name: Platform Api Disarm Request Structure
  property_count: 1
  slug: platform-api-disarm-request-structure
- name: Platform Api Event List Structure
  property_count: 2
  slug: platform-api-event-list-structure
- name: Platform Api Event Structure
  property_count: 6
  slug: platform-api-event-structure
- name: Platform Api System List Structure
  property_count: 1
  slug: platform-api-system-list-structure
- name: Platform Api System Status Response Structure
  property_count: 3
  slug: platform-api-system-status-response-structure
- name: Platform Api System Structure
  property_count: 6
  slug: platform-api-system-structure
- name: Platform Api Video Clip List Structure
  property_count: 1
  slug: platform-api-video-clip-list-structure
- name: Platform Api Video Clip Structure
  property_count: 7
  slug: platform-api-video-clip-structure
jsonld:
- class_count: 11
  name: Adt Business Api Context
  property_count: 17
  slug: adt-business-api-context
- class_count: 19
  name: Adt Platform Api Context
  property_count: 31
  slug: adt-platform-api-context
layout: provider
modified: '2026-04-19'
name: ADT
nav: Providers
network: true
overview: 'ADT publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Access Codes API, Access Control API, Automation API, and 7 more. Tagged areas include Access Control, Automation, Home Security, IoT, and Monitoring.


  The ADT catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  ADT''s developer surface includes authentication, developer portal, support, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Adt Plans Pricing
  plan_count: 1
  slug: adt-plans-pricing
press:
- date: '2026-05-25'
  title: 'The shift from ''smart'' to ''intelligent'': How ADT Is redefining ...'
  url: https://newsroom.adt.com/innovations/the-shift-from-smart-to-intelligent-how-adt-is-redefining-the-future-of-home-security
- date: '2026-05-25'
  title: ADT Invests in Percepta Labs, “Ethical AI” Security ...
  url: https://newsroom.adt.com/adt-commercial/adt-invests-percepta-labs-ethical-ai-security-technology-startup
- date: '2026-05-25'
  title: AI Enhances Safety with ADT's Origin Acquisition
  url: https://www.linkedin.com/posts/darrin-reilly-b0022b7_adt-acquires-origin-ai-to-power-ai-sensing-activity-7432567635315343360-5LtZ
- date: '2026-05-25'
  title: ADT Buys Origin AI – Security Providers are Becoming ...
  url: https://www.parksassociates.com/blogs/home-systems-and-controls/adt-buys-origin-ai-security-providers-are-becoming-whole-home-intelligence-platforms
- date: '2026-05-25'
  title: How ADT embraces AI to make every second count.
  url: https://sierra.ai/customers/adt
random_paper: 41
rate_limits:
- limit_count: 1
  name: Adt Rate Limits
  slug: adt-rate-limits
rules:
- name: ADT API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adt-jsonschema-spectral-rules
- name: ADT API Rules
  rule_count: 37
  severity_counts:
    error: 16
    hint: 0
    info: 6
    warn: 15
  slug: adt-spectral-rules
scopes:
- name: Adt Scopes
  scope_count: 10
  slug: adt-scopes
  summary_line: 10 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 58.1
  delta: 4.6
  facets:
    commercial_clarity: 63.2
    contract_quality: 74.5
    developer_ergonomics: 26.1
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 53.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adt/refs/heads/main/screenshots/adt-2026-06-20T165203.png
security:
- kind: authentication
  name: Adt Authentication
  slug: adt-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Adt Domain Security
  slug: adt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adt
tags:
- Access Control
- Automation
- Home Security
- IoT
- Monitoring
- Security
- Smart Home
- Fortune 1000
use_cases:
- description: Integrate ADT security with third-party home automation platforms like Google Home, Amazon Alexa, and Apple HomeKit.
  name: Home Automation Integration
- description: Manage access codes and security schedules for rental properties, vacation homes, and commercial buildings.
  name: Property Management
- description: Share security monitoring data with insurance providers for smart home insurance discount programs.
  name: Insurance Integration
- description: Trigger automated emergency responses, notifications, and camera recordings when alarms are triggered.
  name: Emergency Response Automation
- description: Analyze security events, access patterns, and alarm history for business operational insights.
  name: Business Intelligence
- description: Issue temporary access codes for service contractors with time-limited entry permissions.
  name: Contractor Access Management
website: https://www.adt.com
---
