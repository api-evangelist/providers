---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - '{''url'': ''https://venafi.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.paloaltonetworks.com/network-security/next-gen-trust-security/certificate-manager — a different registrable domain (venafi.com -> paloaltonetworks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The endpoints in this section allow you to manage your OAuth environment. Using endpoints described in this section, you can configure your global OAuth properties, assign roles to identities, create '
  name: Venafi Access Management APIs API
  slug: venafi-access-management-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The AlgorithmSelector interface provides the ability to retrieve and configure allowed Key Algorithms for policy, key and certificate objects
  name: Venafi AlgorithmSelector APIs API
  slug: venafi-algorithmselector-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Application API from Venafi — 7 operation(s) for application.
  name: Venafi Application API
  slug: venafi-application-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Auth REST SDK manages authorization bearer tokens. The tokens you need are based on the set of API calls that your client uses. The Auth SDK uses the VEDauth service to grant access and manage tok
  name: Venafi Authentication Server APIs API
  slug: venafi-authentication-server-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Approvals API from Venafi — 5 operation(s) for certificate approvals.
  name: Venafi Certificate Approvals API
  slug: venafi-certificate-approvals-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Auto-renewal Monitoring API from Venafi — 4 operation(s) for certificate auto-renewal monitoring.
  name: Venafi Certificate Auto-renewal Monitoring API
  slug: venafi-certificate-auto-renewal-monitoring-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Discovery API from Venafi — 2 operation(s) for certificate discovery.
  name: Venafi Certificate Discovery API
  slug: venafi-certificate-discovery-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Expiration Reports API from Venafi — 2 operation(s) for certificate expiration reports.
  name: Venafi Certificate Expiration Reports API
  slug: venafi-certificate-expiration-reports-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Import API from Venafi — 1 operation(s) for certificate import.
  name: Venafi Certificate Import API
  slug: venafi-certificate-import-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Installations API from Venafi — 4 operation(s) for certificate installations.
  name: Venafi Certificate Installations API
  slug: venafi-certificate-installations-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Inventory Monitoring API from Venafi — 3 operation(s) for certificate inventory monitoring.
  name: Venafi Certificate Inventory Monitoring API
  slug: venafi-certificate-inventory-monitoring-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The endpoints in this section manage TLS certificates. If you want certificates to secure SSH keys, see the _SshCertificates_ section ## PKIX Parameter Set ## As of TPP 25.1 algorithms are identified '
  name: Venafi Certificate Management APIs API
  slug: venafi-certificate-management-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Policy API from Venafi — 3 operation(s) for certificate policy.
  name: Venafi Certificate Policy API
  slug: venafi-certificate-policy-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Request API from Venafi — 5 operation(s) for certificate request.
  name: Venafi Certificate Request API
  slug: venafi-certificate-request-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificate Revocation Approvals API from Venafi — 2 operation(s) for certificate revocation approvals.
  name: Venafi Certificate Revocation Approvals API
  slug: venafi-certificate-revocation-approvals-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Certificates API from Venafi — 8 operation(s) for certificates.
  name: Venafi Certificates API
  slug: venafi-certificates-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: '## OSName Definitions ## * AIX * Android * BlackBerry * BSD * HPux * iOS * Linux * MacOS * Other * Solaris * Unknown * Windows * zOS ## ClientType Definitions ## |ClientType|Description| |---|---| |Ve'
  name: Venafi Client Management APIs API
  slug: venafi-client-management-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: Code Sign Manager allows you to make REST API calls to manage global configurations, templates, projects, signing applications, and rights.
  name: Venafi CodeSigning APIs API
  slug: venafi-codesigning-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: This API allows you to request digital signing of software and manage signing, authentication, and encryption keys. This API requires the CyberArk Code Sign Manager product.
  name: Venafi CodeSigning HSM API
  slug: venafi-codesigning-hsm-api-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: '## Introduction ## The Config interface manages objects, attributes, and policy values. API responses include a `Result` value that describes the result of the API call. If an operation failed, the AP'
  name: Venafi Configuration APIs API
  slug: venafi-configuration-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Credentials interface stores information about credentials for use in requesting certificates and other activities. Trust Protection Foundation only stores the credentials you create. Any remote c
  name: Venafi Credential APIs API
  slug: venafi-credential-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Credential Management API from Venafi — 7 operation(s) for credential management.
  name: Venafi Credential Management API
  slug: venafi-credential-management-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Discovery interface manages certificate, device, and application information from your network.
  name: Venafi Discovery Management APIs API
  slug: venafi-discovery-management-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Crypto interface provides limited access to the cryptography configuration. Trust Protection Foundation installs with two encryption keys, the default Trust Protection Foundation software encrypti
  name: Venafi Encryption APIs API
  slug: venafi-encryption-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Event Logs API from Venafi — 3 operation(s) for event logs.
  name: Venafi Event Logs API
  slug: venafi-event-logs-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Flow API manages the sequence of tasks. If one of the tasks is has an 'approval required', Flow Tickets manages that approval.
  name: Venafi Flow APIs API
  slug: venafi-flow-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The Public Key Infrastructure (PKI) interface allows Trust Protection Foundation to act as an Intermediate Certificate Authority for certificate vaults. This interface also sends the CSR to the CA to '
  name: Venafi HashiCorp PKI APIs API
  slug: venafi-hashicorp-pki-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The Identity interface manages users and group access. The Web SDK supports the following identity providers for viewing individuals and groups of users: |Provider|Requirements| |---|---| |AD|Read onl'
  name: Venafi Identity APIs API
  slug: venafi-identity-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The Workflow/Ticket interface manages certificates in an automated workflow. Trust Protection Foundation engines rely upon workflow object settings and their assignment to folders for the creation of '
  name: Venafi Legacy Workflow APIs API
  slug: venafi-legacy-workflow-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Log APIs allow to manage CyberArk application event logs. The Log interface allow for events to be recorded in the Trust Protection Foundation log table. Many API method calls do not automatically
  name: Venafi Log APIs API
  slug: venafi-log-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Machine Identities API from Venafi — 4 operation(s) for machine identities.
  name: Venafi Machine Identities API
  slug: venafi-machine-identities-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Machine Types API from Venafi — 1 operation(s) for machine types.
  name: Venafi Machine Types API
  slug: venafi-machine-types-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Machines API from Venafi — 8 operation(s) for machines.
  name: Venafi Machines API
  slug: venafi-machines-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The Metadata interface manages Custom Fields for objects that appear in the following places of the UI: * Certificates * Devices * Code Signing Projects * Code Signing Environments # Metadata Types |T'
  name: Venafi Metadata APIs API
  slug: venafi-metadata-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The Permissions interface enables the management and querying of permissions within CyberArk Trust Protection Foundation™. Permissions grant principals (users and groups) privileges to objects within '
  name: Venafi Permission APIs API
  slug: venafi-permission-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The ServerStatus endpoints allow you to query if a Trust Protection Foundation is in the active or idle state. This can be useful in configurations where the standby feature is enabled and load balanc
  name: Venafi Platform APIs API
  slug: venafi-platform-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Plugins API from Venafi — 4 operation(s) for plugins.
  name: Venafi Plugins API
  slug: venafi-plugins-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Private Key Import API from Venafi — 2 operation(s) for private key import.
  name: Venafi Private Key Import API
  slug: venafi-private-key-import-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The ProcessingEngines interface assigns and controls how Platforms engines manage information in Policy folders. These features provide a means for load balancing certificate management across a netwo
  name: Venafi Processing Engines APIs API
  slug: venafi-processing-engines-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The RecycleBin interface allows you to manage old or recently deleted data.
  name: Venafi Recycle Bin APIs API
  slug: venafi-recycle-bin-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: SecretStore APIs
  name: Venafi SecretStore APIs API
  slug: venafi-secretstore-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Service Accounts API from Venafi — 5 operation(s) for service accounts.
  name: Venafi Service Accounts API
  slug: venafi-service-accounts-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The SSH Certificate APIs allow to manage the issuance of special certificates for SSH devices. These endpoints are valid only if you purchased SSH Manager for Machines.
  name: Venafi SSH Certificate APIs API
  slug: venafi-ssh-certificate-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The SSH Management APIs allow to manage device keys and keysets. This interface is valid only if you purchased SSH Manager for Machines. All product-supported operations are exposed via this API, incl
  name: Venafi SSH Management APIs API
  slug: venafi-ssh-management-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Statistics APIs provide metrics about Trust Protection Foundation operations. You can query, group, and filter data and then use it in your own reporting applications.
  name: Venafi Statistics APIs API
  slug: venafi-statistics-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: 'The SystemStatus interface provides status and upgrade information about Trust Protection Foundation engines. This information also appears in the UI. # Engine Upgrade Status EngineUpgradeState descri'
  name: Venafi System Status APIs API
  slug: venafi-system-status-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Tags API from Venafi — 9 operation(s) for tags.
  name: Venafi Tags API
  slug: venafi-tags-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Teams API from Venafi — 4 operation(s) for teams.
  name: Venafi Teams API
  slug: venafi-teams-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Teams interface allows you to associate AD, LDAP, and local Identities to Policy assets and CyberArk products.
  name: Venafi Teams APIs API
  slug: venafi-teams-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The User Accounts API from Venafi — 1 operation(s) for user accounts.
  name: Venafi User Accounts API
  slug: venafi-user-accounts-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Preference APIs allow to manages the caller's user preferences
  name: Venafi User Preference APIs API
  slug: venafi-user-preference-apis-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Users API from Venafi — 7 operation(s) for users.
  name: Venafi Users API
  slug: venafi-users-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The VSatellite API from Venafi — 11 operation(s) for vsatellite.
  name: Venafi V Satellite API
  slug: venafi-vsatellite-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Webhooks API from Venafi — 2 operation(s) for webhooks.
  name: Venafi Webhooks API
  slug: venafi-webhooks-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Workload Identity Manager Configurations API from Venafi — 2 operation(s) for workload identity manager configurations.
  name: Venafi Workload Identity Manager Configurations API
  slug: venafi-workload-identity-manager-configurations-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Workload Identity Manager Intermediate Certificates API from Venafi — 1 operation(s) for workload identity manager intermediate certificates.
  name: Venafi Workload Identity Manager Intermediate Certificates API
  slug: venafi-workload-identity-manager-intermediate-certificates-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Workload Identity Manager Policies API from Venafi — 2 operation(s) for workload identity manager policies.
  name: Venafi Workload Identity Manager Policies API
  slug: venafi-workload-identity-manager-policies-api
- baseURL: https://api.venafi.cloud
  baseurl_source: declared
  description: The Workload Identity Manager Sub CA Providers API from Venafi — 2 operation(s) for workload identity manager sub ca providers.
  name: Venafi Workload Identity Manager Sub CA Providers API
  slug: venafi-workload-identity-manager-sub-ca-providers-api
artifact_total: 71
asyncapis:
- description: ''
  name: Venafi Certificate Manager Saas Webhooks
  slug: venafi-certificate-manager-saas-webhooks
common:
- group: other
  href: https://artifacts.apis.io/venafi/capabilities/venafi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/venafi-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/palo-alto-networks/
- group: auth
  href: https://artifacts.apis.io/venafi/security/venafi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/venafi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/venafi/authentication/venafi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/venafi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://venafi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.venafi.com/tlsprotectcloud
- group: docs
  title: ''
  type: Documentation
  url: https://docs.venafi.cloud/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.venafi.com/tlsprotectcloud/reference/tls-protect-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.venafi.cloud/api/api-setup/
- group: operate
  title: ''
  type: Support
  url: https://community.cyberark.com/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Venafi
- group: start
  title: ''
  type: SignUp
  url: https://login.venafi.cloud/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.venafi.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.venafi.cloud/whatsnew/
- group: build
  href: https://artifacts.apis.io/venafi/packages/venafi-packages.yml
  title: ''
  type: Packages
  url: packages/venafi-packages.yml
- group: build
  href: https://artifacts.apis.io/venafi/packages/venafi-packages.yml
  title: ''
  type: SDKs
  url: packages/venafi-packages.yml
- group: build
  href: https://artifacts.apis.io/venafi/cli/venafi-cli.yml
  title: ''
  type: CLI
  url: cli/venafi-cli.yml
- group: agent
  href: https://artifacts.apis.io/venafi/mcp/venafi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/venafi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/venafi/llms/venafi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/venafi-llms.txt
- group: other
  href: https://artifacts.apis.io/venafi/overlays/venafi-certificate-manager-saas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/venafi-certificate-manager-saas-overlay.yaml
- group: other
  href: https://artifacts.apis.io/venafi/overlays/venafi-trust-protection-foundation-websdk-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/venafi-trust-protection-foundation-websdk-overlay.yaml
- group: design
  href: https://artifacts.apis.io/venafi/conformance/venafi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/venafi-conformance.yml
- group: design
  href: https://artifacts.apis.io/venafi/errors/venafi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/venafi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/venafi/lifecycle/venafi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/venafi-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/venafi/scopes/venafi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/venafi-scopes.yml
- group: design
  href: https://artifacts.apis.io/venafi/conventions/venafi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/venafi-conventions.yml
- group: operate
  href: https://artifacts.apis.io/venafi/changelog/venafi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/venafi-changelog.yml
- group: design
  href: https://artifacts.apis.io/venafi/data-model/venafi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/venafi-data-model.yml
- group: design
  href: https://artifacts.apis.io/venafi/asyncapi/venafi-certificate-manager-saas-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/venafi-certificate-manager-saas-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/venafi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/venafi/plans/venafi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/venafi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/venafi/rate-limits/venafi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/venafi-rate-limits.yml
created: '2026-09-02'
description: 'Venafi is the machine identity security platform for discovering, issuing, provisioning and retiring TLS/SSL certificates, SSH keys, code-signing keys and workload identities across data centers, clouds and Kubernetes. Its Control Plane ships two public REST contracts: the SaaS "Certificate Manager - SaaS" API on api.venafi.cloud (six data-residency regions) and the self-hosted Trust Protection Foundation WebSDK. Venafi was acquired by CyberArk in 2024 and the products now carry CyberArk Certificate Manager branding; venafi.com itself 301s to Palo Alto Networks following its acquisition of CyberArk, while developer.venafi.com, docs.venafi.com, docs.venafi.cloud, api.venafi.cloud and github.com/Venafi remain live and are where every artifact in this profile came from.'
finops:
- has_sources: true
  method: derived
  name: Venafi Finops
  primary_unit: ''
  service_category: ''
  slug: venafi-finops
  template: true
image: https://avatars.githubusercontent.com/u/7817722?v=4
layout: provider
modified: '2026-09-02'
name: Venafi
nav: Providers
network: true
overview: 'Venafi publishes 58 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Management APIs API, AlgorithmSelector APIs API, Application API, and 55 more. Tagged areas include Company, Security, Certificates, PKI, and Machine Identity.


  The Venafi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Venafi''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, changelog, and 25 more developer resources.'
plans:
- name: Venafi Plans Pricing
  plan_count: 0
  slug: venafi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Venafi Rate Limits
  slug: venafi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Venafi API Rules
  rule_count: 53
  severity_counts:
    error: 28
    hint: 0
    info: 5
    warn: 20
  slug: venafi-rules
scopes:
- name: Venafi Scopes
  scope_count: 33
  slug: venafi-scopes
  summary_line: 33 scopes
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 57.3
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 44.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/venafi/venafi-2026-10-11T132803.png
security:
- kind: authentication
  name: Venafi Authentication
  slug: venafi-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Venafi Domain Security
  slug: venafi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: venafi-authenticate-websdk-oauth
  slug: venafi-authenticate-websdk-oauth
- name: venafi-configure-expiration-webhook
  slug: venafi-configure-expiration-webhook
- name: venafi-find-expiring-certificates
  slug: venafi-find-expiring-certificates
- name: venafi-request-tls-certificate
  slug: venafi-request-tls-certificate
- name: venafi-retire-and-recover-certificates
  slug: venafi-retire-and-recover-certificates
slug: venafi
tags:
- Company
- Security
- Certificates
- PKI
- Machine Identity
- Identity
- Cryptography
- Key Management
- Certificate Lifecycle Management
- DevOps
- Kubernetes
- Code Signing
website: https://venafi.com/
---
