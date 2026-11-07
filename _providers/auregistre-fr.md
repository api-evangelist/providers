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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://auregistre.fr/api
  baseurl_source: declared
  description: 'Read-only access by SIREN. There is deliberately no search endpoint: see the documentation for why.'
  name: Auregistre Company API
  slug: auregistre-fr-company-api
- baseURL: https://auregistre.fr/api
  baseurl_source: declared
  description: Aggregate counts of insolvency openings, over the scopes the website already publishes as pages.
  name: Auregistre Insolvency API
  slug: auregistre-fr-insolvency-api
- baseURL: https://auregistre.fr/api
  baseurl_source: declared
  description: What the gazette published on companies you already track. It takes identifiers, never criteria, so it is not a search either.
  name: Auregistre Watch API
  slug: auregistre-fr-watch-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/auregistre-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/auregistre-fr/llms/auregistre-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auregistre-fr-llms.txt
- group: agent
  href: https://artifacts.apis.io/auregistre-fr/mcp/auregistre-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/auregistre-fr-mcp.yml
- group: other
  href: https://artifacts.apis.io/auregistre-fr/hosts/auregistre-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auregistre-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/auregistre-fr/vendors/auregistre-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auregistre-fr-vendors.yml
- group: build
  href: https://artifacts.apis.io/auregistre-fr/packages/auregistre-fr-packages.yml
  title: ''
  type: SDKs
  url: packages/auregistre-fr-packages.yml
- group: build
  href: https://artifacts.apis.io/auregistre-fr/packages/auregistre-fr-packages.yml
  title: ''
  type: Packages
  url: packages/auregistre-fr-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auregistre
- group: auth
  href: https://artifacts.apis.io/auregistre-fr/security/auregistre-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auregistre-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auregistre.fr/
created: '2026-11-02'
description: Auregistre provides historical data on French companies from the official commercial register. Users can search for any enterprise, view changes in directors, headquarters, financial statements, and procedural events since its creation or from 2008 for older records. The service aggregates official bulletins and the Sirene directory under an open licence, offering alerts via email for updates on monitored entities.
image: https://auregistre.fr/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at auregistre.fr.
  name: Auregistre MCP Server
  slug: auregistre-fr-mcp-yml
modified: '2026-11-02'
name: Auregistre
nav: Providers
network: true
overview: 'Auregistre publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Company API, Insolvency API, and Watch API. Tagged areas include Company, Data, French, Registry, and Historical.'
random_paper: 0
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 50.8
    developer_ergonomics: 8.9
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 20.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auregistre Fr Domain Security
  slug: auregistre-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: company-timeline
  slug: auregistre-fr-company-timeline
slug: auregistre-fr
tags:
- Company
- Data
- French
- Registry
- Historical
website: https://auregistre.fr/
---
