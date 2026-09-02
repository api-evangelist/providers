---
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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: 'WordPress core content API (posts, pages, media, taxonomies, users, settings) plus the site''s custom post types — products, careers, events, partners, team members and FAQs — and the optical hardware '
  name: EFFECT Photonics Wp/v2 API
  slug: effect-photonics-wp-v2-api
- description: EFFECT Photonics' own custom REST namespace — a careers synchronisation trigger (POST /effect/v1/careers/sync, observed HTTP 401 anonymously) and a GLB 3D-model position endpoint used by the product v
  name: EFFECT Photonics Effect/v1 API
  slug: effect-photonics-effect-v1-api
- description: Model Context Protocol servers exposed by the WordPress MCP adapter. Both servers require authentication (observed HTTP 401 anonymously); the OAuth server answers with a correct RFC 9728 Bearer challe
  name: EFFECT Photonics MCP API
  slug: effect-photonics-mcp-api
- description: WordPress Abilities API — the registry of named abilities an agent may discover and run, and the surface the MCP adapter projects into tools. Read access is capability-gated (observed HTTP 401 anonymo
  name: EFFECT Photonics Wp Abilities/v1 API
  slug: effect-photonics-wp-abilities-v1-api
- description: oEmbed discovery and proxy endpoints.
  name: EFFECT Photonics Oembed/1.0 API
  slug: effect-photonics-oembed-1-0-api
- description: REST API index / namespace discovery, plus the WordPress batch/v1 request batching endpoint.
  name: EFFECT Photonics Root API
  slug: effect-photonics-root-api
artifact_total: 19
collections:
- collection_type: open
  name: EFFECT Photonics WordPress REST Effect/v1 API
  slug: open-effect-photonics-effect-v1-api
- collection_type: open
  name: EFFECT Photonics WordPress REST MCP API
  slug: open-effect-photonics-mcp-api
- collection_type: open
  name: EFFECT Photonics WordPress REST Oembed/1.0 API
  slug: open-effect-photonics-oembed-1-0-api
- collection_type: open
  name: EFFECT Photonics WordPress REST Root API
  slug: open-effect-photonics-root-api
- collection_type: open
  name: EFFECT Photonics WordPress REST Wp Abilities/v1 API
  slug: open-effect-photonics-wp-abilities-v1-api
- collection_type: open
  name: API Collection
  slug: open-effect-photonics-wp-rest-discovery-original
- collection_type: open
  name: EFFECT Photonics WordPress REST Wp/v2 API
  slug: open-effect-photonics-wp-v2-api
common:
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
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/effect-photonics-wp-rest-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/effect-photonics-wp-rest-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/effect-photonics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/effect-photonics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/effect-photonics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/effect-photonics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/effect-photonics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/effect-photonics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/effect-photonics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/effect-photonics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/effect-photonics-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/effect-photonics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/effect-photonics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/effect-photonics-domain-security.yml
created: '2026-08-12'
description: EFFECT Photonics is an optical-semiconductor company headquartered at High Tech Campus 37 in Eindhoven, the Netherlands, with sites in the United Kingdom, the United States and Taiwan. Spun out of Eindhoven University of Technology, it designs and manufactures coherent optical transceiver subsystems and monolithically integrated Indium Phosphide (InP) photonic integrated circuits, including its pico and nano Integrable Tunable Laser Assemblies for 100G, 400G and 800G coherent links across telecom access and metro networks, data-center interconnect and AI scale-across infrastructure. It operates no developer API programme and publishes no product, network-management or transceiver-control API, no developer portal, no SDK and no pricing. It is catalogued here because its corporate website runs a live WordPress REST API with 290 discoverable routes — including a publicly readable optical-product catalogue with hardware taxonomies (product line, form factor, output power, tuning
  range, operating temperature, target application, management interface) and a first-party `effect/v1` namespace — and because that same install exposes two Model Context Protocol servers guarded by an OAuth 2.1 authorization server the host advertises through RFC 8414 and RFC 9728 metadata.
image: https://effectphotonics.com/wp-content/uploads/2026/05/EFFECT-Photonics_logo-color.svg
layout: provider
mcp_servers:
- description: ''
  name: EFFECT Photonics MCP Server
  slug: effect-photonics-mcp-server
modified: '2026-08-12'
name: EFFECT Photonics
nav: Providers
network: true
overview: 'EFFECT Photonics publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Wp/v2 API, Effect/v1 API, MCP API, and 3 more. Tagged areas include Company, Photonics, Optical Networking, Optical Transceivers, and Photonic Integrated Circuits.


  EFFECT Photonics'' developer surface includes engineering blog, support, FAQ, authentication, and 29 more developer resources.'
plans:
- name: Effect Photonics Plans Pricing
  plan_count: 0
  slug: effect-photonics-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Effect Photonics Rate Limits
  slug: effect-photonics-rate-limits
scopes:
- name: Effect Photonics Scopes
  scope_count: 1
  slug: effect-photonics-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 16.6
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Effect Photonics Authentication
  slug: effect-photonics-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Effect Photonics Domain Security
  slug: effect-photonics-domain-security
  summary_line: TLSv1.3 · DMARC
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
