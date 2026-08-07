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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Getresponse Agentic Access
  operation_count: 20
  slug: getresponse-agentic-access
  summary_line: 20 operations · 8 acting
api_count: 9
apis:
- description: JSON REST API for managing contacts, campaigns, newsletters, autoresponders, landing pages, webinars, custom fields, tags, segments, and workflows in the GetResponse platform. Authentication uses an X
  name: GetResponse API v3
  slug: rest-api
- description: The Accounts API from GetResponse — 1 operation(s) for accounts.
  name: GetResponse Accounts API
  slug: getresponse-accounts-api
- description: The Autoresponders API from GetResponse — 2 operation(s) for autoresponders.
  name: GetResponse Autoresponders API
  slug: getresponse-autoresponders-api
- description: The Campaigns API from GetResponse — 2 operation(s) for campaigns.
  name: GetResponse Campaigns API
  slug: getresponse-campaigns-api
- description: The Contacts API from GetResponse — 2 operation(s) for contacts.
  name: GetResponse Contacts API
  slug: getresponse-contacts-api
- description: The Custom Fields API from GetResponse — 1 operation(s) for custom fields.
  name: GetResponse Custom Fields API
  slug: getresponse-custom-fields-api
- description: The Newsletters API from GetResponse — 2 operation(s) for newsletters.
  name: GetResponse Newsletters API
  slug: getresponse-newsletters-api
- description: The Tags API from GetResponse — 1 operation(s) for tags.
  name: GetResponse Tags API
  slug: getresponse-tags-api
- description: The Webhooks API from GetResponse — 1 operation(s) for webhooks.
  name: GetResponse Webhooks API
  slug: getresponse-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: GetResponse API v3
  slug: open-getresponse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/getresponse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/getresponse-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getresponse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/getresponse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getresponse
- group: company
  title: ''
  type: Website
  url: https://www.getresponse.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.getresponse.com/v3
- group: docs
  title: ''
  type: APIReference
  url: https://apireference.getresponse.com/
- group: start
  title: ''
  type: Signup
  url: https://app.getresponse.com/create_account
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getresponse.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.getresponse.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.getresponse.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.getresponse.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetResponse
created: '2026-05-11'
description: GetResponse is an online marketing platform offering email marketing, marketing automation, landing pages, webinars, and conversion funnels for small businesses, marketers, and enterprises. The platform provides tools to grow email lists, automate campaigns, segment audiences, and engage customers across multiple channels. The GetResponse API v3 is a JSON REST API that uses X-Auth-Token header authentication to manage contacts, campaigns, newsletters, autoresponders, landing pages, webinars, and more.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getresponse.png
layout: provider
modified: '2026-05-11'
name: GetResponse
nav: Providers
network: true
overview: 'GetResponse publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Autoresponders API, Campaigns API, and 5 more. Tagged areas include Email Marketing, Marketing Automation, Landing Pages, Webinars, and Conversion Funnels.


  GetResponse''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, engineering blog, and 7 more developer resources.'
random_paper: 69
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 57.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/screenshots/getresponse-2026-06-20T181811.png
security:
- kind: authentication
  name: Getresponse Authentication
  slug: getresponse-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Getresponse Domain Security
  slug: getresponse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getresponse Trust Center
  slug: getresponse-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: getresponse
tags:
- Email Marketing
- Marketing Automation
- Landing Pages
- Webinars
- Conversion Funnels
- CRM
website: https://www.getresponse.com
---
