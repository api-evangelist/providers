---
access_model:
  confidence: medium
  label: Enterprise · Sales-led (gated)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.9
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Gated, enterprise real-time de-identification API named on the HealthVerity Identity Manager product page. Under the "sync on demand" modality, customers write records to the HealthVerity Identity API
  name: HealthVerity Identity API
  slug: healthverity-identity-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://healthverity.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.healthverity.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthverity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/healthverity
- group: operate
  title: ''
  type: Support
  url: https://healthverity.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthverity.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthverity.com/terms-and-conditions/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/healthverity-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/healthverity-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthverity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthverity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://healthverity.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: https://healthverity.com/trust/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthverity-llms.txt
- group: start
  title: ''
  type: Login
  url: https://marketplace.healthverity.com/
- group: start
  title: ''
  type: SignUp
  url: https://healthverity.com/exos-demo/
- group: build
  title: ''
  type: Packages
  url: packages/healthverity-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthverity-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthverity-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/healthverity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/healthverity-rate-limits.yml
coverage:
  checked: '2026-08-15'
  detail: The vendor-named HealthVerity Identity API has no reference anywhere on the public web - /api and /developers return 404, every api./docs./developer./ portal./platform. subdomain is NXDOMAIN, and the only route to it is the identity-manager-request sales form; the single live application host, marketplace.healthverity.com, 301s to /login/ and its robots.txt disallows all crawling.
  evidence:
  - status: 404
    url: https://healthverity.com/api
  - status: 200
    url: https://healthverity.com/identity-manager-request/
  - status: 301
    url: https://marketplace.healthverity.com/
  - status: 404
    url: https://healthverity.com/openapi.json
  - status: 404
    url: https://healthverity.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-24'
description: HealthVerity is a United States life-sciences data platform, headquartered in Philadelphia, Pennsylvania, that operates what it describes as the nation's largest real-world data (RWD) ecosystem - more than 150 billion de-identified transactions covering over 330 million U.S. patients across 75-plus data sources spanning medical and pharmacy claims, labs, and EHR (following its integration of Symphony Health). Its products are organized around the IPGE framework (Identity, Privacy, Governance, Exchange) and include HealthVerity Marketplace (verified RWD datasets), Identity Manager and Census (privacy-safe probabilistic identity resolution that replaces PII with a universal HealthVerity ID / HVID), Governance Manager, HealthVerity FLOW, and eXOs (an AI-native real-world-evidence agent). HealthVerity is a HIPAA-aligned, tokenization-and-de-identification company serving pharma, payers, and government - not a self-serve, standards-based clinical interoperability vendor. Unlike EHR
  and FHIR-network players, it exposes no public developer portal, no FHIR CapabilityStatement, and no downloadable OpenAPI; the only vendor-named programmatic surface is the gated, enterprise HealthVerity Identity API for real-time de-identification, described conceptually on the Identity Manager product page but without public reference documentation, base URL, or self-serve onboarding.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-15'
name: HealthVerity
nav: Providers
network: true
overview: 'HealthVerity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Life Sciences, Real-World Data, and Identity Resolution.


  HealthVerity''s developer surface includes engineering blog, support, signup flow, and 18 more developer resources.'
plans:
- name: Healthverity Plans Pricing
  plan_count: 0
  slug: healthverity-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 0
  name: Healthverity Rate Limits
  slug: healthverity-rate-limits
score:
  band: emerging
  composite: 22.6
  delta: 4.5
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthverity/refs/heads/main/screenshots/healthverity-2026-07-25T220843.png
security:
- kind: domain-security
  name: Healthverity Domain Security
  slug: healthverity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Healthverity Vulnerability Disclosure
  slug: healthverity-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Healthverity Trust Center
  slug: healthverity-trust-center
  summary_line: trust center published
slug: healthverity
tags:
- Healthcare
- United States
- Life Sciences
- Real-World Data
- Identity Resolution
- De-Identification
- Tokenization
- Data Marketplace
- HIPAA
- Claims
website: https://healthverity.com/
---
