---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Taylor & Francis Content API provides programmatic access to eBook and chapter downloads from the taylorfrancis.com platform. Using DOI-based identifiers, institutional subscribers can retrieve PD
  name: Taylor & Francis Content API
  slug: taylor-francis-content-api
- description: The Taylor & Francis KBART Holdings API enables library management systems to automatically retrieve and synchronise institutional journal and eBook entitlements. Librarians generate a Customer Refere
  name: Taylor & Francis KBART Holdings API
  slug: taylor-francis-kbart-holdings-api
- description: Taylor & Francis Online supports automated harvesting of COUNTER Release 5 usage statistics via the SUSHI protocol. Institutional library administrators can retrieve Title, Database, Platform, and Ite
  name: Taylor & Francis SUSHI / COUNTER 5 API
  slug: taylor-francis-sushi-counter-api
- description: Taylor & Francis provides API-based text and data mining access to subscribed and open-access content for non-commercial research purposes. Institutions notify Taylor & Francis in advance of TDM proje
  name: Taylor & Francis Text and Data Mining API
  slug: taylor-francis-text-data-mining-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taylor-francis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://taylorandfrancis.com/
- group: start
  title: ''
  type: Portal
  url: https://www.tandfonline.com/
- group: other
  title: ''
  type: LibrarianResources
  url: https://librarianresources.taylorandfrancis.com/
- group: auth
  title: ''
  type: Authentication
  url: https://librarianresources.taylorandfrancis.com/services-support/authentication-and-remote-access/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.taylorfrancis.com/how-to-obtain-institutional-token
- group: operate
  title: ''
  type: Support
  url: https://help.tandfonline.com/s/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taylorandfrancis.com/our-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taylorandfrancis.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taylor-&-francis-group
- group: company
  title: ''
  type: Twitter
  url: https://x.com/tandfonline
- group: operate
  title: ''
  type: Contact
  url: https://taylorandfrancis.com/contact/
created: '2026-06-13'
description: Taylor & Francis Group is a British academic publisher offering REST APIs for searching and accessing journal articles, books, metadata, and bibliographic records from over 2,700 Taylor & Francis and Routledge publications. Their API surfaces include content download APIs for books and chapters, KBART holdings automation for library systems, COUNTER 5 SUSHI usage reporting, and text and data mining access for institutional subscribers across humanities, social sciences, science, technology, and medicine.
finops:
- name: Taylor Francis Finops
  service_category: API
  slug: taylor-francis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taylor-francis.png
layout: provider
modified: '2026-06-13'
name: Taylor & Francis
nav: Providers
network: true
overview: 'Taylor & Francis publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Academic, Books, Journals, Metadata, and Publishing.


  Taylor & Francis'' developer surface includes developer portal, authentication, getting-started guide, support, and 8 more developer resources.'
plans:
- name: Taylor Francis Plans Pricing
  plan_count: 3
  slug: taylor-francis-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Taylor Francis Rate Limits
  slug: taylor-francis-rate-limits
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taylor-francis/refs/heads/main/screenshots/taylor-francis-2026-06-20T194941.png
security:
- kind: domain-security
  name: Taylor Francis Domain Security
  slug: taylor-francis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: taylor-francis
tags:
- Academic
- Books
- Journals
- Metadata
- Publishing
- Research
- Text Mining
website: https://taylorandfrancis.com/
---
