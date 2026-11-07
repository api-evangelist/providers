---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI career ecosystem API providing role recommendations, skill pathways, resume building, and application tracking.
  name: AiESphere API
  slug: aiesphere-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/aiesphere-com/changelog/aiesphere-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aiesphere-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aiesphere-com/authentication/aiesphere-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiesphere-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/aiesphere-com/mcp/aiesphere-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiesphere-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aiesphere-com/well-known/aiesphere-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiesphere-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiesphere-com/hosts/aiesphere-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiesphere-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiesphere-com/vendors/aiesphere-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiesphere-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiesphere.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiesphere.com/privacy
- group: start
  title: ''
  type: Login
  url: https://aiesphere.com/auth/signin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aiesphere.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://aiesphere.com/changelog
- group: auth
  href: https://artifacts.apis.io/aiesphere-com/security/aiesphere-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiesphere-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiesphere.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://aiesphere.com/mcp
  - status: 200
    url: https://aiesphere.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AiESphere is an AI career ecosystem based in India, helping users discover suitable roles, build relevant skills, improve their resumes, and apply for jobs with AI assistance. The platform offers role recommendations, skill pathways, resume building tools, and end‑to‑end application tracking, aiming to empower the future of work through upskilling and personalized guidance.
image: https://aiesphere.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at aiesphere.com.
  name: AiESphere MCP Server
  slug: aiesphere-com-mcp-yml
modified: '2026-11-01'
name: AiESphere
nav: Providers
network: true
overview: 'AiESphere is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Careers, Education, Platform, and India.


  AiESphere''s developer surface includes changelog, authentication, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 18.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiesphere Com Authentication
  slug: aiesphere-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aiesphere Com Domain Security
  slug: aiesphere-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiesphere-com
tags:
- Artificial Intelligence
- Careers
- Education
- Platform
- India
website: https://aiesphere.com/
---
