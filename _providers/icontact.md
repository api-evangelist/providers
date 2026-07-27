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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST API v2.2 for managing contacts, lists, segments, campaigns, messages, sends, and reporting inside the iContact email marketing platform. Authentication uses custom HTTP headers including API-AppI
  name: iContact REST API
  slug: rest-api
artifact_total: 2
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
- group: docs
  title: ''
  type: Documentation
  url: https://www.icontact.com/developerportal/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.icontact.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.icontact.com/icp/signup
- group: other
  title: ''
  type: Parent Company
  url: https://www.cision.com
- group: company
  title: ''
  type: Blog
  url: https://www.icontact.com/feed
created: '2026-05-11'
description: iContact is an email marketing and marketing automation platform (now part of Cision) that helps small and mid-market businesses build email campaigns, manage contacts and lists, automate drip sequences, and measure engagement. The iContact REST API v2.2 provides programmatic access to contacts, lists, segments, campaigns, messages, and reporting data using a combination of HTTP headers (API-AppId, API-Version, API-Username, API-Password) for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/icontact.png
layout: provider
modified: '2026-05-11'
name: iContact
nav: Providers
network: true
overview: 'iContact publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Marketing Automation, Campaigns, Contacts, and Lists.


  iContact''s developer surface includes documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 37
score:
  band: minimal
  composite: 14.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/icontact/refs/heads/main/screenshots/icontact-2026-06-20T183200.png
security:
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
- Lists
- SMB
website: https://www.icontact.com
---
