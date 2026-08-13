---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 7
apis:
- description: Network-based verification that the mobile number a user declares is the number of the SIM the request is actually coming from, used to replace or reinforce SMS OTP. Singtel documents this as the CAMA
  name: SingVerify Number Verify API
  slug: singverify-number-verify-api
- description: Real-time signal indicating whether the SIM bound to a mobile number has been changed recently, so that a relying party can block account-takeover attempts that rely on intercepting SMS one-time passc
  name: SingVerify SIM Swap API
  slug: singverify-sim-swap-api
- description: Verifies whether a mobile device is within an expected area or country at the time of a login or transaction, using network-derived location rather than handset GPS. Maps to the CAMARA Device Location
  name: SingVerify Device Location API
  slug: singverify-device-location-api
- description: Reports whether a subscriber's device is currently roaming outside Singapore, used as a risk signal in fraud and authentication decisions. Maps to the CAMARA Device Roaming Status / Device Status fami
  name: SingVerify Device Roaming API
  slug: singverify-device-roaming-api
- description: Detects whether a user is on an active voice call at the moment they attempt a high-value transaction, a signal used to interdict authorised-push-payment and social-engineering fraud. This is Singtel'
  name: SingVerify Scam Sniffer API
  slug: singverify-scam-sniffer-api
- description: Application-to-person SMS sending and receiving for business applications, sold as part of the Singtel CPaaS portfolio. The public page describes the capability and benefits but publishes no endpoint,
  name: Singtel CPaaS SMS API
  slug: singtel-cpaas-sms-api
- description: Programmable voice / VoIP calling embedded into business applications, sold as part of the Singtel CPaaS portfolio. As with the SMS API, the public page is a product description with an enquiry form —
  name: Singtel CPaaS Voice API
  slug: singtel-cpaas-voice-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singtel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/singtel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.singtel.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/singtel-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/singtel-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/singtel-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/singtel-lifecycle.yml
- group: company
  title: ''
  type: Website
  url: https://www.singtel.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/singtel
- group: company
  title: ''
  type: Blog
  url: https://www.singtel.com/about-us/media-centre/news-releases
- group: operate
  title: ''
  type: Support
  url: https://www.singtel.com/business/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.singtel.com/data-protection
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/mobility/singverify
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/mobility/mobility-solutions/singtel-cpaas
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/5g/paragon
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/5g/paragon-for-telcos
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/iot
- group: docs
  title: ''
  type: Documentation
  url: https://www.singtel.com/business/products-services/5g/paragon-for-enterprises
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.singtel.com/business/products-services/mobility/terms/singverify-tnc
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.singtel.com/standard-agreement
- group: company
  title: ''
  type: Partner
  url: https://adunaglobal.com/
- group: company
  title: ''
  type: Partner
  url: https://baex.bridgealliance.com/
- group: other
  title: ''
  type: Standard
  url: https://camaraproject.org/
created: '2026-07-25'
description: 'Singtel (Singapore Telecommunications Limited) is Singapore''s largest mobile network operator and the anchor communications group of Southeast Asia, with a regional footprint that includes Optus in Australia and associate stakes in Airtel, AIS, Globe and Telkomsel. In the network-API value chain Singtel sits on the supply side: it owns the mobile network signals — SIM, line, device, location, call state — that the CAMARA specifications turn into callable APIs, and it packages them for Singapore as SingVerify, a five-API anti-fraud and identity suite built on the GSMA Open Gateway framework. It also operates Paragon, its own 5G/edge/network orchestration platform, which powers the Bridge Alliance API Exchange (BAEx) federating network APIs across Bridge Alliance member operators, and it is one of the twelve carrier equity partners in Aduna, the Ericsson-led joint venture that aggregates operator network APIs into a single global commercial channel. Its API posture, however,
  is partner-gated and sales-led: as of July 2026 there is no first-party developer portal (developer., developers., docs. and opengateway. subdomains do not resolve), no published OpenAPI, no sandbox, no SDKs and no self-serve signup. Every SingVerify and CPaaS API page on singtel.com terminates in an enterprise enquiry form, and the BAEx portal is an explicit login wall for approved partners. Developers reach Singtel''s network capabilities through aggregators — Aduna and its platform partners (Vonage, Sinch, Infobip, Google Cloud), the Bridge Alliance exchange, or identity vendors such as IPification — rather than directly from Singtel. Two surfaces do exist and are captured here: www.singtel.com publishes a first-party llms.txt family (root plus consumer, support and corporate companion files, last updated 2026-06-30) that indexes its marketing and support estate for AI systems while naming none of its APIs, and Singtel runs a footer-linked vulnerability disclosure programme at vdp.singtel.com
  and on HackerOne. api.singtel.com is a live Apigee gateway behind Imperva that answers every unrouted path with an Apigee fault envelope — a real gateway with nothing publicly bound to it.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Singtel
nav: Providers
network: true
overview: 'Singtel publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Singapore, Mobile Network Operator, Network APIs, and CAMARA.


  Singtel''s developer surface includes engineering blog, support, documentation, and 20 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 10.5
  previous_composite: 19.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Singtel Domain Security
  slug: singtel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Singtel Vulnerability Disclosure
  slug: singtel-vulnerability-disclosure
  summary_line: Hackerone
slug: singtel
tags:
- Telecommunications
- Singapore
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- Anti-Fraud
- CPaaS
- Messaging
- Voice
- IoT
- 5G
- Edge Computing
- Aduna
- Partner Gated
website: https://www.singtel.com/
---
