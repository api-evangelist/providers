---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hexagon Agentic Access
  operation_count: 1
  slug: hexagon-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: REST APIs for the Nexus digital reality platform enabling manufacturers to build connected workflows integrating metrology, quality inspection, and production monitoring data. All endpoints are authen
  name: Hexagon Nexus API
  slug: nexus-api
- baseURL: https://docs.hexagonali.com
  baseurl_source: declared
  description: Enterprise Asset Management REST API providing programmatic access to asset lifecycle data including equipment management, work orders, preventive maintenance, document attachments, and service reques
  name: HxGN EAM REST API
  slug: hxgn-eam-api
- description: Smart Digital eXchange API Services enabling integration with Hexagon's engineering data management platform for plant design, document control, and digital twin workflows in process and power industr
  name: HxGN SDx API Services
  slug: hxgn-sdx-api
- description: 'The federated GraphQL API behind Hexagon GeoCloud (formerly HxDR / Reality Cloud Studio) for uploading, processing, organising, streaming and sharing reality-capture and geospatial data. 1,125 types, '
  name: Hexagon GeoCloud GraphQL API
  slug: geocloud-graphql
- description: A remote Model Context Protocol endpoint served from the Hexagon GeoCloud web property and discoverable through RFC 9728 protected-resource metadata and RFC 8414 authorization-server metadata on the s
  name: Hexagon GeoCloud MCP Server
  slug: geocloud-mcp
artifact_total: 15
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hexagon.com/hxmap/5.0.0/getting-started
- group: agent
  href: https://artifacts.apis.io/hexagon/agentic-access/hexagon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hexagon-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hexagon/rules/hexagon-rules.yml
  title: ''
  type: Spectral
  url: rules/hexagon-rules.yml
- group: design
  href: https://artifacts.apis.io/hexagon/vocabulary/hexagon-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hexagon-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/hexagon/hosts/hexagon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hexagon-hosts.yml
- group: build
  href: https://artifacts.apis.io/hexagon/integrations/hexagon-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hexagon-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/hexagon/vendors/hexagon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hexagon-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nexus.hexagon.com/developerportal
- group: operate
  title: ''
  type: Support
  url: https://geocloud.hexagon.com/contact-support/
- group: start
  title: ''
  type: SignUp
  url: https://geocloud.hexagon.com/free-demo/
- group: start
  title: ''
  type: Login
  url: https://geocloud.hxdr.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geocloud.hexagon.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hexagon.com/legal/privacy-notice
- group: operate
  href: https://artifacts.apis.io/hexagon/changelog/hexagon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hexagon-changelog.yml
- group: operate
  href: https://artifacts.apis.io/hexagon/lifecycle/hexagon-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/hexagon-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hexagon/lifecycle/hexagon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hexagon-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/hexagon/authentication/hexagon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hexagon-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hexagon/scopes/hexagon-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hexagon-scopes.yml
- group: agent
  href: https://artifacts.apis.io/hexagon/well-known/hexagon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hexagon-well-known.yml
- group: design
  href: https://artifacts.apis.io/hexagon/conformance/hexagon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hexagon-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://geocloud.hexagon.com/security-compliance/
- group: auth
  href: https://artifacts.apis.io/hexagon/security/hexagon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hexagon-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/hexagon/llms/hexagon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hexagon-llms.txt
- group: agent
  href: https://artifacts.apis.io/hexagon/mcp/hexagon-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hexagon-mcp.yml
- group: operate
  title: ''
  type: FAQ
  url: https://geocloud.hexagon.com/faq/
- group: agent
  href: https://artifacts.apis.io/hexagon/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hexagon-oss
- group: auth
  href: https://artifacts.apis.io/hexagon/security/hexagon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hexagon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hexagon.com
- group: docs
  title: ''
  type: Documentation
  url: https://nexus.hexagon.com/documentationcenter/en-US/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/hexagonab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hexagon-ab
- group: company
  title: ''
  type: Blog
  url: https://blog.manufacturing.hexagon.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hexagon.com/products/product-groups/nexus
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hxdr.app/
- group: other
  title: ''
  type: X
  url: https://x.com/hexagonab
- group: commercial
  href: https://artifacts.apis.io/hexagon/plans/hexagon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hexagon-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/hexagon/finops/hexagon-finops.yml
  title: ''
  type: FinOps
  url: finops/hexagon-finops.yml
created: '2026-06-13'
description: Hexagon is a global leader in digital reality solutions, combining sensor, software and autonomous technologies. Through the Nexus platform and product APIs, Hexagon delivers manufacturing intelligence capabilities spanning metrology, quality inspection, production monitoring, and digital factory solutions. The Nexus Developer Portal provides REST APIs authenticated via OAuth 2.0, enabling manufacturers and third-party developers to build connected, collaborative workflows integrating measurement data, quality processes, and industrial automation across the smart factory lifecycle.
finops:
- has_sources: true
  method: derived
  name: Hexagon Finops
  primary_unit: ''
  service_category: ''
  slug: hexagon-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hexagon.png
layout: provider
mcp_servers:
- description: Remote MCP server at geocloud.hexagon.com requiring OAuth.
  name: Hexagon GeoCloud MCP
  slug: hexagon-geocloud-mcp
modified: '2026-06-13'
name: Hexagon
nav: Providers
network: true
overview: 'Hexagon publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Nexus API, HxGN EAM REST API, and 3 more. Tagged areas include Manufacturing, Metrology, Quality Inspection, Digital Factory, and Production Monitoring.


  The Hexagon catalog on APIs.io includes 1 Spectral governance ruleset.


  Hexagon''s developer surface includes getting-started guide, support, signup flow, changelog, authentication, FAQ, documentation, and 31 more developer resources.'
plans:
- name: Hexagon Plans Pricing
  plan_count: 1
  slug: hexagon-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Hexagon Rate Limits
  slug: hexagon-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Hexagon API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: hexagon-rules
scopes:
- name: Hexagon Scopes
  scope_count: 18
  slug: hexagon-scopes
  summary_line: 18 scopes
score:
  band: strong
  composite: 58.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 81.6
    contract_governance: 35.6
    contract_quality: 46.1
    developer_ergonomics: 51.8
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hexagon/hexagon-2026-06-20T182709.png
security:
- kind: authentication
  name: Hexagon Authentication
  slug: hexagon-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hexagon Domain Security
  slug: hexagon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hexagon Trust Center
  slug: hexagon-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, CSA STAR Level 1
slug: hexagon
tags:
- Manufacturing
- Metrology
- Quality Inspection
- Digital Factory
- Production Monitoring
- Industrial IoT
- Smart Manufacturing
- Geospatial
website: https://hexagon.com
---
