---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Institute Of Standards And Technology Agentic Access
  operation_count: 3
  slug: national-institute-of-standards-and-technology-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Common Platform Enumeration
  name: National Institute of Standards and Technology CPE API
  slug: national-institute-of-standards-and-technology-cpe-api
- description: Common Vulnerabilities and Exposures
  name: National Institute of Standards and Technology CVE API
  slug: national-institute-of-standards-and-technology-cve-api
- description: CVE change history events
  name: National Institute of Standards and Technology CVE History API
  slug: national-institute-of-standards-and-technology-cve-history-api
artifact_total: 10
collections:
- collection_type: open
  name: NIST National Vulnerability Database (NVD) API
  slug: open-national-institute-of-standards-and-technology
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-institute-of-standards-and-technology-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/national-institute-of-standards-and-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-institute-of-standards-and-technology-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usnistgov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nist
- group: company
  title: ''
  type: Website
  url: https://www.nist.gov/
- group: start
  title: ''
  type: Portal
  url: https://nvd.nist.gov/developers
- group: docs
  title: ''
  type: Documentation
  url: https://nvd.nist.gov/developers/vulnerabilities
- group: company
  title: ''
  type: Blog
  url: https://www.nist.gov/news-events/news/rss.xml
created: '2024-12-03'
description: NIST promotes U.S. innovation and industrial competitiveness by advancing measurement science, standards, and technology in ways that enhance economic security and improve our quality of life. NIST operates the National Vulnerability Database (NVD), which provides public APIs for CVE, CVE change history, and CPE records.
finops:
- name: National Institute Of Standards And Technology Finops
  service_category: API
  slug: national-institute-of-standards-and-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-institute-of-standards-and-technology.png
layout: provider
modified: '2026-05-19'
name: National Institute of Standards and Technology
nav: Providers
network: true
overview: 'National Institute of Standards and Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network: CPE API, CVE API, and CVE History API. Tagged areas include Cybersecurity, Federal Government, Standards, Technology, and Vulnerabilities.


  National Institute of Standards and Technology''s developer surface includes developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: National Institute Of Standards And Technology Plans Pricing
  plan_count: 3
  slug: national-institute-of-standards-and-technology-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: National Institute Of Standards And Technology Rate Limits
  slug: national-institute-of-standards-and-technology-rate-limits
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-institute-of-standards-and-technology/refs/heads/main/screenshots/national-institute-of-standards-and-technology-2026-06-20T190029.png
security:
- kind: domain-security
  name: National Institute Of Standards And Technology Domain Security
  slug: national-institute-of-standards-and-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: National Institute Of Standards And Technology Vulnerability Disclosure
  slug: national-institute-of-standards-and-technology-vulnerability-disclosure
  summary_line: disclosure policy published
slug: national-institute-of-standards-and-technology
tags:
- Cybersecurity
- Federal Government
- Standards
- Technology
- Vulnerabilities
website: https://www.nist.gov/
---
