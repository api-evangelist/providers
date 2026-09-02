---
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
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tmt Id Agentic Access
  operation_count: 17
  slug: tmt-id-agentic-access
  summary_line: 17 operations · 12 acting
api_count: 7
apis:
- description: Authenticate user with MNO or OTP. These endpoints can be directly called by the users.
  name: TMT ID Authenticate API
  slug: tmt-id-authenticate-api
- description: The HTTP API API from TMT ID — 3 operation(s) for http api.
  name: TMT ID HTTP API
  slug: tmt-id-http-api-api
- description: The HTTP API v1.3 API from TMT ID — 2 operation(s) for http api v1.3.
  name: TMT ID HTTP API v1.3 API
  slug: tmt-id-http-api-v1-3-api
- description: The HTTP API v2.0 API from TMT ID — 3 operation(s) for http api v2.0.
  name: TMT ID HTTP API v2.0 API
  slug: tmt-id-http-api-v2-0-api
- description: The Network Biometrics API from TMT ID — 1 operation(s) for network biometrics.
  name: TMT ID Network Biometrics API
  slug: tmt-id-network-biometrics-api
- description: Service endpoints
  name: TMT ID Service API
  slug: tmt-id-service-api
- description: The Standard API Call API from TMT ID — 1 operation(s) for standard api call.
  name: TMT ID Standard API Call API
  slug: tmt-id-standard-api-call-api
- description: The v2 (deprecated) API from TMT ID — 2 operation(s) for v2 (deprecated).
  name: TMT ID v2 (deprecated) API
  slug: tmt-id-v2-deprecated-api
artifact_total: 21
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
  title: ''
  type: Overlay
  url: overlays/tmt-id-verify-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-velocity-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-live-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-teleshield-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-score-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-authenticate-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tmt-id-network-biometrics-overlay.yaml
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
  name: TMT ID MCP Server
  slug: tmt-id-mcp-server
modified: '2026-07-25'
name: TMT ID
nav: Providers
network: true
overview: 'TMT ID publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authenticate API, HTTP API, HTTP API v1.3 API, and 5 more. Tagged areas include Telecommunications, United Kingdom, Identity Verification, Mobile Identity, and SIM Swap.


  TMT ID''s developer surface includes sandbox, authentication, documentation, developer portal, signup flow, engineering blog, support, and 38 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 50.6
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
