---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    auth_clarity: bearer
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
  score: 3.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Beglaubigt API provides RESTful endpoints for notarization and incorporation services.
  name: Beglaubigt API
  slug: beglaubigt-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/beglaubigt-de/authentication/beglaubigt-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beglaubigt-de-authentication.yml
- group: agent
  href: https://artifacts.apis.io/beglaubigt-de/llms/beglaubigt-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beglaubigt-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/beglaubigt-de/mcp/beglaubigt-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beglaubigt-de-mcp.yml
- group: other
  href: https://artifacts.apis.io/beglaubigt-de/hosts/beglaubigt-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beglaubigt-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/beglaubigt-de/vendors/beglaubigt-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beglaubigt-de-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.beglaubigt.de/login
- group: auth
  href: https://artifacts.apis.io/beglaubigt-de/security/beglaubigt-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beglaubigt-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beglaubigt.de/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beglaubigt.de/
- group: company
  title: ''
  type: Blog
  url: https://beglaubigt.de/blog
- group: operate
  title: ''
  type: Support
  url: https://beglaubigt.de/kontakt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beglaubigt.de/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beglaubigt.de/datenschutz
coverage:
  checked: '2026-11-02'
  detail: API endpoints require an Authorization Bearer token, and no public OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.beglaubigt.de/incorporation/post
  reason: auth-required
  state: gated
created: '2026-11-02'
description: Beglaubigt is the first digital notary for Europe, offering digital certifications and GmbH/UG company formations under eIDAS. With apostille valid in over 120 countries, prices start at €99. Over 25,000 customers trust our services.
image: https://images.prismic.io/beglaubigt/aaAPVsFoBIGEg2ej_meta-new.jpg?auto=format,compress
layout: provider
mcp_servers:
- description: Remote MCP server at api.beglaubigt.de.
  name: Beglaubigt MCP Server
  slug: beglaubigt-de-mcp-yml
modified: '2026-11-02'
name: Beglaubigt
nav: Providers
network: true
overview: 'Beglaubigt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Notary, Legal Tech, eIDAS, Document Verification, and Startups.


  Beglaubigt''s developer surface includes authentication, documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 20
scopes:
- name: Beglaubigt De Scopes
  scope_count: 0
  slug: beglaubigt-de-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beglaubigt De Authentication
  slug: beglaubigt-de-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beglaubigt De Domain Security
  slug: beglaubigt-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beglaubigt-de
tags:
- Digital Notary
- Legal Tech
- eIDAS
- Document Verification
- Startups
website: https://beglaubigt.de/
---
