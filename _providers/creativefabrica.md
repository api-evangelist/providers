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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Creativefabrica Agentic Access
  operation_count: 10
  slug: creativefabrica-agentic-access
  summary_line: 10 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Official remote Model Context Protocol server for idea.ai (Creative Fabrica B.V.), advertised at https://www.idea.ai/mcp and at the Cursor plugin manifest github.com/creativefabrica/idea-ai-mcp-plugin
  name: idea.ai MCP Server
  slug: idea-ai-mcp-server
- baseURL: https://api.idea.ai/genai
  baseurl_source: declared
  description: Create and track generations
  name: Creative Fabrica Generations API
  slug: creativefabrica-generations-api
- baseURL: https://api.idea.ai/genai
  baseurl_source: declared
  description: Model catalog and capabilities
  name: Creative Fabrica Models API
  slug: creativefabrica-models-api
- baseURL: https://api.idea.ai/genai
  baseurl_source: declared
  description: Ready-made tools with a server-side prompt and output contract
  name: Creative Fabrica Presets API
  slug: creativefabrica-presets-api
- baseURL: https://api.idea.ai/genai
  baseurl_source: declared
  description: Selectable voices for speech models
  name: Creative Fabrica Voices API
  slug: creativefabrica-voices-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/creativefabrica/agentic-access/creativefabrica-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/creativefabrica-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/creativefabrica/plans/creativefabrica-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creativefabrica-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/rules/creativefabrica-rules.yml
  title: ''
  type: Spectral
  url: rules/creativefabrica-rules.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/json-ld/creativefabrica-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creativefabrica-context.jsonld
- group: design
  href: https://artifacts.apis.io/creativefabrica/vocabulary/creativefabrica-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creativefabrica-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/creativefabrica/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/data-model/creativefabrica-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creativefabrica-data-model.yml
- group: start
  href: https://artifacts.apis.io/creativefabrica/sandbox/creativefabrica-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/creativefabrica-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/creativefabrica/scopes/creativefabrica-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/creativefabrica-scopes.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/lifecycle/creativefabrica-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/creativefabrica-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/errors/creativefabrica-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/creativefabrica-problem-types.yml
- group: design
  href: https://artifacts.apis.io/creativefabrica/conformance/creativefabrica-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creativefabrica-conformance.yml
- group: other
  href: https://artifacts.apis.io/creativefabrica/overlays/creativefabrica-idea-ai-genai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/creativefabrica-idea-ai-genai-overlay.yaml
- group: build
  href: https://artifacts.apis.io/creativefabrica/mcp/creativefabrica-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/creativefabrica-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/creativefabrica/mcp/creativefabrica-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/creativefabrica-mcp.yml
- group: agent
  href: https://artifacts.apis.io/creativefabrica/well-known/creativefabrica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/creativefabrica-well-known.yml
- group: build
  href: https://artifacts.apis.io/creativefabrica/packages/creativefabrica-packages.yml
  title: ''
  type: SDKs
  url: packages/creativefabrica-packages.yml
- group: build
  href: https://artifacts.apis.io/creativefabrica/packages/creativefabrica-packages.yml
  title: ''
  type: Packages
  url: packages/creativefabrica-packages.yml
- group: auth
  href: https://artifacts.apis.io/creativefabrica/authentication/creativefabrica-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creativefabrica-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.creativefabrica.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.creativefabrica.com/
- group: company
  title: ''
  type: Blog
  url: https://www.creativefabrica.com/the-artistry/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/creativefabrica
- group: commercial
  title: ''
  type: Pricing
  url: https://www.creativefabrica.com/subscription/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creativefabrica.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creativefabrica.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.creativefabrica.com/login/
- group: other
  href: https://artifacts.apis.io/creativefabrica/hosts/creativefabrica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creativefabrica-hosts.yml
- group: other
  href: https://artifacts.apis.io/creativefabrica/vendors/creativefabrica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creativefabrica-vendors.yml
- group: auth
  href: https://artifacts.apis.io/creativefabrica/security/creativefabrica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creativefabrica-domain-security.yml
created: '2026-10-11'
description: Creative Fabrica is an Amsterdam-based digital marketplace and subscription service for crafters, designers and makers, offering more than 12 million commercial-use creative assets — fonts, graphics, illustrations, SVGs, embroidery designs, print-on-demand (POD) templates, 3D-printing files, laser-cutting files, paper-craft downloads and KDP interiors — plus an online design tool (Studio), AI generation tools, classes and bundles. The company operates the Creative Fabrica store, the Open Store marketplace for independent designers, the Studio web app and the The Artistry editorial blog. Chamber of Commerce 70114412 (NL), VAT NL858147877B01, contact hi@creativefabrica.com.
image: https://raw.githubusercontent.com/creativefabrica/.github/main/assets/logo.svg
json_schemas:
- name: CreateGenerationRequest
  property_count: 0
  slug: creativefabrica-create-generation-request
- name: Generation
  property_count: 20
  slug: creativefabrica-generation
- name: ModelCostRequest
  property_count: 2
  slug: creativefabrica-model-cost-request
- name: ModelCostResponse
  property_count: 3
  slug: creativefabrica-model-cost-response
- name: ModelDetail
  property_count: 8
  slug: creativefabrica-model-detail
- name: PresetDetail
  property_count: 8
  slug: creativefabrica-preset-detail
jsonld:
- class_count: 58
  name: Creativefabrica Context
  property_count: 142
  slug: creativefabrica-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.idea.ai over streamable HTTP requiring OAuth; 4 tools listed.
  name: Creative Fabrica MCP Server
  slug: idea-ai
modified: '2026-11-04'
name: Creative Fabrica
nav: Providers
network: true
overview: 'Creative Fabrica publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Generations API, Models API, Presets API, and 2 more. Tagged areas include Company, Creative Marketplace, Digital Assets, Fonts, and Graphics.


  The Creative Fabrica catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Creative Fabrica''s developer surface includes sandbox, authentication, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Creativefabrica Plans Pricing
  plan_count: 3
  slug: creativefabrica-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Creativefabrica Rate Limits
  slug: creativefabrica-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Creative Fabrica API Rules
  rule_count: 64
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 4
  slug: creativefabrica-rules
scopes:
- name: Creativefabrica Scopes
  scope_count: 4
  slug: creativefabrica-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 45.5
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 36.3
    discoverability: 65.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Creativefabrica Authentication
  slug: creativefabrica-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Creativefabrica Domain Security
  slug: creativefabrica-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: creativefabrica-generate-speech-with-voice
  slug: creativefabrica-generate-speech-with-voice
- name: creativefabrica-generations-workflow
  slug: creativefabrica-generations-workflow
- name: creativefabrica-models-cost-estimation
  slug: creativefabrica-models-cost-estimation
- name: creativefabrica-run-preset
  slug: creativefabrica-run-preset
- name: creativefabrica-upload-input-media
  slug: creativefabrica-upload-input-media
slug: creativefabrica
tags:
- Company
- Creative Marketplace
- Digital Assets
- Fonts
- Graphics
- Print on Demand
- Embroidery
- Design Tools
- Subscription Service
- Amsterdam
website: https://www.creativefabrica.com/
---
