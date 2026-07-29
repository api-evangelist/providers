---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tmt Id Agentic Access
  operation_count: 17
  slug: tmt-id-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 7
apis:
- description: Real-time verification of a mobile number against mobile network operator data. A single POST returns the requested datapoints for a number — subscriber name and address match, account type and tenure
  name: TMT Verify API
  slug: tmt-id-verify
- description: Global mobile number lookup that returns the network operator currently serving a number, including ported numbers, using live HLR/ENUM sourced data. Delivered as a single GET with the API key and sec
  name: TMT Velocity API
  slug: tmt-id-velocity
- description: Checks whether a mobile number is currently assigned and in active use on a network, for data cleansing, deliverability and pre-send validation. Offered over HTTPS and over ENUM/NAPTR against live.tmt
  name: TMT Live API
  slug: tmt-id-live
- description: Telephony fraud and routing intelligence. Five documented POST operations cover TeleShield Routing, TeleShield Fraud and Enhanced Fraud in both the v1.3 and v2.0 data dictionaries, returning number-ra
  name: TMT TeleShield API
  slug: tmt-id-teleshield
- description: Returns a credibility score for a phone number, derived from the age, stability and behaviour of the number across TMT ID's operator data, for risk decisioning at onboarding, login and transaction tim
  name: TMT Score API
  slug: tmt-id-score
- description: Silent Network Authentication and OTP fallback. The client exchanges HTTP Basic credentials at /oauth/token for a PASETO bearer token, calls /get_config to learn how the relevant mobile network operat
  name: TMT Authenticate API
  slug: tmt-id-authenticate
- description: The Phronesis-derived flagship, a single POST that assembles a configurable set of mobile network signals about a number and device — SIM swap and device change look-back windows, GSMA device blacklis
  name: Network Biometrics API
  slug: tmt-id-network-biometrics
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tmtid.com/developers/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tmt-id-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tmt-id-security.txt
- group: auth
  title: ''
  type: Security
  url: https://tmtid.com/responsible-vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tmt-id-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tmt-id-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/tmt-id-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tmt-id-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/tmt-id-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tmt-id-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tmt-id-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tmt-id-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tmt-id-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tmt-id-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/tmt-id-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tmt-id-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tmt-id-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tmt-id-domain-security.yml
- group: auth
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
mcp_servers:
- description: ''
  name: tmt-id-mcp.yml
  slug: tmt-id-mcpyml
modified: '2026-07-25'
name: TMT ID
nav: Providers
network: true
overview: 'TMT ID publishes 7 APIs on the [APIs.io](https://apis.io/) network, including TMT Verify API, TMT Velocity API, TMT Live API, and 4 more. Tagged areas include Telecommunications, United Kingdom, Identity Verification, Mobile Identity, and SIM Swap.


  TMT ID''s developer surface includes sandbox, authentication, documentation, developer portal, signup flow, engineering blog, support, and 31 more developer resources.'
random_paper: 24
score:
  band: developing
  composite: 44.0
  delta: 1.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 48.2
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 71.4
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
