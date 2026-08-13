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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 26
  human_in_the_loop: 3
  name: Cisco Expressway Agentic Access
  operation_count: 47
  slug: cisco-expressway-agentic-access
  summary_line: 47 operations · 26 acting · 3 human-in-the-loop
api_count: 18
apis:
- description: 'SNMP-based monitoring and management interface for Cisco Expressway providing access to system metrics, alarms, and configuration data. Supports SNMP versions v2c and v3 for secure network management '
  name: Cisco Expressway SNMP API
  slug: cisco-expressway-snmp-api
- description: Legacy XML-based API for configuration and status retrieval on Cisco Expressway systems. Uses HTTP Basic Authentication over HTTPS for secure access to system configuration and management functions.
  name: Cisco Expressway XML API
  slug: cisco-expressway-xml-api
- description: Administrator account management
  name: Cisco Expressway Admin Account API
  slug: cisco-expressway-admin-account-api
- description: Active system alarms and warnings
  name: Cisco Expressway Alarms API
  slug: cisco-expressway-alarms-api
- description: Active and historical call information
  name: Cisco Expressway Calls API
  slug: cisco-expressway-calls-api
- description: DNS server configuration management
  name: Cisco Expressway DNS API
  slug: cisco-expressway-dns-api
- description: Smart licensing status and usage
  name: Cisco Expressway Licensing API
  slug: cisco-expressway-licensing-api
- description: NTP server configuration for time synchronization
  name: Cisco Expressway NTP API
  slug: cisco-expressway-ntp-api
- description: Device registration status and details
  name: Cisco Expressway Registrations API
  slug: cisco-expressway-registrations-api
- description: System resource utilization metrics
  name: Cisco Expressway Resource Usage API
  slug: cisco-expressway-resource-usage-api
- description: Search rule configuration for call routing decisions
  name: Cisco Expressway Search Rules API
  slug: cisco-expressway-search-rules-api
- description: SFTP configuration for system upgrades
  name: Cisco Expressway SFTP API
  slug: cisco-expressway-sftp-api
- description: SIP protocol configuration
  name: Cisco Expressway SIP API
  slug: cisco-expressway-sip-api
- description: System-level configuration and information
  name: Cisco Expressway System API
  slug: cisco-expressway-system-api
- description: System overview and health information
  name: Cisco Expressway System Status API
  slug: cisco-expressway-system-status-api
- description: Pre-search transform configuration for alias modification
  name: Cisco Expressway Transforms API
  slug: cisco-expressway-transforms-api
- description: System upgrade operations
  name: Cisco Expressway Upgrade API
  slug: cisco-expressway-upgrade-api
- description: Zone configuration for call routing and firewall traversal
  name: Cisco Expressway Zones API
  slug: cisco-expressway-zones-api
arazzos:
- description: List active calls, active TURN relays, and recent call history for media diagnosis.
  name: Cisco Expressway Active Call Troubleshooting
  slug: cisco-expressway-active-call-troubleshooting-workflow
- description: Read resource usage, then list registrations and active calls to audit load.
  name: Cisco Expressway Capacity and Registrations Audit
  slug: cisco-expressway-capacity-registrations-audit-workflow
- description: Add a pre-search transform, confirm it, then add a search rule that uses the normalized alias.
  name: Cisco Expressway Create Dial Plan Transform
  slug: cisco-expressway-create-dial-plan-transform-workflow
- description: Create a DNS zone for endpoint discovery and a search rule that routes to it.
  name: Cisco Expressway Create DNS Zone Routing
  slug: cisco-expressway-create-dns-zone-routing-workflow
- description: Read smart licensing status and branch on registration to read resource usage.
  name: Cisco Expressway Licensing Compliance Check
  slug: cisco-expressway-licensing-compliance-check-workflow
- description: Create a neighbor zone and a search rule that routes matching calls to it.
  name: Cisco Expressway Onboard Neighbor Zone Routing
  slug: cisco-expressway-onboard-neighbor-zone-routing-workflow
- description: Read system status, active alarms, and resource usage to gate an upgrade.
  name: Cisco Expressway Pre-Upgrade Health Check
  slug: cisco-expressway-pre-upgrade-health-check-workflow
- description: Add a DNS server to an Expressway node and confirm it was applied.
  name: Cisco Expressway Provision DNS Server
  slug: cisco-expressway-provision-dns-server-workflow
- description: Add an NTP time source to an Expressway node and confirm it was applied.
  name: Cisco Expressway Provision NTP Server
  slug: cisco-expressway-provision-ntp-server-workflow
- description: Identify the node, then change an administrator account password.
  name: Cisco Expressway Rotate Admin Password
  slug: cisco-expressway-rotate-admin-password-workflow
- description: Create the matched server/client zones that form an Expressway-E to Expressway-C traversal.
  name: Cisco Expressway Set Up Firewall Traversal Pair
  slug: cisco-expressway-setup-traversal-pair-workflow
- description: Set SFTP details, trigger a software upgrade, then poll upgrade status.
  name: Cisco Expressway System Upgrade
  slug: cisco-expressway-system-upgrade-workflow
- description: Read current SIP configuration, apply changes, then confirm via system status.
  name: Cisco Expressway Update SIP Configuration
  slug: cisco-expressway-update-sip-configuration-workflow
- description: Read upgrade status, then read system status to confirm the running version.
  name: Cisco Expressway Upgrade Progress Monitor
  slug: cisco-expressway-upgrade-progress-monitor-workflow
- description: Inspect zone connectivity, active calls, and recent call history together.
  name: Cisco Expressway Zone Health Investigation
  slug: cisco-expressway-zone-health-investigation-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: Cisco Expressway Configuration API
  slug: postman-cisco-expressway-configuration-api
- collection_type: postman
  name: Cisco Expressway Status API
  slug: postman-cisco-expressway-status-api
- collection_type: open
  name: Cisco Expressway Configuration API
  slug: open-cisco-expressway-configuration-api
- collection_type: open
  name: Cisco Expressway Status API
  slug: open-cisco-expressway-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-expressway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-expressway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-expressway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-expressway-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cisco-expressway/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-active-call-troubleshooting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-capacity-registrations-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-create-dial-plan-transform-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-create-dns-zone-routing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-licensing-compliance-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-onboard-neighbor-zone-routing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-pre-upgrade-health-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-provision-dns-server-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-provision-ntp-server-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-rotate-admin-password-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-setup-traversal-pair-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-system-upgrade-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-update-sip-configuration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-upgrade-progress-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cisco-expressway-zone-health-investigation-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-programming-reference-guides-list.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html
- group: auth
  title: ''
  type: Authentication
  url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/collaboration
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cisco.com/c/en/us/support/web/cloud-status.html
- group: operate
  title: ''
  type: Support
  url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/devnet/ct-p/4409j-developer-home
- group: company
  title: ''
  type: Website
  url: https://www.cisco.com/c/en/us/products/unified-communications/expressway-series/index.html
- group: start
  title: ''
  type: Login
  url: https://developer.cisco.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.cisco.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-release-notes-list.html
- group: other
  title: ''
  type: Downloads
  url: https://software.cisco.com/download/home/286282896
- group: other
  title: ''
  type: Compatibility
  url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-device-support-tables-list.html
- group: design
  title: ''
  type: Spectral
  url: rules/cisco-expressway-rules.yml
created: '2024-01-01'
description: API definitions for Cisco Expressway, a session border controller and firewall traversal solution for Unified Communications that provides secure remote and mobile access for collaboration workloads including video, voice, content, and presence. Programmatic access spans a REST API for configuration (/api/provisioning), a REST API for status and observability (/api/status), an SNMP MIB for metrics, and a legacy XML API for systems still in transition.
finops:
- name: Cisco Expressway Finops
  service_category: Unified Communications
  slug: cisco-expressway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-expressway.png
json_schemas:
- name: Cisco Expressway Alarm
  property_count: 6
  slug: cisco-expressway-alarm
- name: Cisco Expressway Call
  property_count: 16
  slug: cisco-expressway-call
- name: Cisco Expressway Registration
  property_count: 7
  slug: cisco-expressway-registration
- name: Cisco Expressway Search Rule
  property_count: 11
  slug: cisco-expressway-search-rule
- name: Cisco Expressway System Status
  property_count: 12
  slug: cisco-expressway-system-status
- name: Cisco Expressway Pre-Search Transform
  property_count: 8
  slug: cisco-expressway-transform
- name: Cisco Expressway Zone
  property_count: 32
  slug: cisco-expressway-zone
jsonld:
- class_count: 0
  name: Cisco Expressway Context
  property_count: 53
  slug: cisco-expressway-context
layout: provider
modified: '2026-05-19'
name: Cisco Expressway
nav: Providers
network: true
overview: 'Cisco Expressway publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Admin Account API, Alarms API, Calls API, and 13 more. Tagged areas include Collaboration, Firewall Traversal, H.323, Session Border Controller, and SIP.


  The Cisco Expressway catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cisco Expressway''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 31 more developer resources.'
plans:
- name: Cisco Expressway Plans Pricing
  plan_count: 1
  slug: cisco-expressway-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Cisco Expressway Rate Limits
  slug: cisco-expressway-rate-limits
rules:
- name: Cisco Expressway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cisco-expressway-jsonschema-spectral-rules
- name: Cisco Expressway API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: cisco-expressway-rules
score:
  band: strong
  composite: 56.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 72.4
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/screenshots/cisco-expressway-2026-06-20T174356.png
security:
- kind: authentication
  name: Cisco Expressway Authentication
  slug: cisco-expressway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Expressway Domain Security
  slug: cisco-expressway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Expressway Vulnerability Disclosure
  slug: cisco-expressway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cisco-expressway
tags:
- Collaboration
- Firewall Traversal
- H.323
- Session Border Controller
- SIP
- Unified Communications
- Video Conferencing
website: https://www.cisco.com/c/en/us/products/unified-communications/expressway-series/index.html
---
