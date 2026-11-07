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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is provided at the Guides page, but no machine‑readable contract (OpenAPI, AsyncAPI, GraphQL, etc.) was found.
  name: France Care API
  slug: france-care-api
artifact_total: 4
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.france-care.fr/guides
- group: auth
  href: https://artifacts.apis.io/france-care-fr/security/france-care-fr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/france-care-fr-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/france-care-fr/llms/france-care-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/france-care-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/france-care-fr/mcp/france-care-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/france-care-fr-mcp.yml
- group: auth
  href: https://artifacts.apis.io/france-care-fr/well-known/france-care-fr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/france-care-fr-security.txt
- group: auth
  href: https://artifacts.apis.io/france-care-fr/well-known/france-care-fr-france-care-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/france-care-fr-france-care-security.txt
- group: agent
  href: https://artifacts.apis.io/france-care-fr/well-known/france-care-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/france-care-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/france-care-fr/hosts/france-care-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/france-care-fr-hosts.yml
- group: auth
  href: https://artifacts.apis.io/france-care-fr/security/france-care-fr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/france-care-fr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/france-care-fr/security/france-care-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/france-care-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://france-care.fr/
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation pages are public HTML without any OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.france-care.fr/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: France Care FR is a French healthcare technology company that provides digital solutions for patient management, telemedicine, and health data integration. The platform enables clinics and hospitals to streamline appointment scheduling, electronic health records, and remote consultations, improving accessibility and efficiency in the French medical ecosystem. By leveraging secure APIs, France Care FR facilitates interoperability between healthcare providers, insurers, and third‑party health applications, supporting compliance with French health data regulations and fostering innovative care delivery models.
image: https://www.france-care.fr/opengraph-image?e350548c9685c449
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.france-care.fr.
  name: france-care-fr MCP Server
  slug: france-care-fr-mcp-yml
modified: '2026-10-30'
name: france-care-fr
nav: Providers
network: true
overview: 'france-care-fr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, and France.


  france-care-fr''s developer surface includes documentation and 10 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 58.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/france-care-fr/france-care-fr-2026-11-03T132327.png
security:
- kind: domain-security
  name: France Care Fr Domain Security
  slug: france-care-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: France Care Fr Vulnerability Disclosure
  slug: france-care-fr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: france-care-fr
tags:
- Company
- Healthcare
- Telehealth
- France
website: https://france-care.fr/
---
