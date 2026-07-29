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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Administrative Office Of The U S Courts Agentic Access
  operation_count: 4
  slug: administrative-office-of-the-u-s-courts-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 3
apis:
- description: The Cases API from Administrative Office of the U.S. Courts — 1 operation(s) for cases.
  name: Administrative Office of the U.S. Courts Cases API
  slug: administrative-office-of-the-u-s-courts-cases-api
- description: The Parties API from Administrative Office of the U.S. Courts — 1 operation(s) for parties.
  name: Administrative Office of the U.S. Courts Parties API
  slug: administrative-office-of-the-u-s-courts-parties-api
- description: The Services API from Administrative Office of the U.S. Courts — 2 operation(s) for services.
  name: Administrative Office of the U.S. Courts Services API
  slug: administrative-office-of-the-u-s-courts-services-api
artifact_total: 24
collections:
- collection_type: open
  name: Administrative Office of the U.S. Courts PACER Authentication API
  slug: open-pacer-authentication-api
- collection_type: open
  name: Administrative Office of the U.S. Courts PACER Case Locator API
  slug: open-pacer-case-locator-pcl-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/administrative-office-of-the-u-s-courts-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/administrative-office-of-the-u-s-courts-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uscourts.gov/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/administrative-office-of-the-united-states-courts
- group: company
  title: ''
  type: Website
  url: https://www.uscourts.gov/
- group: start
  title: ''
  type: Portal
  url: https://pacer.uscourts.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pacer.uscourts.gov/file-case/developer-resources
- group: start
  title: ''
  type: Signup
  url: https://pacer.uscourts.gov/register-account
- group: operate
  title: ''
  type: Contact
  url: https://pacer.uscourts.gov/contact-us
created: '2024-11-20'
description: The Administrative Office of the United States Courts is the administrative agency of the United States federal court system, established in 1939. It provides legislative, administrative, legal, financial, management, program, and information technology support services to the federal courts. The agency operates PACER (Public Access to Court Electronic Records), which provides programmatic access to case and docket information from Federal Appellate, District, and Bankruptcy courts via the PACER Authentication API and PACER Case Locator (PCL) REST API. The agency also provides CM/ECF developer resources for building tools that interface with the Case Management and Electronic Case Filing system.
features:
- description: Programmatic search across a nationwide index of all Federal Appellate, District, and Bankruptcy court cases using the PCL REST API, supporting case search and party search with immediate and batch result modes.
  name: Federal Court Case Search
- description: Token-based authentication API enabling automated systems to obtain PACER authentication tokens without requiring a user interface, suitable for integration into automated data pipelines and legal research tools.
  name: Automated PACER Authentication
- description: Technical resources for developers building tools that interface with the Case Management and Electronic Case Filing (CM/ECF) system, including XML tag specifications, NextGen CM/ECF documentation, and release notes for appellate and bankruptcy systems.
  name: CM/ECF Developer Integration
- description: JSON and XML data feeds providing court lookup information for identifying CM/ECF courts and their configurations, available for integration into court filing software.
  name: Court Lookup Data Feeds
- description: Specialized resources for bankruptcy petition preparation software and case trustee management software vendors, including creditor claim filing specifications and official form changes.
  name: Bankruptcy Filing Integration
- description: Commercial users can run large batch data pulls via the PCL API, with recommended off-peak hours (6 p.m. to 6 a.m. Central Time) to minimize system impact.
  name: Bulk Data Access
finops:
- name: Administrative Office Of The U S Courts Finops
  service_category: API
  slug: administrative-office-of-the-u-s-courts-finops
image: /assets/icons/administrative-office-of-the-u-s-courts.png
integrations:
- description: Case Management and Electronic Case Filing system for all federal courts.
  name: CM/ECF System
- description: Nationwide index of federal court cases searchable via REST API.
  name: PACER Case Locator
- description: Next-generation electronic filing system with enhanced developer integration support.
  name: NextGen CM/ECF
layout: provider
modified: '2026-05-19'
name: Administrative Office of the U.S. Courts
nav: Providers
network: true
overview: 'Administrative Office of the U.S. Courts publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cases API, Parties API, and Services API. Tagged areas include Courts, Federal Government, Legal, PACER, and Case Records.


  Administrative Office of the U.S. Courts'' developer surface includes engineering blog, developer portal, signup flow, and 6 more developer resources.'
plans:
- name: Administrative Office Of The U S Courts Plans Pricing
  plan_count: 3
  slug: administrative-office-of-the-u-s-courts-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Administrative Office Of The U S Courts Rate Limits
  slug: administrative-office-of-the-u-s-courts-rate-limits
score:
  band: thin
  composite: 29.0
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/administrative-office-of-the-u-s-courts/refs/heads/main/screenshots/administrative-office-of-the-u-s-courts-2026-06-20T164757.png
security:
- kind: domain-security
  name: Administrative Office Of The U S Courts Domain Security
  slug: administrative-office-of-the-u-s-courts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: administrative-office-of-the-u-s-courts
tags:
- Courts
- Federal Government
- Legal
- PACER
- Case Records
- Judiciary
- Open Data
use_cases:
- description: Law firms and legal research platforms can use the PCL API to programmatically search federal court case indexes and retrieve case and party information for automated legal research workflows.
  name: Legal Research Automation
- description: Corporate legal departments can monitor federal court filings involving specific parties, cases, or subject matters using automated PCL API queries.
  name: Litigation Monitoring
- description: Bankruptcy petition preparation software and trustee management applications can integrate with CM/ECF and PACER APIs to file documents, retrieve case data, and manage creditor information.
  name: Bankruptcy Software Integration
- description: Academic researchers and legal analytics firms can build datasets of federal court case activity using batch PCL API searches across federal court jurisdictions.
  name: Court Data Analytics
- description: Legal technology companies can build PACER-integrated products for case tracking, docket monitoring, and court record retrieval using the PACER Authentication and PCL APIs.
  name: Legal Technology Development
website: https://www.uscourts.gov/
---
