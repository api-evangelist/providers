---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Pylon Agentic Access
  operation_count: 68
  slug: pylon-agentic-access
  summary_line: 68 operations · 44 acting
api_count: 1
apis:
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Customer accounts.
  name: Pylon Accounts API
  slug: pylon-accounts-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Individual contacts (end customers).
  name: Pylon Contacts API
  slug: pylon-contacts-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Custom field definitions.
  name: Pylon Custom Fields API
  slug: pylon-custom-fields-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Support issues (tickets).
  name: Pylon Issues API
  slug: pylon-issues-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Knowledge bases, collections, and articles.
  name: Pylon Knowledge Base API
  slug: pylon-knowledge-base-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Tags used across issues, accounts, and contacts.
  name: Pylon Tags API
  slug: pylon-tags-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Tasks, projects, and milestones.
  name: Pylon Tasks API
  slug: pylon-tasks-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Support teams.
  name: Pylon Teams API
  slug: pylon-teams-api
- baseURL: https://api.usepylon.com
  baseurl_source: declared
  description: Internal Pylon users (agents).
  name: Pylon Users API
  slug: pylon-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pylon Accounts API
  slug: open-pylon-accounts-api
- collection_type: open
  name: Pylon Accounts Contacts API
  slug: open-pylon-contacts-api
- collection_type: open
  name: Pylon Accounts Custom Fields API
  slug: open-pylon-custom-fields-api
- collection_type: open
  name: Pylon Accounts Issues API
  slug: open-pylon-issues-api
- collection_type: open
  name: Pylon Accounts Knowledge Base API
  slug: open-pylon-knowledge-base-api
- collection_type: open
  name: Pylon Accounts Tags API
  slug: open-pylon-tags-api
- collection_type: open
  name: Pylon Accounts Tasks API
  slug: open-pylon-tasks-api
- collection_type: open
  name: Pylon Accounts Teams API
  slug: open-pylon-teams-api
- collection_type: open
  name: Pylon Accounts Users API
  slug: open-pylon-users-api
- collection_type: open
  name: Pylon API
  slug: open-pylon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pylon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pylon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pylon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pylon-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usepylon
- group: company
  title: ''
  type: Website
  url: https://usepylon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usepylon.com/pylon-docs/developer/api
- group: commercial
  title: ''
  type: Plans
  url: plans/pylon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pylon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pylon-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://usepylon.com/blog
created: '2026-06-20'
description: Pylon (usepylon.com) is a B2B customer support and customer operations platform that unifies shared Slack, Microsoft Teams, email, and chat support into a single ticketing system, with a knowledge base, accounts and contacts, AI agents, and a documented public REST API at https://api.usepylon.com.
finops:
- name: Pylon Finops
  service_category: Customer Support and Operations
  slug: pylon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pylon.png
layout: provider
modified: '2026-06-20'
name: Pylon
nav: Providers
network: true
overview: 'Pylon publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Custom Fields API, and 6 more. Tagged areas include Customer-Support, Customer Operations, Ticketing, Knowledge Base, and B2B.


  Pylon''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pylon Plans Pricing
  plan_count: 4
  slug: pylon-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Pylon Rate Limits
  slug: pylon-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/pylon/refs/heads/main/screenshots/pylon-2026-06-20T192331.png
security:
- kind: authentication
  name: Pylon Authentication
  slug: pylon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pylon Domain Security
  slug: pylon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pylon Trust Center
  slug: pylon-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: pylon
tags:
- Customer-Support
- Customer Operations
- Ticketing
- Knowledge Base
- B2B
- Help Desk
website: https://usepylon.com/
---
