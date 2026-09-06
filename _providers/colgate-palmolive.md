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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/colgate-palmolive-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colpal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/colgate-palmolive
- group: company
  title: ''
  type: Website
  url: https://www.colgatepalmolive.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.colgatepalmolive.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.colgatepalmolive.com/en-us/sustainability
- group: company
  title: ''
  type: Website
  url: https://www.hillspet.com/
- group: company
  title: ''
  type: Careers
  url: https://jobs.colgate.com/
- group: company
  title: ''
  type: Partners
  url: https://www.colgatepalmolive.com/en-us/suppliers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.colgatepalmolive.com/en-us/legal-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.colgatepalmolive.com/en-us/legal-privacy-policy/terms-of-use
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/colgate-palmolive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/colgate-palmolive-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/colgate-palmolive-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/colgate-palmolive-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/colgate-palmolive-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/colgate-palmolive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/colgate-palmolive-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.colgatepalmolive.com/en-us/news
coverage:
  checked: '2026-09-05'
  detail: 'Colgate-Palmolive ships consumer products, not software: developer.colgatepalmolive.com and api.colgatepalmolive.com do not resolve at all, and no OpenAPI, GraphQL, AsyncAPI, .proto or WSDL exists on any of its seven public hosts or in its own verified GitHub org (github.com/colpal, 38 public repos, all internal CI tooling). Its real machine-to-machine footprint is retail EDI and supplier onboarding routed to third-party platforms (Taulia, Tungsten), which belong to those vendors rather than to Colgate-Palmolive.'
  evidence:
  - status: 0
    url: https://developer.colgatepalmolive.com/
  - status: 0
    url: https://api.colgatepalmolive.com/
  - status: 403
    url: https://www.colgatepalmolive.com/openapi.json
  - status: 403
    url: https://www.colgatepalmolive.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2025-03-21'
description: Colgate-Palmolive Company is a global consumer-products manufacturer operating in oral care, personal care, home care, and pet nutrition through brands such as Colgate, Palmolive, Hill's Pet Nutrition, Speed Stick, Ajax, and Softsoap. Colgate-Palmolive does not publish a general-purpose public developer REST API. Its B2B integration footprint is centered on EDI exchanges with retail trading partners (X12 messages, AS2, VAN), supplier integrations through SAP Ariba, and internal corporate systems. There is also a corporate sustainability and ESG reporting surface, but it is not exposed as a developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/colgate-palmolive.png
layout: provider
modified: '2026-09-05'
name: Colgate-Palmolive
nav: Providers
network: true
overview: 'Colgate-Palmolive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer Products, CPG, EDI, Home Care, and Oral Care.


  Colgate-Palmolive''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Colgate Palmolive Plans Pricing
  plan_count: 0
  slug: colgate-palmolive-plans-pricing
press:
- date: '2026-05-25'
  title: Leverages Artificial Intelligence
  url: https://www.colgatepalmolive.com/en-us/who-we-are/our-policies/artificial-intelligence-policy
- date: '2026-05-25'
  title: Colgate-Palmolive signs on to AI tool for biomaterials ...
  url: https://www.packagingdive.com/news/erthos-colgate-palmolive-zya-ai-platform-biomaterials-development/759412/
- date: '2026-05-25'
  title: How Colgate leverages AI and Big Data
  url: https://blackswan.com/resources/our-thinking/how-colgate-leverages-ai-and-big-data
- date: '2026-05-25'
  title: How Colgate-Palmolive's Hello amplifies marketing by gut- ...
  url: https://www.marketingdive.com/news/how-colgate-palmolives-hello-amplifies-marketing-by-gut-checking-ai/802878/
- date: '2026-05-25'
  title: Colgate - Harnessing AI for innovative oral care
  url: https://www.efp.org/publications-hub/colgate-harnessing-ai-for-innovative-oral-care-how-colgate-palmolive-is-taking-on-the-charge/
random_paper: 6
rate_limits:
- limit_count: 0
  name: Colgate Palmolive Rate Limits
  slug: colgate-palmolive-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 5.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/colgate-palmolive/refs/heads/main/screenshots/colgate-palmolive-2026-06-20T174744.png
security:
- kind: domain-security
  name: Colgate Palmolive Domain Security
  slug: colgate-palmolive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Colgate Palmolive Vulnerability Disclosure
  slug: colgate-palmolive-vulnerability-disclosure
  summary_line: contact published
slug: colgate-palmolive
tags:
- Consumer Products
- CPG
- EDI
- Home Care
- Oral Care
- Personal Care
- Pet Nutrition
- Retail
- Fortune 500
website: https://www.colgatepalmolive.com/
---
