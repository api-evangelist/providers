---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 151
  human_in_the_loop: 7
  name: Gluu Agentic Access
  operation_count: 328
  slug: gluu-agentic-access
  summary_line: 328 operations · 151 acting · 7 human-in-the-loop
api_count: 12
apis:
- description: Gluu Flex is the commercial, self-hosted enterprise distribution of the Linux Foundation Janssen Project. It provides a cloud-native digital identity platform with OAuth 2.0, OpenID Connect, FIDO, SCI
  name: Gluu Flex
  slug: gluu-flex
- description: Gluu Solo is Gluu's hosted, serverless SaaS identity provider, running the Janssen stack on Google Cloud with customer-selected geographic locations, published per-location monthly and annual pricing,
  name: Gluu Solo
  slug: gluu-solo
- description: 'The Janssen Project is the upstream Linux Foundation open-source identity platform that powers Gluu Flex. It implements OAuth 2.0, OpenID Connect, FIDO 2.0, SCIM, UMA, and CIBA, providing a federated '
  name: Janssen Project
  slug: janssen-project
- description: Cedarling is an embeddable Policy Decision Point (PDP) built in Rust that runs anywhere and returns authorization decisions in under 50 microseconds based on declarative Cedar access policies. It vali
  name: Cedarling
  slug: cedarling
- description: Agama Lab is a developer portal for authoring Cedar schema and policies, building authentication workflows using the Agama domain specific language, and managing hosted Gluu infrastructure.
  name: Agama Lab
  slug: agama-lab
- baseURL: https://{host}
  baseurl_source: declared
  description: The Access Evaluation API from Gluu — 1 operation(s) for access evaluation.
  name: Gluu Access Evaluation API
  slug: gluu-access-evaluation-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Cedarling API from Gluu — 3 operation(s) for admin ui - cedarling.
  name: Gluu Admin UI - Cedarling API
  slug: gluu-admin-ui-cedarling-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Configuration API from Gluu — 1 operation(s) for admin ui - configuration.
  name: Gluu Admin UI - Configuration API
  slug: gluu-admin-ui-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - License API from Gluu — 8 operation(s) for admin ui - license.
  name: Gluu Admin UI - License API
  slug: gluu-admin-ui-license-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Permission API from Gluu — 2 operation(s) for admin ui - permission.
  name: Gluu Admin UI - Permission API
  slug: gluu-admin-ui-permission-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Role API from Gluu — 2 operation(s) for admin ui - role.
  name: Gluu Admin UI - Role API
  slug: gluu-admin-ui-role-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Role-Permissions Mapping API from Gluu — 2 operation(s) for admin ui - role-permissions mapping.
  name: Gluu Admin UI - Role-Permissions Mapping API
  slug: gluu-admin-ui-role-permissions-mapping-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Admin UI - Webhooks API from Gluu — 6 operation(s) for admin ui - webhooks.
  name: Gluu Admin UI - Webhooks API
  slug: gluu-admin-ui-webhooks-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Agama API from Gluu — 5 operation(s) for agama.
  name: Gluu Agama API
  slug: gluu-agama-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Agama - Configuration API from Gluu — 1 operation(s) for agama - configuration.
  name: Gluu Agama - Configuration API
  slug: gluu-agama-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Archived JWK - Archived JSON Web Key (JWK) API from Gluu — 1 operation(s) for archived jwk - archived json web key (jwk).
  name: Gluu Archived JWK - Archived JSON Web Key (JWK) API
  slug: gluu-archived-jwk-archived-json-web-key-jwk-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Attribute API from Gluu — 2 operation(s) for attribute.
  name: Gluu Attribute API
  slug: gluu-attribute-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Auth Server Health - Check API from Gluu — 1 operation(s) for auth server health - check.
  name: Gluu Auth Server Health - Check API
  slug: gluu-auth-server-health-check-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Auth - Session Management API from Gluu — 4 operation(s) for auth - session management.
  name: Gluu Auth - Session Management API
  slug: gluu-auth-session-management-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Authorization API from Gluu — 3 operation(s) for authorization.
  name: Gluu Authorization API
  slug: gluu-authorization-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Authorization Challenge API from Gluu — 1 operation(s) for authorization challenge.
  name: Gluu Authorization Challenge API
  slug: gluu-authorization-challenge-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The AuthZEN Access Evaluation Discovery API from Gluu — 1 operation(s) for authzen access evaluation discovery.
  name: Gluu AuthZEN Access Evaluation Discovery API
  slug: gluu-authzen-access-evaluation-discovery-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Bulk API from Gluu — 1 operation(s) for bulk.
  name: Gluu Bulk API
  slug: gluu-bulk-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Cache Configuration API from Gluu — 1 operation(s) for cache configuration.
  name: Gluu Cache Configuration API
  slug: gluu-cache-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Cache Configuration – in-Memory API from Gluu — 1 operation(s) for cache configuration – in-memory.
  name: Gluu Cache Configuration – in-Memory API
  slug: gluu-cache-configuration-in-memory-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Cache Configuration – Memcached API from Gluu — 1 operation(s) for cache configuration – memcached.
  name: Gluu Cache Configuration – Memcached API
  slug: gluu-cache-configuration-memcached-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Cache Configuration – Native-Persistence API from Gluu — 1 operation(s) for cache configuration – native-persistence.
  name: Gluu Cache Configuration – Native-Persistence API
  slug: gluu-cache-configuration-native-persistence-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Cache Configuration – Redis API from Gluu — 1 operation(s) for cache configuration – redis.
  name: Gluu Cache Configuration – Redis API
  slug: gluu-cache-configuration-redis-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Client Authorization API from Gluu — 2 operation(s) for client authorization.
  name: Gluu Client Authorization API
  slug: gluu-client-authorization-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Client Info API from Gluu — 1 operation(s) for client info.
  name: Gluu Client Info API
  slug: gluu-client-info-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Client Registration API from Gluu — 1 operation(s) for client registration.
  name: Gluu Client Registration API
  slug: gluu-client-registration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – Config API API from Gluu — 1 operation(s) for configuration – config api.
  name: Gluu Configuration – Config API
  slug: gluu-configuration-config-api-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – JWK - JSON Web Key (JWK) API from Gluu — 3 operation(s) for configuration – jwk - json web key (jwk).
  name: Gluu Configuration – JWK - JSON Web Key (JWK) API
  slug: gluu-configuration-jwk-json-web-key-jwk-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – Logging API from Gluu — 1 operation(s) for configuration – logging.
  name: Gluu Configuration – Logging API
  slug: gluu-configuration-logging-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – Properties API from Gluu — 3 operation(s) for configuration – properties.
  name: Gluu Configuration – Properties API
  slug: gluu-configuration-properties-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – SMTP API from Gluu — 2 operation(s) for configuration – smtp.
  name: Gluu Configuration – SMTP API
  slug: gluu-configuration-smtp-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Configuration – User Management API from Gluu — 2 operation(s) for configuration – user management.
  name: Gluu Configuration – User Management API
  slug: gluu-configuration-user-management-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Custom Scripts API from Gluu — 7 operation(s) for custom scripts.
  name: Gluu Custom Scripts API
  slug: gluu-custom-scripts-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Database API from Gluu — 1 operation(s) for database.
  name: Gluu Database API
  slug: gluu-database-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Database - LDAP configuration API from Gluu — 3 operation(s) for database - ldap configuration.
  name: Gluu Database - LDAP configuration API
  slug: gluu-database-ldap-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Default Authentication Method API from Gluu — 1 operation(s) for default authentication method.
  name: Gluu Default Authentication Method API
  slug: gluu-default-authentication-method-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints to facilitate discovery of SCIM service provider features
  name: Gluu Discovery API
  slug: gluu-discovery-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The FIDO2 Assertion API from Gluu — 2 operation(s) for fido2 assertion.
  name: Gluu FIDO2 Assertion API
  slug: gluu-fido2-assertion-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The FIDO2 Attestation API from Gluu — 2 operation(s) for fido2 attestation.
  name: Gluu FIDO2 Attestation API
  slug: gluu-fido2-attestation-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Fido2 - Configuration API from Gluu — 2 operation(s) for fido2 - configuration.
  name: Gluu Fido2 - Configuration API
  slug: gluu-fido2-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for management of Fido2 devices
  name: Gluu fido2 devices API
  slug: gluu-fido2-devices-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Fido2 - Metrics API from Gluu — 28 operation(s) for fido2 - metrics.
  name: Gluu Fido2 - Metrics API
  slug: gluu-fido2-metrics-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Fido2 - Registration API from Gluu — 3 operation(s) for fido2 - registration.
  name: Gluu Fido2 - Registration API
  slug: gluu-fido2-registration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Fido2 - Trust API from Gluu — 4 operation(s) for fido2 - trust.
  name: Gluu Fido2 - Trust API
  slug: gluu-fido2-trust-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Search from service root
  name: Gluu global search API
  slug: gluu-global-search-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Global Token Revocation API from Gluu — 1 operation(s) for global token revocation.
  name: Gluu Global Token Revocation API
  slug: gluu-global-token-revocation-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for management of Group resources
  name: Gluu Group API
  slug: gluu-group-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Health - Check API from Gluu — 6 operation(s) for health - check.
  name: Gluu Health - Check API
  slug: gluu-health-check-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Internal Statistic API from Gluu — 1 operation(s) for internal statistic.
  name: Gluu Internal Statistic API
  slug: gluu-internal-statistic-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Jans Assets API from Gluu — 8 operation(s) for jans assets.
  name: Gluu Jans Assets API
  slug: gluu-jans-assets-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Jans Link - Configuration API from Gluu — 1 operation(s) for jans link - configuration.
  name: Gluu Jans Link - Configuration API
  slug: gluu-jans-link-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The JWK - JSON Web Key Set (JWKs) API from Gluu — 1 operation(s) for jwk - json web key set (jwks).
  name: Gluu JWK - JSON Web Key Set (JWKs) API
  slug: gluu-jwk-json-web-key-set-jwks-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Audit API from Gluu — 8 operation(s) for lock - audit.
  name: Gluu Lock - Audit API
  slug: gluu-lock-audit-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Audit Health API from Gluu — 2 operation(s) for lock - audit health.
  name: Gluu Lock - Audit Health API
  slug: gluu-lock-audit-health-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Audit Log API from Gluu — 2 operation(s) for lock - audit log.
  name: Gluu Lock - Audit Log API
  slug: gluu-lock-audit-log-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Audit Telemetry API from Gluu — 2 operation(s) for lock - audit telemetry.
  name: Gluu Lock - Audit Telemetry API
  slug: gluu-lock-audit-telemetry-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Configuration API from Gluu — 1 operation(s) for lock - configuration.
  name: Gluu Lock - Configuration API
  slug: gluu-lock-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Log API from Gluu — 1 operation(s) for lock - log.
  name: Gluu Lock - Log API
  slug: gluu-lock-log-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Policy API from Gluu — 2 operation(s) for lock - policy.
  name: Gluu Lock - Policy API
  slug: gluu-lock-policy-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Server Configuration API from Gluu — 2 operation(s) for lock - server configuration.
  name: Gluu Lock - Server Configuration API
  slug: gluu-lock-server-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Lock - Stat API from Gluu — 1 operation(s) for lock - stat.
  name: Gluu Lock - Stat API
  slug: gluu-lock-stat-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Logs API from Gluu — 1 operation(s) for logs.
  name: Gluu Logs API
  slug: gluu-logs-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Message Configuration API from Gluu — 1 operation(s) for message configuration.
  name: Gluu Message Configuration API
  slug: gluu-message-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Message Configuration – Postgres API from Gluu — 1 operation(s) for message configuration – postgres.
  name: Gluu Message Configuration – Postgres API
  slug: gluu-message-configuration-postgres-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Message Configuration – Redis API from Gluu — 1 operation(s) for message configuration – redis.
  name: Gluu Message Configuration – Redis API
  slug: gluu-message-configuration-redis-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Metric API from Gluu — 4 operation(s) for metric.
  name: Gluu Metric API
  slug: gluu-metric-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The OAuth - OpenID Connect - Clients API from Gluu — 2 operation(s) for oauth - openid connect - clients.
  name: Gluu OAuth - OpenID Connect - Clients API
  slug: gluu-oauth-openid-connect-clients-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The OAuth - Scopes API from Gluu — 4 operation(s) for oauth - scopes.
  name: Gluu OAuth - Scopes API
  slug: gluu-oauth-scopes-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The OAuth - UMA Resources API from Gluu — 3 operation(s) for oauth - uma resources.
  name: Gluu OAuth - UMA Resources API
  slug: gluu-oauth-uma-resources-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Organization Configuration API from Gluu — 1 operation(s) for organization configuration.
  name: Gluu Organization Configuration API
  slug: gluu-organization-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Plugins API from Gluu — 2 operation(s) for plugins.
  name: Gluu Plugins API
  slug: gluu-plugins-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Registration API from Gluu — 2 operation(s) for registration.
  name: Gluu Registration API
  slug: gluu-registration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The SCIM - Config Management API from Gluu — 1 operation(s) for scim - config management.
  name: Gluu SCIM - Config Management API
  slug: gluu-scim-config-management-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Server Configuration API from Gluu — 1 operation(s) for server configuration.
  name: Gluu Server Configuration API
  slug: gluu-server-configuration-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Session Management API from Gluu — 2 operation(s) for session management.
  name: Gluu Session Management API
  slug: gluu-session-management-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Software Statement Assertion (SSA) API from Gluu — 1 operation(s) for software statement assertion (ssa).
  name: Gluu Software Statement Assertion (SSA) API
  slug: gluu-software-statement-assertion-ssa-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The SSA API from Gluu — 3 operation(s) for ssa.
  name: Gluu SSA API
  slug: gluu-ssa-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Statistics API from Gluu — 1 operation(s) for statistics.
  name: Gluu Statistics API
  slug: gluu-statistics-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Statistics - User API from Gluu — 1 operation(s) for statistics - user.
  name: Gluu Statistics - User API
  slug: gluu-statistics-user-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Status List Aggregation API from Gluu — 1 operation(s) for status list aggregation.
  name: Gluu Status List Aggregation API
  slug: gluu-status-list-aggregation-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Status List API from Gluu — 1 operation(s) for status list.
  name: Gluu Status List API
  slug: gluu-status-list-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Token API from Gluu — 7 operation(s) for token.
  name: Gluu Token API
  slug: gluu-token-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The Token Introspection API from Gluu — 1 operation(s) for token introspection.
  name: Gluu Token Introspection API
  slug: gluu-token-introspection-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The UMA 2 Resource API from Gluu — 3 operation(s) for uma 2 resource.
  name: Gluu UMA 2 Resource API
  slug: gluu-uma-2-resource-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The UMA Scope API from Gluu — 1 operation(s) for uma scope.
  name: Gluu UMA Scope API
  slug: gluu-uma-scope-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The UMA (User Managed Access) API from Gluu — 3 operation(s) for uma (user managed access).
  name: Gluu UMA (User Managed Access) API
  slug: gluu-uma-user-managed-access-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for management of User resources
  name: Gluu User API
  slug: gluu-user-api
- baseURL: https://{host}
  baseurl_source: declared
  description: The User Info API from Gluu — 1 operation(s) for user info.
  name: Gluu User Info API
  slug: gluu-user-info-api
artifact_total: 109
asyncapis:
- description: ''
  name: Gluu Webhooks
  slug: gluu-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/gluu/finops/gluu-finops.yml
  title: ''
  type: FinOps
  url: finops/gluu-finops.yml
- group: other
  href: https://artifacts.apis.io/gluu/capabilities/gluu-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gluu-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/gluu/overlays/gluu-jans-auth-server-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gluu-jans-auth-server-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gluu/overlays/gluu-jans-config-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gluu-jans-config-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/gluu/overlays/gluu-jans-scim-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gluu-jans-scim-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://gluu.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jans.io/stable/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gluu.org/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jans.io/stable/janssen-server/reference/openapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gluu.org/stable/install/
- group: company
  title: ''
  type: Blog
  url: https://gluu.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.gluu.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GluuFederation
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/GluuFederation/flex/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/GluuFederation/flex/releases
- group: operate
  href: https://artifacts.apis.io/gluu/changelog/gluu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gluu-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://gluu.org/gluu-flex-roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://gluu.org/solo/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.gluu.org/agama-lab
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gluu.org/gluu-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gluu.org/gluu-privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://gluu.org/security/
- group: operate
  title: ''
  type: Contact
  url: https://gluu.org/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gluufederation
- group: agent
  href: https://artifacts.apis.io/gluu/agentic-access/gluu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gluu-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gluu/authentication/gluu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gluu-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gluu/scopes/gluu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gluu-scopes.yml
- group: design
  href: https://artifacts.apis.io/gluu/conventions/gluu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gluu-conventions.yml
- group: design
  href: https://artifacts.apis.io/gluu/errors/gluu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gluu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gluu/conformance/gluu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gluu-conformance.yml
- group: design
  href: https://artifacts.apis.io/gluu/lifecycle/gluu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gluu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gluu/data-model/gluu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gluu-data-model.yml
- group: build
  href: https://artifacts.apis.io/gluu/packages/gluu-packages.yml
  title: ''
  type: Packages
  url: packages/gluu-packages.yml
- group: build
  href: https://artifacts.apis.io/gluu/packages/gluu-packages.yml
  title: ''
  type: SDKs
  url: packages/gluu-packages.yml
- group: build
  href: https://artifacts.apis.io/gluu/cli/gluu-cli.yml
  title: ''
  type: CLI
  url: cli/gluu-cli.yml
- group: start
  href: https://artifacts.apis.io/gluu/sandbox/gluu-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gluu-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/gluu/mcp/gluu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gluu-mcp.yml
- group: build
  href: https://artifacts.apis.io/gluu/mcp/gluu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gluu-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/gluu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/gluu/llms/gluu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gluu-llms.txt
- group: other
  href: https://artifacts.apis.io/gluu/grpc/gluu-jans-lock-audit.proto
  title: ''
  type: Protobuf
  url: grpc/gluu-jans-lock-audit.proto
- group: design
  href: https://artifacts.apis.io/gluu/asyncapi/gluu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gluu-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/gluu/rate-limits/gluu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gluu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gluu/plans/gluu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gluu-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/gluu/security/gluu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gluu-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gluu/security/gluu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gluu-vulnerability-disclosure.yml
created: '2025-08-14'
description: Gluu is a technology company that specializes in providing identity and access management solutions for businesses. Their platform allows organizations to centrally manage the authentication and authorization of users across various applications and systems, ensuring secure access to sensitive data and resources. Gluu leads the Linux Foundation Janssen Project, whose OAuth 2.0 / OpenID Connect authorization server, SCIM 2.0 service, FIDO2 server, Config API and Cedarling policy decision point are the components Gluu packages commercially as Gluu Flex and hosts as Gluu Solo.
finops:
- has_sources: true
  method: derived
  name: Gluu Finops
  primary_unit: location
  service_category: ''
  slug: gluu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gluu.png
layout: provider
mcp_servers:
- description: 'The Janssen Project ships one real MCP server: the Janssen Tarp MCP server, which lets an AI assistant inside the Tarp browser extension register an OIDC client and drive an authorization-code flow ag'
  name: Gluu MCP Server
  slug: jans-tarp-mcp-server
modified: '2026-09-16'
name: Gluu
nav: Providers
network: true
overview: 'Gluu publishes 93 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Evaluation API, Admin UI - Cedarling API, Admin UI - Configuration API, and 90 more. Tagged areas include Identity and Access Management, Authentication, Authorization, Cedar, and FIDO2.


  The Gluu catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gluu''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, pricing, and 39 more developer resources.'
plans:
- name: Gluu Plans Pricing
  plan_count: 6
  slug: gluu-plans-pricing
- name: Gluu Price Estimates
  plan_count: 0
  slug: gluu-price-estimates
random_paper: 13
rate_limits:
- limit_count: 0
  name: Gluu Rate Limits
  slug: gluu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Gluu API Rules
  rule_count: 59
  severity_counts:
    error: 37
    hint: 0
    info: 4
    warn: 18
  slug: gluu-rules
scopes:
- name: Gluu Scopes
  scope_count: 162
  slug: gluu-scopes
  summary_line: 162 scopes · clientCredentials
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 55.4
    developer_ergonomics: 80.4
    discoverability: 68.3
    operational_transparency: 42.1
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 21.6
      derived: 0
      marker_coverage: 0.0
      total: 88
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/gluu/gluu-2026-06-20T181925.png
security:
- kind: authentication
  name: Gluu Authentication
  slug: gluu-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gluu Domain Security
  slug: gluu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gluu Vulnerability Disclosure
  slug: gluu-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: gluu-admin-webhooks
  slug: gluu-admin-webhooks
- name: gluu-fido2-passkey-enrollment
  slug: gluu-fido2-passkey-enrollment
- name: gluu-oauth-client-lifecycle
  slug: gluu-oauth-client-lifecycle
- name: gluu-scim-user-provisioning
  slug: gluu-scim-user-provisioning
slug: gluu
tags:
- Identity and Access Management
- Authentication
- Authorization
- Cedar
- FIDO2
- Identities
- OAuth
- Open Source
- OpenID Connect
- SCIM
- Identity Federation
website: https://gluu.org/
---
