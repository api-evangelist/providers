---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cisco Psirt Agentic Access
  operation_count: 30
  slug: cisco-psirt-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- description: Current supported API endpoints.
  name: Cisco PSIRT openVuln API Current Endpoints API
  slug: cisco-psirt-current-endpoints-api
- description: These API endpoints are no longer available. Migrate to current version calls.
  name: Cisco PSIRT openVuln API Obsolete Endpoints API
  slug: cisco-psirt-obsolete-endpoints-api
- description: The "security/advisories" basepath will be deprecated in the future. These API endpoints have changed with the introduction of v2 basepath. Migrate the below endpoints to current endpoint calls. The b
  name: Cisco PSIRT openVuln API Sunset Endpoints API
  slug: cisco-psirt-sunset-endpoints-api
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cisco-psirt-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-psirt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-psirt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-psirt-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/psirt/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/psirt/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/psirt/
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/CiscoPSIRT/openVulnAPI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoPSIRT
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: build
  title: ''
  type: Packages
  url: packages/cisco-psirt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cisco-psirt-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cisco-psirt-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cisco-psirt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cisco-psirt-security.txt
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-psirt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cisco-psirt-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustportal.cisco.com/c/r/ctp/home.html
- group: design
  title: ''
  type: Conformance
  url: conformance/cisco-psirt-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cisco-psirt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cisco-psirt-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cisco-psirt-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cisco-psirt-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cisco-psirt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cisco-psirt-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/cisco-psirt-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cisco-psirt-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cisco-psirt-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cisco-psirt-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cisco-psirt-tool-crosswalk.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/psirt/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.cisco.com/docs/psirt/authentication/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.cisco.com/docs/psirt/faq/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/site/support/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/psirt
- group: start
  title: ''
  type: SignUp
  url: https://apiconsole.cisco.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/CiscoPSIRT/openVulnAPI/blob/master/LICENSE.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
created: '2026-08-19'
description: The Cisco Product Security Incident Response Team (PSIRT) openVuln API is Cisco's machine-readable vulnerability disclosure service. It lets security teams query Cisco security advisories by CVE, advisory ID, severity, publication date, affected product or specific IOS/IOS-XE release, and returns CVRF and OVAL content alongside JSON. It is one of the few Cisco surfaces with a genuinely public, fetchable OpenAPI 3.0.3 document, published in the CiscoPSIRT GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco.png
layout: provider
modified: '2026-08-19'
name: Cisco PSIRT openVuln API
nav: Providers
network: true
overview: 'Cisco PSIRT openVuln API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Current Endpoints API, Obsolete Endpoints API, and Sunset Endpoints API. Tagged areas include Security, Vulnerability Management, Threat Intelligence, Disclosure, and Compliance.


  Cisco PSIRT openVuln API''s developer surface includes authentication, developer portal, documentation, API reference, CLI, getting-started guide, FAQ, and 34 more developer resources.'
plans:
- name: Cisco Psirt Plans Pricing
  plan_count: 0
  slug: cisco-psirt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Cisco Psirt Rate Limits
  slug: cisco-psirt-rate-limits
scopes:
- name: Cisco Psirt Scopes
  scope_count: 2
  slug: cisco-psirt-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 48.3
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Cisco Psirt Authentication
  slug: cisco-psirt-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cisco Psirt Domain Security
  slug: cisco-psirt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Psirt Vulnerability Disclosure
  slug: cisco-psirt-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cisco Psirt Trust Center
  slug: cisco-psirt-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, BSI C5, GDPR
slug: cisco-psirt
tags:
- Security
- Vulnerability Management
- Threat Intelligence
- Disclosure
- Compliance
- Networking
website: https://developer.cisco.com/psirt/
---
