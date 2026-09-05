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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Gorgias Agentic Access
  operation_count: 49
  slug: gorgias-agentic-access
  summary_line: 49 operations · 26 acting
api_count: 1
apis:
- description: Outbound webhook surface delivered through Gorgias HTTP Integrations. When configured triggers fire on a Gorgias account, Gorgias sends an HTTP request to the URL set on the TicketHttpIntegration, wit
  name: Gorgias Webhooks
  slug: webhooks
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Account API from Gorgias — 2 operation(s) for account.
  name: Gorgias Account API
  slug: gorgias-account-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Customers API from Gorgias — 2 operation(s) for customers.
  name: Gorgias Customers API
  slug: gorgias-customers-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Integrations API from Gorgias — 2 operation(s) for integrations.
  name: Gorgias Integrations API
  slug: gorgias-integrations-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Macros API from Gorgias — 2 operation(s) for macros.
  name: Gorgias Macros API
  slug: gorgias-macros-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Messages API from Gorgias — 1 operation(s) for messages.
  name: Gorgias Messages API
  slug: gorgias-messages-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Rules API from Gorgias — 2 operation(s) for rules.
  name: Gorgias Rules API
  slug: gorgias-rules-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Surveys API from Gorgias — 1 operation(s) for surveys.
  name: Gorgias Surveys API
  slug: gorgias-surveys-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Tags API from Gorgias — 3 operation(s) for tags.
  name: Gorgias Tags API
  slug: gorgias-tags-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Teams API from Gorgias — 1 operation(s) for teams.
  name: Gorgias Teams API
  slug: gorgias-teams-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Tickets API from Gorgias — 2 operation(s) for tickets.
  name: Gorgias Tickets API
  slug: gorgias-tickets-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Users API from Gorgias — 2 operation(s) for users.
  name: Gorgias Users API
  slug: gorgias-users-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Views API from Gorgias — 2 operation(s) for views.
  name: Gorgias Views API
  slug: gorgias-views-api
- baseURL: https://{subdomain}.gorgias.com/api
  baseurl_source: declared
  description: The Widgets API from Gorgias — 2 operation(s) for widgets.
  name: Gorgias Widgets API
  slug: gorgias-widgets-api
artifact_total: 36
asyncapis:
- description: Best-effort AsyncAPI 2.6 description of the Gorgias webhook surface, delivered through Gorgias HTTP Integrations. When the configured triggers fire inside a Gorgias account, Gorgias performs an HTTP r
  name: Gorgias Webhooks (HTTP Integrations)
  slug: gorgias-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gorgias REST Account API
  slug: open-gorgias-account-api
- collection_type: open
  name: Gorgias REST Account Customers API
  slug: open-gorgias-customers-api
- collection_type: open
  name: Gorgias REST Account Integrations API
  slug: open-gorgias-integrations-api
- collection_type: open
  name: Gorgias REST Account Macros API
  slug: open-gorgias-macros-api
- collection_type: open
  name: Gorgias REST Account Messages API
  slug: open-gorgias-messages-api
- collection_type: open
  name: Gorgias REST Account Rules API
  slug: open-gorgias-rules-api
- collection_type: open
  name: Gorgias REST Account Surveys API
  slug: open-gorgias-surveys-api
- collection_type: open
  name: Gorgias REST Account Tags API
  slug: open-gorgias-tags-api
- collection_type: open
  name: Gorgias REST Account Teams API
  slug: open-gorgias-teams-api
- collection_type: open
  name: Gorgias REST Account Tickets API
  slug: open-gorgias-tickets-api
- collection_type: open
  name: Gorgias REST Account Users API
  slug: open-gorgias-users-api
- collection_type: open
  name: Gorgias REST Account Views API
  slug: open-gorgias-views-api
- collection_type: open
  name: Gorgias REST Account Widgets API
  slug: open-gorgias-widgets-api
- collection_type: open
  name: Gorgias REST API
  slug: open-gorgias
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gorgias-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gorgias-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gorgias-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gorgias-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gorgias-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gorgias.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gorgias
- group: company
  title: ''
  type: Website
  url: https://www.gorgias.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gorgias.com
- group: operate
  title: ''
  type: Help Center
  url: https://docs.gorgias.com/en-US
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gorgias.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.gorgias.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gorgias.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.gorgias.com/changelog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gorgiasio
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.gorgias.com/llms.txt
created: '2026-05-11'
description: Gorgias is a customer support and helpdesk platform purpose-built for ecommerce brands, with deep native integrations into Shopify, BigCommerce, Magento, and other commerce stacks to unify email, chat, social, SMS, and voice conversations alongside order data. The platform automates repetitive support tasks with AI agents and macros, surfaces revenue attribution for support interactions, and powers self-service flows on storefronts. The Gorgias REST API provides full CRUD access to tickets, customers, macros, integrations, and widgets using HTTP Basic authentication or OAuth2 for public apps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gorgias.png
layout: provider
modified: '2026-05-30'
name: Gorgias
nav: Providers
network: true
overview: 'Gorgias publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Account API, Customers API, and 11 more. Tagged areas include Customer-Support, Help Desk, E-Commerce, Shopify, and Tickets.


  The Gorgias catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gorgias'' developer surface includes authentication, engineering blog, documentation, pricing, signup flow, changelog, and 10 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Gorgias API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: gorgias-asyncapi-spectral-rules
scopes:
- name: Gorgias Scopes
  scope_count: 6
  slug: gorgias-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 11.4
    contract_quality: 57.1
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gorgias/refs/heads/main/screenshots/gorgias-2026-06-20T182307.png
security:
- kind: authentication
  name: Gorgias Authentication
  slug: gorgias-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gorgias Domain Security
  slug: gorgias-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gorgias Vulnerability Disclosure
  slug: gorgias-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gorgias
tags:
- Customer-Support
- Help Desk
- E-Commerce
- Shopify
- Tickets
- Conversations
website: https://www.gorgias.com
---
