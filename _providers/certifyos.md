---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 350
  human_in_the_loop: 61
  name: Certifyos Agentic Access
  operation_count: 520
  slug: certifyos-agentic-access
  summary_line: 520 operations · 350 acting · 61 human-in-the-loop
api_count: 59
apis:
- description: Address standardization and validation preview (CP-28784)
  name: Certifyos Address Standardization API
  slug: certifyos-addressstandardization-api
- description: Authentication endpoints
  name: Certifyos Auth API
  slug: certifyos-auth-api
- description: The Auth Resource API from Certifyos — 1 operation(s) for auth resource.
  name: Certifyos Auth Resource API
  slug: certifyos-auth-resource-api
- description: The auth-tokens API from Certifyos — 1 operation(s) for auth-tokens.
  name: Certifyos Auth Tokens API
  slug: certifyos-auth-tokens-api
- description: APIs for managing contracts entities
  name: Certifyos Contracts API
  slug: certifyos-contracts-api
- description: The Credentialing Outreach Resource API from Certifyos — 5 operation(s) for credentialing outreach resource.
  name: Certifyos Credentialing Outreach Resource API
  slug: certifyos-credentialing-outreach-resource-api
- description: The credentialing-workflows API from Certifyos — 5 operation(s) for credentialing-workflows.
  name: Certifyos Credentialing Workflows API
  slug: certifyos-credentialing-workflows-api
- description: APIs for managing credentialing workflows
  name: Certifyos Credentialing Workflow API
  slug: certifyos-credentialingworkflow-api
- description: The Dal Reactive Test Resource API from Certifyos — 1 operation(s) for dal reactive test resource.
  name: Certifyos Dal Reactive Test Resource API
  slug: certifyos-dal-reactive-test-resource-api
- description: APIs for directory operations
  name: Certifyos Directory API
  slug: certifyos-directory-api
- description: Operations for managing egress template configurations
  name: Certifyos Egress Template API
  slug: certifyos-egresstemplate-api
- description: Manage event email notification settings
  name: Certifyos Event Email Settings API
  slug: certifyos-event-email-settings-api
- description: APIs for managing facility entities
  name: Certifyos Facility API
  slug: certifyos-facility-api
- description: The Facility Credentialing Outreach Resource API from Certifyos — 4 operation(s) for facility credentialing outreach resource.
  name: Certifyos Facility Credentialing Outreach Resource API
  slug: certifyos-facility-credentialing-outreach-resource-api
- description: APIs for managing notes in facility credentialing workflows
  name: Certifyos Facility Note API
  slug: certifyos-facility-note-api
- description: APIs for managing facility credentialing workflows
  name: Certifyos Facility Credentialing Workflow API
  slug: certifyos-facilitycredentialingworkflow-api
- description: The File Storage Resource API from Certifyos — 3 operation(s) for file storage resource.
  name: Certifyos File Storage Resource API
  slug: certifyos-file-storage-resource-api
- description: APIs for managing flag entities
  name: Certifyos Flag API
  slug: certifyos-flag-api
- description: APIs for calculating and managing flags for monitoring workflows
  name: Certifyos Flag Calculator API
  slug: certifyos-flagcalculator-api
- description: The flags API from Certifyos — 10 operation(s) for flags.
  name: Certifyos Flags API
  slug: certifyos-flags-api
- description: APIs for managing form submissions
  name: Certifyos Form Submissions API
  slug: certifyos-form-submissions-api
- description: The forms API from Certifyos — 2 operation(s) for forms.
  name: Certifyos Forms API
  slug: certifyos-forms-api
- description: APIs for managing group entities
  name: Certifyos Group API
  slug: certifyos-group-api
- description: Endpoints for managing locations.
  name: Certifyos Locations API
  slug: certifyos-locations-api
- description: APIs for managing monitoring runs
  name: Certifyos Monitoring Run API
  slug: certifyos-monitoringrun-api
- description: APIs for managing monitoring workflows
  name: Certifyos Monitoring Workflow API
  slug: certifyos-monitoringworkflow-api
- description: APIs for managing notes in monitoring workflows
  name: Certifyos Monitoring Workflow Note API
  slug: certifyos-monitoringworkflownote-api
- description: APIs for managing network entities
  name: Certifyos Network API
  slug: certifyos-network-api
- description: APIs for managing notes in credentialing workflows
  name: Certifyos Note API
  slug: certifyos-note-api
- description: NPI validation operations
  name: Certifyos Npi Validation API
  slug: certifyos-npivalidation-api
- description: The Organization Outreach Settings Resource API from Certifyos — 4 operation(s) for organization outreach settings resource.
  name: Certifyos Organization Outreach Settings Resource API
  slug: certifyos-organization-outreach-settings-resource-api
- description: This resource represents a payer in the healthcare system. A payer refers to an entity that finances or reimburses the cost of health services. Use it to get, create, and update payers.
  name: Certifyos Payers API
  slug: certifyos-payers-api
- description: APIs for managing permissions
  name: Certifyos Permission API
  slug: certifyos-permission-api
- description: APIs for managing plan entities
  name: Certifyos Plan API
  slug: certifyos-plan-api
- description: Endpoints for managing practitioner information and associations.
  name: Certifyos Practitioner API
  slug: certifyos-practitioner-api
- description: The providers API from Certifyos — 4 operation(s) for providers.
  name: Certifyos Providers API
  slug: certifyos-providers-api
- description: Endpoints for managing roles.
  name: Certifyos Role API
  slug: certifyos-role-api
- description: The Role Resource API from Certifyos — 1 operation(s) for role resource.
  name: Certifyos Role Resource API
  slug: certifyos-role-resource-api
- description: APIs for managing roster file uploads and processing
  name: Certifyos Roster API
  slug: certifyos-roster-api
- description: APIs for roster upload file column mappings
  name: Certifyos Roster upload API
  slug: certifyos-roster-upload-api
- description: APIs for managing individual roster record entries
  name: Certifyos Roster Record API
  slug: certifyos-rosterrecord-api
- description: The Send Grid Webhook Resource API from Certifyos — 2 operation(s) for send grid webhook resource.
  name: Certifyos Send Grid Webhook Resource API
  slug: certifyos-send-grid-webhook-resource-api
- description: Endpoints for managing medical specialties.
  name: Certifyos Specialty API
  slug: certifyos-specialty-api
- description: Cloud storage operations and file access management
  name: Certifyos Storage API
  slug: certifyos-storage-api
- description: APIs for managing roster templates and configurations
  name: Certifyos Template API
  slug: certifyos-template-api
- description: Endpoints for managing tenant configurations.
  name: Certifyos Tenant Configuration API
  slug: certifyos-tenant-configuration-api
- description: Endpoints for managing tenant-specific specialties.
  name: Certifyos Tenant Specialty API
  slug: certifyos-tenant-specialty-api
- description: Endpoints for managing UDF schemas.
  name: Certifyos UDF Schema API
  slug: certifyos-udf-schema-api
- description: Endpoints for managing users.
  name: Certifyos User API
  slug: certifyos-user-api
- description: The v2/credentialing-workflows API from Certifyos — 5 operation(s) for v2/credentialing-workflows.
  name: Certifyos V2/credentialing Workflows API
  slug: certifyos-v2-credentialing-workflows-api
- description: The v2/facilities API from Certifyos — 8 operation(s) for v2/facilities.
  name: Certifyos V2/facilities API
  slug: certifyos-v2-facilities-api
- description: The v2/facility-credentialing-workflows API from Certifyos — 3 operation(s) for v2/facility-credentialing-workflows.
  name: Certifyos V2/facility Credentialing Workflows API
  slug: certifyos-v2-facility-credentialing-workflows-api
- description: The v2/flags API from Certifyos — 4 operation(s) for v2/flags.
  name: Certifyos V2/flags API
  slug: certifyos-v2-flags-api
- description: The v2/groups API from Certifyos — 1 operation(s) for v2/groups.
  name: Certifyos V2/groups API
  slug: certifyos-v2-groups-api
- description: The v2/provider API from Certifyos — 14 operation(s) for v2/provider.
  name: Certifyos V2/provider API
  slug: certifyos-v2-provider-api
- description: The v2/provider-with-groups API from Certifyos — 1 operation(s) for v2/provider-with-groups.
  name: Certifyos V2/provider With Groups API
  slug: certifyos-v2-provider-with-groups-api
- description: The v2/providers API from Certifyos — 7 operation(s) for v2/providers.
  name: Certifyos V2/providers API
  slug: certifyos-v2-providers-api
- description: APIs for managing webhook entities
  name: Certifyos Webhook API
  slug: certifyos-webhook-api
- description: APIs for managing webhooks
  name: Certifyos Webhooks API
  slug: certifyos-webhooks-api
artifact_total: 64
asyncapis:
- description: ''
  name: Certifyos Webhooks
  slug: certifyos-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/certifyos-api-service-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/certifyos-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.certifyos.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.certifyos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.certifyos.com/providerhub
- group: docs
  title: ''
  type: APIReference
  url: https://docs.certifyos.com/reference/api-service/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.certifyos.com/providerhub#getting-started
- group: operate
  title: ''
  type: Support
  url: https://certifyos.atlassian.net/servicedesk/customer/portal/53
- group: start
  title: ''
  type: Login
  url: https://ng.certifyos.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.certifyos.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CertifyOS
- group: operate
  title: ''
  type: StatusPage
  url: https://status.certifyos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certifyos.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certifyos.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.certifyos.com/company/news/third-soc2-compliance
- group: auth
  title: ''
  type: Authentication
  url: authentication/certifyos-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certifyos-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certifyos-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/certifyos-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/certifyos-mcp.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/certifyos-json-schema.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/certifyos-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/certifyos-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/certifyos-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/certifyos-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certifyos-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/certifyos-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Certify (operating as CertifyOS, certifyos.com) is a New York-based healthcare provider data platform that automates the end-to-end provider network management lifecycle: credentialing, licensing, payer enrollment, compliance monitoring, and roster management. Founded in 2020 by CEO Anshul Rathi, the company describes itself as API-first and UI-agnostic, connecting directly to hundreds of primary sources for real-time primary source verification (PSV) and exposing verified provider data to downstream systems through REST APIs, webhooks, and bulk exports. Its public developer surface — the Certify ProviderHub API — is documented on a Redocly-hosted docs site and backed by three published OpenAPI documents covering 520 operations across practitioner, facility, credentialing-workflow, monitoring, roster, contract, network, and tenant/role administration. The company also publishes ~95 first-party JSON Schemas at stable canonical URLs on schemas.certifyos.com. Customers are payers,
  health systems, multi-state provider groups, and digital-health companies. Backed by General Catalyst, Transformation Capital, Upfront Ventures, and SemperVirens; total disclosed funding $70.45M through a $40M Series B in June 2025.'
image: https://www.certifyos.com/certifyos-favicon.png
layout: provider
mcp_servers:
- description: ''
  name: certifyos-mcp.yml
  slug: certifyos-mcpyml
modified: '2026-08-08'
name: Certifyos
nav: Providers
network: true
overview: 'Certifyos publishes 59 APIs on the [APIs.io](https://apis.io/) network, including Address Standardization API, Auth API, Auth Resource API, and 56 more. Tagged areas include Company, Healthcare, Provider Data, Credentialing, and Licensing.


  The Certifyos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Certifyos'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 56
score:
  band: developing
  composite: 49.9
  delta: -0.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 69.2
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 59
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certifyos/refs/heads/main/screenshots/certifyos-2026-07-25T205001.png
security:
- kind: authentication
  name: Certifyos Authentication
  slug: certifyos-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Certifyos Domain Security
  slug: certifyos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: certifyos
tags:
- Company
- Healthcare
- Provider Data
- Credentialing
- Licensing
- Payer Enrollment
- Primary Source Verification
- Provider Network Management
- Roster Management
- Compliance Monitoring
- Healthcare API
- Webhooks
website: https://www.certifyos.com/
---
