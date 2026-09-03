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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://proofdraw.com/api/v1
  baseurl_source: declared
  description: The Account API from ProofDraw — 2 operation(s) for account.
  name: ProofDraw Account API
  slug: proofdraw-account-api
- baseURL: https://proofdraw.com/api/v1
  baseurl_source: declared
  description: The Auth API from ProofDraw — 2 operation(s) for auth.
  name: ProofDraw Auth API
  slug: proofdraw-auth-api
- baseURL: https://proofdraw.com/api/v1
  baseurl_source: declared
  description: The Draws API from ProofDraw — 6 operation(s) for draws.
  name: ProofDraw Draws API
  slug: proofdraw-draws-api
- baseURL: https://proofdraw.com/api/v1
  baseurl_source: declared
  description: The System API from ProofDraw — 1 operation(s) for system.
  name: ProofDraw System API
  slug: proofdraw-system-api
- baseURL: https://proofdraw.com/api/v1
  baseurl_source: declared
  description: Public, unauthenticated artifacts used to verify a draw.
  name: ProofDraw Verification API
  slug: proofdraw-verification-api
artifact_total: 12
asyncapis:
- description: ''
  name: Proofdraw Webhooks
  slug: proofdraw-webhooks
collections:
- collection_type: open
  name: ProofDraw API
  slug: open-proofdraw-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/proofdraw/verifier/blob/main/LICENSE
- group: other
  title: ''
  type: Overlay
  url: overlays/proofdraw-api-overlay.yaml
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
overview: 'ProofDraw publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Auth API, Draws API, and 2 more. Tagged areas include Randomness, Provably Fair, drand, Verifiable Randomness, and Cryptography.


  The ProofDraw catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ProofDraw''s developer surface includes documentation, API reference, support, signup flow, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Proofdraw Plans Pricing
  plan_count: 2
  slug: proofdraw-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Proofdraw Rate Limits
  slug: proofdraw-rate-limits
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 59.6
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 33.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proofdraw/refs/heads/main/screenshots/proofdraw-2026-08-17T081348.png
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
- Randomness
- Provably Fair
- drand
- Verifiable Randomness
- Cryptography
- raffle
- giveaway
- Sweepstakes
- Lottery
- Verification
- Webhook
- REST API
website: https://proofdraw.com/
---
