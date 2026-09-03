---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: DS Core is the open cloud platform from Dentsply Sirona that connects dental practices, laboratories, and DSOs through a single web-based experience. The DS Core API enables Practice Management System
  name: DS Core API
  slug: ds-core-api
- description: The DSIO modality API enables third-party imaging software to drive Dentsply Sirona intraoral imaging hardware (sensors and cameras) through a documented protocol. The API and its reference client are
  name: Dentsply Sirona Intraoral Imaging Modality API
  slug: dsio-modality-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dentsply-sirona-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dentsplysirona
- group: company
  title: ''
  type: Website
  url: https://www.dentsply-sirona.com
- group: company
  title: ''
  type: USA Website
  url: https://www.dentsplysirona.com/en-us
- group: other
  title: ''
  type: Open Platform
  url: https://open.dscore.com/
- group: other
  title: ''
  type: DS Core Marketing
  url: https://www.dentsplysirona.com/en-us/discover/discover-by-brand/ds-core.html
- group: start
  title: ''
  type: Connected Dentistry
  url: https://www.dentsplysirona.com/en/lp/connected-dentistry.html
- group: other
  title: ''
  type: Connect Software
  url: https://www.dentsplysirona.com/en-us/discover/discover-by-brand/connect-software.html
- group: start
  title: ''
  type: Service Portal
  url: https://service.dscore.com/
- group: build
  title: ''
  type: GitHub Imaging
  url: https://github.com/dsimaging
- group: company
  title: ''
  type: Investors
  url: https://investor.dentsplysirona.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.dentsplysirona.com/en/about-dentsply-sirona/news.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.dentsplysirona.com/en/about-dentsply-sirona/sustainability.html
- group: company
  title: ''
  type: Careers
  url: https://www.dentsplysirona.com/en/about-dentsply-sirona/careers.html
- group: operate
  title: ''
  type: Contact
  url: https://www.dentsplysirona.com/en/about-dentsply-sirona/contact-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dentsplysirona.com/en/legal-notice.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dentsplysirona.com/en/legal-notice/privacy-policy.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dentsply-sirona-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dentsply-sirona-vocabulary.yml
created: '2026-03-24'
description: Dentsply Sirona is the world's largest manufacturer of professional dental products and technologies, providing comprehensive solutions for dentists, dental laboratories, and dental specialists worldwide. The company exposes developer integrations through DS Core, an open cloud platform, and through the Dentsply Sirona Imaging modality API for intraoral imaging hardware.
finops:
- name: Dentsply Sirona Finops
  service_category: Dental Technology / Practice Management
  slug: dentsply-sirona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dentsply-sirona.png
jsonld:
- class_count: 0
  name: Dentsply Sirona Context
  property_count: 6
  slug: dentsply-sirona-context
layout: provider
modified: '2026-04-28'
name: Dentsply Sirona
nav: Providers
network: true
overview: 'Dentsply Sirona publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CAD/CAM, CEREC, Dental, DS Core, and Imaging.


  The Dentsply Sirona catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Dentsply Sirona Plans Pricing
  plan_count: 1
  slug: dentsply-sirona-plans-pricing
press:
- date: '2026-05-25'
  title: 'Dentsply Sirona: Digital Transformation in Dentistry - Prophet'
  url: https://prophet.com/case-studies/denstply-sirona-digital-transformation/
- date: '2026-05-25'
  title: ORCA Dental AI & Dentsply Sirona Expanding in Japan
  url: https://cephx.com/orca-dental-ai-and-dentsply-sirona-announce-the-expansion-of-their-integration-partnership-in-japan/
- date: '2026-05-25'
  title: Detect, World's First FDA-Cleared AI-enabled diagnostic ...
  url: https://investor.dentsplysirona.com/news-releases/news-release-details/dentsply-sirona-launches-smart-view-detect-worlds-first-fda
- date: '2026-05-25'
  title: Dentsply Sirona Releases FDA-Cleared Dental AI
  url: https://www.mpo-mag.com/breaking-news/dentsply-sirona-releases-fda-cleared-dental-ai/
- date: '2026-05-25'
  title: Dentsply Sirona presents Primescan® 2 powered by DS ...
  url: https://www.prnewswire.com/news-releases/dentsply-sirona-presents-primescan-2-powered-by-ds-core-the-first-cloud-native-intraoral-scanning-solution-302239312.html
random_paper: 5
rate_limits:
- limit_count: 1
  name: Dentsply Sirona Rate Limits
  slug: dentsply-sirona-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 10
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 15.2
    contract_quality: 6.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 10.5
  previous_composite: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dentsply-sirona/refs/heads/main/screenshots/dentsply-sirona-2026-06-20T175914.png
security:
- kind: domain-security
  name: Dentsply Sirona Domain Security
  slug: dentsply-sirona-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dentsply-sirona
tags:
- CAD/CAM
- CEREC
- Dental
- DS Core
- Imaging
- Intraoral Imaging
- Lab Management
- Practice Management
- Fortune 1000
website: https://www.dentsply-sirona.com
---
