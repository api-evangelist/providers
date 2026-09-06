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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 366
  human_in_the_loop: 7
  name: Cohesity Agentic Access
  operation_count: 687
  slug: cohesity-agentic-access
  summary_line: 687 operations · 366 acting · 7 human-in-the-loop
api_count: 4
apis:
- baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
  baseurl_source: declared
  description: Helios is Cohesity's SaaS-based control plane that manages a fleet of Cohesity clusters from a single global pane of glass. The Helios REST API authenticates via an apiKey generated from the Helios UI
  name: Cohesity Helios REST API
  slug: helios-rest-api
- baseURL: https://{cluster-vip}/irisservices/api/v1/public
  baseurl_source: declared
  description: The DataProtect REST API is the per-cluster RESTful interface exposed by every Cohesity cluster, providing programmatic control over data management operations including backups, restores, replication
  name: Cohesity DataProtect REST API
  slug: dataprotect-rest-api
- baseURL: https://helios.cohesity.com/heliosreporting/api/v1
  baseurl_source: declared
  description: The Helios Reporting service exposes Cohesity's cross-cluster reporting layer as a standalone REST API with 20 operations. It publishes a catalog of report types and their components, renders on-deman
  name: Cohesity Helios Reporting API
  slug: helios-reporting-api
- baseURL: https://helios.cohesity.com/v2/mcm/site-continuity/v2
  baseurl_source: declared
  description: Site Continuity is Cohesity's disaster-recovery orchestration service, exposed as a 25-operation REST API on the Helios control plane. It models sites, applications and DR plans, runs health checks th
  name: Cohesity Site Continuity API
  slug: site-continuity-api
artifact_total: 15
asyncapis:
- description: ''
  name: Cohesity Webhooks
  slug: cohesity-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cohesity-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cohesity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohesity-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cohesity
- group: company
  title: ''
  type: Website
  url: https://www.cohesity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cohesity.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.cohesity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cohesity.com/apidocs/versions/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cohesity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cohesity.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cohesity.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cohesity.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cohesity.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cohesity.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cohesity.com/agreements/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cohesity.com/agreements/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cohesity.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cohesity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cohesity.com/buy/cohesity-data-cloud-packaging/
- group: start
  title: ''
  type: SignUp
  url: https://www.cohesity.com/free-trial/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cohesity/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cohesity-cluster-v1-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cohesity-cluster-v2-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cohesity-helios-reporting-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cohesity-site-continuity-openapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/cohesity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cohesity-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cohesity-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cohesity-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cohesity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cohesity-cluster-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cohesity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cohesity.com/trust/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cohesity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cohesity-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cohesity.com/docs/whats-new-65
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cohesity-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cohesity-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cohesity-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cohesity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cohesity.com/trust/security-profile/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cohesity-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cohesity-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cohesity-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cohesity-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cohesity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cohesity-rate-limits.yml
created: '2025-03-01'
description: Cohesity is a data security and management company providing backup, disaster recovery, archive, and cyber resilience capabilities across on-premises, cloud, and SaaS workloads. Following the merger with Veritas, the combined company protects enterprise data while powering automation, orchestration, and AI- driven recovery. The Cohesity developer surface centers on the Cohesity REST API, exposed both per-cluster (DataProtect/cluster API) and via the Helios global control plane, with versioned v1 and v2 endpoints, API-key authentication, and SDKs for Python, PowerShell, Ansible, Terraform, and ServiceNow.
finops:
- name: Cohesity Finops
  service_category: API
  slug: cohesity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cohesity.png
layout: provider
mcp_servers:
- description: ''
  name: Cohesity Gaia MCP
  slug: cohesity-gaia-mcp
modified: '2026-09-05'
name: Cohesity
nav: Providers
network: true
overview: 'Cohesity publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Helios REST API, DataProtect REST API, Helios Reporting API, and 1 more. Tagged areas include Automation, Backup, Cyber Resilience, Data Management, and Data Protection.


  The Cohesity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cohesity''s developer surface includes authentication, developer portal, API reference, GitHub presence, documentation, support, engineering blog, and 41 more developer resources.'
plans:
- name: Cohesity Plans Pricing
  plan_count: 2
  slug: cohesity-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Cohesity Rate Limits
  slug: cohesity-rate-limits
scopes:
- name: Cohesity Scopes
  scope_count: 6
  slug: cohesity-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 59.0
    catalog_earned_first_party: 16.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 44.2
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 56.9
    developer_ergonomics: 68.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 22.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cohesity/refs/heads/main/screenshots/cohesity-2026-06-20T174720.png
security:
- kind: authentication
  name: Cohesity Authentication
  slug: cohesity-authentication
  summary_line: apiKey/oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Cohesity Domain Security
  slug: cohesity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cohesity Vulnerability Disclosure
  slug: cohesity-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cohesity Trust Center
  slug: cohesity-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, FedRAMP Moderate, GovRAMP, HIPAA, Common Criteria EAL2+ (ALC_FLR.1), NIST FIPS 140-2 Level 1, USGv6, Trade Agreements Act (TAA)
slug: cohesity
tags:
- Automation
- Backup
- Cyber Resilience
- Data Management
- Data Protection
- Data Security
- DataProtect
- Disaster Recovery
- Helios
- Orchestration
- Ransomware Recovery
- Site Continuity
- Reporting
- Model Context Protocol
- Enterprise Storage
website: https://www.cohesity.com/
---
