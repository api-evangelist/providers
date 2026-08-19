---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Humana Agentic Access
  operation_count: 12
  slug: humana-agentic-access
  summary_line: 12 operations
api_count: 7
apis:
- description: FHIR R4-compliant API surface for medication-related resources including Medication, MedicationKnowledge, MedicationRequest, drug formulary List resources, and supporting payer data.
  name: Humana FHIR Medication API
  slug: humana-fhir-medication-api
- description: FHIR R4-compliant API surface for insurance coverage data, including Coverage, ExplanationOfBenefits, and InsurancePlan resources used to satisfy CMS Patient Access and Provider Directory rules.
  name: Humana FHIR Coverage and Benefits API
  slug: humana-fhir-coverage-api
- description: FHIR R4-compliant API surface for provider directory information, including Patient, Practitioner, PractitionerRole, Organization, Location, and DocumentReference resources.
  name: Humana FHIR Provider Directory API
  slug: humana-fhir-provider-directory-api
- description: Clinical FHIR resources
  name: Humana Clinical API
  slug: humana-clinical-api
- description: Coverage and insurance FHIR resources
  name: Humana Coverage API
  slug: humana-coverage-api
- description: Patient and provider demographic FHIR resources
  name: Humana Demographic API
  slug: humana-demographic-api
- description: Medication FHIR resources
  name: Humana Medications API
  slug: humana-medications-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Humana FHIR Clinical API
  slug: open-humana-clinical-api
- collection_type: open
  name: Humana FHIR Clinical Coverage API
  slug: open-humana-coverage-api
- collection_type: open
  name: Humana FHIR Clinical Demographic API
  slug: open-humana-demographic-api
- collection_type: open
  name: Humana FHIR Clinical Medications API
  slug: open-humana-medications-api
- collection_type: open
  name: Humana FHIR API
  slug: open-humana
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/humana-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humana
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/humana
- group: start
  title: ''
  type: Portal
  url: https://developers.humana.com/
- group: company
  title: ''
  type: Website
  url: https://www.humana.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.humana.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humana.com/legal/terms-conditions
- group: design
  title: ''
  type: Rules
  url: https://raw.githubusercontent.com/api-evangelist/humana/refs/heads/main/humana-rules.yml
created: '2025-01-07'
description: Humana is a U.S. health insurance company that provides Medicare, Medicaid, and employer-sponsored health insurance plans, along with wellness programs and healthcare services. Humana publishes a suite of FHIR-compliant APIs that give third-party applications access to member health data, coverage information, drug formularies, and provider directories under CMS interoperability rules.
finops:
- name: Humana Finops
  service_category: Healthcare Interoperability
  slug: humana-finops
graphqls:
- description: This conceptual GraphQL schema models the Humana healthcare insurance platform, covering Medicare plans, commercial insurance, provider directories, pharmacy and formulary data, claims, prior authoriz
  name: Humana GraphQL Schema
  slug: humana-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humana.png
layout: provider
modified: '2026-05-19'
name: Humana
nav: Providers
network: true
overview: 'Humana publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Clinical API, Coverage API, Demographic API, and 1 more. Tagged areas include FHIR, Health Insurance, Healthcare, Interoperability, and Medicare.


  Humana''s developer surface includes authentication, developer portal, and 8 more developer resources.'
plans:
- name: Humana Plans Pricing
  plan_count: 4
  slug: humana-plans-pricing
press:
- date: '2026-05-25'
  title: Humana Redefines the Member Experience with Agent ...
  url: https://news.humana.com/news/articles/humana-redefines-the-member-experience-with-agent-assist-built-with-google-cloud
- date: '2026-05-25'
  title: Humana and Google Expand Partnership to Help Reduce ...
  url: https://www.googlecloudpresscorner.com/2024-07-25-Humana-and-Google-Expand-Partnership-to-Help-Reduce-Cost-of-Care-and-Improve-Member-Experiences
- date: '2026-05-25'
  title: Humana deploys AI support tool for call centers
  url: https://www.healthcaredive.com/news/humana-call-center-ai-agent-assist-google-cloud/811200/
- date: '2026-05-25'
  title: October 9, 2025 VIA EMAIL Mr. Jim Rechtin President and ...
  url: https://www.hsgac.senate.gov/wp-content/uploads/2025-10-09-Letter-from-Ranking-Member-Blumenthal-to-Humana.pdf
- date: '2026-05-25'
  title: Humana Redefines the Member Experience with Agent ...
  url: https://www.prnewswire.com/news-releases/humana-redefines-the-member-experience-with-agent-assist-built-with-google-cloud-302677922.html
random_paper: 38
rate_limits:
- limit_count: 4
  name: Humana Rate Limits
  slug: humana-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 1.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 57.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humana/refs/heads/main/screenshots/humana-2026-06-20T182931.png
security:
- kind: authentication
  name: Humana Authentication
  slug: humana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Humana Domain Security
  slug: humana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: humana
tags:
- FHIR
- Health Insurance
- Healthcare
- Interoperability
- Medicare
- Fortune 100
website: https://www.humana.com/
---
