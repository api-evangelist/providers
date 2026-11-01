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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DataBahn.ai provides an agentic data control plane for enterprise telemetry, but no machine‑readable API contract was found.
  name: DataBahn AI API
  slug: databahn-ai-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/databahn-ai/llms/databahn-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/databahn-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/databahn-ai/hosts/databahn-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/databahn-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/databahn-ai/vendors/databahn-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/databahn-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.databahn.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.databahn.ai/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.databahn.ai/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.databahn.ai/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.databahn.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.databahn.ai/blog/data-onboarding-in-the-modern-enterprise
- group: auth
  href: https://artifacts.apis.io/databahn-ai/security/databahn-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/databahn-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.databahn.ai
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract discovered despite public docs.
  evidence:
  - status: 0
    url: https://api.databahn.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: DataBahn.ai provides an agentic data control plane that automates, enriches, and governs enterprise telemetry for security, observability, and AI use cases. The platform unifies data ingestion, enrichment, routing, and AI‑ready preparation, offering products like Data Pipeline, Federated Search, and Autonomous In‑Stream Data Intelligence, while integrating with major security and cloud tools.
image: https://cdn.prod.website-files.com/67eb571d0fe797071c2c2759/680cd260793b86722f0dcd57_open-graph.jpg
layout: provider
modified: '2026-10-22'
name: DataBahn.ai
nav: Providers
network: true
overview: 'DataBahn.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Pipeline, Security, Observability, AI Agents, and Edge Telemetry.


  DataBahn.ai''s developer surface includes engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Databahn Ai Domain Security
  slug: databahn-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: databahn-ai
tags:
- Data Pipeline
- Security
- Observability
- AI Agents
- Edge Telemetry
- Data Fabric
- SIEM Optimization
- Federated Search
website: https://www.databahn.ai
---
