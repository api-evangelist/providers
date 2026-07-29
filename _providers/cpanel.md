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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cpanel Agentic Access
  operation_count: 5
  slug: cpanel-agentic-access
  summary_line: 5 operations
api_count: 7
apis:
- description: The cPanel User API (UAPI) is the modern HTTP API for performing cPanel-level operations such as managing email accounts, mailboxes, files, databases, FTP accounts, SSL certificates, and DNS zones for
  name: cPanel UAPI
  slug: uapi
- description: The WHM API 1 is the HTTP API for server-wide and reseller-level operations including creating, suspending, and terminating cPanel accounts, managing packages and feature lists, configuring DNS cluste
  name: WHM API 1
  slug: whm-api-1
- description: cPanel API 2 is the legacy XML/JSON API for cPanel-user operations. It remains supported for backward compatibility but has been largely superseded by UAPI; new development should target UAPI where po
  name: cPanel API 2 (Legacy)
  slug: cpanel-api-2
- description: Domain information (DomainInfo module)
  name: cPanel DomainInfo API
  slug: cpanel-domaininfo-api
- description: Email account management (Email module)
  name: cPanel Email API
  slug: cpanel-email-api
- description: MySQL database operations (Mysql module)
  name: cPanel Mysql API
  slug: cpanel-mysql-api
- description: Generic UAPI execute endpoint
  name: cPanel UAPI API
  slug: cpanel-uapi-api
artifact_total: 15
collections:
- collection_type: open
  name: cPanel UAPI
  slug: open-cpanel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cpanel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cpanel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cpanel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cpanel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cpanel.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.cpanel.net/
- group: auth
  title: ''
  type: Authentication
  url: https://api.docs.cpanel.net/guides/guide-to-api-authentication/
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.docs.cpanel.net/whm/release-notes/
- group: operate
  title: ''
  type: Forums
  url: https://forums.cpanel.net/
- group: operate
  title: ''
  type: Support
  url: https://support.cpanel.net/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cpanel.net/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CpanelInc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cpanel.net/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cpanel.net/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cpanel
- group: agent
  title: ''
  type: LlmsText
  url: https://api.docs.cpanel.net/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cpanel.net/blog/
created: '2025-02-09'
description: cPanel is a web-based control panel that provides a graphical interface and automation tools to simplify the management of web hosting services. cPanel exposes a family of HTTP APIs (UAPI, WHM API 1, and the legacy cPanel API 2) for automating account, domain, email, database, DNS, and server-wide operations. APIs accept API tokens or Basic Authentication and return JSON or XML responses.
finops:
- name: Cpanel Finops
  service_category: API
  slug: cpanel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cpanel.png
layout: provider
modified: '2026-04-28'
name: cPanel
nav: Providers
network: true
overview: 'cPanel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including DomainInfo API, Email API, Mysql API, and 1 more. Tagged areas include Control Panel, DNS, Domains, Email, and Hosting.


  cPanel''s developer surface includes authentication, documentation, changelog, support, GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: Cpanel Plans Pricing
  plan_count: 3
  slug: cpanel-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Cpanel Rate Limits
  slug: cpanel-rate-limits
score:
  band: developing
  composite: 46.2
  delta: -3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cpanel/refs/heads/main/screenshots/cpanel-2026-06-20T175154.png
security:
- kind: authentication
  name: Cpanel Authentication
  slug: cpanel-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Cpanel Domain Security
  slug: cpanel-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cpanel Vulnerability Disclosure
  slug: cpanel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cpanel
tags:
- Control Panel
- DNS
- Domains
- Email
- Hosting
- Reseller
- Server Administration
- Web Hosting
- WHM
website: https://cpanel.net/
---
