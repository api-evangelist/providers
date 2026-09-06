---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Corbado Agentic Access
  operation_count: 29
  slug: corbado-agentic-access
  summary_line: 29 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: Short-lived tokens authorizing Corbado Connect frontend flows.
  name: Corbado ConnectTokens API
  slug: corbado-connecttokens-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: Project data exports and download links.
  name: Corbado Exports API
  slug: corbado-exports-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: Manage login identifiers (email, phone, username) attached to a user.
  name: Corbado Identifiers API
  slug: corbado-identifiers-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: Record and query passkey lifecycle events for a user.
  name: Corbado PasskeyEvents API
  slug: corbado-passkeyevents-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: WebAuthn passkey registration and login ceremonies and verification.
  name: Corbado Passkeys API
  slug: corbado-passkeys-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: List and revoke authenticated sessions.
  name: Corbado Sessions API
  slug: corbado-sessions-api
- baseURL: https://backendapi.corbado.io/v2
  baseurl_source: declared
  description: Create and manage end users and their social logins and credentials.
  name: Corbado Users API
  slug: corbado-users-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Corbado Backend ConnectTokens API
  slug: open-corbado-connecttokens-api
- collection_type: open
  name: Corbado Backend ConnectTokens Exports API
  slug: open-corbado-exports-api
- collection_type: open
  name: Corbado Backend ConnectTokens Identifiers API
  slug: open-corbado-identifiers-api
- collection_type: open
  name: Corbado Backend ConnectTokens PasskeyEvents API
  slug: open-corbado-passkeyevents-api
- collection_type: open
  name: Corbado Backend ConnectTokens Passkeys API
  slug: open-corbado-passkeys-api
- collection_type: open
  name: Corbado Backend ConnectTokens Sessions API
  slug: open-corbado-sessions-api
- collection_type: open
  name: Corbado Backend ConnectTokens Users API
  slug: open-corbado-users-api
- collection_type: open
  name: Corbado Backend API
  slug: open-corbado
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/corbado-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/corbado-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/corbado-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corbado-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corbado-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corbado
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/corbado
- group: company
  title: ''
  type: Website
  url: https://www.corbado.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corbado.com
- group: commercial
  title: ''
  type: Plans
  url: plans/corbado-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/corbado-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/corbado-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.corbado.com/blog
created: '2026-06-20'
description: Corbado is a passkey-first authentication platform that helps companies add WebAuthn passkeys to their products. The Corbado Backend API manages users, login identifiers, sessions, passkeys/credentials, and connect tokens, while passkey intelligence and analytics surface readiness, adoption, and per-user debugging for passwordless rollouts.
finops:
- name: Corbado Finops
  service_category: Identity and Access Management
  slug: corbado-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corbado.png
layout: provider
modified: '2026-06-20'
name: Corbado
nav: Providers
network: true
overview: 'Corbado publishes 7 APIs on the [APIs.io](https://apis.io/) network, including ConnectTokens API, Exports API, Identifiers API, and 4 more. Tagged areas include Authentication, Passkeys, WebAuthn, Passwordless, and CIAM.


  Corbado''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Corbado Plans Pricing
  plan_count: 4
  slug: corbado-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Corbado Rate Limits
  slug: corbado-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corbado/refs/heads/main/screenshots/corbado-2026-06-20T175018.png
security:
- kind: authentication
  name: Corbado Authentication
  slug: corbado-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Corbado Domain Security
  slug: corbado-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Corbado Vulnerability Disclosure
  slug: corbado-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Corbado Trust Center
  slug: corbado-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: corbado
tags:
- Authentication
- Passkeys
- WebAuthn
- Passwordless
- CIAM
- Identity
website: https://www.corbado.com
---
