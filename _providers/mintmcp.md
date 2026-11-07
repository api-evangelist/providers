---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.mintmcp.com
  baseurl_source: declared
  description: 'MintMCP API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: MintMCP API
  slug: mintmcp-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/mintmcp/well-known/mintmcp-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mintmcp-status-security.txt
- group: company
  title: ''
  type: Newsroom
  url: https://www.mintive.com/media
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mintmcp.com/docs/quickstart
- group: design
  href: https://artifacts.apis.io/mintmcp/rules/mintmcp-rules.yml
  title: ''
  type: Spectral
  url: rules/mintmcp-rules.yml
- group: design
  href: https://artifacts.apis.io/mintmcp/json-ld/mintmcp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mintmcp-context.jsonld
- group: design
  href: https://artifacts.apis.io/mintmcp/vocabulary/mintmcp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mintmcp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mintmcp/data-model/mintmcp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mintmcp-data-model.yml
- group: build
  href: https://artifacts.apis.io/mintmcp/cli/mintmcp-cli.yml
  title: ''
  type: CLI
  url: cli/mintmcp-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mintmcp.com/
- group: auth
  href: https://artifacts.apis.io/mintmcp/authentication/mintmcp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mintmcp-authentication.yml
- group: design
  href: https://artifacts.apis.io/mintmcp/conformance/mintmcp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mintmcp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mintmcp/llms/mintmcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mintmcp-llms.txt
- group: agent
  href: https://artifacts.apis.io/mintmcp/well-known/mintmcp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mintmcp-well-known.yml
- group: other
  href: https://artifacts.apis.io/mintmcp/hosts/mintmcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mintmcp-hosts.yml
- group: other
  href: https://artifacts.apis.io/mintmcp/vendors/mintmcp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mintmcp-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mintmcp.com/
- group: auth
  href: https://artifacts.apis.io/mintmcp/security/mintmcp-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mintmcp-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mintmcp/security/mintmcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mintmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mintmcp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.mintmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mintmcp.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://www.mintmcp.com/docs/intro
- group: operate
  title: ''
  type: Support
  url: https://www.mintmcp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.mintmcp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mintmcp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mintmcp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mintmcp.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mintmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mintmcp.com/privacy
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found at known endpoints.
  evidence:
  - status: 0
    url: https://api.mintmcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: MintMCP, now operating as Mintive, provides an MCP Gateway and AI Agent Infrastructure platform. It enables teams to integrate AI agents with controlled access to tools, models, and data, offering role‑based governance, security monitoring, and audit logging. The platform supports a wide range of enterprise tools and services, delivering unified access, policy enforcement, and detailed usage analytics for AI‑driven workflows.
image: https://www.mintmcp.com/og-image-mintive.png
json_schemas:
- name: GetApiAdminV1McpActivitySummaryResponse
  property_count: 6
  slug: mintmcp-get-api-admin-v1-mcp-activity-summary-response
- name: GetApiAdminV1McpActivityUsersResponse
  property_count: 3
  slug: mintmcp-get-api-admin-v1-mcp-activity-users-response
- name: GetApiAdminV1OrganizationsMeResponse
  property_count: 1
  slug: mintmcp-get-api-admin-v1-organizations-me-response
jsonld:
- class_count: 3
  name: Mintmcp Context
  property_count: 9
  slug: mintmcp-context
layout: provider
modified: '2026-10-18'
name: MintMCP
nav: Providers
network: true
overview: 'MintMCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Enterprise, Security, and Integration.


  The MintMCP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MintMCP''s developer surface includes getting-started guide, CLI, authentication, documentation, API reference, support, engineering blog, and 22 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: MintMCP API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: mintmcp-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 41.7
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 46.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mintmcp/mintmcp-2026-11-03T135654.png
security:
- kind: authentication
  name: Mintmcp Authentication
  slug: mintmcp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mintmcp Domain Security
  slug: mintmcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mintmcp Trust Center
  slug: mintmcp-trust-center
  summary_line: SOC 2, HIPAA
slug: mintmcp
tags:
- Artificial Intelligence
- Platform
- Enterprise
- Security
- Integration
website: https://www.mintmcp.com/
---
