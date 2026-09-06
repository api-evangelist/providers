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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ondeck-capital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ondeck.com/security-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ondeck-capital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ondeck.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ondeck.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.ondeck.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ondeck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ondeck.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ondeck-capital-llms.txt
created: '2026-07-17'
description: OnDeck Capital (ODK Capital, LLC) is one of the largest online small business lenders in the United States, providing term loans and business lines of credit to small and medium-sized businesses. Founded in 2007 and headquartered in New York, OnDeck uses data-driven underwriting and cash-flow analytics to deliver fast funding decisions, and has delivered more than $13 billion in financing to over 100,000 businesses across the U.S. OnDeck operates as a subsidiary of Enova International and also markets under the Headway Capital brand. It surfaced in the API Evangelist network as a portfolio company of IVP; OnDeck publishes a public marketing site and an llms.txt resource index but does not currently expose a public developer or partner API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ondeck-capital.png
layout: provider
modified: '2026-07-20'
name: OnDeck Capital
nav: Providers
network: true
overview: 'OnDeck Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Small Business, and Business Loans.


  OnDeck Capital''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.7
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ondeck-capital/refs/heads/main/screenshots/ondeck-capital-2026-08-07T190225.png
security:
- kind: domain-security
  name: Ondeck Capital Domain Security
  slug: ondeck-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ondeck Capital Vulnerability Disclosure
  slug: ondeck-capital-vulnerability-disclosure
  summary_line: Hackerone
slug: ondeck-capital
tags:
- Company
- Fintech
- Lending
- Small Business
- Business Loans
- Working Capital
- Financial-Services
website: https://www.ondeck.com/
---
