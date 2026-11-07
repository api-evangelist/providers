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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI-powered supply chain verification and fraud detection for the organic agriculture industry.
  name: Atlas Verified API
  slug: atlas-verified-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/atlasverified-ai/plans/atlasverified-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlasverified-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/atlasverified-ai/authentication/atlasverified-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlasverified-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/atlasverified-ai/llms/atlasverified-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlasverified-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/atlasverified-ai/mcp/atlasverified-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlasverified-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/atlasverified-ai/well-known/atlasverified-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atlasverified-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/atlasverified-ai/well-known/atlasverified-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlasverified-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlasverified-ai/hosts/atlasverified-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasverified-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlasverified-ai/vendors/atlasverified-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasverified-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.atlasverified.ai/auth/sign-up
- group: auth
  href: https://artifacts.apis.io/atlasverified-ai/security/atlasverified-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasverified-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasverified.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://help.atlasverified.ai/en/
- group: docs
  title: ''
  type: APIReference
  url: https://help.atlasverified.ai/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://atlasverified.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://atlasverified.ai/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlasverified.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasverified.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.atlasverified.ai/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.atlasverified.ai/en/
coverage:
  checked: '2026-11-02'
  detail: Developer portal provides human-readable docs but no machine-readable API specification.
  evidence:
  - status: 200
    url: https://dev.atlasverified.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atlas Verified provides AI-powered supplier verification for global trade, offering rapid checks on organic certification, OFAC, FDA, and import documents to ensure trustworthy partnerships.
image: https://atlasverified.ai/atlas-agent-chat-share-landscape.jpg?v=20261017a
layout: provider
mcp_servers:
- description: Remote MCP server at api.atlasverified.ai.
  name: Atlas Verified MCP Server
  slug: atlasverified-ai-mcp-yml
modified: '2026-11-01'
name: Atlas Verified
nav: Providers
network: true
overview: 'Atlas Verified is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Verification, Trade, and Compliance.


  Atlas Verified''s developer surface includes authentication, signup flow, documentation, API reference, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Atlasverified Ai Plans Pricing
  plan_count: 3
  slug: atlasverified-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Atlasverified Ai Rate Limits
  slug: atlasverified-ai-rate-limits
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.3
    operational_transparency: 10.5
  previous_composite: 31.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlasverified Ai Authentication
  slug: atlasverified-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atlasverified Ai Domain Security
  slug: atlasverified-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlasverified-ai
tags:
- Company
- Artificial Intelligence
- Verification
- Trade
- Compliance
website: https://atlasverified.ai/
---
