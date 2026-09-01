---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Zoho Mail Agentic Access
  operation_count: 23
  slug: zoho-mail-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 1
apis:
- description: Manage email accounts, vacation replies, forwarding, and account settings
  name: Zoho Mail Accounts API
  slug: zoho-mail-accounts-api
- description: Create and manage email folders
  name: Zoho Mail Folders API
  slug: zoho-mail-folders-api
- description: Send, receive, search, and manage email messages and attachments
  name: Zoho Mail Messages API
  slug: zoho-mail-messages-api
- description: Admin-level organization, domain, group, user, and policy management
  name: Zoho Mail Organization API
  slug: zoho-mail-organization-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Mail Accounts API
  slug: open-zoho-mail-accounts-api
- collection_type: open
  name: Zoho Mail Accounts Folders API
  slug: open-zoho-mail-folders-api
- collection_type: open
  name: Zoho Mail Accounts Messages API
  slug: open-zoho-mail-messages-api
- collection_type: open
  name: Zoho Mail Accounts Organization API
  slug: open-zoho-mail-organization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-mail-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-mail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-mail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-mail-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-mail-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/mail/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/mail/help/api/overview.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/zoho-mail
- group: company
  title: ''
  type: Blog
  url: https://blog.zoho.com/mail
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/mail/zohomail-pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com
- group: other
  title: ''
  type: X
  url: https://x.com/zohomail
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-mail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-mail-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-mail-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zoho-mail.json
created: '2026-06-13'
description: Zoho Mail is an ad-free, privacy-first email and collaboration platform offering a comprehensive REST API for managing email accounts, folders, messages, contacts, calendars, and organizational email administration. The API supports 15 modules including Organization, Domains, Groups, Users, Mail Policy, Accounts, Folders, Labels, Email Messages, Signatures, Threads, Tasks, Bookmarks, Notes, and Logs. Authentication uses OAuth 2.0 and responses are returned in JSON format with region-specific base URLs for US, Europe, India, Australia, Japan, Canada, UAE, Saudi Arabia, and China deployments.
finops:
- name: Zoho Mail Finops
  service_category: ''
  slug: zoho-mail-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Zoho Mail API. Zoho Mail provides a comprehensive REST API for managing email accounts, folders, messages, contacts, calendars, tasks, and
  name: Zoho Mail GraphQL Schema
  slug: zoho-mail-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-mail.png
layout: provider
modified: '2026-06-13'
name: Zoho Mail
nav: Providers
network: true
overview: 'Zoho Mail publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Folders API, Messages API, and 1 more. Tagged areas include Email, Mail, Collaboration, Messaging, and Calendar.


  Zoho Mail''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Zoho Mail Plans Pricing
  plan_count: 6
  slug: zoho-mail-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Zoho Mail Rate Limits
  slug: zoho-mail-rate-limits
scopes:
- name: Zoho Mail Scopes
  scope_count: 11
  slug: zoho-mail-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 58.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-mail/refs/heads/main/screenshots/zoho-mail-2026-06-20T201942.png
security:
- kind: authentication
  name: Zoho Mail Authentication
  slug: zoho-mail-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Mail Domain Security
  slug: zoho-mail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Mail Vulnerability Disclosure
  slug: zoho-mail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-mail
tags:
- Email
- Mail
- Collaboration
- Messaging
- Calendar
- Contacts
- Organization Management
- Software-as-a-Service
website: https://www.zoho.com/mail/
---
