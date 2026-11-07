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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Symbiotic Agentic Access
  operation_count: 22
  slug: symbiotic-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 2
apis:
- description: The SymbioticAPIService API from Symbiotic — 22 operation(s) for symbioticapiservice.
  name: Symbiotic SymbioticAPIService API
  slug: symbiotic-symbioticapiservice-api
artifact_total: 8
collections:
- collection_type: open
  name: v1/api.proto SymbioticAPIService API
  slug: open-symbiotic-symbioticapiservice-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://resources.symbiotic.fi/rss.xml
- group: agent
  href: https://artifacts.apis.io/symbiotic/skills/symbiotic-query-validator-set.md
  title: ''
  type: AgentSkill
  url: skills/symbiotic-query-validator-set.md
- group: agent
  href: https://artifacts.apis.io/symbiotic/mcp/symbiotic-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/symbiotic-mcp.yml
- group: other
  href: https://artifacts.apis.io/symbiotic/overlays/symbiotic-relay-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/symbiotic-relay-overlay.yaml
- group: other
  href: https://artifacts.apis.io/symbiotic/a2a/symbiotic-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/symbiotic-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://symbiotic.fi
created: '2026-07-17'
description: 'Symbiotic is a company surfaced as a portfolio company of paradigm and added to the API Evangelist network as a stub for enrichment. Sector: crypto-defi. This profile is a lead awaiting the enrichment pipeline.'
layout: provider
modified: '2026-10-06'
name: Symbiotic
nav: Providers
network: true
overview: 'Symbiotic publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: SymbioticAPIService API. Tagged areas include Company, Crypto Defi, and A2A.


  The Symbiotic catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Symbiotic API Rules
  rule_count: 39
  severity_counts:
    error: 31
    hint: 0
    info: 4
    warn: 4
  slug: symbiotic-rules
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 24.5
    catalog_earned_first_party: 0.0
    catalog_gap: 90.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 32.4
    developer_ergonomics: 1.8
    discoverability: 42.9
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/symbiotic/symbiotic-2026-09-02T161442.png
security:
- kind: domain-security
  name: Symbiotic Domain Security
  slug: symbiotic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Symbiotic Vulnerability Disclosure
  slug: symbiotic-vulnerability-disclosure
  summary_line: disclosure policy published
skill_count: 2
skills:
- name: Query the Symbiotic Relay validator set
  slug: symbiotic-query-validator-set
- name: Sign a message and collect its aggregation proof
  slug: symbiotic-sign-and-aggregate
slug: symbiotic
tags:
- Company
- Crypto Defi
- A2A
website: https://symbiotic.fi
---
