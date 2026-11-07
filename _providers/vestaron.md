---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Vestaron Agentic Access
  operation_count: 89
  slug: vestaron-agentic-access
  summary_line: 89 operations · 54 acting
api_count: 2
apis:
- description: 'A remote Model Context Protocol server published on the vestaron.com host and advertised anonymously through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. The '
  name: Vestaron MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Vestaron website at vestaron.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Vestaron Website (WordPress REST)
  slug: vestaron-com-website-wordpress-rest
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://vestaron.com/
- group: company
  title: ''
  type: About
  url: https://vestaron.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://vestaron.com/overview/
- group: other
  title: ''
  type: Technology
  url: https://vestaron.com/science/
- group: company
  title: ''
  type: News
  url: https://vestaron.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://vestaron.com/feed/
- group: other
  title: ''
  type: Resources
  url: https://vestaron.com/resources/
- group: other
  title: ''
  type: Downloads
  url: https://vestaron.com/downloads/
- group: other
  title: ''
  type: Sustainability
  url: https://vestaron.com/socialresponsibility/
- group: operate
  title: ''
  type: Support
  url: https://vestaron.com/contact/
- group: operate
  title: ''
  type: Contact
  url: https://vestaron.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vestaron.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vestaron.com/legal/privacy-statement/
- group: commercial
  title: ''
  type: Legal
  url: https://vestaron.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vestaron-corporation
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@vestaroncropprotection
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vestaron_stock/
- group: other
  href: https://artifacts.apis.io/vestaron/overlays/vestaron-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vestaron-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/vestaron/mcp/vestaron-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vestaron-mcp.yml
- group: build
  href: https://artifacts.apis.io/vestaron/mcp/vestaron-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vestaron-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/vestaron/authentication/vestaron-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vestaron-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vestaron/scopes/vestaron-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vestaron-scopes.yml
- group: agent
  href: https://artifacts.apis.io/vestaron/well-known/vestaron-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vestaron-well-known.yml
- group: design
  href: https://artifacts.apis.io/vestaron/conventions/vestaron-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vestaron-conventions.yml
- group: design
  href: https://artifacts.apis.io/vestaron/conformance/vestaron-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vestaron-conformance.yml
- group: design
  href: https://artifacts.apis.io/vestaron/errors/vestaron-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vestaron-problem-types.yml
- group: build
  href: https://artifacts.apis.io/vestaron/examples/vestaron-examples.yml
  title: ''
  type: Examples
  url: examples/vestaron-examples.yml
- group: design
  href: https://artifacts.apis.io/vestaron/data-model/vestaron-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vestaron-data-model.yml
- group: design
  href: https://artifacts.apis.io/vestaron/lifecycle/vestaron-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vestaron-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/vestaron/security/vestaron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vestaron-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/vestaron/agentic-access/vestaron-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vestaron-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/vestaron/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/vestaron/llms/vestaron-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vestaron-llms.txt
created: '2026-08-05'
description: Vestaron is an agricultural biotechnology company founded in 2005 and headquartered in Kalamazoo, Michigan, that develops peptide-based bioinsecticides derived from the venom of spiders and other venomous species. Its peptides deliver insecticidal modes of action that had never before been used for insect control — SPEAR, the first commercialised active ingredient, introduced IRAC Group 32, the first new neuromuscular mode of action since the diamides — and are effective on lepidopteran and sucking pests while remaining gentle on pollinators and beneficial insects. The commercial portfolio is SPEAR LEP, SPEAR RC, SPEAR T, BASIN FLEX, LEPROTEC and LEPROTEC WG, manufactured in partnership with ADM. The company has won the Crop Science Award and an EPA Green Chemistry Challenge award, and in 2024 became the first agriculture and food company inducted into the Global CleanTech 100 Hall of Fame. Vestaron publishes no developer program, no product API and no API documentation. The
  only machine-readable surfaces on vestaron.com are the WordPress REST content API (wp/v2), which is anonymously readable and serves the corporate newsroom, product and company pages and media library, and an OAuth-gated Model Context Protocol endpoint advertised through RFC 8414 and RFC 9728 metadata.
image: https://vestaron.com/wp-content/uploads/Logo_sep_23.png
layout: provider
mcp_servers:
- description: Remote MCP server at vestaron.com over HTTP.
  name: Vestaron MCP Server
  slug: vestaron
modified: '2026-08-05'
name: Vestaron
nav: Providers
network: true
overview: 'Vestaron is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biotechnology, and Crop Protection.


  Vestaron''s developer surface includes product news, support, legal docs, YouTube channel, authentication, code examples, and 27 more developer resources.'
random_paper: 18
scopes:
- name: Vestaron Scopes
  scope_count: 1
  slug: vestaron-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 7.3
    developer_ergonomics: 23.2
    discoverability: 60.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vestaron/vestaron-2026-09-02T165821.png
security:
- kind: authentication
  name: Vestaron Authentication
  slug: vestaron-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Vestaron Domain Security
  slug: vestaron-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Read the Vestaron newsroom
  slug: vestaron-read-newsroom
- name: Search Vestaron products and resources
  slug: vestaron-search-products-and-resources
slug: vestaron
tags:
- Company
- Agriculture
- AgTech
- Biotechnology
- Crop Protection
- Bioinsecticides
- Peptides
- Biologicals
- Sustainability
- Pollinator Safety
- Life Sciences
website: https://vestaron.com/
---
