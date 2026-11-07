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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Anycutlist Com Agentic Access
  operation_count: 42
  slug: anycutlist-com-agentic-access
  summary_line: 42 operations · 23 acting
api_count: 1
apis:
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Assembly Templates API from AnyCutlist — 3 operation(s) for assembly templates.
  name: AnyCutlist Assembly Templates API
  slug: anycutlist-com-assembly-templates-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Cutlists API from AnyCutlist — 5 operation(s) for cutlists.
  name: AnyCutlist Cutlists API
  slug: anycutlist-com-cutlists-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Exports API from AnyCutlist — 3 operation(s) for exports.
  name: AnyCutlist Exports API
  slug: anycutlist-com-exports-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Files API from AnyCutlist — 2 operation(s) for files.
  name: AnyCutlist Files API
  slug: anycutlist-com-files-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Materials API from AnyCutlist — 2 operation(s) for materials.
  name: AnyCutlist Materials API
  slug: anycutlist-com-materials-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Optimize API from AnyCutlist — 3 operation(s) for optimize.
  name: AnyCutlist Optimize API
  slug: anycutlist-com-optimize-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Optimize Jobs API from AnyCutlist — 2 operation(s) for optimize jobs.
  name: AnyCutlist Optimize Jobs API
  slug: anycutlist-com-optimize-jobs-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Parse API from AnyCutlist — 1 operation(s) for parse.
  name: AnyCutlist Parse API
  slug: anycutlist-com-parse-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Parse File API from AnyCutlist — 1 operation(s) for parse file.
  name: AnyCutlist Parse File API
  slug: anycutlist-com-parse-file-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Parse Jobs API from AnyCutlist — 2 operation(s) for parse jobs.
  name: AnyCutlist Parse Jobs API
  slug: anycutlist-com-parse-jobs-api
- baseURL: https://www.anycutlist.com/api/v1
  baseurl_source: declared
  description: The Parse Text API from AnyCutlist — 1 operation(s) for parse text.
  name: AnyCutlist Parse Text API
  slug: anycutlist-com-parse-text-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/anycutlist-com/agentic-access/anycutlist-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anycutlist-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/anycutlist-com/plans/anycutlist-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anycutlist-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anycutlist-com/rules/anycutlist-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anycutlist-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/anycutlist-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/security/anycutlist-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/anycutlist-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/authentication/anycutlist-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anycutlist-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/anycutlist-com/errors/anycutlist-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anycutlist-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anycutlist-com/conformance/anycutlist-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anycutlist-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anycutlist-com/llms/anycutlist-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anycutlist-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/well-known/anycutlist-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anycutlist-com-security.txt
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/well-known/anycutlist-com-anycutlist-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anycutlist-com-anycutlist-security.txt
- group: agent
  href: https://artifacts.apis.io/anycutlist-com/well-known/anycutlist-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anycutlist-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anycutlist-com/hosts/anycutlist-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anycutlist-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anycutlist-com/vendors/anycutlist-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anycutlist-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anycutlist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anycutlist.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anycutlist.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.anycutlist.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.anycutlist.com/blog
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/security/anycutlist-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anycutlist-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anycutlist-com/security/anycutlist-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anycutlist-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anycutlist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anycutlist.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.anycutlist.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.anycutlist.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.anycutlist.com/docs
- group: operate
  title: ''
  type: Support
  url: mailto:admin@positivesocialdigital.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://anycutlist.com/openapi.json
  - status: null
    url: https://www.anycutlist.com/openapi.json
  - status: 401
    url: https://www.anycutlist.com/api/mcp
  - status: 200
    url: https://anycutlist.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AnyCutlist provides AI-powered cutlist software for cut-and-edge shops and cabinet makers, built in Kenya. It converts handwritten, photo, PDF, Excel, and 3D model cutting lists into checked parts, priced quotes, and MaxCut-ready files. Features include OCR, edge-banding notation, sheet optimization, Zoho Books integration, and an MCP server for AI assistants.
image: https://www.anycutlist.com/branding/icon-512.png
layout: provider
modified: '2026-11-01'
name: AnyCutlist
nav: Providers
network: true
overview: 'AnyCutlist publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assembly Templates API, Cutlists API, Exports API, and 8 more. Tagged areas include Artificial Intelligence, Manufacturing, Cutlist, Kenya, and Software.


  The AnyCutlist catalog on APIs.io includes 1 Spectral governance ruleset.


  AnyCutlist''s developer surface includes authentication, pricing, engineering blog, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
plans:
- name: Anycutlist Com Plans Pricing
  plan_count: 4
  slug: anycutlist-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Anycutlist Com Rate Limits
  slug: anycutlist-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AnyCutlist API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: anycutlist-com-rules
scopes:
- name: Anycutlist Com Scopes
  scope_count: 0
  slug: anycutlist-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 48.4
    developer_ergonomics: 43.3
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - kenya
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anycutlist Com Authentication
  slug: anycutlist-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Anycutlist Com Domain Security
  slug: anycutlist-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anycutlist Com Vulnerability Disclosure
  slug: anycutlist-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: parse-text
  slug: anycutlist-com-parse-text-skill
slug: anycutlist-com
tags:
- Artificial Intelligence
- Manufacturing
- Cutlist
- Kenya
- Software
website: https://anycutlist.com/
---
