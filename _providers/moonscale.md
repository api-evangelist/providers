---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.moonscale.com/
  - https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/createApiKey
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Moonscale Agentic Access
  operation_count: 4
  slug: moonscale-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api-prd.moonscale.com
  baseurl_source: declared
  description: The Live Avatar API from Moonscale — 2 operation(s) for live avatar.
  name: Moonscale Live Avatar API
  slug: moonscale-live-avatar-api
- baseURL: https://api-prd.moonscale.com
  baseurl_source: declared
  description: The Video Generation API from Moonscale — 2 operation(s) for video generation.
  name: Moonscale Video Generation API
  slug: moonscale-video-generation-api
artifact_total: 11
asyncapis:
- description: ''
  name: Moonscale Webhooks
  slug: moonscale-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/moonscale/agentic-access/moonscale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moonscale-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/moonscale/security/moonscale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moonscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moonscale.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moonscale.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.moonscale.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moonscale.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moonscale.com/legal/terms-and-conditions
- group: other
  title: ''
  type: Imprint
  url: https://www.moonscale.com/legal/imprint
- group: docs
  title: ''
  type: Documentation
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/liveAvatarsCreateRoom
- group: start
  title: ''
  type: GettingStarted
  url: https://vidlab7-d7584a5d.mintlify.app/api-reference/endpoint/createApiKey
- group: start
  title: ''
  type: Login
  url: https://app.moonscale.com
- group: agent
  href: https://artifacts.apis.io/moonscale/llms/moonscale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moonscale-llms.txt
- group: auth
  href: https://artifacts.apis.io/moonscale/authentication/moonscale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moonscale-authentication.yml
- group: design
  href: https://artifacts.apis.io/moonscale/conventions/moonscale-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moonscale-conventions.yml
- group: design
  href: https://artifacts.apis.io/moonscale/errors/moonscale-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moonscale-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moonscale/data-model/moonscale-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moonscale-data-model.yml
- group: build
  href: https://artifacts.apis.io/moonscale/examples/moonscale-examples.yml
  title: ''
  type: Examples
  url: examples/moonscale-examples.yml
- group: design
  href: https://artifacts.apis.io/moonscale/asyncapi/moonscale-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moonscale-webhooks.yml
- group: design
  href: https://artifacts.apis.io/moonscale/lifecycle/moonscale-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moonscale-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moonscale/conformance/moonscale-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moonscale-conformance.yml
- group: build
  href: https://artifacts.apis.io/moonscale/packages/moonscale-packages.yml
  title: ''
  type: Packages
  url: packages/moonscale-packages.yml
- group: commercial
  href: https://artifacts.apis.io/moonscale/plans/moonscale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moonscale-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/moonscale/rate-limits/moonscale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moonscale-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/moonscale/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/moonscale/overlays/moonscale-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moonscale-api-overlay.yaml
created: '2026-07-17'
description: 'Moonscale (formerly VidLab7) is a Munich-based AI sales advisor platform whose "Digital Sales Human" avatars automate top-of-funnel sales conversations — pitching products, qualifying inbound buyers, running interactive demos, handling objections, booking meetings and following up around the clock across websites, landing pages, emails and apps, with support for 130+ languages and CRM connections to Salesforce, HubSpot, Pipedrive, Slack and Clay. Moonscale does publish a real, machine-readable API: an OpenAPI 3.0.1 document titled "Moonscale API" served from its Mintlify documentation site, covering four operations across two surfaces — live-avatar meeting rooms with conversation transcripts and summaries (/api/v1/), and asynchronous studio-avatar video generation with a caller-registered completion webhook (/api/studio-avatar/). Requests authenticate with an x-api-key header against https://api-prd.moonscale.com; keys are issued from Moonscale Studio, but API access is feature-flagged
  per account and must be requested from support. There is no first-party SDK, MCP server, agent card, status page, changelog, published rate limit or published price. Backed by EQT Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonscale.png
layout: provider
modified: '2026-08-14'
name: Moonscale
nav: Providers
network: true
overview: 'Moonscale publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Live Avatar API and Video Generation API. Tagged areas include Company, Artificial Intelligence, Sales, Sales Automation, and Lead Generation.


  The Moonscale catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Moonscale''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, authentication, code examples, and 19 more developer resources.'
plans:
- name: Moonscale Plans Pricing
  plan_count: 0
  slug: moonscale-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Moonscale Rate Limits
  slug: moonscale-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Moonscale API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: moonscale-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moonscale/moonscale-2026-08-07T184246.png
security:
- kind: authentication
  name: Moonscale Authentication
  slug: moonscale-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Moonscale Domain Security
  slug: moonscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Generate a studio avatar video and collect the result
  slug: moonscale-generate-avatar-video
- name: Run a live AI sales avatar meeting and collect the transcript
  slug: moonscale-run-live-avatar-meeting
slug: moonscale
tags:
- Company
- Artificial Intelligence
- Sales
- Sales Automation
- Lead Generation
- AI Agents
- Conversational AI
- CRM
- Video Generation
- Avatars
- Speech
- Germany
website: https://www.moonscale.com/
---
