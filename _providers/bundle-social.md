---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 119
  human_in_the_loop: 2
  name: Bundle Social Agentic Access
  operation_count: 195
  slug: bundle-social-agentic-access
  summary_line: 195 operations · 119 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The analytics API from bundle.social — 7 operation(s) for analytics.
  name: bundle.social Analytics API
  slug: bundle-social-analytics-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The app API from bundle.social — 1 operation(s) for app.
  name: bundle.social App API
  slug: bundle-social-app-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: Build, publish and monitor automation flows that react to incoming messages and comments, plus the per-account provider settings they rely on.
  name: bundle.social Automation API
  slug: bundle-social-automation-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The comment API from bundle.social — 7 operation(s) for comment.
  name: bundle.social Comment API
  slug: bundle-social-comment-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: Read and reply to Instagram and Facebook direct message conversations, react to messages, and send private replies to comments.
  name: bundle.social Conversation API
  slug: bundle-social-conversation-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The credit API from bundle.social — 2 operation(s) for credit.
  name: bundle.social Credit API
  slug: bundle-social-credit-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The misc API from bundle.social — 63 operation(s) for misc.
  name: bundle.social Misc API
  slug: bundle-social-misc-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The organization API from bundle.social — 6 operation(s) for organization.
  name: bundle.social Organization API
  slug: bundle-social-organization-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The post API from bundle.social — 6 operation(s) for post.
  name: bundle.social Post API
  slug: bundle-social-post-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The postCSV API from bundle.social — 4 operation(s) for postcsv.
  name: bundle.social Post CSV API
  slug: bundle-social-postcsv-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The postImport API from bundle.social — 4 operation(s) for postimport.
  name: bundle.social Post Import API
  slug: bundle-social-postimport-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The socialAccount API from bundle.social — 13 operation(s) for socialaccount.
  name: bundle.social Social Account API
  slug: bundle-social-socialaccount-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The team API from bundle.social — 2 operation(s) for team.
  name: bundle.social Team API
  slug: bundle-social-team-api
- baseURL: https://api.bundle.social
  baseurl_source: declared
  description: The upload API from bundle.social — 9 operation(s) for upload.
  name: bundle.social Upload API
  slug: bundle-social-upload-api
artifact_total: 24
common:
- group: auth
  href: https://artifacts.apis.io/bundle-social/well-known/bundle-social-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bundle-social-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/bundle-social/agentic-access/bundle-social-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bundle-social-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/bundle-social/rate-limits/bundle-social-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bundle-social-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bundle-social/plans/bundle-social-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bundle-social-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bundle-social/rules/bundle-social-rules.yml
  title: ''
  type: Spectral
  url: rules/bundle-social-rules.yml
- group: design
  href: https://artifacts.apis.io/bundle-social/vocabulary/bundle-social-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bundle-social-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bundle-social/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/bundle-social/cli/bundle-social-cli.yml
  title: ''
  type: CLI
  url: cli/bundle-social-cli.yml
- group: operate
  href: https://artifacts.apis.io/bundle-social/changelog/bundle-social-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bundle-social-changelog.yml
- group: design
  href: https://artifacts.apis.io/bundle-social/conventions/bundle-social-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bundle-social-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://bundle.social/trust
- group: auth
  title: ''
  type: Security
  url: https://bundle.social/trust
- group: auth
  href: https://artifacts.apis.io/bundle-social/authentication/bundle-social-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bundle-social-authentication.yml
- group: design
  href: https://artifacts.apis.io/bundle-social/errors/bundle-social-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bundle-social-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bundle-social/conformance/bundle-social-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bundle-social-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bundle-social/llms/bundle-social-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bundle-social-llms.txt
- group: other
  href: https://artifacts.apis.io/bundle-social/a2a/bundle-social-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bundle-social-a2a.yml
- group: auth
  href: https://artifacts.apis.io/bundle-social/well-known/bundle-social-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bundle-social-security.txt
- group: agent
  href: https://artifacts.apis.io/bundle-social/well-known/bundle-social-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bundle-social-well-known.yml
- group: other
  href: https://artifacts.apis.io/bundle-social/hosts/bundle-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bundle-social-hosts.yml
- group: other
  href: https://artifacts.apis.io/bundle-social/vendors/bundle-social-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bundle-social-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bundle.social/terms
- group: start
  title: ''
  type: SignUp
  url: https://bundle.social/auth/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bundle.social/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://info.bundle.social/changelog
- group: auth
  href: https://artifacts.apis.io/bundle-social/security/bundle-social-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bundle-social-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bundle-social/security/bundle-social-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bundle-social-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bundle-social/security/bundle-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bundle-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bundle.social
- group: docs
  title: ''
  type: Documentation
  url: https://info.bundle.social/api-reference/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://info.bundle.social
- group: docs
  title: ''
  type: APIReference
  url: https://info.bundle.social/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://info.bundle.social/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://bundle.social/contact
- group: company
  title: ''
  type: Blog
  url: https://bundle.social/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bundleglobal
- group: commercial
  title: ''
  type: Pricing
  url: https://bundle.social/#pricing
created: '2026-11-02'
description: bundle.social provides a unified social media API that enables developers to publish content, retrieve analytics, and manage comments across platforms such as Instagram, TikTok, YouTube, Facebook, and more. The service offers API key authentication via the x-api-key header, a consistent /api/v1 prefix for endpoints, and clear rate-limit guidance. It positions itself as an unlimited-account alternative to Zernio and Ayrshare, targeting automation tools and developers seeking scalable social media integration.
image: https://bundle.social/og.png
layout: provider
modified: '2026-11-02'
name: bundle.social
nav: Providers
network: true
overview: 'bundle.social publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, App API, Automation API, and 11 more. Tagged areas include Social, Media, Integration, Unlimited, and Automation.


  The bundle.social catalog on APIs.io includes 1 Spectral governance ruleset.


  bundle.social''s developer surface includes CLI, changelog, authentication, signup flow, documentation, API reference, getting-started guide, and 30 more developer resources.'
plans:
- name: Bundle Social Plans Pricing
  plan_count: 4
  slug: bundle-social-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Bundle Social Rate Limits
  slug: bundle-social-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: bundle.social API Rules
  rule_count: 54
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 3
  slug: bundle-social-rules
scopes:
- name: Bundle Social Scopes
  scope_count: 0
  slug: bundle-social-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 66.8
    catalog_earned_first_party: 24.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 48.4
    developer_ergonomics: 48.1
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bundle Social Authentication
  slug: bundle-social-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bundle Social Domain Security
  slug: bundle-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bundle Social Vulnerability Disclosure
  slug: bundle-social-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bundle Social Trust Center
  slug: bundle-social-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 1
skills:
- name: automation
  slug: bundle-social-automation
slug: bundle-social
tags:
- Social
- Media
- Integration
- Unlimited
- Automation
website: https://bundle.social
---
