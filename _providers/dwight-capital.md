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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dwight-capital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dwightcapital.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dwightcapital
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dwight-capital
- group: company
  title: ''
  type: About
  url: https://www.dwightcapital.com/about
- group: other
  title: ''
  type: Services
  url: https://www.dwightcapital.com/services
- group: other
  title: ''
  type: Team
  url: https://www.dwightcapital.com/team
- group: company
  title: ''
  type: News
  url: https://www.dwightcapital.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.dwightcapital.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.dwightcapital.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dwightcapital.com/privacy-policy
- group: start
  title: ''
  type: ServicingPortal
  url: https://www.dwightcapital.com/servicing-portal
- group: agent
  title: ''
  type: LlmsText
  url: https://dwightcapital.com/llms.txt
created: '2024-01-15'
description: Dwight Capital LLC is a leading commercial real estate finance company in the United States, with a loan servicing portfolio exceeding $15 billion across all affiliates. The firm originates Balance-Sheet Bridge and New Construction Loans, FHA/HUD Insured Loans, C-PACE Financing, Mezzanine Financing, and Preferred Equity for multifamily, healthcare, and mixed-use commercial real estate. Headquartered in New York City with an additional office in Sunny Isles Beach, Florida, Dwight is consistently ranked among the top FHA/HUD multifamily lenders in the country and operates as a privately held business specializing in bridge-to-HUD execution for commercial real estate sponsors.
features:
- description: Federally insured multifamily and healthcare loans under HUD programs including 223(f) acquisition/refinance, 221(d)(4) new construction and substantial rehabilitation, 223(a)(7) refinance, and 232 healthcare/seniors housing financing.
  name: FHA / HUD Insured Lending
- description: Short-term bridge financing with terms up to three years designed to position properties for a permanent FHA/HUD takeout. Borrowers receive time to stabilize operations and meet HUD underwriting requirements.
  name: Balance-Sheet Bridge Loans
- description: In-house construction lending program for multifamily and mixed-use properties, covering ground-up development of garden-style and mid-rise assets through substantial rehabilitation and adaptive reuse conversions.
  name: Balance-Sheet Construction Loans
- description: Commercial Property Assessed Clean Energy financing for energy efficiency, renewable energy, water conservation, and resiliency improvements on commercial real estate.
  name: C-PACE Financing
- description: Subordinate debt layered behind senior mortgages to bridge the gap between senior loan proceeds and the borrower's equity contribution on commercial real estate transactions.
  name: Mezzanine Financing
- description: Equity-style capital structured with priority distributions, used alongside senior debt to recapitalize, acquire, or develop multifamily and commercial properties.
  name: Preferred Equity
- description: Servicing portfolio exceeding $15 billion across all Dwight Capital affiliates, handling payment processing, escrow administration, draws, and asset management for HUD and balance-sheet loans.
  name: In-House Loan Servicing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dwight-capital.png
integrations:
- description: Approved Multifamily Accelerated Processing (MAP) and LEAN Section 232 lender, originating and underwriting loans directly with HUD field offices and the Office of Multifamily Housing.
  name: HUD MAP & LEAN Programs
- description: HUD-insured loans are pooled into Ginnie Mae mortgage-backed securities, providing the capital markets execution behind the firm's FHA/HUD origination volume.
  name: Ginnie Mae MBS
- description: Direct origination relationships with multifamily, healthcare, and mixed-use property sponsors across the United States.
  name: Commercial Real Estate Sponsors
layout: provider
modified: '2026-05-23'
name: Dwight Capital
nav: Providers
network: true
overview: 'Dwight Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Commercial Real Estate, Real Estate Finance, HUD Lending, FHA Lending, and Bridge Lending.


  Dwight Capital''s developer surface includes product news and 12 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 7.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dwight-capital/refs/heads/main/screenshots/dwight-capital-2026-06-20T180330.png
security:
- kind: domain-security
  name: Dwight Capital Domain Security
  slug: dwight-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: dwight-capital
tags:
- Commercial Real Estate
- Real Estate Finance
- HUD Lending
- FHA Lending
- Bridge Lending
- Multifamily
- Mortgage
- Financial Services
use_cases:
- description: HUD 223(f) insured loans for the acquisition or refinance of existing market-rate, affordable, and subsidized multifamily housing properties.
  name: Multifamily Acquisition Financing
- description: HUD 221(d)(4) financing for ground-up multifamily construction or substantial rehabilitation projects requiring long-term, non-recourse, fixed-rate debt.
  name: New Construction & Substantial Rehab
- description: HUD Section 232 loans for skilled nursing facilities, assisted living, and intermediate care properties.
  name: Seniors Housing & Healthcare
- description: Sponsors use Dwight's bridge loan to acquire or stabilize a property, then refinance into a permanent FHA/HUD insured loan once HUD underwriting criteria are met.
  name: Bridge-to-HUD Execution
- description: Combine senior HUD or bank debt with mezzanine, preferred equity, or C-PACE from Dwight to maximize proceeds and lower blended cost of capital.
  name: Capital Stack Optimization
website: https://www.dwightcapital.com/
---
