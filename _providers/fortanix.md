---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 184
  human_in_the_loop: 10
  name: Fortanix Agentic Access
  operation_count: 316
  slug: fortanix-agentic-access
  summary_line: 316 operations · 184 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: 'REST API for the Fortanix Confidential Computing Manager (CCM) backend: compute-node and application enrollment, enclave image build and conversion, attestation, certificate issuance, container regist'
  name: Fortanix Confidential Computing Manager REST API
  slug: ccm
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Account_extensions API from Fortanix — 1 operation(s) for account_extensions.
  name: Fortanix Account Extensions API
  slug: fortanix-account-extensions-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Accounts API from Fortanix — 9 operation(s) for accounts.
  name: Fortanix Accounts API
  slug: fortanix-accounts-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Admin API from Fortanix — 1 operation(s) for admin.
  name: Fortanix Admin API
  slug: fortanix-admin-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The App API from Fortanix — 5 operation(s) for app.
  name: Fortanix App API
  slug: fortanix-app-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The ApplicationConfig API from Fortanix — 4 operation(s) for applicationconfig.
  name: Fortanix Application Config API
  slug: fortanix-applicationconfig-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Approval_requests API from Fortanix — 6 operation(s) for approval_requests.
  name: Fortanix Approval Requests API
  slug: fortanix-approval-requests-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The ApprovalRequests API from Fortanix — 5 operation(s) for approvalrequests.
  name: Fortanix Approval Requests API
  slug: fortanix-approvalrequests-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Apps API from Fortanix — 7 operation(s) for apps.
  name: Fortanix Apps API
  slug: fortanix-apps-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Auth API from Fortanix — 5 operation(s) for auth.
  name: Fortanix Auth API
  slug: fortanix-auth-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding creating or ending a session.
  name: Fortanix Authentication API
  slug: fortanix-authentication-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Batch API from Fortanix — 1 operation(s) for batch.
  name: Fortanix Batch API
  slug: fortanix-batch-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Build API from Fortanix — 5 operation(s) for build.
  name: Fortanix Build API
  slug: fortanix-build-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Certificate API from Fortanix — 1 operation(s) for certificate.
  name: Fortanix Certificate API
  slug: fortanix-certificate-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The ComputeClusters API from Fortanix — 2 operation(s) for computeclusters.
  name: Fortanix Compute Clusters API
  slug: fortanix-computeclusters-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Credentials API from Fortanix — 3 operation(s) for credentials.
  name: Fortanix Credentials API
  slug: fortanix-credentials-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Crypto API from Fortanix — 24 operation(s) for crypto.
  name: Fortanix Crypto API
  slug: fortanix-crypto-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Dataset API from Fortanix — 2 operation(s) for dataset.
  name: Fortanix Dataset API
  slug: fortanix-dataset-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the reports related to AWS.
  name: Fortanix Discovery Aws Reports API
  slug: fortanix-discoveryawsreports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the reports related to Azure.
  name: Fortanix Discovery Azure Reports API
  slug: fortanix-discoveryazurereports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining details about the connection.
  name: Fortanix Discovery Connection API
  slug: fortanix-discoveryconnection-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the reports related to DSM.
  name: Fortanix Discovery Dsm Reports API
  slug: fortanix-discoverydsmreports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the details about the inventory objects.
  name: Fortanix Discovery Inventory API
  slug: fortanix-discoveryinventory-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the reports related to On-Prem infrastructure.
  name: Fortanix Discovery On Prem Reports API
  slug: fortanix-discoveryonpremreports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining details about the policies.
  name: Fortanix Discovery Policies API
  slug: fortanix-discoverypolicies-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the PQC reports.
  name: Fortanix Discovery Pqc Reports API
  slug: fortanix-discoverypqcreports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining details about the scans.
  name: Fortanix Discovery Scan API
  slug: fortanix-discoveryscan-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the details about the inventory objects associated to a scan.
  name: Fortanix Discovery Scan Inventory API
  slug: fortanix-discoveryscaninventory-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: APIs regarding obtaining the reports for Services.
  name: Fortanix Discovery Services Reports API
  slug: fortanix-discoveryservicesreports-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The External_roles API from Fortanix — 3 operation(s) for external_roles.
  name: Fortanix External Roles API
  slug: fortanix-external-roles-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Fido API from Fortanix — 2 operation(s) for fido.
  name: Fortanix Fido API
  slug: fortanix-fido-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Groups API from Fortanix — 10 operation(s) for groups.
  name: Fortanix Groups API
  slug: fortanix-groups-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Keys API from Fortanix — 20 operation(s) for keys.
  name: Fortanix Keys API
  slug: fortanix-keys-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Logs API from Fortanix — 1 operation(s) for logs.
  name: Fortanix Logs API
  slug: fortanix-logs-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Marketplace API from Fortanix — 1 operation(s) for marketplace.
  name: Fortanix Marketplace API
  slug: fortanix-marketplace-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Misc API from Fortanix — 9 operation(s) for misc.
  name: Fortanix Misc API
  slug: fortanix-misc-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Node API from Fortanix — 5 operation(s) for node.
  name: Fortanix Node API
  slug: fortanix-node-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Plugins API from Fortanix — 2 operation(s) for plugins.
  name: Fortanix Plugins API
  slug: fortanix-plugins-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Registry API from Fortanix — 4 operation(s) for registry.
  name: Fortanix Registry API
  slug: fortanix-registry-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Roles API from Fortanix — 2 operation(s) for roles.
  name: Fortanix Roles API
  slug: fortanix-roles-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Session API from Fortanix — 11 operation(s) for session.
  name: Fortanix Session API
  slug: fortanix-session-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Stats API from Fortanix — 5 operation(s) for stats.
  name: Fortanix Stats API
  slug: fortanix-stats-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The System API from Fortanix — 1 operation(s) for system.
  name: Fortanix System API
  slug: fortanix-system-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Task API from Fortanix — 3 operation(s) for task.
  name: Fortanix Task API
  slug: fortanix-task-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Tools API from Fortanix — 2 operation(s) for tools.
  name: Fortanix Tools API
  slug: fortanix-tools-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Users API from Fortanix — 20 operation(s) for users.
  name: Fortanix Users API
  slug: fortanix-users-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Version API from Fortanix — 1 operation(s) for version.
  name: Fortanix Version API
  slug: fortanix-version-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Workflow API from Fortanix — 2 operation(s) for workflow.
  name: Fortanix Workflow API
  slug: fortanix-workflow-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The WorkflowFinal API from Fortanix — 3 operation(s) for workflowfinal.
  name: Fortanix Workflow Final API
  slug: fortanix-workflowfinal-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The WorkflowRuns API from Fortanix — 5 operation(s) for workflowruns.
  name: Fortanix Workflow Runs API
  slug: fortanix-workflowruns-api
- baseURL: https://amer.smartkey.io
  baseurl_source: declared
  description: The Zone API from Fortanix — 5 operation(s) for zone.
  name: Fortanix Zone API
  slug: fortanix-zone-api
artifact_total: 60
collections:
- collection_type: open
  name: Armor API
  slug: open-fortanix-armor-key-insight-openapi-original
- collection_type: open
  name: Confidential Computing Manager
  slug: open-fortanix-ccm-openapi-original
- collection_type: open
  name: Fortanix DSM REST API
  slug: open-fortanix-dsm-openapi-original
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fortanix-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fortanix-dsm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fortanix-armor-key-insight-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fortanix-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fortanix-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fortanix-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fortanix-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.fortanix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.fortanix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.fortanix.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://support.fortanix.com/apidocs/dsm-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://support.fortanix.com/docs/getting-started-with-fortanix-dsm
- group: operate
  title: ''
  type: Support
  url: https://support.fortanix.com/docs/fortanix-support
- group: company
  title: ''
  type: Blog
  url: https://www.fortanix.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortanix
- group: start
  title: ''
  type: SignUp
  url: https://www.fortanix.com/start-your-free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fortanix.com/legal/agreements-and-standard-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fortanix.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fortanix.com/
- group: start
  title: ''
  type: Console
  url: https://amer.smartkey.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/fortanix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fortanix-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortanix-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fortanix.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.fortanix.com/trust-center
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fortanix-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fortanix-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/fortanix-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fortanix-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/fortanix-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fortanix-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fortanix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fortanix-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fortanix-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fortanix-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fortanix-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fortanix-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fortanix-llms.txt
created: '2026-08-01'
description: Fortanix is a data-security company building the Fortanix Data & AI Security Platform, a unified control plane for enterprise cryptography. Its products include Data Security Manager (DSM) — a FIPS 140-2 Level 3 validated key-management, HSM, tokenization and secrets service delivered as SaaS or as on-premises appliances; Confidential Computing Manager (CCM) for enclave conversion, attestation and workload signing on Intel SGX and AWS Nitro; Key Insight for cryptographic discovery, posture and post-quantum readiness across cloud and on-premises estates; and Fortanix Armor. All three products publish public REST APIs with machine-readable OpenAPI/Swagger contracts, and Fortanix ships first-party client SDKs (Java, Python, Go, Rust, C#, PHP, JavaScript), a Python CLI (sdkms-cli), Terraform providers, and legacy cryptographic interfaces (PKCS#11, Microsoft CNG, Java JCE).
image: https://cdn.aglty.io/fortanix/global-header/fortanix-logo.svg
layout: provider
modified: '2026-08-01'
name: Fortanix
nav: Providers
network: true
overview: 'Fortanix publishes 51 APIs on the [APIs.io](https://apis.io/) network, including Confidential Computing Manager REST API, Account Extensions API, Accounts API, and 48 more. Tagged areas include Company, Security, Encryption, Key Management, and Cryptography.


  Fortanix''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, developer console, and 32 more developer resources.'
random_paper: 14
scopes:
- name: Fortanix Scopes
  scope_count: 0
  slug: fortanix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortanix/refs/heads/main/screenshots/fortanix-2026-08-07T165417.png
security:
- kind: authentication
  name: Fortanix Authentication
  slug: fortanix-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Fortanix Domain Security
  slug: fortanix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fortanix Vulnerability Disclosure
  slug: fortanix-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Fortanix Trust Center
  slug: fortanix-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FIPS 140-2 Level 3, CIS Benchmarks
slug: fortanix
tags:
- Company
- Security
- Encryption
- Key Management
- Cryptography
- Confidential Computing
- HSM
- Data Security
- Post-Quantum
- Secrets Management
website: https://www.fortanix.com/
---
