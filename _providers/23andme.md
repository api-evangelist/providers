---
access_model:
  confidence: medium
  label: Partner Only
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.23andme.org/partners/marketplace/
  - https://api.23andme.com/dev/
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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.23andme.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/23andMe
- group: company
  title: ''
  type: Blog
  url: https://www.23andme.org/blog/
- group: operate
  title: ''
  type: Support
  url: https://customercare.23andme.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.23andme.org/shop/compare-dna-tests/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.23andme.org/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.23andme.org/legal/terms-of-service/
- group: auth
  title: ''
  type: TrustCenter
  url: security/23andme-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.23andme.org/trust-center/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/23andme-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/23andme_bbp?type=team
- group: auth
  title: ''
  type: DomainSecurity
  url: security/23andme-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/23andme-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/23andme-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/23andme-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/23andme-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/23andme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/23andme-rate-limits.yml
created: '2026-07-17'
description: 23andMe is a consumer genetics company founded in 2006 that sells saliva-based DNA test kits and returns ancestry composition across 4,500+ regions, DNA relative matching, FDA-cleared genetic health predisposition and carrier-status reports, pharmacogenetics, polygenic risk scores, wellness and trait insights, plus a Total Health tier adding exome sequencing, biannual blood testing and genetics-informed telehealth. It is now operated by the 23andMe Research Institute, a non-profit, following the company's 2025 Chapter 11 bankruptcy; the canonical consumer domain migrated from 23andme.com to 23andme.org, which serves the company's llms.txt, trust center and shop. 23andMe published a scope-gated OAuth 2.0 Personal Genome API at api.23andme.com but closed general third-party developer access in September 2018. It still markets API and raw-data integration through the 23andMe Marketplace as a partner arrangement, though no machine-readable contract, API reference, pricing or rate
  limits are published publicly, and the developer portal host answers a Cloudflare bot challenge to anonymous requests.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/23andme.png
layout: provider
modified: '2026-08-15'
name: 23andMe
nav: Providers
network: true
overview: '23andMe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Genetics, Genomics, and DNA Testing.


  23andMe''s developer surface includes engineering blog, support, pricing, and 15 more developer resources.'
plans:
- name: 23Andme Plans Pricing
  plan_count: 4
  slug: 23andme-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: 23Andme Rate Limits
  slug: 23andme-rate-limits
score:
  band: thin
  composite: 29.7
  delta: 1.7
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 28.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: 23Andme Domain Security
  slug: 23andme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 23Andme Vulnerability Disclosure
  slug: 23andme-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: 23Andme Trust Center
  slug: 23andme-trust-center
  summary_line: HIPAA Compliance, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 27018, Genetic Information Nondiscrimination Act (GINA), General Data Protection Regulation (GDPR), State Consumer Privacy & Health Privacy Laws (U.S.), FDA Authorization, Common Rule
slug: 23andme
tags:
- Company
- Healthtech
- Genetics
- Genomics
- DNA Testing
- Ancestry
- Consumer Health
- Bioinformatics
- Precision Medicine
- Pharmacogenomics
- Telehealth
- Health Research
website: https://www.23andme.org/
---
