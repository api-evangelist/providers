---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bayapay-sdn-bhd-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bayapay-sdn-bhd-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bayapay-sdn-bhd-llms.txt
- group: company
  title: ''
  type: Website
  url: https://bayapay.com
- group: operate
  title: ''
  type: Support
  url: https://www.bayapay.com/frequently-asked-questions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bayapay.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bayapay.com/privacypolicy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bayapay/
created: '2026-07-17'
description: BayaPay Sdn Bhd is a Malaysian fintech (incorporated 2021, registration 202101021154 / 1421454-H, based in Subang Jaya, Selangor) building programmable, permission-based business and vehicle expense management on an open-loop prepaid Mastercard. Its flagship BayaFuel FuelFleet programme gives fleet operators, SMBs, corporate teams and gig workers real-time spend controls, customizable limits, fraud deterrence and digitized expense tracking across fuel, travel and operational spend. The reloadable prepaid card is issued under license from Instapay Technologies Sdn Bhd (a Bank Negara Malaysia e-money issuer and Mastercard Asia/Pacific licensee), and BayaPay is one of the first Full Functional Open-Loop payment solutions in the APAC region. A 500 Global portfolio company. The public site is Wix-powered and exposes an agent-accessible llms.txt and a hosted Wix Site MCP endpoint; no bespoke BayaPay developer/payments API is publicly documented at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bayapay-sdn-bhd.png
layout: provider
mcp_servers:
- description: ''
  name: BayaPay Wix Site MCP
  slug: bayapay-wix-site-mcp
modified: '2026-07-18'
name: Bayapay Sdn Bhd
nav: Providers
network: true
overview: 'Bayapay Sdn Bhd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Prepaid Cards, and Expense Management.


  Bayapay Sdn Bhd''s developer surface includes support and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bayapay-sdn-bhd/refs/heads/main/screenshots/bayapay-sdn-bhd-2026-07-25T202442.png
security:
- kind: domain-security
  name: Bayapay Sdn Bhd Domain Security
  slug: bayapay-sdn-bhd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bayapay-sdn-bhd
tags:
- Company
- Payments
- Fintech
- Prepaid Cards
- Expense Management
- Fleet
- Mastercard
- Malaysia
- APAC
website: https://bayapay.com
---
