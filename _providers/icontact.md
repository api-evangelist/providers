---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API v2.2 for managing contacts, lists, segments, campaigns, messages, sends, and reporting inside the iContact email marketing platform. Authentication uses custom HTTP headers including API-AppI
  name: iContact REST API
  slug: rest-api
artifact_total: 8
asyncapis:
- description: 'Derived AsyncAPI description of the four contact-lifecycle webhook events iContact documents at https://help.icontact.com/customers/s/article/Web-Hooks-iContact-API. NOT A PROVIDER ARTIFACT. iContact '
  name: iContact Webhooks
  slug: icontact-webhooks-asyncapi
- description: ''
  name: Icontact Webhooks
  slug: icontact-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/icontact-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/icontact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icontact
- group: company
  title: ''
  type: Website
  url: https://www.icontact.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.icontact.com/customers/s/article/API-Developer-Portal
- group: docs
  title: ''
  type: Documentation
  url: https://help.icontact.com/customers/s/article/Documentation-iContact-API
- group: docs
  title: ''
  type: APIReference
  url: https://help.icontact.com/customers/s/article/Resource-Call-References-List-iContact-API
- group: start
  title: ''
  type: GettingStarted
  url: https://help.icontact.com/customers/s/article/API-Getting-Started-Guide
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.icontact.com/customers/s/
- group: operate
  title: ''
  type: Support
  url: https://www.icontact.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.icontact.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/icontact-plans-pricing.yml
- group: start
  title: ''
  type: Signup
  url: https://www.icontact.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.icontact.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.icontact.com/legal/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.icontact.com/legal/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.icontact.com/
- group: build
  title: ''
  type: Packages
  url: packages/icontact-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/icontact-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/icontact-llms.txt
- group: other
  title: ''
  type: Parent Company
  url: https://www.cision.com
- group: company
  title: ''
  type: Blog
  url: https://www.icontact.com/feed
- group: company
  title: ''
  type: BlogRSS
  url: https://www.icontact.com/resources/blog/feed/
created: '2026-05-11'
description: iContact is an email marketing and marketing automation platform (now part of Cision) that helps small and mid-market businesses build email campaigns, manage contacts and lists, automate drip sequences, and measure engagement. The iContact REST API v2.2 provides programmatic access to contacts, lists, segments, campaigns, messages, and reporting data using a combination of HTTP headers (API-AppId, API-Version, API-Username, API-Password) for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icontact.png
layout: provider
mcp_servers:
- description: ''
  name: iContact MCP server
  slug: icontact-mcp-server
modified: '2026-08-13'
name: iContact
nav: Providers
network: true
overview: 'iContact publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Email Marketing, Marketing Automation, Campaigns, Contacts, and List.


  The iContact catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  iContact''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Icontact Plans Pricing
  plan_count: 4
  slug: icontact-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Icontact Rate Limits
  slug: icontact-rate-limits
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 44.4
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 48.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icontact/refs/heads/main/screenshots/icontact-2026-06-20T183200.png
security:
- kind: authentication
  name: Icontact Authentication
  slug: icontact-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Icontact Domain Security
  slug: icontact-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: icontact
tags:
- Email Marketing
- Marketing Automation
- Campaigns
- Contacts
- List
- Segments
- Webhook
- Email Deliverability
- SMB
website: https://www.icontact.com
---
