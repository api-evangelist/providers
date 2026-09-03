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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aig
- group: company
  title: ''
  type: Website
  url: https://www.aig.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/american-international-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/american-international-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/american-international-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/american-international-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/american-international-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/american-international-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/american-international-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/american-international-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-international-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/american-international-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-international-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/american-international-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aig.com/home/about/cyber-and-information-security/vulnerability-disclosure
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
- group: company
  title: ''
  type: Blog
  url: https://www.aig.com/home/newsroom/stories
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aig.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aig.com/terms-of-use
created: '2024-11-15'
description: American International Group (AIG) is one of the world's most extensive international insurance organizations, operating in more than 200 countries and jurisdictions. AIG provides a broad range of property casualty insurance, life insurance, retirement solutions, and other financial services to commercial and individual customers worldwide. The company's offerings include casualty, property, cyber, professional liability, management liability, marine, aviation, energy, trade credit, and private client insurance. AIG runs a live production API gateway at commercial.api.aig.com behind an Okta "Protect Proxy" policy, and its customer identity host auth1.customerpltfm.aig.com serves anonymous OpenID Connect and OAuth 2.0 authorization-server metadata. AIG publishes no OpenAPI, no public API reference, no SDK and no self-service signup — API credentials are provisioned to appointed brokers, producers and clients through myAIG and the Producer Management Portal. AIG's own developer
  portal host, developers.aig.com, is still indexed by search engines but refused TCP connections when probed on 2026-09-02.
features:
- description: Comprehensive commercial insurance including excess casualty, foreign casualty, primary coverage, commercial property, and builders risk for global businesses.
  name: Commercial Property and Casualty Insurance
- description: Cyber liability coverage protecting businesses from data breaches, ransomware, business interruption, and regulatory penalties across global operations.
  name: Cyber Insurance
- description: Directors and officers liability, employment practices liability, errors and omissions, and fiduciary liability for corporate clients worldwide.
  name: Management and Professional Liability
- description: Ocean cargo, inland marine, marine liability, aviation hull, and aviation liability coverage for transportation and logistics industries.
  name: Marine and Aviation Insurance
- description: Insurance protecting businesses from commercial payment defaults and political risks in domestic and cross-border trade transactions.
  name: Trade Credit and Political Risk
- description: Digital client portal enabling claims filing, risk data access, loss reporting, and risk management analytics across 100+ countries.
  name: IntelliRisk Advanced Platform
- description: High-net-worth individual insurance including homes, autos, art, jewelry, and personal liability through AIG's Private Client Group.
  name: Private Client Insurance
- description: Multinational insurance programs and network solutions coordinating coverage for corporations operating across multiple international jurisdictions.
  name: Global Network Insurance
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-international.png
integrations:
- description: Integration with insurance broker platforms and agent management systems for policy quoting, binding, and servicing across AIG's commercial lines.
  name: Broker and Agent Management Systems
- description: Digital portal integrating with client risk management systems for claims reporting, loss data analysis, and risk control services globally.
  name: IntelliRisk Client Portal
- description: Integration with reinsurance markets and treaty reinsurers to manage AIG's risk retention and cession across global insurance programs.
  name: Reinsurance Platforms
layout: provider
modified: '2026-09-02'
name: American International Group (AIG)
nav: Providers
network: true
overview: 'American International Group (AIG) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Property Casualty, Cyber Insurance, Commercial Insurance, and Global Insurance.


  American International Group (AIG)''s developer surface includes authentication, documentation, developer portal, support, engineering blog, and 20 more developer resources.'
plans:
- name: American International Plans Pricing
  plan_count: 0
  slug: american-international-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: American International Rate Limits
  slug: american-international-rate-limits
scopes:
- name: American International Scopes
  scope_count: 0
  slug: american-international-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 27.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-international/refs/heads/main/screenshots/american-international-2026-06-20T171919.png
security:
- kind: authentication
  name: American International Authentication
  slug: american-international-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: American International Domain Security
  slug: american-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: American International Vulnerability Disclosure
  slug: american-international-vulnerability-disclosure
  summary_line: Hackerone
slug: american-international
tags:
- Insurance
- Property Casualty
- Cyber Insurance
- Commercial Insurance
- Global Insurance
- Financial-Services
- Reinsurance
- Fortune 500
use_cases:
- description: Coordinating insurance programs for corporations with operations in multiple countries, ensuring consistent coverage under local regulatory requirements.
  name: Multinational Corporate Risk Management
- description: Transferring enterprise cyber risk through comprehensive cyber liability policies covering first-party losses and third-party liability.
  name: Cyber Risk Transfer
- description: Protecting executives and corporate boards from personal liability through directors and officers, fiduciary, and employment practices liability coverage.
  name: Executive and Corporate Governance Protection
- description: Protecting banks, exporters, and buyers from payment default and political risks in international trade transactions.
  name: International Trade Finance
- description: Providing specialized coverage for high-value homes, vehicles, art collections, jewelry, and personal liability for affluent individuals.
  name: High-Net-Worth Personal Lines
website: https://www.aig.com
---
