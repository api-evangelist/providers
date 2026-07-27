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
- acting_count: 11
  human_in_the_loop: 0
  name: Pardot Agentic Access
  operation_count: 35
  slug: pardot-agentic-access
  summary_line: 35 operations · 11 acting
api_count: 3
apis:
- description: Version 5 REST API for managing prospects, accounts, campaigns, emails, forms, lists, and engagement programs in Marketing Cloud Account Engagement. Authentication uses Salesforce OAuth 2.0 with the p
  name: Account Engagement API v5
  slug: account-engagement-api-v5
- description: Legacy v3/v4 REST API endpoints for Pardot resources. Still supported for many objects not yet migrated to v5; uses the same Salesforce OAuth 2.0 authentication scheme.
  name: Account Engagement API v3/v4 (Legacy)
  slug: account-engagement-api-v4
- description: The Objects API from Salesforce Marketing Cloud Account Engagement (Pardot) — 24 operation(s) for objects.
  name: Salesforce Marketing Cloud Account Engagement (Pardot) Objects API
  slug: pardot-objects-api
artifact_total: 9
collections:
- collection_type: open
  name: Salesforce Account Engagement (Pardot) API v5
  slug: open-pardot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pardot-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pardot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pardot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pardot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pardot-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pardot
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/marketing/b2b-automation/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/marketing/pardot/guide/overview.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/marketing/b2b-automation/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.salesforce.com/form/signup/freetrial-b2bma/
created: '2026-05-11'
description: Salesforce Marketing Cloud Account Engagement, formerly known as Pardot, is a B2B marketing automation platform tightly integrated with Salesforce CRM for lead generation, lead nurturing, email marketing, and marketing ROI reporting. The platform provides campaigns, forms, landing pages, dynamic content, lead scoring/grading, and Engagement Studio for multi-step nurture programs. Version 5 of the Account Engagement REST API uses Salesforce OAuth 2.0 authentication and requires a Business Unit ID header, with hosts at pi.pardot.com (production) and pi.demo.pardot.com (sandbox).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pardot.png
layout: provider
modified: '2026-05-11'
name: Salesforce Marketing Cloud Account Engagement (Pardot)
nav: Providers
network: true
overview: 'Salesforce Marketing Cloud Account Engagement (Pardot) publishes 1 API on the [APIs.io](https://apis.io/) network: Objects API. Tagged areas include Marketing Automation, B2B Marketing, Lead Generation, Email Marketing, and Salesforce.


  Salesforce Marketing Cloud Account Engagement (Pardot)''s developer surface includes authentication, documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 38
scopes:
- name: Pardot Scopes
  scope_count: 1
  slug: pardot-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 28.7
  delta: 3.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 47.8
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pardot/refs/heads/main/screenshots/pardot-2026-06-20T191406.png
security:
- kind: authentication
  name: Pardot Authentication
  slug: pardot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pardot Domain Security
  slug: pardot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pardot Vulnerability Disclosure
  slug: pardot-vulnerability-disclosure
  summary_line: disclosure policy published
slug: pardot
tags:
- Marketing Automation
- B2B Marketing
- Lead Generation
- Email Marketing
- Salesforce
- Account Engagement
website: https://www.salesforce.com/marketing/b2b-automation/
---
