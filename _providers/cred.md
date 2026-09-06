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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cred-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cred-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cred-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cred.club/
- group: company
  title: ''
  type: Engineering Blog
  url: https://engineering.cred.club/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CRED-CLUB
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cred-club
- group: company
  title: ''
  type: Careers
  url: https://careers.cred.club/
- group: company
  title: ''
  type: Partnerships
  url: https://cred.club/partner-with-us
- group: company
  title: ''
  type: Blog
  url: https://engineering.cred.club/feed
created: '2026-05-23'
description: CRED is an Indian consumer fintech that started with premium credit-card bill payments and rewards and has expanded into peer-to-peer payments (Scan & Pay, Tap to Pay, RuPay credit card on UPI), short-term credit (CRED Cash, CRED Mint), wealth (CRED Money), e-commerce (CRED Store), and travel. CRED's surface area is overwhelmingly consumer-app and the company does not publish a public, self-service developer portal. Its engineering organisation contributes to the broader ecosystem via the engineering.cred.club tech blog and open-source repositories under the CRED-CLUB GitHub org. B2B integrations (merchant acceptance, issuer partnerships, etc.) are negotiated directly with the partnerships team.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cred.png
layout: provider
modified: '2026-05-23'
name: CRED
nav: Providers
network: true
overview: 'CRED is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer Fintech, Credit Cards, Bill Payments, Rewards, and UPI.


  CRED''s developer surface includes GitHub presence, engineering blog, and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 24.0
    catalog_earned_first_party: 0.0
    catalog_gap: 91.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cred/refs/heads/main/screenshots/cred-2026-06-20T175222.png
security:
- kind: domain-security
  name: Cred Domain Security
  slug: cred-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cred Vulnerability Disclosure
  slug: cred-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cred Trust Center
  slug: cred-trust-center
  summary_line: ISO 27001, PCI DSS
slug: cred
tags:
- Consumer Fintech
- Credit Cards
- Bill Payments
- Rewards
- UPI
- Lending
- India
website: https://cred.club/
---
