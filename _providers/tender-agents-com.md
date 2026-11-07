---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Tender Agents Com Agentic Access
  operation_count: 45
  slug: tender-agents-com-agentic-access
  summary_line: 45 operations · 19 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The agent-discovery API from tender-agents-com — 7 operation(s) for agent-discovery.
  name: tender-agents-com Agent Discovery API
  slug: tender-agents-com-agent-discovery-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The erp-export API from tender-agents-com — 2 operation(s) for erp-export.
  name: tender-agents-com ERP Export API
  slug: tender-agents-com-erp-export-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The gaeb API from tender-agents-com — 2 operation(s) for gaeb.
  name: tender-agents-com Gaeb API
  slug: tender-agents-com-gaeb-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The keys API from tender-agents-com — 2 operation(s) for keys.
  name: tender-agents-com Keys API
  slug: tender-agents-com-keys-api
- baseURL: https://www.tender-agents.com
  baseurl_source: declared
  description: The mcp API from tender-agents-com — 2 operation(s) for mcp.
  name: tender-agents-com MCP API
  slug: tender-agents-com-mcp-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The oauth API from tender-agents-com — 3 operation(s) for oauth.
  name: tender-agents-com OAuth API
  slug: tender-agents-com-oauth-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The profiles API from tender-agents-com — 8 operation(s) for profiles.
  name: tender-agents-com Profiles API
  slug: tender-agents-com-profiles-api
- baseURL: https://www.tender-agents.com
  baseurl_source: declared
  description: The signup API from tender-agents-com — 2 operation(s) for signup.
  name: tender-agents-com Signup API
  slug: tender-agents-com-signup-api
- baseURL: https://www.tender-agents.com
  baseurl_source: declared
  description: The Source Status API from tender-agents-com — 1 operation(s) for source status.
  name: tender-agents-com Source Status API
  slug: tender-agents-com-source-status-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The tenders API from tender-agents-com — 10 operation(s) for tenders.
  name: tender-agents-com Tenders API
  slug: tender-agents-com-tenders-api
- baseURL: https://www.tender-agents.com
  baseurl_source: declared
  description: The Tenders Public API from tender-agents-com — 1 operation(s) for tenders public.
  name: tender-agents-com Tenders Public API
  slug: tender-agents-com-tenders-public-api
- baseURL: https://app.tender-agents.com
  baseurl_source: declared
  description: The webhooks API from tender-agents-com — 2 operation(s) for webhooks.
  name: tender-agents-com Webhooks API
  slug: tender-agents-com-webhooks-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/tender-agents-com/agentic-access/tender-agents-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tender-agents-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tender-agents-com/rate-limits/tender-agents-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tender-agents-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tender-agents-com/plans/tender-agents-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tender-agents-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tender-agents-com/rules/tender-agents-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tender-agents-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tender-agents-com/json-ld/tender-agents-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tender-agents-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tender-agents-com/vocabulary/tender-agents-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tender-agents-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tender-agents-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tender-agents-com/data-model/tender-agents-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tender-agents-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tender-agents-com/authentication/tender-agents-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tender-agents-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/tender-agents-com/errors/tender-agents-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tender-agents-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tender-agents-com/conformance/tender-agents-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tender-agents-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tender-agents-com/llms/tender-agents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tender-agents-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tender-agents-com/a2a/tender-agents-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tender-agents-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tender-agents-com/well-known/tender-agents-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tender-agents-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/tender-agents-com/hosts/tender-agents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tender-agents-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tender-agents-com/vendors/tender-agents-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tender-agents-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/tender-agents-com/packages/tender-agents-com-packages.yml
  title: ''
  type: SDKs
  url: packages/tender-agents-com-packages.yml
- group: build
  href: https://artifacts.apis.io/tender-agents-com/packages/tender-agents-com-packages.yml
  title: ''
  type: Packages
  url: packages/tender-agents-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.tender-agents.com/status
- group: start
  title: ''
  type: Login
  url: https://www.tender-agents.com/login
- group: auth
  href: https://artifacts.apis.io/tender-agents-com/scopes/tender-agents-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tender-agents-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/tender-agents-com/security/tender-agents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tender-agents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tender-agents.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tender-agents.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.tender-agents.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.tender-agents.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tender-agents.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tender-agents.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tender-agents.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tender-agents.com/privacy
created: '2026-10-31'
description: Tender Agents offers an API‑first platform that aggregates EU public procurement notices from the TED database across 27 member states. Users can search free previews of tenders, retrieve structured JSON, CSV or XLSX exports, and integrate with AI agents via a public JSON API, MCP endpoint, and A2A JSON‑RPC. Paid plans provide full access, pricing details are listed on the site, and the service supports German GAEB XML formats. The platform emphasizes transparency, open data, and detailed documentation for developers.
image: https://www.tender-agents.com/og-image.png
json_schemas:
- name: CompanyProfileCreatedOut
  property_count: 42
  slug: tender-agents-com-company-profile-created-out
- name: CompanyProfileIn
  property_count: 36
  slug: tender-agents-com-company-profile-in
- name: CompanyProfileOut
  property_count: 40
  slug: tender-agents-com-company-profile-out
- name: CompanyTenderMatchOut
  property_count: 13
  slug: tender-agents-com-company-tender-match-out
- name: PublicTenderOut
  property_count: 27
  slug: tender-agents-com-public-tender-out
- name: SourceStatus
  property_count: 6
  slug: tender-agents-com-source-status
- name: TenderOut
  property_count: 30
  slug: tender-agents-com-tender-out
- name: Tender
  property_count: 13
  slug: tender-agents-com-tender
jsonld:
- class_count: 33
  name: Tender Agents Com Context
  property_count: 166
  slug: tender-agents-com-context
layout: provider
modified: '2026-10-31'
name: tender-agents-com
nav: Providers
network: true
overview: 'tender-agents-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Discovery API, ERP Export API, Gaeb API, and 9 more. Tagged areas include EU, Procurement, Tenders, Artificial Intelligence, and Public Data.


  The tender-agents-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tender-agents-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 25 more developer resources.'
plans:
- name: Tender Agents Com Plans Pricing
  plan_count: 4
  slug: tender-agents-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Tender Agents Com Rate Limits
  slug: tender-agents-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: tender-agents-com API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 4
  slug: tender-agents-com-rules
scopes:
- name: Tender Agents Com Scopes
  scope_count: 4
  slug: tender-agents-com-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 55.3
    developer_ergonomics: 44.5
    discoverability: 71.4
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 36.4
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tender-agents-com/tender-agents-com-2026-11-03T144431.png
security:
- kind: authentication
  name: Tender Agents Com Authentication
  slug: tender-agents-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tender Agents Com Domain Security
  slug: tender-agents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: public-tenders-search
  slug: tender-agents-com-public-tenders-search
slug: tender-agents-com
tags:
- EU
- Procurement
- Tenders
- Artificial Intelligence
- Public Data
website: https://tender-agents.com/
---
