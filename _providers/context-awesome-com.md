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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to curated awesome lists and resources via MCP endpoints.
  name: Context Awesome API
  slug: context-awesome-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/context-awesome-com/conformance/context-awesome-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/context-awesome-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/context-awesome-com/llms/context-awesome-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/context-awesome-com-llms.txt
- group: other
  href: https://artifacts.apis.io/context-awesome-com/hosts/context-awesome-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/context-awesome-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/context-awesome-com/vendors/context-awesome-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/context-awesome-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.context-awesome.com/list/narkoz/guides
- group: auth
  href: https://artifacts.apis.io/context-awesome-com/security/context-awesome-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/context-awesome-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.context-awesome.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.context-awesome.com/browse
- group: operate
  title: ''
  type: Support
  url: https://www.context-awesome.com/submit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bh-rat/context-awesome
coverage:
  checked: '2026-11-04'
  detail: Documentation exists but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://www.context-awesome.com/list/narkoz/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Context Awesome provides an MCP server offering over 8,500 curated awesome lists and more than 1.5 million vetted resources for AI agents. It aggregates community‑curated collections across technology domains, enabling agents to recommend high‑quality tools, libraries, and resources instead of random search results. The platform supports browsing, submitting lists, and integrates with GitHub and other developer tools.
image: https://www.context-awesome.com/opengraph-image?56176eeab5711698
layout: provider
modified: '2026-11-04'
name: Context Awesome
nav: Providers
network: true
overview: 'Context Awesome is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data, Tools, Community, and MCP.


  Context Awesome''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Context Awesome Com Domain Security
  slug: context-awesome-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: context-awesome-com
tags:
- Artificial Intelligence
- Data
- Tools
- Community
- MCP
website: https://www.context-awesome.com/
---
