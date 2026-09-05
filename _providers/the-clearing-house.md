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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The RTP network is The Clearing House's real-time payments scheme for the United States, moving credit-push payments instantly, 24/7/365, with final settlement up to $10 million per transaction. It is
  name: RTP Network (ISO 20022 Messaging)
  slug: rtp-network
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.theclearinghouse.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.theclearinghouse.org/payment-systems/rtp/technical-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.theclearinghouse.org/payment-systems/rtp/document-library
- group: company
  title: ''
  type: Blog
  url: https://www.theclearinghouse.org/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theclearinghouse.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theclearinghouse.org/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-clearing-house-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-clearing-house-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-clearing-house-llms.txt
created: '2026-07-24'
description: 'The Clearing House (TCH) is a U.S. banking association and payments company owned by many of the largest commercial banks. It operates three core payment systems: CHIPS (large-value wire clearing), the EPN automated clearing house (ACH), and the RTP network, the private-sector real-time payments rail it launched in 2017 as the first new U.S. payments infrastructure in decades. RTP is a 24/7/365 instant-payments scheme built on the ISO 20022 messaging standard, supporting immediate credit-push transfers up to $10 million with final settlement, plus Request for Payment (RfP), remittance data, and a UID addressing/directory lookup. TCH is the scheme operator for the U.S. market and competes with the Federal Reserve''s FedNow service. Its API posture is documentation- and rulebook-first: TCH does not publish an open, self-serve public REST API or downloadable OpenAPI/Swagger specification. Instead it publishes ISO 20022 message specifications (pacs, pain, camt, remt) as PDFs, the
  RTP network operating rules, playbooks, and a technology-provider program. Real-time HTTP/JSON RTP APIs are surfaced to businesses by participating financial institutions (for example U.S. Bank) and registered technology providers that connect to the RTP network on their behalf.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: The Clearing House (RTP)
nav: Providers
network: true
overview: 'The Clearing House (RTP) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, United States, Real-Time Payments, Instant Payments, and ISO 20022.


  The Clearing House (RTP)''s developer surface includes documentation, API reference, engineering blog, and 6 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 12.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-clearing-house/refs/heads/main/screenshots/the-clearing-house-2026-09-02T163332.png
security:
- kind: domain-security
  name: The Clearing House Domain Security
  slug: the-clearing-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-clearing-house
tags:
- Payments
- United States
- Real-Time Payments
- Instant Payments
- ISO 20022
- Account-to-Account
- Payment Rails
- Scheme Operator
- Request for Payment
website: https://www.theclearinghouse.org/
---
