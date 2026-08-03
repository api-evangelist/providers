---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Threatlocker Agentic Access
  operation_count: 83
  slug: threatlocker-agentic-access
  summary_line: 83 operations · 46 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Public REST API for the ThreatLocker Portal. 83 operations across 18 resource groups — ActionLog, Application, ApprovalRequest, Computer, ComputerCheckin, ComputerGroup, MaintenanceMode, OnlineDevices
  name: ThreatLocker PortalAPI
  slug: threatlocker-portalapi
artifact_total: 7
asyncapis:
- description: ''
  name: Threatlocker Webhooks
  slug: threatlocker-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/threatlocker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/threatlocker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.threatlocker.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://threatlocker.kb.help/api-documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://threatlocker.kb.help/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://portalapi.threatlocker.com/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://threatlocker.kb.help/getting-started-with-threatlocker-portalapis/
- group: operate
  title: ''
  type: Support
  url: https://threatlocker.kb.help/
- group: operate
  title: ''
  type: HelpCenter
  url: https://threatlocker.kb.help/
- group: company
  title: ''
  type: Blog
  url: https://www.threatlocker.com/resources/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.threatlocker.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.threatlocker.com/try-threatlocker
- group: start
  title: ''
  type: Login
  url: https://portal.threatlocker.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.threatlocker.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.threatlocker.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://threatlockerstatus.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://threatlocker.kb.help/portal-release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/threatlocker-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://threatlocker.kb.help/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/threatlocker-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/threatlocker-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/threatlocker-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/threatlocker-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/threatlocker-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/threatlocker-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/threatlocker-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/threatlocker-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/threatlocker-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/threatlocker-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/threatlocker-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/threatlocker-portal-overlay.yaml
created: '2026-08-02'
description: ThreatLocker is a Zero Trust endpoint and cloud security platform used by enterprises and managed service providers to enforce least privilege across endpoints, networks, and cloud workloads. Its capabilities include Application Control (allowlisting), Ringfencing, Elevation Control, Storage Control, Network Control / ZTNA, Web Content Control, Patch Management, and ThreatLocker Detect (managed detection and response). The multi-tenant ThreatLocker Portal is exposed programmatically through the PortalAPI — a public OpenAPI 3.0 REST contract covering action logs, applications, approval requests, computers and computer groups, maintenance mode, organizations, policies, reports, saved searches, scheduled agent actions, system audit, tags, upload requests, and agent versions. The platform is deployed as regionally isolated instances (A–H plus AE1, AU1, CA1, EU1, SA1 and a FedRAMP instance), so both the portal and the API are addressed per instance.
image: https://cdn.prod.website-files.com/6356c441ce34029b327802bf/6972a0af939532eaa67988e1_ThreatLocker_Generic%20OpenGraph-Meta%20image.png
layout: provider
mcp_servers:
- description: ''
  name: threatlocker-mcp.yml
  slug: threatlocker-mcpyml
modified: '2026-08-02'
name: ThreatLocker
nav: Providers
network: true
overview: 'ThreatLocker publishes 1 API on the [APIs.io](https://apis.io/) network: PortalAPI. Tagged areas include cybersecurity, zero-trust, endpoint-security, application-control, and allowlisting.


  The ThreatLocker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThreatLocker''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 53
score:
  band: developing
  composite: 52.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.7
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Threatlocker Authentication
  slug: threatlocker-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Threatlocker Domain Security
  slug: threatlocker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Threatlocker Trust Center
  slug: threatlocker-trust-center
  summary_line: SOC 2 Type II, ISO 27001, FedRAMP
slug: threatlocker
tags:
- cybersecurity
- zero-trust
- endpoint-security
- application-control
- allowlisting
- ransomware-prevention
- privileged-access-management
- network-access-control
- managed-detection-and-response
- device-management
- msp
- compliance
website: https://www.threatlocker.com/
---
