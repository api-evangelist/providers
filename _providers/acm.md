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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: The ACM Digital Library search endpoint allows programmatic querying of computing literature across ACM's full publication corpus. Queries are issued against the doSearch action endpoint with paramete
  name: ACM Digital Library Search API
  slug: acm-search-api
- description: Individual publications, conference papers, and journal articles in the ACM Digital Library are accessible via persistent DOI-based URLs at dl.acm.org/doi/{doi}. ACM maintains DOI registration through
  name: ACM Digital Library Content Retrieval API
  slug: acm-content-retrieval-api
- description: The ACM Digital Library provides citation export functionality supporting BibTeX, EndNote, and ACM Reference format downloads for individual articles and bulk search result sets. Users can export indi
  name: ACM Digital Library Citation Export API
  slug: acm-citation-export-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dl.acm.org/
- group: docs
  title: ''
  type: Documentation
  url: https://libraries.acm.org/digital-library/platform-and-features
- group: auth
  title: ''
  type: Authentication
  url: https://libraries.acm.org/subscriptions-access/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://libraries.acm.org/subscriptions-access
- group: commercial
  title: ''
  type: CorporatePricing
  url: https://libraries.acm.org/subscriptions-access/corporate-pricing
- group: commercial
  title: ''
  type: GovernmentPricing
  url: https://libraries.acm.org/subscriptions-access/government/dl-pricing
- group: commercial
  title: ''
  type: AcademicPricing
  url: https://libraries.acm.org/subscriptions-access/academic/dl-pricing
- group: other
  title: ''
  type: OpenAccess
  url: https://dl.acm.org/openaccess
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acm.org/publications/policies/copyright-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acm.org/about-acm/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://cacm.acm.org/
- group: learn
  title: ''
  type: TrainingResources
  url: https://libraries.acm.org/training-resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/association-for-computing-machinery
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TheOfficialACM
- group: operate
  title: ''
  type: Support
  url: https://dl.acm.org/contact
created: '2026-06-13'
description: The ACM Digital Library is the world's most comprehensive collection of full-text articles and bibliographic literature covering computing and information technology. Published by the Association for Computing Machinery (ACM), it provides access to journals, conference proceedings, magazines, newsletters, and technical reports spanning the complete history of ACM publications. As of January 2026, the ACM Digital Library is fully open access, offering free basic access to its entire corpus of computing research. Programmatic access is available through web-based search endpoints, DOI-based content retrieval, citation export (BibTeX, EndNoteL, ACM Ref), and Premium tier bulk download and research analytics capabilities. The library also provides the ACM Guide to Computing Literature, a comprehensive bibliographic database extending beyond ACM publications to cover the broader computing literature.
finops:
- name: Acm Finops
  service_category: API
  slug: acm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acm.png
layout: provider
modified: '2026-06-13'
name: ACM Digital Library
nav: Providers
network: true
overview: 'ACM Digital Library publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Academic, Bibliographic Records, Citations, Computing, and Conference Proceedings.


  ACM Digital Library''s developer surface includes documentation, authentication, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Acm Plans Pricing
  plan_count: 2
  slug: acm-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 3
  name: Acm Rate Limits
  slug: acm-rate-limits
score:
  band: thin
  composite: 28.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 28.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acm/refs/heads/main/screenshots/acm-2026-06-20T171406.png
security:
- kind: domain-security
  name: Acm Domain Security
  slug: acm-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Acm Vulnerability Disclosure
  slug: acm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: acm
tags:
- Academic
- Bibliographic Records
- Citations
- Computing
- Conference Proceedings
- DOI
- Digital Library
- Journals
- Metadata
- Open Access
- Publications
- Research
- Scholarly
website: https://dl.acm.org/
---
