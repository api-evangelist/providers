---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Vbout Agentic Access
  operation_count: 37
  slug: vbout-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 15
apis:
- description: The Account API from VBOUT — 2 operation(s) for account.
  name: VBOUT Account API
  slug: vbout-account-api
- description: The AIchatbot API from VBOUT — 4 operation(s) for aichatbot.
  name: VBOUT AIchatbot API
  slug: vbout-aichatbot-api
- description: The Application API from VBOUT — 1 operation(s) for application.
  name: VBOUT Application API
  slug: vbout-application-api
- description: The Automation API from VBOUT — 2 operation(s) for automation.
  name: VBOUT Automation API
  slug: vbout-automation-api
- description: The Contact API from VBOUT — 18 operation(s) for contact.
  name: VBOUT Contact API
  slug: vbout-contact-api
- description: The Email Marketing API from VBOUT — 10 operation(s) for email marketing.
  name: VBOUT Email Marketing API
  slug: vbout-email-marketing-api
- description: The EmailMarketing API from VBOUT — 25 operation(s) for emailmarketing.
  name: VBOUT EmailMarketing API
  slug: vbout-emailmarketing-api
- description: The Goals API from VBOUT — 6 operation(s) for goals.
  name: VBOUT Goals API
  slug: vbout-goals-api
- description: The Help API from VBOUT — 1 operation(s) for help.
  name: VBOUT Help API
  slug: vbout-help-api
- description: The Pipeline API from VBOUT — 3 operation(s) for pipeline.
  name: VBOUT Pipeline API
  slug: vbout-pipeline-api
- description: The Popups API from VBOUT — 5 operation(s) for popups.
  name: VBOUT Popups API
  slug: vbout-popups-api
- description: The Settings API from VBOUT — 8 operation(s) for settings.
  name: VBOUT Settings API
  slug: vbout-settings-api
- description: The Social Media API from VBOUT — 7 operation(s) for social media.
  name: VBOUT Social Media API
  slug: vbout-social-media-api
- description: The SocialMedia API from VBOUT — 7 operation(s) for socialmedia.
  name: VBOUT SocialMedia API
  slug: vbout-socialmedia-api
- description: The Users & Workflow API from VBOUT — 9 operation(s) for users & workflow.
  name: VBOUT Users & Workflow API
  slug: vbout-users-workflow-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vbout-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vbout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vbout.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vbout.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vbout.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vbout.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vbout.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.vbout.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vbout.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vbout
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vbout.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.vbout.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vbout.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vbout.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.vbout.com/apistatus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vbout-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/vboutcom
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/vbout
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/vboutcom
- group: auth
  title: ''
  type: Authentication
  url: authentication/vbout-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vbout-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vbout-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vbout-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vbout-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vbout-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vbout-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/vbout-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vbout-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vbout-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vbout-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vbout-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: VBOUT is an AI-enabled marketing automation platform used by agencies and small-to-mid-size businesses to run email marketing, social media scheduling, landing pages, popups, lead scoring, and an AI chatbot from one place. The VBOUT REST API (v1.0 at api.vbout.com/1) exposes the platform programmatically — contacts, lists, audiences, email campaigns and stats, social channels, calendar and posts, conversion goals, sub-users and groups, on-site engagement actions, automations, pipeline boards, and account settings — authenticated with an account API key, with responses in JSON or XML and a documented 15 requests/second rate limit. VBOUT is a 500 Global portfolio company.
image: https://developers.vbout.com/images/front/icons/logo-square-114x114.png
layout: provider
mcp_servers:
- description: ''
  name: vbout-mcp.yml
  slug: vbout-mcpyml
modified: '2026-07-21'
name: VBOUT
nav: Providers
network: true
overview: 'VBOUT publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, AIchatbot API, Application API, and 12 more. Tagged areas include Marketing Automation, Email Marketing, Social Media, Lead Management, and Landing Pages.


  VBOUT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, YouTube channel, and 25 more developer resources.'
random_paper: 74
rate_limits:
- limit_count: 0
  name: Vbout Rate Limits
  slug: vbout-rate-limits
score:
  band: developing
  composite: 46.7
  delta: -1.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 47.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Vbout Authentication
  slug: vbout-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vbout Domain Security
  slug: vbout-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vbout
tags:
- Marketing Automation
- Email Marketing
- Social Media
- Lead Management
- Landing Pages
- Chatbots
- Contacts
- Campaigns
- SaaS
website: https://vbout.com
---
