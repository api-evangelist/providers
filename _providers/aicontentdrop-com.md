---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 3
  name: Aicontentdrop Com Agentic Access
  operation_count: 37
  slug: aicontentdrop-com-agentic-access
  summary_line: 37 operations · 24 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: API-key identity and credit balance
  name: AI Content Drop Account API
  slug: aicontentdrop-com-account-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: The Authentication API from AI Content Drop — 1 operation(s) for authentication.
  name: AI Content Drop Authentication API
  slug: aicontentdrop-com-authentication-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: Run many read operations in one request instead of looping.
  name: AI Content Drop Batch API
  slug: aicontentdrop-com-batch-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: Unauthenticated index and capability discovery
  name: AI Content Drop Discovery API
  slug: aicontentdrop-com-discovery-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: A drop is one piece of work that runs from research through concepts, a plan, generation and assembly without the caller moving it between endpoints. Available to accounts enabled for drops; every pat
  name: AI Content Drop Drops API
  slug: aicontentdrop-com-drops-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: Start and poll video/image generations (submit-and-poll)
  name: AI Content Drop Generation API
  slug: aicontentdrop-com-generation-api
- baseURL: https://aicontentdrop.com
  baseurl_source: declared
  description: Model catalogue and credit-cost estimates
  name: AI Content Drop Models API
  slug: aicontentdrop-com-models-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/aicontentdrop-com/agentic-access/aicontentdrop-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aicontentdrop-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/aicontentdrop-com/rate-limits/aicontentdrop-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aicontentdrop-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aicontentdrop-com/plans/aicontentdrop-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aicontentdrop-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/rules/aicontentdrop-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aicontentdrop-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/json-ld/aicontentdrop-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aicontentdrop-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/vocabulary/aicontentdrop-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aicontentdrop-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aicontentdrop-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/data-model/aicontentdrop-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aicontentdrop-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/aicontentdrop-com/cli/aicontentdrop-com-cli.yml
  title: ''
  type: CLI
  url: cli/aicontentdrop-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/aicontentdrop-com/changelog/aicontentdrop-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aicontentdrop-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/conventions/aicontentdrop-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aicontentdrop-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/conventions/aicontentdrop-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aicontentdrop-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/aicontentdrop-com/sandbox/aicontentdrop-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aicontentdrop-com-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://aicontentdrop.com/terms-of-use
- group: auth
  href: https://artifacts.apis.io/aicontentdrop-com/authentication/aicontentdrop-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicontentdrop-com-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://aicontentdrop.com/docs/versioning
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/lifecycle/aicontentdrop-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aicontentdrop-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/errors/aicontentdrop-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aicontentdrop-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aicontentdrop-com/conformance/aicontentdrop-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicontentdrop-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicontentdrop-com/llms/aicontentdrop-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicontentdrop-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aicontentdrop-com/a2a/aicontentdrop-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aicontentdrop-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aicontentdrop-com/mcp/aicontentdrop-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aicontentdrop-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aicontentdrop-com/well-known/aicontentdrop-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aicontentdrop-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aicontentdrop-com/well-known/aicontentdrop-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicontentdrop-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicontentdrop-com/hosts/aicontentdrop-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicontentdrop-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aicontentdrop-com/vendors/aicontentdrop-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aicontentdrop-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://aicontentdrop.com/support
- group: start
  title: ''
  type: SignUp
  url: https://aicontentdrop.com/register
- group: start
  title: ''
  type: GettingStarted
  url: https://aicontentdrop.com/.well-known/agent-onboarding.json
- group: auth
  href: https://artifacts.apis.io/aicontentdrop-com/security/aicontentdrop-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aicontentdrop-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aicontentdrop-com/security/aicontentdrop-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicontentdrop-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicontentdrop.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aicontentdrop.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://aicontentdrop.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aicontentdrop.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://aicontentdrop.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aicontentdrop.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicontentdrop.com/privacy-policy
created: '2026-11-01'
description: AI Content Drop provides an AI-powered video generation platform that transforms text prompts into high-quality video ads, marketing content, and social media clips. The service offers a suite of tools including ad‑spy, marketing‑studio, canvas planning, and a marketplace of AI models such as Kling, Sora, and Veo‑3. Users can create, edit, and publish videos quickly, leveraging features like caption generation, hashtag tools, and e‑commerce use‑case templates. The company emphasizes ease of use, rapid iteration, and integration with popular e‑commerce and social platforms, aiming to democratize video creation for creators, agencies, and brands.
image: https://aicontentdrop.com/og-home-2026-08.png
json_schemas:
- name: AgentRegistration
  property_count: 13
  slug: aicontentdrop-com-agent-registration
- name: DropBrief
  property_count: 8
  slug: aicontentdrop-com-drop-brief
- name: DropLanes
  property_count: 3
  slug: aicontentdrop-com-drop-lanes
- name: DropProposal
  property_count: 1
  slug: aicontentdrop-com-drop-proposal
- name: Plans
  property_count: 8
  slug: aicontentdrop-com-plans
- name: SignupInitiated
  property_count: 8
  slug: aicontentdrop-com-signup-initiated
jsonld:
- class_count: 53
  name: Aicontentdrop Com Context
  property_count: 205
  slug: aicontentdrop-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at aicontentdrop.com requiring OAuth.
  name: AI Content Drop MCP Server
  slug: aicontentdrop-com-mcp-yml
modified: '2026-11-01'
name: AI Content Drop
nav: Providers
network: true
overview: 'AI Content Drop publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authentication API, Batch API, and 4 more. Tagged areas include Artificial Intelligence, Video, Marketing, Content Creation, and Software-as-a-Service.


  The AI Content Drop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Content Drop''s developer surface includes CLI, changelog, sandbox, authentication, support, signup flow, getting-started guide, and 31 more developer resources.'
plans:
- name: Aicontentdrop Com Plans Pricing
  plan_count: 5
  slug: aicontentdrop-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 10
  name: Aicontentdrop Com Rate Limits
  slug: aicontentdrop-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AI Content Drop API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: aicontentdrop-com-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.3
    developer_ergonomics: 47.0
    discoverability: 65.0
    operational_transparency: 56.6
  previous_composite: 64.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicontentdrop Com Authentication
  slug: aicontentdrop-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aicontentdrop Com Domain Security
  slug: aicontentdrop-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aicontentdrop Com Vulnerability Disclosure
  slug: aicontentdrop-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: aicontentdrop-com-discover-nl-query
  slug: aicontentdrop-com-discover-nl-query
- name: aicontentdrop-com-estimate-model-cost
  slug: aicontentdrop-com-estimate-model-cost
- name: aicontentdrop-com-generate-video-and-poll
  slug: aicontentdrop-com-generate-video-and-poll
- name: aicontentdrop-com-get-account
  slug: aicontentdrop-com-get-account
- name: aicontentdrop-com-run-drop
  slug: aicontentdrop-com-run-drop
slug: aicontentdrop-com
tags:
- Artificial Intelligence
- Video
- Marketing
- Content Creation
- Software-as-a-Service
website: https://aicontentdrop.com/
---
