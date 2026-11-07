---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Document360 Agentic Access
  operation_count: 15
  slug: document360-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Articles API from Document360 — 2 operation(s) for articles.
  name: Document360 Articles API
  slug: document360-articles-api
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Categories API from Document360 — 2 operation(s) for categories.
  name: Document360 Categories API
  slug: document360-categories-api
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Drive API from Document360 — 2 operation(s) for drive.
  name: Document360 Drive API
  slug: document360-drive-api
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Project Versions API from Document360 — 1 operation(s) for project versions.
  name: Document360 Project Versions API
  slug: document360-project-versions-api
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Teams API from Document360 — 1 operation(s) for teams.
  name: Document360 Teams API
  slug: document360-teams-api
- baseURL: https://apihub.document360.io/v2
  baseurl_source: declared
  description: The Users API from Document360 — 1 operation(s) for users.
  name: Document360 Users API
  slug: document360-users-api
artifact_total: 31
collections:
- collection_type: postman
  name: Document360 Articles API
  slug: postman-document360-articles-api
- collection_type: postman
  name: Document360 Articles Categories API
  slug: postman-document360-categories-api
- collection_type: postman
  name: Document360 Articles Drive API
  slug: postman-document360-drive-api
- collection_type: postman
  name: Document360 Articles Project Versions API
  slug: postman-document360-project-versions-api
- collection_type: postman
  name: Document360 Articles Teams API
  slug: postman-document360-teams-api
- collection_type: postman
  name: Document360 Articles Users API
  slug: postman-document360-users-api
- collection_type: open
  name: Document360 Articles API
  slug: open-document360-articles-api
- collection_type: open
  name: Document360 Articles Categories API
  slug: open-document360-categories-api
- collection_type: open
  name: Document360 API
  slug: open-document360-document360-api
- collection_type: open
  name: Document360 Articles Drive API
  slug: open-document360-drive-api
- collection_type: open
  name: Document360 Articles Project Versions API
  slug: open-document360-project-versions-api
- collection_type: open
  name: Document360 Articles Teams API
  slug: open-document360-teams-api
- collection_type: open
  name: Document360 Articles Users API
  slug: open-document360-users-api
common:
- group: design
  href: https://artifacts.apis.io/document360/rules/document360-rules.yml
  title: ''
  type: Spectral
  url: rules/document360-rules.yml
- group: design
  href: https://artifacts.apis.io/document360/rules/document360-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/document360-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/document360/vocabulary/document360-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/document360-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/document360/data-model/document360-data-model.yml
  title: ''
  type: DataModel
  url: data-model/document360-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://document360.com/compliance/soc2/
- group: design
  href: https://artifacts.apis.io/document360/conformance/document360-conformance.yml
  title: ''
  type: Conformance
  url: conformance/document360-conformance.yml
- group: agent
  href: https://artifacts.apis.io/document360/llms/document360-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/document360-llms.txt
- group: agent
  href: https://artifacts.apis.io/document360/mcp/document360-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/document360-mcp.yml
- group: agent
  href: https://artifacts.apis.io/document360/well-known/document360-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/document360-well-known.yml
- group: other
  href: https://artifacts.apis.io/document360/hosts/document360-hosts.yml
  title: ''
  type: Hosts
  url: hosts/document360-hosts.yml
- group: build
  href: https://artifacts.apis.io/document360/integrations/document360-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/document360-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/document360/vendors/document360-vendors.yml
  title: ''
  type: Vendors
  url: vendors/document360-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.document360.com/
- group: start
  title: ''
  type: SignUp
  url: https://document360.com/signup/
- group: auth
  title: ''
  type: Security
  url: https://document360.com/security/
- group: other
  title: ''
  type: Leadership
  url: https://document360.com/solutions/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.document360.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://document360.com/blog/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.document360.com/apidocs
- group: commercial
  href: https://artifacts.apis.io/document360/plans/document360-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/document360-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/document360/rate-limits/document360-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/document360-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/document360/finops/document360-finops.yml
  title: ''
  type: FinOps
  url: finops/document360-finops.yml
- group: other
  href: https://artifacts.apis.io/document360/capabilities/document360-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/document360-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.document360.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/document360/overview
- group: agent
  href: https://artifacts.apis.io/document360/agentic-access/document360-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/document360-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/document360/security/document360-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/document360-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/document360/security/document360-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/document360-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/document360/authentication/document360-authentication.yml
  title: ''
  type: Authentication
  url: authentication/document360-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/document360
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/document360
- group: start
  title: ''
  type: Portal
  url: https://document360.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.document360.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://document360.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://document360.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://document360.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.document360.com/
created: '2026-03-16'
description: Document360 is a SaaS knowledge base platform that allows teams to create, manage, and publish self-service knowledge bases and documentation portals. It supports version control, categories, team collaboration, analytics, and an API for integrating documentation into external workflows.
finops:
- has_sources: false
  method: generated
  name: Document360 Finops
  primary_unit: request
  service_category: API
  slug: document360-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/document360.png
json_schemas:
- name: Document360 Article
  property_count: 11
  slug: document360-article
- name: Document360 Category
  property_count: 5
  slug: document360-category
jsonld:
- class_count: 31
  name: Document360 Context
  property_count: 0
  slug: document360-context
layout: provider
mcp_servers:
- description: Document360 publishes an MCP server card at https://document360.com/.well-known/mcp.json (saved verbatim as document360-mcp-server-card.json). It advertises the Document360 MCP Server, streamable HTTP
  name: Document360 MCP Server
  slug: document360-mcp-yml
modified: '2026-05-19'
name: Document360
nav: Providers
network: true
overview: 'Document360 publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Articles API, Categories API, Drive API, and 3 more. Tagged areas include Documentation, Knowledge Base, Software-as-a-Service, Knowledge Management, and API Documentation.


  The Document360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Document360''s developer surface includes signup flow, getting-started guide, changelog, API reference, authentication, developer portal, documentation, and 30 more developer resources.'
plans:
- name: Document360 Plans Pricing
  plan_count: 3
  slug: document360-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Document360 Rate Limits
  slug: document360-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Document360 — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: document360-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 63.3
    catalog_earned_first_party: 0.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 46.4
    discoverability: 69.2
    operational_transparency: 31.6
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/document360/document360-2026-06-20T180118.png
security:
- kind: authentication
  name: Document360 Authentication
  slug: document360-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Document360 Domain Security
  slug: document360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Document360 Trust Center
  slug: document360-trust-center
  summary_line: SOC 2
slug: document360
tags:
- Documentation
- Knowledge Base
- Software-as-a-Service
- Knowledge Management
- API Documentation
- Developer Portal
website: https://www.document360.com/
---
