---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Armis Agentic Access
  operation_count: 34
  slug: armis-agentic-access
  summary_line: 34 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote MCP server hosted on the Armis developer portal exposing endpoint discovery, endpoint detail, search, authentication and request execution against the Armis API.
  name: Armis Developer Portal MCP Server
  slug: armis-developer-portal-mcp
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Alerts API from Armis — 1 operation(s) for alerts.
  name: Armis Alerts API
  slug: armis-alerts-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The ARP API from Armis — 1 operation(s) for arp.
  name: Armis ARP API
  slug: armis-arp-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Assets API from Armis — 3 operation(s) for assets.
  name: Armis Assets API
  slug: armis-assets-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: Manage authentication of the API.
  name: Armis Authentication API
  slug: armis-authentication-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Boundaries API from Armis — 2 operation(s) for boundaries.
  name: Armis Boundaries API
  slug: armis-boundaries-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Collectors API from Armis — 3 operation(s) for collectors.
  name: Armis Collectors API
  slug: armis-collectors-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Data Export API from Armis — 2 operation(s) for data export.
  name: Armis Data Export API
  slug: armis-data-export-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Device Custom Properties API from Armis — 2 operation(s) for device custom properties.
  name: Armis Device Custom Properties API
  slug: armis-device-custom-properties-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Integrations API from Armis — 3 operation(s) for integrations.
  name: Armis Integrations API
  slug: armis-integrations-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Policies API from Armis — 1 operation(s) for policies.
  name: Armis Policies API
  slug: armis-policies-api
- baseURL: https://api.armis.com/v3
  baseurl_source: declared
  description: The Sites API from Armis — 2 operation(s) for sites.
  name: Armis Sites API
  slug: armis-sites-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/armis/capabilities/armis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/armis-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/armis/agentic-access/armis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/armis-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/armis/rules/armis-rules.yml
  title: ''
  type: Spectral
  url: rules/armis-rules.yml
- group: design
  href: https://artifacts.apis.io/armis/json-ld/armis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/armis-context.jsonld
- group: design
  href: https://artifacts.apis.io/armis/vocabulary/armis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/armis-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/armis/data-model/armis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/armis-data-model.yml
- group: auth
  href: https://artifacts.apis.io/armis/security/armis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/armis-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/armis/errors/armis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/armis-problem-types.yml
- group: auth
  href: https://artifacts.apis.io/armis/well-known/armis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/armis-security.txt
- group: agent
  href: https://artifacts.apis.io/armis/well-known/armis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/armis-well-known.yml
- group: other
  href: https://artifacts.apis.io/armis/hosts/armis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/armis-hosts.yml
- group: build
  href: https://artifacts.apis.io/armis/integrations/armis-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/armis-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/armis/vendors/armis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/armis-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.armis.com/about/newsroom/
- group: auth
  href: https://artifacts.apis.io/armis/security/armis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/armis-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/armis/conformance/armis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/armis-conformance.yml
- group: design
  href: https://artifacts.apis.io/armis/conventions/armis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/armis-conventions.yml
- group: company
  title: ''
  type: Website
  url: https://www.armis.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.armis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://armis-python-sdk.readthedocs.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArmisSecurity
- group: company
  title: ''
  type: Blog
  url: https://www.armis.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.armis.com/
- group: auth
  href: https://artifacts.apis.io/armis/security/armis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/armis-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.armis.com/
- group: auth
  href: https://artifacts.apis.io/armis/authentication/armis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/armis-authentication.yml
- group: build
  href: https://artifacts.apis.io/armis/packages/armis-packages.yml
  title: ''
  type: Packages
  url: packages/armis-packages.yml
- group: build
  href: https://artifacts.apis.io/armis/packages/armis-packages.yml
  title: ''
  type: SDKs
  url: packages/armis-packages.yml
- group: build
  href: https://artifacts.apis.io/armis/cli/armis-cli.yml
  title: ''
  type: CLI
  url: cli/armis-cli.yml
- group: agent
  href: https://artifacts.apis.io/armis/mcp/armis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/armis-mcp.yml
- group: agent
  href: https://artifacts.apis.io/armis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/armis/security/armis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armis-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/armis/llms/armis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/armis-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://dev.armis.com/docs/your-guide-to-building-with-armis-apis
- group: docs
  title: ''
  type: APIReference
  url: https://dev.armis.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.armis.com/docs/migration-from-api-v1
created: '2026-07-17'
description: Armis is a cyber exposure management and asset intelligence company. Its Armis Centrix platform discovers, protects, and manages every physical and virtual asset in an enterprise environment — IT, OT, ICS, IoT, IoMT, medical devices, cloud workloads, and applications — giving security teams real-time visibility, risk prioritization, and threat detection across the full attack surface. Armis exposes this intelligence through a tenant-scoped REST API secured with OAuth2 client-credentials, an official Python SDK (armis-sdk), a Go application-security scanning CLI (armis-cli), and two published Model Context Protocol servers (armis-knowledge-mcp and armis-appsec-mcp) for agent-native AppSec workflows. The company was surfaced as a portfolio company of General Catalyst and Insight Partners and enriched by the API Evangelist pipeline from its public developer surface.
image: https://avatars.githubusercontent.com/u/32813597?v=4
json_schemas:
- name: AuthRequest
  property_count: 6
  slug: armis-auth-request
- name: PersistentAlert
  property_count: 18
  slug: armis-persistent-alert
- name: PersistentCollector
  property_count: 23
  slug: armis-persistent-collector
- name: PersistentIntegration
  property_count: 11
  slug: armis-persistent-integration
- name: PersistentSite
  property_count: 11
  slug: armis-persistent-site
- name: SearchAssetsRequest
  property_count: 3
  slug: armis-search-assets-request
jsonld:
- class_count: 91
  name: Armis Context
  property_count: 152
  slug: armis-context
layout: provider
mcp_servers:
- description: Remote MCP server at dev.armis.com.
  name: Armis MCP Server
  slug: armis-mcp-yml
modified: '2026-10-20'
name: Armis
nav: Providers
network: true
overview: 'Armis publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, ARP API, Assets API, and 9 more. Tagged areas include Company, Defense Government, Security, Cybersecurity, and Asset Intelligence.


  The Armis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Armis'' developer surface includes documentation, engineering blog, support, authentication, CLI, API reference, changelog, and 29 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Armis Rate Limits
  slug: armis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Armis API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: armis-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 35.6
    contract_quality: 64.1
    developer_ergonomics: 66.7
    discoverability: 66.7
    operational_transparency: 52.6
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/armis/armis-2026-07-25T201217.png
security:
- kind: authentication
  name: Armis Authentication
  slug: armis-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Armis Domain Security
  slug: armis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Armis Vulnerability Disclosure
  slug: armis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Armis Trust Center
  slug: armis-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, FedRAMP, CSA STAR
slug: armis
tags:
- Company
- Defense Government
- Security
- Cybersecurity
- Asset Intelligence
- Exposure Management
- IoT
- OT Security
- Vulnerability Management
- Developer Tools
website: https://www.armis.com
---
