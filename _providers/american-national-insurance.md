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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-national-insurance-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-national-insurance-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.americannational.com/home/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.americannational.com/home/legal/client-site---mobile-app-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.americannational.com/home/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.americannational.com/home/newsroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-national-insurance
- group: company
  title: ''
  type: Website
  url: https://www.americannational.com
coverage:
  checked: '2026-09-02'
  detail: American National ships customer-facing web and mobile apps but no developer program at all — /developers, /developer, /api-docs, /openapi.json, /swagger.json and /llms.txt are all hard 404s on www.americannational.com, its 280-URL sitemap contains no API or integration page, and the two IBM API Connect gateways found in the client-portal JavaScript bundle (api.americannational.com and apigw.americannational.com/american-national/prod) are private back ends that answer every path with an HTTP 500 SOAP fault rather than a published contract.
  evidence:
  - status: 404
    url: https://www.americannational.com/developers
  - status: 404
    url: https://www.americannational.com/openapi.json
  - status: 404
    url: https://www.americannational.com/llms.txt
  - status: 404
    url: https://www.americannational.com/.well-known/api-catalog
  - status: 500
    url: https://apigw.americannational.com/american-national/prod/openapi.json
  - status: 404
    url: https://apigw.americannational.com/american-national/prod/public/
  reason: no-developer-program
  state: none
created: '2024-11-15'
description: American National Insurance Company is a multi-line insurance holding company founded in 1905 and headquartered in Galveston, Texas. The company offers life insurance, annuities, pension risk transfer, health insurance, and property and casualty insurance through multiple subsidiary companies operating in all 50 states. American National holds A-level ratings from A.M. Best, Fitch, and S&P.
features:
- description: Term, whole life, and universal life insurance products through multiple American National subsidiary companies operating across all 50 states.
  name: Life Insurance
- description: Fixed, fixed indexed, and income annuity products providing retirement income solutions, guaranteed interest rates, and tax-deferred growth.
  name: Annuity Products
- description: Group annuity products allowing defined benefit pension plan sponsors to transfer pension obligations and longevity risk to American National.
  name: Pension Risk Transfer
- description: Supplemental health, Medicare supplement, and group health insurance products for individuals and employer groups.
  name: Health Insurance
- description: Farm, ranch, and business property and casualty insurance distributed through the Farm Family brand, covering agricultural and rural properties.
  name: Farm and Ranch Insurance
- description: Customer self-service portal for policy management, annuity fund access, claims tracking, and tax document retrieval.
  name: Online Account Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-national-insurance.png
integrations:
- description: Products distributed through independent life and health agents, financial advisors, and broker-dealers across all 50 states.
  name: Independent Agent Distribution Network
- description: Integration with pension actuaries, consultants, and plan sponsors for group annuity and pension risk transfer transactions.
  name: Pension Consultant Platforms
layout: provider
modified: '2026-09-02'
name: American National Insurance
nav: Providers
network: true
overview: 'American National Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Life Insurance, Annuities, Health Insurance, and Property Casualty.


  American National Insurance''s developer surface includes support, engineering blog, and 6 more developer resources.'
press:
- date: '2026-05-25'
  title: American National Insurance Company (ANICO) Data ...
  url: https://hackread.com/american-national-insurance-company-anico-moveit-breach/
- date: '2026-05-25'
  title: American National Insurance Company has been named ...
  url: https://www.facebook.com/AmericanNationalInsuranceCompany/posts/american-national-insurance-company-has-been-named-one-of-forbes-americas-best-i/1249475107202369/
- date: '2026-05-25'
  title: CAPE Analytics Announces Strategic Collaboration with ...
  url: https://www.webwire.com/ViewPressRel.asp?aId=300821
- date: '2026-05-25'
  title: American National Insurance Company
  url: https://www.reinsurancene.ws/tag/american-national-insurance-company/
- date: '2026-05-25'
  title: American National Insurance Company Experiences Data ...
  url: https://www.jdsupra.com/legalnews/american-national-insurance-company-3470457/
random_paper: 14
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: American National Insurance Domain Security
  slug: american-national-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-national-insurance
tags:
- Insurance
- Life Insurance
- Annuities
- Health Insurance
- Property Casualty
- Pension
- Financial-Services
- Fortune 1000
use_cases:
- description: Using annuity products to create guaranteed lifetime income streams for retirees and near-retirees concerned about outliving their assets.
  name: Retirement Income Planning
- description: Transferring defined benefit pension obligations from plan sponsors to American National through group annuity pension risk transfer products.
  name: Corporate Pension De-Risking
- description: Insuring farm and ranch operations, equipment, crops, and livestock through specialized property and casualty products under the Farm Family brand.
  name: Agricultural Business Protection
- description: Providing income replacement and estate planning solutions for families and business owners through life insurance products.
  name: Life Insurance Protection
website: https://www.americannational.com
---
