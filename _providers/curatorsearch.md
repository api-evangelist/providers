---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://curatorsearch.com
  baseurl_source: declared
  description: Keyless, read-only REST/JSON API for searching museum/curatorial vacancies and retrieving individual listings, plus the full advertised-salary archive. Documented via a live OpenAPI 3.1 contract.
  name: CuratorSearch API
  slug: curatorsearch-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://curatorsearch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://curatorsearch.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://curatorsearch.com/developers
- group: operate
  title: ''
  type: Support
  url: https://curatorsearch.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://curatorsearch.com/developers#attribution
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://curatorsearch.com/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/well-known/curatorsearch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/curatorsearch-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/authentication/curatorsearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curatorsearch-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/conventions/curatorsearch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curatorsearch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/lifecycle/curatorsearch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/curatorsearch-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/conformance/curatorsearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curatorsearch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/errors/curatorsearch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/curatorsearch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/data-model/curatorsearch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curatorsearch-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/overlays/curatorsearch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/curatorsearch-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/components/curatorsearch-components.yml
  title: ''
  type: Components
  url: components/curatorsearch-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/plans/curatorsearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curatorsearch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/rate-limits/curatorsearch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/curatorsearch-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/security/curatorsearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curatorsearch-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/curatorsearch/refs/heads/main/mcp/curatorsearch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/curatorsearch-tool-crosswalk.yml
- group: other
  title: ''
  type: RSS
  url: https://curatorsearch.com/feed.xml
created: '2026-09-19'
description: An independent, daily-refreshed record of museum/gallery/curatorial vacancies and advertised salaries, aggregated from 400+ institutions' careers pages. Exposes a keyless REST/JSON API, an OpenAPI 3.1 contract, a hosted MCP server, llms.txt, open datasets (CC BY 4.0, with DOI), and RSS.
image: https://curatorsearch.com/icon.png
layout: provider
mcp_servers:
- description: Official hosted MCP server for CuratorSearch. Stateless Streamable HTTP (POST) endpoint on the provider's primary domain, no key required. Live tools/list retrieved anonymously and saved verbatim to m
  name: CuratorSearch MCP Server
  slug: curatorsearch-mcp-server
- description: ''
  name: MCP endpoint (hosted)
  slug: mcp-endpoint-hosted
modified: '2026-09-20'
name: CuratorSearch
nav: Providers
network: true
overview: 'CuratorSearch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include agent-native, MCP, OpenAPI, llms-txt, and Open Data.


  CuratorSearch''s developer surface includes documentation, support, authentication, and 18 more developer resources.'
plans:
- name: Curatorsearch Plans Pricing
  plan_count: 0
  slug: curatorsearch-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Curatorsearch Rate Limits
  slug: curatorsearch-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Curatorsearch Authentication
  slug: curatorsearch-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Curatorsearch Domain Security
  slug: curatorsearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curatorsearch
tags:
- agent-native
- MCP
- OpenAPI
- llms-txt
- Open Data
- Job
- Cultural Heritage
- Museums
- curatorial
- salary-transparency
- glam
- museum jobs
- Job Board
- Salaries
- Pay Transparency
- Datasets
- RSS
website: https://curatorsearch.com
---
