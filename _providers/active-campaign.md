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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Active Campaign Agentic Access
  operation_count: 31
  slug: active-campaign-agentic-access
  summary_line: 31 operations · 20 acting
api_count: 10
apis:
- description: REST API for managing contacts, deals, automations, campaigns, lists, tags, custom fields, and ecommerce data in ActiveCampaign. Each account uses its own base URL ({account}.api-us1.com/api/3) and au
  name: ActiveCampaign API v3
  slug: api-v3
- description: The Broadcasts API from ActiveCampaign — 1 operation(s) for broadcasts.
  name: ActiveCampaign Broadcasts API
  slug: active-campaign-broadcasts-api
- description: The Bulk API from ActiveCampaign — 3 operation(s) for bulk.
  name: ActiveCampaign Bulk API
  slug: active-campaign-bulk-api
- description: The Campaigns API from ActiveCampaign — 4 operation(s) for campaigns.
  name: ActiveCampaign Campaigns API
  slug: active-campaign-campaigns-api
- description: The Contacts API from ActiveCampaign — 4 operation(s) for contacts.
  name: ActiveCampaign Contacts API
  slug: active-campaign-contacts-api
- description: The Custom Fields API from ActiveCampaign — 3 operation(s) for custom fields.
  name: ActiveCampaign Custom Fields API
  slug: active-campaign-custom-fields-api
- description: The Deals API from ActiveCampaign — 2 operation(s) for deals.
  name: ActiveCampaign Deals API
  slug: active-campaign-deals-api
- description: The Lists API from ActiveCampaign — 1 operation(s) for lists.
  name: ActiveCampaign Lists API
  slug: active-campaign-lists-api
- description: The Segments API from ActiveCampaign — 2 operation(s) for segments.
  name: ActiveCampaign Segments API
  slug: active-campaign-segments-api
- description: The Variables API from ActiveCampaign — 2 operation(s) for variables.
  name: ActiveCampaign Variables API
  slug: active-campaign-variables-api
artifact_total: 15
collections:
- collection_type: open
  name: ActiveCampaign API
  slug: open-active-campaign
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/active-campaign-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/active-campaign-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/active-campaign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/active-campaign-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActiveCampaign
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/activecampaign
- group: company
  title: ''
  type: Website
  url: https://www.activecampaign.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.activecampaign.com
- group: operate
  title: ''
  type: Help Center
  url: https://help.activecampaign.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.activecampaign.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.activecampaign.com/signup/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.activecampaign.com/llms.txt
created: '2026-05-11'
description: ActiveCampaign is a customer experience automation platform that combines email marketing, marketing automation, CRM, sales engagement, and transactional messaging for small and mid-sized businesses. The ActiveCampaign API v3 is a REST/JSON API organized around resources such as contacts, deals, automations, campaigns, lists, and tags, with per-account base URLs of the form youraccountname.api-us1.com/api/3. Authentication is performed via an Api-Token HTTP header containing the account API key.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/active-campaign.png
layout: provider
modified: '2026-05-11'
name: ActiveCampaign
nav: Providers
network: true
overview: 'ActiveCampaign publishes 10 APIs on the [APIs.io](https://apis.io/) network, including API v3, Broadcasts API, Bulk API, and 7 more. Tagged areas include Marketing Automation, Email Marketing, CRM, Customer Experience Automation, and Sales Engagement.


  ActiveCampaign''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.0
  delta: 3.3
  facets:
    commercial_clarity: 18.4
    contract_quality: 43.4
    developer_ergonomics: 23.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/active-campaign/refs/heads/main/screenshots/active-campaign-2026-06-20T164200.png
security:
- kind: authentication
  name: Active Campaign Authentication
  slug: active-campaign-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Active Campaign Domain Security
  slug: active-campaign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Active Campaign Trust Center
  slug: active-campaign-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: active-campaign
tags:
- Marketing Automation
- Email Marketing
- CRM
- Customer Experience Automation
- Sales Engagement
website: https://www.activecampaign.com
---
