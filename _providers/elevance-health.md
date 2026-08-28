---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elevance Health Agentic Access
  operation_count: 10
  slug: elevance-health-agentic-access
  summary_line: 10 operations
api_count: 9
apis:
- description: The Patient Access API enables Anthem and Elevance Health members to securely access and exchange their medical, pharmacy, dental, and vision claims and clinical data through third-party applications.
  name: Elevance Health Patient Access API
  slug: patient-access
- description: 'The Provider Directory API exposes Elevance Health network provider information including practitioners, practitioner roles, organizations, locations, and insurance plans. The API conforms to the HL7 '
  name: Elevance Health Provider Directory API
  slug: provider-directory
- description: The Formulary API publishes Elevance Health drug coverage information including covered drug lists, tier placement, prior authorization requirements, and step therapy rules. The API conforms to the HL
  name: Elevance Health Formulary API
  slug: formulary
- description: The Payer to Payer API enables Elevance Health to exchange member coverage and clinical data with other health plans when members move between payers, supporting the CMS Interoperability and Prior Aut
  name: Elevance Health Payer to Payer API
  slug: payer-to-payer
- description: The Claims API from Elevance Health — 3 operation(s) for claims.
  name: Elevance Health Claims API
  slug: elevance-health-claims-api
- description: The Conformance API from Elevance Health — 1 operation(s) for conformance.
  name: Elevance Health Conformance API
  slug: elevance-health-conformance-api
- description: The Coverage API from Elevance Health — 2 operation(s) for coverage.
  name: Elevance Health Coverage API
  slug: elevance-health-coverage-api
- description: The Patient API from Elevance Health — 2 operation(s) for patient.
  name: Elevance Health Patient API
  slug: elevance-health-patient-api
- description: The Provider Directory API from Elevance Health — 2 operation(s) for provider directory.
  name: Elevance Health Provider Directory API
  slug: elevance-health-provider-directory-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims API
  slug: open-elevance-health-claims-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Conformance API
  slug: open-elevance-health-conformance-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Coverage API
  slug: open-elevance-health-coverage-api
- collection_type: open
  name: Elevance Health Access FHIR Claims Patient API
  slug: open-elevance-health-patient-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Provider Directory API
  slug: open-elevance-health-provider-directory-api
- collection_type: open
  name: Elevance Health Patient Access FHIR API
  slug: open-elevance-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elevance-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elevance-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elevance-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elevance-health-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elevance-health
- group: company
  title: ''
  type: Website
  url: https://www.elevancehealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.anthem.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://patient360c.anthem.com/P360Member/fhir/documentation
- group: start
  title: ''
  type: Signup
  url: https://www.anthem.com/developers/request-anthem-io
created: '2026-03-21'
description: Elevance Health (formerly Anthem) is a Fortune 500 health benefits company that serves members through Blue Cross and Blue Shield affiliated health plans across multiple states. The company offers medical, pharmacy, dental, vision, and other specialty insurance and exposes a set of CMS Interoperability and Patient Access FHIR APIs to enable members, providers, and partner payers to securely exchange coverage, clinical, claims, provider directory, and formulary data.
finops:
- name: Elevance Health Finops
  service_category: Healthcare Interoperability
  slug: elevance-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elevance-health.png
layout: provider
modified: '2026-04-28'
name: Elevance Health
nav: Providers
network: true
overview: 'Elevance Health publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Conformance API, Coverage API, and 2 more. Tagged areas include Fortune 500, Healthcare, Health Insurance, FHIR, and Interoperability.


  Elevance Health''s developer surface includes authentication, documentation, signup flow, and 6 more developer resources.'
plans:
- name: Elevance Health Plans Pricing
  plan_count: 4
  slug: elevance-health-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Elevance Health Rate Limits
  slug: elevance-health-rate-limits
scopes:
- name: Elevance Health Scopes
  scope_count: 3
  slug: elevance-health-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elevance-health/refs/heads/main/screenshots/elevance-health-2026-06-20T180559.png
security:
- kind: authentication
  name: Elevance Health Authentication
  slug: elevance-health-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Elevance Health Domain Security
  slug: elevance-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elevance-health
tags:
- Fortune 500
- Healthcare
- Health Insurance
- FHIR
- Interoperability
website: https://www.elevancehealth.com
---
