---
access_model:
  confidence: low
  label: Partner-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - developer-portal
  - documentation
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
api_count: 4
apis:
- description: ProtectBuy is Discover Global Network's EMV 3-D Secure (3DS) cardholder authentication service. Built on the EMVCo 3-D Secure protocol, it lets merchants, acquirers, and 3DS servers authenticate Disco
  name: Discover ProtectBuy 3-D Secure API
  slug: protectbuy-3ds
- description: Discover's Secure Remote Commerce (SRC) implementation powers Click to Pay, the EMVCo standard for a streamlined, tokenized online checkout across participating card networks. The SRC developer progra
  name: Discover Secure Remote Commerce (Click to Pay) API
  slug: secure-remote-commerce
- description: 'Stored Token Services is Discover Global Network''s payment tokenization service. It replaces sensitive card account numbers with network tokens for card-on-file, digital-wallet, and recurring-payment '
  name: Discover Stored Token Services API
  slug: stored-token-services
- description: Discover Deliver is Discover Global Network's push-payments (Original Credit Transaction) service, enabling the quick, convenient, and secure transfer of funds directly to eligible Discover, Diners Cl
  name: Discover Deliver Push Payments API
  slug: discover-deliver-push-payments
artifact_total: 6
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.discover.com/terms-of-use
- group: start
  title: ''
  type: Signup
  url: https://www.discover.com/register-account/?ICMPGN=SA_LOGIN_OVERLAY_REGISTER
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/discover-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/discover-financial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discover-financial-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/discover-financial-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/discover-financial-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/discoverfinancial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/discover-financial-services
- group: company
  title: ''
  type: Website
  url: https://www.discover.com/
- group: other
  title: ''
  type: Corporate
  url: https://www.discover-financial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.discover.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://partner.discoverglobalnetwork.com/
- group: other
  title: ''
  type: Network
  url: https://www.discoverglobalnetwork.com/
- group: company
  title: ''
  type: Blog
  url: https://technology.discover.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investorrelations.discover.com/
- group: commercial
  title: ''
  type: Legal
  url: https://www.discover.com/company/our-company/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discover.com/privacy-statements/
created: '2026-03-21'
description: Discover Financial Services is a US direct bank and payments company that owns the Discover Network, the PULSE debit network, and Diners Club International. Its Discover Global Network (DGN) developer program exposes a partner-gated developer center with interactive OpenAPI documentation for card-network products — EMV 3-D Secure (ProtectBuy), Secure Remote Commerce / Click to Pay, Stored Token Services (tokenization), and Discover Deliver push payments. Consumer account-data access is delivered through open-finance aggregators (Plaid, Finicity) rather than a first-party retail-banking API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/discover-financial.png
layout: provider
modified: '2026-07-23'
name: Discover Financial Services
nav: Providers
network: true
overview: 'Discover Financial Services publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Cards, Financial Services, Fortune 500, and Open Banking.


  Discover Financial Services'' developer surface includes signup flow, engineering blog, legal docs, and 15 more developer resources.'
press:
- date: '2026-05-25'
  title: Artificial intelligence press releases
  url: https://newsroom.ibm.com/press-releases-artificial-intelligence?l=100&o=200
- date: '2026-05-25'
  title: Discover Financial Services - Latest News
  url: https://www.americanbanker.com/organization/discover-financial-services
- date: '2026-05-25'
  title: Discover Financial Services Deploys Google Cloud's ...
  url: https://investorrelations.discover.com/newsroom/press-releases/press-release-details/2024/Discover-Financial-Services-Deploys-Google-Clouds-Generative-AI-to-Transform-Customer-Service/default.aspx
- date: '2026-05-25'
  title: Discover Partners with ZestFinance to Implement AI-Based ...
  url: https://investorrelations.discover.com/newsroom/press-releases/press-release-details/2019/Discover-Partners-with-ZestFinance-to-Implement-AI-Based-Underwriting-Platform/default.aspx
- date: '2026-05-25'
  title: Discover Financial Services Builds a Generative AI ...
  url: https://aws.amazon.com/solutions/case-studies/discover-financial-services-generative-ai/
random_paper: 41
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 21.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/discover-financial/refs/heads/main/screenshots/discover-financial-2026-06-20T180040.png
security:
- kind: domain-security
  name: Discover Financial Domain Security
  slug: discover-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Discover Financial Vulnerability Disclosure
  slug: discover-financial-vulnerability-disclosure
  summary_line: Hackerone
slug: discover-financial
tags:
- Banking
- Cards
- Financial Services
- Fortune 500
- Open Banking
- Payments
- United States
- Card Network
- 3-D Secure
- Tokenization
website: https://www.discover.com/
---
