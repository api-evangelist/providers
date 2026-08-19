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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: FHIR R4 compliant Patient Access API providing members secure access to their health data including claims, clinical data, and coverage information. Required under CMS Interoperability and Patient Acc
  name: Aetna Patient Access FHIR API
  slug: aetna-patient-access-fhir-api
- description: FHIR R4 compliant Provider Directory API providing standardized access to in-network provider and facility information. Enables third-party applications to search for providers, verify network partici
  name: Aetna Provider Directory FHIR API
  slug: aetna-provider-directory-fhir-api
- description: FHIR R4 compliant Drug Formulary API providing standardized access to plan formulary data including covered drugs, tiers, cost-sharing requirements, and prior authorization requirements. Implements th
  name: Aetna Drug Formulary FHIR API
  slug: aetna-drug-formulary-fhir-api
- description: 'Electronic Data Interchange connectivity for healthcare providers enabling electronic submission of claims, eligibility verification, claim status inquiries, and remittance advice. Accessible through '
  name: Aetna Provider EDI API
  slug: aetna-provider-edi-api
artifact_total: 27
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aetna-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetnahealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aetna
- group: company
  title: ''
  type: Website
  url: https://www.aetna.com
- group: start
  title: ''
  type: Portal
  url: https://www.aetna.com/health-care-professionals.html
- group: start
  title: ''
  type: Login
  url: https://member.aetna.com
- group: operate
  title: ''
  type: Support
  url: https://www.aetna.com/individuals-families/contact-aetna.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aetna.com/legal-notices/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aetna.com/legal-notices/terms-of-use.html
description: Aetna, a CVS Health company, offers health insurance, dental, vision, and other plans for individuals, families, employers, health care providers, and insurance agents and brokers. As a major U.S. health insurer, Aetna provides federally mandated FHIR R4 APIs for patient access, provider directory, and drug formulary data under CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Provider connectivity is supported through the Availity portal for EDI transactions.
features:
- description: All patient-facing APIs implement HL7 FHIR Release 4 standard for interoperability.
  name: FHIR R4 Compliance
- description: Secure OAuth 2.0 authorization framework for patient-authorized third-party app access.
  name: SMART on FHIR Authorization
- description: Full compliance with CMS-9115-F Interoperability and Patient Access Final Rule.
  name: CMS Interoperability Compliance
- description: Complete HIPAA-compliant EDI transaction set for provider administrative workflows.
  name: EDI Transaction Support
- description: Supports member-directed payer-to-payer data exchange for continuity of care.
  name: Payer-to-Payer Data Exchange
- description: Implements HL7 DaVinci Project PDEX, PDex Drug Formulary, and Plan Net guides.
  name: DaVinci Implementation Guides
finops:
- name: Aetna Finops
  service_category: API
  slug: aetna-finops
graphqls:
- description: Aetna, a CVS Health company, is a major U.S. health insurer offering health insurance, dental, vision, pharmacy, and wellness plans for individuals, families, employers, healthcare providers, and brok
  name: Aetna GraphQL Schema
  slug: aetna-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aetna.png
integrations:
- description: Integrated pharmacy benefit management for prescription drug coverage and mail-order pharmacy.
  name: CVS Caremark
- description: Primary provider portal for EDI transactions, eligibility, claims, and authorization requests.
  name: Availity
- description: EHR integration enabling clinical workflows including prior authorization and care management.
  name: Epic Payer Platform
- description: FHIR-based integration enabling Aetna members to view health data in Apple Health app.
  name: Apple Health
- description: Interoperability network participation for cross-organization health data exchange.
  name: CommonWell Health Alliance
- description: Alignment with CMS Blue Button 2.0 FHIR API patterns for Medicare data access.
  name: CMS Blue Button 2.0
layout: provider
modified: '2026-04-19'
name: Aetna
nav: Providers
network: true
overview: 'Aetna publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Health Insurance, Healthcare, FHIR, Patient Access, and Provider Directory.


  Aetna''s developer surface includes developer portal, support, and 7 more developer resources.'
plans:
- name: Aetna Plans Pricing
  plan_count: 3
  slug: aetna-plans-pricing
press:
- date: '2026-05-25'
  title: Aetna taps into AI with Care Paths tech
  url: https://www.healthcarefinancenews.com/news/aetna-taps-ai-care-paths-tech
- date: '2026-05-25'
  title: Aetna launches leading edge conversational AI navigation
  url: https://www.cvshealth.com/news/innovation/aetna-launches-leading-edge-conversational-ai-navigation.html
- date: '2026-05-25'
  title: Aetna launches conversational AI for health care navigation
  url: https://www.linkedin.com/posts/nathan-frank-3b00807_aetna-cvshealth-aetnatechnology-activity-7396987415451746304-uAKd
- date: '2026-05-25'
  title: Aetna expands initiatives to simplify experiences for health ...
  url: https://www.prnewswire.com/news-releases/aetna-expands-initiatives-to-simplify-experiences-for-health-care-professionals-and-patients-302632202.html
- date: '2026-05-25'
  title: Aetna Launches New AI and Digital Tools to Improve ...
  url: https://www.cvshealth.com/news/innovation/aetna-launches-new-ai-and-digital-tools-to-improve-access-and-care.html
random_paper: 74
rate_limits:
- limit_count: 5
  name: Aetna Rate Limits
  slug: aetna-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: -3.6
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Aetna Domain Security
  slug: aetna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aetna
tags:
- Health Insurance
- Healthcare
- FHIR
- Patient Access
- Provider Directory
- Fortune 100
use_cases:
- description: Members use SMART on FHIR apps to access their complete health records across providers.
  name: Member Health Record Access
- description: Developers build directory search tools to help patients find in-network providers.
  name: Provider Network Verification
- description: Applications use formulary API to compare medication costs across Aetna plans.
  name: Drug Cost Comparison
- description: Healthcare providers submit claims electronically via EDI 837 transactions through Availity.
  name: Electronic Claims Submission
- description: Providers verify member eligibility and benefits in real time using 270/271 EDI transactions.
  name: Eligibility Verification
- description: Providers receive and process electronic remittance advice via EDI 835 transactions.
  name: Remittance Processing
website: https://www.aetna.com
---
