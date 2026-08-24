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
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Microsoft Yammer Agentic Access
  operation_count: 33
  slug: microsoft-yammer-agentic-access
  summary_line: 33 operations · 12 acting
api_count: 10
apis:
- description: 'The Yammer REST API (now Viva Engage) provides access to enterprise social networking features including messages, groups, users, and networks. Developers can post messages, manage group memberships, '
  name: Yammer REST API
  slug: rest-api
- description: The Files API from Microsoft Yammer — 1 operation(s) for files.
  name: Microsoft Yammer Files API
  slug: microsoft-yammer-files-api
- description: The Groups API from Microsoft Yammer — 2 operation(s) for groups.
  name: Microsoft Yammer Groups API
  slug: microsoft-yammer-groups-api
- description: The Messages API from Microsoft Yammer — 12 operation(s) for messages.
  name: Microsoft Yammer Messages API
  slug: microsoft-yammer-messages-api
- description: The Networks API from Microsoft Yammer — 1 operation(s) for networks.
  name: Microsoft Yammer Networks API
  slug: microsoft-yammer-networks-api
- description: The Search API from Microsoft Yammer — 1 operation(s) for search.
  name: Microsoft Yammer Search API
  slug: microsoft-yammer-search-api
- description: The Subscriptions API from Microsoft Yammer — 2 operation(s) for subscriptions.
  name: Microsoft Yammer Subscriptions API
  slug: microsoft-yammer-subscriptions-api
- description: The Threads API from Microsoft Yammer — 1 operation(s) for threads.
  name: Microsoft Yammer Threads API
  slug: microsoft-yammer-threads-api
- description: The Topics API from Microsoft Yammer — 1 operation(s) for topics.
  name: Microsoft Yammer Topics API
  slug: microsoft-yammer-topics-api
- description: The Users API from Microsoft Yammer — 5 operation(s) for users.
  name: Microsoft Yammer Users API
  slug: microsoft-yammer-users-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files API
  slug: open-microsoft-yammer-files-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Groups API
  slug: open-microsoft-yammer-groups-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Messages API
  slug: open-microsoft-yammer-messages-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Networks API
  slug: open-microsoft-yammer-networks-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Search API
  slug: open-microsoft-yammer-search-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Subscriptions API
  slug: open-microsoft-yammer-subscriptions-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Threads API
  slug: open-microsoft-yammer-threads-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Topics API
  slug: open-microsoft-yammer-topics-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST Files Users API
  slug: open-microsoft-yammer-users-api
- collection_type: open
  name: Viva Engage (Yammer) Legacy REST API
  slug: open-microsoft-yammer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-yammer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-yammer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-yammer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-yammer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yammer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yammer-inc
- group: start
  title: ''
  type: Portal
  url: https://engage.cloud.microsoft/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/rest/api/yammer/oauth-2
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: APIs for Yammer (now Viva Engage) enterprise social networking platform providing access to messages, groups, users, and networks.
finops:
- name: Microsoft Yammer Finops
  service_category: API
  slug: microsoft-yammer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-yammer.png
layout: provider
modified: '2026-04-28'
name: Microsoft Yammer
nav: Providers
network: true
overview: 'Microsoft Yammer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Files API, Groups API, Messages API, and 6 more. Tagged areas include Enterprise Social, Microsoft, Social Networking, Viva Engage, and Yammer.


  Microsoft Yammer''s developer surface includes authentication, developer portal, support, and 8 more developer resources.'
plans:
- name: Microsoft Yammer Plans Pricing
  plan_count: 3
  slug: microsoft-yammer-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Microsoft Yammer Rate Limits
  slug: microsoft-yammer-rate-limits
scopes:
- name: Microsoft Yammer Scopes
  scope_count: 2
  slug: microsoft-yammer-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.1
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-yammer/refs/heads/main/screenshots/microsoft-yammer-2026-06-20T185547.png
security:
- kind: authentication
  name: Microsoft Yammer Authentication
  slug: microsoft-yammer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Yammer Domain Security
  slug: microsoft-yammer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: microsoft-yammer
tags:
- Enterprise Social
- Microsoft
- Social Networking
- Viva Engage
- Yammer
website: https://engage.cloud.microsoft/
---
