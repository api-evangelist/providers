---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 2
  human_in_the_loop: 0
  name: Lumen Technologies Agentic Access
  operation_count: 4
  slug: lumen-technologies-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: The Lumen Network API provides programmatic access to Lumen's network and data services. The Developer Center enables access to simple, global, secure, and reliable network APIs that allow customers t
  name: Lumen Network API
  slug: network-api
- description: Bandwidth provisioning and adjustment
  name: Lumen Technologies Bandwidth API
  slug: lumen-technologies-bandwidth-api
- description: Manage internet connections
  name: Lumen Technologies Connections API
  slug: lumen-technologies-connections-api
artifact_total: 11
collections:
- collection_type: open
  name: Lumen Internet On-Demand API
  slug: open-lumen-internet-on-demand-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lumen-technologies-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumen-technologies-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lumen-technologies-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lumen-technologies-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lumen-Technologies-LLC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lumentechnologies
- group: company
  title: ''
  type: Website
  url: https://www.lumen.com
- group: start
  title: ''
  type: Portal
  url: https://developer.lumen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lumen.com/library
- group: operate
  title: ''
  type: FAQ
  url: https://developer.lumen.com/faq
- group: operate
  title: ''
  type: Support
  url: https://www.lumen.com/help/en-us/developer-center.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lumen.com/en-us/about/legal/api-developer-terms-and-conditions.html
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.lumen.com/llms.txt
created: '2026-03-21'
description: Lumen Technologies is a multinational technology company that delivers networking, edge cloud, security, communication and collaboration, and managed and professional services to global enterprises and consumers. Through its Developer Center, Lumen exposes REST APIs that allow customers to programmatically provision and manage network and bandwidth services across its global fiber infrastructure using OAuth 2.0 authentication.
finops:
- name: Lumen Technologies Finops
  service_category: Networking
  slug: lumen-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lumen-technologies.png
layout: provider
modified: '2026-05-19'
name: Lumen Technologies
nav: Providers
network: true
overview: 'Lumen Technologies publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bandwidth API and Connections API. Tagged areas include Bandwidth, Edge Cloud, Fiber, Infrastructure, and Internet.


  Lumen Technologies'' developer surface includes authentication, developer portal, documentation, FAQ, support, and 8 more developer resources.'
plans:
- name: Lumen Technologies Plans Pricing
  plan_count: 2
  slug: lumen-technologies-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Lumen Technologies Rate Limits
  slug: lumen-technologies-rate-limits
scopes:
- name: Lumen Technologies Scopes
  scope_count: 2
  slug: lumen-technologies-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 41.5
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 45.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumen-technologies/refs/heads/main/screenshots/lumen-technologies-2026-06-20T184754.png
security:
- kind: authentication
  name: Lumen Technologies Authentication
  slug: lumen-technologies-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lumen Technologies Domain Security
  slug: lumen-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lumen-technologies
tags:
- Bandwidth
- Edge Cloud
- Fiber
- Infrastructure
- Internet
- Network
- Networking
- Security
- Telecom
website: https://www.lumen.com
---
