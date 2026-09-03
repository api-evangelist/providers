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
    delegated_identity: false
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
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Podbean Api Agentic Access
  operation_count: 8
  slug: podbean-api-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. Provides OAu
  name: Podbean API
  slug: podbean-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Per-podcast analytics and report downloads.
  name: Podbean API Analytics API
  slug: podbean-api-analytics-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: List and inspect episodes.
  name: Podbean API Episodes API
  slug: podbean-api-episodes-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Token issuance endpoints.
  name: Podbean API OAuth API
  slug: podbean-api-oauth-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: List podcasts in the account.
  name: Podbean API Podcasts API
  slug: podbean-api-podcasts-api
- baseURL: https://api.podbean.com/v1
  baseurl_source: declared
  description: Manage private podcast members.
  name: Podbean API PrivateMembers API
  slug: podbean-api-privatemembers-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Podbean Analytics API
  slug: open-podbean-api-analytics-api
- collection_type: open
  name: Podbean Analytics Episodes API
  slug: open-podbean-api-episodes-api
- collection_type: open
  name: Podbean Analytics OAuth API
  slug: open-podbean-api-oauth-api
- collection_type: open
  name: Podbean Analytics Podcasts API
  slug: open-podbean-api-podcasts-api
- collection_type: open
  name: Podbean Analytics PrivateMembers API
  slug: open-podbean-api-privatemembers-api
- collection_type: open
  name: Podbean API
  slug: open-podbean-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/podbean-api-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podbean-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podbean-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podbean-api-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podbean-api-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.podbean.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podbean
- group: company
  title: ''
  type: Website
  url: https://www.podbean.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.podbean.com/podbean-api-docs/
created: '2025-05-02'
description: This is for third-party apps to connect to Podbean in order to manage a user's podcast. To manage your own podcast via API, please use Client Credentials and Get Multiple Podcasts Tokens. The Podbean API supports OAuth 2.0 authentication and provides programmatic access to podcasts, episodes, analytics, and account management resources.
finops:
- name: Podbean Api Finops
  service_category: API
  slug: podbean-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podbean-api.png
layout: provider
modified: '2026-04-28'
name: Podbean API
nav: Providers
network: true
overview: 'Podbean API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Episodes API, OAuth API, and 2 more. Tagged areas include Podcasts, Podcasting, Audio, Media, and Authentication.


  Podbean API''s developer surface includes authentication, engineering blog, documentation, and 6 more developer resources.'
plans:
- name: Podbean Api Plans Pricing
  plan_count: 3
  slug: podbean-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Podbean Api Rate Limits
  slug: podbean-api-rate-limits
scopes:
- name: Podbean Api Scopes
  scope_count: 5
  slug: podbean-api-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.8
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podbean-api/refs/heads/main/screenshots/podbean-api-2026-06-20T191831.png
security:
- kind: authentication
  name: Podbean Api Authentication
  slug: podbean-api-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Podbean Api Domain Security
  slug: podbean-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: podbean-api
tags:
- Podcasts
- Podcasting
- Audio
- Media
- Authentication
- Episodes
website: https://www.podbean.com
---
