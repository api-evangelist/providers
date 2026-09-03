---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.halborn.com/
- group: company
  title: ''
  type: Blog
  url: https://www.halborn.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.halborn.com/blog/feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HalbornSecurity
- group: operate
  title: ''
  type: Support
  url: https://www.halborn.com/contact
- group: start
  title: ''
  type: Login
  url: https://one.halborn.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.halborn.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halborn.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halborn-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/halborn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/halborn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/halborn-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/halborn-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/halborn-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halborn-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/halborn-packages.yml
coverage:
  checked: '2026-08-22'
  detail: 'Halborn sells blockchain security assessments as professional services and ships no developer product: its 1,020-URL sitemap contains no /developers, /docs or /api section, docs.halborn.com and api.halborn.com do not resolve at all, and the only authenticated surface — Halborn ONE at one.halborn.com — is an invitation-only client portal whose login page says "Contact your local org-owner for an invitation". It does publish a real llms.txt, which lists services, industries, reports and RSS feeds and names no API.'
  evidence:
  - status: 200
    url: https://www.halborn.com/llms.txt
  - status: 404
    url: https://www.halborn.com/openapi.json
  - status: 0
    url: https://docs.halborn.com/
  - status: 404
    url: https://one.halborn.com/openapi.json
  - status: 404
    url: https://www.halborn.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Halborn is a blockchain and digital-asset cybersecurity firm that sells professional security services rather than a developer product. Its assurance practice covers smart contract assessments, Layer 1 protocol reviews, code security audits, web application and cloud infrastructure penetration testing, red team exercises, and custody and key management assessments; its advisory practice covers AI security, blockchain architecture, compliance readiness, risk assessment, technical due diligence and technical training for banks, exchanges, custodians, tokenization platforms, stablecoin issuers, DeFi protocols, central banks and blockchain infrastructure providers. Halborn publishes its engagement results as a public audit repository, discloses zero-day findings under its own CVE assignment scope as a CVE Numbering Authority, and maintains BVSS, the Blockchain Vulnerability Scoring System. As of August 2026 it publishes no public API, no developer portal and no machine-readable
  contract; its Halborn ONE client platform at one.halborn.com is an invitation-only customer portal.
image: https://www.halborn.com/og-image.jpeg
layout: provider
modified: '2026-08-22'
name: Halborn
nav: Providers
network: true
overview: 'Halborn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Blockchain, and Smart Contracts.


  Halborn''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Halborn Plans Pricing
  plan_count: 0
  slug: halborn-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Halborn Rate Limits
  slug: halborn-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 19.7
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Halborn Domain Security
  slug: halborn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Halborn Vulnerability Disclosure
  slug: halborn-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Halborn Trust Center
  slug: halborn-trust-center
  summary_line: SOC 2, SOC 2, ISO/IEC 27001, NIST CSF 2.0
slug: halborn
tags:
- Company
- Security
- Cybersecurity
- Blockchain
- Smart Contracts
- Security Auditing
- Penetration Testing
- Web3
- Vulnerability Disclosure
- Compliance
- Financial-Services
- Professional Services
website: https://www.halborn.com/
---
