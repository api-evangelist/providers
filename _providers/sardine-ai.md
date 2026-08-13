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
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: Submit customer profile and onboarding signals (KYC, KYB, document verification, sanctions/PEP screening, identity fraud, synthetic ID detection, behavioral biometrics, device intelligence) and receiv
  name: Sardine Customer API
  slug: sardine-customer-api
- description: 'Capture device, network, and behavioral signals from web, iOS, and Android SDKs and resolve them to a Sardine device session for downstream scoring. Powers account takeover protection, bot detection, '
  name: Sardine Device Intelligence API
  slug: sardine-device-api
- description: Submit payment, ACH, wire, card, and crypto transactions for real-time fraud scoring and AML transaction monitoring. Backs Sardine's card chargeback guarantee program and ACH indemnification for unaut
  name: Sardine Transaction API
  slug: sardine-transaction-api
- description: Real-time card authorization fraud scoring for card issuers. Returns an approve/decline/step-up recommendation on each authorization event using Sardine's issuer-specific ML models and configurable ru
  name: Sardine Issuing API
  slug: sardine-issuing-api
- description: Crypto-specific risk and compliance APIs covering wallet screening, on-chain attribution, and Travel Rule messaging for VASPs (Virtual Asset Service Providers). Tracked as Crypto APIs and Crypto Web o
  name: Sardine Crypto API
  slug: sardine-crypto-api
- description: Programmatic access to Sardine's unified case management surface for fraud and AML investigations. Cases are routed through Sardine's "atomic agents" — OSINT search, data analysis, transaction monitor
  name: Sardine Case Management API
  slug: sardine-case-management-api
artifact_total: 32
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sardine-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sardine-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sardine-ai-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.sardine.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/home
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sardine.ai/guides/public/getting-started/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/getting-started/apiaccess
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/getting-started/integration-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/getting-started/what-powers-sardine
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/getting-started/how-sardine-bills
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/getting-started/common-risk-problems
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/account-risk/account-risk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/account-risk/account-takeover
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/account-risk/kyb
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/business-risk/about-business-risk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/card-spending-risk/card-spending
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/funding-risk/funding-risk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/funding-risk/ach-indemnification
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/funding-risk/card-indemnification
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sardine.ai/guides/public/risk/transaction-monitoring/transaction-monitoring
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sardine.ai
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.sardine.ai
- group: operate
  title: ''
  type: Support
  url: https://www.sardine.ai/contact
- group: operate
  title: ''
  type: Support
  url: mailto:risksupport@sardine.ai
- group: company
  title: ''
  type: AboutUs
  url: https://www.sardine.ai/about
- group: other
  title: ''
  type: CustomerCaseStudies
  url: https://www.sardine.ai/customers
- group: company
  title: ''
  type: Blog
  url: https://www.sardine.ai/blog
- group: company
  title: ''
  type: Careers
  url: https://www.sardine.ai/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sardine-ai
- group: company
  title: ''
  type: Twitter
  url: https://x.com/sardine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sardine-ai
- group: build
  title: ''
  type: Tools
  url: https://github.com/sardine-ai/openapi-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/sardine-ai/mcp-server-manager
- group: build
  title: ''
  type: Tools
  url: https://github.com/sardine-ai/chronon
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/sardine-ai/mintlify-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sardine.ai/pricing
created: '2026-05-25T00:00:00.000Z'
description: Sardine is a San Francisco-based fraud prevention, AML compliance, and risk management platform for fintechs, banks, marketplaces, and crypto VASPs. It unifies onboarding (KYC, KYB, document and bank verification), device intelligence and behavioral biometrics, payment and card fraud scoring, AML transaction monitoring, sanctions screening, and case management into a single risk operating system. Sardine's "agentic" layer applies atomic agents (OSINT, data analysis, transaction monitoring, business due diligence, sanctions screening) to compress investigation time from days to minutes, while Sonar provides cross-industry fraud intelligence across the consortium. The platform serves 400+ enterprise customers including FIS, GoDaddy, Intuit, Nubank, Novo, and bunq, has screened $1.3T+ in payments, and profiled 5.4B+ devices. Sardine has raised ~$170M from Andreessen Horowitz, Visa, Experian, Google Ventures, FIS, and others. Public docs cover the risk landscape and integration
  overview; full API reference, SDKs, and sandbox access are gated and require a Sardine account.
features:
- Agentic AML Ops — atomic agents for OSINT, data analysis, business due diligence, and sanctions screening compress investigations from days to minutes
- Agentic Fraud Ops — agent-assisted review of fraud alerts with audit-ready outputs
- Global KYC and Global KYB onboarding with sanctions and PEP screening
- Identity Verification including document verification, synthetic ID detection, and deepfake detection
- Device Intelligence and Behavioral Biometrics SDKs for web, iOS, and Android (5.4B+ devices profiled)
- Real-time payment fraud detection across card, ACH, wire, and crypto rails ($1.3T+ payments screened)
- Card Chargeback Guarantee Program with liability protection on covered transactions
- ACH Indemnification covering unauthorized returns (R05, R07, R10, R11, R29)
- Issued Card Fraud protection with real-time authorization scoring for card issuers
- Transaction Monitoring for AML compliance with behavioral profiling and customer risk rating
- Sanctions Screening and Customer Risk Rating
- Case Management with unified queues across fraud, AML, credit, and operations
- Sonar — cross-industry fraud intelligence consortium
- Connection Graph for relationship and ring-detection across customers, devices, and accounts
- Rules Engine plus ML models with configurable scoring per use case
- Bot Detection, Account Takeover Protection, Policy Abuse Prevention, Refund Fraud Detection
- Job Applicant Fraud Detection
- Sponsor Banking Risk Management for BaaS sponsor banks
- Credit Underwriting tools and bank/cash flow verification
- Crypto compliance APIs including wallet screening and Travel Rule
- 400+ enterprise customers including FIS, GoDaddy, Intuit, Nubank, Coastal, Experian, Kalshi, Ascensus, Gusto, Deel, Novo, bunq, Prezzee, Raise, SeatGeek, ZoomInfo, LHV, Whop, First Federal Bank of Kansas City
- Investors include Andreessen Horowitz, Visa, Experian, Google Ventures, FIS, Activant Capital, Moody's Analytics, Geodesic Capital, Nyca Partners, Cross Creek Advisors, XYZ Venture Capital, NA Ventures (~$170M total raised)
- 4.9/5 G2 rating
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sardine-ai.png
layout: provider
modified: '2026-05-25'
name: Sardine
nav: Providers
network: true
overview: 'Sardine publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Prevention, AML, Compliance, KYC, and KYB.


  Sardine''s developer surface includes developer portal, documentation, getting-started guide, support, engineering blog, tooling, pricing, and 32 more developer resources.'
random_paper: 29
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sardine-ai/refs/heads/main/screenshots/sardine-ai-2026-06-20T193433.png
security:
- kind: domain-security
  name: Sardine Ai Domain Security
  slug: sardine-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sardine Ai Vulnerability Disclosure
  slug: sardine-ai-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Sardine Ai Trust Center
  slug: sardine-ai-trust-center
  summary_line: SOC 2
slug: sardine-ai
tags:
- Fraud Prevention
- AML
- Compliance
- KYC
- KYB
- Identity Verification
- Transaction Monitoring
- Device Intelligence
- Behavioral Biometrics
- Risk
- Financial Crime
- Agentic AI
- Fintech
website: https://www.sardine.ai
---
