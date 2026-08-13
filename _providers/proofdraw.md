---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Provably-fair random selection REST API (v1) covering draw lifecycle, account, health, and public verification artifacts. HMAC-signed webhooks. Bearer API-key auth.
  name: ProofDraw API
  slug: proofdraw-api
artifact_total: 7
asyncapis:
- description: ''
  name: Proofdraw Webhooks
  slug: proofdraw-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://proofdraw.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://proofdraw.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://proofdraw.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://proofdraw.com/api
- group: operate
  title: ''
  type: Support
  url: https://proofdraw.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/proofdraw
- group: start
  title: ''
  type: SignUp
  url: https://proofdraw.com/register
- group: start
  title: ''
  type: Login
  url: https://proofdraw.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://proofdraw.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://proofdraw.com/privacy
- group: other
  title: ''
  type: Whitepaper
  url: https://proofdraw.com/whitepaper
- group: company
  title: ''
  type: Twitter
  url: https://x.com/proofdraw
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/proofdraw
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/proofdraw/verifier
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proofdraw-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/proofdraw-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/proofdraw-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/proofdraw-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proofdraw-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/proofdraw-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/proofdraw-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/proofdraw-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/proofdraw-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/proofdraw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/proofdraw-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proofdraw-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/proofdraw-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://proofdraw.com/contact
created: '2026-07-13'
description: Provably-fair random selection REST API that seals entry lists with SHA-256 commitments bound to future drand (League of Entropy) randomness rounds, producing publicly verifiable draw receipts with client-side open-source verification. A draw is created, entries are added as opaque ticket ids, then sealed against a chosen future beacon round on the quicknet (3s) or classic (30s) chain; the canonical list file is hashed, mirrored to a public GitHub repository, and anchored with OpenTimestamps, so any entrant can re-derive the winner in their own browser from public sources alone. Serves giveaways, raffles and sweepstakes, non-profit draws, audit sample selection and task allocation, with HMAC-signed webhooks and bearer API-key authentication.
image: https://proofdraw.com/og.png
layout: provider
modified: '2026-08-11'
name: ProofDraw
nav: Providers
network: true
overview: 'ProofDraw publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include randomness, provably-fair, drand, verifiable-randomness, and cryptography.


  The ProofDraw catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ProofDraw''s developer surface includes documentation, API reference, support, signup flow, authentication, sandbox, and 23 more developer resources.'
plans:
- name: Proofdraw Plans Pricing
  plan_count: 2
  slug: proofdraw-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Proofdraw Rate Limits
  slug: proofdraw-rate-limits
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 59.1
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 49.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Proofdraw Authentication
  slug: proofdraw-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Proofdraw Domain Security
  slug: proofdraw-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Proofdraw Vulnerability Disclosure
  slug: proofdraw-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: proofdraw
tags:
- randomness
- provably-fair
- drand
- verifiable-randomness
- cryptography
- raffle
- giveaway
- sweepstakes
- lottery
- verification
- webhooks
- rest-api
website: https://proofdraw.com/
---
