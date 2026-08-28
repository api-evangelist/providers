---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Respondology external API accepts posts and comments for moderation and analysis and returns results asynchronously over customer-configured webhooks. Nine REST operations cover submitting, updati
  name: Respondology API
  slug: respondology-api
artifact_total: 7
asyncapis:
- description: ''
  name: Respondology Webhooks
  slug: respondology-webhooks
common:
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
overview: 'Respondology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Content Moderation, Social Media, Comment Moderation, and Trust and Safety.


  The Respondology catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Respondology''s developer surface includes pricing, support, engineering blog, changelog, and 15 more developer resources.'
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
  composite: 42.7
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 20.5
    contract_quality: 55.5
    developer_ergonomics: 20.8
    discoverability: 79.6
    governance: 20.5
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
- Social Media
- Comment Moderation
- Trust and Safety
- Artificial Intelligence
- Brand Protection
- Social Listening
- Webhooks
- Marketing
website: https://respondology.com/
---
