---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 98
  human_in_the_loop: 5
  name: Aembit Agentic Access
  operation_count: 167
  slug: aembit-agentic-access
  summary_line: 167 operations · 98 acting · 5 human-in-the-loop
api_count: 2
apis:
- description: A first-party hosted Model Context Protocol server that gives AI agents and MCP clients read-only access to a tenant's Aembit event logs. Three tools — get_audit_logs, get_auth_events and get_workload
  name: Aembit MCP Server
  slug: aembit-mcp-server
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Authorization Event API from Aembit — 2 operation(s) for access authorization event.
  name: Aembit Access Authorization Event API
  slug: aembit-access-authorization-event-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Condition API from Aembit — 2 operation(s) for access condition.
  name: Aembit Access Condition API
  slug: aembit-access-condition-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Condition v2 API from Aembit — 2 operation(s) for access condition v2.
  name: Aembit Access Condition v2 API
  slug: aembit-access-condition-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Policy (Deprecated) API from Aembit — 4 operation(s) for access policy (deprecated).
  name: Aembit Access Policy (Deprecated) API
  slug: aembit-access-policy-deprecated-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Policy v2 API from Aembit — 5 operation(s) for access policy v2.
  name: Aembit Access Policy v2 API
  slug: aembit-access-policy-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Agent Controller API from Aembit — 3 operation(s) for agent controller.
  name: Aembit Agent Controller API
  slug: aembit-agent-controller-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Audit Log API from Aembit — 2 operation(s) for audit log.
  name: Aembit Audit Log API
  slug: aembit-audit-log-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Auth API from Aembit — 1 operation(s) for auth.
  name: Aembit Auth API
  slug: aembit-auth-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Client Workload API from Aembit — 3 operation(s) for client workload.
  name: Aembit Client Workload API
  slug: aembit-client-workload-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Compliance API from Aembit — 1 operation(s) for compliance.
  name: Aembit Compliance API
  slug: aembit-compliance-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Content Security API from Aembit — 2 operation(s) for content security.
  name: Aembit Content Security API
  slug: aembit-content-security-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider (Deprecated) API from Aembit — 4 operation(s) for credential provider (deprecated).
  name: Aembit Credential Provider (Deprecated) API
  slug: aembit-credential-provider-deprecated-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider Integration API from Aembit — 3 operation(s) for credential provider integration.
  name: Aembit Credential Provider Integration API
  slug: aembit-credential-provider-integration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider v2 API from Aembit — 4 operation(s) for credential provider v2.
  name: Aembit Credential Provider v2 API
  slug: aembit-credential-provider-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credentials API from Aembit — 1 operation(s) for credentials.
  name: Aembit Credentials API
  slug: aembit-credentials-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The DiscoveryIntegration API from Aembit — 2 operation(s) for discoveryintegration.
  name: Aembit Discovery Integration API
  slug: aembit-discoveryintegration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The DiscoveryServerWorkloadDraft API from Aembit — 1 operation(s) for discoveryserverworkloaddraft.
  name: Aembit Discovery Server Workload Draft API
  slug: aembit-discoveryserverworkloaddraft-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Health API from Aembit — 1 operation(s) for health.
  name: Aembit Health API
  slug: aembit-health-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Integration API from Aembit — 2 operation(s) for integration.
  name: Aembit Integration API
  slug: aembit-integration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Integration v2 API from Aembit — 2 operation(s) for integration v2.
  name: Aembit Integration v2 API
  slug: aembit-integration-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Log Stream API from Aembit — 2 operation(s) for log stream.
  name: Aembit Log Stream API
  slug: aembit-log-stream-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The MFA SignOn Policy API from Aembit — 1 operation(s) for mfa signon policy.
  name: Aembit MFA SignOn Policy API
  slug: aembit-mfa-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Policy API from Aembit — 1 operation(s) for policy.
  name: Aembit Policy API
  slug: aembit-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Resource Set API from Aembit — 2 operation(s) for resource set.
  name: Aembit Resource Set API
  slug: aembit-resource-set-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Role API from Aembit — 2 operation(s) for role.
  name: Aembit Role API
  slug: aembit-role-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Routing API from Aembit — 2 operation(s) for routing.
  name: Aembit Routing API
  slug: aembit-routing-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Server Workload API from Aembit — 2 operation(s) for server workload.
  name: Aembit Server Workload API
  slug: aembit-server-workload-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SignOn Policy API from Aembit — 1 operation(s) for signon policy.
  name: Aembit SignOn Policy API
  slug: aembit-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SSO Identity Provider API from Aembit — 3 operation(s) for sso identity provider.
  name: Aembit SSO Identity Provider API
  slug: aembit-sso-identity-provider-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SSO SignOn Policy API from Aembit — 1 operation(s) for sso signon policy.
  name: Aembit SSO SignOn Policy API
  slug: aembit-sso-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Standalone Certificate Authority API from Aembit — 2 operation(s) for standalone certificate authority.
  name: Aembit Standalone Certificate Authority API
  slug: aembit-standalone-certificate-authority-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Standalone TLS Decrypt API from Aembit — 1 operation(s) for standalone tls decrypt.
  name: Aembit Standalone TLS Decrypt API
  slug: aembit-standalone-tls-decrypt-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The TLS Decrypt API from Aembit — 1 operation(s) for tls decrypt.
  name: Aembit TLS Decrypt API
  slug: aembit-tls-decrypt-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Trust Provider API from Aembit — 2 operation(s) for trust provider.
  name: Aembit Trust Provider API
  slug: aembit-trust-provider-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Trust Provider Secret API from Aembit — 2 operation(s) for trust provider secret.
  name: Aembit Trust Provider Secret API
  slug: aembit-trust-provider-secret-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The User API from Aembit — 3 operation(s) for user.
  name: Aembit User API
  slug: aembit-user-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Workload Event API from Aembit — 2 operation(s) for workload event.
  name: Aembit Workload Event API
  slug: aembit-workload-event-api
artifact_total: 47
asyncapis:
- description: ''
  name: Aembit Event Surface
  slug: aembit-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://aembit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aembit.io/dev-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aembit.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aembit.io/dev-guide/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aembit.io/get-started/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://support.aembit.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://aembit.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aembit
- group: commercial
  title: ''
  type: Pricing
  url: https://aembit.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://useast2.aembit.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aembit.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aembit.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aembit.io/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/lifecycle/aembit-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aembit-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aembit.io/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/security/aembit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aembit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/security/aembit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aembit-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aembit.io/changelog/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/cli/aembit-cli.yml
  title: ''
  type: CLI
  url: cli/aembit-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/packages/aembit-packages.yml
  title: ''
  type: Packages
  url: packages/aembit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/packages/aembit-packages.yml
  title: ''
  type: SDKs
  url: packages/aembit-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/mcp/aembit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aembit-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/mcp/aembit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aembit-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/llms/aembit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aembit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/agentic-access/aembit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aembit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/authentication/aembit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aembit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/conventions/aembit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aembit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/errors/aembit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aembit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/lifecycle/aembit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aembit-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/conformance/aembit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aembit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/data-model/aembit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aembit-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/plans/aembit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aembit-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/rate-limits/aembit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aembit-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/sandbox/aembit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aembit-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://useast2.aembit.io/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/overlays/aembit-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aembit-cloud-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/overlays/aembit-edge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aembit-edge-overlay.yaml
created: '2026-09-09'
description: Aembit is a Workload Identity and Access Management (Workload IAM) platform for non-human identities — AI agents, applications, microservices, CI/CD pipelines, scripts and service accounts. Instead of long-lived, hard-coded secrets, Aembit cryptographically attests a workload against a Trust Provider (AWS, Azure, GCP, GitHub Actions, GitLab, Kubernetes, Terraform Cloud, OIDC, SPIFFE, Kerberos), evaluates an Access Policy with optional conditional-access signals from CrowdStrike and Wiz, and injects a short-lived credential just-in-time so the application never stores one. The platform is delivered as a SaaS control plane (Aembit Cloud) plus a distributed enforcement layer (Aembit Edge — Agent Proxy, Agent Injector, AWS Lambda extension, CLI and Edge SDKs). Aembit publishes two OpenAPI 3.1.1 contracts — the Aembit Cloud API for managing every platform resource and the Aembit Edge API for workload authentication and credential retrieval — alongside a hosted, read-only MCP Server
  for querying audit, authorization and workload events, an MCP Identity Gateway and an MCP Authorization Server for governing AI-agent access to MCP servers.
image: https://aembit.io/wp-content/uploads/2023/08/aembit-favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Aembit MCP Server
  slug: aembit-mcp-server
modified: '2026-09-09'
name: Aembit
nav: Providers
network: true
overview: 'Aembit publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Access Authorization Event API, Access Condition API, Access Condition v2 API, and 34 more. Tagged areas include Security, Identity, Access Management, Workload Identity, and Non-Human Identity.


  The Aembit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aembit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Aembit Plans Pricing
  plan_count: 6
  slug: aembit-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Aembit Rate Limits
  slug: aembit-rate-limits
score:
  band: exemplar
  composite: 71.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 66.0
    developer_ergonomics: 76.8
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Aembit Authentication
  slug: aembit-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Aembit Domain Security
  slug: aembit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aembit Vulnerability Disclosure
  slug: aembit-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Aembit Trust Center
  slug: aembit-trust-center
  summary_line: SOC 2, ISO 27001
slug: aembit
tags:
- Security
- Identity
- Access Management
- Workload Identity
- Non-Human Identity
- Secrets Management
- Zero Trust
- Agentic AI
- MCP
- Authentication
- Authorization
- DevSecOps
- Cloud Security
website: https://aembit.io/
---
