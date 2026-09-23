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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tmt Id Agentic Access
  operation_count: 17
  slug: tmt-id-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 7
apis:
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: Authenticate user with MNO or OTP. These endpoints can be directly called by the users.
  name: TMT ID Authenticate API
  slug: tmt-id-authenticate-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The HTTP API API from TMT ID — 3 operation(s) for http api.
  name: TMT ID HTTP API
  slug: tmt-id-http-api-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The HTTP API v1.3 API from TMT ID — 2 operation(s) for http api v1.3.
  name: TMT ID HTTP API v1.3 API
  slug: tmt-id-http-api-v1-3-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The HTTP API v2.0 API from TMT ID — 3 operation(s) for http api v2.0.
  name: TMT ID HTTP API v2.0 API
  slug: tmt-id-http-api-v2-0-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The Network Biometrics API from TMT ID — 1 operation(s) for network biometrics.
  name: TMT ID Network Biometrics API
  slug: tmt-id-network-biometrics-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: Service endpoints
  name: TMT ID Service API
  slug: tmt-id-service-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The Standard API Call API from TMT ID — 1 operation(s) for standard api call.
  name: TMT ID Standard API Call API
  slug: tmt-id-standard-api-call-api
- baseURL: https://api.tmtverify.com
  baseurl_source: declared
  description: The v2 (deprecated) API from TMT ID — 2 operation(s) for v2 (deprecated).
  name: TMT ID v2 (deprecated) API
  slug: tmt-id-v2-deprecated-api
artifact_total: 20
collections:
- collection_type: open
  name: TMT Authenticate API specs
  slug: open-tmt-id-authenticate
- collection_type: open
  name: TMT Live API specs
  slug: open-tmt-id-live
- collection_type: open
  name: Network Biometrics™ by TMT ID
  slug: open-tmt-id-network-biometrics
- collection_type: open
  name: TMT Score API specs
  slug: open-tmt-id-score
- collection_type: open
  name: TMT Teleshield API specs
  slug: open-tmt-id-teleshield
- collection_type: open
  name: TMT Velocity API specs
  slug: open-tmt-id-velocity
- collection_type: open
  name: TMT Verify API specs
  slug: open-tmt-id-verify
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-verify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-verify-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-velocity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-velocity-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-live-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-live-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-teleshield-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-teleshield-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-score-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-score-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-authenticate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-authenticate-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/overlays/tmt-id-network-biometrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tmt-id-network-biometrics-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tmtid.com/developers/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/well-known/tmt-id-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tmt-id-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/well-known/tmt-id-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tmt-id-security.txt
- group: auth
  title: ''
  type: Security
  url: https://tmtid.com/responsible-vulnerability-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/security/tmt-id-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tmt-id-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/llms/tmt-id-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tmt-id-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/conventions/tmt-id-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tmt-id-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/errors/tmt-id-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tmt-id-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/errors/tmt-id-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/tmt-id-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/lifecycle/tmt-id-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tmt-id-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/conformance/tmt-id-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tmt-id-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/sandbox/tmt-id-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tmt-id-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/data-model/tmt-id-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tmt-id-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/mcp/tmt-id-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tmt-id-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/packages/tmt-id-packages.yml
  title: ''
  type: Packages
  url: packages/tmt-id-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/agentic-access/tmt-id-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tmt-id-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/security/tmt-id-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tmt-id-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/security/tmt-id-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tmt-id-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/authentication/tmt-id-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tmt-id-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tmtid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tmtid.com/developers/
- group: start
  title: ''
  type: Portal
  url: https://viteza.tmtanalysis.com/register
- group: start
  title: ''
  type: SignUp
  url: https://viteza.tmtanalysis.com/register
- group: other
  title: ''
  type: Products
  url: https://tmtid.com/products/
- group: company
  title: ''
  type: Blog
  url: https://tmtid.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tmtid.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tmtid.com/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://tmtid.com/acceptable-use-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://tmtid.com/trust-centre/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://tmtid.com/responsible-vulnerability-disclosure-policy/
- group: operate
  title: ''
  type: Support
  url: https://tmtid.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://tmtid.com/faq/
- group: other
  title: ''
  type: Glossary
  url: https://tmtid.com/glossary/
- group: other
  title: ''
  type: CaseStudies
  url: https://tmtid.com/case-studies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tmtid/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/tmtid_limited
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCFSippD9W0TL_rNfk8ETCmQ
created: '2026-07-25'
description: 'TMT ID (trading name of TMT Analysis Limited, London) is a United Kingdom mobile number intelligence and anti-fraud data provider that sits between the mobile network operators and the businesses that need to trust a phone number. Founded in 2017 as TMT Analysis, it acquired Phronesis Technologies in 2023 and rebranded to TMT ID in 2024. It does not own network infrastructure; it aggregates operator, numbering-plan and ENUM data and resells it as real-time REST lookups — number validity and reachability, current network and portability, SIM-swap and device-change events, subscriber-data matching, risk scoring, telephony-fraud and routing intelligence, and silent network authentication as an alternative to SMS OTP. Its API posture is genuinely open by telecom standards: seven product APIs are documented publicly as ReDoc-rendered OpenAPI 3.0 documents at tmtid.com/developer with no login, and the Viteza portal offers self-serve signup with 500 free queries. Credentials for the
  production APIs are still issued through a commercial onboarding conversation rather than instant key generation. TMT ID states on its own site that it is a GSMA Open Gateway member, but it publishes no CAMARA-conformant API — its SIM-swap and network-authentication products ship under TMT ID''s own proprietary schemas, which is the honest position of most of the identity-and-antifraud layer of this market.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: TMT ID
nav: Providers
network: true
overview: 'TMT ID publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authenticate API, HTTP API, HTTP API v1.3 API, and 5 more. Tagged areas include Telecommunications, United Kingdom, Identity Verification, Mobile Identity, and SIM Swap.


  TMT ID''s developer surface includes sandbox, authentication, documentation, developer portal, signup flow, engineering blog, support, and 38 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 49.9
    developer_ergonomics: 54.2
    discoverability: 81.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tmt-id/refs/heads/main/screenshots/tmt-id-2026-08-17T082402.png
security:
- kind: authentication
  name: Tmt Id Authentication
  slug: tmt-id-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Tmt Id Domain Security
  slug: tmt-id-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tmt Id Vulnerability Disclosure
  slug: tmt-id-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tmt Id Trust Center
  slug: tmt-id-trust-center
  summary_line: trust center published
slug: tmt-id
tags:
- Telecommunications
- United Kingdom
- Identity Verification
- Mobile Identity
- SIM Swap
- Anti-Fraud
- Number Intelligence
- Silent Network Authentication
- GSMA Open Gateway
- Network APIs
- ENUM
- KYC
website: https://tmtid.com/
---
