---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://api.justyo.co
  baseurl_source: declared
  description: Read account/subscriber information.
  name: justyo Account API
  slug: justyo-account-api
- baseURL: https://api.justyo.co
  baseurl_source: declared
  description: Send Yo notifications to subscribers.
  name: justyo Yo API
  slug: justyo-yo-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yo Account API
  slug: open-justyo-account-api
- collection_type: open
  name: Account Yo API
  slug: open-justyo-yo-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/overlays/justyo-yo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/justyo-yo-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://justyo.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.justyo.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://dev.justyo.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YoApp
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.justyo.co/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/packages/justyo-packages.yml
  title: ''
  type: Packages
  url: packages/justyo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/packages/justyo-packages.yml
  title: ''
  type: SDKs
  url: packages/justyo-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/mcp/justyo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/justyo-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/llms/justyo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/justyo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/well-known/justyo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/justyo-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/authentication/justyo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/justyo-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/conventions/justyo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/justyo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/lifecycle/justyo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/justyo-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/security/justyo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/justyo-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Yo (justyo.co) was a single-tap notification app and "the world''s simplest API." A service registered an API username, received an api_token, and could push a lightweight "Yo" notification to a single subscriber or broadcast to all subscribers, optionally attaching a link, plus read the subscriber count. The Yo API had effectively one job — fire a push — with an api_token for auth (an OAuth 2.0 page was documented but never enabled) and first-party client SDKs across Python, PHP, Java, Node, Ruby, Scala and iOS under the github.com/YoApp organization. The Yo service is now defunct: the justyo.co host is suspended and its api/docs/dev subdomains no longer resolve. This API Evangelist profile captures the historical Yo API surface for the record.'
image: https://raw.githubusercontent.com/api-evangelist/justyo/refs/heads/main/openapi/justyo-yo-openapi.yml
layout: provider
modified: '2026-09-16'
name: justyo
nav: Providers
network: true
overview: 'justyo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Yo API. Tagged areas include Company, Notification, Push Notifications, Messaging, and Mobile.


  justyo''s developer surface includes documentation, signup flow, authentication, and 13 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Justyo Rate Limits
  slug: justyo-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  provenance:
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Justyo Authentication
  slug: justyo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Justyo Domain Security
  slug: justyo-domain-security
  summary_line: no transport/DNS hardening detected
slug: justyo
tags:
- Company
- Notification
- Push Notifications
- Messaging
- Mobile
- Developer Tools
- Defunct
website: https://justyo.co
---
