---
access_model:
  confidence: high
  label: Contract only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/transunion-plans-pricing.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The STIR/SHAKEN call Authentication Service and Verification Service behind TransUnion TruContact Branded Communications. Nine POST operations sign SIP Identity headers (PASSporTs) and verify them, wi
  name: TransUnion TruContact Trusted Call Solutions (STI-AS / STI-VS)
  slug: trucontact-trusted-call-solutions
- description: TransUnion's API products for credit reporting, identity verification, fraud prevention and consumer risk decisioning. Access requires a business agreement with TransUnion and credentials issued by an
  name: TransUnion Global Developer Portal
  slug: global-developer-portal
- description: Device recognition and fraud signals, formerly iovation FraudForce. Mobile SDKs collect a device "blackbox" that is submitted to a risk check from your servers. The API host api.iovation.com is behind
  name: TransUnion TruValidate Device Risk
  slug: truvalidate-device-risk
artifact_total: 10
collections:
- collection_type: open
  name: 3GPP-based Call Authentication APIs
  slug: open-transunion-trucontact-3gpp-call-authentication
- collection_type: open
  name: STIR/SHAKEN Authentication & Verification Service APIs
  slug: open-transunion-trucontact-tcs-shaken
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transunion-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transunion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/transunion
- group: auth
  title: ''
  type: Authentication
  url: authentication/transunion-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/transunion-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transunion-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transunion-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/transunion-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/transunion-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/transunion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/transunion-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transunion-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/transunion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transunion-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neustar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transunion
- group: company
  title: ''
  type: Website
  url: https://www.transunion.com/
- group: other
  title: ''
  type: Business
  url: https://www.transunion.com/business
- group: company
  title: ''
  type: News
  url: https://newsroom.transunion.com/
- group: company
  title: ''
  type: Investors
  url: https://investors.transunion.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.transunion.com/
- group: company
  title: ''
  type: About
  url: https://www.transunion.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://newsroom.transunion.com/feed/
created: '2026-05-05'
description: A global information and insights company providing credit reporting, risk, fraud, and identity solutions. One of the three largest consumer credit bureaus in the United States, serving businesses and consumers across multiple international markets. Its credit and TruValidate decisioning APIs are contract-gated, but its TruContact Trusted Call Solutions business — acquired with Neustar in December 2021 — publishes an open, MIT-licensed OpenAPI for the STIR/SHAKEN call authentication and verification service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transunion.png
layout: provider
modified: '2026-08-13'
name: TransUnion
nav: Providers
network: true
overview: 'TransUnion publishes 1 API on the [APIs.io](https://apis.io/) network: TruContact Trusted Call Solutions (STI-AS / STI-VS). Tagged areas include Financial, Credit Reporting, Risk, Identity, and Fraud.


  TransUnion''s developer surface includes authentication, product news, engineering blog, and 21 more developer resources.'
plans:
- name: Transunion Plans Pricing
  plan_count: 0
  slug: transunion-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 0
  name: Transunion Rate Limits
  slug: transunion-rate-limits
score:
  band: thin
  composite: 29.0
  delta: -1.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 52.4
    developer_ergonomics: 23.2
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 13.2
  previous_composite: 30.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transunion/refs/heads/main/screenshots/transunion-2026-06-20T195631.png
security:
- kind: authentication
  name: Transunion Authentication
  slug: transunion-authentication
  summary_line: apiKey/ip-allowlist/mutualTLS · 3 schemes
- kind: domain-security
  name: Transunion Domain Security
  slug: transunion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Transunion Vulnerability Disclosure
  slug: transunion-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: transunion
tags:
- Financial
- Credit Reporting
- Risk
- Identity
- Fraud
- Marketing
- Telecommunications
- Call Authentication
- STIR/SHAKEN
website: https://www.transunion.com/
---
