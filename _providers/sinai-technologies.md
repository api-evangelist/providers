---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - '{''url'': ''https://sinaitechnologies.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.sinai.com/ — a different registrable domain (sinaitechnologies.com -> sinai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.sinai.com/v1
  baseurl_source: declared
  description: The Baseline forecasts API from Sinai Technologies — 7 operation(s) for baseline forecasts.
  name: Sinai Technologies Baseline forecasts API
  slug: sinai-technologies-baseline-forecasts-api
- baseURL: https://api.sinai.com/v1
  baseurl_source: declared
  description: The Carbon accounting API from Sinai Technologies — 5 operation(s) for carbon accounting.
  name: Sinai Technologies Carbon accounting API
  slug: sinai-technologies-carbon-accounting-api
- baseURL: https://api.sinai.com/v1
  baseurl_source: declared
  description: The Organization management API from Sinai Technologies — 20 operation(s) for organization management.
  name: Sinai Technologies Organization management API
  slug: sinai-technologies-organization-management-api
artifact_total: 14
collections:
- collection_type: open
  name: SINAI Baseline forecasts API
  slug: open-sinai-technologies-baseline-forecasts-api
- collection_type: open
  name: SINAI Baseline forecasts Carbon accounting API
  slug: open-sinai-technologies-carbon-accounting-api
- collection_type: open
  name: SINAI Baseline forecasts Organization management API
  slug: open-sinai-technologies-organization-management-api
common:
- group: other
  href: https://artifacts.apis.io/sinai-technologies/capabilities/sinai-technologies-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sinai-technologies-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/sinai-technologies/security/sinai-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sinai-technologies-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sinai-technologies/authentication/sinai-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sinai-technologies-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sinai-technologies/scopes/sinai-technologies-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sinai-technologies-scopes.yml
- group: design
  href: https://artifacts.apis.io/sinai-technologies/conventions/sinai-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sinai-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/sinai-technologies/errors/sinai-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sinai-technologies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sinai-technologies/conformance/sinai-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sinai-technologies-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sinai.com/resources/security-practices
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sinai.com/
- group: design
  href: https://artifacts.apis.io/sinai-technologies/lifecycle/sinai-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sinai-technologies-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sinai-technologies/data-model/sinai-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sinai-technologies-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sinai-technologies/mcp/sinai-technologies-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sinai-technologies-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sinai-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/sinai-technologies/overlays/sinai-technologies-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sinai-technologies-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sinai-technologies/llms/sinai-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sinai-technologies-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sinai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sinai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.sinai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sinai.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.sinai.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.sinai.com/resources/blog
- group: start
  title: ''
  type: Login
  url: https://app.sinai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iubenda.com/terms-and-conditions/57352437
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/57352437
- group: company
  title: ''
  type: Website
  url: https://sinaitechnologies.com
created: '2026-07-17'
description: SINAI (Sinai Technologies, Inc.) is an AI-powered enterprise carbon management and sustainability platform for measuring, reducing, and reporting greenhouse-gas emissions. Its HTTP API uses OAuth 2.0 and exposes carbon accounting, the organization / business-entity hierarchy, emissions sources and models, industry taxonomy, activity periods, and baseline forecasts for decarbonization planning. SINAI supports audit-ready reporting for frameworks including CSRD, CBAM, California SB 253/261, and Brazil CVM/SBCE.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sinai-technologies.png
layout: provider
modified: '2026-07-21'
name: Sinai Technologies
nav: Providers
network: true
overview: 'Sinai Technologies publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Baseline forecasts API, Carbon accounting API, and Organization management API. Tagged areas include Company, Carbon Management, Carbon Accounting, Emissions, and Sustainability.


  The Sinai Technologies catalog on APIs.io includes 1 Spectral governance ruleset.


  Sinai Technologies'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Sinai Technologies API Rules
  rule_count: 65
  severity_counts:
    error: 55
    hint: 0
    info: 3
    warn: 7
  slug: sinai-technologies-rules
scopes:
- name: Sinai Technologies Scopes
  scope_count: 6
  slug: sinai-technologies-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 57.2
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 44.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
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
    score: 0.0
screenshot: https://apis.io/screenshots/sinai-technologies/sinai-technologies-2026-08-17T081904.png
security:
- kind: authentication
  name: Sinai Technologies Authentication
  slug: sinai-technologies-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Sinai Technologies Domain Security
  slug: sinai-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sinai Technologies Trust Center
  slug: sinai-technologies-trust-center
  summary_line: SOC 2 Type 2
skill_count: 3
skills:
- name: Configure emissions sources and read monthly emissions
  slug: sinai-technologies-manage-emissions-sources
- name: Map an organization's carbon-accounting hierarchy
  slug: sinai-technologies-map-organization
- name: Read baseline forecasts and decarbonization projections
  slug: sinai-technologies-read-baseline-forecasts
slug: sinai-technologies
tags:
- Company
- Carbon Management
- Carbon Accounting
- Emissions
- Sustainability
- ESG
- Decarbonization
- Climate
website: https://sinaitechnologies.com
---
