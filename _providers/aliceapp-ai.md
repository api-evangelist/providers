---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Aliceapp Ai Agentic Access
  operation_count: 5
  slug: aliceapp-ai-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: API for Alice voice recorder and transcription service.
  name: Alice API
  slug: alice-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/aliceapp-ai/agentic-access/aliceapp-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aliceapp-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aliceapp-ai/plans/aliceapp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aliceapp-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aliceapp-ai/rules/aliceapp-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/aliceapp-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/aliceapp-ai/vocabulary/aliceapp-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aliceapp-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aliceapp-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.aliceapp.ai/
- group: auth
  href: https://artifacts.apis.io/aliceapp-ai/authentication/aliceapp-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aliceapp-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/aliceapp-ai/errors/aliceapp-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aliceapp-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aliceapp-ai/conformance/aliceapp-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aliceapp-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aliceapp-ai/llms/aliceapp-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aliceapp-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aliceapp-ai/mcp/aliceapp-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aliceapp-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/aliceapp-ai/hosts/aliceapp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aliceapp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/aliceapp-ai/vendors/aliceapp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aliceapp-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://aliceapp.ai/security
- group: company
  title: ''
  type: Newsroom
  url: https://aliceapp.ai/press
- group: start
  title: ''
  type: Login
  url: https://aliceapp.ai/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://aliceapp.ai/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://aliceapp.ai/api-docs/index.html
- group: auth
  href: https://artifacts.apis.io/aliceapp-ai/security/aliceapp-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aliceapp-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aliceapp-ai/security/aliceapp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aliceapp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aliceapp.ai/
- group: company
  title: ''
  type: About
  url: https://aliceapp.ai/about
- group: commercial
  title: ''
  type: Pricing
  url: https://aliceapp.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aliceapp.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aliceapp.ai/tos
- group: operate
  title: ''
  type: Support
  url: https://vbx.to/@alice
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://aliceapp.ai/mcp/v1
  - status: 200
    url: https://aliceapp.ai/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Alice is a private voice recorder and AI transcription app for iPhone and the web. It records or imports audio and video and transcribes it in over 100 languages with high accuracy. The service is HIPAA, SOC 2, GDPR and CCPA compliant, targeting journalists, legal teams, healthcare professionals, researchers, and podcasters. It integrates with Slack, Dropbox, Notion, Discord, OneDrive, Outlook, Gmail, and more, offering multiple export formats and team collaboration features.
image: https://aliceapp.ai/marketing/6900e569fbfbf0e5832853df_alice-secure-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at aliceapp.ai.
  name: Alice MCP Server
  slug: aliceapp-ai-mcp-yml
modified: '2026-11-01'
name: Alice
nav: Providers
network: true
overview: 'Alice is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Transcription, Artificial Intelligence, Privacy, and Healthcare.


  The Alice catalog on APIs.io includes 1 Spectral governance ruleset.


  Alice''s developer surface includes authentication, getting-started guide, API reference, pricing, support, and 21 more developer resources.'
plans:
- name: Aliceapp Ai Plans Pricing
  plan_count: 3
  slug: aliceapp-ai-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Aliceapp Ai Rate Limits
  slug: aliceapp-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Alice API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: aliceapp-ai-rules
scopes:
- name: Aliceapp Ai Scopes
  scope_count: 0
  slug: aliceapp-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 0.0
    developer_ergonomics: 30.2
    discoverability: 65.8
    operational_transparency: 5.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 29.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aliceapp Ai Authentication
  slug: aliceapp-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aliceapp Ai Domain Security
  slug: aliceapp-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aliceapp Ai Trust Center
  slug: aliceapp-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: aliceapp-ai
tags:
- Audio
- Transcription
- Artificial Intelligence
- Privacy
- Healthcare
website: https://aliceapp.ai/
---
