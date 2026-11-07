---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: API documentation is provided via the guides page, but no machine‑readable contract (OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL) was found.
  name: CELPass API
  slug: celpass-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/celpass-com/plans/celpass-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/celpass-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/celpass-com/llms/celpass-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/celpass-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/celpass-com/mcp/celpass-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/celpass-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/celpass-com/hosts/celpass-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celpass-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/celpass-com/vendors/celpass-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celpass-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celpass.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://celpass.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celpass.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://celpass.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://celpass.com/celpip/vocabulary/topics/news
- group: docs
  title: ''
  type: Documentation
  url: https://celpass.com/guides
- group: company
  title: ''
  type: Blog
  url: https://celpass.com/blog
- group: auth
  href: https://artifacts.apis.io/celpass-com/security/celpass-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celpass-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celpass.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://celpass.com/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Independent online CELPIP practice platform with AI‑scored practice tests, mock exams and a free CLB diagnostic. It offers full‑length CELPIP‑General mock tests, AI scoring for speaking and writing, a free 25‑minute CLB diagnostic, daily drills, and resources for Canadian citizenship English preparation. Not affiliated with Paragon Testing Enterprises.
image: https://celpass.com/opengraph-image?9834f206a735d4d3
layout: provider
mcp_servers:
- description: Remote MCP server at celpass.com.
  name: CELPass MCP Server
  slug: celpass-com-mcp-yml
modified: '2026-11-04'
name: CELPass
nav: Providers
network: true
overview: 'CELPass is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Language, Test Prep, and Artificial Intelligence.


  CELPass'' developer surface includes signup flow, pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Celpass Com Plans Pricing
  plan_count: 4
  slug: celpass-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celpass Com Domain Security
  slug: celpass-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celpass-com
tags:
- Company
- Education
- Language
- Test Prep
- Artificial Intelligence
- Canada
website: https://celpass.com/
---
