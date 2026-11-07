---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Postonce Agentic Access
  operation_count: 22
  slug: postonce-agentic-access
  summary_line: 22 operations · 14 acting
api_count: 1
apis:
- description: Public API for PostOnce paid users
  name: PostOnce Public API
  slug: postonce-public-api
- baseURL: https://postonce.to/api/public
  baseurl_source: declared
  description: The Accounts API from PostOnce — 3 operation(s) for accounts.
  name: PostOnce Accounts API
  slug: postonce-accounts-api
- baseURL: https://postonce.to/api/public
  baseurl_source: declared
  description: The Drafts API from PostOnce — 2 operation(s) for drafts.
  name: PostOnce Drafts API
  slug: postonce-drafts-api
- baseURL: https://postonce.to/api/public
  baseurl_source: declared
  description: The Media API from PostOnce — 2 operation(s) for media.
  name: PostOnce Media API
  slug: postonce-media-api
- baseURL: https://postonce.to/api/public
  baseurl_source: declared
  description: The Posts API from PostOnce — 5 operation(s) for posts.
  name: PostOnce Posts API
  slug: postonce-posts-api
- baseURL: https://postonce.to/api/public
  baseurl_source: declared
  description: The Workflows API from PostOnce — 2 operation(s) for workflows.
  name: PostOnce Workflows API
  slug: postonce-workflows-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/postonce/agentic-access/postonce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postonce-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/postonce/finops/postonce-finops.yml
  title: ''
  type: FinOps
  url: finops/postonce-finops.yml
- group: build
  href: https://artifacts.apis.io/postonce/integrations/postonce-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/postonce-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/postonce/capabilities/postonce-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/postonce-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/postonce/rules/postonce-rules.yml
  title: ''
  type: Spectral
  url: rules/postonce-rules.yml
- group: design
  href: https://artifacts.apis.io/postonce/json-ld/postonce-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postonce-context.jsonld
- group: design
  href: https://artifacts.apis.io/postonce/vocabulary/postonce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postonce-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/postonce/conformance/postonce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postonce-conformance.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postonce.to/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postonce.to/privacy-policy
- group: operate
  href: https://artifacts.apis.io/postonce/rate-limits/postonce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postonce-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/postonce/plans/postonce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postonce-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/postonce/data-model/postonce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postonce-data-model.yml
- group: operate
  href: https://artifacts.apis.io/postonce/changelog/postonce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postonce-changelog.yml
- group: design
  href: https://artifacts.apis.io/postonce/conventions/postonce-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postonce-conventions.yml
- group: design
  href: https://artifacts.apis.io/postonce/conventions/postonce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postonce-conventions.yml
- group: auth
  href: https://artifacts.apis.io/postonce/authentication/postonce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postonce-authentication.yml
- group: design
  href: https://artifacts.apis.io/postonce/errors/postonce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postonce-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/postonce/llms/postonce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postonce-llms.txt
- group: other
  href: https://artifacts.apis.io/postonce/a2a/postonce-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/postonce-a2a.yml
- group: agent
  href: https://artifacts.apis.io/postonce/well-known/postonce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postonce-well-known.yml
- group: other
  href: https://artifacts.apis.io/postonce/hosts/postonce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postonce-hosts.yml
- group: other
  href: https://artifacts.apis.io/postonce/vendors/postonce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postonce-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://postonce.to/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postoncehq
- group: auth
  href: https://artifacts.apis.io/postonce/security/postonce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postonce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postonce.to
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postonce.to/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.postonce.to/api-reference/list-accounts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.postonce.to/getting-started/authentication
- group: operate
  title: ''
  type: Support
  url: https://postonce.to/contact
- group: company
  title: ''
  type: Blog
  url: https://postonce.to/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://postonce.to/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.postonce.to/mcp
  - status: null
    url: https://postonce.to/openapi.json
  - status: 401
    url: https://postonce.to/mcp
  - status: 200
    url: https://postonce.to
  reason: partner-login
  state: gated
created: '2026-10-14'
description: PostOnce is a cross‑posting platform that lets creators and businesses publish content to multiple social media channels from a single dashboard. Users can connect accounts on TikTok, Instagram, YouTube, Facebook, LinkedIn, X, Threads, Bluesky, Pinterest and more, then schedule or instantly push posts across all selected networks. The service offers integrations with tools like ChatGPT, Canva, and n8n, and provides API access for automating workflows, managing media, and tracking performance.
finops:
- has_sources: true
  method: derived
  name: Postonce Finops
  primary_unit: seat
  service_category: ''
  slug: postonce-finops
  template: false
image: https://postonce.to/og-image-v3.png?v=1
json_schemas:
- name: Account
  property_count: 9
  slug: postonce-account
- name: ConnectAccountResponse
  property_count: 1
  slug: postonce-connect-account-response
- name: MediaInput
  property_count: 7
  slug: postonce-media-input
- name: PostTargetInput
  property_count: 3
  slug: postonce-post-target-input
- name: Workflow
  property_count: 13
  slug: postonce-workflow
- name: WorkflowSettings
  property_count: 3
  slug: postonce-workflow-settings
jsonld:
- class_count: 14
  name: Postonce Context
  property_count: 53
  slug: postonce-context
layout: provider
modified: '2026-10-14'
name: PostOnce
nav: Providers
network: true
overview: 'PostOnce publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Drafts API, Media API, and 3 more. Tagged areas include Company, Social Media, Automation, and Marketing.


  The PostOnce catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PostOnce''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 26 more developer resources.'
plans:
- name: Postonce Plans Pricing
  plan_count: 6
  slug: postonce-plans-pricing
- name: Postonce Price Estimates
  plan_count: 0
  slug: postonce-price-estimates
random_paper: 11
rate_limits:
- limit_count: 2
  name: Postonce Rate Limits
  slug: postonce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: PostOnce API Rules
  rule_count: 54
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 4
  slug: postonce-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 80.8
    catalog_earned_first_party: 20.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 67.7
    developer_ergonomics: 29.8
    discoverability: 64.3
    operational_transparency: 39.5
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/postonce/postonce-2026-11-03T141425.png
security:
- kind: authentication
  name: Postonce Authentication
  slug: postonce-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Postonce Domain Security
  slug: postonce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postonce
tags:
- Company
- Social Media
- Automation
- Marketing
website: https://postonce.to
---
