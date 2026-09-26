---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Moonbounce Agentic Access
  operation_count: 8
  slug: moonbounce-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- baseURL: https://gateway.app.clavata.ai:8443
  baseurl_source: declared
  description: The Batch Processing API from Moonbounce — 2 operation(s) for batch processing.
  name: Moonbounce Batch Processing API
  slug: moonbounce-batch-processing-api
- baseURL: https://gateway.app.clavata.ai:8443
  baseurl_source: declared
  description: The Create Jobs API from Moonbounce — 2 operation(s) for create jobs.
  name: Moonbounce Create Jobs API
  slug: moonbounce-create-jobs-api
- baseURL: https://gateway.app.clavata.ai:8443
  baseurl_source: declared
  description: The Get Jobs API from Moonbounce — 2 operation(s) for get jobs.
  name: Moonbounce Get Jobs API
  slug: moonbounce-get-jobs-api
- baseURL: https://gateway.app.clavata.ai:8443
  baseurl_source: declared
  description: The Labels API from Moonbounce — 1 operation(s) for labels.
  name: Moonbounce Labels API
  slug: moonbounce-labels-api
artifact_total: 13
asyncapis:
- description: ''
  name: Moonbounce Webhooks
  slug: moonbounce-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clavata Public API v1 Batch Processing API
  slug: open-moonbounce-batch-processing-api
- collection_type: open
  name: Clavata Public API v1 Batch Processing Create Jobs API
  slug: open-moonbounce-create-jobs-api
- collection_type: open
  name: Clavata Public API v1 Batch Processing Get Jobs API
  slug: open-moonbounce-get-jobs-api
- collection_type: open
  name: Clavata Public API v1 Batch Processing Labels API
  slug: open-moonbounce-labels-api
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/openapi/_original/moonbounce-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/moonbounce-openapi-original.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/overlays/moonbounce-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moonbounce-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/authentication/moonbounce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moonbounce-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/agentic-access/moonbounce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moonbounce-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/security/moonbounce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moonbounce-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/packages/moonbounce-packages.yml
  title: ''
  type: Packages
  url: packages/moonbounce-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/packages/moonbounce-packages.yml
  title: ''
  type: SDKs
  url: packages/moonbounce-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/mcp/moonbounce-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moonbounce-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/llms/moonbounce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moonbounce-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/errors/moonbounce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moonbounce-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/conventions/moonbounce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moonbounce-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/data-model/moonbounce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moonbounce-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/conformance/moonbounce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moonbounce-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/lifecycle/moonbounce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moonbounce-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/changelog/moonbounce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moonbounce-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/asyncapi/moonbounce-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/moonbounce-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clavata.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clavata.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clavata.ai/getting_started/getting_started_guide
- group: other
  title: ''
  type: Playground
  url: https://play.moonbounce.io
- group: company
  title: ''
  type: Blog
  url: https://moonbounce.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://moonbounce.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://web.app.clavata.ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@moonbounce.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moonbounce.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moonbounce.io/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clavataai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moonbounceio
- group: company
  title: ''
  type: Website
  url: https://moonbounce.io
created: '2026-07-17'
description: Moonbounce (formerly Clavata) is a realtime AI control and content-moderation platform. Its policy-first engine uses a concise, structured policy syntax to evaluate text and image content in real time and enforce an organization's safety policies at scale. The Clavata Public API v1 exposes content-evaluation jobs, bulk batch processing (CSV via presigned URL), real-time streaming evaluation, completion webhooks, and label evaluation, backed by Python, JavaScript/TypeScript, and Go SDKs and bearer-token API keys. Founded by ex-Meta Integrity and ex-Apple AI-infrastructure leaders and backed by Amplify Partners.
image: https://framerusercontent.com/assets/qhocdI2pyd7eqIyEeG1ZxNPvsgw.png
layout: provider
modified: '2026-07-20'
name: Moonbounce
nav: Providers
network: true
overview: 'Moonbounce publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch Processing API, Create Jobs API, Get Jobs API, and 1 more. Tagged areas include Company, Ai Ml, Content Moderation, Trust and Safety, and AI Governance.


  The Moonbounce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moonbounce''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 60.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/moonbounce/refs/heads/main/screenshots/moonbounce-2026-08-07T184233.png
security:
- kind: authentication
  name: Moonbounce Authentication
  slug: moonbounce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moonbounce Domain Security
  slug: moonbounce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moonbounce
tags:
- Company
- Ai Ml
- Content Moderation
- Trust and Safety
- AI Governance
- Policy Enforcement
- Content Evaluation
website: https://moonbounce.io
---
