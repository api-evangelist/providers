---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: JWT-authenticated Virgil Cloud services — Cards (public key + identity management), Keyknox (private-key storage), Pythia (password PRF) and PFS (perfect-forward-secrecy messaging). Consumed through t
  name: Virgil Cloud API
  slug: virgil-cloud-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.virgilsecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.virgilsecurity.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.virgilsecurity.com/docs/platform/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.virgilsecurity.com/docs/e3kit/get-started/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VirgilSecurity
- group: company
  title: ''
  type: Blog
  url: https://virgilsecurity.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://virgilsecurity.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://virgilsecurity.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.virgilsecurity.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.virgilsecurity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virgilsecurity.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virgilsecurity.com/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/virgil-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/virgil-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/virgil-security-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virgil-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virgil-security-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virgil-security-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virgil-security-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virgil-security-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virgil-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.virgilsecurity.com/
created: '2026-07-17'
description: Virgil Security is an end-to-end encryption and key-management platform for developers. It ships client SDKs and JWT-authenticated cloud services that let applications add end-to-end encryption for messaging and files (E3Kit), breach-proof password and data protection using Password-Hardened Encryption and the Pythia PRF protocol (PureKit), secure private-key storage and sync (Keyknox), Double Ratchet perfect-forward-secrecy messaging (Ratchet), and IoT device security and provisioning (IoTKit). The platform's Virgil Cards service manages public keys and identities, and its cryptography runs client-side so providers never hold plaintext, helping teams meet HIPAA, GDPR and PCI DSS requirements. SDKs are published for JavaScript/TypeScript, Python, Go, Java, Swift, PHP, Ruby, .NET and C/C++, with a Go CLI for account and key management.
image: https://virgilsecurity.com/images/virgil_800x500.png
layout: provider
modified: '2026-07-21'
name: Virgil Security
nav: Providers
network: true
overview: 'Virgil Security publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Encryption, End-to-End Encryption, and Cryptography.


  Virgil Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 30.4
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virgil-security/refs/heads/main/screenshots/virgil-security-2026-09-02T165954.png
security:
- kind: authentication
  name: Virgil Security Authentication
  slug: virgil-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Virgil Security Domain Security
  slug: virgil-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: virgil-security
tags:
- Company
- Security
- Encryption
- End-to-End Encryption
- Cryptography
- Key Management
- Authentication
- Passwords
- IoT Security
- Developer Tools
website: http://www.virgilsecurity.com/
---
