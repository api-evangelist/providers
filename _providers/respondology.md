---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
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
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://webhooks.respondology.io/
  baseurl_source: declared
  description: 'Respondology delivers comment moderation and analysis results via webhook. These webhooks provide the outcome of moderation decisions along with any recorded analysis data. To configure or update the '
  name: Respondology Comment Results API
  slug: respondology-comment-results-api
- baseURL: https://webhooks.respondology.io/
  baseurl_source: declared
  description: Send comments to Respondology for moderation and analysis, update or remove them as needed, and check their current processing status.
  name: Respondology Comments API
  slug: respondology-comments-api
- baseURL: https://webhooks.respondology.io/
  baseurl_source: declared
  description: The following table lists all of the possible moderation rejection reasons that may be returned in the `moderation_reasons` array when a comment is rejected, ordered alphabetically. If a comment is re
  name: Respondology Moderation Reasons API
  slug: respondology-moderation-reasons-api
- baseURL: https://webhooks.respondology.io/
  baseurl_source: declared
  description: Respondology delivers post analysis and recording results via webhook. To configure or update the endpoint where result webhooks are sent, contact your account manager.
  name: Respondology Post Results API
  slug: respondology-post-results-api
- baseURL: https://webhooks.respondology.io/
  baseurl_source: declared
  description: Submit posts to Respondology for moderation and analysis, update or remove them as needed, and check their current processing status.
  name: Respondology Posts API
  slug: respondology-posts-api
artifact_total: 11
asyncapis:
- description: ''
  name: Respondology Webhooks
  slug: respondology-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/respondology-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/respondology-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/respondology-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://respondology.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://respondology.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://respondology.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://respondology.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://respondology.com/company/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://respondology.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/respondology
- group: start
  title: ''
  type: Login
  url: https://v2.app.respondology.io/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.respondology.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/respondology-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/respondology-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/respondology-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/respondology-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/respondology-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/respondology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/respondology-rate-limits.yml
created: '2026-08-26'
description: 'Respondology is a Boulder, Colorado social media Comment Activation Platform that helps brands moderate, analyze, and activate the conversations happening in their comment sections. Its three products share one platform: Moderate hides brand-damaging, spam, and toxic comments in under a second using keyphrase and business rules, generative AI, and human moderators across 100+ languages; Respond centralizes paid and organic social comments into a unified inbox and uses AI agents to reply in the brand voice; and Discover pulls comment data from any public handle for sentiment, theme, and trend analysis. Respondology publishes a public OpenAPI 3.1 contract for its external moderation API, letting customers submit posts and comments for moderation and analysis and receive results asynchronously over webhooks.'
image: https://avatars.githubusercontent.com/u/143194429?v=4
layout: provider
modified: '2026-08-26'
name: Respondology
nav: Providers
network: true
overview: 'Respondology publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Comment Results API, Comments API, Moderation Reasons API, and 2 more. Tagged areas include Company, Content Moderation, Social-Media, Comment Moderation, and Trust and Safety.


  The Respondology catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Respondology''s developer surface includes pricing, support, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: Respondology Plans Pricing
  plan_count: 3
  slug: respondology-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Respondology Rate Limits
  slug: respondology-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 8.3
    contract_quality: 51.4
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 8.3
    operational_transparency: 26.3
  previous_composite: 39.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/respondology/refs/heads/main/screenshots/respondology-2026-09-02T153555.png
security:
- kind: authentication
  name: Respondology Authentication
  slug: respondology-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Respondology Domain Security
  slug: respondology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Respondology Trust Center
  slug: respondology-trust-center
  summary_line: SOC 2, GDPR
slug: respondology
tags:
- Company
- Content Moderation
- Social-Media
- Comment Moderation
- Trust and Safety
- Artificial Intelligence
- Brand Protection
- Social Listening
- Webhook
- Marketing
website: https://respondology.com/
---
