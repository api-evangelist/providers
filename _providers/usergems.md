---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 64.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Usergems Agentic Access
  operation_count: 5
  slug: usergems-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 4
apis:
- description: Add and remove accounts UserGems should source prospects against.
  name: UserGems Accounts API
  slug: usergems-accounts-api
- description: Add and remove contacts UserGems should track for job changes.
  name: UserGems Contacts API
  slug: usergems-contacts-api
- description: Honor data-subject deletion requests for tracked contacts.
  name: UserGems Privacy API
  slug: usergems-privacy-api
- description: Hosted remote MCP server that lets an agent in Claude, ChatGPT or any MCP-compatible client work against the customer's own UserGems workspace — searching accounts and prospects, pulling signal and sc
  name: UserGems MCP
  slug: usergems-mcp
artifact_total: 57
asyncapis:
- description: ''
  name: Usergems Webhooks
  slug: usergems-webhooks
collections:
- collection_type: postman
  name: UserGems Accounts API
  slug: postman-usergems-accounts-api
- collection_type: postman
  name: UserGems Accounts Contacts API
  slug: postman-usergems-contacts-api
- collection_type: postman
  name: UserGems Accounts Privacy API
  slug: postman-usergems-privacy-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UserGems Accounts API
  slug: open-usergems-accounts-api
- collection_type: open
  name: UserGems API
  slug: open-usergems-api
- collection_type: open
  name: UserGems Accounts Contacts API
  slug: open-usergems-contacts-api
- collection_type: open
  name: UserGems Accounts Privacy API
  slug: open-usergems-privacy-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/usergems/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usergems-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/usergems-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/usergems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usergems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/usergems-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/usergems-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/usergems-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/usergems-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/usergems-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/usergems-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/usergems-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/usergems-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/usergems-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/usergems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/usergems-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/usergems-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.usergems.com/data-security
- group: auth
  title: ''
  type: Security
  url: https://www.usergems.com/legal-security/security
- group: design
  title: ''
  type: DataModel
  url: data-model/usergems-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/usergems-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.usergems.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.usergems.com/api/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app.usergems.com/api/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.usergems.com/article/using-the-usergems-api
- group: start
  title: ''
  type: Portal
  url: https://www.usergems.com/product/overview
- group: docs
  title: ''
  type: Documentation
  url: https://app.usergems.com/api/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/using-the-usergems-api
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-implementation-guide-salesforce-crm
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-implementation-guide-hubspot-crm
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/how-many-salesforce-api-calls-does-usergems-use
- group: docs
  title: ''
  type: Documentation
  url: https://help.usergems.com/article/usergems-outreach-configuration
- group: other
  title: ''
  type: Product
  url: https://www.usergems.com/product/api
- group: start
  title: ''
  type: SignUp
  url: https://www.usergems.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.usergems.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usergems.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.usergems.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.usergems.com/customers
- group: company
  title: ''
  type: Careers
  url: https://www.usergems.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.usergems.com/contact
- group: operate
  title: ''
  type: Support
  url: mailto:support@usergems.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usergems.com/legal-security/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usergems.com/legal-security/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.usergems.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usergems
- group: company
  title: ''
  type: Twitter
  url: https://x.com/usergems
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@UserGems
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usergems
- group: commercial
  title: ''
  type: Plans
  url: plans/usergems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usergems-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usergems-finops.yml
created: '2026-05-25'
description: UserGems is a San Francisco-based sales intelligence platform that tracks champion job changes and surfaces buying signals so sales and marketing teams can prioritize outbound and ABM motions. The platform packages 30+ native signals (job changes, contact-level intent, M&A, hiring, web visits), Gem-E AI agents for prospect list building and email personalization, and custom AI scoring trained on 600+ closed-won patterns. UserGems exposes a public REST API at api.usergems.com/v1 that lets customers programmatically add and remove contacts to track for job changes, add and remove target accounts, and honor data-subject deletion requests. That API is deliberately write-only — there are no read or GET endpoints — authenticates with a single company-wide X-Api-Key header, is capped at 20 requests per second with one record per request, and acknowledges enqueueing rather than completion. UserGems also ships a hosted remote MCP server at app.usergems.com/mcp/usergems, in gated early
  access as of August 2026, that lets agents in Claude or ChatGPT search accounts and prospects, pull signal and score history, run research, draft Gem-E messages, and build and run campaigns including CRM writes, sequence enrollment and ad-audience sync — authorized with OAuth 2.0, dynamic client registration, PKCE S256 and a single mcp:use scope. Native integrations include Salesforce, HubSpot, Microsoft Dynamics, Outreach, Salesloft, Gong Engage, Marketo, LinkedIn Ads, Meta Ads, and Google Ads.
examples:
- key_count: 6
  name: Usergems Add Account Example
  slug: usergems-add-account-example
- key_count: 8
  name: Usergems Add Contact Example
  slug: usergems-add-contact-example
- key_count: 1
  name: Usergems Privacy Delete Example
  slug: usergems-privacy-delete-example
features:
- Gem-E AI agents for prospect list building and email personalization
- 30+ native signals (job changes, contact-level intent, hiring, M&A, web visits)
- Custom AI scoring trained on 600+ closed-won patterns
- Intelligent workflows orchestrating ads, outreach, and CRM updates
- Contact-level intent (specific buyers, not just account-level)
- Outbound REST API for contact and account submission with up to 100 custom signal fields per contact
- Privacy delete endpoint for GDPR/CCPA right-to-erasure
- X-Api-Key header authentication
- Asynchronous queue-based processing
- Customer-configurable Salesforce API cap (default 20K calls per 24h per instance)
- Native integrations with Salesforce, HubSpot, Dynamics, Outreach, Salesloft, Gong, Marketo, LinkedIn/Meta/Google Ads
- Chrome extension for in-workflow access
- SOC 2 Type 2, GDPR, and CCPA compliance posture
- Money-back ROI guarantee — $100K spend tied to $100K pipeline
finops:
- name: Usergems Finops
  service_category: Sales Intelligence and ABM
  slug: usergems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usergems.png
integrations:
- category: CRM
  name: Salesforce
- category: CRM
  name: HubSpot
- category: CRM
  name: Microsoft Dynamics
- category: Sales Engagement
  name: Outreach
- category: Sales Engagement
  name: Salesloft
- category: Sales Engagement
  name: Gong Engage
- category: Marketing Automation
  name: HubSpot Marketing
- category: Marketing Automation
  name: Marketo
- category: Advertising
  name: LinkedIn Ads
- category: Advertising
  name: Meta Ads
- category: Advertising
  name: Google Ads
- category: Productivity
  name: Chrome Extension
json_schemas:
- name: UserGems Account
  property_count: 7
  slug: usergems-account
- name: UserGems Contact
  property_count: 9
  slug: usergems-contact
jsonld:
- class_count: 0
  name: Usergems Context
  property_count: 3
  slug: usergems-context
layout: provider
mcp_servers:
- description: ''
  name: usergems-mcp.yml
  slug: usergems-mcpyml
modified: '2026-08-13'
name: UserGems
nav: Providers
network: true
overview: 'UserGems publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Contacts API, and Privacy API. Tagged areas include Sales Intelligence, Outbound, ABM, Champion Tracking, and Job Changes.


  The UserGems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  UserGems'' developer surface includes authentication, API reference, getting-started guide, developer portal, documentation, signup flow, pricing, and 46 more developer resources.'
plans:
- name: Usergems Plans Pricing
  plan_count: 1
  slug: usergems-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 5
  name: Usergems Rate Limits
  slug: usergems-rate-limits
rules:
- name: UserGems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: usergems-jsonschema-spectral-rules
- name: UserGems API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: usergems-rules
scopes:
- name: Usergems Scopes
  scope_count: 1
  slug: usergems-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 79.6
  delta: 18.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 85.8
    developer_ergonomics: 71.7
    discoverability: 92.6
    governance: 79.2
    operational_transparency: 55.3
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/usergems/refs/heads/main/screenshots/usergems-2026-06-20T200715.png
security:
- kind: authentication
  name: Usergems Authentication
  slug: usergems-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Usergems Domain Security
  slug: usergems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usergems Vulnerability Disclosure
  slug: usergems-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Usergems Trust Center
  slug: usergems-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA, EU AI Act (limited risk)
slug: usergems
tags:
- Sales Intelligence
- Outbound
- ABM
- Champion Tracking
- Job Changes
- Buying Signals
- AI Scoring
- Sales Engagement
- CRM
- Revenue Operations
- GTM
- MCP
- AI Agents
website: https://www.usergems.com
---
