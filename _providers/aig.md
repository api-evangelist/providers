---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: AIG offers commercial and personal insurance products globally including property casualty, cyber insurance, casualty, professional liability, financial lines, specialty risk, and reinsurance. AIG ser
  name: AIG Insurance
  slug: aig
artifact_total: 36
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aig-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aig
- group: company
  title: ''
  type: Website
  url: https://www.aig.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.com/business
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.com/individual
- group: start
  title: ''
  type: Portal
  url: https://myaig.aig.com
- group: start
  title: ''
  type: Portal
  url: https://www.aig.com/business/insurance/workers-compensation/intellirisk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aig.com/about-us/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aig.com/about-us/terms-and-conditions
- group: start
  title: ''
  type: Portal
  url: https://www.aig.com/about-us/investors
- group: start
  title: ''
  type: Portal
  url: https://jobs.aig.com
- group: company
  title: ''
  type: Blog
  url: https://www.aig.com/home/newsroom/stories
created: '2025-02-17'
description: American International Group, Inc. (AIG) is a global insurance organization founded in 1919 and operating in over 200 countries and jurisdictions. AIG provides comprehensive risk solutions including property casualty, cyber, professional liability, casualty, specialty insurance, and reinsurance services for individuals and businesses. AIG operates digital portals for brokers and clients including myAIG for North America brokers and IntelliRisk Advanced for claims management, but does not currently offer a public developer API.
examples:
- key_count: 9
  name: Aig Cyber Risk Profile Example
  slug: aig-cyber-risk-profile-example
- key_count: 8
  name: Aig Insurance Claim Example
  slug: aig-insurance-claim-example
- key_count: 9
  name: Aig Insurance Policy Example
  slug: aig-insurance-policy-example
- key_count: 7
  name: Aig Risk Profile Example
  slug: aig-risk-profile-example
features:
- description: Property casualty, financial lines, specialty, and other commercial insurance in 200+ countries.
  name: Global Commercial Insurance
- description: Cyber risk solutions protecting organizations from data breaches, ransomware, and cyber liability.
  name: Cyber Insurance
- description: Directors and Officers (D&O), Errors and Omissions (E&O), and employment practices liability.
  name: Professional Liability
- description: Coordinated global insurance programs for multinational corporations with local and global coverage.
  name: Multinational Insurance Programs
- description: Global claims expertise with IntelliRisk Advanced platform for self-administered claims programs.
  name: Claims Management
- description: Broker portal providing online access to policy information, endorsements, and certificates.
  name: myAIG Digital Portal
- description: High-value personal insurance for homes, autos, collections, and liability for wealthy individuals.
  name: Private Client Group
- description: Travel protection plans for trip cancellation, medical emergencies, and travel-related risks.
  name: Travel Insurance
finops:
- name: Aig Finops
  service_category: Insurance
  slug: aig-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aig.png
integrations:
- description: Integration with broker platforms for quoting, binding, and policy management via myAIG portal.
  name: Broker Management Systems
- description: Data feeds and integrations with RMIS platforms for risk data management.
  name: Risk Management Information Systems
- description: Partnership with Anthropic to implement AI for insurance operations and underwriting enhancement.
  name: Anthropic AI
- description: Enterprise resource planning integration for certificate management and compliance tracking.
  name: ERP Integration
json_schemas:
- name: CyberRiskProfile
  property_count: 9
  slug: aig-cyber-risk-profile
- name: InsuranceClaim
  property_count: 8
  slug: aig-insurance-claim
- name: InsurancePolicy
  property_count: 9
  slug: aig-insurance-policy
- name: RiskProfile
  property_count: 7
  slug: aig-risk-profile
json_structures:
- name: Aig Cyber Risk Profile Structure
  property_count: 9
  slug: aig-cyber-risk-profile-structure
- name: Aig Insurance Claim Structure
  property_count: 8
  slug: aig-insurance-claim-structure
- name: Aig Insurance Policy Structure
  property_count: 9
  slug: aig-insurance-policy-structure
- name: Aig Risk Profile Structure
  property_count: 7
  slug: aig-risk-profile-structure
jsonld:
- class_count: 4
  name: Aig Context
  property_count: 17
  slug: aig-context
layout: provider
modified: '2026-04-19'
name: AIG
nav: Providers
network: true
overview: 'AIG publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial Services, Property Casualty, Cyber Insurance, and Enterprise.


  The AIG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIG''s developer surface includes documentation, developer portal, engineering blog, and 9 more developer resources.'
plans:
- name: Aig Plans Pricing
  plan_count: 1
  slug: aig-plans-pricing
press:
- date: '2026-05-25'
  title: Q4 2025 Earnings Release
  url: https://www.aig.com/content/dam/aig/america-canada/us/documents/investor-relations/earnings-result/aig-reports-4q25-results.pdf
- date: '2026-05-25'
  title: 'AIG''s Zaffino: Outcomes From AI Use Went From '' ...'
  url: https://www.insurancejournal.com/news/national/2026/02/13/858033.htm
- date: '2026-05-25'
  title: AIG set to report earnings as AI bets face profitability test
  url: https://www.investing.com/news/earnings/aig-set-to-report-earnings-as-ai-bets-face-profitability-test-93CH-4650425
- date: '2026-05-25'
  title: AIG leans on generative AI to speed underwriting
  url: https://www.ciodive.com/news/aig-insurance-agentic-generative-ai-underwriting/732183/
- date: '2026-05-25'
  title: AIG Investor Day 2025
  url: https://www.aig.com/home/investor-relations/aig-investor-day-2025
random_paper: 73
rate_limits:
- limit_count: 1
  name: Aig Rate Limits
  slug: aig-rate-limits
rules:
- name: AIG API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aig-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 32.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aig/refs/heads/main/screenshots/aig-2026-06-20T170849.png
security:
- kind: domain-security
  name: Aig Domain Security
  slug: aig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aig
tags:
- Insurance
- Financial Services
- Property Casualty
- Cyber Insurance
- Enterprise
- Fortune 100
use_cases:
- description: Comprehensive risk transfer solutions for large corporations across property, liability, and specialty lines.
  name: Enterprise Risk Management
- description: Protect businesses from financial losses due to cyber incidents, data breaches, and regulatory fines.
  name: Cyber Risk Transfer
- description: Coordinate insurance coverage for global operations with consistent terms across jurisdictions.
  name: Multinational Program Administration
- description: Bankers blanket bond, fidelity, professional liability, and other coverages for financial institutions.
  name: Financial Institution Risk
- description: Contractor liability, builders risk, and environmental coverages for construction projects.
  name: Construction and Infrastructure
website: https://www.aig.com
---
