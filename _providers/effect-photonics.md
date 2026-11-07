---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 2 published API entries'
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: platform
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
  score: 40.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the EFFECT Photonics website at effectphotonics.com: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: EFFECT Photonics Website (WordPress REST)
  slug: effectphotonics-com-website-wordpress-rest
- baseURL: https://effectphotonics.com/wp-json/
  baseurl_source: declared
  description: Model Context Protocol servers exposed by the WordPress MCP adapter. Both servers require authentication (observed HTTP 401 anonymously); the OAuth server answers with a correct RFC 9728 Bearer challe
  name: EFFECT Photonics MCP API
  slug: effect-photonics-mcp-api
artifact_total: 14
collections:
- collection_type: open
  name: EFFECT Photonics WordPress REST MCP API
  slug: open-effect-photonics-mcp-api
- collection_type: open
  name: API Collection
  slug: open-effect-photonics-wp-rest-discovery-original
common:
- group: commercial
  href: https://artifacts.apis.io/effect-photonics/plans/effect-photonics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/effect-photonics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/effect-photonics/rate-limits/effect-photonics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/effect-photonics-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://effectphotonics.com/
- group: company
  title: ''
  type: About
  url: https://effectphotonics.com/about/
- group: other
  title: ''
  type: Products
  url: https://effectphotonics.com/products/
- group: company
  title: ''
  type: Newsroom
  url: https://effectphotonics.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://effectphotonics.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://effectphotonics.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://effectphotonics.com/get-in-touch/support/
- group: operate
  title: ''
  type: Contact
  url: https://effectphotonics.com/get-in-touch/
- group: operate
  title: ''
  type: FAQ
  url: https://effectphotonics.com/faq/
- group: company
  title: ''
  type: Careers
  url: https://effectphotonics.com/careers/
- group: company
  title: ''
  type: Investors
  url: https://effectphotonics.com/investors/
- group: other
  title: ''
  type: Events
  url: https://effectphotonics.com/events/
- group: company
  title: ''
  type: Partners
  url: https://effectphotonics.com/find-a-partner/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://effectphotonics.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://effectphotonics.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://effectphotonics.com/cookie-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://effectphotonics.com/newsroom/iso-9001-certification-reaffirms-effect-photonics-commitment-to-quality-across-operations/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: other
  href: https://artifacts.apis.io/effect-photonics/overlays/effect-photonics-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/effect-photonics-wp-rest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/effect-photonics/mcp/effect-photonics-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/effect-photonics-mcp.yml
- group: build
  href: https://artifacts.apis.io/effect-photonics/mcp/effect-photonics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/effect-photonics-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/effect-photonics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/effect-photonics/llms/effect-photonics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/effect-photonics-llms.txt
- group: agent
  href: https://artifacts.apis.io/effect-photonics/well-known/effect-photonics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/effect-photonics-well-known.yml
- group: auth
  href: https://artifacts.apis.io/effect-photonics/authentication/effect-photonics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/effect-photonics-authentication.yml
- group: auth
  href: https://artifacts.apis.io/effect-photonics/scopes/effect-photonics-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/effect-photonics-scopes.yml
- group: design
  href: https://artifacts.apis.io/effect-photonics/conventions/effect-photonics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/effect-photonics-conventions.yml
- group: design
  href: https://artifacts.apis.io/effect-photonics/errors/effect-photonics-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/effect-photonics-problem-types.yml
- group: design
  href: https://artifacts.apis.io/effect-photonics/data-model/effect-photonics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/effect-photonics-data-model.yml
- group: design
  href: https://artifacts.apis.io/effect-photonics/lifecycle/effect-photonics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/effect-photonics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/effect-photonics/conformance/effect-photonics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/effect-photonics-conformance.yml
- group: auth
  href: https://artifacts.apis.io/effect-photonics/security/effect-photonics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/effect-photonics-domain-security.yml
created: '2026-08-12'
description: EFFECT Photonics is an optical-semiconductor company headquartered at High Tech Campus 37 in Eindhoven, the Netherlands, with sites in the United Kingdom, the United States and Taiwan. Spun out of Eindhoven University of Technology, it designs and manufactures coherent optical transceiver subsystems and monolithically integrated Indium Phosphide (InP) photonic integrated circuits, including its pico and nano Integrable Tunable Laser Assemblies for 100G, 400G and 800G coherent links across telecom access and metro networks, data-center interconnect and AI scale-across infrastructure. It operates no developer API programme and publishes no product, network-management or transceiver-control API, no developer portal, no SDK and no pricing. It is catalogued here because its corporate website runs a live WordPress REST API with 290 discoverable routes — including a publicly readable optical-product catalogue with hardware taxonomies (product line, form factor, output power, tuning
  range, operating temperature, target application, management interface) and a first-party `effect/v1` namespace — and because that same install exposes two Model Context Protocol servers guarded by an OAuth 2.1 authorization server the host advertises through RFC 8414 and RFC 9728 metadata.
image: https://effectphotonics.com/wp-content/uploads/2026/05/EFFECT-Photonics_logo-color.svg
layout: provider
mcp_servers:
- description: EFFECT Photonics' corporate WordPress site exposes two live Model Context Protocol servers under the `mcp` REST namespace, guarded by an OAuth 2.1 authorization server the same host advertises via RFC
  name: EFFECT Photonics MCP Server
  slug: effect-photonics-mcp-yml
modified: '2026-08-12'
name: EFFECT Photonics
nav: Providers
network: true
overview: 'EFFECT Photonics is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including MCP API, and 1 more. Tagged areas include Company, Photonics, Optical Networking, Optical Transceivers, and Photonic Integrated Circuits.


  The EFFECT Photonics catalog on APIs.io includes 1 Spectral governance ruleset.


  EFFECT Photonics'' developer surface includes engineering blog, support, FAQ, authentication, and 30 more developer resources.'
plans:
- name: Effect Photonics Plans Pricing
  plan_count: 0
  slug: effect-photonics-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Effect Photonics Rate Limits
  slug: effect-photonics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: EFFECT Photonics API Rules
  rule_count: 67
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 7
  slug: effect-photonics-rules
scopes:
- name: Effect Photonics Scopes
  scope_count: 1
  slug: effect-photonics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 17.0
    developer_ergonomics: 25.6
    discoverability: 61.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 26.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/effect-photonics/effect-photonics-2026-10-11T104049.png
security:
- kind: authentication
  name: Effect Photonics Authentication
  slug: effect-photonics-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Effect Photonics Domain Security
  slug: effect-photonics-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Browse the EFFECT Photonics optical product catalogue
  slug: effect-photonics-browse-optical-product-catalog
- name: Discover the EFFECT Photonics API surface
  slug: effect-photonics-discover-surface
- name: Read EFFECT Photonics' commercial terms and newsroom
  slug: effect-photonics-read-commercial-terms-and-newsroom
slug: effect-photonics
tags:
- Company
- Photonics
- Optical Networking
- Optical Transceivers
- Photonic Integrated Circuits
- Semiconductors
- Telecommunications
- Data Center Interconnect
- Hardware
- MCP
- WordPress
- Netherlands
website: https://effectphotonics.com/
---
