---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.7
  scored_at: '2026-09-02'
api_count: 24
apis:
- description: Official Model Context Protocol server published by ControlUp as the npm package @controlup-ai/mcp. Runs locally over stdio via npx, authenticates with a ControlUp API key plus organization ID, and ex
  name: ControlUp MCP Server
  slug: controlup-mcp-server
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Alerts let you receive notifications or automatically run an action when certain conditions occur on a device.
  name: ControlUp Alerts API
  slug: controlup-alerts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Alerts - Devices API from ControlUp — 2 operation(s) for alerts - devices.
  name: ControlUp Alerts - Devices API
  slug: controlup-alerts-devices-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Applications usage reports
  name: ControlUp Applications API
  slug: controlup-applications-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Audit Log API from ControlUp — 1 operation(s) for audit log.
  name: ControlUp Audit Log API
  slug: controlup-audit-log-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Cloud providers API from ControlUp — 3 operation(s) for cloud providers.
  name: ControlUp Cloud providers API
  slug: controlup-cloud-providers-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The DAL (data access layer) is an advanced way to get data from an index.
  name: ControlUp Dal API
  slug: controlup-dal-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: These endpoints are for interacting with the raw data stored in data indices.
  name: ControlUp Data API
  slug: controlup-data-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Get information about devices.
  name: ControlUp Devices API
  slug: controlup-devices-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Dynamic SQL transformation and execution
  name: ControlUp Dynamic Query API API
  slug: controlup-dynamic-query-api-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The System Events log reports important events and alerts in your ControlUp for Desktops environment.
  name: ControlUp Events API
  slug: controlup-events-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Features API from ControlUp — 2 operation(s) for features.
  name: ControlUp Features API
  slug: controlup-features-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Health API from ControlUp — 3 operation(s) for health.
  name: ControlUp Health API
  slug: controlup-health-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Hives are the locations from which Scouts (tests) are initiated. Custom Hives allow you to test internal resources from within your network. They must be installed on a computer with access to your ne
  name: ControlUp Hives API
  slug: controlup-hives-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Host usage reports
  name: ControlUp Host API
  slug: controlup-host-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool cost API from ControlUp — 4 operation(s) for host pool cost.
  name: ControlUp Host pool cost API
  slug: controlup-host-pool-cost-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool deployments API from ControlUp — 1 operation(s) for host pool deployments.
  name: ControlUp Host pool deployments API
  slug: controlup-host-pool-deployments-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool scaling policies API from ControlUp — 2 operation(s) for host pool scaling policies.
  name: ControlUp Host pool scaling policies API
  slug: controlup-host-pool-scaling-policies-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool session host deployments API from ControlUp — 1 operation(s) for host pool session host deployments.
  name: ControlUp Host pool session host deployments API
  slug: controlup-host-pool-session-host-deployments-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool session hosts API from ControlUp — 1 operation(s) for host pool session hosts.
  name: ControlUp Host pool session hosts API
  slug: controlup-host-pool-session-hosts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool user sessions API from ControlUp — 1 operation(s) for host pool user sessions.
  name: ControlUp Host pool user sessions API
  slug: controlup-host-pool-user-sessions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pool VM settings API from ControlUp — 2 operation(s) for host pool vm settings.
  name: ControlUp Host pool VM settings API
  slug: controlup-host-pool-vm-settings-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Host pools API from ControlUp — 6 operation(s) for host pools.
  name: ControlUp Host pools API
  slug: controlup-host-pools-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Integrations API from ControlUp — 1 operation(s) for integrations.
  name: ControlUp Integrations API
  slug: controlup-integrations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Invitations API from ControlUp — 1 operation(s) for invitations.
  name: ControlUp Invitations API
  slug: controlup-invitations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The IP Allowlist API from ControlUp — 2 operation(s) for ip allowlist.
  name: ControlUp IP Allowlist API
  slug: controlup-ip-allowlist-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Jobs API from ControlUp — 8 operation(s) for jobs.
  name: ControlUp Jobs API
  slug: controlup-jobs-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The License API from ControlUp — 1 operation(s) for license.
  name: ControlUp License API
  slug: controlup-license-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The License Usage API from ControlUp — 1 operation(s) for license usage.
  name: ControlUp License Usage API
  slug: controlup-license-usage-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Machine usage reports
  name: ControlUp Machine API
  slug: controlup-machine-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Endpoints to manage and query machines
  name: ControlUp Machines API
  slug: controlup-machines-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Master images API from ControlUp — 20 operation(s) for master images.
  name: ControlUp Master images API
  slug: controlup-master-images-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Endpoints to manage and query metrics
  name: ControlUp Metrics API
  slug: controlup-metrics-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Multi-factor authentication (MFA) is supported for gateway access on all EUC platforms except Citrix Storefront. Use this resource to retrieve the sets of usernames and phone numbers that have been co
  name: ControlUp MF As API
  slug: controlup-mfas-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Netscaler usage reports
  name: ControlUp Net Scaler API
  slug: controlup-netscaler-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Onboarding API from ControlUp — 5 operation(s) for onboarding.
  name: ControlUp Onboarding API
  slug: controlup-onboarding-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Organization Settings API from ControlUp — 1 operation(s) for organization settings.
  name: ControlUp Organization Settings API
  slug: controlup-organization-settings-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Organizations API from ControlUp — 2 operation(s) for organizations.
  name: ControlUp Organizations API
  slug: controlup-organizations-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Overview API from ControlUp — 11 operation(s) for overview.
  name: ControlUp Overview API
  slug: controlup-overview-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Process usage reports
  name: ControlUp Processes API
  slug: controlup-processes-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Public API API from ControlUp — 11 operation(s) for public api.
  name: ControlUp Public API API
  slug: controlup-public-api-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Roles API from ControlUp — 2 operation(s) for roles.
  name: ControlUp Roles API
  slug: controlup-roles-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The SAML API from ControlUp — 2 operation(s) for saml.
  name: ControlUp SAML API
  slug: controlup-saml-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Scaling profiles API from ControlUp — 3 operation(s) for scaling profiles.
  name: ControlUp Scaling profiles API
  slug: controlup-scaling-profiles-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: 'Scouts are the proactive tests that you configure to monitor the availability and health of various resources. There are different types of Scouts, depending on the type of resource you want to test. '
  name: ControlUp Scouts API
  slug: controlup-scouts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Scripts API from ControlUp — 1 operation(s) for scripts.
  name: ControlUp Scripts API
  slug: controlup-scripts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Session statistics report
  name: ControlUp Session API
  slug: controlup-session-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Session hosts API from ControlUp — 2 operation(s) for session hosts.
  name: ControlUp Session hosts API
  slug: controlup-session-hosts-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The SSO Groups API from ControlUp — 2 operation(s) for sso groups.
  name: ControlUp SSO Groups API
  slug: controlup-sso-groups-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Subscriptions API from ControlUp — 27 operation(s) for subscriptions.
  name: ControlUp Subscriptions API
  slug: controlup-subscriptions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Provides an additional information about customer's data
  name: ControlUp Support endpoint API
  slug: controlup-support-endpoint-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: These endpoints are for interacting with Employee Sentiment surveys.
  name: ControlUp Surveys API
  slug: controlup-surveys-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Tags API from ControlUp — 2 operation(s) for tags.
  name: ControlUp Tags API
  slug: controlup-tags-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Tenants API from ControlUp — 23 operation(s) for tenants.
  name: ControlUp Tenants API
  slug: controlup-tenants-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The output of the scout tests
  name: ControlUp Tests API
  slug: controlup-tests-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Triggers API from ControlUp — 2 operation(s) for triggers.
  name: ControlUp Triggers API
  slug: controlup-triggers-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The TriggerSchedules API from ControlUp — 2 operation(s) for triggerschedules.
  name: ControlUp Trigger Schedules API
  slug: controlup-triggerschedules-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: User activity reports
  name: ControlUp User API
  slug: controlup-user-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The User sessions API from ControlUp — 1 operation(s) for user sessions.
  name: ControlUp User sessions API
  slug: controlup-user-sessions-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: The Users API from ControlUp — 4 operation(s) for users.
  name: ControlUp Users API
  slug: controlup-users-api
- baseURL: https://api.controlup.com/v1
  baseurl_source: declared
  description: Windows Event Log Monitoring history
  name: ControlUp Windows Events API
  slug: controlup-windowsevents-api
artifact_total: 129
asyncapis:
- description: ''
  name: Controlup Webhooks
  slug: controlup-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Controlup Alerts API
  slug: open-controlup-alerts-api
- collection_type: open
  name: Dex Alerts Alerts - Devices API
  slug: open-controlup-alerts-devices-api
- collection_type: open
  name: VDI & DAAS Applications API
  slug: open-controlup-applications-api
- collection_type: open
  name: Dex Audit Log API
  slug: open-controlup-audit-log-api
- collection_type: open
  name: DaaS IQ Cloud providers API
  slug: open-controlup-cloud-providers-api
- collection_type: open
  name: ControlUp for Desktops Dal API
  slug: open-controlup-dal-api
- collection_type: open
  name: ControlUp for Desktops Data API
  slug: open-controlup-data-api
- collection_type: open
  name: Controlup Devices API
  slug: open-controlup-devices-api
- collection_type: open
  name: VDI & DAAS Dynamic Query API API
  slug: open-controlup-dynamic-query-api-api
- collection_type: open
  name: Controlup Events API
  slug: open-controlup-events-api
- collection_type: open
  name: DaaS IQ Features API
  slug: open-controlup-features-api
- collection_type: open
  name: DaaS IQ Health API
  slug: open-controlup-health-api
- collection_type: open
  name: Synthetic Monitoring Hives API
  slug: open-controlup-hives-api
- collection_type: open
  name: VDI & DAAS Host API
  slug: open-controlup-host-api
- collection_type: open
  name: DaaS IQ Host pool cost API
  slug: open-controlup-host-pool-cost-api
- collection_type: open
  name: DaaS IQ Host pool deployments API
  slug: open-controlup-host-pool-deployments-api
- collection_type: open
  name: DaaS IQ Host pool scaling policies API
  slug: open-controlup-host-pool-scaling-policies-api
- collection_type: open
  name: DaaS IQ Host pool session host deployments API
  slug: open-controlup-host-pool-session-host-deployments-api
- collection_type: open
  name: DaaS IQ Host pool session hosts API
  slug: open-controlup-host-pool-session-hosts-api
- collection_type: open
  name: DaaS IQ Host pool user sessions API
  slug: open-controlup-host-pool-user-sessions-api
- collection_type: open
  name: DaaS IQ Host pool VM settings API
  slug: open-controlup-host-pool-vm-settings-api
- collection_type: open
  name: DaaS IQ Host pools API
  slug: open-controlup-host-pools-api
- collection_type: open
  name: Synthetic Monitoring Integrations API
  slug: open-controlup-integrations-api
- collection_type: open
  name: Dex Invitations API
  slug: open-controlup-invitations-api
- collection_type: open
  name: Dex IP Allowlist API
  slug: open-controlup-ip-allowlist-api
- collection_type: open
  name: DaaS IQ Jobs API
  slug: open-controlup-jobs-api
- collection_type: open
  name: DaaS IQ License API
  slug: open-controlup-license-api
- collection_type: open
  name: Dex License Usage API
  slug: open-controlup-license-usage-api
- collection_type: open
  name: VDI & DAAS Machine API
  slug: open-controlup-machine-api
- collection_type: open
  name: VDI & DaaS Configuration Machines API
  slug: open-controlup-machines-api
- collection_type: open
  name: DaaS IQ Master images API
  slug: open-controlup-master-images-api
- collection_type: open
  name: VDI & DaaS Realtime Metrics API
  slug: open-controlup-metrics-api
- collection_type: open
  name: Synthetic Monitoring MF As API
  slug: open-controlup-mfas-api
- collection_type: open
  name: VDI & DAAS Net Scaler API
  slug: open-controlup-netscaler-api
- collection_type: open
  name: DaaS IQ Onboarding API
  slug: open-controlup-onboarding-api
- collection_type: open
  name: Dex Organization Settings API
  slug: open-controlup-organization-settings-api
- collection_type: open
  name: Dex Organizations API
  slug: open-controlup-organizations-api
- collection_type: open
  name: DaaS IQ Overview API
  slug: open-controlup-overview-api
- collection_type: open
  name: VDI & DAAS Processes API
  slug: open-controlup-processes-api
- collection_type: open
  name: Flow3 Public Public API API
  slug: open-controlup-public-api-api
- collection_type: open
  name: Dex Roles API
  slug: open-controlup-roles-api
- collection_type: open
  name: Dex SAML API
  slug: open-controlup-saml-api
- collection_type: open
  name: DaaS IQ Scaling profiles API
  slug: open-controlup-scaling-profiles-api
- collection_type: open
  name: Synthetic Monitoring Scouts API
  slug: open-controlup-scouts-api
- collection_type: open
  name: ControlUp for Desktops Scripts API
  slug: open-controlup-scripts-api
- collection_type: open
  name: VDI & DAAS Session API
  slug: open-controlup-session-api
- collection_type: open
  name: DaaS IQ Session hosts API
  slug: open-controlup-session-hosts-api
- collection_type: open
  name: Dex SSO Groups API
  slug: open-controlup-sso-groups-api
- collection_type: open
  name: DaaS IQ Subscriptions API
  slug: open-controlup-subscriptions-api
- collection_type: open
  name: VDI & DAAS Support endpoint API
  slug: open-controlup-support-endpoint-api
- collection_type: open
  name: ControlUp for Desktops Surveys API
  slug: open-controlup-surveys-api
- collection_type: open
  name: Dex Tags API
  slug: open-controlup-tags-api
- collection_type: open
  name: DaaS IQ Tenants API
  slug: open-controlup-tenants-api
- collection_type: open
  name: Synthetic Monitoring Tests API
  slug: open-controlup-tests-api
- collection_type: open
  name: VDI & DaaS Configuration Triggers API
  slug: open-controlup-triggers-api
- collection_type: open
  name: VDI & DaaS Configuration Trigger Schedules API
  slug: open-controlup-triggerschedules-api
- collection_type: open
  name: VDI & DAAS User API
  slug: open-controlup-user-api
- collection_type: open
  name: DaaS IQ User sessions API
  slug: open-controlup-user-sessions-api
- collection_type: open
  name: Controlup Users API
  slug: open-controlup-users-api
- collection_type: open
  name: VDI & DAAS Windows Events API
  slug: open-controlup-windowsevents-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/controlup-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/controlup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/controlup-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.controlup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.controlup.io/
- group: docs
  title: ''
  type: Documentation
  url: https://support.controlup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.controlup.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.controlup.io/reference/how-to-make-api-requests-1
- group: operate
  title: ''
  type: Support
  url: https://support.controlup.com/
- group: company
  title: ''
  type: Blog
  url: https://www.controlup.com/resources/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/controlup
- group: operate
  title: ''
  type: Roadmap
  url: https://support.controlup.com/docs/submit-and-vote-on-feature-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://www.controlup.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.controlup.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://app.controlup.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.controlup.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.controlup.com/privacy-policy/controlup-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.controlup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.controlup.com/docs/release-notes
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trustcenter.controlup.com/
- group: auth
  title: ''
  type: Security
  url: https://trustcenter.controlup.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/controlup-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/controlup-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/controlup-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/controlup-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/controlup-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/controlup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/controlup-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/controlup-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/controlup-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/controlup-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/controlup-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/controlup-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/controlup-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.controlup.com/docs/controlup-product-version-lifecycle-quick-guide
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/controlup-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/controlup-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/controlup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/controlup-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/controlup-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-alerts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-dex-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-desktops-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-compliance-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-historical-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-realtime-metrics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-daas-configuration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-vdi-config-triggers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-daas-iq-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-synthetic-monitoring-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/controlup-workflows-overlay.yaml
created: '2026-08-04'
description: ControlUp is a Digital Employee Experience (DEX) and Autonomous Endpoint Management (AEM) platform that monitors, scores and remediates the end-user computing estate — physical desktops and laptops, VDI and DaaS (Citrix CVAD / Citrix Cloud, Omnissa Horizon, Azure Virtual Desktop, Windows 365, Parallels RAS), the applications and sessions running on them, and the network path in between. The ControlUp ONE platform spans ControlUp for Desktops, for VDI, for Apps, for Frontline Workers and for Compliance, plus Synthetic Monitoring (Scouts and Hives), Workflows, and Pulse AI. It publishes a public REST API surface at api.controlup.com documented on a ReadMe hub at api.controlup.io, an RFC 9727 /.well-known/api-catalog linkset enumerating twelve OpenAPI definitions, an official Model Context Protocol server on npm (@controlup-ai/mcp) exposing 106 tools across six product domains, PowerShell cmdlets for monitor and agent automation, and llms.txt indexes on both the documentation and
  API hosts.
image: https://www.controlup.com/wp-content/uploads/controlup_prev.webp
layout: provider
mcp_servers:
- description: ''
  name: ControlUp MCP Server
  slug: controlup-mcp-server
modified: '2026-08-04'
name: ControlUp
nav: Providers
network: true
overview: 'ControlUp publishes 60 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Alerts - Devices API, Applications API, and 57 more. Tagged areas include Digital Employee Experience, Endpoint Management, VDI, DaaS, and Virtual Desktop.


  The ControlUp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ControlUp''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 47 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 6
  name: Controlup Rate Limits
  slug: controlup-rate-limits
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 69.3
    developer_ergonomics: 58.9
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 97.4
  previous_composite: 62.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 60
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/controlup/refs/heads/main/screenshots/controlup-2026-08-07T163802.png
security:
- kind: authentication
  name: Controlup Authentication
  slug: controlup-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Controlup Domain Security
  slug: controlup-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Controlup Vulnerability Disclosure
  slug: controlup-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Controlup Trust Center
  slug: controlup-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701:2019, SOC 2 Type 2, SOC 3, FIPS 140-2 Level 1, CSA STAR Level 1, GDPR
slug: controlup
tags:
- Digital Employee Experience
- Endpoint Management
- VDI
- DaaS
- Virtual Desktop
- Observability
- Monitoring
- Synthetic Monitoring
- Device Management
- Compliance
- Vulnerability Management
- Workflow-Automation
- Citrix
- Azure Virtual Desktop
- MCP
- agent-native
website: https://www.controlup.com/
---
