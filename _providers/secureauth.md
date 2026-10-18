---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 546
  human_in_the_loop: 39
  name: Secureauth Agentic Access
  operation_count: 979
  slug: secureauth-agentic-access
  summary_line: 979 operations · 546 acting · 39 human-in-the-loop
api_count: 23
apis:
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The ACRs API from SecureAuth (incl. Cloudentity) — 2 operation(s) for acrs.
  name: SecureAuth (incl. Cloudentity) ACRs API
  slug: secureauth-acrs-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The apis API from SecureAuth (incl. Cloudentity) — 5 operation(s) for apis.
  name: SecureAuth (incl. Cloudentity) APIs API
  slug: secureauth-apis-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The applications API from SecureAuth (incl. Cloudentity) — 1 operation(s) for applications.
  name: SecureAuth (incl. Cloudentity) Applications API
  slug: secureauth-applications-api
- baseURL: https://localhost:8443/
  baseurl_source: spec
  description: The audit-events API from SecureAuth (incl. Cloudentity) — 1 operation(s) for audit-events.
  name: SecureAuth (incl. Cloudentity) Audit Events API
  slug: secureauth-audit-events-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The auditEvents API from SecureAuth (incl. Cloudentity) — 1 operation(s) for auditevents.
  name: SecureAuth (incl. Cloudentity) Audit Events API
  slug: secureauth-auditevents-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The authorizationDetails API from SecureAuth (incl. Cloudentity) — 3 operation(s) for authorizationdetails.
  name: SecureAuth (incl. Cloudentity) Authorization Details API
  slug: secureauth-authorizationdetails-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The B2BUsers API from SecureAuth (incl. Cloudentity) — 2 operation(s) for b2busers.
  name: SecureAuth (incl. Cloudentity) B2B Users API
  slug: secureauth-b2busers-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The bruteForceLimits API from SecureAuth (incl. Cloudentity) — 2 operation(s) for bruteforcelimits.
  name: SecureAuth (incl. Cloudentity) Brute Force Limits API
  slug: secureauth-bruteforcelimits-api
- baseURL: https://localhost:8443/
  baseurl_source: spec
  description: The captcha API from SecureAuth (incl. Cloudentity) — 2 operation(s) for captcha.
  name: SecureAuth (incl. Cloudentity) Captcha API
  slug: secureauth-captcha-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The CDR API from SecureAuth (incl. Cloudentity) — 3 operation(s) for cdr.
  name: SecureAuth (incl. Cloudentity) CDR API
  slug: secureauth-cdr-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The claims API from SecureAuth (incl. Cloudentity) — 3 operation(s) for claims.
  name: SecureAuth (incl. Cloudentity) Claims API
  slug: secureauth-claims-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The clients API from SecureAuth (incl. Cloudentity) — 16 operation(s) for clients.
  name: SecureAuth (incl. Cloudentity) Clients API
  slug: secureauth-clients-api
- baseURL: https://localhost:8443/api/identity/system
  baseurl_source: spec
  description: The configuration API from SecureAuth (incl. Cloudentity) — 3 operation(s) for configuration.
  name: SecureAuth (incl. Cloudentity) Configuration API
  slug: secureauth-configuration-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The CONSENT_PAGE API from SecureAuth (incl. Cloudentity) — 41 operation(s) for consent_page.
  name: SecureAuth (incl. Cloudentity) CONSENT PAGE API
  slug: secureauth-consent-page-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The consents API from SecureAuth (incl. Cloudentity) — 11 operation(s) for consents.
  name: SecureAuth (incl. Cloudentity) Consents API
  slug: secureauth-consents-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The customApps API from SecureAuth (incl. Cloudentity) — 2 operation(s) for customapps.
  name: SecureAuth (incl. Cloudentity) Custom Apps API
  slug: secureauth-customapps-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The DCR API from SecureAuth (incl. Cloudentity) — 7 operation(s) for dcr.
  name: SecureAuth (incl. Cloudentity) DCR API
  slug: secureauth-dcr-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The environment API from SecureAuth (incl. Cloudentity) — 2 operation(s) for environment.
  name: SecureAuth (incl. Cloudentity) Environment API
  slug: secureauth-environment-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The FDX API from SecureAuth (incl. Cloudentity) — 3 operation(s) for fdx.
  name: SecureAuth (incl. Cloudentity) FDX API
  slug: secureauth-fdx-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The features API from SecureAuth (incl. Cloudentity) — 4 operation(s) for features.
  name: SecureAuth (incl. Cloudentity) Features API
  slug: secureauth-features-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The gateways API from SecureAuth (incl. Cloudentity) — 9 operation(s) for gateways.
  name: SecureAuth (incl. Cloudentity) Gateways API
  slug: secureauth-gateways-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The Groups API from SecureAuth (incl. Cloudentity) — 12 operation(s) for groups.
  name: SecureAuth (incl. Cloudentity) Groups API
  slug: secureauth-groups-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The idps API from SecureAuth (incl. Cloudentity) — 89 operation(s) for idps.
  name: SecureAuth (incl. Cloudentity) Idps API
  slug: secureauth-idps-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The images API from SecureAuth (incl. Cloudentity) — 1 operation(s) for images.
  name: SecureAuth (incl. Cloudentity) Images API
  slug: secureauth-images-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The keys API from SecureAuth (incl. Cloudentity) — 5 operation(s) for keys.
  name: SecureAuth (incl. Cloudentity) Keys API
  slug: secureauth-keys-api
- baseURL: https://localhost:8443/api/licensing/default
  baseurl_source: spec
  description: The license API from SecureAuth (incl. Cloudentity) — 1 operation(s) for license.
  name: SecureAuth (incl. Cloudentity) License API
  slug: secureauth-license-api
- baseURL: https://localhost:8443/api/licensing
  baseurl_source: spec
  description: The licenses API from SecureAuth (incl. Cloudentity) — 3 operation(s) for licenses.
  name: SecureAuth (incl. Cloudentity) Licenses API
  slug: secureauth-licenses-api
- baseURL: https://localhost:8443/
  baseurl_source: spec
  description: The limits API from SecureAuth (incl. Cloudentity) — 2 operation(s) for limits.
  name: SecureAuth (incl. Cloudentity) Limits API
  slug: secureauth-limits-api
- baseURL: https://localhost:8443/api/system/default
  baseurl_source: spec
  description: The logins API from SecureAuth (incl. Cloudentity) — 6 operation(s) for logins.
  name: SecureAuth (incl. Cloudentity) Logins API
  slug: secureauth-logins-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The MANAGEMENT API from SecureAuth (incl. Cloudentity) — 12 operation(s) for management.
  name: SecureAuth (incl. Cloudentity) MANAGEMENT API
  slug: secureauth-management-api
- baseURL: https://localhost:8443/default/default/identity
  baseurl_source: spec
  description: The mfa API from SecureAuth (incl. Cloudentity) — 2 operation(s) for mfa.
  name: SecureAuth (incl. Cloudentity) Mfa API
  slug: secureauth-mfa-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The mfaMethods API from SecureAuth (incl. Cloudentity) — 3 operation(s) for mfamethods.
  name: SecureAuth (incl. Cloudentity) Mfa Methods API
  slug: secureauth-mfamethods-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The oauth2 API from SecureAuth (incl. Cloudentity) — 13 operation(s) for oauth2.
  name: SecureAuth (incl. Cloudentity) Oauth2 API
  slug: secureauth-oauth2-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The OBBR API from SecureAuth (incl. Cloudentity) — 26 operation(s) for obbr.
  name: SecureAuth (incl. Cloudentity) OBBR API
  slug: secureauth-obbr-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The OBUK API from SecureAuth (incl. Cloudentity) — 25 operation(s) for obuk.
  name: SecureAuth (incl. Cloudentity) OBUK API
  slug: secureauth-obuk-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The openbanking API from SecureAuth (incl. Cloudentity) — 1 operation(s) for openbanking.
  name: SecureAuth (incl. Cloudentity) Openbanking API
  slug: secureauth-openbanking-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The OPIN API from SecureAuth (incl. Cloudentity) — 2 operation(s) for opin.
  name: SecureAuth (incl. Cloudentity) OPIN API
  slug: secureauth-opin-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The organizations API from SecureAuth (incl. Cloudentity) — 4 operation(s) for organizations.
  name: SecureAuth (incl. Cloudentity) Organizations API
  slug: secureauth-organizations-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The OTP API from SecureAuth (incl. Cloudentity) — 9 operation(s) for otp.
  name: SecureAuth (incl. Cloudentity) OTP API
  slug: secureauth-otp-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The permissions API from SecureAuth (incl. Cloudentity) — 6 operation(s) for permissions.
  name: SecureAuth (incl. Cloudentity) Permissions API
  slug: secureauth-permissions-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The phoneProviderConfig API from SecureAuth (incl. Cloudentity) — 1 operation(s) for phoneproviderconfig.
  name: SecureAuth (incl. Cloudentity) Phone Provider Config API
  slug: secureauth-phoneproviderconfig-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The policies API from SecureAuth (incl. Cloudentity) — 5 operation(s) for policies.
  name: SecureAuth (incl. Cloudentity) Policies API
  slug: secureauth-policies-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The PoolMetrics API from SecureAuth (incl. Cloudentity) — 1 operation(s) for poolmetrics.
  name: SecureAuth (incl. Cloudentity) Pool Metrics API
  slug: secureauth-poolmetrics-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The Pools API from SecureAuth (incl. Cloudentity) — 8 operation(s) for pools.
  name: SecureAuth (incl. Cloudentity) Pools API
  slug: secureauth-pools-api
- baseURL: https://localhost:8443/api/system/default
  baseurl_source: spec
  description: The post-authn API from SecureAuth (incl. Cloudentity) — 3 operation(s) for post-authn.
  name: SecureAuth (incl. Cloudentity) Post Authn API
  slug: secureauth-post-authn-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The recentActivities API from SecureAuth (incl. Cloudentity) — 1 operation(s) for recentactivities.
  name: SecureAuth (incl. Cloudentity) Recent Activities API
  slug: secureauth-recentactivities-api
- baseURL: https://localhost:8443/api/system/default
  baseurl_source: spec
  description: The recovery API from SecureAuth (incl. Cloudentity) — 3 operation(s) for recovery.
  name: SecureAuth (incl. Cloudentity) Recovery API
  slug: secureauth-recovery-api
- baseURL: https://localhost:8443/api/permissions/default
  baseurl_source: spec
  description: The Relationships API from SecureAuth (incl. Cloudentity) — 1 operation(s) for relationships.
  name: SecureAuth (incl. Cloudentity) Relationships API
  slug: secureauth-relationships-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The roles API from SecureAuth (incl. Cloudentity) — 10 operation(s) for roles.
  name: SecureAuth (incl. Cloudentity) Roles API
  slug: secureauth-roles-api
- baseURL: https://localhost:8443/api/hub
  baseurl_source: spec
  description: The RootConfiguration API from SecureAuth (incl. Cloudentity) — 3 operation(s) for rootconfiguration.
  name: SecureAuth (incl. Cloudentity) Root Configuration API
  slug: secureauth-rootconfiguration-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The saml API from SecureAuth (incl. Cloudentity) — 5 operation(s) for saml.
  name: SecureAuth (incl. Cloudentity) SAML API
  slug: secureauth-saml-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The Schemas API from SecureAuth (incl. Cloudentity) — 6 operation(s) for schemas.
  name: SecureAuth (incl. Cloudentity) Schemas API
  slug: secureauth-schemas-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The SCIMv2Configuration API from SecureAuth (incl. Cloudentity) — 5 operation(s) for scimv2configuration.
  name: SecureAuth (incl. Cloudentity) SCI Mv2 Configuration API
  slug: secureauth-scimv2configuration-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The SCIMv2Groups API from SecureAuth (incl. Cloudentity) — 2 operation(s) for scimv2groups.
  name: SecureAuth (incl. Cloudentity) SCI Mv2 Groups API
  slug: secureauth-scimv2groups-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The SCIMv2Users API from SecureAuth (incl. Cloudentity) — 2 operation(s) for scimv2users.
  name: SecureAuth (incl. Cloudentity) SCI Mv2 Users API
  slug: secureauth-scimv2users-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The scopes API from SecureAuth (incl. Cloudentity) — 4 operation(s) for scopes.
  name: SecureAuth (incl. Cloudentity) Scopes API
  slug: secureauth-scopes-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The scripts API from SecureAuth (incl. Cloudentity) — 6 operation(s) for scripts.
  name: SecureAuth (incl. Cloudentity) Scripts API
  slug: secureauth-scripts-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The secrets API from SecureAuth (incl. Cloudentity) — 2 operation(s) for secrets.
  name: SecureAuth (incl. Cloudentity) Secrets API
  slug: secureauth-secrets-api
- baseURL: https://localhost:8443/
  baseurl_source: spec
  description: The security API from SecureAuth (incl. Cloudentity) — 2 operation(s) for security.
  name: SecureAuth (incl. Cloudentity) Security API
  slug: secureauth-security-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The servers API from SecureAuth (incl. Cloudentity) — 13 operation(s) for servers.
  name: SecureAuth (incl. Cloudentity) Servers API
  slug: secureauth-servers-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The services API from SecureAuth (incl. Cloudentity) — 7 operation(s) for services.
  name: SecureAuth (incl. Cloudentity) Services API
  slug: secureauth-services-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The sessions API from SecureAuth (incl. Cloudentity) — 2 operation(s) for sessions.
  name: SecureAuth (incl. Cloudentity) Sessions API
  slug: secureauth-sessions-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The system API from SecureAuth (incl. Cloudentity) — 9 operation(s) for system.
  name: SecureAuth (incl. Cloudentity) System API
  slug: secureauth-system-api
- baseURL: https://localhost:8443/api/permissions/default
  baseurl_source: spec
  description: The Systems API from SecureAuth (incl. Cloudentity) — 2 operation(s) for systems.
  name: SecureAuth (incl. Cloudentity) Systems API
  slug: secureauth-systems-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The SystemTenantMetrics API from SecureAuth (incl. Cloudentity) — 9 operation(s) for systemtenantmetrics.
  name: SecureAuth (incl. Cloudentity) System Tenant Metrics API
  slug: secureauth-systemtenantmetrics-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The SystemWorkspaceMetrics API from SecureAuth (incl. Cloudentity) — 2 operation(s) for systemworkspacemetrics.
  name: SecureAuth (incl. Cloudentity) System Workspace Metrics API
  slug: secureauth-systemworkspacemetrics-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The templates API from SecureAuth (incl. Cloudentity) — 5 operation(s) for templates.
  name: SecureAuth (incl. Cloudentity) Templates API
  slug: secureauth-templates-api
- baseURL: https://localhost:8443/api/hub
  baseurl_source: spec
  description: The TenantConfiguration API from SecureAuth (incl. Cloudentity) — 3 operation(s) for tenantconfiguration.
  name: SecureAuth (incl. Cloudentity) Tenant Configuration API
  slug: secureauth-tenantconfiguration-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The TenantMetrics API from SecureAuth (incl. Cloudentity) — 15 operation(s) for tenantmetrics.
  name: SecureAuth (incl. Cloudentity) Tenant Metrics API
  slug: secureauth-tenantmetrics-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The tenants API from SecureAuth (incl. Cloudentity) — 9 operation(s) for tenants.
  name: SecureAuth (incl. Cloudentity) Tenants API
  slug: secureauth-tenants-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The themes API from SecureAuth (incl. Cloudentity) — 3 operation(s) for themes.
  name: SecureAuth (incl. Cloudentity) Themes API
  slug: secureauth-themes-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The tokens API from SecureAuth (incl. Cloudentity) — 5 operation(s) for tokens.
  name: SecureAuth (incl. Cloudentity) Tokens API
  slug: secureauth-tokens-api
- baseURL: https://localhost:8443/default/default
  baseurl_source: spec
  description: The transientOtp API from SecureAuth (incl. Cloudentity) — 2 operation(s) for transientotp.
  name: SecureAuth (incl. Cloudentity) Transient Otp API
  slug: secureauth-transientotp-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The translations API from SecureAuth (incl. Cloudentity) — 2 operation(s) for translations.
  name: SecureAuth (incl. Cloudentity) Translations API
  slug: secureauth-translations-api
- baseURL: https://localhost:8443/api/licensing/default
  baseurl_source: spec
  description: The usage API from SecureAuth (incl. Cloudentity) — 2 operation(s) for usage.
  name: SecureAuth (incl. Cloudentity) Usage API
  slug: secureauth-usage-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The UserMetrics API from SecureAuth (incl. Cloudentity) — 4 operation(s) for usermetrics.
  name: SecureAuth (incl. Cloudentity) User Metrics API
  slug: secureauth-usermetrics-api
- baseURL: https://localhost:8443/api/identity/default
  baseurl_source: spec
  description: The Users API from SecureAuth (incl. Cloudentity) — 68 operation(s) for users.
  name: SecureAuth (incl. Cloudentity) Users API
  slug: secureauth-users-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The vanityDomains API from SecureAuth (incl. Cloudentity) — 1 operation(s) for vanitydomains.
  name: SecureAuth (incl. Cloudentity) Vanity Domains API
  slug: secureauth-vanitydomains-api
- description: The web API from SecureAuth (incl. Cloudentity) — 2 operation(s) for web.
  name: SecureAuth (incl. Cloudentity) Web API
  slug: secureauth-web-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The webhooks API from SecureAuth (incl. Cloudentity) — 3 operation(s) for webhooks.
  name: SecureAuth (incl. Cloudentity) Webhooks API
  slug: secureauth-webhooks-api
- baseURL: https://localhost:8443/
  baseurl_source: spec
  description: The workforce API from SecureAuth (incl. Cloudentity) — 1 operation(s) for workforce.
  name: SecureAuth (incl. Cloudentity) Workforce API
  slug: secureauth-workforce-api
- baseURL: https://localhost:8443/api/hub
  baseurl_source: spec
  description: The WorkspaceConfiguration API from SecureAuth (incl. Cloudentity) — 4 operation(s) for workspaceconfiguration.
  name: SecureAuth (incl. Cloudentity) Workspace Configuration API
  slug: secureauth-workspaceconfiguration-api
- baseURL: https://localhost:8443/api/analytics/default
  baseurl_source: spec
  description: The WorkspaceMetrics API from SecureAuth (incl. Cloudentity) — 20 operation(s) for workspacemetrics.
  name: SecureAuth (incl. Cloudentity) Workspace Metrics API
  slug: secureauth-workspacemetrics-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The workspaces API from SecureAuth (incl. Cloudentity) — 5 operation(s) for workspaces.
  name: SecureAuth (incl. Cloudentity) Workspaces API
  slug: secureauth-workspaces-api
- baseURL: https://localhost:8443/api/admin/default
  baseurl_source: spec
  description: The API Keys API from SecureAuth (incl. Cloudentity) — 2 operation(s) for api keys.
  name: SecureAuth (incl. Cloudentity) API Keys API
  slug: secureauth-api-keys-api
artifact_total: 90
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/capabilities/secureauth-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/secureauth-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/agentic-access/secureauth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/secureauth-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/rules/secureauth-rules.yml
  title: ''
  type: Spectral
  url: rules/secureauth-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/data-model/secureauth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/secureauth-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/conventions/secureauth-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/secureauth-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/conventions/secureauth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/secureauth-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/errors/secureauth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secureauth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/conformance/secureauth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/secureauth-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/llms/secureauth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secureauth-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/well-known/secureauth-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/secureauth-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/well-known/secureauth-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/secureauth-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/hosts/secureauth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secureauth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/vendors/secureauth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/secureauth-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secureauth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secureauth.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://secureauth.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://secureauth.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://secureauth.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/scopes/secureauth-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/secureauth-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/authentication/secureauth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secureauth-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/secureauth/refs/heads/main/security/secureauth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secureauth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secureauth.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.secureauth.com/home/index.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secureauth.com
- group: operate
  title: ''
  type: Support
  url: https://support.secureauth.com
- group: company
  title: ''
  type: Blog
  url: https://secureauth.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SecureAuthCorp
- group: build
  title: ''
  type: SDK
  url: https://github.com/SecureAuthCorp/ciam-client-go
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://status.secureauth.com/mcp
  - status: 200
    url: https://secureauth.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: SecureAuth is an identity and access management company. It acquired Cloudentity; cloudentity.com now redirects to secureauth.com and the former Cloudentity Authorization Control Plane ships as SecureAuth CIAM, whose 23 OpenAPI definitions (979 operations) are published in the SecureAuthCorp/ciam-client-go repository.
image: https://secureauth.com/og-image.png
layout: provider
modified: '2026-10-13'
name: SecureAuth (incl. Cloudentity)
nav: Providers
network: true
overview: 'SecureAuth (incl. Cloudentity) publishes 85 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACRs API, APIs API, Applications API, and 82 more. Tagged areas include Company, Identity, Authentication, Authorization, and Open Banking.


  The SecureAuth (incl. Cloudentity) catalog on APIs.io includes 1 Spectral governance ruleset.


  SecureAuth (incl. Cloudentity)''s developer surface includes pricing, authentication, documentation, support, engineering blog, SDKs, and 22 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: SecureAuth (incl. Cloudentity) API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 7
  slug: secureauth-rules
scopes:
- name: Secureauth Scopes
  scope_count: 44
  slug: secureauth-scopes
  summary_line: 44 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 45.8
    developer_ergonomics: 35.7
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 85
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 61.1
security:
- kind: authentication
  name: Secureauth Authentication
  slug: secureauth-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Secureauth Domain Security
  slug: secureauth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: secureauth
tags:
- Company
- Identity
- Authentication
- Authorization
- Open Banking
website: https://secureauth.com
---
