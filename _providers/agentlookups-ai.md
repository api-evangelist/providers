---
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
  scored_at: '2026-10-31'
api_count: 6
apis:
- description: Checks a contractor's license by number or business name in official licensing-board records.
  name: Plumbline
  slug: plumbline
- description: What US pharmacies pay for a drug (CMS NADAC), a fair cash-price range, FDA generic equivalents and Medicare negotiated prices.
  name: CounterScript
  slug: counterscript
- description: Federal environmental records near a US address, drinking-water violations by county, and address due-diligence layers.
  name: GroundTruth
  slug: groundtruth
- description: Whether a Maryland property assessment is fair next to similar homes, with the appeal windows.
  name: Overassessed
  slug: overassessed
- description: Which governments make law at a US address, and the original text of US law with its citation, source and date.
  name: GroundRules
  slug: groundrules
- description: 'What labs, regulators and recalls have found in US packaged foods: lab results for metals and plastic chemicals, FDA recalls, additive rules, and FDA''s typical levels for each kind of food.'
  name: Spoon Scout
  slug: spoon-scout
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/agentlookups-ai/llms/agentlookups-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentlookups-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentlookups-ai/mcp/agentlookups-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentlookups-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentlookups-ai/well-known/agentlookups-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentlookups-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentlookups-ai/hosts/agentlookups-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentlookups-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentlookups-ai/security/agentlookups-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentlookups-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentlookups.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agentlookups.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://agentlookups.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://agentlookups.ai/docs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentlookups.ai/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentlookups.ai/terms/
created: '2026-10-29'
description: agentlookups.ai provides a suite of public‑record lookup tools for consumers and agents, offering APIs for contractor license verification, drug price transparency, environmental record access, and property‑assessment fairness. The platform hosts six services—license, drug price, environmental, property, food, and water—each exposed via a simple, unauthenticated MCP (Machine‑Connect‑Protocol) endpoint that returns JSON. Documentation is available at /docs/, with privacy and terms pages. The service is operated by TopHat Monkey Software LLC and aims to champion open data for everyday decisions.
image: https://agentlookups.ai/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at contractors.agentlookups.ai.
  name: agentlookups-ai MCP Server
  slug: agentlookups-ai-mcp-yml
modified: '2026-10-29'
name: agentlookups-ai
nav: Providers
network: true
overview: 'agentlookups-ai is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Public Records, Consumer Tools, API, Data, and Beta.


  agentlookups-ai''s developer surface includes documentation, API reference, getting-started guide, and 8 more developer resources.'
plans:
- name: Agentlookups Ai Plans Pricing
  plan_count: 0
  slug: agentlookups-ai-plans-pricing
random_paper: 19
scopes:
- name: Agentlookups Ai Scopes
  scope_count: 0
  slug: agentlookups-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 70.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentlookups Ai Authentication
  slug: agentlookups-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentlookups Ai Domain Security
  slug: agentlookups-ai-domain-security
  summary_line: TLSv1.3
slug: agentlookups-ai
tags:
- Public Records
- Consumer Tools
- API
- Data
- Beta
website: https://agentlookups.ai/
---
