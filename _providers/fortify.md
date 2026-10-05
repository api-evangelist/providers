---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 62
  human_in_the_loop: 1
  name: Fortify Agentic Access
  operation_count: 138
  slug: fortify-agentic-access
  summary_line: 138 operations · 62 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage alert definitions
  name: Fortify Alert Definitions API
  slug: fortify-alert-definitions-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage API keys for programmatic access
  name: Fortify API Keys API
  slug: fortify-api-keys-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage applications and their configurations
  name: Fortify Applications API
  slug: fortify-applications-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage scan artifacts and uploads
  name: Fortify Artifacts API
  slug: fortify-artifacts-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage application attributes
  name: Fortify Attributes API
  slug: fortify-attributes-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage audit templates for vulnerability triage
  name: Fortify Audit Templates API
  slug: fortify-audit-templates-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage authentication entities (users and LDAP groups)
  name: Fortify Auth Entities API
  slug: fortify-auth-entities-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage authentication tokens
  name: Fortify Authentication API
  slug: fortify-authentication-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: CI/CD pipeline integration endpoints
  name: Fortify CI/CD API
  slug: fortify-ci-cd-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage cloud scan worker pools
  name: Fortify Cloud Pools API
  slug: fortify-cloud-pools-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage custom tags for issue triage
  name: Fortify Custom Tags API
  slug: fortify-custom-tags-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Configure and start DAST automated scans
  name: Fortify DAST Automated Scans API
  slug: fortify-dast-automated-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Configure and start dynamic application security testing scans
  name: Fortify Dynamic Scans API
  slug: fortify-dynamic-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Access tenant event logs
  name: Fortify Event Logs API
  slug: fortify-event-logs-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: System feature and connectivity information
  name: Fortify Features API
  slug: fortify-features-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage file transfer tokens
  name: Fortify File Tokens API
  slug: fortify-file-tokens-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Retrieve issue filter metadata
  name: Fortify Issue Selectors API
  slug: fortify-issue-selectors-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Access and manage vulnerability issues
  name: Fortify Issues API
  slug: fortify-issues-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Monitor processing jobs
  name: Fortify Jobs API
  slug: fortify-jobs-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Retrieve lookup and reference data
  name: Fortify Lookup Items API
  slug: fortify-lookup-items-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage microservices within applications
  name: Fortify Microservices API
  slug: fortify-microservices-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Configure and start mobile application security testing scans
  name: Fortify Mobile Scans API
  slug: fortify-mobile-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage user notifications
  name: Fortify Notifications API
  slug: fortify-notifications-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: View open source component data
  name: Fortify Open Source Components API
  slug: fortify-open-source-components-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage open source / software composition analysis scans
  name: Fortify Open Source Scans API
  slug: fortify-open-source-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Access performance indicator data
  name: Fortify Performance Indicators API
  slug: fortify-performance-indicators-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage personal access tokens
  name: Fortify Personal Access Tokens API
  slug: fortify-personal-access-tokens-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage application versions within projects
  name: Fortify Project Versions API
  slug: fortify-project-versions-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage top-level projects
  name: Fortify Projects API
  slug: fortify-projects-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage releases within applications
  name: Fortify Releases API
  slug: fortify-releases-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Generate and download reports
  name: Fortify Reports API
  slug: fortify-reports-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage saved report configurations
  name: Fortify Saved Reports API
  slug: fortify-saved-reports-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage scan policies
  name: Fortify Scan Policies API
  slug: fortify-scan-policies-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage scheduled scans
  name: Fortify Scan Schedules API
  slug: fortify-scan-schedules-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage scan configuration settings
  name: Fortify Scan Settings API
  slug: fortify-scan-settings-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: View and manage security scans
  name: Fortify Scans API
  slug: fortify-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage sensor pools for scan distribution
  name: Fortify Sensor Pools API
  slug: fortify-sensor-pools-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage WebInspect sensors
  name: Fortify Sensors API
  slug: fortify-sensors-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Configure and start static application security testing scans
  name: Fortify Static Scans API
  slug: fortify-static-scans-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: System health and configuration
  name: Fortify System API
  slug: fortify-system-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Manage local user accounts
  name: Fortify Users API
  slug: fortify-users-api
- baseURL: https://api.ams.fortify.com
  baseurl_source: declared
  description: Access and manage vulnerability findings
  name: Fortify Vulnerabilities API
  slug: fortify-vulnerabilities-api
artifact_total: 254
collections:
- collection_type: postman
  name: Fortify on Demand Alert Definitions API
  slug: postman-fortify-alert-definitions-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions API Keys API
  slug: postman-fortify-api-keys-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Applications API
  slug: postman-fortify-applications-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Artifacts API
  slug: postman-fortify-artifacts-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Attributes API
  slug: postman-fortify-attributes-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Audit Templates API
  slug: postman-fortify-audit-templates-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Auth Entities API
  slug: postman-fortify-auth-entities-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Authentication API
  slug: postman-fortify-authentication-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions CI/CD API
  slug: postman-fortify-ci-cd-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Cloud Pools API
  slug: postman-fortify-cloud-pools-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Custom Tags API
  slug: postman-fortify-custom-tags-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions DAST Automated Scans API
  slug: postman-fortify-dast-automated-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Dynamic Scans API
  slug: postman-fortify-dynamic-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Event Logs API
  slug: postman-fortify-event-logs-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Features API
  slug: postman-fortify-features-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions File Tokens API
  slug: postman-fortify-file-tokens-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Issue Selectors API
  slug: postman-fortify-issue-selectors-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Issues API
  slug: postman-fortify-issues-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Jobs API
  slug: postman-fortify-jobs-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Lookup Items API
  slug: postman-fortify-lookup-items-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Microservices API
  slug: postman-fortify-microservices-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Mobile Scans API
  slug: postman-fortify-mobile-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Notifications API
  slug: postman-fortify-notifications-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Open Source Components API
  slug: postman-fortify-open-source-components-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Open Source Scans API
  slug: postman-fortify-open-source-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Performance Indicators API
  slug: postman-fortify-performance-indicators-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Personal Access Tokens API
  slug: postman-fortify-personal-access-tokens-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Project Versions API
  slug: postman-fortify-project-versions-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Projects API
  slug: postman-fortify-projects-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Releases API
  slug: postman-fortify-releases-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Reports API
  slug: postman-fortify-reports-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Saved Reports API
  slug: postman-fortify-saved-reports-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Scan Policies API
  slug: postman-fortify-scan-policies-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Scan Schedules API
  slug: postman-fortify-scan-schedules-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Scan Settings API
  slug: postman-fortify-scan-settings-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Scans API
  slug: postman-fortify-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Sensor Pools API
  slug: postman-fortify-sensor-pools-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Sensors API
  slug: postman-fortify-sensors-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Static Scans API
  slug: postman-fortify-static-scans-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions System API
  slug: postman-fortify-system-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Users API
  slug: postman-fortify-users-api
- collection_type: postman
  name: Fortify on Demand Alert Definitions Vulnerabilities API
  slug: postman-fortify-vulnerabilities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fortify on Demand Alert Definitions API
  slug: open-fortify-alert-definitions-api
- collection_type: open
  name: Fortify on Demand Alert Definitions API Keys API
  slug: open-fortify-api-keys-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Applications API
  slug: open-fortify-applications-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Artifacts API
  slug: open-fortify-artifacts-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Attributes API
  slug: open-fortify-attributes-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Audit Templates API
  slug: open-fortify-audit-templates-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Auth Entities API
  slug: open-fortify-auth-entities-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Authentication API
  slug: open-fortify-authentication-api
- collection_type: open
  name: Fortify on Demand Alert Definitions CI/CD API
  slug: open-fortify-ci-cd-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Cloud Pools API
  slug: open-fortify-cloud-pools-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Custom Tags API
  slug: open-fortify-custom-tags-api
- collection_type: open
  name: Fortify on Demand Alert Definitions DAST Automated Scans API
  slug: open-fortify-dast-automated-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Dynamic Scans API
  slug: open-fortify-dynamic-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Event Logs API
  slug: open-fortify-event-logs-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Features API
  slug: open-fortify-features-api
- collection_type: open
  name: Fortify on Demand Alert Definitions File Tokens API
  slug: open-fortify-file-tokens-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Issue Selectors API
  slug: open-fortify-issue-selectors-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Issues API
  slug: open-fortify-issues-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Jobs API
  slug: open-fortify-jobs-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Lookup Items API
  slug: open-fortify-lookup-items-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Microservices API
  slug: open-fortify-microservices-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Mobile Scans API
  slug: open-fortify-mobile-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Notifications API
  slug: open-fortify-notifications-api
- collection_type: open
  name: Fortify on Demand API
  slug: open-fortify-on-demand
- collection_type: open
  name: Fortify on Demand Alert Definitions Open Source Components API
  slug: open-fortify-open-source-components-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Open Source Scans API
  slug: open-fortify-open-source-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Performance Indicators API
  slug: open-fortify-performance-indicators-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Personal Access Tokens API
  slug: open-fortify-personal-access-tokens-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Project Versions API
  slug: open-fortify-project-versions-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Projects API
  slug: open-fortify-projects-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Releases API
  slug: open-fortify-releases-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Reports API
  slug: open-fortify-reports-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Saved Reports API
  slug: open-fortify-saved-reports-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Scan Policies API
  slug: open-fortify-scan-policies-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Scan Schedules API
  slug: open-fortify-scan-schedules-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Scan Settings API
  slug: open-fortify-scan-settings-api
- collection_type: open
  name: Fortify ScanCentral DAST API
  slug: open-fortify-scancentral-dast
- collection_type: open
  name: Fortify on Demand Alert Definitions Scans API
  slug: open-fortify-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Sensor Pools API
  slug: open-fortify-sensor-pools-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Sensors API
  slug: open-fortify-sensors-api
- collection_type: open
  name: Fortify Software Security Center API
  slug: open-fortify-software-security-center
- collection_type: open
  name: Fortify on Demand Alert Definitions Static Scans API
  slug: open-fortify-static-scans-api
- collection_type: open
  name: Fortify on Demand Alert Definitions System API
  slug: open-fortify-system-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Users API
  slug: open-fortify-users-api
- collection_type: open
  name: Fortify on Demand Alert Definitions Vulnerabilities API
  slug: open-fortify-vulnerabilities-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/finops/fortify-finops.yml
  title: ''
  type: FinOps
  url: finops/fortify-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/rate-limits/fortify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fortify-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/rules/fortify-rules.yml
  title: ''
  type: Spectral
  url: rules/fortify-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/rules/fortify-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/fortify-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-ld/fortify-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fortify-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/vocabulary/fortify-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fortify-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/data-model/fortify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fortify-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/errors/fortify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fortify-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/hosts/fortify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fortify-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/vendors/fortify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fortify-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cybersecurity.opentext.com/products/saas-backup/pricing/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/plans/fortify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fortify-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/overlays/fortify-fod-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fortify-fod-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.ams.fortify.com/swagger/ui/index
- group: docs
  title: ''
  type: APIReference
  url: https://api.ams.fortify.com/swagger/ui/index
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/mcp/fortify-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fortify-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/packages/fortify-packages.yml
  title: ''
  type: Packages
  url: packages/fortify-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/cli/fortify-cli.yml
  title: ''
  type: CLI
  url: cli/fortify-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/well-known/fortify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fortify-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/well-known/fortify-well-known.yml
  title: ''
  type: SecurityTxt
  url: well-known/fortify-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/llms/fortify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fortify-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/conformance/fortify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fortify-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/lifecycle/fortify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fortify-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/security/fortify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fortify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.opentext.com/about/security-acknowledgements
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/conventions/fortify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fortify-conventions.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/capabilities/fortify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fortify-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fortify/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/agentic-access/fortify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fortify-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/security/fortify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fortify-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/authentication/fortify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fortify-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://ams.fortify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.microfocus.com/documentation/fortify-on-demand/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.microfocus.com/documentation/fortify-on-demand/
- group: auth
  title: ''
  type: Authentication
  url: https://api.ams.fortify.com/swagger/ui/index
- group: company
  title: ''
  type: Blog
  url: https://community.opentext.com/cyberres/b/cybersecurity-blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fortify.com/
- group: operate
  title: ''
  type: Support
  url: https://www.opentext.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opentext.com/about/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opentext.com/about/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortify
- group: operate
  title: ''
  type: Community
  url: https://community.opentext.com/cybersec/fortify
- group: company
  title: ''
  type: Website
  url: https://www.opentext.com/products/fortify-on-demand
- group: start
  title: ''
  type: Login
  url: https://ams.fortify.com/
- group: start
  title: ''
  type: Signup
  url: https://www.opentext.com/products/fortify-on-demand/trial
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.opentext.com/cybersec/fortify/w/tips
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fortify/fortify-client-api
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-ld/fortify-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/fortify-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-schema/fortify-application-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fortify-application-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-schema/fortify-vulnerability-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fortify-vulnerability-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-schema/fortify-scan-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fortify-scan-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-schema/fortify-release-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fortify-release-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/json-schema/fortify-project-version-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fortify-project-version-schema.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/fortify/skills
created: '2024-01-15'
description: Fortify is a comprehensive application security platform from OpenText that provides static application security testing (SAST), dynamic application security testing (DAST), and software composition analysis (SCA) capabilities. It helps organizations identify and remediate vulnerabilities across the software development lifecycle.
finops:
- name: Fortify Finops
  service_category: Application Security
  slug: fortify-finops
image: https://www.microfocus.com/brand/fortify-logo.png
json_schemas:
- name: AlertDefinitionListResponse
  property_count: 2
  slug: fortify-alert-definition-list-response
- name: ApiKeyListResponse
  property_count: 2
  slug: fortify-api-key-list-response
- name: ApiKeyRequest
  property_count: 2
  slug: fortify-api-key-request
- name: ApiKeyResponse
  property_count: 1
  slug: fortify-api-key-response
- name: ApiKey
  property_count: 5
  slug: fortify-api-key
- name: ApiResultArtifact
  property_count: 3
  slug: fortify-api-result-artifact
- name: ApiResultAttributeDefinition
  property_count: 3
  slug: fortify-api-result-attribute-definition
- name: ApiResultAuthToken
  property_count: 3
  slug: fortify-api-result-auth-token
- name: ApiResultCustomTag
  property_count: 3
  slug: fortify-api-result-custom-tag
- name: ApiResultFileToken
  property_count: 3
  slug: fortify-api-result-file-token
- name: ApiResultIssue
  property_count: 3
  slug: fortify-api-result-issue
- name: ApiResultJob
  property_count: 3
  slug: fortify-api-result-job
- name: ApiResultLocalUser
  property_count: 3
  slug: fortify-api-result-local-user
- name: ApiResultProject
  property_count: 3
  slug: fortify-api-result-project
- name: ApiResultProjectVersion
  property_count: 3
  slug: fortify-api-result-project-version
- name: ApiResultSavedReport
  property_count: 3
  slug: fortify-api-result-saved-report
- name: ApiResultVoid
  property_count: 2
  slug: fortify-api-result-void
- name: ApplicationIssueCountListResponse
  property_count: 1
  slug: fortify-application-issue-count-list-response
- name: Fortify Application
  property_count: 10
  slug: fortify-application
- name: ArtifactListResponse
  property_count: 2
  slug: fortify-artifact-list-response
- name: AttributeListResponse
  property_count: 2
  slug: fortify-attribute-list-response
- name: AttributeValue
  property_count: 4
  slug: fortify-attribute-value
- name: AuthEntityListResponse
  property_count: 2
  slug: fortify-auth-entity-list-response
- name: AuthEntity
  property_count: 3
  slug: fortify-auth-entity
- name: CategoryRollupsResponse
  property_count: 1
  slug: fortify-category-rollups-response
- name: CloudPoolListResponse
  property_count: 2
  slug: fortify-cloud-pool-list-response
- name: CreateAttributeDefinitionRequest
  property_count: 6
  slug: fortify-create-attribute-definition-request
- name: CreateFileTokenRequest
  property_count: 1
  slug: fortify-create-file-token-request
- name: CreateLocalUserRequest
  property_count: 8
  slug: fortify-create-local-user-request
- name: CreateProjectRequest
  property_count: 3
  slug: fortify-create-project-request
- name: CreateProjectVersionRequest
  property_count: 6
  slug: fortify-create-project-version-request
- name: CreateScanScheduleRequest
  property_count: 6
  slug: fortify-create-scan-schedule-request
- name: CreateScanSettingsRequest
  property_count: 6
  slug: fortify-create-scan-settings-request
- name: CreateSensorPoolRequest
  property_count: 2
  slug: fortify-create-sensor-pool-request
- name: CreateTokenRequest
  property_count: 3
  slug: fortify-create-token-request
- name: CustomTagListResponse
  property_count: 2
  slug: fortify-custom-tag-list-response
- name: DastScan
  property_count: 17
  slug: fortify-dast-scan
- name: DastScanSummary
  property_count: 11
  slug: fortify-dast-scan-summary
- name: DeleteResponse
  property_count: 1
  slug: fortify-delete-response
- name: FeatureListResponse
  property_count: 2
  slug: fortify-feature-list-response
- name: FortifyConnectNetworkListResponse
  property_count: 2
  slug: fortify-fortify-connect-network-list-response
- name: GenerateReportRequest
  property_count: 4
  slug: fortify-generate-report-request
- name: GetAuditOptionsResponse
  property_count: 1
  slug: fortify-get-audit-options-response
- name: GetDastAutomatedScanSetupResponse
  property_count: 7
  slug: fortify-get-dast-automated-scan-setup-response
- name: GetDynamicScanSetupResponse
  property_count: 4
  slug: fortify-get-dynamic-scan-setup-response
- name: GetStaticScanOptionsResponse
  property_count: 2
  slug: fortify-get-static-scan-options-response
- name: HealthResponse
  property_count: 2
  slug: fortify-health-response
- name: IssueListResponse
  property_count: 2
  slug: fortify-issue-list-response
- name: IssueSelectorSetResponse
  property_count: 1
  slug: fortify-issue-selector-set-response
- name: JobListResponse
  property_count: 2
  slug: fortify-job-list-response
- name: LocalUserListResponse
  property_count: 2
  slug: fortify-local-user-list-response
- name: LookupItemListResponse
  property_count: 2
  slug: fortify-lookup-item-list-response
- name: MarkNotificationsAsReadRequest
  property_count: 1
  slug: fortify-mark-notifications-as-read-request
- name: MicroserviceListResponse
  property_count: 2
  slug: fortify-microservice-list-response
- name: MobileScanSetup
  property_count: 5
  slug: fortify-mobile-scan-setup
- name: NotificationListResponse
  property_count: 2
  slug: fortify-notification-list-response
- name: OpenSourceComponentListResponse
  property_count: 2
  slug: fortify-open-source-component-list-response
- name: PerformanceIndicatorListResponse
  property_count: 2
  slug: fortify-performance-indicator-list-response
- name: PersonalAccessToken
  property_count: 4
  slug: fortify-personal-access-token
- name: PollingScanSummary
  property_count: 5
  slug: fortify-polling-scan-summary
- name: PostApiKeyResponse
  property_count: 3
  slug: fortify-post-api-key-response
- name: PostApplicationRequest
  property_count: 9
  slug: fortify-post-application-request
- name: PostApplicationResponse
  property_count: 3
  slug: fortify-post-application-response
- name: PostAttributeRequest
  property_count: 4
  slug: fortify-post-attribute-request
- name: PostAuditActionRequest
  property_count: 1
  slug: fortify-post-audit-action-request
- name: PostMicroserviceRequest
  property_count: 1
  slug: fortify-post-microservice-request
- name: PostMicroserviceResponse
  property_count: 2
  slug: fortify-post-microservice-response
- name: PostReleaseRequest
  property_count: 5
  slug: fortify-post-release-request
- name: ProjectListResponse
  property_count: 2
  slug: fortify-project-list-response
- name: ProjectVersionActionRequest
  property_count: 2
  slug: fortify-project-version-action-request
- name: ProjectVersionListResponse
  property_count: 2
  slug: fortify-project-version-list-response
- name: Fortify Project Version
  property_count: 11
  slug: fortify-project-version
- name: PutApplicationRequest
  property_count: 5
  slug: fortify-put-application-request
- name: PutAttributeRequest
  property_count: 3
  slug: fortify-put-attribute-request
- name: PutDastAutomatedOpenApiScanSetupRequest
  property_count: 7
  slug: fortify-put-dast-automated-open-api-scan-setup-request
- name: PutDastAutomatedWebsiteScanSetupRequest
  property_count: 10
  slug: fortify-put-dast-automated-website-scan-setup-request
- name: PutDynamicScanSetupRequest
  property_count: 9
  slug: fortify-put-dynamic-scan-setup-request
- name: PutDynamicScanSetupResponse
  property_count: 1
  slug: fortify-put-dynamic-scan-setup-response
- name: PutMobileScanSetupRequest
  property_count: 5
  slug: fortify-put-mobile-scan-setup-request
- name: PutMobileScanSetupResponse
  property_count: 1
  slug: fortify-put-mobile-scan-setup-response
- name: Fortify Release
  property_count: 19
  slug: fortify-release
- name: ReportDefinitionListResponse
  property_count: 2
  slug: fortify-report-definition-list-response
- name: SavedReportListResponse
  property_count: 2
  slug: fortify-saved-report-list-response
- name: ScanPolicyListResponse
  property_count: 2
  slug: fortify-scan-policy-list-response
- name: ScanPolicy
  property_count: 4
  slug: fortify-scan-policy
- name: ScanScheduleListResponse
  property_count: 2
  slug: fortify-scan-schedule-list-response
- name: ScanSchedule
  property_count: 7
  slug: fortify-scan-schedule
- name: Fortify Scan
  property_count: 20
  slug: fortify-scan
- name: ScanSettingsListResponse
  property_count: 2
  slug: fortify-scan-settings-list-response
- name: ScanSettings
  property_count: 11
  slug: fortify-scan-settings
- name: SensorListResponse
  property_count: 2
  slug: fortify-sensor-list-response
- name: SensorPoolListResponse
  property_count: 2
  slug: fortify-sensor-pool-list-response
- name: SensorPool
  property_count: 5
  slug: fortify-sensor-pool
- name: Sensor
  property_count: 11
  slug: fortify-sensor
- name: StartDynamicScanRequest
  property_count: 8
  slug: fortify-start-dynamic-scan-request
- name: StartScanCicdRequest
  property_count: 2
  slug: fortify-start-scan-cicd-request
- name: StartScanRequest
  property_count: 3
  slug: fortify-start-scan-request
- name: StartScanResponse
  property_count: 2
  slug: fortify-start-scan-response
- name: UpdateLocalUserRequest
  property_count: 6
  slug: fortify-update-local-user-request
- name: UpdateProjectRequest
  property_count: 3
  slug: fortify-update-project-request
- name: UpdateProjectVersionRequest
  property_count: 5
  slug: fortify-update-project-version-request
- name: UpdateScanScheduleRequest
  property_count: 6
  slug: fortify-update-scan-schedule-request
- name: UpdateScanSettingsRequest
  property_count: 6
  slug: fortify-update-scan-settings-request
- name: UpdateSensorPoolRequest
  property_count: 2
  slug: fortify-update-sensor-pool-request
- name: UpdateSensorRequest
  property_count: 2
  slug: fortify-update-sensor-request
- name: VulnerabilityListResponse
  property_count: 2
  slug: fortify-vulnerability-list-response
- name: Fortify Vulnerability
  property_count: 24
  slug: fortify-vulnerability
jsonld:
- class_count: 0
  name: Fortify Context
  property_count: 11
  slug: fortify-context
layout: provider
modified: '2026-05-19'
name: Fortify
nav: Providers
network: true
overview: 'Fortify publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Alert Definitions API, API Keys API, Applications API, and 39 more. Tagged areas include Application Security, DAST, DevSecOps, SAST, and SCA.


  The Fortify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Fortify''s developer surface includes pricing, API reference, CLI, authentication, developer portal, documentation, getting-started guide, and 48 more developer resources.'
plans:
- name: Fortify Plans Pricing
  plan_count: 0
  slug: fortify-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Fortify Rate Limits
  slug: fortify-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Fortify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fortify-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Fortify API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: fortify-rules
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 72.0
    discoverability: 85.7
    operational_transparency: 34.2
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fortify/refs/heads/main/screenshots/fortify-2026-08-17T123433.png
security:
- kind: authentication
  name: Fortify Authentication
  slug: fortify-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Fortify Domain Security
  slug: fortify-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Fortify Vulnerability Disclosure
  slug: fortify-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 7
skills:
- name: fcli-common
  slug: fcli-common
- name: fortify-cicd-integration
  slug: fortify-cicd-integration
- name: fortify-create-app
  slug: fortify-create-app
- name: fortify-exploitability-analysis
  slug: fortify-exploitability-analysis
- name: fortify-fod
  slug: fortify-fod
- name: fortify-remediate
  slug: fortify-remediate
- name: fortify-ssc
  slug: fortify-ssc
slug: fortify
tags:
- Application Security
- DAST
- DevSecOps
- SAST
- SCA
- Security Testing
- Vulnerability Scanning
website: https://www.opentext.com/products/fortify-on-demand
---
