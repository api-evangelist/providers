---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cigna Agentic Access
  operation_count: 22
  slug: cigna-agentic-access
  summary_line: 22 operations
api_count: 15
apis:
- description: The Bulk Data API from Cigna — 1 operation(s) for bulk data.
  name: Cigna Bulk Data API
  slug: cigna-bulk-data-api
- description: The Condition API from Cigna — 1 operation(s) for condition.
  name: Cigna Condition API
  slug: cigna-condition-api
- description: The Coverage API from Cigna — 1 operation(s) for coverage.
  name: Cigna Coverage API
  slug: cigna-coverage-api
- description: The Encounter API from Cigna — 1 operation(s) for encounter.
  name: Cigna Encounter API
  slug: cigna-encounter-api
- description: The ExplanationOfBenefit API from Cigna — 1 operation(s) for explanationofbenefit.
  name: Cigna ExplanationOfBenefit API
  slug: cigna-explanationofbenefit-api
- description: The HealthcareService API from Cigna — 1 operation(s) for healthcareservice.
  name: Cigna HealthcareService API
  slug: cigna-healthcareservice-api
- description: The InsurancePlan API from Cigna — 2 operation(s) for insuranceplan.
  name: Cigna InsurancePlan API
  slug: cigna-insuranceplan-api
- description: The Location API from Cigna — 1 operation(s) for location.
  name: Cigna Location API
  slug: cigna-location-api
- description: The MedicationKnowledge API from Cigna — 1 operation(s) for medicationknowledge.
  name: Cigna MedicationKnowledge API
  slug: cigna-medicationknowledge-api
- description: The MedicationRequest API from Cigna — 1 operation(s) for medicationrequest.
  name: Cigna MedicationRequest API
  slug: cigna-medicationrequest-api
- description: The Observation API from Cigna — 1 operation(s) for observation.
  name: Cigna Observation API
  slug: cigna-observation-api
- description: The Organization API from Cigna — 1 operation(s) for organization.
  name: Cigna Organization API
  slug: cigna-organization-api
- description: The Patient API from Cigna — 4 operation(s) for patient.
  name: Cigna Patient API
  slug: cigna-patient-api
- description: The Practitioner API from Cigna — 2 operation(s) for practitioner.
  name: Cigna Practitioner API
  slug: cigna-practitioner-api
- description: The PractitionerRole API from Cigna — 1 operation(s) for practitionerrole.
  name: Cigna PractitionerRole API
  slug: cigna-practitionerrole-api
artifact_total: 32
collections:
- collection_type: open
  name: Cigna Drug Formulary API
  slug: open-cigna-drug-formulary-api
- collection_type: open
  name: Cigna Patient Access API
  slug: open-cigna-patient-access-api
- collection_type: open
  name: Cigna Provider Access API
  slug: open-cigna-provider-access-api
- collection_type: open
  name: Cigna Provider Directory API
  slug: open-cigna-provider-directory-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cigna-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cigna-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cigna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cigna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cigna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cigna-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cigna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-cigna-group
- group: company
  title: ''
  type: Website
  url: https://www.cigna.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cigna.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.cigna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cigna.com/docs/service-apis
- group: operate
  title: ''
  type: Support
  url: https://developer.cigna.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cigna.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cigna.com/legal/privacy
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cigna-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cigna-patient-schema.json
- group: design
  title: ''
  type: Spectral
  url: spectral/cigna-spectral.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.cigna.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsroom.cigna.com/
created: '2025-02-21'
description: Cigna Healthcare is a leading global health services company offering medical, dental, behavioral, and pharmacy plans for individuals, families, and employers. The Cigna Developer Portal exposes CMS-mandated FHIR APIs for Patient Access, Provider Directory, Drug Formulary, and Provider Access, along with member and provider service APIs that enable third-party applications, electronic health record systems, and partners to access member health data with consent and look up Cigna network providers and formulary information.
finops:
- name: Cigna Finops
  service_category: Healthcare / Health Insurance
  slug: cigna-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for Cigna Healthcare, one of the largest global health services companies. Cigna's Developer Portal exposes CMS-mandated FHIR APIs for Patient Acces
  name: Cigna GraphQL Schema
  slug: cigna-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cigna.png
json_schemas:
- name: CignaPatient
  property_count: 10
  slug: cigna-patient
jsonld:
- class_count: 0
  name: Cigna Context
  property_count: 8
  slug: cigna-context
layout: provider
modified: '2026-05-19'
name: Cigna
nav: Providers
network: true
overview: 'Cigna publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Bulk Data API, Condition API, Coverage API, and 12 more. Tagged areas include CMS Interoperability, Da Vinci, Drug Formulary, FHIR, and Health Insurance.


  The Cigna catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cigna''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 15 more developer resources.'
plans:
- name: Cigna Plans Pricing
  plan_count: 3
  slug: cigna-plans-pricing
press:
- date: '2026-05-25'
  title: Cigna launches new generative AI assistant for members
  url: https://www.healthcaredive.com/news/cigna-launches-generative-ai-member-assistant/750480/
- date: '2026-05-25'
  title: Cigna Healthcare Unveils Industry-Leading AI-Powered ...
  url: https://www.prnewswire.com/news-releases/cigna-healthcare-unveils-industry-leading-ai-powered-digital-tools-for-a-simple-and-reliable-customer-experience-302479742.html
- date: '2026-05-25'
  title: Press Releases | Cigna Healthcare Newsroom
  url: https://newsroom.cigna.com/cigna-healthcare-unveils-industry-leading-ai-powered-digital-tools
- date: '2026-05-25'
  title: The Cigna Group's approach to ethical AI practices
  url: https://newsroom.thecignagroup.com/the-cigna-group-approach-to-ethical-ai-practices
- date: '2026-05-25'
  title: Cigna Uses Data and AI to Improve Patient Outcomes
  url: https://newsroom.cigna.com/how-cigna-uses-data-and-ai-to-improve-patient-outcomes
- date: '2020-11-23'
  title: Cigna Affordable Care Act Health Plans to Expand into 63 New Counties Across North Carolina for 2021
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-affordable-care-act-health-plans-to-expand-into-63-new-counties-across-north-carolina-for-2021.html
- date: '2020-11-18'
  title: Cigna Leads Industry in 2020 Dow Jones Sustainability Indices
  url: https://www.cigna.com/newsroom/news-releases/2020/cigna-leads-industry-in-2020-dow-jones-sustainability-indices.html
- date: '2020-11-17'
  title: Veterans Recovery Resources of Mobile Receives $100,000 Cigna Foundation Grant to Provide Mental Health Services to Area Veterans
  url: https://www.cigna.com/newsroom/news-releases/2020/veterans-recovery-resources-of-mobile-receives-100000-cigna-foundation-grant-to-provide-mental-health-services-to-area-veterans.html
random_paper: 38
rate_limits:
- limit_count: 2
  name: Cigna Rate Limits
  slug: cigna-rate-limits
rules:
- name: Cigna API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cigna-jsonschema-spectral-rules
scopes:
- name: Cigna Scopes
  scope_count: 6
  slug: cigna-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 62.0
  delta: 2.8
  facets:
    commercial_clarity: 68.4
    contract_quality: 49.6
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 59.2
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 100.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cigna/refs/heads/main/screenshots/cigna-2026-06-20T174340.png
security:
- kind: authentication
  name: Cigna Authentication
  slug: cigna-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cigna Domain Security
  slug: cigna-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cigna Vulnerability Disclosure
  slug: cigna-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cigna Trust Center
  slug: cigna-trust-center
  summary_line: SOC 2, HIPAA
slug: cigna
tags:
- CMS Interoperability
- Da Vinci
- Drug Formulary
- FHIR
- Health Insurance
- Healthcare
- Patient Access
- Provider Directory
- SMART on FHIR
- Fortune 100
website: https://www.cigna.com/
---
