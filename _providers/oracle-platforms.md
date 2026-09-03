---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-09-03'
api_count: 6
apis:
- description: REST API for Oracle Fusion Cloud ERP providing access to financial management, procurement, and project management capabilities.
  name: Oracle Fusion Cloud ERP API
  slug: oracle-fusion-cloud-erp-api
- description: RESTful services for Oracle Application Express enabling low-code application development.
  name: Oracle APEX REST APIs
  slug: oracle-apex-rest-apis
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The analytics API from Oracle Platforms — 19 operation(s) for analytics.
  name: Oracle Platforms Analytics API
  slug: oracle-platforms-analytics-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The blockstorage API from Oracle Platforms — 33 operation(s) for blockstorage.
  name: Oracle Platforms Blockstorage API
  slug: oracle-platforms-blockstorage-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The compute API from Oracle Platforms — 82 operation(s) for compute.
  name: Oracle Platforms Compute API
  slug: oracle-platforms-compute-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The computeManagement API from Oracle Platforms — 23 operation(s) for computemanagement.
  name: Oracle Platforms Compute Management API
  slug: oracle-platforms-computemanagement-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The database API from Oracle Platforms — 319 operation(s) for database.
  name: Oracle Platforms Database API
  slug: oracle-platforms-database-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The dataScience API from Oracle Platforms — 99 operation(s) for datascience.
  name: Oracle Platforms Data Science API
  slug: oracle-platforms-datascience-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The integrationInstance API from Oracle Platforms — 19 operation(s) for integrationinstance.
  name: Oracle Platforms Integration Instance API
  slug: oracle-platforms-integrationinstance-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The oceInstance API from Oracle Platforms — 7 operation(s) for oceinstance.
  name: Oracle Platforms Oce Instance API
  slug: oracle-platforms-oceinstance-api
- baseURL: https://iaas.{region}.oraclecloud.com
  baseurl_source: declared
  description: The virtualNetwork API from Oracle Platforms — 176 operation(s) for virtualnetwork.
  name: Oracle Platforms Virtual Network API
  slug: oracle-platforms-virtualnetwork-api
artifact_total: 20
asyncapis:
- description: ''
  name: Oracle Platforms Events
  slug: oracle-platforms-events
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-platforms-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-core-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-database-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-integration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-content-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-analytics-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-platforms-data-science-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-platforms-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/oracle-platforms-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oracle-platforms-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oracle-platforms-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-platforms-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-platforms-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-platforms-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/oracle-platforms-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-platforms-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-platforms-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-platforms-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-platforms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/oracle-platforms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oracle-platforms-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oracle-platforms-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-platforms-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/oracle-platforms-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oracle-platforms-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/oracle-platforms-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-platforms-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/oracle-platforms-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oracle-platforms-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/oracle-platforms-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.oracle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en-us/iaas/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
- group: operate
  title: ''
  type: Support
  url: https://developer.oracle.com/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/cloud/price-list.html
- group: start
  title: ''
  type: SignUp
  url: https://signup.oraclecloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-15'
description: 'Oracle Platforms is the API Evangelist index of Oracle''s cloud and enterprise platform APIs: the Oracle Cloud Infrastructure (OCI) control plane for compute, storage, networking and databases, plus the PaaS and SaaS services layered on it — Autonomous Database, Integration Cloud, Content Management, Fusion Cloud ERP, Analytics Cloud, Data Science and APEX. Oracle publishes a machine-readable index of every OCI service specification at docs.oracle.com/en-us/iaas/api/specs/index.json, and six of those contracts — 1,154 operations across Core Services, Database, Data Science, Analytics, Integration and Content Management — are harvested verbatim into this repo. Authentication is RSA request signing rather than a bearer token, idempotency is the opc-retry-token header, and Oracle ships both managed remote MCP servers and 32 open-source reference MCP servers.'
finops:
- name: Oracle Platforms Finops
  service_category: API
  slug: oracle-platforms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-platforms.png
layout: provider
mcp_servers:
- description: ''
  name: Oracle Platforms MCP Server
  slug: oracle-platforms-mcp-server
modified: '2026-08-27'
name: Oracle Platforms
nav: Providers
network: true
overview: 'Oracle Platforms publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Blockstorage API, Compute API, and 6 more. Tagged areas include Analytics, Cloud Computing, Database, Enterprise Software, and Infrastructure-as-a-Service.


  The Oracle Platforms catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Oracle Platforms'' developer surface includes authentication, sandbox, changelog, CLI, documentation, API reference, getting-started guide, and 36 more developer resources.'
plans:
- name: Oracle Platforms Plans Pricing
  plan_count: 4
  slug: oracle-platforms-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 13
  name: Oracle Platforms Rate Limits
  slug: oracle-platforms-rate-limits
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 87.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 92.1
  previous_composite: 69.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-platforms/refs/heads/main/screenshots/oracle-platforms-2026-06-20T191139.png
security:
- kind: authentication
  name: Oracle Platforms Authentication
  slug: oracle-platforms-authentication
  summary_line: 7 schemes
- kind: domain-security
  name: Oracle Platforms Domain Security
  slug: oracle-platforms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oracle Platforms Vulnerability Disclosure
  slug: oracle-platforms-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Oracle Platforms Trust Center
  slug: oracle-platforms-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, PCI DSS, HIPAA, HITRUST, FedRAMP, DoD Impact Level authorizations, IRAP, C5, CSA STAR
slug: oracle-platforms
tags:
- Analytics
- Cloud Computing
- Database
- Enterprise Software
- Infrastructure-as-a-Service
- Integration
- Machine-Learning
- Platform-as-a-Service
- Software-as-a-Service
website: https://developer.oracle.com/
---
