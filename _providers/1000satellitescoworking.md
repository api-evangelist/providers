---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.0
  scored_at: '2026-09-14'
api_count: 2
apis:
- description: A remote Model Context Protocol server served from the 1000satellites.de WordPress estate under the "mcp" REST namespace. Two MCP routes are advertised in the route index — mcp-oauth-server and mcp-ad
  name: 1000 Satellites MCP Server (WordPress MCP Adapter)
  slug: mcp
- baseURL: https://1000satellites.de/wp-json
  baseurl_source: declared
  description: The anonymously readable WordPress REST content surface of 1000satellites.de. Ten resources returned HTTP 200 to an unauthenticated request on 2026-09-05 — posts, pages, media, categories, tags, comme
  name: 1000 Satellites Content API (WordPress REST wp/v2)
  slug: content-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://1000satellites.de/
- group: company
  title: ''
  type: Blog
  url: https://1000satellites.de/en/news/
- group: operate
  title: ''
  type: Support
  url: https://1000satellites.de/kontakt/
- group: operate
  title: ''
  type: FAQ
  url: https://1000satellites.de/faq/
- group: commercial
  title: ''
  type: Pricing
  url: https://1000satellites.de/preise
- group: start
  title: ''
  type: SignUp
  url: https://1000satellites.de/buchung/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1000satellites.de/agb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1000satellites.de/datenschutz/
- group: other
  title: ''
  type: Imprint
  url: https://1000satellites.de/impressum/
- group: company
  title: ''
  type: Careers
  url: https://1000satellites.de/jobs/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1000-satellites-coworking
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/well-known/1000satellitescoworking-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1000satellitescoworking-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/mcp/1000satellitescoworking-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1000satellitescoworking-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/mcp/1000satellitescoworking-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/1000satellitescoworking-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/authentication/1000satellitescoworking-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1000satellitescoworking-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/scopes/1000satellitescoworking-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/1000satellitescoworking-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/security/1000satellitescoworking-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1000satellitescoworking-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/conformance/1000satellitescoworking-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1000satellitescoworking-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/errors/1000satellitescoworking-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/1000satellitescoworking-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/conventions/1000satellitescoworking-conventions.yml
  title: ''
  type: Conventions
  url: conventions/1000satellitescoworking-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/lifecycle/1000satellitescoworking-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/1000satellitescoworking-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/data-model/1000satellitescoworking-data-model.yml
  title: ''
  type: DataModel
  url: data-model/1000satellitescoworking-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/overlays/1000satellitescoworking-content-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/1000satellitescoworking-content-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/llms/1000satellitescoworking-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1000satellitescoworking-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/packages/1000satellitescoworking-packages.yml
  title: ''
  type: Packages
  url: packages/1000satellitescoworking-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/plans/1000satellitescoworking-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/1000satellitescoworking-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/rate-limits/1000satellitescoworking-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/1000satellitescoworking-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/1000satellitescoworking/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: '1000 Satellites GmbH is a German flex-office and coworking operator founded in 2019 in Mannheim by Caro Windlin, Markus Hummelsberger and Gregory von Abendroth as a spin-off of BASF''s innovation unit Chemovator. It converts underused office space from corporate real-estate portfolios into professionally operated, decentralised "satellite" workspaces across the Rhein-Neckar region, Munich, Hamburg and Berlin, selling day passes, monthly memberships, team tickets, fixed desks, meeting rooms and event space rather than a software product. It is not a software vendor and publishes no product or developer API. Its machine-readable surface is what the company''s WordPress estate exposes on 1000satellites.de: an anonymously readable WordPress REST content API (wp/v2) serving news posts, location and marketing pages, media and site search; and — notably for a business of this kind — a live remote Model Context Protocol server published through the WordPress MCP Adapter, advertised
  by real RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata, with tools/list authentication-gated.'
image: https://1000satellites.de/wp-content/uploads/2023/12/cropped-1000-Satellites-Coworking.jpg
layout: provider
mcp_servers:
- description: 1000 Satellites publishes a live remote Model Context Protocol server on its primary marketing host. It appears in no MCP registry and in no company documentation — it was found by probing the named /
  name: 1000 Satellites MCP Server
  slug: 1000-satellites-mcp-server
modified: '2026-09-05'
name: 1000 Satellites
nav: Providers
network: true
overview: '1000 Satellites publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Co-Working, Flex Office, Real-Estate, and Office Space.


  1000 Satellites'' developer surface includes engineering blog, support, FAQ, pricing, signup flow, authentication, and 22 more developer resources.'
plans:
- name: 1000Satellitescoworking Plans Pricing
  plan_count: 10
  slug: 1000satellitescoworking-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 1000Satellitescoworking Rate Limits
  slug: 1000satellitescoworking-rate-limits
scopes:
- name: 1000Satellitescoworking Scopes
  scope_count: 1
  slug: 1000satellitescoworking-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 13.1
    developer_ergonomics: 20.8
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 31.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: 1000Satellitescoworking Authentication
  slug: 1000satellitescoworking-authentication
  summary_line: none/oauth2 · 3 schemes
- kind: domain-security
  name: 1000Satellitescoworking Domain Security
  slug: 1000satellitescoworking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1000satellitescoworking
tags:
- Company
- Co-Working
- Flex Office
- Real-Estate
- Office Space
- Workplace
- Meeting Rooms
- Germany
- Content
- MCP
website: https://1000satellites.de/
---
