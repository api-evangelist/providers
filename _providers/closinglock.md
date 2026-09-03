---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.closinglock.com/
- group: company
  title: ''
  type: Blog
  url: https://www.closinglock.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.closinglock.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.closinglock.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://closinglock.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.closinglock.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.closinglock.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: security/closinglock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/closinglock-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/closinglock-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/closinglock-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/closinglock-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/closinglock-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/closinglock-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/closinglock_stock/
coverage:
  checked: '2026-08-09'
  detail: Closinglock ships an end-user closing platform only — its 55-page sitemap contains no developer, API, or integration page, api./docs./developer.closinglock.com do not resolve at all, and its SoftPro, RamQuest, ResWare and DocuSign integrations are built bilaterally by those vendors rather than through any published API program.
  evidence:
  - status: 0
    url: https://api.closinglock.com/
  - status: 0
    url: https://docs.closinglock.com/
  - status: 404
    url: https://closinglock.com/openapi.json
  - status: 404
    url: https://closinglock.com/graphql
  - status: 200
    url: https://www.closinglock.com/page-sitemap.xml
  - status: 404
    url: https://www.closinglock.com/llms.txt
  - status: 200
    url: https://www.closinglock.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Closinglock is an Austin, Texas fintech and fraud-prevention company whose platform secures the money movement and identity checks inside a residential real estate closing. Title companies, real estate attorneys, agents, underwriters and their buyers and sellers use it to share wire instructions over an authenticated channel instead of email, verify identity and bank-account ownership before funds move, collect and disburse funds through SecurePay digital payments, retrieve and verify mortgage payoff statements, manage and e-sign closing documents, run two-way text messaging with the parties to a file, and evidence FinCEN and ALTA Best Practices obligations. The company announced SOC 2 Type II certification in August 2023 and raised a $34M Series B led by Sageview Capital in January 2025. Closinglock ships integrations into the major title production systems — SoftPro, RamQuest and ResWare — plus a DocuSign e-signature partnership, but those integrations are built bilaterally
  with each vendor: as of this profile Closinglock publishes no public developer portal, API reference, or machine-readable contract.'
image: https://www.closinglock.com/wp-content/uploads/2025/12/closing_lock_thumb.png
layout: provider
modified: '2026-08-09'
name: Closinglock
nav: Providers
network: true
overview: 'Closinglock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Title Insurance, Fraud Prevention, Payments, and Identity Verification.


  Closinglock''s developer surface includes engineering blog, support, signup flow, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 12.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/closinglock/refs/heads/main/screenshots/closinglock-2026-09-02T145109.png
security:
- kind: domain-security
  name: Closinglock Domain Security
  slug: closinglock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Closinglock Vulnerability Disclosure
  slug: closinglock-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: closinglock
tags:
- Real-Estate
- Title Insurance
- Fraud Prevention
- Payments
- Identity Verification
- Document-Management
- Fintech
- Compliance
- Security
- Company
website: https://www.closinglock.com/
---
