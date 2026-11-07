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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://mcp.agentcollect.com
  baseurl_source: declared
  description: 'AgentCollect API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgentCollect API
  slug: agentcollect-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/agentcollect-com/rules/agentcollect-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentcollect-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentcollect-com/vocabulary/agentcollect-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentcollect-com-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.agentcollect.com/security
- group: design
  href: https://artifacts.apis.io/agentcollect-com/conformance/agentcollect-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcollect-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcollect-com/llms/agentcollect-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcollect-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentcollect-com/well-known/agentcollect-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcollect-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentcollect-com/hosts/agentcollect-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcollect-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcollect-com/vendors/agentcollect-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcollect-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.agentcollect.com/security
- group: company
  title: ''
  type: Blog
  url: https://www.agentcollect.com/blog
- group: auth
  href: https://artifacts.apis.io/agentcollect-com/security/agentcollect-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agentcollect-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agentcollect-com/security/agentcollect-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcollect-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentcollect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentcollect.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentcollect.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentcollect.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentcollect.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentcollect.com/privacy
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or MCP spec found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.agentcollect.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AgentCollect provides an AI-powered billing concierge that integrates with existing billing systems to accelerate invoice payments, reduce disputes, and improve cash flow. Their platform offers voice‑enabled agents, AI audit tools, and customizable workflows for businesses of all sizes, emphasizing security and compliance. The service includes real‑time analytics, automated dispute handling, and seamless integration via API or spreadsheet upload, aiming to streamline the entire accounts‑receivable process.
image: https://www.agentcollect.com/og.png?v=5
layout: provider
modified: '2026-10-31'
name: AgentCollect
nav: Providers
network: true
overview: 'AgentCollect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Artificial Intelligence, Billing, Payments, and Software-as-a-Service.


  The AgentCollect catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentCollect''s developer surface includes engineering blog, documentation, getting-started guide, pricing, and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentCollect API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentcollect-com-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 27.6
    contract_governance: 35.6
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 30.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentcollect Com Domain Security
  slug: agentcollect-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Agentcollect Com Trust Center
  slug: agentcollect-com-trust-center
  summary_line: SOC 2, GDPR
slug: agentcollect-com
tags:
- Fintech
- Artificial Intelligence
- Billing
- Payments
- Software-as-a-Service
- Company
website: https://www.agentcollect.com/
---
