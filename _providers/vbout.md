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
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Vbout Agentic Access
  operation_count: 37
  slug: vbout-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 2
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
artifact_total: 38
asyncapis:
- description: ''
  name: Vbout Webhooks
  slug: vbout-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VBOUT EmailMarketing Account API
  slug: open-vbout-account-api
- collection_type: open
  name: VBOUT EmailMarketing AIchatbot API
  slug: open-vbout-aichatbot-api
- collection_type: open
  name: VBOUT EmailMarketing Application API
  slug: open-vbout-application-api
- collection_type: open
  name: VBOUT EmailMarketing Automation API
  slug: open-vbout-automation-api
- collection_type: open
  name: VBOUT EmailMarketing Contact API
  slug: open-vbout-contact-api
- collection_type: open
  name: VBOUT EmailMarketing Email Marketing API
  slug: open-vbout-email-marketing-api
- collection_type: open
  name: VBOUT EmailMarketing API
  slug: open-vbout-emailmarketing-api
- collection_type: open
  name: VBOUT EmailMarketing Goals API
  slug: open-vbout-goals-api
- collection_type: open
  name: VBOUT EmailMarketing Help API
  slug: open-vbout-help-api
- collection_type: open
  name: VBOUT EmailMarketing Pipeline API
  slug: open-vbout-pipeline-api
- collection_type: open
  name: VBOUT EmailMarketing Popups API
  slug: open-vbout-popups-api
- collection_type: open
  name: VBOUT EmailMarketing Settings API
  slug: open-vbout-settings-api
- collection_type: open
  name: VBOUT EmailMarketing Social Media API
  slug: open-vbout-social-media-api
- collection_type: open
  name: VBOUT EmailMarketing SocialMedia API
  slug: open-vbout-socialmedia-api
- collection_type: open
  name: VBOUT EmailMarketing Users & Workflow API
  slug: open-vbout-users-workflow-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vbout-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vbout-openapi-overlay.yaml
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
- group: commercial
  title: ''
  type: Plans
  url: plans/vbout-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vbout-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/vbout-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vbout-sandbox.yml
created: '2026-07-17'
description: VBOUT is an AI-enabled marketing automation platform used by agencies and small-to-mid-size businesses to run email marketing, social media scheduling, landing pages, popups, lead scoring, and an AI chatbot from one place. The VBOUT REST API (v1.0 at api.vbout.com/1) exposes the platform programmatically — contacts, lists, audiences, email campaigns and stats, social channels, calendar and posts, conversion goals, sub-users and groups, on-site engagement actions, automations, pipeline boards, and account settings — authenticated with an account API key, with responses in JSON or XML and a documented 15 requests/second rate limit. VBOUT is a 500 Global portfolio company.
image: https://developers.vbout.com/images/front/icons/logo-square-114x114.png
layout: provider
mcp_servers:
- description: Candidate MCP server tool surface for the VBOUT API, derived one tool per operation from the provider-published OpenAPI 3.1.0 document (71 operations across Application, Social Media, Email Marketing,
  name: VBOUT MCP Server
  slug: vbout-mcp-server
modified: '2026-08-13'
name: VBOUT
nav: Providers
network: true
overview: 'VBOUT publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, AIchatbot API, Application API, and 12 more. Tagged areas include Marketing Automation, Email Marketing, Social-Media, Lead Management, and Landing Pages.


  The VBOUT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VBOUT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, YouTube channel, and 31 more developer resources.'
plans:
- name: Vbout Plans Pricing
  plan_count: 4
  slug: vbout-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Vbout Rate Limits
  slug: vbout-rate-limits
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 47.4
  previous_composite: 56.2
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vbout/refs/heads/main/screenshots/vbout-2026-08-17T082712.png
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
- Social-Media
- Lead Management
- Landing Pages
- Chatbots
- Contacts
- Campaigns
- Software-as-a-Service
website: https://vbout.com
---
