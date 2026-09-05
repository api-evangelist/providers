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
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Savvly Agentic Access
  operation_count: 12
  slug: savvly-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Comparisons API from Savvly — 2 operation(s) for comparisons.
  name: Savvly Comparisons API
  slug: savvly-comparisons-api
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Product API from Savvly — 6 operation(s) for product.
  name: Savvly Product API
  slug: savvly-product-api
- baseURL: https://api.savvly.com
  baseurl_source: spec
  description: The Projections API from Savvly — 4 operation(s) for projections.
  name: Savvly Projections API
  slug: savvly-projections-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Savvly Public Comparisons API
  slug: open-savvly-comparisons-api
- collection_type: open
  name: Savvly Public Comparisons Product API
  slug: open-savvly-product-api
- collection_type: open
  name: Savvly Public Comparisons Projections API
  slug: open-savvly-projections-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/savvly-compare-and-explain.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/savvly-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/savvly-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/savvly-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://savvly.com/
created: '2026-07-17'
description: Savvly is a company surfaced as a portfolio company of techstars and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: First-party Savvly MCP server exposing the Savvly Public API (product data, projections, comparisons, eligibility, FAQ) to AI agents. No authentication; rate-limited. Also distributed as npm @savvly/m
  name: Savvly MCP Server
  slug: savvly-mcp-server
modified: '2026-07-17'
name: Savvly
nav: Providers
network: true
overview: 'Savvly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Comparisons API, Product API, and Projections API. Tagged areas include Company.'
random_paper: 5
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 48.8
    developer_ergonomics: 1.8
    discoverability: 35.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 16.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/savvly/refs/heads/main/screenshots/savvly-2026-09-02T154449.png
security:
- kind: domain-security
  name: Savvly Domain Security
  slug: savvly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: savvly
tags:
- Company
website: https://savvly.com/
---
