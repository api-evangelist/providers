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
- acting_count: 8
  human_in_the_loop: 1
  name: Passage 1Password Agentic Access
  operation_count: 11
  slug: passage-1password-agentic-access
  summary_line: 11 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.passage.id/v1
  baseurl_source: declared
  description: WebAuthn (passkey) device management for a user.
  name: Passage by 1Password Devices API
  slug: passage-1password-devices-api
- baseURL: https://api.passage.id/v1
  baseurl_source: declared
  description: Magic link creation for passwordless login and identifier verification.
  name: Passage by 1Password Magic Links API
  slug: passage-1password-magic-links-api
- baseURL: https://api.passage.id/v1
  baseurl_source: declared
  description: Refresh-token management for a user.
  name: Passage by 1Password Tokens API
  slug: passage-1password-tokens-api
- baseURL: https://api.passage.id/v1
  baseurl_source: declared
  description: User administration for a Passage app.
  name: Passage by 1Password Users API
  slug: passage-1password-users-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Passage by 1Password Management Devices API
  slug: open-passage-1password-devices-api
- collection_type: open
  name: Passage by 1Password Management Devices Magic Links API
  slug: open-passage-1password-magic-links-api
- collection_type: open
  name: Passage by 1Password Management Devices Tokens API
  slug: open-passage-1password-tokens-api
- collection_type: open
  name: Passage by 1Password Management Devices Users API
  slug: open-passage-1password-users-api
- collection_type: open
  name: Passage by 1Password Management API
  slug: open-passage-1password
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/passage-1password-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/passage-1password-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/passage-1password-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passage-1password-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/passage-1password-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/passageidentity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1password
- group: company
  title: ''
  type: Website
  url: https://passage.1password.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.passage.id/home
- group: commercial
  title: ''
  type: Plans
  url: plans/passage-1password-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/passage-1password-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/passage-1password-finops.yml
created: '2026-06-20'
description: Passage by 1Password is a passwordless authentication platform that lets developers add passkeys (WebAuthn), magic links, and biometric login to their apps. It exposes a REST Management API at https://api.passage.id/v1 for server-side user administration (CRUD, devices, tokens) and magic link creation, alongside frontend Auth/WebAuthn flows. Note - 1Password has announced that the Passage product is being retired on 2026-01-16; this catalog documents the API as published and is distinct from the separate 1Password secrets-manager catalog.
finops:
- name: Passage 1Password Finops
  service_category: Identity and Access Management
  slug: passage-1password-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/passage-1password.png
layout: provider
modified: '2026-06-20'
name: Passage by 1Password
nav: Providers
network: true
overview: 'Passage by 1Password publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Magic Links API, Tokens API, and 1 more. Tagged areas include Authentication, Passkeys, WebAuthn, Passwordless, and Identity.


  Passage by 1Password''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Passage 1Password Plans Pricing
  plan_count: 3
  slug: passage-1password-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Passage 1Password Rate Limits
  slug: passage-1password-rate-limits
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passage-1password/refs/heads/main/screenshots/passage-1password-2026-06-20T191432.png
security:
- kind: authentication
  name: Passage 1Password Authentication
  slug: passage-1password-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Passage 1Password Domain Security
  slug: passage-1password-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Passage 1Password Vulnerability Disclosure
  slug: passage-1password-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Passage 1Password Trust Center
  slug: passage-1password-trust-center
  summary_line: SOC 2
slug: passage-1password
tags:
- Authentication
- Passkeys
- WebAuthn
- Passwordless
- Identity
- Magic Links
website: https://passage.1password.com
---
