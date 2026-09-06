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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Framework-agnostic HTTP API behind the AI Autocomplete SDKs. A single POST /api/suggest endpoint drives keystroke-by-keystroke guided autocomplete over a placeholder-based query model, with a POST /ap
  name: AI Autocomplete API
  slug: ai-autocomplete-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://magicx.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai-autocomplete.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ai-autocomplete.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ai-autocomplete.com/docs/http/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://ai-autocomplete.com/docs/http/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://ai-autocomplete.com/other/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://ai-autocomplete.com/other/faqs
- group: start
  title: ''
  type: Login
  url: https://ai-autocomplete.com/account/keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai-autocomplete.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-autocomplete.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://ai-autocomplete.com/other/enterprise
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magicx-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/magicx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/magicx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magicx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/magicx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/magicx-problem-types.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/magicx-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/magicx-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magicx-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: MagicX Inc. builds software that lets people take actions instantly from any text box. Its flagship developer product, AI Autocomplete, is a drop-in SDK and HTTP API that turns a blank input into instant intent — guiding users on what to type with roughly 200ms suggestions, delivered as native SDKs for React, Angular, Vanilla JS and Swift or a framework-agnostic HTTP API. Auth uses public, secret, and short-lived access-token keys, and pricing is usage-based per prediction with a SOC 2 enterprise tier. MagicX also ships Hero Assistant, a consumer AI assistant. The company is backed by Forerunner Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magicx.png
layout: provider
modified: '2026-07-20'
name: MagicX
nav: Providers
network: true
overview: 'MagicX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Autocomplete, Developer Tools, and SDK.


  MagicX''s developer surface includes documentation, API reference, getting-started guide, pricing, authentication, and 16 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magicx/refs/heads/main/screenshots/magicx-2026-07-25T225856.png
security:
- kind: authentication
  name: Magicx Authentication
  slug: magicx-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Magicx Domain Security
  slug: magicx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: magicx
tags:
- Company
- Artificial Intelligence
- Autocomplete
- Developer Tools
- SDK
- Natural-Language
- Productivity
- Machine-Learning
website: https://magicx.ai
---
