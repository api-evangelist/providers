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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Anthem Patient Access API provides members access to their personal health data via HL7 FHIR R4, as required by the CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Members can aut
  name: Anthem Patient Access API
  slug: anthem-patient-access-api
- description: The Anthem Provider Directory API provides public access to provider directory information via HL7 FHIR R4, as required by CMS interoperability rules. Supports searching for in-network providers, faci
  name: Anthem Provider Directory API
  slug: anthem-provider-directory-api
- description: 'The Anthem Drug Formulary API provides access to prescription drug formulary data via HL7 FHIR R4, including covered medications, cost tiers, prior authorization requirements, and quantity limits for '
  name: Anthem Drug Formulary API
  slug: anthem-drug-formulary-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anthem-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antheminc
- group: start
  title: ''
  type: Portal
  url: https://www.anthem.com
- group: start
  title: ''
  type: Signup
  url: https://www.anthem.com/developer/register/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthem.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthem.com/legal/privacy-policy/
created: '2026-03-23'
description: Anthem, Inc. (now operating as Elevance Health) is one of the largest health benefits companies in the United States, serving members through affiliated Blue Cross and Blue Shield health plans across multiple states including California, New York, Virginia, Georgia, and others. Anthem provides health insurance, pharmacy benefits, and behavioral health services to over 40 million members. Under CMS interoperability rules (CMS-9115-F), Anthem offers FHIR- based Patient Access and Provider Directory APIs.
features:
- description: All Anthem interoperability APIs implement HL7 FHIR Release 4 standards with USCDI-conformant resource profiles.
  name: FHIR R4 Compliance
- description: Patient Access APIs use SMART on FHIR for secure OAuth2-based authorization allowing members to grant third-party app access.
  name: SMART on FHIR Authorization
- description: Members can access their claims history, clinical notes, lab results, immunizations, and medication history through the Patient Access API.
  name: Claims and Clinical Data
- description: Search for in-network providers by specialty, location, name, and plan type through the public Provider Directory API.
  name: Provider Directory Search
finops:
- name: Anthem Finops
  service_category: Healthcare / FHIR Interoperability
  slug: anthem-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anthem.png
integrations:
- description: Anthem participates in the CommonWell Health Alliance for cross-organizational clinical data exchange.
  name: CommonWell Health Alliance
- description: Anthem participates in the Carequality interoperability framework for health data exchange between networks.
  name: Carequality Framework
layout: provider
modified: '2026-04-19'
name: Anthem
nav: Providers
network: true
overview: 'Anthem publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blue Cross Blue Shield, FHIR, Health Benefits, Health Insurance, and Healthcare.


  Anthem''s developer surface includes developer portal, signup flow, and 4 more developer resources.'
plans:
- name: Anthem Plans Pricing
  plan_count: 1
  slug: anthem-plans-pricing
press:
- date: '2026-05-25'
  title: 'Subject: Uncategorized'
  url: https://blog.anthempress.com/?subject=uncategorized
- date: '2026-05-25'
  title: Anthem Link & AI In Healthcare
  url: https://www.anthembluecross.com/employer/the-benefits-guide/the-future-of-healthcare-is-digital
- date: '2026-05-25'
  title: Anthem, Inc. Leads Collaboration to Develop Tools to Help ...
  url: https://www.elevancehealth.com/newsroom/anthem-inc-leads-collaboration-to-develop-tools-to-help-public-officials-and-businesses-make-informed-decisions-related-to-covid-19
- date: '2026-05-25'
  title: AI and Ada
  url: https://anthempress.com/books/ai-and-ada-pb
- date: '2026-05-25'
  title: doc.ai Partners with Anthem to Introduce Groundbreaking ...
  url: https://www.prnewswire.com/news-releases/docai-partners-with-anthem-to-introduce-groundbreaking-end-to-end-data-trial-powered-by-artificial-intelligence-on-the-blockchain-300689910.html
random_paper: 63
rate_limits:
- limit_count: 2
  name: Anthem Rate Limits
  slug: anthem-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anthem/refs/heads/main/screenshots/anthem-2026-06-20T172028.png
security:
- kind: domain-security
  name: Anthem Domain Security
  slug: anthem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anthem
tags:
- Blue Cross Blue Shield
- FHIR
- Health Benefits
- Health Insurance
- Healthcare
- Interoperability
- Fortune 100
use_cases:
- description: Enable member-authorized third-party health apps to aggregate claims, clinical, and formulary data from Anthem plans.
  name: Member Health Apps
- description: Allow care coordinators and providers to access member health history with member authorization for improved care transitions.
  name: Care Coordination
- description: Enable applications to search Anthem's provider directory for in-network physicians, hospitals, and specialists.
  name: Provider Lookup
website: https://www.anthem.com
---
