---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: 'REST API of the Keysight CyPerf controller for managing agents, sessions, configurations, test execution, results, licensing and certificates. The API runs on each customer-deployed CyPerf controller '
  name: Keysight CyPerf REST API
  slug: cyperf-rest-api
- description: Experimental local (stdio) Model Context Protocol server published by Keysight that wraps the cyperf Python SDK as 100 tools across 15 categories for driving a CyPerf controller from an AI assistant.
  name: Keysight CyPerf MCP Server
  slug: cyperf-mcp
- description: 'Keysight Technologies API as documented publicly: 96 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: Keysight Technologies API
  slug: keysight-technologies-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/keysight-technologies/rules/keysight-technologies-rules.yml
  title: ''
  type: Spectral
  url: rules/keysight-technologies-rules.yml
- group: design
  href: https://artifacts.apis.io/keysight-technologies/vocabulary/keysight-technologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/keysight-technologies-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/keysight-technologies/authentication/keysight-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keysight-technologies-authentication.yml
- group: auth
  href: https://artifacts.apis.io/keysight-technologies/scopes/keysight-technologies-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/keysight-technologies-scopes.yml
- group: design
  href: https://artifacts.apis.io/keysight-technologies/conformance/keysight-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keysight-technologies-conformance.yml
- group: build
  href: https://artifacts.apis.io/keysight-technologies/mcp/keysight-technologies-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/keysight-technologies-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/keysight-technologies/mcp/keysight-technologies-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/keysight-technologies-mcp.yml
- group: other
  href: https://artifacts.apis.io/keysight-technologies/hosts/keysight-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keysight-technologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/keysight-technologies/vendors/keysight-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keysight-technologies-vendors.yml
- group: build
  href: https://artifacts.apis.io/keysight-technologies/packages/keysight-technologies-packages.yml
  title: ''
  type: SDKs
  url: packages/keysight-technologies-packages.yml
- group: build
  href: https://artifacts.apis.io/keysight-technologies/packages/keysight-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/keysight-technologies-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keysight.com/us/en/contact/terms-of-use.html
- group: operate
  title: ''
  type: Support
  url: https://support.keysight.com/s/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keysight.com/us/en/contact/privacy.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.keysight.com/go/news
- group: auth
  href: https://artifacts.apis.io/keysight-technologies/security/keysight-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keysight-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.keysight.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keysight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keysight-technologies
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Keysight/cyperf-api-wrapper
created: '2026-05-05'
description: 'Keysight Technologies is an electronic design, emulation and test company (Fortune 1000, rank 617). Its developer surface is product-side: the CyPerf network performance and security test platform exposes a REST API (/api/v2, OAuth2/OpenID Connect via a Keycloak ''keysight'' realm) on each self-hosted or cloud controller, with an official generated Python SDK (cyperf on PyPI) and an experimental local stdio MCP server (cyperf-mcp, 100 tools). Keysight also publishes ixnetwork-restpy and snappi client libraries and Terraform modules for its virtual test products on GitHub.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keysight-technologies.png
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 100 tools listed.
  name: Keysight CyPerf MCP Server
  slug: keysight-cyperf-mcp-server
modified: '2026-10-19'
name: Keysight Technologies
nav: Providers
network: true
overview: 'Keysight Technologies is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Network Testing, Test and Measurement, Performance Testing, Security Testing, and Electronics.


  The Keysight Technologies catalog on APIs.io includes 1 Spectral governance ruleset.


  Keysight Technologies'' developer surface includes authentication, support, and 18 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Keysight Technologies Rate Limits
  slug: keysight-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Keysight Technologies API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: keysight-technologies-rules
scopes:
- name: Keysight Technologies Scopes
  scope_count: 2
  slug: keysight-technologies-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 7.8
    developer_ergonomics: 33.3
    discoverability: 63.3
    operational_transparency: 5.3
  previous_composite: 25.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/keysight-technologies/keysight-technologies-2026-06-20T184023.png
security:
- kind: authentication
  name: Keysight Technologies Authentication
  slug: keysight-technologies-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Keysight Technologies Domain Security
  slug: keysight-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keysight-technologies
tags:
- Network Testing
- Test and Measurement
- Performance Testing
- Security Testing
- Electronics
- Traffic Generation
- MCP
website: https://www.keysight.com
---
