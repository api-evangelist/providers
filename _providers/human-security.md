---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Bot Defender (formerly PerimeterX Bot Defender) is HUMAN's flagship product for stopping automated traffic against web and mobile properties. A JavaScript sensor and mobile SDKs collect signals from t
  name: HUMAN Bot Defender
  slug: bot-defender
- description: Account Defender protects against account takeover, fake account creation, and post-login abuse by scoring login, signup, and session events with behavioral, device, and credential-intel signals. It i
  name: HUMAN Account Defender
  slug: account-defender
- description: Code Defender is HUMAN's client-side security product, providing runtime visibility and controls for third-party scripts, supply-chain attacks (Magecart, formjacking), and unauthorized data exfiltrati
  name: HUMAN Code Defender
  slug: code-defender
- description: Transaction Abuse Defense extends HUMAN's signals into checkout, payment, and high-value transaction flows to detect carding, payment abuse, gift-card cracking, and similar automated attacks that surv
  name: HUMAN Transaction Abuse Defense
  slug: transaction-abuse-defense
- description: Scraper Protection targets large-scale content scraping by automated agents, including LLM training scrapers and competitive intelligence bots, layering signals from the JS sensor with edge enforcemen
  name: HUMAN Scraper Protection
  slug: scraper-protection
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/human-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/human-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.humansecurity.com/
- group: other
  title: ''
  type: Products
  url: https://www.humansecurity.com/products/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humansecurity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.humansecurity.com/learn/blog/
- group: other
  title: ''
  type: ThreatIntelligence
  url: https://www.humansecurity.com/learn/satori-threat-intelligence-and-research/
- group: company
  title: ''
  type: Careers
  url: https://www.humansecurity.com/company/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humansecurity/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HUMANSecurityIQ
- group: operate
  title: ''
  type: Contact
  url: https://www.humansecurity.com/contact/
- group: company
  title: ''
  type: News
  url: https://www.humansecurity.com/products/mediaguard/
created: '2026-05-23'
description: 'HUMAN Security (formerly PerimeterX) is an application security company focused on stopping automated abuse: sophisticated bots, account takeover, fake account creation, scraping, ad fraud, client-side supply-chain attacks, and transaction fraud. HUMAN operates the Human Defense Platform, which combines a JavaScript sensor and mobile SDKs running on the client with risk decisioning services on the server side. Products in the platform include Bot Defender (formerly PerimeterX Bot Defender), Account Defender, Credential Intelligence, Transaction Abuse Defense, Ad Fraud Sensor / MediaGuard, Code Defender (client-side script and supply-chain protection), and Scraper Protection. HUMAN is primarily an enterprise vendor — onboarding, sensor configuration, and policy tuning go through the HUMAN portal and a customer success team — but the platform exposes REST APIs and SDKs that engineering teams integrate into web apps, mobile apps, edge workers, and back-end services.'
finops:
- name: Human Security Finops
  service_category: API
  slug: human-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/human-security.png
layout: provider
modified: '2026-07-25'
name: HUMAN Security
nav: Providers
network: true
overview: 'HUMAN Security publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bot Mitigation, Account Takeover, Ad Fraud, Client-Side Security, and Application Security.


  HUMAN Security''s developer surface includes documentation, engineering blog, product news, and 10 more developer resources.'
plans:
- name: Human Security Plans Pricing
  plan_count: 1
  slug: human-security-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Human Security Rate Limits
  slug: human-security-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/human-security/refs/heads/main/screenshots/human-security-2026-06-20T182929.png
security:
- kind: domain-security
  name: Human Security Domain Security
  slug: human-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Human Security Vulnerability Disclosure
  slug: human-security-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Human Security Trust Center
  slug: human-security-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: human-security
tags:
- Bot Mitigation
- Account Takeover
- Ad Fraud
- Client-Side Security
- Application Security
- Fraud
- Bot Defender
- PerimeterX
- JavaScript Sensor
- Edge Security
website: https://www.humansecurity.com/
---
