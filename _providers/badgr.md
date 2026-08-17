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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 3
  name: Badgr Agentic Access
  operation_count: 48
  slug: badgr-agentic-access
  summary_line: 48 operations · 26 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: The Assertions API from Badgr — 6 operation(s) for assertions.
  name: Badgr Assertions API
  slug: badgr-assertions-api
- description: The Authentication API from Badgr — 5 operation(s) for authentication.
  name: Badgr Authentication API
  slug: badgr-authentication-api
- description: The Backpack API from Badgr — 5 operation(s) for backpack.
  name: Badgr Backpack API
  slug: badgr-backpack-api
- description: The BadgeClasses API from Badgr — 4 operation(s) for badgeclasses.
  name: Badgr BadgeClasses API
  slug: badgr-badgeclasses-api
- description: The Collections API from Badgr — 3 operation(s) for collections.
  name: Badgr Collections API
  slug: badgr-collections-api
- description: The Issuers API from Badgr — 3 operation(s) for issuers.
  name: Badgr Issuers API
  slug: badgr-issuers-api
- description: The Users API from Badgr — 3 operation(s) for users.
  name: Badgr Users API
  slug: badgr-users-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Badgr Assertions API
  slug: open-badgr-assertions-api
- collection_type: open
  name: Badgr Assertions Authentication API
  slug: open-badgr-authentication-api
- collection_type: open
  name: Badgr Assertions Backpack API
  slug: open-badgr-backpack-api
- collection_type: open
  name: Badgr Assertions BadgeClasses API
  slug: open-badgr-badgeclasses-api
- collection_type: open
  name: Badgr Assertions Collections API
  slug: open-badgr-collections-api
- collection_type: open
  name: Badgr Assertions Issuers API
  slug: open-badgr-issuers-api
- collection_type: open
  name: Badgr Assertions Users API
  slug: open-badgr-users-api
- collection_type: open
  name: Badgr API
  slug: open-badgr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/badgr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/badgr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/badgr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/badgr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/concentricsky
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/instructure
- group: company
  title: ''
  type: Website
  url: https://badgr.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.badgr.io/docs/v2/
- group: commercial
  title: ''
  type: Plans
  url: plans/badgr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/badgr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/badgr-finops.yml
created: '2026-07-05'
description: Badgr is an open digital badging and micro-credentialing platform built on the Open Badges standard. Originally created by Concentric Sky, Badgr is now operated by Instructure as Canvas Credentials (and folded into Parchment Digital Badges). It lets organizations issue verifiable, portable achievement badges and learners collect them in a shareable Backpack. The platform is backed by the open-source badgr-server (github.com/concentricsky/badgr-server), which implements Open Badges 2.0/2.1 (Badge Connect). The documented REST API (base https://api.badgr.io/v2, with regional deployments in the EU, Canada, and Australia) uses OAuth2 bearer tokens and exposes Issuers, BadgeClasses, Assertions (awarded badges), the learner Backpack, Collections, and Users.
finops:
- name: Badgr Finops
  service_category: Education and Credentialing
  slug: badgr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/badgr.png
layout: provider
modified: '2026-07-05'
name: Badgr
nav: Providers
network: true
overview: 'Badgr publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assertions API, Authentication API, Backpack API, and 4 more. Tagged areas include Digital Badges, Open Badges, Micro-Credentials, Credentialing, and Verifiable Credentials.


  Badgr''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Badgr Plans Pricing
  plan_count: 4
  slug: badgr-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 4
  name: Badgr Rate Limits
  slug: badgr-rate-limits
scopes:
- name: Badgr Scopes
  scope_count: 3
  slug: badgr-scopes
  summary_line: 3 scopes · password/authorizationCode
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/badgr/refs/heads/main/screenshots/badgr-2026-07-25T202239.png
security:
- kind: authentication
  name: Badgr Authentication
  slug: badgr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Badgr Domain Security
  slug: badgr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: badgr
tags:
- Digital Badges
- Open Badges
- Micro-Credentials
- Credentialing
- Verifiable Credentials
- Education
- Open Source
website: https://badgr.com
---
