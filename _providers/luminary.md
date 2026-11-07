---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Luminary Agentic Access
  operation_count: 31
  slug: luminary-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 1
apis:
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Documents API from Luminary — 8 operation(s) for documents.
  name: Luminary Documents API
  slug: luminary-documents-api
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Entities API from Luminary — 4 operation(s) for entities.
  name: Luminary Entities API
  slug: luminary-entities-api
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Households API from Luminary — 5 operation(s) for households.
  name: Luminary Households API
  slug: luminary-households-api
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Individuals API from Luminary — 3 operation(s) for individuals.
  name: Luminary Individuals API
  slug: luminary-individuals-api
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Users API from Luminary — 2 operation(s) for users.
  name: Luminary Users API
  slug: luminary-users-api
- baseURL: https://lum.withluminary.com/api/public/v1
  baseurl_source: declared
  description: The Valuations API from Luminary — 1 operation(s) for valuations.
  name: Luminary Valuations API
  slug: luminary-valuations-api
artifact_total: 23
collections:
- collection_type: open
  name: Luminary Documents API
  slug: open-luminary-documents-api
- collection_type: open
  name: Luminary Documents Entities API
  slug: open-luminary-entities-api
- collection_type: open
  name: Luminary Documents Households API
  slug: open-luminary-households-api
- collection_type: open
  name: Luminary Documents Individuals API
  slug: open-luminary-individuals-api
- collection_type: open
  name: Luminary Documents Users API
  slug: open-luminary-users-api
- collection_type: open
  name: Luminary Documents Valuations API
  slug: open-luminary-valuations-api
common:
- group: commercial
  href: https://artifacts.apis.io/luminary/plans/luminary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/luminary-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/luminary/overlays/luminary-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/luminary-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://withluminary.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withluminary
- group: company
  title: ''
  type: Blog
  url: https://withluminary.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://withluminary.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.withluminary.com
- group: operate
  title: ''
  type: Support
  url: https://withluminary.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withluminary.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withluminary.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://withluminary.com/security
- group: auth
  href: https://artifacts.apis.io/luminary/security/luminary-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/luminary-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/luminary/security/luminary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/luminary-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/luminary/authentication/luminary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/luminary-authentication.yml
- group: auth
  href: https://artifacts.apis.io/luminary/scopes/luminary-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/luminary-scopes.yml
- group: agent
  href: https://artifacts.apis.io/luminary/well-known/luminary-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/luminary-well-known.yml
- group: build
  href: https://artifacts.apis.io/luminary/packages/luminary-packages.yml
  title: ''
  type: Packages
  url: packages/luminary-packages.yml
- group: build
  href: https://artifacts.apis.io/luminary/packages/luminary-packages.yml
  title: ''
  type: SDKs
  url: packages/luminary-packages.yml
- group: agent
  href: https://artifacts.apis.io/luminary/mcp/luminary-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/luminary-mcp.yml
- group: agent
  href: https://artifacts.apis.io/luminary/llms/luminary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/luminary-llms.txt
- group: design
  href: https://artifacts.apis.io/luminary/conformance/luminary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/luminary-conformance.yml
- group: design
  href: https://artifacts.apis.io/luminary/errors/luminary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/luminary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/luminary/lifecycle/luminary-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/luminary-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/luminary/conventions/luminary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/luminary-conventions.yml
- group: design
  href: https://artifacts.apis.io/luminary/data-model/luminary-data-model.yml
  title: ''
  type: DataModel
  url: data-model/luminary-data-model.yml
- group: agent
  href: https://artifacts.apis.io/luminary/agentic-access/luminary-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/luminary-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/luminary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Luminary is AI-powered estate planning software for wealth advisors, family offices, attorneys, and professional services firms. It turns static estate planning documents into organized, digital records — with AI document digitization and summarization, dynamic estate flowcharts and waterfalls, scenario modeling, and role-based collaboration. Its public REST API (v1) exposes households, individuals, entities, documents, AI document summaries, and entity valuations so estate data can sync with CRMs, client portals, and planning tools. First-party TypeScript and Go SDKs are published on GitHub. OAuth2-secured (authorizationCode + clientCredentials) and SOC 2 Type II audited. Backed by 8vc.
finops:
- has_sources: true
  method: derived
  name: Luminary Finops
  primary_unit: ''
  service_category: ''
  slug: luminary-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luminary.png
layout: provider
modified: '2026-07-20'
name: Luminary
nav: Providers
network: true
overview: 'Luminary publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, Entities API, Households API, and 3 more. Tagged areas include Company, Estate Planning, Wealth Management, Financial Services, and Legal Tech.


  The Luminary catalog on APIs.io includes 1 Spectral governance ruleset.


  Luminary''s developer surface includes engineering blog, pricing, support, authentication, and 23 more developer resources.'
plans:
- name: Luminary Plans Pricing
  plan_count: 1
  slug: luminary-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Luminary API Rules
  rule_count: 60
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 4
  slug: luminary-rules
scopes:
- name: Luminary Scopes
  scope_count: 4
  slug: luminary-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 75.0
    contract_governance: 18.2
    contract_quality: 49.3
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/luminary/luminary-2026-07-25T225714.png
security:
- kind: authentication
  name: Luminary Authentication
  slug: luminary-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Luminary Domain Security
  slug: luminary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Luminary Trust Center
  slug: luminary-trust-center
  summary_line: SOC 2
skill_count: 3
skills:
- name: Ingest a document and retrieve its AI summary
  slug: luminary-document-summaries
- name: Value an estate entity
  slug: luminary-entity-valuation
- name: Onboard an estate-planning household
  slug: luminary-onboard-household
slug: luminary
tags:
- Company
- Estate Planning
- Wealth Management
- Financial Services
- Legal Tech
- Document AI
- Family Office
- OAuth
- Authentication
website: https://withluminary.com
---
