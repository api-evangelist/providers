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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Passage 1Password Agentic Access
  operation_count: 11
  slug: passage-1password-agentic-access
  summary_line: 11 operations · 8 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: WebAuthn (passkey) device management for a user.
  name: Passage by 1Password Devices API
  slug: passage-1password-devices-api
- description: Magic link creation for passwordless login and identifier verification.
  name: Passage by 1Password Magic Links API
  slug: passage-1password-magic-links-api
- description: Refresh-token management for a user.
  name: Passage by 1Password Tokens API
  slug: passage-1password-tokens-api
- description: User administration for a Passage app.
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
random_paper: 78
rate_limits:
- limit_count: 2
  name: Passage 1Password Rate Limits
  slug: passage-1password-rate-limits
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
