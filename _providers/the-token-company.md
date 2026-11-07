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
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.thetokencompany.com
  baseurl_source: declared
  description: Prompt and conversation compression
  name: The Token Company Compression API
  slug: the-token-company-compression-api
- baseURL: https://api.thetokencompany.com
  baseurl_source: declared
  description: Compressed web search
  name: The Token Company Search API
  slug: the-token-company-search-api
artifact_total: 12
collections:
- collection_type: open
  name: The Token Company Compression API
  slug: open-the-token-company-compression-api
- collection_type: open
  name: The Token Company Compression Search API
  slug: open-the-token-company-search-api
common:
- group: commercial
  href: https://artifacts.apis.io/the-token-company/plans/the-token-company-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-token-company-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.thetokencompany.com/
- group: other
  href: https://artifacts.apis.io/the-token-company/overlays/the-token-company-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/the-token-company-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/the-token-company/security/the-token-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-token-company-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thetokencompany.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://thetokencompany.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://thetokencompany.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thetokencompany.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://thetokencompany.com/blog
- group: operate
  title: ''
  type: Support
  url: https://thetokencompany.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheTokenCompany
- group: commercial
  title: ''
  type: Pricing
  url: https://thetokencompany.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.thetokencompany.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thetokencompany.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thetokencompany.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thetokencompany.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.thetokencompany.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.thetokencompany.com
- group: build
  href: https://artifacts.apis.io/the-token-company/packages/the-token-company-packages.yml
  title: ''
  type: Packages
  url: packages/the-token-company-packages.yml
- group: build
  href: https://artifacts.apis.io/the-token-company/packages/the-token-company-packages.yml
  title: ''
  type: SDKs
  url: packages/the-token-company-packages.yml
- group: auth
  href: https://artifacts.apis.io/the-token-company/authentication/the-token-company-authentication.yml
  title: ''
  type: Authentication
  url: authentication/the-token-company-authentication.yml
- group: design
  href: https://artifacts.apis.io/the-token-company/errors/the-token-company-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/the-token-company-problem-types.yml
- group: design
  href: https://artifacts.apis.io/the-token-company/conventions/the-token-company-conventions.yml
  title: ''
  type: Conventions
  url: conventions/the-token-company-conventions.yml
- group: design
  href: https://artifacts.apis.io/the-token-company/lifecycle/the-token-company-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/the-token-company-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/the-token-company/changelog/the-token-company-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/the-token-company-changelog.yml
- group: agent
  href: https://artifacts.apis.io/the-token-company/mcp/the-token-company-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/the-token-company-mcp.yml
- group: agent
  href: https://artifacts.apis.io/the-token-company/llms/the-token-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-token-company-llms.txt
- group: design
  href: https://artifacts.apis.io/the-token-company/conformance/the-token-company-conformance.yml
  title: ''
  type: Conformance
  url: conformance/the-token-company-conformance.yml
- group: design
  href: https://artifacts.apis.io/the-token-company/data-model/the-token-company-data-model.yml
  title: ''
  type: DataModel
  url: data-model/the-token-company-data-model.yml
- group: agent
  href: https://artifacts.apis.io/the-token-company/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: The Token Company builds LLM input-compression middleware. A single API call runs a prompt, a full chat conversation, or web-search results through their bear compression models (bear-2 latest, plus bear-1.2/1.1/1) to strip low-signal tokens before the text reaches a language model, cutting cost and latency while preserving output quality. It ships drop-in Python and Node.js SDKs that wrap the OpenAI, Anthropic, Vercel AI SDK, and OpenRouter clients so existing apps compress automatically, plus content-protection (ttc_safe) tags, per-app usage tagging, and a zero-data-retention policy. A Y Combinator (W26) company based in San Francisco.
finops:
- has_sources: true
  method: derived
  name: The Token Company Finops
  primary_unit: ''
  service_category: ''
  slug: the-token-company-finops
  template: true
image: https://thetokencompany.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: The Token Company
nav: Providers
network: true
overview: 'The Token Company publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Compression API and Search API. Tagged areas include Company, LLM, Artificial Intelligence, Prompt Compression, and Tokens.


  The The Token Company catalog on APIs.io includes 1 Spectral governance ruleset.


  The Token Company''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: The Token Company Plans Pricing
  plan_count: 2
  slug: the-token-company-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: The Token Company API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: the-token-company-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 43.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/the-token-company/the-token-company-2026-08-17T082339.png
security:
- kind: authentication
  name: The Token Company Authentication
  slug: the-token-company-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Token Company Domain Security
  slug: the-token-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: The Token Company Trust Center
  slug: the-token-company-trust-center
  summary_line: HIPAA
skill_count: 2
skills:
- name: Compress a chat conversation in one request
  slug: the-token-company-compress-chat
- name: Compress a prompt before an LLM call
  slug: the-token-company-compress-prompt
slug: the-token-company
tags:
- Company
- LLM
- Artificial Intelligence
- Prompt Compression
- Tokens
- Cost Optimization
- Developer Tools
- Middleware
website: https://www.thetokencompany.com/
---
