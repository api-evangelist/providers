---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: API discovered via MCP endpoint providing tool list. No OpenAPI spec available.
  name: Bonebenders API
  slug: bonebenders-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/bonebenders-com/security/bonebenders-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bonebenders-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bonebenders-com/llms/bonebenders-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bonebenders-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bonebenders-com/mcp/bonebenders-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bonebenders-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bonebenders-com/well-known/bonebenders-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bonebenders-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bonebenders-com/well-known/bonebenders-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonebenders-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bonebenders-com/hosts/bonebenders-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonebenders-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonebenders-com/vendors/bonebenders-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonebenders-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bonebenders.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bonebenders.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://bonebenders.com/blog/
- group: auth
  href: https://artifacts.apis.io/bonebenders-com/security/bonebenders-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bonebenders-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bonebenders-com/security/bonebenders-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonebenders-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonebenders.com/
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint provides tool list but no OpenAPI or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://bonebenders.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bonebenders is an evidence‑based dentistry blog founded by Dr. Ernesto Bruschi, a periodontist and oral surgeon in Frosinone, Italy. It provides detailed articles on periodontology, dental implantology, oral surgery, bone regeneration and related clinical techniques, serving professionals and patients seeking reliable oral health information.
image: https://bonebenders.com/images/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at bonebenders.com.
  name: Bonebenders MCP Server
  slug: bonebenders-com-mcp-yml
modified: '2026-11-02'
name: Bonebenders
nav: Providers
network: true
overview: 'Bonebenders is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dentistry, Oral Health, Periodontology, Implantology, and Surgery.


  Bonebenders'' developer surface includes engineering blog and 12 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonebenders Com Domain Security
  slug: bonebenders-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bonebenders Com Vulnerability Disclosure
  slug: bonebenders-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bonebenders-com
tags:
- Dentistry
- Oral Health
- Periodontology
- Implantology
- Surgery
- Education
website: https://bonebenders.com/
---
