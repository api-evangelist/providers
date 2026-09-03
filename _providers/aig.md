---
access_model:
  confidence: medium
  label: Contract-only — credentials provisioned to appointed brokers and producers
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 20.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: AIG offers commercial and personal insurance products globally including property casualty, cyber insurance, casualty, professional liability, financial lines, specialty risk, and reinsurance. AIG ser
  name: AIG Insurance
  slug: aig
- description: 'AIG''s production API gateway for its commercial broker and producer applications, discovered from the publicly served runtime configuration of the AIG Producer Management Portal. The host is live and '
  name: AIG Commercial API Gateway
  slug: aig-commercial-api-gateway
artifact_total: 41
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aig-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aig-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aig.com/home/about/cyber-and-information-security/vulnerability-disclosure
- group: auth
  title: ''
  type: Authentication
  url: authentication/aig-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aig-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aig-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aig-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aig-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aig-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aig-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/aig-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aig-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aig-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aig-rate-limits.yml
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
  url: https://www.myaig.com
- group: start
  title: ''
  type: Portal
  url: https://www.producermanagementportal.aig.com
- group: start
  title: ''
  type: Portal
  url: https://www.aig.com/home/claims/intellirisk
- group: operate
  title: ''
  type: Support
  url: https://www.aig.com/home/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aig.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aig.com/terms-of-use
- group: commercial
  title: ''
  type: Legal
  url: https://www.aig.com/legal-notice
- group: start
  title: ''
  type: Portal
  url: https://www.aig.com/home/investor-relations
- group: start
  title: ''
  type: Portal
  url: https://www.aig.com/home/careers
- group: company
  title: ''
  type: Blog
  url: https://www.aig.com/home/newsroom/stories
created: '2025-02-17'
description: American International Group, Inc. (AIG) is a global insurance organization founded in 1919 and operating in over 200 countries and jurisdictions. AIG provides comprehensive risk solutions including property casualty, cyber, professional liability, casualty, specialty insurance, and reinsurance services for individuals and businesses. AIG runs a live, production API gateway at commercial.api.aig.com fronted by an Okta policy proxy, and its Okta identity host serves anonymous OpenID Connect and OAuth 2.0 authorization-server metadata, but AIG publishes no OpenAPI, no public API reference, no SDK and no self-service signup — API credentials are provisioned to appointed brokers, producers and clients through myAIG, the Producer Management Portal and distribution agreements. AIG's own developer portal host, www.developers.aig.com, is still indexed by search engines but refused TCP connections on ports 443 and 80 when probed in August 2026.
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
- description: Travel protection plans for trip cancellation, medical emergencies, and travel-related risks. Note that AIG's Travel Guard brand and travelguard.com now sit with Zurich; the site names American Zurich Insurance Company and Zurich American Insurance Company as underwriters and carries no AIG branding.
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
- description: AIG's customer identity platform; auth1.customerpltfm.aig.com issues the OAuth 2.0 / OpenID Connect tokens that the commercial API gateway requires.
  name: Okta
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
modified: '2026-08-30'
name: AIG
nav: Providers
network: true
overview: 'AIG publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Financial-Services, Property Casualty, Cyber Insurance, and Enterprise.


  The AIG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIG''s developer surface includes authentication, documentation, developer portal, support, legal docs, engineering blog, and 22 more developer resources.'
plans:
- name: Aig Plans Pricing
  plan_count: 0
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
random_paper: 11
rate_limits:
- limit_count: 0
  name: Aig Rate Limits
  slug: aig-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AIG API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aig-jsonschema-spectral-rules
scopes:
- name: Aig Scopes
  scope_count: 0
  slug: aig-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 24
    catalog_gap: 68.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.0
    contract_quality: 10.7
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 28.0
    operational_transparency: 10.5
  previous_composite: 33.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aig/refs/heads/main/screenshots/aig-2026-06-20T170849.png
security:
- kind: authentication
  name: Aig Authentication
  slug: aig-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Aig Domain Security
  slug: aig-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aig Vulnerability Disclosure
  slug: aig-vulnerability-disclosure
  summary_line: Hackerone
slug: aig
tags:
- Insurance
- Financial-Services
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
