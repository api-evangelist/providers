---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Be Sew Bizzy product search and other tools.
  name: Be Sew Bizzy API
  slug: be-sew-bizzy-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/besewbizzy-com/mcp/besewbizzy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/besewbizzy-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/besewbizzy-com/hosts/besewbizzy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/besewbizzy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/besewbizzy-com/vendors/besewbizzy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/besewbizzy-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://besewbizzy.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/besewbizzy-com/security/besewbizzy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/besewbizzy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://besewbizzy.com/
- group: company
  title: ''
  type: Blog
  url: https://besewbizzy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://besewbizzy.com/terms
- group: operate
  title: ''
  type: Support
  url: https://besewbizzy.com/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://besewbizzy.com/about
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found at standard locations.
  evidence:
  - status: 404
    url: https://besewbizzy.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Be Sew Bizzy is a family‑owned quilt shop and fabric store located in Los Alamitos, California. Offering a wide selection of quilting cotton by the yard, curated quilt kits, and machine embroidery supplies, the shop serves hobbyists and professional makers alike. As a Kimberbell partner, they provide premium threads and accessories. The store also hosts live fabric sales, a blog with crafting tips, and tools like a quilt designer and thread‑match service to help customers create beautiful projects.
image: https://besewbizzy.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at besewbizzy.com.
  name: Be Sew Bizzy MCP Server
  slug: besewbizzy-com-mcp-yml
modified: '2026-11-02'
name: Be Sew Bizzy
nav: Providers
network: true
overview: 'Be Sew Bizzy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Quilt, Fabric, Embroidery, Craft, and Los Alamitos.


  Be Sew Bizzy''s developer surface includes engineering blog, support, getting-started guide, and 7 more developer resources.'
random_paper: 2
scopes:
- name: Besewbizzy Com Scopes
  scope_count: 0
  slug: besewbizzy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Besewbizzy Com Authentication
  slug: besewbizzy-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Besewbizzy Com Domain Security
  slug: besewbizzy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: besewbizzy-com
tags:
- Quilt
- Fabric
- Embroidery
- Craft
- Los Alamitos
website: https://besewbizzy.com/
---
