---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Nace Ai Agentic Access
  operation_count: 13
  slug: nace-ai-agentic-access
  summary_line: 13 operations · 10 acting
api_count: 1
apis:
- baseURL: https://ndi-api.nace.ai/api/v1
  baseurl_source: declared
  description: The health API from Nace Ai — 1 operation(s) for health.
  name: Nace Ai Health API
  slug: nace-ai-health-api
- baseURL: https://ndi-api.nace.ai/api/v1
  baseurl_source: declared
  description: The public-api API from Nace Ai — 12 operation(s) for public-api.
  name: Nace Ai Public API
  slug: nace-ai-public-api-api
artifact_total: 11
collections:
- collection_type: open
  name: NDI Service health API
  slug: open-nace-ai-health-api
- collection_type: open
  name: NDI Service health public-api API
  slug: open-nace-ai-public-api-api
common:
- group: other
  href: https://artifacts.apis.io/nace-ai/capabilities/nace-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nace-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nace-ai/overlays/nace-ai-ndi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nace-ai-ndi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/nace-ai/agentic-access/nace-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nace-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/nace-ai/rate-limits/nace-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nace-ai-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/nace-ai/security/nace-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nace-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nace-ai/authentication/nace-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nace-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/errors/nace-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nace-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/conventions/nace-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nace-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/conventions/nace-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/nace-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/conformance/nace-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nace-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/lifecycle/nace-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nace-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nace-ai/data-model/nace-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nace-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/nace-ai/mcp/nace-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nace-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nace-ai/llms/nace-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nace-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/nace-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://nace.ai
- group: company
  title: ''
  type: Blog
  url: https://nace.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://nace.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nace.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nace.ai/policies/privacy-policy
created: '2026-07-17'
description: 'Nace.AI builds specialized AI models and agents that run enterprise business processes end-to-end on small models customers control. Its NAVI product automates workflows across financial auditing, loan processing, billing, accounts payable, and claims. Nace Document Intelligence (NDI) is its public API: an API-key REST + MCP service that parses documents to high-fidelity markdown, categorizes contents against a taxonomy, grounds values to precise page coordinates, and extracts schema-shaped structured JSON via async jobs.'
image: https://nace.ai
layout: provider
mcp_servers:
- description: MCP server; 6 tools listed.
  name: NDI MCP Server
  slug: ndi-mcp-server
modified: '2026-09-16'
name: Nace Ai
nav: Providers
network: true
overview: 'Nace Ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Public API. Tagged areas include Company, Artificial Intelligence, Document Intelligence, Document Processing, and Data Extraction.


  Nace Ai''s developer surface includes authentication, engineering blog, signup flow, and 17 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Nace Ai Rate Limits
  slug: nace-ai-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.9
    developer_ergonomics: 44.6
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nace-ai/nace-ai-2026-08-07T184600.png
security:
- kind: authentication
  name: Nace Ai Authentication
  slug: nace-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nace Ai Domain Security
  slug: nace-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: nace-ai-extract-document-data
  slug: nace-ai-extract-document-data
- name: nace-ai-parse-and-ground
  slug: nace-ai-parse-and-ground
slug: nace-ai
tags:
- Company
- Artificial Intelligence
- Document Intelligence
- Document Processing
- Data Extraction
- OCR
- Machine Learning
- Enterprise Automation
- MCP
website: https://nace.ai
---
