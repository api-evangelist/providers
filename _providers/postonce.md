---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.6
  scored_at: '2026-10-17'
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
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/rules/postonce-rules.yml
  title: ''
  type: Spectral
  url: rules/postonce-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/json-ld/postonce-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postonce-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/vocabulary/postonce-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postonce-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/conformance/postonce-conformance.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/rate-limits/postonce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postonce-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/plans/postonce-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postonce-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/data-model/postonce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postonce-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/changelog/postonce-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postonce-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/conventions/postonce-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postonce-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/conventions/postonce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postonce-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/authentication/postonce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postonce-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/errors/postonce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postonce-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/llms/postonce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postonce-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/a2a/postonce-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/postonce-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/well-known/postonce-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postonce-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/hosts/postonce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postonce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/vendors/postonce-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/postonce/refs/heads/main/security/postonce-domain-security.yml
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


  PostOnce''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Postonce Plans Pricing
  plan_count: 6
  slug: postonce-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Postonce Rate Limits
  slug: postonce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: PostOnce API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: postonce-rules
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 77.0
    catalog_earned_first_party: 20.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 67.7
    developer_ergonomics: 47.6
    discoverability: 64.3
    operational_transparency: 42.1
  provenance:
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
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
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
