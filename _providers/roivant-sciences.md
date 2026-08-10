---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Roivant Sciences Agentic Access
  operation_count: 15
  slug: roivant-sciences-agentic-access
  summary_line: 15 operations
api_count: 16
apis:
- description: 'Datavant''s privacy-preserving tokenization technology lets organizations link patient records across datasets without exchanging personally identifiable information. It is delivered as a downloadable '
  name: Datavant Tokenization (Datavant Connect)
  slug: datavant-tokenization
- description: Lokavant is Roivant's clinical-trial intelligence operating unit. Its platform ingests data via 21+ source connectors and a proprietary repository of 2,000+ harmonized prior trials plus 14,000+ third-
  name: Lokavant Clinical Trial Intelligence Platform
  slug: lokavant-clinical-trial-intelligence
- description: Datavant Connect is the customer-facing portal that brokers access to Datavant's linkage, privacy, and retrieval solutions. Access is invite-only and requires portal-administrator credentials; the por
  name: Datavant Connect Customer Portal
  slug: datavant-connect-portal
- description: Recorded patient allergies.
  name: Roivant Sciences Allergies API
  slug: roivant-sciences-allergies-api
- description: Appointment and scheduling data.
  name: Roivant Sciences Appointments API
  slug: roivant-sciences-appointments-api
- description: Clinical diagnoses and problem list.
  name: Roivant Sciences Diagnoses API
  slug: roivant-sciences-diagnoses-api
- description: Unstructured clinical notes and document extraction.
  name: Roivant Sciences Documents API
  slug: roivant-sciences-documents-api
- description: Clinical encounters and visits.
  name: Roivant Sciences Encounters API
  slug: roivant-sciences-encounters-api
- description: Immunization history.
  name: Roivant Sciences Immunizations API
  slug: roivant-sciences-immunizations-api
- description: Laboratory orders and results.
  name: Roivant Sciences Labs API
  slug: roivant-sciences-labs-api
- description: Prescribed and administered medications.
  name: Roivant Sciences Medications API
  slug: roivant-sciences-medications-api
- description: Patient demographics and identifiers.
  name: Roivant Sciences Patients API
  slug: roivant-sciences-patients-api
- description: Connected EHR practice metadata.
  name: Roivant Sciences Practices API
  slug: roivant-sciences-practices-api
- description: Procedures performed.
  name: Roivant Sciences Procedures API
  slug: roivant-sciences-procedures-api
- description: Provider directory and identifiers.
  name: Roivant Sciences Providers API
  slug: roivant-sciences-providers-api
- description: Vital signs measurements.
  name: Roivant Sciences Vitals API
  slug: roivant-sciences-vitals-api
artifact_total: 34
collections:
- collection_type: open
  name: Datavant Healthjump EHR Integration API
  slug: open-datavant-healthjump-ehr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roivant-sciences-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roivant-sciences-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roivant-sciences-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/roivant-sciences-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://roivant.com
- group: docs
  title: ''
  type: Documentation
  url: https://roivant.com/companies
- group: company
  title: ''
  type: Blog
  url: https://roivant.com/news/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.roivant.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datavant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roivant-sciences
- group: commercial
  title: ''
  type: TermsOfService
  url: https://roivant.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roivant.com/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/roivant-sciences-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/roivant-sciences-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/roivant-sciences-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/roivant-sciences-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/roivant-sciences-context.jsonld
created: '2026-05-23'
description: 'Roivant Sciences (Nasdaq: ROIV) is a holding company that builds focused subsidiary biotech and health-tech operating units called "Vants." Founded by Vivek Ramaswamy in 2014 and now led by CEO Matt Gline, Roivant has launched companies across immunology (Immunovant, Priovant, Covant, PsiThera), pulmonology (Pulmovant), delivery technology (Genevant, Proxima), virtual care (Zest Health), and health-data infrastructure (Datavant, Lokavant). Roivant''s most material technology surface is operated by Datavant — the US health-data exchange and tokenization network it co-founded — which connects 80,000+ hospitals and clinics, links data for 100% of US payers, and operates a public EHR data-extraction API under the Healthjump brand. Lokavant operates a customer-only Clinical Trial Intelligence Platform on AWS. The drug-discovery Vants (Immunovant, Priovant, Genevant, etc.) do not expose developer APIs.'
examples:
- key_count: 12
  name: Datavant Healthjump Encounter Example
  slug: datavant-healthjump-encounter-example
- key_count: 23
  name: Datavant Healthjump Patient Example
  slug: datavant-healthjump-patient-example
- key_count: 16
  name: Datavant Healthjump Vitals Example
  slug: datavant-healthjump-vitals-example
finops:
- name: Roivant Sciences Finops
  service_category: ''
  slug: roivant-sciences-finops
image: https://roivant.com/favicon.ico
json_schemas:
- name: Datavant Healthjump Encounter
  property_count: 12
  slug: datavant-healthjump-encounter
- name: Datavant Healthjump Patient
  property_count: 23
  slug: datavant-healthjump-patient
- name: Datavant Healthjump Vitals
  property_count: 16
  slug: datavant-healthjump-vitals
json_structures:
- name: Datavant Healthjump Structure
  property_count: 11
  slug: datavant-healthjump-structure
jsonld:
- class_count: 45
  name: Roivant Sciences Context
  property_count: 9
  slug: roivant-sciences-context
layout: provider
modified: '2026-05-23'
name: Roivant Sciences
nav: Providers
network: true
overview: 'Roivant Sciences publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Allergies API, Appointments API, Diagnoses API, and 10 more. Tagged areas include Biotech, Pharmaceutical, Drug Development, Clinical Trials, and Health Data.


  The Roivant Sciences catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Roivant Sciences'' developer surface includes authentication, developer portal, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Roivant Sciences Plans Pricing
  plan_count: 3
  slug: roivant-sciences-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 0
  name: Roivant Sciences Rate Limits
  slug: roivant-sciences-rate-limits
rules:
- name: Roivant Sciences API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: datavant-healthjump-rules
- name: Roivant Sciences API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: roivant-sciences-jsonschema-spectral-rules
scopes:
- name: Roivant Sciences Scopes
  scope_count: 3
  slug: roivant-sciences-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 31.3
    operational_transparency: 5.3
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roivant-sciences/refs/heads/main/screenshots/roivant-sciences-2026-06-20T193202.png
security:
- kind: authentication
  name: Roivant Sciences Authentication
  slug: roivant-sciences-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Roivant Sciences Domain Security
  slug: roivant-sciences-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: roivant-sciences
tags:
- Biotech
- Pharmaceutical
- Drug Development
- Clinical Trials
- Health Data
- Tokenization
- Electronic Health Records
- Real World Evidence
- Holding Company
- Healthcare
website: https://roivant.com
---
