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
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: The Copyright Public Records System (CPRS) provides access to U.S. copyright registration and recordation data with advanced search capabilities and improved interfaces. Replaced the Online Public Cat
  name: Copyright Public Records System
  slug: copyright-public-records
- description: Bulk download of approximately 22 million U.S. copyright registration records from January 1, 1978 to June 27, 2025. Available in raw unparsed MARC, parsed CSV, and tabular CSV formats. Includes regis
  name: Copyright Bulk Datasets
  slug: copyright-bulk-datasets
- description: Searchable directory of licensing documents including compulsory license statements of account, royalty payments, and statutory license records maintained by the Copyright Office.
  name: Licensing Documents Search
  slug: licensing-documents-search
- description: Searchable directory of Online Service Providers (OSPs) that have registered DMCA designated agents with the U.S. Copyright Office per Section 512 of the Digital Millennium Copyright Act.
  name: DMCA Designated Agent Directory
  slug: dmca-designated-agent
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-copyright-office-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.copyright.gov/newsnet/rss.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-copyright-office
- group: company
  title: ''
  type: Website
  url: https://www.copyright.gov/
- group: docs
  title: Search Copyright Records
  type: Documentation
  url: https://www.copyright.gov/public-records/
- group: other
  title: Bulk Data Downloads
  type: DataAPI
  url: https://data.copyright.gov
- group: start
  title: Register Your Work
  type: GettingStarted
  url: https://www.copyright.gov/registration/
- group: operate
  title: Online Registration FAQs
  type: FAQ
  url: https://www.copyright.gov/eco/faq.html
- group: commercial
  title: Website Policies
  type: TermsOfService
  url: https://www.copyright.gov/en/about/policies/
- group: operate
  title: Contact the Copyright Office
  type: Contact
  url: https://www.copyright.gov/about/contact/
- group: design
  title: US Copyright Office Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/vocabulary/us-copyright-office-vocabulary.yml
- group: design
  title: US Copyright Office JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/json-ld/us-copyright-office-context.jsonld
created: '2024-12-03'
description: The US Copyright Office is a government agency responsible for administering and enforcing copyright laws in the United States. The office is responsible for registering and documenting copyright claims, maintaining the public catalog of copyright records, providing bulk data downloads of registration records, and administering licensing programs. The Copyright Office provides open bulk datasets of approximately 22 million registration records and is modernizing its systems through the Enterprise Copyright System (ECS) program.
examples:
- key_count: 10
  name: Us Copyright Office Dmca Agent Example
  slug: us-copyright-office-dmca-agent-example
- key_count: 10
  name: Us Copyright Office Recordation Example
  slug: us-copyright-office-recordation-example
- key_count: 11
  name: Us Copyright Office Registration Example
  slug: us-copyright-office-registration-example
features:
- description: Approximately 22 million copyright registration records from 1978 to present available for bulk download in MARC, parsed CSV, and tabular CSV formats across all copyright work categories.
  name: Copyright Registration Bulk Data
- description: Advanced search system for copyright registration and recordation data, replacing the Online Public Catalog in June 2025.
  name: Copyright Public Records System (CPRS)
- description: Electronic Copyright Office registration system for submitting new copyright registration applications online.
  name: Online Registration (eCO)
- description: Searchable database of compulsory license statements of account and royalty payments filed with the Copyright Office.
  name: Licensing Documents Search
- description: Directory of online service providers that have registered DMCA designated agents per Section 512 of the DMCA.
  name: DMCA Designated Agent Directory
- description: Ongoing modernization of all Copyright Office IT systems into a unified, interconnected digital infrastructure.
  name: Enterprise Copyright System Modernization
finops:
- name: Us Copyright Office Finops
  service_category: API
  slug: us-copyright-office-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-copyright-office.png
integrations:
- description: Copyright Office is a department of the Library of Congress; data integrates with LC catalog systems and MARC format records.
  name: Library of Congress
- description: Collaborates with USPTO on intellectual property policy, including joint AI and copyright/patent studies.
  name: U.S. Patent and Trademark Office
json_schemas:
- name: DMCADesignatedAgent
  property_count: 10
  slug: us-copyright-office-dmca-agent
- name: CopyrightRecordation
  property_count: 10
  slug: us-copyright-office-recordation
- name: CopyrightRegistration
  property_count: 11
  slug: us-copyright-office-registration
json_structures:
- name: Us Copyright Office Dmca Agent Structure
  property_count: 10
  slug: us-copyright-office-dmca-agent-structure
- name: Us Copyright Office Recordation Structure
  property_count: 10
  slug: us-copyright-office-recordation-structure
- name: Us Copyright Office Registration Structure
  property_count: 11
  slug: us-copyright-office-registration-structure
jsonld:
- class_count: 5
  name: Us Copyright Office Context
  property_count: 28
  slug: us-copyright-office-context
layout: provider
modified: '2026-05-03'
name: US Copyright Office
nav: Providers
network: true
overview: 'US Copyright Office publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Copyright, Federal-Government, Intellectual Property, and Open Data.


  The US Copyright Office catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  US Copyright Office''s developer surface includes engineering blog, documentation, getting-started guide, FAQ, and 8 more developer resources.'
plans:
- name: Us Copyright Office Plans Pricing
  plan_count: 3
  slug: us-copyright-office-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Us Copyright Office Rate Limits
  slug: us-copyright-office-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Copyright Office API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-copyright-office-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 68.3
    catalog_earned_first_party: 0.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 28.0
    developer_ergonomics: 23.8
    discoverability: 55.6
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 24.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-copyright-office/refs/heads/main/screenshots/us-copyright-office-2026-06-20T200655.png
security:
- kind: domain-security
  name: Us Copyright Office Domain Security
  slug: us-copyright-office-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-copyright-office
tags:
- Copyright
- Federal-Government
- Intellectual Property
- Open Data
use_cases:
- description: Searching copyright records to determine ownership, registration status, and rights information for works before licensing or use.
  name: Copyright Research and Due Diligence
- description: Downloading bulk copyright registration datasets for academic research, legal analysis, or statistical studies of copyright registration trends.
  name: Bulk Data Analysis and Research
- description: Looking up DMCA designated agents for online service providers to send takedown notices per Section 512 requirements.
  name: DMCA Compliance
- description: Searching licensing documents to verify statutory license compliance and royalty payment records.
  name: Licensing Compliance Verification
- description: Using copyright records to research ownership of works when rights holders cannot be identified or located.
  name: Orphan Works Identification
website: https://www.copyright.gov/
---
