---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Undocumented HTTPS API behind WaveBL's public Certificate of Authenticity tool — the free service at coa.wavebl.com that lets any party verify that a bill of lading or trade document was issued and tr
  name: WaveBL Certificate of Authenticity API
  slug: wavebl-certificate-of-authenticity-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wavebl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wavebl.com/
- group: company
  title: ''
  type: Blog
  url: https://wavebl.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://wsupport.wavebl.com/
- group: start
  title: ''
  type: SignUp
  url: https://register.wavebl.com/wavebl/?trustedOrganizationCode=Generic
- group: commercial
  title: ''
  type: Pricing
  url: https://wavebl.com/pricing-page/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wavebl.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wavebl.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://wavebl.com/wave-bl-achieves-iso-27001-and-27017-compliance-certification/
- group: design
  title: ''
  type: Conformance
  url: conformance/wavebl-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wavebl-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wavebl-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/wavebl-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wavebl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wavebl-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wavebl-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wavebl-llms.txt
coverage:
  checked: '2026-09-04'
  detail: WaveBL's only public API documentation was a single help-centre article stating that its platform complies with the DCSA eBL Issuance and Surrender Response APIs; that Zendesk help centre has been decommissioned and support.wavebl.com now fails the TLS handshake outright, while its replacement — the Salesforce Experience Cloud community at wsupport.wavebl.com — serves an article sitemap that 404s and answers 401 on every non-public path, so integration material is now reachable only by signed-in customers and partners.
  evidence:
  - status: 0
    url: https://support.wavebl.com/hc/en-us/articles/18817090320029-DCSA
  - status: 404
    url: https://wsupport.wavebl.com/s/sitemap-topicarticle-1.xml
  - status: 401
    url: https://wsupport.wavebl.com/.well-known/api-catalog
  - status: 403
    url: https://docs.wavebl.com/openapi.json
  - status: 404
    url: https://wavebl.com/llms.txt
  - status: 403
    url: https://coa.wavebl.com/coadocuments/search
  - status: 0
    url: https://developer.wavebl.com/
  reason: customer-only-docs
  state: gated
created: '2026-09-04'
description: WaveBL is an Israeli digital trade platform, headquartered in Kfar Saba and founded out of the ZIM shipping group, that moves original electronic bills of lading (eBLs) and the trade documents around them between carriers, freight forwarders, cargo owners, customs brokers and banks. Its blockchain-backed, peer-to-peer network issues, endorses, transfers, amends and surrenders title documents without a central repository, and is sold as the WaveBL Digital Document Hub, electronic Master and House Bills of Lading, WaveBL for Customs and a trade finance module that presents structured documents to banks. It is used by MSC, ZIM, Hapag-Lloyd, ONE, PIL, Evergreen and Leschaco among others, is approved by the International Group of P&I Clubs, and has implemented the DCSA Standard Annex for eBL Platform Interoperability so eBLs can cross to other platforms. WaveBL runs a real API programme — it states publicly that its platform complies with the DCSA OpenAPI specification for Issuance
  and the DCSA eBL Surrender Response API — but it operates no developer portal, publishes no API reference, base URL or machine-readable specification, and its only public API article lived on a Zendesk help centre that has since been decommissioned.
image: https://wavebl.com/wp-content/uploads/2024/05/Logo.svg
layout: provider
modified: '2026-09-04'
name: WaveBL
nav: Providers
network: true
overview: 'WaveBL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electronic Bill of Lading, Digital Trade, Trade Documents, Trade Finance, and Ocean Freight.


  WaveBL''s developer surface includes engineering blog, support, signup flow, pricing, authentication, and 12 more developer resources.'
plans:
- name: Wavebl Plans Pricing
  plan_count: 4
  slug: wavebl-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Wavebl Rate Limits
  slug: wavebl-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Wavebl Authentication
  slug: wavebl-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wavebl Domain Security
  slug: wavebl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wavebl
tags:
- Electronic Bill of Lading
- Digital Trade
- Trade Documents
- Trade Finance
- Ocean Freight
- Shipping
- Logistics
- Supply Chain
- Maritime
- Customs
- Blockchain
- Freight Forwarding
- Banking
- Document Exchange
website: https://wavebl.com/
---
