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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/echo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.echo.ai/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/echo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.echo.ai/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echo-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.echo.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.echo.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.echohq.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.echo.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.echo.ai/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.echo.ai/
created: '2026-07-17'
description: Echo is a software supply-chain security company that delivers vulnerability-free (CVE-free), secure-by-design base container images, language libraries, hardened virtual machines, serverless runtimes, and OS packages. Its artifacts are built as drop-in replacements so engineering teams eliminate known CVEs across their software supply chain without changing application code, cutting remediation toil and easing compliance with frameworks like FedRAMP, FIPS, PCI DSS, DORA, and the EU Cyber Resilience Act. Echo operates as a CVE Numbering Authority (CNA) and publishes a Trust Center with SOC 2 Type 2, ISO/IEC 27001:2022, and FIPS 140-3 assurance. The company is backed by GGV Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/echo.png
layout: provider
modified: '2026-07-19'
name: Echo
nav: Providers
network: true
overview: 'Echo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Supply Chain Security, Container Security, and Vulnerability Management.


  Echo''s developer surface includes engineering blog, pricing, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/echo/refs/heads/main/screenshots/echo-2026-07-25T212737.png
security:
- kind: domain-security
  name: Echo Domain Security
  slug: echo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Echo Vulnerability Disclosure
  slug: echo-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Echo Trust Center
  slug: echo-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, FIPS 140-3
slug: echo
tags:
- Company
- Security
- Supply Chain Security
- Container Security
- Vulnerability Management
- DevSecOps
- Compliance
- Open-Source
website: https://www.echo.ai/
---
