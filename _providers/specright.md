---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'REST API over Specright''s specification data. Forty-six operations across six areas: token issuance, specifications, spec families (BOM / finished good), suppliers, a generic /objects/{api-name} endpo'
  name: Specright API
  slug: specright-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.specright.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.specright.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.specright.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.specright.com/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.specright.com/plans-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.specright.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.specright.com/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.specright.com/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://www.specright.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.specright.com/feed/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.specright.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/specright-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/specright-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/specright-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/specright-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/specright-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/specright-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/specright-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/specright-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/specright-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/specright-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/specright-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/specright-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/specright-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/specright-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/specright-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/specright-domain-security.yml
created: '2026-08-28'
description: 'Specright is a specification data management (SDM) platform that centralizes the specifications behind a physical product — raw materials, ingredients, formulas, packaging components, finished goods and the bills of materials that connect them — and shares them across a company''s suppliers, co-manufacturers and internal teams. Founded in 2015 and headquartered in Tustin, California, the platform is built on Salesforce, which surfaces directly in its API: records are addressed by Salesforce IDs or by a configurable external ID, and field names carry the specright__*__c managed-package prefix. Specright publishes a REST API at api.specright.com/v1 covering specifications, spec families, suppliers, a generic object endpoint that reaches any configured Specright object, file retrieval and asynchronous CSV bulk jobs, documented through a developer portal at developer.specright.com. It also serves an OAuth-protected Model Context Protocol endpoint from its marketing site.'
image: https://www.specright.com/wp-content/uploads/2026/04/AI-Specright-1-scaled.png
layout: provider
mcp_servers:
- description: Specright serves two live Model Context Protocol endpoints from the WordPress REST API behind its marketing site, www.specright.com. Both were discovered from the site's own RFC 9728 protected-resourc
  name: Specright MCP server
  slug: specright-mcp-server
modified: '2026-08-28'
name: Specright
nav: Providers
network: true
overview: 'Specright publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Specification Management, Supply Chain, Packaging, and Product Lifecycle Management.


  Specright''s developer surface includes documentation, API reference, pricing, support, engineering blog, authentication, changelog, and 21 more developer resources.'
plans:
- name: Specright Plans Pricing
  plan_count: 3
  slug: specright-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Specright Rate Limits
  slug: specright-rate-limits
scopes:
- name: Specright Scopes
  scope_count: 0
  slug: specright-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 31.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/specright/refs/heads/main/screenshots/specright-2026-09-02T160357.png
security:
- kind: authentication
  name: Specright Authentication
  slug: specright-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Specright Domain Security
  slug: specright-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: specright
tags:
- Company
- Specification Management
- Supply Chain
- Packaging
- Product Lifecycle Management
- Manufacturing
- Sustainability
- Supplier Collaboration
- Bill of Materials
- Salesforce
- Enterprise Software
website: https://www.specright.com/
---
