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
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-family-insurance-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-family-insurance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amfam.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amfam.com/privacy-security
- group: operate
  title: ''
  type: Support
  url: https://www.amfam.com/contact
- group: start
  title: ''
  type: Login
  url: https://myaccount.amfam.com/login
- group: company
  title: ''
  type: Blog
  url: https://newsroom.amfam.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://newsroom.amfam.com/feed/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-family-insurance-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/american-family-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-family-insurance-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.amfam.com
- group: start
  title: ''
  type: PartnerPortal
  url: https://b2b.amfam.com/lender
coverage:
  checked: '2026-09-02'
  detail: American Family Insurance runs no developer program of any kind — developer.amfam.com, developers.amfam.com and apis.amfam.com do not resolve, the amfamlabs GitHub org has zero public repositories, and the only non-consumer surface is b2b.amfam.com/lender, a SiteMinder login for mortgage servicers with no API behind it.
  evidence:
  - detail: HTML single-page-app shell, not a spec — www.amfam.com answers 200 with the same 143KB shell for every unknown path
    status: 200
    url: https://www.amfam.com/openapi.json
  - status: 404
    url: https://b2b.amfam.com/openapi.json
  - status: 404
    url: https://b2b.amfam.com/.well-known/agent-card.json
  - detail: organization exists with public_repos 0
    status: 200
    url: https://api.github.com/orgs/amfamlabs
  - detail: host resolves (165.200.238.15) and accepts TCP but returned nothing within a 10s ceiling; one attempt, not retried
    status: <no response>
    url: https://api.amfam.com/openapi.json
  reason: no-developer-program
  state: none
created: '2024-11-15'
description: American Family Insurance is a private mutual company that offers auto, homeowners, life, renters, umbrella, business, and farm/ranch insurance throughout the United States. The company serves customers through a network of exclusive agents, digital tools including the MyAmFam mobile app, and online self-service capabilities. American Family is headquartered in Madison, Wisconsin, and is one of the largest property-casualty insurers in the country.
features:
- description: Customizable auto insurance coverage including liability, collision, comprehensive, uninsured motorist, and roadside assistance for personal and commercial vehicles.
  name: Auto Insurance
- description: Homeowners insurance protecting against property damage, personal liability, and loss of use, with optional coverage for valuables and natural disasters.
  name: Home Insurance
- description: Term, whole, and universal life insurance products providing financial protection and wealth accumulation options for families and individuals.
  name: Life Insurance
- description: Small business and commercial insurance covering property, liability, workers compensation, and professional liability for business owners.
  name: Business Insurance
- description: Discount programs allowing customers to save up to 40% by bundling home and auto insurance policies together.
  name: Multi-Policy Bundling
- description: Mobile app with 4.7-star rating enabling policy management, claims filing, bill payment, digital ID cards, and agent communication for customers.
  name: MyAmFam Digital App
- description: Digital claims filing and tracking tools allowing customers to report claims, upload documentation, and monitor claim status online and via mobile app.
  name: Online Claims Management
- description: B2B portal for mortgage lenders and financial institutions to verify insurance coverage, manage escrow billing, and coordinate insurance requirements.
  name: Lender Services Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-family-insurance.png
integrations:
- description: B2B integration with mortgage servicers and lenders for insurance verification, escrow billing, and lender-placed insurance coordination.
  name: Mortgage Lender Systems
- description: Integration with exclusive agent tools for policy quoting, binding, and customer management across all lines of business.
  name: Agent Management Platforms
layout: provider
modified: '2026-09-02'
name: American Family Insurance
nav: Providers
network: true
overview: 'American Family Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Auto Insurance, Home Insurance, Life Insurance, and Property Casualty.


  American Family Insurance''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: American Family Insurance Plans Pricing
  plan_count: 0
  slug: american-family-insurance-plans-pricing
press:
- date: '2026-05-25'
  title: Creative Destruction Lab announces a new program ...
  url: https://creativedestructionlab.com/blog/cdl-announces-a-new-program-focused-on-transforming-societys-ability-to-manage-risk/
- date: '2026-05-25'
  title: Artificial Intelligence at American Family Insurance Group
  url: https://emerj.com/artificial-intelligence-at-american-family-insurance-group/
- date: '2026-05-25'
  title: American Family Insurance streamlines claims operations ...
  url: https://www.prnewswire.com/news-releases/american-family-insurance-streamlines-claims-operations-with-tractables-ai-301585429.html
- date: '2026-05-25'
  title: Seeding tech growth in Wisconsin's fertile ground
  url: https://madisonbiz.com/uw-madison-american-family-insurance-seeding-tech-growth-in-wisconsins-fertile-ground/
- date: '2026-05-25'
  title: American Family Insurance and AWS Team Up to Drive ...
  url: https://www.businesswire.com/news/home/20221201005413/en/American-Family-Insurance-and-AWS-Team-Up-to-Drive-Innovation-in-the-Insurance-Industry
random_paper: 12
rate_limits:
- limit_count: 0
  name: American Family Insurance Rate Limits
  slug: american-family-insurance-rate-limits
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-family-insurance/refs/heads/main/screenshots/american-family-insurance-2026-06-20T171911.png
security:
- kind: domain-security
  name: American Family Insurance Domain Security
  slug: american-family-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-family-insurance
tags:
- Insurance
- Auto Insurance
- Home Insurance
- Life Insurance
- Property Casualty
- Financial-Services
- Fortune 500
use_cases:
- description: Protecting personal vehicles and homes from accidents, theft, weather damage, and liability claims through bundled personal lines insurance policies.
  name: Personal Auto and Home Protection
- description: Covering small business operations against property damage, general liability, professional liability, and workers compensation claims.
  name: Small Business Coverage
- description: Providing financial security for families through life insurance products that replace income and cover expenses in the event of the policyholder's death.
  name: Life Insurance Planning
- description: Enabling mortgage lenders to verify homeowners insurance coverage requirements are met and manage escrow-based insurance premium payments.
  name: Mortgage Lender Insurance Verification
- description: Allowing customers to manage their entire insurance relationship digitally through the MyAmFam app and online portal without requiring agent interaction.
  name: Digital Self-Service
website: https://www.amfam.com
---
