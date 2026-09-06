---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://taito.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://taito.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://taito.ai/blog
- group: company
  title: ''
  type: About
  url: https://taito.ai/company
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taito.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taito.ai/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.taito.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.taito.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taitoai-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taitoai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taitoai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taitoai-llms.txt
created: '2026-07-17'
description: Taito.ai is an AI-native people operations (HRIS) platform headquartered in Helsinki, Finland, built for teams scaling from roughly 30 to 300 employees. It unifies the employee lifecycle in one system — a people directory, time-off and attendance, documents and eSignatures, and performance reviews — alongside AI "people agents" that handle onboarding, reminders, payroll reporting, and policy questions on demand from Slack, Claude, or any MCP-compatible tool. Every platform action is exposed over the Model Context Protocol rather than a public REST API. Pricing is a single per-seat tier covering both the people-ops and performance modules. The company is ISO 27001 certified and GDPR compliant, publishing audit reports on a Vanta-hosted Trust Center, and raised a $2.7M seed round led by Accel.
image: https://taito.ai/og-default.jpg
layout: provider
mcp_servers:
- description: ''
  name: Taito.ai MCP Server
  slug: taitoai-mcp-server
modified: '2026-07-21'
name: Taito.ai
nav: Providers
network: true
overview: 'Taito.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, HR, People Operations, and HRIS.


  Taito.ai''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 14.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taitoai/refs/heads/main/screenshots/taitoai-2026-09-02T162426.png
security:
- kind: domain-security
  name: Taitoai Domain Security
  slug: taitoai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Taitoai Trust Center
  slug: taitoai-trust-center
  summary_line: ISO 27001
slug: taitoai
tags:
- Company
- Artificial Intelligence
- HR
- People Operations
- HRIS
- Performance Management
- Employee Experience
- AI Agents
- MCP
- Software-as-a-Service
- GDPR
- ISO 27001
website: https://taito.ai/
---
